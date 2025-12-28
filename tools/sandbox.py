import tempfile
import subprocess
import sys
import os
import re
import time   # ✅ needed for unique filenames with timestamp

# === Persistent directory for plots in Docker ===
# By default, plots were saved inside a TemporaryDirectory (deleted at the end of execution).
# This prevented the frontend from accessing the file via /download_file.
# We now use a persistent folder "uploads/plots" so that Flask can serve the image.
PLOTS_DIR = os.path.join(os.getcwd(), "uploads", "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


def detect_ptrac_mode(ptrac_path):
    """
    Automatically detect the format of a PTRAC file using a 3-level strategy:

    1. HDF5 detection (extension .h5/.hdf5 OR magic bytes)
    2. Fortran binary markers detection (size1 == size2)
    3. ASCII content analysis (ratio + keywords)

    UNIVERSAL: Works with ANY file extension (.ptrac, .p, .ip, .bin, .txt, etc.)
    Only HDF5 uses extension hints - all other formats rely on CONTENT analysis.

    Returns:
      - 'HDF5_PTRAC' if HDF5 format detected
      - 'BIN_PTRAC' if Fortran binary format detected
      - 'ASC_PTRAC' if ASCII text format detected
    """
    try:
        # === Level 1: HDF5 detection (only reliable extension shortcut) ===
        filename_lower = os.path.basename(ptrac_path).lower()

        # HDF5 extension hint (will be confirmed by magic bytes)
        if '.h5' in filename_lower or filename_lower.endswith('.hdf5'):
            return 'HDF5_PTRAC'

        # === Level 2: Magic bytes detection ===
        with open(ptrac_path, "rb") as f:
            header = f.read(512)

        # HDF5 magic signature (8 bytes)
        if len(header) >= 8 and header[:8] == b'\x89HDF\r\n\x1a\n':
            return 'HDF5_PTRAC'

        # === Level 3: Content analysis ===
        # Strategy: Check for Fortran binary markers FIRST (more reliable)
        # Then fall back to ASCII detection

        # Check for Fortran binary record markers
        if len(header) >= 8:
            try:
                # First 4 bytes = record size, should match after record
                size1 = int.from_bytes(header[0:4], byteorder='little')
                if 0 < size1 < 10000:  # Reasonable header size
                    # Check if size2 matches (Fortran record end marker)
                    if len(header) >= 8 + size1:
                        size2 = int.from_bytes(header[4+size1:8+size1], byteorder='little')
                        if size1 == size2:
                            # Valid Fortran binary format detected
                            return 'BIN_PTRAC'
            except:
                pass

        # If no clear binary markers, check for ASCII content
        ascii_count = 0
        for byte in header[:256]:
            # Printable ASCII or whitespace
            if (32 <= byte <= 126) or byte in (9, 10, 13):  # tab, LF, CR
                ascii_count += 1

        ascii_ratio = ascii_count / min(256, len(header))

        # High ASCII ratio (>95%) = ASCII PTRAC
        if ascii_ratio > 0.95:
            return 'ASC_PTRAC'

        # Lower threshold (>85%) + PTRAC keywords = ASCII PTRAC
        if ascii_ratio > 0.85:
            try:
                text_sample = header[:256].decode('ascii', errors='ignore').lower()
                if 'ptrac' in text_sample or 'nps' in text_sample or 'mcnp' in text_sample:
                    return 'ASC_PTRAC'
            except:
                pass

        # Ambiguous case: default to BINARY (safer for Fortran files)
        return 'BIN_PTRAC'

    except Exception as e:
        # Fallback: assume ASCII (safest default for text-based errors)
        return 'ASC_PTRAC'


def patch_ptrac_instantiation(code: str, ptrac_path: str, mode: str) -> str:
    """
    Patch all instances of Ptrac instantiation in the given code.
    Ensures the correct file path and detected mode are always used.
    """
    safe_path = ptrac_path.replace("\\", "\\\\")
    ptrac_line = f"Ptrac(r'{safe_path}', Ptrac.{mode})"

    code_patched = re.sub(
        r"Ptrac\s*\((?:[^)(]+|\((?:[^)(]+|\([^)(]*\))*\))*\)",
        ptrac_line,
        code,
        flags=re.MULTILINE
    )
    code_patched = re.sub(
        r"Ptrac\.(BIN_PTRAC|ASC_PTRAC|HDF5_PTRAC)", f"Ptrac.{mode}", code_patched
    )

    if code != code_patched:
        print(f"[EVA/SANDBOX] Patch : Ptrac instantiations forced to mode {mode}")

    return code_patched


def patch_plots(code: str, allow_plots: bool, output_file="plot.png") -> str:
    """
    Handle matplotlib plotting:
      - Local (allow_plots=True): keep plt.show().
      - Docker (allow_plots=False): use Agg backend and save plots to persistent path.
    """
    if allow_plots:
        patched = re.sub(
            r"plt\.show\s*\([^\)]*\)",
            "import sys; sys.stdout.flush(); sys.stderr.flush(); plt.show()",
            code
        )
        return patched

    # Docker mode → force non-interactive backend
    header = "import matplotlib\nmatplotlib.use('Agg')\n"
    code = header + code

    # Save figure in persistent location
    output_path = os.path.join(PLOTS_DIR, output_file)

    # ✅ sécuriser le chemin pour éviter les \U, \n... (Windows)
    safe_output_path = output_path.replace("\\", "\\\\")

    code = re.sub(
        r"plt\.show\s*\([^\)]*\)",
        f"plt.savefig(r'{safe_output_path}')",
        code
    )
    return code


ACTIVE_PROCESS = None  # Global handle for subprocess management


def run_ptrac_code(code: str, ptrac_path: str, timeout=600, allow_plots=False):
    """
    Execute Python code (generated by OTACON) in a sandboxed environment.
    Steps:
      1. Detect PTRAC file mode (ASCII/Binary).
      2. Patch Ptrac instantiation.
      3. Handle matplotlib plotting (interactive vs headless).
      4. Run code in a subprocess with timeout handling.
      5. Collect results (stdout, stderr, plots).
    """
    global ACTIVE_PROCESS

    mode = detect_ptrac_mode(ptrac_path)
    patched_code = patch_ptrac_instantiation(code, ptrac_path, mode)

    # Use unique filename for each plot (avoid browser caching old images)
    unique_filename = f"plot_{int(time.time()*1000)}.png"
    patched_code = patch_plots(patched_code, allow_plots=allow_plots, output_file=unique_filename)

    with tempfile.TemporaryDirectory() as tmpdir:
        code_file = os.path.join(tmpdir, "llm_code.py")
        with open(code_file, "w", encoding="utf-8") as f:
            f.write(patched_code + "\n")

        try:
            # === Clean old plots to keep only the last 10 ===
            all_plots = sorted(
                [f for f in os.listdir(PLOTS_DIR) if f.startswith("plot_")],
                key=lambda x: os.path.getmtime(os.path.join(PLOTS_DIR, x))
            )
            if len(all_plots) > 10:
                for old_file in all_plots[:-10]:
                    try:
                        os.remove(os.path.join(PLOTS_DIR, old_file))
                    except Exception:
                        pass

            ACTIVE_PROCESS = subprocess.Popen(
                [sys.executable, code_file],
                cwd=tmpdir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = ACTIVE_PROCESS.communicate(timeout=timeout)
            exit_code = ACTIVE_PROCESS.returncode if ACTIVE_PROCESS else -1

            result = {
                "stdout": stdout or "",
                "stderr": stderr or "",
                "exception": None if exit_code == 0 else f"Exit code {exit_code}",
                "output_files": []
            }

            # Attach saved plot if generated
            plot_path = os.path.join(PLOTS_DIR, unique_filename)
            if os.path.exists(plot_path):
                result["output_files"].append(plot_path)

            return result

        except subprocess.TimeoutExpired:
            if ACTIVE_PROCESS:
                ACTIVE_PROCESS.kill()
            return {
                "stdout": "",
                "stderr": "Timeout: execution too long.",
                "exception": "TimeoutExpired",
                "output_files": []
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": str(e),
                "exception": "Exception",
                "output_files": []
            }
        finally:
            ACTIVE_PROCESS = None
