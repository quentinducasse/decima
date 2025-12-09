#!/usr/bin/env python3
"""
DECIMA Development Installation Script
========================================

This script automates the installation of DECIMA in editable mode with mcnptools compilation.

Usage:
    python install_dev.py

What it does:
    1. Compiles mcnptools C++ extension with CMake (supports ASCII PTRAC files)
    2. Copies HDF5 DLLs if available (Windows only, optional - for HDF5 PTRAC support)
    3. Installs DECIMA in editable mode (pip install -e .)
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{'='*70}")
    print(f"{description}")
    print(f"{'='*70}")
    print(f"Command: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n[ERROR] {description} failed!")
        sys.exit(1)

    print(f"\n[OK] {description} completed successfully")
    return result

def main():
    print("="*70)
    print("DECIMA Development Installation")
    print("="*70)
    print()
    print("This will:")
    print("  1. Install build dependencies (setuptools, wheel)")
    print("  2. Compile mcnptools C++ extension (takes a few minutes)")
    print("  3. Copy HDF5 DLLs if available (Windows, optional)")
    print("  4. Install DECIMA in editable mode")
    print()

    # Check if we're in the right directory
    if not os.path.exists('setup.py'):
        print("[ERROR] setup.py not found!")
        print("Please run this script from the DECIMA root directory.")
        sys.exit(1)

    # Step 1: Install build dependencies
    run_command(
        [sys.executable, '-m', 'pip', 'install', 'setuptools', 'wheel'],
        "Step 1/3: Installing build dependencies"
    )

    # Step 2: Build mcnptools extension
    run_command(
        [sys.executable, 'setup.py', 'build_ext', '--inplace'],
        "Step 2/3: Building mcnptools C++ extension"
    )

    # Step 3: Install DECIMA in editable mode
    run_command(
        [sys.executable, '-m', 'pip', 'install', '-e', '.'],
        "Step 3/3: Installing DECIMA in editable mode"
    )

    print()
    print("="*70)
    print("Installation completed successfully!")
    print("="*70)
    print()
    print("You can now:")
    print("  1. Import DECIMA: from modules.campbell import CampbellOrchestrator")
    print("  2. Import mcnptools: import mcnptools")
    print("  3. Run examples: python examples/test_decima_with_mcnptools.py")
    print()
    print("To test the installation:")
    print("  python test_mcnptools_direct.py")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[CANCELLED] Installation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n[ERROR] Installation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
