# test_campbell_agent.py

import json
from modules.campbell import CampbellOrchestrator

# Chemin PTRAC test (change-le selon ton cas)
PTRAC_PATH = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp.ptrac"
# PTRAC_PATH = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp_ASCII.ptrac"

def debug_query(query, ptrac_path=PTRAC_PATH):
    print("\n" + "="*80)
    print(f"QUERY: {query}\nPTRAC: {ptrac_path}")
    print("="*80)
    orc = CampbellOrchestrator()
    result = orc.process_query(query, ptrac_path=ptrac_path)
    # print("\n--- Résultat complet ---")
    # print(json.dumps(result, indent=2, ensure_ascii=False))
    if result.get("logs"):
        print("\n--- LOGS ---")
        for log in result["logs"]:
            print(log)
    if result.get("error"):
        print("\n--- ERROR ---")
        print(result["error"])
    if result.get("execution_result"):
        print("\n--- EXECUTION RESULT ---")
        print(json.dumps(result["execution_result"], indent=2, ensure_ascii=False))
    print("="*80 + "\n")

if __name__ == "__main__":
    # Test de base
    debug_query("Affiche l'énergie minimale et la position x y z des neutrons traversant la surface 300.", ptrac_path=PTRAC_PATH)

    # Test complexe (pour forcer les bugs ou le LLM à générer du code compliqué)
    # debug_query("Donne-moi l’énergie minimale, maximale et la variance pour les photons secondaires produits par les réactions photo-nucléaires traversant la surface 7 entre 0.1 et 1 MeV.", ptrac_path=PTRAC_PATH)

    # Ajoute d'autres queries à volonté !
