import tempfile
import subprocess
import sys
import os
import re

def detect_ptrac_mode(ptrac_path):
    """
    Détecte automatiquement le format du fichier PTRAC :
    - Retourne 'BIN_PTRAC' si binaire (MCNP classique)
    - Retourne 'ASC_PTRAC' si ASCII (ou ASCII étendu)
    """
    try:
        with open(ptrac_path, "rb") as f:
            head = f.read(256)
            # Signature ASCII : contient du texte lisible (MCNP ou ptrac dans l'en-tête)
            if b'ptrac' in head.lower() or all(32 <= b <= 126 or b in b'\r\n\t' for b in head):
                return 'ASC_PTRAC'
            else:
                return 'BIN_PTRAC'
    except Exception:
        return 'BIN_PTRAC'

def patch_ptrac_instantiation(code: str, ptrac_path: str, mode: str) -> str:
    """
    Remplace TOUTE instanciation de Ptrac par la version robuste adaptée au fichier et au chemin.
    Couvre : tous les noms de variable, multi-instanciations, indentation variable, sur une ou plusieurs lignes.
    """
    safe_path = ptrac_path.replace("\\", "\\\\")
    ptrac_line = f"Ptrac(r'{safe_path}', Ptrac.{mode})"

    # Remplacement ultra-robuste : tout appel à Ptrac(…) dans tout le code (peu importe variable, indentation, etc.)
    # Couvre les cas multi-lignes et espace/indentation variable.
    code_patched = re.sub(
        r"Ptrac\s*\((?:[^)(]+|\((?:[^)(]+|\([^)(]*\))*\))*\)",
        ptrac_line,
        code,
        flags=re.MULTILINE
    )

    # Facultatif : Normalise aussi les modes en dur si jamais il en reste
    code_patched = re.sub(
        r"Ptrac\.(BIN_PTRAC|ASC_PTRAC|HDF5_PTRAC)", f"Ptrac.{mode}", code_patched
    )

    # Log pour debug (optionnel)
    if code != code_patched:
        print(f"[EVA/SANDBOX] Patch : toutes les instanciations Ptrac forcent le mode détecté : {mode}")

    return code_patched

def patch_disable_plots(code: str) -> str:
    """
    Patche le code Python pour neutraliser toute instruction plt.show(), plt.savefig(), plt.ion(), plt.figure().show(), etc.
    """
    # Neutraalise tout plt.show() / plt.ion() / plt.savefig() / .show()
    code = re.sub(r"plt\.show\s*\([^\)]*\)", "# plt.show() désactivé par EVA", code)
    code = re.sub(r"plt\.ion\s*\([^\)]*\)", "# plt.ion() désactivé par EVA", code)
    code = re.sub(r"plt\.savefig\s*\([^\)]*\)", "# plt.savefig() désactivé par EVA", code)
    code = re.sub(r"\.show\s*\([^\)]*\)", "# .show() désactivé par EVA", code)  # pour fig.show()
    return code

ACTIVE_PROCESS = None  # Ajout global

def run_ptrac_code(code: str, ptrac_path: str, timeout=60, allow_plots=False):
    global ACTIVE_PROCESS

    mode = detect_ptrac_mode(ptrac_path)
    patched_code = patch_ptrac_instantiation(code, ptrac_path, mode)

    if not allow_plots:
        patched_code = patch_disable_plots(patched_code)

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

            # Si le process a été interrompu proprement, returncode existe
            exit_code = ACTIVE_PROCESS.returncode if ACTIVE_PROCESS else -1

            return {
                "stdout": stdout or "",
                "stderr": stderr or "",
                "exception": None if exit_code == 0 else f"Code retour {exit_code}",
                "output_files": []
            }
        except subprocess.TimeoutExpired:
            if ACTIVE_PROCESS:
                ACTIVE_PROCESS.kill()
            return {
                "stdout": "",
                "stderr": "Timeout: exécution trop longue.",
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

