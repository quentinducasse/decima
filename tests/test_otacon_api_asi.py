# test_otacon_api_asi.py

from dotenv import load_dotenv
load_dotenv()

import os
from modules.otacon import OTACON

def test_otacon_api():
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    print(f"[INFO] Provider détecté : {provider}")

    # Clé selon le provider
    if provider == "asi1":
        api_key = os.getenv("ASI1_API_KEY")
        if not api_key or not api_key.startswith("sk"):
            print("[FAIL] Clé ASI1_API_KEY absente ou incorrecte.")
            return False
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not api_key.startswith("sk"):
            print("[FAIL] Clé OPENAI_API_KEY absente ou incorrecte.")
            return False

    agent = OTACON()
    user_query = "Donne-moi un exemple très simple de parsing PTRAC avec mcnptools"
    emma_context = {"entities": [], "use_context": False}  # pas de contexte EMMA

    try:
        print("[INFO] Envoi de la requête au LLM...")
        result = agent.run(user_query, emma_context)
        print("\n[OK] Explication LLM :")
        print(result["explanation"][:400] + " [...]")
        print("\n[OK] Bloc code :")
        print(result["code"][:400] + " [...]")
        print("\n[SUCCESS] Appel API réussi.\n")
        return True
    except Exception as e:
        print(f"[FAIL] Erreur lors de l'appel LLM : {e}")
        return False

if __name__ == "__main__":
    test_otacon_api()
