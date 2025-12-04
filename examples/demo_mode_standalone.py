#!/usr/bin/env python3
"""
DECIMA Demo Mode - Standalone Example
======================================

Minimal setup for testing DECIMA without external dependencies.
Returns pre-written example code regardless of your query.

See examples/README.md for:
- Full comparison of all three modes
- Detailed advantages and limitations
- When to use each mode
"""

import os
import sys

# Add project root to path
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# IMPORTANT: Set DEMO_MODE BEFORE importing DECIMA modules
# ============================================================
os.environ['DEMO_MODE'] = 'true'
os.environ['OPENAI_API_KEY'] = ''  # Empty - not needed in demo mode
os.environ['NEO4J_URI'] = 'bolt://localhost:7687'  # Not used in demo mode
os.environ['NEO4J_USER'] = 'neo4j'
os.environ['NEO4J_PASSWORD'] = 'neo4j'

print("=" * 60)
print("DECIMA - DEMO MODE (Standalone - No Dependencies)")
print("=" * 60)
print()
print("Configuration:")
print("   [+] DEMO_MODE: enabled")
print("   [+] OpenAI API: not required")
print("   [+] Neo4j KG: not required")
print("   [!] mcnptools: required (not on PyPI yet)")
print()
print("-" * 60)

# Import after environment is set
from modules.campbell import CampbellOrchestrator

def main():
    """Run DECIMA in demo mode - returns fixed example code."""

    # Sample PTRAC file path (relative to project root)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ptrac_path = os.path.join(project_root, "data", "ptrac_samples", "basic_ptrac_example_decima_ascii.ptrac")

    # User query (will be ignored in demo mode)
    query = "Plot the energy distribution of neutrons"

    print(f"PTRAC file: {ptrac_path}")
    print(f"Query: {query}")
    print()
    print("[!] NOTE: In DEMO MODE, your query is ignored.")
    print("    The system returns a fixed collision analysis example.")
    print()
    print("-" * 60)
    print()

    # Initialize orchestrator
    orchestrator = CampbellOrchestrator()

    # Run analysis (demo mode will return fixed code)
    print("Running DECIMA workflow...")
    print()

    result = orchestrator.process_query(
        query=query,
        ptrac_path=ptrac_path,
        use_context=False  # No KG context in demo mode
    )

    # Display results
    print("=" * 60)
    print("DEMO MODE RESULT")
    print("=" * 60)
    print()

    if result.get('error'):
        print(f"[!] Workflow Error: {result['error']}")
        print()

    print("Explanation:")
    print("-" * 60)
    print(result.get('response', 'No explanation available'))
    print()

    print("Generated Code (Fixed Example):")
    print("-" * 60)
    print(result.get('code', 'No code generated'))
    print()

    print("=" * 60)
    print("[+] Demo Mode Example Completed!")
    print("=" * 60)
    print()
    print("[i] See examples/README.md for:")
    print("    - Comparison with other modes")
    print("    - How to enable full functionality")
    print("=" * 60)
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
