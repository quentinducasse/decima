"""
Compare MCNP 6.2 vs 6.3 PTRAC files
Analyzes differences in parsing output for the same filter types
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'python'))

import mcnptoolspro as m

def analyze_file(file_path):
    """Analyze a PTRAC file and return detailed info"""
    try:
        ptrac = m.Ptrac(str(file_path), m.Ptrac.ASC_PTRAC)

        # Read all histories (limited to first 10)
        histories = ptrac.ReadHistories(10)

        if len(histories) == 0:
            return None

        # Collect statistics
        total_events = 0
        event_types = {}

        for hist in histories:
            num_events = hist.GetNumEvents()
            total_events += num_events

            for i in range(num_events):
                event = hist.GetEvent(i)
                evt_type = event.Type()

                # Group by base type (1000=SRC, 2000=BNK, etc.)
                base_type = (evt_type // 1000) * 1000
                event_types[base_type] = event_types.get(base_type, 0) + 1

        return {
            'num_histories': len(histories),
            'total_events': total_events,
            'avg_events_per_history': total_events / len(histories) if histories else 0,
            'event_types': event_types,
        }

    except Exception as e:
        return {'error': str(e)}

def compare_filter(filter_name):
    """Compare a specific filter between MCNP 6.2 and 6.3"""
    test_dir = Path(__file__).parent / 'test_data'

    file_62 = test_dir / f'ptrac_filter_{filter_name}.ip'
    file_63 = test_dir / f'ptrac63_filter_{filter_name}.ip'

    results = {}

    # Analyze MCNP 6.2
    if file_62.exists():
        results['6.2'] = analyze_file(file_62)
    else:
        results['6.2'] = {'error': 'file not found'}

    # Analyze MCNP 6.3
    if file_63.exists():
        results['6.3'] = analyze_file(file_63)
    else:
        results['6.3'] = {'error': 'file not found'}

    return results

def format_event_types(event_types):
    """Format event types dictionary for display"""
    type_names = {
        1000: 'SRC',
        2000: 'BNK',
        2030: 'BNK*',  # New in MCNP 6.3?
        3000: 'SUR',
        4000: 'COL',
        5000: 'TER',
        9000: 'LST',
    }

    parts = []
    for evt_type in sorted(event_types.keys()):
        count = event_types[evt_type]
        name = type_names.get(evt_type, f'TYPE_{evt_type}')
        parts.append(f'{name}:{count}')

    return ', '.join(parts)

def main():
    print("=" * 80)
    print("MCNP 6.2 vs 6.3 COMPARISON")
    print("=" * 80)
    print()

    filters = ['none', 'event', 'type', 'filter']

    for filter_name in filters:
        print(f"Filter: {filter_name.upper()}")
        print("-" * 80)

        results = compare_filter(filter_name)

        # Display MCNP 6.2 results
        result_62 = results['6.2']
        if result_62 and 'error' not in result_62:
            print(f"  MCNP 6.2:")
            print(f"    Histories:     {result_62['num_histories']}")
            print(f"    Total events:  {result_62['total_events']}")
            print(f"    Avg/history:   {result_62['avg_events_per_history']:.1f}")
            print(f"    Event types:   {format_event_types(result_62['event_types'])}")
        else:
            print(f"  MCNP 6.2: {result_62.get('error', 'unknown error')}")

        print()

        # Display MCNP 6.3 results
        result_63 = results['6.3']
        if result_63 and 'error' not in result_63:
            print(f"  MCNP 6.3:")
            print(f"    Histories:     {result_63['num_histories']}")
            print(f"    Total events:  {result_63['total_events']}")
            print(f"    Avg/history:   {result_63['avg_events_per_history']:.1f}")
            print(f"    Event types:   {format_event_types(result_63['event_types'])}")
        else:
            print(f"  MCNP 6.3: {result_63.get('error', 'unknown error')}")

        print()

        # Display differences
        if result_62 and 'error' not in result_62 and result_63 and 'error' not in result_63:
            diff_events = result_63['total_events'] - result_62['total_events']
            diff_pct = (diff_events / result_62['total_events'] * 100) if result_62['total_events'] > 0 else 0

            print(f"  DIFFERENCE:")
            print(f"    Total events:  {diff_events:+d} ({diff_pct:+.1f}%)")

            # Compare event types
            all_types = set(result_62['event_types'].keys()) | set(result_63['event_types'].keys())
            type_diffs = []
            for evt_type in sorted(all_types):
                count_62 = result_62['event_types'].get(evt_type, 0)
                count_63 = result_63['event_types'].get(evt_type, 0)
                if count_62 != count_63:
                    type_names = {1000: 'SRC', 2000: 'BNK', 2030: 'BNK*', 3000: 'SUR', 4000: 'COL', 5000: 'TER', 9000: 'LST'}
                    name = type_names.get(evt_type, f'TYPE_{evt_type}')
                    type_diffs.append(f'{name}:{count_63-count_62:+d}')

            if type_diffs:
                print(f"    Event types:   {', '.join(type_diffs)}")

        print()
        print("=" * 80)
        print()

    print()
    print("NOTES:")
    print("  - Event type 2030 appears to be new in MCNP 6.3")
    print("  - Differences in event counts are expected (different simulations)")
    print("  - The important thing is that parsing works correctly for both versions")
    print()

if __name__ == '__main__':
    sys.exit(main())
