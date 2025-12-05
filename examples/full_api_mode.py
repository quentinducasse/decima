#!/usr/bin/env python3
"""
DECIMA Full API Mode - Complete Example
========================================

WARNING: IMPORTANT: This mode requires Neo4j Knowledge Graph for full functionality!

Without Neo4j:
- EMMA (Knowledge Graph agent) is disabled
- OTACON generates code WITHOUT MCNP domain context
- Generated code may have errors (wrong classes, methods, syntax)
- Limited functionality

With DEMO_MODE=true (no API key):
- Returns fixed code examples (ignores your query)

RECOMMENDED: Use Docker mode for easiest setup with full functionality:
  → docker compose up -d
  → See INSTALL.md Method 2

This Python package mode is for developers who want to:
- Run DECIMA programmatically with their own Neo4j instance
- Integrate DECIMA into custom workflows
- Develop and debug DECIMA modules

Prerequisites for FULL functionality:
1. Install DECIMA: python install_dev.py
2. Start Neo4j: docker compose up -d neo4j (or Neo4j Desktop)
3. Load Knowledge Graph: docker compose run --rm app python kg/loader/neo4j_loader.py
4. Configure .env.local with:
   - OPENAI_API_KEY=sk-...
   - NEO4J_URI=bolt://localhost:7687
   - NEO4J_USER=neo4j
   - NEO4J_PASSWORD=decima123

See examples/README.md for detailed comparison of modes.
"""

import os
import sys

# Add project root to path
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# IMPORTANT: Load .env file BEFORE importing DECIMA modules
# ============================================================
from dotenv import load_dotenv

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_docker = os.path.join(project_root, ".env.docker")
env_local = os.path.join(project_root, ".env.local")

# Priority: .env.docker > .env.local > default .env
if os.path.exists(env_docker):
    load_dotenv(env_docker, override=True)
    print(f"[ENV] Loaded: {env_docker}")
elif os.path.exists(env_local):
    load_dotenv(env_local, override=True)
    print(f"[ENV] Loaded: {env_local}")
else:
    load_dotenv(override=True)
    print("[ENV] Loaded: default .env")

# Override Neo4j URI for local execution (not in Docker)
os.environ['NEO4J_URI'] = 'bolt://localhost:7687'
print("[INFO] Neo4j URI set to localhost:7687 (for local execution)")

# Check if we need to enable DEMO_MODE
api_key = os.getenv('OPENAI_API_KEY', '')
invalid_keys = ['', 'your_openai_api_key_here', 'your_key_here', 'sk-placeholder']
if not api_key or api_key.lower().strip() in invalid_keys:
    os.environ['DEMO_MODE'] = 'true'
    print("[WARNING] No valid API key found - enabling DEMO_MODE")
    print("          Set OPENAI_API_KEY in .env.docker for full functionality")
print()

from modules.campbell import CampbellOrchestrator


def main():
    """Run DECIMA with full API and Knowledge Graph context."""

    print("=" * 70)
    print("  DECIMA - Full API Mode (Python Package)")
    print("=" * 70)
    print()

    # Check configuration
    demo_mode = os.getenv('DEMO_MODE', 'false').lower() == 'true'
    has_valid_key = api_key and api_key.lower().strip() not in invalid_keys

    print("📋 Configuration Status:")
    print()
    if has_valid_key:
        print(f"   + OpenAI API: {api_key[:20]}...")
    else:
        print("   - OpenAI API: NOT SET")
        print("      → Will use DEMO_MODE (fixed responses)")

    neo4j_uri = os.getenv('NEO4J_URI')
    print(f"   WARNING: Neo4j URI: {neo4j_uri}")
    print("      → Neo4j must be running for Knowledge Graph!")
    print(f"   Demo Mode: {demo_mode}")
    print()

    if demo_mode:
        print("WARNING: WARNING: DEMO_MODE is active")
        print("   → Returns fixed collision analysis code")
        print("   → EMMA Knowledge Graph disabled")
        print()
        print("   To enable full functionality:")
        print("   1. Set OPENAI_API_KEY in .env.local")
        print("   2. Start Neo4j: docker compose up -d neo4j")
        print("   3. Load KG: docker compose run --rm app python kg/loader/neo4j_loader.py")
        print()

    print("💡 TIP: For easier setup, use Docker mode instead:")
    print("   → docker compose up -d")
    print("   → Everything configured automatically!")
    print()
    print("=" * 70)
    print()

    # Sample PTRAC file
    ptrac_path = os.path.join(project_root, "data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac")

    if not os.path.exists(ptrac_path):
        print(f"[!] PTRAC file not found: {ptrac_path}")
        return

    print(f"PTRAC file: {ptrac_path}")

    # User query
    query = "Calculate the average energy of collision events for the first 10 histories"
    print(f"Query: {query}")
    print()

    # Initialize orchestrator
    orchestrator = CampbellOrchestrator()

    # Run analysis with Knowledge Graph context
    print("Running DECIMA workflow (with Knowledge Graph context)...")
    print()

    result = orchestrator.process_query(
        query=query,
        ptrac_path=ptrac_path,
        use_context=True  # Use EMMA Knowledge Graph
    )

    # Display results
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)
    print()

    if result.get('error'):
        print(f"[!] Workflow Error: {result['error']}")
        print()

    # EMMA Context (if available)
    context = result.get('context', {})
    if context.get('entities'):
        print(f"Knowledge Graph Context: {len(context['entities'])} entities extracted")
        print()

    # OTACON Response
    print("Explanation:")
    print("-" * 60)
    print(result.get('response', 'No explanation available'))
    print()

    print("Generated Code:")
    print("-" * 60)
    print(result.get('code', 'No code generated'))
    print()

    # EVA Execution
    exec_result = result.get('execution_result', {})
    if exec_result:
        print("Execution Output:")
        print("-" * 60)
        stdout = exec_result.get('stdout', '')
        if stdout:
            print(stdout[:1000])  # Limit output
            if len(stdout) > 1000:
                print(f"... [truncated, total {len(stdout)} chars]")
        else:
            print("(empty)")

        stderr = exec_result.get('stderr', '')
        if stderr:
            print()
            print("WARNING: Execution Errors:")
            print(stderr)
            print()
            print("💡 If you see errors like 'AttributeError', 'NameError', or wrong methods:")
            print("   → This is likely due to MISSING Knowledge Graph context!")
            print("   → OTACON generated code without MCNP domain knowledge")
            print("   → Solution: Start Neo4j and load KG, or use Docker mode")
        print()

    # Workflow logs
    if result.get('logs'):
        print("Workflow Logs:")
        print("-" * 60)
        for log in result['logs']:
            print(f"   {log}")
        print()

    print("=" * 70)
    print("  + Full API Mode Example Completed")
    print("=" * 70)
    print()
    print("WARNING: PYTHON PACKAGE MODE LIMITATIONS:")
    print("   • Requires manual Neo4j setup (or Docker for Neo4j only)")
    print("   • Without Neo4j: EMMA disabled, limited functionality")
    print("   • Manual environment configuration needed")
    print()
    print("💡 FOR EASIER FULL FUNCTIONALITY:")
    print("   → Use Docker mode: docker compose up -d")
    print("   → Neo4j + mcnptools + all services configured automatically")
    print("   → See INSTALL.md Method 2")
    print()
    print("=" * 70)


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
        print("   1. Neo4j not running:")
        print("      - Start Neo4j: docker compose up -d neo4j")
        print("      - Load KG: docker compose run --rm app python kg/loader/neo4j_loader.py")
        print()
        print("   2. Invalid API key:")
        print("      - Set OPENAI_API_KEY in .env.local")
        print()
        print("   3. Too complex to setup?")
        print("      - Use Docker mode instead: docker compose up -d")
        print("      - See INSTALL.md Method 2 (everything automatic!)")
        print()
        print("=" * 70)
        sys.exit(1)
