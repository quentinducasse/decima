#!/usr/bin/env python3
"""
DECIMA Demo Mode - Standalone Example
======================================

This example demonstrates DECIMA in DEMO_MODE with LIMITED functionality:
- + Works without OpenAI API (no costs)
- + Works without Neo4j Knowledge Graph
- + Base mcnptools context IS injected (API structure + code example)
- - Returns FIXED code example (DEMO_MODE=true, ignores your query)
- - No intelligent code generation
- - No MCNP domain-specific context from Knowledge Graph (EMMA disabled)

NOTE: Even with OpenAI API (DEMO_MODE=false), without Neo4j Knowledge Graph,
OTACON generates code using only basic mcnptools syntax (from structure + example).
This may work for simple queries but lacks domain-specific MCNP knowledge.

For FULL functionality with intelligent code generation AND KG context,
use Docker mode: docker compose up -d

See examples/README.md for detailed comparison.
"""

import os
import sys

# Add project root to path
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# IMPORTANT: Load .env.docker BEFORE importing DECIMA modules
# ============================================================
from dotenv import load_dotenv

# Load environment configuration
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_docker = os.path.join(project_root, ".env.docker")

if os.path.exists(env_docker):
    load_dotenv(env_docker, override=True)
else:
    # Fallback to demo mode if no .env.docker
    os.environ['DEMO_MODE'] = 'true'
    os.environ['OPENAI_API_KEY'] = ''

# Check configuration
demo_mode = os.getenv('DEMO_MODE', 'false').lower() == 'true'
api_key = os.getenv('OPENAI_API_KEY', '')

print("=" * 70)
print("  DECIMA - Standalone Example (Python Package)")
print("=" * 70)
print()
print("Configuration (from .env.docker):")
print(f"   DEMO_MODE: {demo_mode}")
print(f"   OpenAI API Key: {'Set' if api_key and api_key != 'your_api_key_here' else 'Not set'}")
print()

if demo_mode:
    print("MODE: Using DEMO_MODE (fixed code examples)")
    print("   + No API calls (no costs)")
    print("   + Works without OpenAI API")
    print("   - Returns FIXED code example (ignores your query)")
    print("   - No intelligent code generation")
else:
    print("MODE: Using OpenAI API (DEMO_MODE=false)")
    print("   + Will call OpenAI API for code generation")
    print("   + Generates code for YOUR query")
    print("   - WITHOUT Neo4j: May generate code with errors")
    print("   - Missing MCNP domain knowledge context")

print()
print("WARNING: This standalone mode has NO Neo4j Knowledge Graph")
print("   -> EMMA (Knowledge Graph agent) is DISABLED")
print("   -> BUT: Base mcnptools context IS injected (API structure + code example)")
print("   -> This provides basic mcnptools syntax guidance")
print()
print("TIP: For FULL functionality with Knowledge Graph:")
print("   -> Use Docker mode: docker compose up -d")
print("   -> See INSTALL.md Method 2")
print()
print("=" * 70)

# Import after environment is set
from modules.campbell import CampbellOrchestrator

def main():
    """Run DECIMA in demo mode - returns fixed example code."""

    # Sample PTRAC file path (relative to project root)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ptrac_path = os.path.join(project_root, "data", "ptrac_samples", "basic_ptrac_example_decima_ascii.ptrac")

    # Simple user query (will be ignored in demo mode)
    query = "What is the average energy of the collision events?"

    print()
    print(f"PTRAC file: {ptrac_path}")
    print(f"Query: {query}")
    print()

    if demo_mode:
        print("NOTE: In DEMO_MODE=true, your query is IGNORED")
        print("   The system always returns the same fixed collision analysis code.")
    else:
        print("NOTE: With DEMO_MODE=false, OpenAI will generate code for your query")
        print("   Base mcnptools context IS provided (API structure + example)")
        print("   BUT without Neo4j KG, lacks domain-specific MCNP knowledge")

    print()
    print("-" * 70)
    print()

    # Initialize orchestrator
    orchestrator = CampbellOrchestrator()

    # Run analysis (demo mode will return fixed code)
    print("Running DECIMA workflow...")
    print()

    result = orchestrator.process_query(
        query=query,
        ptrac_path=ptrac_path,
        use_context=True  # Inject base mcnptools context (structure + example), but no EMMA KG
    )

    # Display results
    print("=" * 70)
    if demo_mode:
        print("  RESULT (DEMO_MODE=true: FIXED EXAMPLE)")
    else:
        print("  RESULT (DEMO_MODE=false: OpenAI Generated Code)")
    print("=" * 70)
    print()

    if result.get('error'):
        print(f"Workflow Error: {result['error']}")
        print()

    print("Explanation:")
    print("-" * 70)
    print(result.get('response', 'No explanation available'))
    print()

    if demo_mode:
        print("Generated Code (FIXED - Same for all queries):")
    else:
        print("Generated Code (OpenAI API):")
    print("-" * 70)
    print(result.get('code', 'No code generated'))
    print()

    # Check execution result
    exec_result = result.get('execution_result', {})
    if exec_result:
        stdout = exec_result.get('stdout', '')
        stderr = exec_result.get('stderr', '')

        if stdout:
            print("Execution Output:")
            print("-" * 70)
            print(stdout)
            print()

        if stderr:
            print("=" * 70)
            print("EXECUTION ERROR DETECTED")
            print("=" * 70)
            print(stderr)
            print()
            print("POSSIBLE CAUSE: Missing Knowledge Graph context")
            print("   -> Without Neo4j, OTACON generates code without MCNP domain knowledge")
            print("   -> This can lead to incorrect classes, methods, or syntax")
            print()
            print("SOLUTION: Use Docker mode for full functionality")
            print("   -> docker compose up -d")
            print("   -> See INSTALL.md Method 2")
            print()

    print("=" * 70)
    print("  Example Completed")
    print("=" * 70)
    print()

    if demo_mode:
        print("LIMITATIONS (DEMO_MODE=true):")
        print("   - Fixed code example (your query was IGNORED)")
        print("   - No intelligent code generation")
    else:
        print("LIMITATIONS (DEMO_MODE=false without Neo4j):")
        print("   + Has base mcnptools context (API structure + example)")
        print("   - Missing MCNP domain-specific knowledge from KG")
        print("   - May generate code with domain errors")

    print("   - No Knowledge Graph EMMA context (only base mcnptools syntax)")
    print()
    print("TO GET FULL FUNCTIONALITY:")
    print("   -> Use Docker mode: docker compose up -d")
    print("   -> Includes Neo4j + Knowledge Graph automatically")
    print("   -> See INSTALL.md Method 2")
    print()
    print("=" * 70)
    print()

    # Show workflow logs
    if result.get('logs'):
        print("Workflow Logs:")
        print("-" * 60)
        for log in result['logs']:
            print(f"   {log}")
        print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print()
        print("=" * 60)
        print("[X] ERROR")
        print("=" * 60)
        print(f"   {str(e)}")
        print()
        print("[i] Common Issues:")
        print()
        print("   1. mcnptools not installed:")
        print("      - mcnptools is not yet on PyPI")
        print("      - Install from source or use Docker mode")
        print()
        print("   2. PTRAC file not found:")
        print("      - Check path: data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac")
        print()
        print("=" * 60)
        sys.exit(1)
