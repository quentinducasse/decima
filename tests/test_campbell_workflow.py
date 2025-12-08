# tests/test_campbell_agent.py

import json
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.campbell import CampbellOrchestrator

# === Path to the PTRAC file used for testing ===
# ⚠️ IMPORTANT: Replace this path with the location of your own PTRAC file
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # remonte au dossier racine du repo
PTRAC_PATH = os.path.join(BASE_DIR, "data", "ptrac_samples", "basic_ptrac_example_decima_ascii.ptrac")

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

        # Check for Neo4j-related errors
        error_msg = str(result["error"])
        is_neo4j_error = (
            ("EMMA ERROR" in error_msg and "NoneType" in error_msg) or
            ("OTACON ERROR" in error_msg and "not a mapping" in error_msg) or
            ("EMMA ERROR" in error_msg and "connection" in error_msg.lower()) or
            ("EMMA ERROR" in error_msg and "7687" in error_msg)
        )
        if is_neo4j_error:
            print("\n" + "=" * 80)
            print("TIP: This error usually means Neo4j is not running")
            print("=" * 80)
            print("\nTo fix this:")
            print("  1. Start Neo4j:")
            print("     docker compose up -d neo4j")
            print("\n  2. Wait ~15 seconds for Neo4j to start")
            print("\n  3. Load the Knowledge Graph:")
            print("     docker compose exec app python kg/loader/neo4j_loader.py")
            print("\n  4. Run this test again")
            print("\nAlternatively, use DEMO_MODE=true in .env.docker to test without Neo4j")
            print("=" * 80)

    # Display execution result if available
    if result.get("execution_result"):
        print("\n--- EXECUTION RESULT ---")
        print(json.dumps(result["execution_result"], indent=2, ensure_ascii=False))

        # Check for mcnptools import error in EVA sandbox
        exec_result = result["execution_result"]
        stderr = exec_result.get("stderr", "")
        if "No module named 'mcnptools'" in stderr and not exec_result.get("success"):
            print("\n" + "=" * 80)
            print("NOTE: mcnptools not available in EVA sandbox (Python Package mode)")
            print("=" * 80)
            print("\nThis is expected behavior when running in Python Package mode.")
            print("The workflow completed successfully:")
            print("  [OK] QUIET - Query interpretation")
            print("  [OK] EMMA - Knowledge Graph context extraction")
            print("  [OK] OTACON - Code generation")
            print("  [OK] EVA - Code execution attempted")
            print("\nHowever, mcnptools is not available in the EVA sandbox environment.")
            print("\nFor full execution with results:")
            print("  1. Use Docker mode:")
            print("     docker compose up -d")
            print("     docker compose exec app python kg/loader/neo4j_loader.py")
            print("     # Then use web interface at http://localhost:5050")
            print("\n  2. Or run the generated code directly (outside sandbox):")
            print("     # Copy the generated code from OTACON output above")
            print("     # Save it to a file and run: python your_script.py")
            print("=" * 80)

    print("=" * 80 + "\n")


if __name__ == "__main__":
    # Basic test query
    debug_query(
        "Display the minimum energy and the x y z positions of particles in the 10 first histories.",
        ptrac_path=PTRAC_PATH
    )

