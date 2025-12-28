"""
Test mcnptoolspro with MCNP 6.3 PTRAC files

This script tests all filter types with MCNP 6.3 generated files
to verify compatibility between MCNP 6.2 and 6.3 formats.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'python'))

import mcnptoolspro as m

# Test files (MCNP 6.3)
test_files = {
    'none': 'test_data/ptrac63_filter_none.ip',
    'event': 'test_data/ptrac63_filter_event.ip',
    'type': 'test_data/ptrac63_filter_type.ip',
    'filter': 'test_data/ptrac63_filter_filter.ip',
    'tally': 'test_data/ptrac63_filter_tally.ip',
    'all': 'test_data/ptrac63_filter_all.ip',
}

def test_filter(filter_name, file_path):
    """Test reading a single PTRAC file"""
    full_path = Path(__file__).parent / file_path

    if not full_path.exists():
        return f"SKIP (file not found: {file_path})"

    try:
        # Open PTRAC file
        ptrac = m.Ptrac(str(full_path), m.Ptrac.ASC_PTRAC)

        # Read first history
        histories = ptrac.ReadHistories(1)

        if len(histories) == 0:
            return "FAIL (no histories read)"

        # Count events
        hist = histories[0]
        num_events = hist.GetNumEvents()

        # Verify we can access events
        if num_events > 0:
            event = hist.GetEvent(0)
            event_type = event.Type()

        return f"OK ({num_events} events)"

    except Exception as e:
        return f"FAIL ({str(e)})"

def main():
    print("=" * 80)
    print("TESTING MCNP 6.3 COMPATIBILITY")
    print("=" * 80)
    print()

    results = {}
    all_passed = True

    for filter_name, file_path in test_files.items():
        result = test_filter(filter_name, file_path)
        results[filter_name] = result

        status = "[OK]" if result.startswith("OK") else "[FAIL]"
        print(f"  {status} Testing filter: {filter_name:10s} ... {result}")

        if not result.startswith("OK") and not result.startswith("SKIP"):
            all_passed = False

    print()
    print("=" * 80)

    if all_passed:
        print("[OK] ALL TESTS PASSED - MCNP 6.3 files are compatible!")
    else:
        print("[FAIL] SOME TESTS FAILED - See details above")

    print("=" * 80)

    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())
