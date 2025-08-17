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
    """
    Agent chargé d’exécuter le code Python généré par OTACON,
    en sandbox, sur un fichier PTRAC MCNP. Il capture les résultats,
    les logs, les erreurs et les fichiers produits.
    """

    def __init__(self):
        self.ptrac_path = None
        self.logs = []

    def load_file(self, ptrac_path: str) -> bool:
        """ Charge le fichier PTRAC à analyser. """
        if not os.path.isfile(ptrac_path):
            self.logs.append(f"[EVA] Fichier non trouvé: {ptrac_path}")
            return False
        self.ptrac_path = ptrac_path
        self.logs.append(f"[EVA] Fichier PTRAC chargé: {ptrac_path}")
        return True

    def execute_code(self, code: str, language: str = "python", allow_plots=False) -> dict:
        """ Exécute le code Python sur le fichier PTRAC chargé. """
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
        """ Retourne l’historique des exécutions/logs. """
        return self.logs
