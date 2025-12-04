# DECIMA Usage Examples

This directory contains examples demonstrating **three different ways to use DECIMA**, each with specific advantages and limitations.

---

## 📋 Overview: Three Usage Modes

DECIMA can be used in three distinct modes depending on your needs:

| Mode | Files/Dependencies | API Key | Neo4j | mcnptools | Use Case |
|------|-------------------|---------|-------|-----------|----------|
| **Demo (Standalone)** | `demo_mode_standalone.py` | ❌ Not needed | ❌ Not needed | ✅ Auto-installed* | Quick testing, offline demos |
| **Hybrid (pip + Docker)** | `hybrid_mode_pip_docker.py`<br/>`basic_usage.py` | ⚠️ Optional** | 🐳 Docker | ✅ Auto-installed* | Python scripting, automation |
| **Full Docker (Web App)** | `full_docker_mode.md` | ⚠️ Optional** | 🐳 Docker | 🐳 Bundled | End users, teams, production |

*mcnptools is automatically compiled and installed when you run `python install_dev.py` (see [INSTALL.md](../INSTALL.md))
**If no API key provided, automatically falls back to DEMO_MODE (returns fixed collision analysis code)

---

## 🎯 Mode 1: Demo Mode (Standalone)

**File:** `demo_mode_standalone.py`

### Description

Minimal setup for testing DECIMA without external dependencies. Returns pre-written example code regardless of your query.

### Advantages

✅ **No API key required** - Zero costs
✅ **No Neo4j needed** - No Docker containers
✅ **Quick validation** - Test installation instantly
✅ **Offline capable** - Works without internet (except initial install)
✅ **No LLM calls** - Predictable, reproducible output

### Limitations

❌ **Fixed responses only** - Ignores your actual query
❌ **No Knowledge Graph** - EMMA is disabled
❌ **No custom code** - Returns pre-written collision example only
✅ **mcnptools included** - Auto-installed with DECIMA
❌ **Limited functionality** - Demonstrates workflow only

### Use Cases

- Initial installation testing
- Validating DECIMA setup
- Offline demonstrations
- Understanding the workflow
- Cost-free exploration

### Prerequisites

```bash
# Install DECIMA package (includes mcnptools compilation)
python install_dev.py
# Or manually: python setup.py build_ext --inplace && pip install -e .
```

### How to Run

```bash
# Set demo mode in environment
export DEMO_MODE=true         # Unix/macOS
set DEMO_MODE=true            # Windows CMD
$env:DEMO_MODE="true"         # Windows PowerShell

# Run the example
python examples/demo_mode_standalone.py
```

### Expected Output

```
============================================================
DECIMA - DEMO MODE (Standalone - No Dependencies)
============================================================

⚙️  Configuration:
   ✅ DEMO_MODE: enabled
   ✅ OpenAI API: not required
   ✅ Neo4j KG: not required
   ✅ mcnptools: auto-installed

------------------------------------------------------------
📂 PTRAC file: data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac
❓ Query: Plot the energy distribution of neutrons

⚠️  NOTE: In DEMO MODE, your query is ignored.
   The system returns a fixed collision analysis example.

============================================================
💡 Explanation:
[DEMO MODE] No API key provided or DEMO_MODE enabled. This is a sample...

💻 Generated Code (Fixed Example):
from mcnptools import Ptrac

# DEMO MODE: this is a fixed example, independent of the user query
p = Ptrac("<PTRAC_PATH_PLACEHOLDER>", Ptrac.BIN_PTRAC)
cnt = 0
...
```

### When to Use

- ✅ First time trying DECIMA
- ✅ Testing without OpenAI costs
- ✅ Validating installation
- ✅ Offline demonstrations
- ❌ Production analysis (use Hybrid or Full Docker mode)

---

## 🔄 Mode 2: Hybrid Mode (pip + Docker Neo4j)

**Files:** `hybrid_mode_pip_docker.py`, `basic_usage.py`

### Description

Full DECIMA functionality via Python API with Neo4j running in Docker. Custom code generation for each query with Knowledge Graph context.

### Advantages

✅ **Full functionality** - All agents active (QUIET, EMMA, OTACON, EVA)
✅ **Python API access** - Programmatic integration
✅ **Custom code generation** - LLM creates code for YOUR query
✅ **Knowledge Graph context** - EMMA provides MCNP domain knowledge
✅ **Scriptable/Automatable** - Integration into workflows
✅ **Verbose output** - See all intermediate steps
✅ **Lower resource usage** - Only Neo4j container needed

### Limitations

❌ **Neo4j required** - Must run Docker container for KG context
⚠️ **API key optional** - Falls back to DEMO_MODE if not provided (fixed responses)
❌ **mcnptools required** - Must be installed separately
❌ **No web interface** - Command-line only
❌ **Manual Neo4j setup** - Must start and load KG

### Use Cases

- Python developers integrating DECIMA
- Automated batch analysis
- Jupyter notebooks
- Research scripts
- CI/CD pipelines
- Custom workflows

### Prerequisites

```bash
# 1. Install DECIMA package
pip install -e .

# 2. Configure environment
cp .env.docker.example .env.docker
# Edit .env.docker and add your OPENAI_API_KEY

# 3. Start Neo4j container
docker compose up -d neo4j

# 4. Wait for Neo4j to be ready
# Wait ~15 seconds for Neo4j to fully start

# 5. Load Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py
```

### How to Run

**Option A: Verbose example (recommended)**
```bash
python examples/hybrid_mode_pip_docker.py
```

**Option B: Original basic example**
```bash
python examples/basic_usage.py
```

**Note:** If `OPENAI_API_KEY` is not set, both examples automatically enable DEMO_MODE (returns fixed collision analysis code).


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

### When to Use

- ✅ Python developers
- ✅ Custom automation scripts
- ✅ Batch processing workflows
- ✅ Research notebooks
- ❌ Non-programmers (use Full Docker mode)

---

## 🐳 Mode 3: Full Docker Mode (Web Interface)

**File:** `full_docker_mode.md`

### Description

Complete web application with user-friendly chat interface. Everything runs in Docker containers.

### Advantages

✅ **Web interface** - User-friendly chat with OTACON
✅ **Everything containerized** - No local Python setup
✅ **Consistent environment** - Works same on all platforms
✅ **Production-ready** - Isolated, reproducible deployment
✅ **Visual interface** - Upload files, see plots, chat UI
✅ **mcnptools bundled** - No separate installation needed
✅ **Team-ready** - Can be deployed for multiple users

### Limitations

❌ **Higher resource usage** - Multiple containers running
❌ **No programmatic API** - Web interface only (not scriptable)
❌ **Requires Docker** - Additional software installation
❌ **Port binding** - Ports 5050, 7474, 7687 must be available
❌ **More complex** - Full stack deployment

### Use Cases

- End users without programming background
- Team/organizational deployments
- Production environments
- Demonstrations and presentations
- Workshops and training
- Shared access scenarios

### Prerequisites

```bash
# 1. Docker Desktop installed and running
# Windows/macOS: Docker Desktop
# Linux: Docker Engine

# 2. Clone repository
git clone https://github.com/quentinducasse/decima.git
cd decima

# 3. Configure environment
cp .env.docker.example .env.docker
# Edit .env.docker and add your OPENAI_API_KEY
```

### How to Run

**Standard mode:**
```bash
# Build and start all services
docker compose build app
docker compose up -d

# Wait for Neo4j (~15 seconds)
# Wait approximately 15 seconds for Neo4j

# Load Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py

# Access web interface
# Open http://localhost:5050 in browser
```

**Verbose/Debug mode:**
```bash
# Stop background services
docker compose down

# Start only Neo4j
docker compose up -d neo4j

# Wait for Neo4j
# Wait approximately 15 seconds for Neo4j

# Load Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py

# Run in verbose mode
docker compose run --rm --service-ports app python app.py -v
```

Verbose mode shows:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5050      ← Click this link!
 * Running on http://172.18.0.3:5050
 * Debugger is active!
```

### Web Interface Features

1. **Load PTRAC File**
   - Upload your file or use sample
   - Binary or ASCII format supported

2. **Model Selection**
   - gpt-4o-mini (fast, cheap)
   - gpt-4o (more capable, expensive)

3. **Knowledge Graph Toggle**
   - "Add context" ON: Uses EMMA + Neo4j
   - "Add context" OFF: Direct LLM query

4. **Natural Language Queries**
   - English or French
   - Example queries provided
   - Custom questions

5. **Results Display**
   - Natural language explanation
   - Generated Python code
   - Execution output
   - Plots and visualizations

### When to Use

- ✅ Non-programmers
- ✅ Team deployments
- ✅ Production use
- ✅ Demonstrations
- ❌ Scripting/automation (use Hybrid mode)

---

## 📊 Feature Comparison

| Feature | Demo Mode | Hybrid Mode | Full Docker |
|---------|-----------|-------------|-------------|
| **OpenAI API** | ❌ Not needed | ✅ Required | ✅ Required |
| **Neo4j KG** | ❌ Disabled | ✅ Docker | ✅ Docker |
| **Custom Code** | ❌ Fixed only | ✅ Yes | ✅ Yes |
| **EMMA Context** | ❌ No | ✅ Yes | ✅ Yes |
| **Web Interface** | ❌ No | ❌ No | ✅ Yes |
| **Python API** | ✅ Yes | ✅ Yes | ❌ No |
| **Resource Usage** | 🟢 Low | 🟡 Medium | 🔴 High |
| **Setup Complexity** | 🟢 Easy | 🟡 Medium | 🔴 Complex |
| **Cost** | 🟢 Free | 🟡 API costs | 🟡 API costs |
| **mcnptools** | ⚠️ Separate | ⚠️ Separate | ✅ Bundled |

---

## 🛠️ Common Configuration

### Environment Variables

All modes use `.env.docker` for configuration:

```env
# LLM Provider
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here

# Neo4j (for Hybrid and Full Docker modes)
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123

# Demo mode flag
DEMO_MODE=false    # Set to true for demo mode
```

### Sample PTRAC Files

Located in `data/ptrac_samples/`:
- `basic_ptrac_example_decima_ascii.ptrac` - ASCII format example

### Output Files

Generated plots are saved to:
- **Hybrid mode**: `uploads/plots/`
- **Full Docker**: `/app/uploads/plots/` (inside container)

---

## 🔧 Troubleshooting

### Neo4j Connection Issues

**Problem:** `Connection refused to neo4j:7687`

**Solution:**
```bash
# Check if Neo4j is running
docker compose ps

# Check Neo4j logs
docker compose logs neo4j

# Wait for "Started" message
# Wait approximately 15 seconds for Neo4j

# Restart if needed
docker compose restart neo4j
```

### Knowledge Graph Empty

**Problem:** EMMA returns no entities

**Solution:**
```bash
# Reload Knowledge Graph
docker compose run --rm app python kg/loader/neo4j_loader.py

# Verify in Neo4j browser (http://localhost:7474)
# Run: MATCH (n) RETURN count(n)
```

### API Key Invalid

**Problem:** `Invalid API key` error

**Solution:**
- Check `.env.docker` for typos
- Verify key at [OpenAI Platform](https://platform.openai.com/api-keys)
- Ensure sufficient credits
- No extra spaces in the key

### mcnptools Not Found

**Problem:** `ModuleNotFoundError: No module named 'mcnptools'`

**Solution:**
- **Demo/Hybrid mode**: mcnptools is auto-installed with `python install_dev.py`
- **Full Docker mode**: Already bundled in container

---

## 📚 Additional Resources

- **Main README**: `../README.md` - Project overview
- **Installation Guide**: `../INSTALL.md` - Detailed setup
- **Full Docker Guide**: `full_docker_mode.md` - Web interface details
- **Documentation**: `../doc/` - Technical documentation

---

## 🚀 Quick Start Recommendations

### For First-Time Users

1. **Start with Demo Mode** (`demo_mode_standalone.py`)
   - Test without costs
   - Understand the workflow
   - Validate installation

2. **Try Full Docker Mode** (`full_docker_mode.md`)
   - User-friendly web interface
   - Complete experience
   - Upload your PTRAC files

### For Developers

1. **Start with Hybrid Mode** (`hybrid_mode_pip_docker.py`)
   - Full programmatic access
   - Python API integration
   - Custom automation

2. **Reference basic_usage.py**
   - Original example
   - Verbose output
   - All agent details

### For Teams/Production

1. **Use Full Docker Mode** (`full_docker_mode.md`)
   - Web interface for all users
   - Consistent deployment
   - Production-ready

---

## 💡 Tips

- **Start simple**: Begin with demo mode to test
- **Check Neo4j**: Always wait for "Started" message before loading KG
- **Use verbose mode**: Add `-v` flag or use verbose examples for debugging
- **Monitor costs**: gpt-4o-mini costs ~$0.001 per query
- **Toggle context**: Try with/without Knowledge Graph to see the difference
- **Read logs**: Check `docker compose logs` for issues

---

**Choose the mode that best fits your needs and technical expertise!** 🎯
