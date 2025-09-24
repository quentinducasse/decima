# tests/test_campbell_agent.py

import json
import os
import sys
from modules.campbell import CampbellOrchestrator

# === Path to the PTRAC file used for testing ===
# ⚠️ IMPORTANT: Replace this path with the location of your own PTRAC file
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # remonte au dossier racine du repo
PTRAC_PATH = os.path.join(BASE_DIR, "data", "ptrac_samples", "example_ptrac_1.mcnp.ptrac")

# --- Early check before running anything ---
if "username" in PTRAC_PATH or not os.path.isfile(PTRAC_PATH):
    print(f"\n[ERROR] PTRAC_PATH is not set correctly!\n"
          f"Please edit tests/test_campbell_agent.py and set PTRAC_PATH to the path of your own PTRAC file.\n"
          f"Current PTRAC_PATH = {PTRAC_PATH}\n")
    sys.exit(1)


def debug_query(query, ptrac_path=PTRAC_PATH):
    """
    Helper function to run a query with CampbellOrchestrator
    and print logs, errors, and execution results.
    Provides clearer error reporting for LLM API key issues.
    """
    print("\n" + "=" * 80)
    print(f"QUERY: {query}\nPTRAC: {ptrac_path}")
    print("=" * 80)

    orc = CampbellOrchestrator()
    try:
        result = orc.process_query(query, ptrac_path=ptrac_path)
    except Exception as e:
        # Special handling for invalid/missing API key
        err_str = str(e)
        if "401" in err_str or "Unauthorized" in err_str:
            print("\n[ERROR] LLM API request failed with '401 Unauthorized'.")
            print("This usually means your OpenAI API key is missing or invalid.")
            print("➡️  Please open your `.env.docker` (or `.env.local`) file and set a valid key, for example:")
            print("    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            sys.exit(1)
        else:
            print(f"\n[ERROR] Unexpected exception during query execution: {err_str}\n")
            sys.exit(1)

    # Display logs if available
    if result.get("logs"):
        print("\n--- LOGS ---")
        for log in result["logs"]:
            print(log)

    # Display error if available
    if result.get("error"):
        print("\n--- ERROR ---")
        print(result["error"])

    # Display execution result if available
    if result.get("execution_result"):
        print("\n--- EXECUTION RESULT ---")
        print(json.dumps(result["execution_result"], indent=2, ensure_ascii=False))

    print("=" * 80 + "\n")


if __name__ == "__main__":
    # Basic test query
    debug_query(
        "Display the minimum energy and the x y z positions of particles in the 10 first histories.",
        ptrac_path=PTRAC_PATH
    )

