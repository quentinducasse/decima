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

### Method 1: One-Command Install (Recommended for Development)

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
1. ✅ Compiles mcnptools C++ extension
2. ✅ Copies HDF5 DLLs (Windows)
3. ✅ Installs DECIMA in editable mode

**Note**: Using a virtual environment is recommended to avoid dependency conflicts with other Python projects.

---

### Method 2: Manual Install (Two Steps)

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima

# Optional: Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/macOS

# Step 1: Compile mcnptools
python setup.py build_ext --inplace

# Step 2: Install DECIMA
pip install -e .
```

---

### Method 3: Regular Install (Non-Editable)

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima

# Optional: Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/macOS

pip install .  # Without -e
```

This triggers CMake compilation automatically, but you won't be able to edit the code.

---

### Method 4: Docker (No Local Installation)

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
cp .env.docker.example .env.docker
# Edit .env.docker to add your OpenAI API key
docker compose up -d
```

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
