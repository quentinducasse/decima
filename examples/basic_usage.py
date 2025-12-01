#!/usr/bin/env python3
"""
DECIMA Basic Usage Example

This example demonstrates how to use DECIMA as a Python library
to analyze MCNP PTRAC files programmatically

NOTE: Environment variables must be loaded BEFORE importing DECIMA modules,
because modules like otacon.py read DEMO_MODE at import time
"""

import os
import sys


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# IMPORTANT: Load .env file BEFORE importing DECIMA modules!
# The modules read environment variables at import time.
# ============================================================
from dotenv import load_dotenv

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_local = os.path.join(project_root, ".env.local")
env_docker = os.path.join(project_root, ".env.docker")

if os.path.exists(env_local):
    load_dotenv(env_local, override=True)
    print(f"[ENV] Loaded: {env_local}")
elif os.path.exists(env_docker):
    load_dotenv(env_docker, override=True)
    print(f"[ENV] Loaded: {env_docker}")
else:
    load_dotenv(override=True)
    print("[ENV] Loaded: default .env")


from modules.campbell import CampbellOrchestrator


def print_emma_context(result):
    """Display EMMA Knowledge Graph context in verbose mode."""
    print("\n" + "=" * 60)
    print(" EMMA - Knowledge Graph Context")
    print("=" * 60)

    context = result.get('context', {})

    #  map from QUIET
    focus_map = context.get('focus_map', {})
    if focus_map:
        print("\n QUIET Focus Detection:")
        for key, values in focus_map.items():
            if values and values != ['']:
                print(f"   • {key}: {values}")

    # Entities extracted from KG
    entities = context.get('entities', [])
    if entities:
        print(f"\n Entities Extracted from KG ({len(entities)} total):")
        print("-" * 60)
        for ent in entities:
            # Build entity string
            parts = [f"id: {ent.get('id', 'N/A')}"]

            if ent.get('type'):
                parts.append(f"type: {ent['type']}")

            if ent.get('focus_type'):
                parts.append(f"matched_by: {','.join(ent['focus_type'])}")

            if ent.get('parent_class'):
                parts.append(f"parent_class: {ent['parent_class']}")

            if ent.get('parent_enum'):
                parts.append(f"parent_enum: {ent['parent_enum']}")

            if ent.get('parent_dict'):
                parts.append(f"parent_dict: {ent['parent_dict']}")

            if ent.get('value') is not None:
                parts.append(f"value: {ent['value']}")

            if ent.get('score') is not None:
                parts.append(f"score: {ent['score']}")

            desc = ent.get('description', '')
            if desc:
                # Truncate long descriptions
                desc_short = desc.strip().replace('\n', ' ')[:100]
                parts.append(f"desc: {desc_short}...")

            print(f"   • {', '.join(parts)}")
    else:
        print("\n  No entities extracted from Knowledge Graph")

    print("=" * 60)


def main():
    print("=" * 60)
    print("DECIMA - Basic Usage Example (Verbose Mode)")
    print("=" * 60)

    # Check API key
    api_key = os.getenv('OPENAI_API_KEY')
    demo_mode = os.getenv('DEMO_MODE', 'false').lower() == 'true'

    if not api_key:
        print("\n  OPENAI_API_KEY not found")
        print("Please set your API key in .env.docker file")
        return

    print(f"\n API key found: {api_key[:20]}...")
    print(f"   LLM Provider: {os.getenv('LLM_PROVIDER', 'openai')}")
    print(f"   Demo mode: {demo_mode}")
    print("-" * 60)

    # Path to sample PTRAC file - use ABSOLUTE path
    ptrac_path = os.path.join(project_root, "data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac")

    if not os.path.exists(ptrac_path):
        print(f"\n  PTRAC file not found: {ptrac_path}")
        return

    print(f" PTRAC file: {ptrac_path}")

    # Initialize orchestrator 
    orchestrator = CampbellOrchestrator()

    # Run analysis
    query = "Plot the z-axis direction cosine (W) distribution of emitted source particles"
    print(f"\n Query: {query}")
    print("-" * 60)

    result = orchestrator.process_query(
        query=query,
        ptrac_path=ptrac_path,
        use_context=True
    )

    # ============================================================
    # Display EMMA Knowledge Graph Context (verbose)
    # ============================================================
    print_emma_context(result)

    # ============================================================
    # Display OTACON LLM Response
    # ============================================================
    print("\n" + "=" * 60)
    print(" OTACON - LLM Response")
    print("=" * 60)

    print("\n Explanation:")
    print(result.get('response', 'N/A'))

    print("\n Generated Code:")
    print("-" * 60)
    print(result.get('code', 'N/A'))

    # ============================================================
    # Display EVA Execution Results
    # ============================================================
    print("\n" + "=" * 60)
    print("⚡ EVA - Code Execution")
    print("=" * 60)

    exec_result = result.get('execution_result', {})
    if exec_result:
        print("\n Stdout:")
        stdout = exec_result.get('stdout', '')
        if stdout:
            print(stdout[:2000])  # Limit output
            if len(stdout) > 2000:
                print(f"... [truncated, total {len(stdout)} chars]")
        else:
            print("(empty)")

        stderr = exec_result.get('stderr', '')
        if stderr:
            print("\n Stderr:")
            print(stderr)

        if exec_result.get('output_files'):
            print(f"\n Output files: {exec_result['output_files']}")
    else:
        print("\n(No execution result)")

    # ============================================================
    # Workflow Summary
    # ============================================================
    print("\n" + "=" * 60)
    print(" Workflow Logs")
    print("=" * 60)
    for log in result.get('logs', []):
        print(f"   {log}")

    if result.get('error'):
        print(f"\n Error: {result['error']}")

    print("\n" + "=" * 60)
    print(" Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
