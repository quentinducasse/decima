# DECIMA - Installation Guide

This guide covers two installation methods for DECIMA.

---

## Prerequisites (ALL METHODS)

### Step 1: Clone the Repository

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
```

### Step 2: Configure Environment

**IMPORTANT**: All methods require configuring `.env.docker` first.

Copy the environment template:

**Unix systems (Linux/macOS):**
```bash
cp .env.docker.example .env.docker
```

**Windows systems:**
```bash
copy .env.docker.example .env.docker
```

Edit `.env.docker` with your configuration:

```env
# LLM Provider Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here        # <- Insert your OpenAI API key here

# Neo4j Configuration (keep defaults)
NEO4J_URI=bolt://neo4j:7687              # For Docker mode
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123

# Demo mode flag
DEMO_MODE=false                          # false = use API, true = fixed code examples
```

**About DEMO_MODE:**
- `DEMO_MODE=false` (default): Uses OpenAI API for intelligent code generation
- `DEMO_MODE=true`: Returns fixed code examples (no API costs, no custom code)
- If `OPENAI_API_KEY` is empty or invalid, automatically enables DEMO_MODE

---

## Which Installation Method to Choose?

### Method 1: Python Package (LIMITED - Testing Only)
- **Use for**: Testing installation, understanding workflow
- **Limitations**: No Neo4j (EMMA disabled)
- **With DEMO_MODE=true**: Returns fixed code examples
- **With DEMO_MODE=false**: Calls API but may generate code with errors (no KG context)
- **Good for**: Developers wanting to test mcnptools compilation
- **NOT for**: Real analysis

### Method 2: Docker (RECOMMENDED - Full Functionality)
- **Use for**: Production analysis, full DECIMA experience
- **Advantages**: Everything automatic, Neo4j + mcnptools included
- **Full functionality**: Always works correctly
- **Good for**: Everyone who wants the complete system
- **Best for**: Real PTRAC analysis work

**TLDR: Use Docker mode unless you specifically need to test the Python package installation.**

---

## Method 1: Python Package Installation

### Prerequisites

- **Python 3.10+**
- **CMake 3.13+**: `pip install cmake`
- **C++ Compiler**:
  - Windows: Visual Studio 2022 (Community Edition)
  - Linux: GCC/G++
  - macOS: Xcode Command Line Tools
- **HDF5** (Windows): Download from https://www.hdfgroup.org/downloads/hdf5/
  - Required for mcnptools compilation
  - DLLs are automatically copied to mcnptools package during installation

### Installation Steps

```bash
# Already done in Prerequisites: clone + configure .env.docker

# Optional but recommended: Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install DECIMA (compiles mcnptools automatically)
python install_dev.py
```

This automatically:
1. Compiles mcnptools C++ extension
2. Copies HDF5 DLLs (Windows)
3. Installs DECIMA in editable mode

### Verify Installation

```bash
# Test mcnptools compilation
python examples/test_mcnptools_direct.py

# Test DECIMA + mcnptools integration
python examples/test_decima_with_mcnptools.py

# Run demo - automatically uses settings from .env.docker
python examples/demo_mode_standalone.py
```

Expected output:
```
======================================================================
SUCCESS! mcnptools + DECIMA working correctly
======================================================================
```

### Understanding Behavior Based on .env.docker

The examples automatically detect settings from `.env.docker`:

**If DEMO_MODE=true in .env.docker:**
- Uses fixed code examples (no API calls)
- Your query is ignored
- No costs
- Print: "Using DEMO_MODE: returning fixed code example"

**If DEMO_MODE=false in .env.docker:**
- Calls OpenAI API for code generation
- Generates code for YOUR query
- BUT: Without Neo4j, generated code may have errors (missing MCNP context)
- If execution fails: "Possible cause: missing Knowledge Graph context. Use Docker mode."
- Print: "Using OpenAI API (DEMO_MODE=false)"

### Limitations of Python Package Mode

**WITHOUT Neo4j Knowledge Graph:**
- EMMA (Knowledge Graph agent) is disabled
- DEMO_MODE=true: Returns fixed code examples
- DEMO_MODE=false: May generate code with errors (missing MCNP domain context)
- No intelligent code generation with proper MCNP syntax

**To get full functionality**, you need to:
1. Manually setup Neo4j (requires Docker anyway!)
2. Load the Knowledge Graph
3. Configure environment variables

**RECOMMENDATION**: If you need Neo4j anyway, just use Method 2 (Docker) - it's easier!

### Troubleshooting Python Package

**CMake not found:**
```bash
pip install cmake
```

**HDF5 DLLs not found (Windows):**
Download and install HDF5 from: https://www.hdfgroup.org/downloads/hdf5/

Or manually copy DLLs to `mcnptools/python/mcnptools/`:
- hdf5.dll
- hdf5_cpp.dll
- hdf5_hl.dll

**Compilation fails:**
Check that:
1. Visual Studio 2022 is installed (Windows)
2. CMake 3.13+ is available
3. HDF5 is installed

**Import error: No module named 'mcnptools':**
Run compilation first:
```bash
python setup.py build_ext --inplace
```

**PYTHONPATH conflicts breaking venv isolation:**

**Symptom:** Code execution fails with numpy import errors like:
```
ModuleNotFoundError: No module named 'numpy.core._multiarray_umath'
The NumPy version is: "1.20.3"  # Wrong version being loaded
```

**Cause:** Global `PYTHONPATH` environment variable forces Python to load packages from system-wide locations (e.g., `~/.local/lib/python3.8/site-packages`) instead of the virtual environment, causing version conflicts.

**Solution - Temporary (Quick Fix):**
```bash
# Unset PYTHONPATH before activating venv
unset PYTHONPATH
source venv/bin/activate
python3.10 examples/demo_mode_standalone.py
```
---

## Method 2: Docker Installation (RECOMMENDED)

### Prerequisites

#### Required Software
- **Docker**: https://docs.docker.com/get-docker/
  - Windows/macOS: Docker Desktop
  - Linux: Docker Engine

#### API Keys
- **OpenAI API Key** (Recommended): Get one at https://platform.openai.com/api-keys
- **Note**: Demo mode available without API key (see below)

#### Important Notes for Linux Users
You might need to run Docker commands with `sudo` unless you've added your user to the Docker group.

See: https://docs.docker.com/engine/install/linux-postinstall/

### Installation Steps

#### Step 1: Clone the Repository

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
```

#### Step 2: Configure Environment

Copy the Docker environment template:

**Unix systems (Linux/macOS):**
```bash
cp .env.docker.example .env.docker
```

**Windows systems:**
```bash
copy .env.docker.example .env.docker
```

Edit `.env.docker` with your configuration:

```env
# LLM Provider Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here        # <- Insert your OpenAI API key here

# Neo4j Configuration (keep defaults)
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123

# Demo mode flag (set to true for fallback without API key)
DEMO_MODE=false
```

**About DEMO_MODE:**
- `DEMO_MODE=false` (default): Uses OpenAI API for intelligent code generation
- `DEMO_MODE=true`: Returns fixed code examples (no API costs, no custom code)
- If `OPENAI_API_KEY` is empty or invalid, automatically enables DEMO_MODE

#### Step 3: Build and Launch

Before running these commands:
- **Windows** → Start Docker Desktop application
- **Linux** → Ensure Docker daemon is running: `sudo systemctl start docker`

```bash
# Build the containers (first time only, takes ~5 minutes)
docker compose build app

# Start all services
docker compose up -d
```

This automatically:
- Starts a Neo4j container (ports 7474 + 7687)
- Starts the DECIMA web server (port 5050)
- Mounts your local source code into the container
- Configures all services

Wait ~15 seconds for Neo4j to fully start.

#### Step 4: Load the Knowledge Graph

```bash
# Load MCNP Knowledge Graph into Neo4j
docker compose exec app python kg/loader/neo4j_loader.py
```

Expected output:
```
Loading MCNP Knowledge Graph...
Loaded X nodes and Y relationships
Knowledge Graph ready!
```

#### Step 5: Access the Application

After all containers are running, access DECIMA:

- **DECIMA Web App**: http://localhost:5050
- **Neo4j Browser**: http://localhost:7474 (optional, for inspection)

**Neo4j Login Credentials** (if accessing browser):
- Username: `neo4j`
- Password: `decima123`

---

## Daily Usage (Docker Mode)

### Standard Mode

Start the entire DECIMA stack:
```bash
docker compose up -d
```

Load or reload the Knowledge Graph (required after Neo4j restarts):
```bash
docker compose exec app python kg/loader/neo4j_loader.py
```

Stop all services when done:
```bash
docker compose down
```

### Debug/Verbose Mode

For development or troubleshooting, use verbose mode:

```bash
# Start only Neo4j in the background
docker compose up -d neo4j

# Wait ~15 seconds for Neo4j to be ready

# Load the Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py

# Run the application with detailed logs
docker compose run --rm --service-ports app python app.py -v
```

**Debug/Verbose mode provides:**
- Full logs and debug information
- Context sent to the LLM is visible
- Detailed workflow inspection
- Real-time request/response monitoring

Access at: http://localhost:5050

---

## Troubleshooting

### Docker Issues

**Permission denied (Linux):**
```bash
# Option 1: Use sudo
sudo docker compose up -d

# Option 2: Add user to docker group (permanent solution)
sudo usermod -aG docker $USER
# Then logout and login again
```

**Port conflicts:**
```bash
# Check what's using the ports
# Linux/macOS:
netstat -tulpn | grep :5050
netstat -tulpn | grep :7474
netstat -tulpn | grep :7687

# Windows:
netstat -ano | findstr :5050
netstat -ano | findstr :7474
netstat -ano | findstr :7687

# Solution: Stop conflicting services or change ports in docker-compose.yml
```

**Build failures:**
```bash
# Clean rebuild
docker compose down
docker compose build --no-cache app
docker compose up -d
```

### Neo4j Issues

**Connection refused:**
```bash
# Check if Neo4j is running
docker compose ps

# Check Neo4j logs
docker compose logs neo4j

# Wait for "Started" message in logs
docker compose logs -f neo4j

# Restart Neo4j if needed
docker compose restart neo4j
```

**Knowledge Graph not loading:**
```bash
# Ensure Neo4j is fully started (wait ~15 seconds after docker compose up -d)

# Reload the KG
docker compose exec app python kg/loader/neo4j_loader.py

# If that fails, check Neo4j browser at http://localhost:7474
# Run: MATCH (n) RETURN count(n)
# Should show nodes in database
```

### API Key Issues

**Invalid API key error:**
- Verify your OpenAI API key is correct (starts with `sk-`)
- Check you have sufficient credits on your OpenAI account
- Ensure no extra spaces in `.env.docker`
- Key format: `OPENAI_API_KEY=sk-proj-...` (no quotes)

**Want to test without API key:**
Edit `.env.docker`:
```bash
DEMO_MODE=true
OPENAI_API_KEY=

# Or simply leave OPENAI_API_KEY empty for automatic demo mode
```

Then restart:
```bash
docker compose down
docker compose up -d
docker compose exec app python kg/loader/neo4j_loader.py
```

**API rate limits:**
- Use `gpt-4o-mini` model (cheaper, faster)
- Costs ~$0.001 per query with mini model
- Monitor usage at https://platform.openai.com/usage

---

## Getting Started (Docker Mode)

After successful installation, visit http://localhost:5050 to see the DECIMA interface.

### 1. Test with Sample Data

Use the provided PTRAC file:
- Path: `data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac`
- Format: ASCII (ready to use immediately)

### 2. Load Your Own PTRAC File

- Click "Load PTRAC File" button in the interface
- Supports both binary and ASCII PTRAC formats
- File will be uploaded and ready for analysis

### 3. Try Example Queries

Click on suggested queries from the interface, or try:

```text
Print x y z positions and energies of all the particles entering the Water moderator (cell 502)
```

```text
How many secondary photons are emitted and what is their process of termination?
```

```text
Plot the z-axis direction cosine (W) distribution of emitted source particles and display their average energy
```

### 4. Experiment with Your Own Questions

- Ask in natural language (English or French)
- Be specific about what data you want to extract
- DECIMA will generate Python code and execute it for you

### 5. Explore Advanced Features

- **Toggle "Add context"**: See how Knowledge Graph affects responses
- **Switch models**: Try `gpt-4o-mini` (fast/cheap) vs `gpt-4o` (more capable)
- **Verbose mode**: Use debug mode for detailed inspection
- **Compare outputs**: Try same query with/without KG context

### Understanding the Interface

- **OTACON Character**: Your AI assistant for PTRAC analysis
- **Model Selection**: Choose between OpenAI models
- **Add Context Toggle**: Enable/disable Knowledge Graph context injection
- **Example Queries**: Pre-written questions to get you started
- **Chat Area**: Conversations and generated code appear here
- **Execution Results**: Output from the generated Python code
- **Plot Display**: Visualizations rendered inline

---

## Next Steps

### For Python Package Users

- **Examples**: See [examples/README.md](examples/README.md)
- **Limitations**: Understand what works without Neo4j
- **Upgrade**: Consider switching to Docker mode for full functionality

### For Docker Users

- **Documentation**: Review `doc/` for architecture details
- **API Usage**: See [README.md](README.md) for programmatic access
- **Advanced**: Explore custom queries and workflows
- **Verbose Mode**: Use debug mode to understand how DECIMA works

### Getting Help

For support and questions:
- Check the troubleshooting section above
- Review the documentation in `doc/`
- Report issues: https://github.com/quentinducasse/decima/issues

---

## Comparison: Python Package vs Docker

| Feature | Python Package | Docker Mode |
|---------|----------------|-------------|
| **Setup Complexity** | Medium (manual steps) | Easy (one command) |
| **Neo4j KG** | Manual setup required | Auto-configured |
| **mcnptools** | Must compile locally | Pre-built in container |
| **Knowledge Graph** | Manual loading | Automatic |
| **Web Interface** | No | Yes |
| **Full Functionality** | Only with Neo4j setup | Always |
| **DEMO_MODE** | Returns fixed code | Returns fixed code |
| **With API + No Neo4j** | Code may have errors | N/A (Neo4j included) |
| **With API + Neo4j** | Full functionality | Full functionality |
| **Use Case** | Testing, development | Production, analysis |

**Recommendation**: Use Docker mode for real work. Use Python package only for testing installation or development.
