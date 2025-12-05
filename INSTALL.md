# DECIMA - Quick Installation Guide

## Prerequisites

- **Python 3.10+**
- **CMake 3.13+**: `pip install cmake`
- **C++ Compiler**:
  - Windows: Visual Studio 2022 (Community Edition)
  - Linux: GCC/G++
  - macOS: Xcode Command Line Tools
- **HDF5** (Windows): Download from https://www.hdfgroup.org/downloads/hdf5/
  - Required for mcnptools compilation
  - DLLs are automatically copied to mcnptools package during installation

---

## Installation Methods

### Method 1: Python Package (Limited - Testing Only)

**WARNING: IMPORTANT**: This method is for **testing installation** and understanding the workflow.

**For full functionality, use Method 2 (Docker) instead!**

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima

# Optional but recommended: Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
# source venv/bin/activate

python install_dev.py
```

This automatically:
1. + Compiles mcnptools C++ extension
2. + Copies HDF5 DLLs (Windows)
3. + Installs DECIMA in editable mode

**Limitations**:
- - No Neo4j Knowledge Graph (EMMA disabled)
- - Returns fixed code examples only
- - Requires manual Neo4j setup for full functionality

**Good for**: Installation testing, understanding workflow structure
**NOT for**: Real analysis (use Docker mode)

---

### Method 2: Docker (RECOMMENDED - Full Functionality)

** This is the easiest way to get DECIMA with full functionality!**

Everything is configured automatically:
- + Neo4j Knowledge Graph (EMMA agent active)
- + mcnptools pre-built and ready
- + All services configured
- + Web interface included
- + One command setup

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
cp .env.docker.example .env.docker
# Edit .env.docker to add your OpenAI API key
docker compose up -d
```

Then open http://localhost:5050 in your browser - ready to use!

---

## Verify Installation

```bash
# Test mcnptools
python examples/test_mcnptools_direct.py

# Test DECIMA + mcnptools integration
python examples/test_decima_with_mcnptools.py

# Run demo
python examples/demo_mode_standalone.py
```

Expected output:
```
======================================================================
SUCCESS! mcnptools + DECIMA working correctly
======================================================================
```

---

## Troubleshooting

### CMake not found
```bash
pip install cmake
```

### HDF5 DLLs not found (Windows)
Download and install HDF5 from: https://www.hdfgroup.org/downloads/hdf5/

Or manually copy DLLs to `mcnptools/python/mcnptools/`:
- hdf5.dll
- hdf5_cpp.dll
- hdf5_hl.dll

### Compilation fails
Check that:
1. Visual Studio 2022 is installed (Windows)
2. CMake 3.13+ is available
3. HDF5 is installed

### Import error: No module named 'mcnptools'
Run compilation first:
```bash
python setup.py build_ext --inplace
```

---

## Next Steps

- **Examples**: See [examples/README.md](examples/README.md)
- **API Usage**: See [README.md](README.md)
- **Architecture**: See [doc/architecture_decima.md](doc/architecture_decima.md)
