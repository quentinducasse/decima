from dotenv import load_dotenv
load_dotenv()
import os
import json
from modules.quiet import QUIET
from modules.emma import EMMA

try:
    from termcolor import colored
except ImportError:
    def colored(s, color): return s

def load_testset(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def compare_entities(expected, detected):
    exp_set = set([e.upper() for e in expected])
    det_set = set([e["id"].upper() for e in detected])
    tp = exp_set & det_set
    fp = det_set - exp_set
    fn = exp_set - det_set
    return tp, fp, fn, det_set, exp_set

def quiet_detected_entities(quiet_out):
    quiet_set = set()
    for k in ["focus_events", "focus_data", "focus_dictionaries", "focus_classes", "focus_methods", "focus_attributes"]:
        quiet_set |= set(x.upper() for x in quiet_out.get(k, []) if x)
    return quiet_set

def print_match_details(log, detected_quiet_set, color_output=True):
    def col(s, color):
        if color_output:
            return colored(s, color)
        return s
    lines = []
    lines.append("-" * 40)
    lines.append(f"Query: {log['query']}")
    lines.append(f"TP: {log['TP']}  |  FP: {log['FP']}  |  FN: {log['FN']}\n")
    lines.append("Expected entities:")
    for e in sorted(log["expected"]):
        if e in log["detected"]:
            lines.append(col(f"  + {e}", "green"))
        else:
            lines.append(col(f"  ! {e}", "red"))
    lines.append("\nDetected by QUIET:")
    for e in sorted(detected_quiet_set):
        if e in log["expected"]:
            lines.append(col(f"  ~ {e} (also expected)", "cyan"))
        else:
            lines.append(col(f"  ~ {e}", "blue"))
    lines.append("\nDetected entities (EMMA):")
    for e in sorted(log["detected"]):
        if e in log["expected"]:
            lines.append(col(f"  + {e}", "green"))
        elif e in detected_quiet_set:
            lines.append(col(f"  ~ {e} [QUIET]", "blue"))
        else:
            lines.append(col(f"  x {e}", "yellow"))
    lines.append("-" * 40)
    return "\n".join(lines)

def main():
    testset_path = os.path.join(os.path.dirname(__file__), "testsets", "matching_eval.json")
    testset = load_testset(testset_path)
    quiet = QUIET()
    emma = EMMA(neo4j_user="neo4j", neo4j_password="decima123")
    total, exact, total_tp, total_fp, total_fn = 0, 0, 0, 0, 0
    logs = []
    output_lines = []
    # Ajout compteur FN global
    fn_counter = {}

    for case in testset:
        query = case["query"]
        expected = case.get("expected_focus_emma", [])
        quiet_out = quiet.analyze(query)
        kg_context = emma.extract_kg_context(quiet_out)
        detected = kg_context.get("entities", [])
        detected_quiet_set = quiet_detected_entities(quiet_out)
        tp, fp, fn, det_set, exp_set = compare_entities(expected, detected)
        match = det_set == exp_set
        total += 1
        if match:
            exact += 1
        total_tp += len(tp)
        total_fp += len(fp)
        total_fn += len(fn)
        log = {
            "query": query,
            "expected": list(exp_set),
            "detected": list(det_set),
            "TP": len(tp), "FP": len(fp), "FN": len(fn),
            "detected_quiet": list(detected_quiet_set)
        }
        logs.append(log)
        # Ajout FN global
        for missed in fn:
            fn_counter[missed] = fn_counter.get(missed, 0) + 1
        print(print_match_details(log, detected_quiet_set))
        output_lines.append(print_match_details(log, detected_quiet_set, color_output=False))

    print(f"\nEMMAAgent entity matching: {exact}/{total} exact matches")
    print(f"Total TP: {total_tp}, FP: {total_fp}, FN: {total_fn}")

    # Résumé des FN par entité
    if fn_counter:
        print("\n[FN SUMMARY] (entities missed at least once)")
        for entity, count in sorted(fn_counter.items(), key=lambda x: -x[1]):
            print(f"  - {entity}: {count} occurrence(s)")

    out_txt = os.path.join(os.path.dirname(__file__), "emma_eval_output.txt")
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
        # Aussi log des FN à la fin du fichier
        if fn_counter:
            f.write("\n\n[FN SUMMARY]\n")
            for entity, count in sorted(fn_counter.items(), key=lambda x: -x[1]):
                f.write(f"{entity}: {count} occurrence(s)\n")
    print(f"\nResults written to {out_txt}")

    emma.close()

if __name__ == "__main__":
    main()
