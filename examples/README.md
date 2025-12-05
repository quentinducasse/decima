# DECIMA Usage Examples

This directory contains examples demonstrating **three ways to use DECIMA**.

**IMPORTANT:** Each example below references the corresponding installation method in [INSTALL.md](../INSTALL.md). Follow the installation guide first, then run the examples.

---

## Quick Start Guide

### New Users - Start Here

1. **First time?** Follow [INSTALL.md](../INSTALL.md) to choose your installation method
2. **Docker Mode (RECOMMENDED):** Complete Method 2 in INSTALL.md → Run Mode 3 example below
3. **Python Package Mode:** Complete Method 1 in INSTALL.md → Run Mode 1 or Mode 2 examples below

---

## Overview: Three Usage Modes

| Mode | Example File | Installation | API Key | Neo4j KG | Functionality |
|------|-------------|--------------|---------|----------|---------------|
| **Mode 1: Demo** | `demo_mode_standalone.py` | [Method 1](../INSTALL.md#method-1-python-package-installation) | Optional | No | Basic (with base mcnptools context) |
| **Mode 2: Full API** | `full_api_mode.py` | [Method 1](../INSTALL.md#method-1-python-package-installation) + Manual Neo4j | Required | Manual | Full (if Neo4j configured) |
| **Mode 3: Docker** | Web Interface | [Method 2](../INSTALL.md#method-2-docker-installation-recommended) | Required | Auto | **FULL (RECOMMENDED)** |

**Recommendation:** Use Mode 3 (Docker) for production work. Use Mode 1 for testing installation only.

---

## Mode 1: Demo Mode (Standalone)

**Prerequisites:** Complete [INSTALL.md Method 1](../INSTALL.md#method-1-python-package-installation) first

**File:** `demo_mode_standalone.py`

### What This Mode Does

- + Works without Neo4j Knowledge Graph
- + Injects base mcnptools context (API structure + code example)
- With `DEMO_MODE=true`: Returns fixed code (no API calls, no costs)
- With `DEMO_MODE=false`: Generates code for YOUR query (basic mcnptools syntax only)

**Limitations:**
- No EMMA Knowledge Graph context (only base mcnptools syntax)
- May work for simple queries but lacks domain-specific MCNP knowledge

### Quick Start

**Step 1:** Install using [INSTALL.md Method 1](../INSTALL.md#method-1-python-package-installation)

**Step 2:** Run the example
```bash
python examples/demo_mode_standalone.py
```

The example uses `.env.docker` settings (configured in INSTALL.md Prerequisites).

### What You'll See

- Configuration status from `.env.docker`
- Query: "What is the average energy of the collision events?"
- Generated code (based on DEMO_MODE setting)
- Execution output with calculated average energy

### When to Use

- + First installation test after completing INSTALL.md Method 1
- + Verifying mcnptools compilation works
- + Understanding basic workflow
- - **NOT for production analysis** (use Mode 3 Docker instead)

---

## Mode 2: Full API Mode (Python Package)

**Prerequisites:** Complete [INSTALL.md Method 1](../INSTALL.md#method-1-python-package-installation) + Manual Neo4j setup

**File:** `full_api_mode.py`

### What This Mode Does

- + Full DECIMA functionality with Python API access
- + EMMA Knowledge Graph context (requires Neo4j)
- + Programmatic integration capability
- Requires manual Neo4j setup and Knowledge Graph loading

**For most users, Mode 3 (Docker) is easier!**

### Quick Start

**Step 1:** Install using [INSTALL.md Method 1](../INSTALL.md#method-1-python-package-installation)

**Step 2:** Build Docker app container (needed for KG loading)
```bash
docker compose build app
```

**Step 3:** Start Neo4j and load Knowledge Graph
```bash
# Start Neo4j container
docker compose up -d neo4j

# Wait for Neo4j (~15 seconds)
sleep 15

# Load Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py
```

**Step 4:** Run the example
```bash
python examples/full_api_mode.py
```

### Description

Python package mode with full functionality **IF** you manually setup Neo4j.

### When Full Functionality Works

+ **OpenAI API configured** - Custom code generation for YOUR queries
+ **Neo4j running + KG loaded** - EMMA provides MCNP domain knowledge
+ **Python API access** - Programmatic integration
+ **Scriptable** - Integration into workflows

### Limitations vs Docker Mode

- **Manual Neo4j setup required** - Need to run Docker for Neo4j anyway!
- **Manual KG loading** - Extra steps
- **Manual configuration** - More complex
- **No web interface** - Command-line only

**💡 If you need to run Docker for Neo4j anyway, why not use Docker mode for everything?**

### Programmatic Usage

Create your own script:

```python
from modules.campbell import CampbellOrchestrator

# Initialize
orchestrator = CampbellOrchestrator()

# Run analysis
result = orchestrator.process_query(
    query="Your natural language query here",
    ptrac_path="/path/to/file.ptrac",
    use_context=True  # Use Knowledge Graph
)

# Access results
print(result['response'])      # Explanation
print(result['code'])          # Generated code
print(result['stdout'])        # Execution output
print(result['output_files'])  # Generated plots
```

### When to Use This Mode

**ONLY if you specifically need:**
- + Programmatic Python API access
- + Custom automation/batch scripts
- + Integration into existing Python workflows
- + AND you're comfortable with manual Neo4j setup

**Otherwise, use Docker mode - it's easier and includes everything!**

---

## Mode 3: Docker Mode (RECOMMENDED)

**Prerequisites:** Complete [INSTALL.md Method 2](../INSTALL.md#method-2-docker-installation-recommended) first

**Interface:** Web application at http://localhost:5050

### What This Mode Does

- + **RECOMMENDED** - Easiest and most complete setup
- + Everything automatic: Neo4j + mcnptools + all services
- + Full DECIMA functionality out of the box
- + User-friendly web interface
- + No manual configuration needed

### Quick Start

**Complete INSTALL.md Method 2 fully, including:**

1. Build the app container: `docker compose build app`
2. Start all services: `docker compose up -d`
3. Load Knowledge Graph: `docker compose exec app python kg/loader/neo4j_loader.py`
4. Access web interface: http://localhost:5050

**IMPORTANT:** You must run `docker compose build app` before `docker compose up -d`, otherwise you'll get an error.

### Why Docker Mode is Best

+ **Everything automatic** - Neo4j + mcnptools + all services configured
+ **One command** - Just `docker compose up -d`
+ **Full functionality** - All agents (QUIET, EMMA, OTACON, EVA) active
+ **Web interface** - User-friendly chat with OTACON
+ **No manual setup** - No Neo4j installation, no KG loading
+ **Production-ready** - Isolated, reproducible deployment

### vs Python Package Mode

| Feature | Python Package | Docker Mode |
|---------|----------------|-------------|
| Setup complexity | 🟡 Manual Neo4j | 🟢 One command |
| Neo4j included | - Manual | + Automatic |
| KG loading | - Manual | + Automatic |
| mcnptools | WARNING: Must compile | + Pre-built |
| Web interface | - No | + Yes |
| Full functionality | WARNING: If Neo4j setup | + Always |

### When to Use

- + **RECOMMENDED for everyone**
- + First-time users
- + Production analysis
- + Team deployments
- + Demonstrations
- - Only skip if you specifically need Python API for automation

---

## 📊 Feature Comparison

| Feature | Demo Mode | Full API Mode | Docker Mode |
|---------|-----------|---------------|-------------|
| **OpenAI API** | - Not needed | + Required | + Required |
| **Neo4j KG** | - Disabled | + Docker | + Docker |
| **Custom Code** | - Fixed only | + Yes | + Yes |
| **EMMA Context** | - No | + Yes | + Yes |
| **Web Interface** | - No | - No | + Yes |
| **Python API** | + Yes | + Yes | - No |
| **mcnptools** | + Auto-installed | + Auto-installed | + Bundled |
| **Setup** | 🟢 Easy | 🟡 Medium | 🟡 Medium |
| **Cost** | 🟢 Free | 🟡 API costs | 🟡 API costs |

---

## 🧪 Testing Scripts

Additional test scripts are available to verify installation:

```bash
# Test mcnptools installation
python examples/test_mcnptools_direct.py

# Test DECIMA + mcnptools integration
python examples/test_decima_with_mcnptools.py
```

---

## 🔧 Common Configuration

### Environment Variables

All modes use `.env.docker` or `.env.local` for configuration:

```env
# LLM Provider
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here

# Neo4j (for Full API and Docker modes)
NEO4J_URI=bolt://localhost:7687  # or bolt://neo4j:7687 inside Docker
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123

# Demo mode flag (optional)
DEMO_MODE=false    # Set to true to force demo mode
```

### Sample PTRAC Files

Located in `data/ptrac_samples/`:
- `basic_ptrac_example_decima_ascii.ptrac` - ASCII format example

---

## 🚀 Quick Start Recommendations

### For First-Time Users

1. **Start with Demo Mode** (`demo_mode_standalone.py`)
   - Test without costs
   - Understand the workflow
   - Validate installation

2. **Try Docker Mode** (see [INSTALL.md](../INSTALL.md))
   - User-friendly web interface
   - Complete experience

### For Developers

1. **Start with Full API Mode** (`full_api_mode.py`)
   - Full programmatic access
   - Python API integration
   - Custom automation

### For Teams/Production

1. **Use Docker Mode** (see [INSTALL.md](../INSTALL.md))
   - Web interface for all users
   - Consistent deployment
   - Production-ready

---

## 💡 Tips

- **Start simple**: Begin with demo mode to test installation
- **Check Neo4j**: Always wait ~15 seconds for Neo4j to start before loading KG
- **Monitor costs**: gpt-4o-mini costs ~$0.001 per query
- **Toggle context**: Try with/without Knowledge Graph to see the difference

---

**Choose the mode that best fits your needs and technical expertise!** 🎯
