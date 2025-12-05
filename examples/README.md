# DECIMA Usage Examples

This directory contains examples demonstrating **two ways to use DECIMA**.

---

## WARNING: IMPORTANT: Python Package vs Docker

### Python Package Mode (This Directory)
- + Good for: Testing installation, understanding workflow
- - **LIMITED**: Requires manual Neo4j setup for full functionality
- - Without Neo4j: EMMA disabled, returns fixed code examples
- 🎯 Use case: Developers who want programmatic API access

### 🐳 Docker Mode (RECOMMENDED for full functionality)
- + **Everything automatic**: Neo4j + mcnptools + all services
- + **No manual setup**: Just `docker compose up -d`
- + **Full functionality** out of the box
- + Web interface included
- 🎯 Use case: Production use, easiest full setup

**→ For full DECIMA experience, use Docker mode (see [INSTALL.md](../INSTALL.md) Method 2)**

---

## 📋 Overview: Usage Modes

| Mode | File | API Key | Neo4j KG | Setup Complexity | Functionality |
|------|------|---------|----------|------------------|---------------|
| **Demo (Standalone)** | `demo_mode_standalone.py` | - Not needed | - Not needed | 🟢 Easy | WARNING: **LIMITED** (fixed code only) |
| **Full API (Python)** | `full_api_mode.py` | + Required | WARNING: Manual setup | 🟡 Medium | WARNING: Requires Neo4j for full features |
| **Docker (RECOMMENDED)** | See [INSTALL.md](../INSTALL.md) | + Required | + Auto-configured | 🟢 Easy | + **FULL** functionality |

**Note:** mcnptools is automatically compiled when you run `python install_dev.py`

---

## 🎯 Mode 1: Demo Mode (Standalone)

**File:** `demo_mode_standalone.py`

### WARNING: IMPORTANT: This is a LIMITED demo

This mode demonstrates the DECIMA workflow but with **DEMO_MODE=true**:
- - **Always returns the same fixed code** (collision analysis)
- - **Your query is completely IGNORED** (DEMO_MODE behavior)
- - **No intelligent code generation**
- - **No Knowledge Graph context**

**Note**: Even with OpenAI API (DEMO_MODE=false), without Neo4j Knowledge Graph,
OTACON may generate code with errors due to missing MCNP domain context.

**Use this ONLY for:**
- Testing that installation worked
- Understanding the basic workflow
- Offline demonstrations

**For real analysis, use Docker mode!**

### Quick Start

```bash
# Install DECIMA (includes mcnptools compilation)
python install_dev.py

# Run demo (will show limitations clearly)
python examples/demo_mode_standalone.py
```

### What You'll See

The demo uses a simple query: **"What is the average energy of the collision events?"**

But DEMO_MODE **ignores this** and returns a fixed collision analysis code instead.

This demonstrates the workflow, but not the intelligent code generation capabilities.

### When to Use

- + First installation test
- + Verifying mcnptools compilation
- + Understanding workflow structure
- - **NOT for real analysis** (use Docker mode)

---

## 🚀 Mode 2: Full API Mode (Python Package)

**File:** `full_api_mode.py`

### WARNING: IMPORTANT: Requires Manual Neo4j Setup

This mode is for **developers** who want programmatic access to DECIMA.

**Without Neo4j**, this mode has the **same limitations as Demo Mode**:
- - EMMA (Knowledge Graph) disabled
- - Returns fixed code examples
- - No intelligent code generation

**For most users, Docker mode is easier and better!**

### Quick Start

```bash
# 1. Install DECIMA (includes mcnptools)
python install_dev.py

# 2. Configure environment
cp .env.docker.example .env.local
# Edit .env.local and add your OPENAI_API_KEY

# 3. Start Neo4j (REQUIRED for full functionality!)
docker compose up -d neo4j

# 4. Wait for Neo4j to be ready (~15 seconds)
sleep 15

# 5. Load Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py

# 6. Run example
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

## 🐳 Mode 3: Docker Mode (RECOMMENDED)

**See:** [INSTALL.md](../INSTALL.md) - Method 2

###  RECOMMENDED for Full Functionality

This is the **easiest way** to get DECIMA with **full functionality**.

### Quick Start

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
cp .env.docker.example .env.docker
# Edit .env.docker to add your OpenAI API key
docker compose up -d
```

Then open http://localhost:5050 in your browser.

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
