#!/usr/bin/env python3
"""Worker script to test a single PTRAC file"""
import sys
import json
from pathlib import Path

# Get arguments
filepath = Path(sys.argv[1])
max_histories = int(sys.argv[2])
project_root = Path(sys.argv[3])

# Setup path
sys.path.insert(0, str(project_root))

try:
    from tools.sandbox import detect_ptrac_mode
    import mcnptoolspro as m

    # Detect format based on extension and content
    filename_lower = filepath.name.lower()

    if 'h5' in filename_lower:
        # HDF5 format (reliable extension)
        format_type = 'HDF5'
        ptrac_mode = m.Ptrac.HDF5_PTRAC
        detected_mode = 'HDF5_PTRAC'
    else:
        # Use content-based detection for all other files
        # (.p, .ip, .ptrac can be either ASCII or BINARY)
        detected_mode = detect_ptrac_mode(str(filepath))

        if detected_mode == 'ASC_PTRAC':
            format_type = 'ASCII'
            ptrac_mode = m.Ptrac.ASC_PTRAC
        elif detected_mode == 'BIN_PTRAC':
            format_type = 'BINARY'
            ptrac_mode = m.Ptrac.BIN_PTRAC
        else:
            format_type = 'UNKNOWN'
            ptrac_mode = m.Ptrac.ASC_PTRAC

    # Try to open and read
    ptrac = m.Ptrac(str(filepath), ptrac_mode)
    histories = ptrac.ReadHistories(max_histories)

    events_count = 0
    if histories:
        first_hist = histories[0]
        events_count = first_hist.GetNumEvents()

    # Return success result as JSON
    result = {
        'status': 'SUCCESS',
        'format': format_type,
        'detected_mode': detected_mode,
        'histories_count': len(histories),
        'events_count': events_count,
        'error': None
    }
    print(json.dumps(result))

except Exception as e:
    # Return error result as JSON
    result = {
        'status': 'FAILED',
        'format': 'UNKNOWN',
        'detected_mode': None,
        'histories_count': 0,
        'events_count': 0,
        'error': str(e)[:150]
    }
    print(json.dumps(result))
