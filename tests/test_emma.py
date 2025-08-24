# tests/test_emma.py
from dotenv import load_dotenv, find_dotenv
# Load environment variables (.env or .env.local)
load_dotenv(find_dotenv(usecwd=True))
load_dotenv(".env.local", override=False)

import os
import json

try:
    from termcolor import colored
except ImportError:
    def colored(s, color): return s

from modules.quiet import QUIET
from modules.emma import EMMA


def load_testset(path):
    """Load evaluation testset (JSON)."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compare_entities(expected, detected):
    """
    Compare expected entities vs. detected entities.
    Returns sets of true positives, false positives, and false negatives.
    """
    exp_set = set([e.upper() for e in expected])
    det_set = set([e["id"].upper() for e in detected])
    tp = exp_set & det_set
    fp = det_set - exp_set
    fn = exp_set - det_set
    return tp, fp, fn, det_set, exp_set


def quiet_detected_entities(quiet_out):
    """Extract all entities detected by QUIET into a flat set."""
    quiet_set = set()
    for k in ["focus_events", "focus_data", "focus_dictionaries", "focus_classes", "focus_methods", "focus_attributes"]:
        quiet_set |= set(x.upper() for x in quiet_out.get(k, []) if x)
    return quiet_set


def print_match_details(log, detected_quiet_set, color_output=True):
    """Pretty-print comparison between expected and detected entities."""
    def col(s, color):
        return colored(s, color) if color_output else s

    lines = []
    lines.append("-" * 40)
    lines.append(f"Query: {log['query']}")
    lines.append(f"TP: {log['TP']}  |  FP: {log['FP']}  |  FN: {log['FN']}\n")
    lines.append("Expected entities:")
    for e in sorted(log["expected"]):
        if e in log["detected"]:
            lines.append(col(f"  + {e}", "green"))   # correctly detected
        else:
            lines.append(col(f"  ! {e}", "red"))     # missed entity
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
            lines.append(col(f"  x {e}", "yellow"))  # detected but unexpected
    lines.append("-" * 40)
    return "\n".join(lines)


def main():
    testset_path = os.path.join(os.path.dirname(__file__), "testsets", "matching_eval.json")
    testset = load_testset(testset_path)

    quiet = QUIET()
    # Neo4j credentials are read from environment (local or docker .env)
    emma = EMMA(
        neo4j_user=os.getenv("NEO4J_USER", "neo4j"),
        neo4j_password=os.getenv("NEO4J_PASSWORD", "decima123"),
    )

    total, exact, total_tp, total_fp, total_fn = 0, 0, 0, 0, 0
    fn_counter = {}
    output_lines = []

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

        # Display match details in console
        print(print_match_details(log, detected_quiet_set))
        output_lines.append(print_match_details(log, detected_quiet_set, color_output=False))

        # Count false negatives for summary
        for missed in fn:
            fn_counter[missed] = fn_counter.get(missed, 0) + 1

    # Print global stats
    print(f"\nEMMAAgent entity matching: {exact}/{total} exact matches")
    print(f"Total TP: {total_tp}, FP: {total_fp}, FN: {total_fn}")

    if fn_counter:
        print("\n[FN SUMMARY] (entities missed at least once)")
        for entity, count in sorted(fn_counter.items(), key=lambda x: -x[1]):
            print(f"  - {entity}: {count} occurrence(s)")

    # Save evaluation output
    out_txt = os.path.join(os.path.dirname(__file__), "emma_eval_output.txt")
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
        if fn_counter:
            f.write("\n\n[FN SUMMARY]\n")
            for entity, count in sorted(fn_counter.items(), key=lambda x: -x[1]):
                f.write(f"{entity}: {count} occurrence(s)\n")
    print(f"\nResults written to {out_txt}")

    emma.close()


if __name__ == "__main__":
    main()
