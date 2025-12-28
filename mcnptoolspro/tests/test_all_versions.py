"""
Test ALL PTRAC files - MCNP 6.2 and 6.3

This script tests all filter types for both MCNP versions to ensure
that code changes don't break existing functionality.

Usage:
    python test_all_versions.py

Expected behavior:
    - All MCNP 6.2 files should pass (6/6)
    - All MCNP 6.3 files except tally should pass (5/6)
    - After fixing tally support, all 6.3 files should pass (6/6)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'python'))

import mcnptoolspro as m

# Test files organized by version
test_files = {
    'MCNP 6.2': {
        'none': 'test_data/ptrac_filter_none.ip',
        'event': 'test_data/ptrac_filter_event.ip',
        'type': 'test_data/ptrac_filter_type.ip',
        'filter': 'test_data/ptrac_filter_filter.ip',
        'tally': 'test_data/ptrac_filter_tally.ip',
        'all': 'test_data/ptrac_filter_all.ip',
    },
    'MCNP 6.3': {
        'none': 'test_data/ptrac63_filter_none.ip',
        'event': 'test_data/ptrac63_filter_event.ip',
        'type': 'test_data/ptrac63_filter_type.ip',
        'filter': 'test_data/ptrac63_filter_filter.ip',
        'tally': 'test_data/ptrac63_filter_tally.ip',
        'all': 'test_data/ptrac63_filter_all.ip',
    },
}

# Expected to work (for regression detection)
expected_working = {
    'MCNP 6.2': ['none', 'event', 'type', 'filter', 'tally', 'all'],
    'MCNP 6.3': ['none', 'event', 'type', 'filter', 'tally', 'all'],  # tally now fixed!
}


def test_file(file_path):
    """Test a single PTRAC file"""
    full_path = Path(__file__).parent / file_path

    if not full_path.exists():
        return {'status': 'SKIP', 'reason': 'file not found'}

    try:
        # Test reading
        ptrac = m.Ptrac(str(full_path), m.Ptrac.ASC_PTRAC)
        histories = ptrac.ReadHistories(1)

        if len(histories) == 0:
            return {'status': 'FAIL', 'reason': 'no histories'}

        hist = histories[0]
        num_events = hist.GetNumEvents()

        if num_events == 0:
            return {'status': 'FAIL', 'reason': 'no events'}

        # Verify we can access an event
        event = hist.GetEvent(0)
        event_type = event.Type()

        return {'status': 'PASS', 'events': num_events}

    except Exception as e:
        return {'status': 'FAIL', 'reason': str(e)[:50]}


def main():
    print("=" * 80)
    print("COMPREHENSIVE TEST: MCNP 6.2 and 6.3 PTRAC FILES")
    print("=" * 80)
    print()

    all_results = {}

    for version, files in test_files.items():
        print(f"{version}")
        print("-" * 80)

        version_results = {}

        for filter_name, file_path in files.items():
            # Test all files including tally (fix attempted)
            result = test_file(file_path)
            version_results[filter_name] = result

            status = result['status']

            # Format output
            if status == 'PASS':
                events = result['events']
                status_str = f"[PASS] {events} events"
                symbol = "[OK]  "
            elif status == 'SKIP':
                status_str = f"[SKIP] {result['reason']}"
                symbol = "[--]  "
            else:  # FAIL
                status_str = f"[FAIL] {result['reason']}"
                symbol = "[XX]  "

            print(f"  {symbol}{filter_name:10s}: {status_str}")

        all_results[version] = version_results
        print()

    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    total_pass = 0
    total_fail = 0
    regressions = []
    improvements = []

    for version, results in all_results.items():
        pass_count = sum(1 for r in results.values() if r['status'] == 'PASS')
        fail_count = sum(1 for r in results.values() if r['status'] == 'FAIL')
        skip_count = sum(1 for r in results.values() if r['status'] == 'SKIP')

        total_pass += pass_count
        total_fail += fail_count

        total_tests = len(results) - skip_count

        print(f"\n{version}:")
        print(f"  PASS:    {pass_count}/{total_tests}")
        print(f"  FAIL:    {fail_count}/{total_tests}")

        # Check for regressions (expected to work but failed)
        expected = expected_working.get(version, [])
        for filter_name in expected:
            if filter_name in results and results[filter_name]['status'] != 'PASS':
                regressions.append(f"{version} {filter_name}")

        # Check for improvements (expected to fail but passed)
        for filter_name, result in results.items():
            if filter_name not in expected and result['status'] == 'PASS':
                improvements.append(f"{version} {filter_name}")

    # Regression detection
    print()
    if regressions:
        print("[WARNING] REGRESSIONS DETECTED:")
        for reg in regressions:
            print(f"  - {reg} (was working, now broken)")
        print()

    if improvements:
        print("[GOOD NEWS] IMPROVEMENTS:")
        for imp in improvements:
            print(f"  + {imp} (now working!)")
        print()

    # Overall result
    print("=" * 80)
    if regressions:
        print("[REGRESSION] Some tests that were passing are now failing!")
        print("             DO NOT COMMIT - Fix the code first")
        return_code = 2
    elif total_fail > 0:
        print("[PARTIAL] Some tests failing (may be expected)")
        print(f"          {total_pass} passing, {total_fail} failing")
        if not improvements:
            return_code = 1
        else:
            print("          But we have improvements - progress made!")
            return_code = 0
    else:
        print("[SUCCESS] All tests passing!")
        return_code = 0

    print("=" * 80)

    return return_code


if __name__ == '__main__':
    sys.exit(main())
