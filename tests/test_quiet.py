from dotenv import load_dotenv
load_dotenv()
import sys, os, json, re
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.quiet import QUIET

CATEGORIES = ["events", "data", "classes", "methods", "attributes", "dictionaries"]

def bilan_par_categorie(agent, testset, output_file=None):
    stats = {cat: {"TP": 0, "FN": 0, "FP": 0, "TN": 0} for cat in CATEGORIES}
    details = defaultdict(list)
    lines = []

    for case in testset:
        detected = agent.analyze(case["query"])
        expected = case.get("expected_focus_quiet", {})
        for cat in CATEGORIES:
            exp = set(x.upper() for x in expected.get(cat, []) if x != "")
            det = set(x.upper() for x in detected.get(f"focus_{cat}", []) if x != "")
            # Comptage pour chaque catégorie
            for label in exp | det:
                if label in exp and label in det:
                    stats[cat]["TP"] += 1
                elif label in exp and label not in det:
                    stats[cat]["FN"] += 1
                    details[cat].append({"query": case["query"], "FN": label})
                elif label not in exp and label in det:
                    stats[cat]["FP"] += 1
                    details[cat].append({"query": case["query"], "FP": label})
                else:
                    stats[cat]["TN"] += 1

    lines.append("\n=== BILAN PAR AXE (FN/FP/TP) ===")
    for cat in CATEGORIES:
        d = stats[cat]
        lines.append(f"{cat.capitalize():11}: TP={d['TP']:2} | FN={d['FN']:2} | FP={d['FP']:2}")
    lines.append("\n--- Détail des principaux FN/FP par axe ---")
    for cat in CATEGORIES:
        if details[cat]:
            lines.append(f"\n{cat.upper()}:")
            for entry in details[cat][:5]:  # Les 5 premiers par axe
                lines.append(str(entry))

    if output_file:
        with open(output_file, "a", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
    else:
        for line in lines:
            print(line)

def main():
    # Chemin au jeu de test
    testset_path = os.path.join(os.path.dirname(__file__), 'testsets', 'matching_eval.json')    
    output_file = "quiet_focus_eval.txt"
    print(f"[INFO] Chargement du jeu de tests : {testset_path}")
    print(f"[INFO] Les résultats détaillés sont également enregistrés dans {output_file}")
    with open(testset_path, encoding="utf-8") as f:
        testset = json.load(f)

    agent = QUIET()
    total = len(testset)
    mismatches = []

    # Comptage exact match sur toutes les catégories à la fois
    exact_match = 0
    for case in testset:
        query = case["query"]
        expected = case.get("expected_focus_quiet", {})
        detected = agent.analyze(query)
        match_all = True
        case_diff = {"query": query, "diffs": {}}
        for cat in CATEGORIES:
            exp = set(x.upper() for x in expected.get(cat, []) if x != "")
            det = set(x.upper() for x in detected.get(f"focus_{cat}", []) if x != "")
            if exp != det:
                match_all = False
                case_diff["diffs"][cat] = {"expected": list(exp), "detected": list(det),
                                           "FP": list(det - exp), "FN": list(exp - det)}
        if match_all:
            exact_match += 1
        else:
            mismatches.append(case_diff)

    print(f"\nQUIETAgent multi-focus matching: {exact_match}/{total} exact matches (all categories)")
    print(f"Total queries with at least 1 mismatch: {len(mismatches)}\n")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"QUIETAgent multi-focus matching: {exact_match}/{total} exact matches (all categories)\n")
        f.write(f"Total queries with at least 1 mismatch: {len(mismatches)}\n\n")
        for d in mismatches:
            f.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    # Bilan détaillé par axe (affiche et sauvegarde)
    bilan_par_categorie(agent, testset, output_file=output_file)
    bilan_par_categorie(agent, testset, output_file=None)

if __name__ == "__main__":
    main()
