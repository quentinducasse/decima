# test_otacon_agent_api.py

from dotenv import load_dotenv
load_dotenv()  # Charge automatiquement les variables du .env dans l'environnement

import os
from modules.otacon import OTACON

def test_otacon_api_key():
    # Vérifie la clé dans l'env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not api_key.startswith("sk-"):
        print("[FAIL] Clé OPENAI_API_KEY absente ou mal formée (pas chargée du .env ?).")
        return False

    agent = OTACON()
    user_query = "Donne-moi un exemple d'utilisation de mcnptools pour parser un fichier PTRAC."
    emma_context = {"entities": []}  # Aucun contexte filtré

    try:
        print("[INFO] Test d'appel LLM via OTACON...")
        result = agent.run(user_query, emma_context)
        print("\n[OPENAI/OTACON OK] Explication LLM :")
        print(result["explanation"][:400] + " [...]")
        print("\nBloc code extrait par parsing :")
        print(result["code"][:400] + " [...]")
        print("\n[SUCCESS] Clé API et accès LLM confirmés.\n")
        return True
    except Exception as e:
        print(f"[FAIL] Erreur lors de l'appel OpenAI : {e}")
        return False

if __name__ == "__main__":
    test_otacon_api_key()
