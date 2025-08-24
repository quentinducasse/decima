"""
DECIMA Agent - EVA - Execution & Validation Agent
Secure sandbox for executing OTACON-generated Python code on PTRAC files, capturing results and errors
"""
from dotenv import load_dotenv
import os

if os.path.exists(".env.local"):
    load_dotenv(".env.local")
elif os.path.exists(".env.docker"):
    load_dotenv(".env.docker")
else:
    load_dotenv()

import os
from tools.sandbox import run_ptrac_code

class EVA:
    def __init__(self):
        self.ptrac_path = None
        self.logs = []

    def load_file(self, ptrac_path: str) -> bool:
        if not os.path.isfile(ptrac_path):
            self.logs.append(f"[EVA] Fichier non trouvé: {ptrac_path}")
            return False
        self.ptrac_path = ptrac_path
        self.logs.append(f"[EVA] Fichier PTRAC chargé: {ptrac_path}")
        return True

    def execute_code(self, code: str, language: str = "python", allow_plots=False) -> dict:
        if not self.ptrac_path:
            result = {
                "success": False,
                "stdout": "",
                "stderr": "[EVA] Aucun fichier PTRAC chargé.",
                "exception": "NoFileLoaded",
                "output_files": []
            }
            self.logs.append(result)
            return result
        # Exécution sécurisée
        code = code.replace("<PTRAC_PATH_PLACEHOLDER>", self.ptrac_path.replace("\\", "\\\\"))
        result = run_ptrac_code(code, self.ptrac_path, allow_plots=allow_plots)
        result["success"] = result["exception"] is None
        self.logs.append(result)
        return result


    def get_logs(self):
        return self.logs
