#!/usr/bin/env python3
"""
DECIMA Demo Mode - Standalone Example
======================================

This example demonstrates DECIMA in DEMO_MODE with LIMITED functionality:
- + Works without OpenAI API (no costs)
- + Works without Neo4j Knowledge Graph
- - Returns FIXED code example (DEMO_MODE=true, ignores your query)
- - No intelligent code generation
- - No MCNP domain context from Knowledge Graph

NOTE: Even with OpenAI API (DEMO_MODE=false), without Neo4j Knowledge Graph,
OTACON may generate code with errors due to missing MCNP domain context.

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
# IMPORTANT: Set DEMO_MODE BEFORE importing DECIMA modules
# ============================================================
os.environ['DEMO_MODE'] = 'true'
os.environ['OPENAI_API_KEY'] = ''  # Empty - not needed in demo mode
os.environ['NEO4J_URI'] = 'bolt://localhost:7687'  # Not used in demo mode
os.environ['NEO4J_USER'] = 'neo4j'
os.environ['NEO4J_PASSWORD'] = 'neo4j'

print("=" * 70)
print("  DECIMA - DEMO MODE (LIMITED FUNCTIONALITY)")
print("=" * 70)
print()
print("WARNING: WARNING: This is a LIMITED demo version")
print()
print("   + Works without OpenAI API")
print("   + Works without Neo4j Knowledge Graph")
print("   - Returns FIXED code example (ignores your query)")
print("   - No intelligent code generation")
print("   - No MCNP domain knowledge context")
print()
print("💡 For FULL functionality with intelligent code generation:")
print("   → Use Docker mode: docker compose up -d")
print("   → See INSTALL.md for setup instructions")
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
    print(f"📂 PTRAC file: {ptrac_path}")
    print(f"Query: {query}")
    print()
    print("WARNING: IMPORTANT: In DEMO MODE, your query is IGNORED")
    print("   The system always returns the same fixed collision analysis code.")
    print()
    print("   To get intelligent code generation that answers YOUR query,")
    print("   use Docker mode with OpenAI API and Neo4j Knowledge Graph.")
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
        use_context=False  # No KG context in demo mode
    )

    # Display results
    print("=" * 70)
    print("  DEMO MODE RESULT (FIXED EXAMPLE - NOT YOUR QUERY)")
    print("=" * 70)
    print()

    if result.get('error'):
        print(f"- Workflow Error: {result['error']}")
        print()

    print("💬 Explanation:")
    print("-" * 70)
    print(result.get('response', 'No explanation available'))
    print()

    print("💻 Generated Code (FIXED - Same for all queries):")
    print("-" * 70)
    print(result.get('code', 'No code generated'))
    print()

    print("=" * 70)
    print("  + Demo Mode Example Completed")
    print("=" * 70)
    print()
    print("WARNING: LIMITATIONS OF THIS DEMO MODE:")
    print("   • This demo always returns the SAME code (collision analysis)")
    print("   • Your query was IGNORED")
    print("   • No intelligent code generation")
    print("   • No MCNP Knowledge Graph context")
    print()
    print("💡 TO GET FULL FUNCTIONALITY:")
    print("   • Intelligent code generation for YOUR queries")
    print("   • MCNP domain knowledge from Knowledge Graph")
    print("   • Context-aware code with proper syntax")
    print()
    print("   → Use Docker mode: docker compose up -d")
    print("   → See INSTALL.md Method 2")
    print("   → See examples/README.md for comparison")
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
