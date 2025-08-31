import tempfile
import subprocess
import sys
import os
import re
import uuid, shutil


def detect_ptrac_mode(ptrac_path):
    """
    Automatically detect the format of a PTRAC file.
    Returns:
      - 'BIN_PTRAC' if the file is binary (classic MCNP format).
      - 'ASC_PTRAC' if the file is ASCII (or extended ASCII).
    Detection is based on the header content (presence of readable text).
    """
    try:
        with open(ptrac_path, "rb") as f:
            head = f.read(256)
            if b'ptrac' in head.lower() or all(32 <= b <= 126 or b in b'\r\n\t' for b in head):
                return 'ASC_PTRAC'
            else:
                return 'BIN_PTRAC'
    except Exception:
        return 'BIN_PTRAC'


def patch_ptrac_instantiation(code: str, ptrac_path: str, mode: str) -> str:
    """
    Patch all instances of Ptrac instantiation in the given code.
    - Replaces any form of `Ptrac(...)` with a safe instantiation
      using the correct path and detected mode (ASC_PTRAC or BIN_PTRAC).
    - Works across multiple lines, with varying variable names and indentation.
    Ensures that the correct file path and mode are always used.
    """
    safe_path = ptrac_path.replace("\\", "\\\\")
    ptrac_line = f"Ptrac(r'{safe_path}', Ptrac.{mode})"

    # Replace any generic instantiation of Ptrac(...)
    code_patched = re.sub(
        r"Ptrac\s*\((?:[^)(]+|\((?:[^)(]+|\([^)(]*\))*\))*\)",
        ptrac_line,
        code,
        flags=re.MULTILINE
    )

    # Normalize any explicit mode (force to detected one)
    code_patched = re.sub(
        r"Ptrac\.(BIN_PTRAC|ASC_PTRAC|HDF5_PTRAC)", f"Ptrac.{mode}", code_patched
    )

    if code != code_patched:
        print(f"[EVA/SANDBOX] Patch : toutes les instanciations Ptrac forcent le mode détecté : {mode}")

    return code_patched


def patch_plots(code: str, allow_plots: bool, output_file="plot.png") -> str:
    import re
    if allow_plots:
        # Local/interactive: just flush around plt.show()
        return re.sub(
            r"plt\.show\s*\([^\)]*\)",
            "import sys; sys.stdout.flush(); sys.stderr.flush(); plt.show()",
            code
        )

    # Headless (Docker): force Agg backend
    header = (
        "import matplotlib\n"
        "matplotlib.use('Agg')\n"
        "import matplotlib.pyplot as plt\n"
    )
    code = header + code

    # If the user called show(), replace it with savefig
    code = re.sub(r"plt\.show\s*\([^\)]*\)", f"plt.savefig('{output_file}')", code)

    # Final guard: save ONLY if there's a real figure with content
    code += f"""
# conditional save: avoid blank images
try:
    import matplotlib.pyplot as _plt
    _fig_nums = _plt.get_fignums()
    if _fig_nums:
        _fig = _plt.gcf()
        _has_content = False
        for _ax in _fig.get_axes():
            if _ax.has_data() or _ax.lines or _ax.collections or _ax.images:
                _has_content = True
                break
        if _has_content:
            _fig.savefig('{output_file}')
except Exception:
    pass
"""
    return code

ACTIVE_PROCESS = None  # Global handle for subprocess management

def run_ptrac_code(code: str, ptrac_path: str, timeout=60, allow_plots=False):
    """
    Execute LLM code in a sandboxed subprocess with PTRAC context.
    - Patches Ptrac(...) to the correct path/mode.
    - Forces headless matplotlib in Docker and GUARANTEES a saved figure.
    - Copies any produced images out of the temp dir BEFORE it is deleted.
    - Returns stdout/stderr and persisted output file paths.
    """
    import tempfile, subprocess, sys, os, glob

    global ACTIVE_PROCESS

    # 1) Patch MCNP Ptrac usage
    mode = detect_ptrac_mode(ptrac_path)  # 'ASC_PTRAC' or 'BIN_PTRAC'
    patched_code = patch_ptrac_instantiation(code, ptrac_path, mode)

    # 2) Patch matplotlib behavior (headless save)
    patched_code = patch_plots(patched_code, allow_plots=allow_plots)

    # Optional: dump patched code for debugging
    try:
        persist_root = os.path.join(os.getcwd(), "uploads", "plots")
        os.makedirs(persist_root, exist_ok=True)
        with open(os.path.join(persist_root, "last_patched_code.py"), "w", encoding="utf-8") as dbg:
            dbg.write(patched_code)
    except Exception:
        pass

    # 3) Run in isolated temp dir
    with tempfile.TemporaryDirectory() as tmpdir:
        code_file = os.path.join(tmpdir, "llm_code.py")
        with open(code_file, "w", encoding="utf-8") as f:
            f.write(patched_code + "\n")

        try:
            ACTIVE_PROCESS = subprocess.Popen(
                [sys.executable, code_file],
                cwd=tmpdir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = ACTIVE_PROCESS.communicate(timeout=timeout)
            exit_code = ACTIVE_PROCESS.returncode if ACTIVE_PROCESS else -1

            # 4) Copy any produced images out of tmpdir BEFORE it is deleted
            persisted = []
            try:
                persist_root = os.path.join(os.getcwd(), "uploads", "plots")
                os.makedirs(persist_root, exist_ok=True)

                # collect common image extensions (and pdf/svg)
                for ext in ("png", "jpg", "jpeg", "svg", "pdf"):
                    for p in glob.glob(os.path.join(tmpdir, f"*.{ext}")):
                        if os.path.isfile(p):
                            dest = os.path.join(persist_root, f"plot_{uuid.uuid4().hex}.{ext}")
                            shutil.copy2(p, dest)
                            persisted.append(dest)

                # back-compat: ensure canonical plot.png is captured if not matched above
                p_default = os.path.join(tmpdir, "plot.png")
                if os.path.exists(p_default) and not any(dest.endswith(".png") for dest in persisted):
                    dest = os.path.join(persist_root, f"plot_{uuid.uuid4().hex}.png")
                    shutil.copy2(p_default, dest)
                    persisted.append(dest)
            except Exception:
                # ignore persistence failures; frontend will simply not get files
                pass

            # 5) Build result
            try:
                tmp_listing = os.listdir(tmpdir)
            except Exception as e:
                tmp_listing = [f"error listing tmpdir: {e}"]

            return {
                "stdout": stdout or "",
                "stderr": stderr or "",
                "exception": None if exit_code == 0 else f"Return code {exit_code}",
                "success": exit_code == 0,
                "output_files": persisted,   # persisted, stable paths (e.g., /app/uploads/plots/plot_<uuid>.png)
                "tmpdir_files": tmp_listing  # for debugging/verification
            }

        except subprocess.TimeoutExpired:
            if ACTIVE_PROCESS:
                ACTIVE_PROCESS.kill()
            return {
                "stdout": "",
                "stderr": "Timeout: execution too long.",
                "exception": "TimeoutExpired",
                "success": False,
                "output_files": [],
                "tmpdir_files": []
            }
        except Exception as e:
            return {
                "stdout": "",
                "stderr": str(e),
                "exception": "Exception",
                "success": False,
                "output_files": [],
                "tmpdir_files": []
            }
        finally:
            ACTIVE_PROCESS = None
