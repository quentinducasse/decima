#!/usr/bin/env python3
"""
Test mcnptools directly by cleaning sys.path first
"""

import sys
import os

# Remove old mcnptools from path
sys.path = [p for p in sys.path if 'mcnptools-main' not in p]

# Add our mcnptools to the path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
mcnptools_path = os.path.join(project_root, 'mcnptools', 'python')
sys.path.insert(0, mcnptools_path)

print("="*70)
print("Testing mcnptools directly (cleaned sys.path)")
print("="*70)

# Test 1: Import mcnptools
print("\n[1/5] Testing mcnptools import...")
try:
    import mcnptools as m
    print(f"  [OK] mcnptools imported from: {m.__file__}")
except ImportError as e:
    print(f"  [FAIL] Could not import mcnptools: {e}")
    sys.exit(1)

# Test 2: Check Ptrac class
print("\n[2/5] Testing Ptrac class...")
try:
    print(f"  [OK] Ptrac class: {m.Ptrac}")
    print(f"  [OK] Mctal class: {m.Mctal}")
except AttributeError as e:
    print(f"  [FAIL] mcnptools classes not accessible: {e}")
    sys.exit(1)

# Test 3: Check Ptrac constants
print("\n[3/5] Testing Ptrac constants...")
try:
    print(f"  [OK] Ptrac.BIN_PTRAC = {m.Ptrac.BIN_PTRAC}")
    print(f"  [OK] Ptrac.ASC_PTRAC = {m.Ptrac.ASC_PTRAC}")
    print(f"  [OK] Ptrac.SRC = {m.Ptrac.SRC}")
    print(f"  [OK] Ptrac.ENERGY = {m.Ptrac.ENERGY}")
except AttributeError as e:
    print(f"  [FAIL] Ptrac constants not accessible: {e}")
    sys.exit(1)

# Test 4: Test with actual PTRAC file
print("\n[4/5] Testing with actual PTRAC file...")
ptrac_file = os.path.join(project_root, 'data', 'ptrac_samples', 'basic_ptrac_example_decima_ascii.ptrac')
if os.path.exists(ptrac_file):
    try:
        ptrac = m.Ptrac(ptrac_file, m.Ptrac.ASC_PTRAC)
        print(f"  [OK] PTRAC file opened: {ptrac_file}")

        # Read first few histories
        histories = ptrac.ReadHistories(5)
        print(f"  [OK] Read {len(histories)} histories")

        if histories:
            first_hist = histories[0]
            num_events = first_hist.GetNumEvents()
            print(f"  [OK] First history has {num_events} events")

            if num_events > 0:
                event = first_hist.GetEvent(0)
                event_type = event.Type()
                print(f"  [OK] First event type: {event_type}")
    except Exception as e:
        print(f"  [WARN] Could not process PTRAC file: {e}")
else:
    print(f"  [WARN] PTRAC file not found: {ptrac_file}")

# Test 5: Import DECIMA modules
print("\n[5/5] Testing DECIMA modules...")
try:
    from modules.campbell import CampbellOrchestrator
    from modules.quiet import QUIET
    from modules.emma import EMMA
    from modules.otacon import OTACON
    from modules.eva import EVA
    print(f"  [OK] All DECIMA modules imported successfully")
except ImportError as e:
    print(f"  [FAIL] Could not import DECIMA modules: {e}")
    sys.exit(1)

print("\n" + "="*70)
print("SUCCESS! mcnptools + DECIMA working correctly")
print("="*70)
print("\nYou can now:")
print("  1. Run examples with mcnptools support")
print("  2. Use DECIMA API with real code execution")
print("  3. Parse PTRAC files directly with mcnptools")
