# DECIMA

**Data Extraction & Contextual Inference for MCNP Analysis**

> The first open-source framework combining LLMs and Knowledge Graphs for analyzing MCNP Particle Track Output (PTRAC) files

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)

---

## 🎯 What is DECIMA?

DECIMA transforms how nuclear engineers and researchers interact with MCNP simulation data. Instead of writing complex analysis scripts, simply ask questions in natural language:

**"Display collision positions and energies deposited for the first 20 particle histories"**
**"Plot the z-axis direction cosine (W) distribution of emitted source particles"**
**"How many secondary photons are emitted and what is their process of termination?"**

DECIMA's AI assistant **OTACON** will generate the Python code, execute it, and provide you with results and visualizations.

---

## ✨ See DECIMA in Action

<p align="center">
  <img src="frontend/static/img/decima_interface.jpg" width="800" alt="DECIMA Chat Interface"/>
</p>

*Ask questions in natural language - DECIMA generates and executes analysis code automatically. The interface shows example queries, model selection, and the friendly OTACON character ready to assist.*

---

## 🚀 Key Features

- **🗣️ Natural Language Queries** - No complex scripting required
- **🧠 AI-Powered Analysis** - Leverages OpenAI LLMs (gpt-4o, gpt-4o-mini)
- **📊 Automated Visualization** - Generates plots and tables automatically
- **�� Knowledge Graph Integration** - Uses MCNP domain knowledge for accurate context
- **🌐 Web Interface** - User-friendly Flask-based web app
- **🐍 Python API** - Programmatic access for integration and automation
- **🔍 Verbose Debug Mode** - Inspect full LLM prompts and workflow
- **🎯 Demo Mode** - Test without API key

---

## 🏗️ Architecture

DECIMA uses a modular multi-agent architecture inspired by *Metal Gear Solid*:

| Agent | Role | Technology |
|-------|------|------------|
| **🤫 QUIET** | Query interpretation & focus detection | Rule-based NLP |
| **🧠 EMMA** | Knowledge Graph context extraction | Neo4j |
| **👨‍💻 OTACON** | LLM reasoning & code generation | OpenAI API |
| **⚡ EVA** | Secure Python code execution sandbox | RestrictedPython |
| **📡 CAMPBELL** | System orchestration & workflow | LangGraph |

**Workflow:**
```
User Query → QUIET → EMMA → OTACON → EVA → Results
              ↓        ↓        ↓       ↓
          Focus    KG Context  Code  Execution
```

---

## 📦 Quick Start

DECIMA can be used in **two ways**:

### 🐳 Docker (Web Interface - Recommended)

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
cp .env.docker.example .env.docker
# Edit .env.docker to add your OpenAI API key
docker compose up -d
# Wait ~15 seconds for Neo4j to start
docker compose exec app python kg/loader/neo4j_loader.py
```

**Access:** [http://localhost:5050](http://localhost:5050)

### 🐍 Python Package (For Developers)

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
pip install -e .
docker compose up -d neo4j  # Start Neo4j only
python examples/basic_usage.py
```

**Usage:**
```python
from decima import DECIMA

analyzer = DECIMA(openai_api_key='your-key')
result = analyzer.analyze(
    ptrac_path='data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac',
    query='Plot energy distribution of neutrons'
)

print(result['explanation'])  # Natural language explanation
print(result['code'])         # Generated Python code
```

**📖 Full installation guide:** See [INSTALL_new.md](INSTALL_new.md)

---

## 🔑 API Key & Cost

To use DECIMA's full capabilities, you need an **OpenAI API key**:

- **Get one here:** [OpenAI Platform](https://platform.openai.com/api-keys)
- **Supported models:** gpt-4o-mini (default), gpt-4o
- **Cost:** ~10 queries for $0.01 with gpt-4o-mini
- **Demo mode:** Available without API key (returns fixed example)

---

## 🛠️ What Can DECIMA Do?

### Supported MCNP Data Analysis

- **Event Filtering:** Source (SRC), Collision (COL), Bank (BNK), Surface (SUR), Termination (TER)
- **Particle Data:** Position (X,Y,Z), Energy, Time, Direction (U,V,W), Weight
- **Particle Types:** Neutrons, photons, electrons, and more
- **Visualizations:** Histograms, scatter plots, energy distributions, spatial plots
- **Statistics:** Counts, averages, filtering, event correlations
- **Advanced:** Cell tracking, surface crossings, termination analysis

### Example Queries

**Basic Analysis:**
```
Show the first 10 source particles with their positions and energies
```

**Visualization:**
```
Plot the energy distribution of collision events
```

**Complex Analysis:**
```
Print x y z positions and energies of all particles entering the Water moderator (cell 502)
```

**Statistical:**
```
How many neutrons were terminated by capture vs escape?
```

---

## 📂 Project Structure

```
decima/
├── decima/                    # Python package (NEW)
│   └── __init__.py           # Main DECIMA class for programmatic use
├── modules/                   # Core agents
│   ├── quiet.py              # Query interpretation
│   ├── emma.py               # Knowledge Graph manager
│   ├── otacon.py             # LLM engine
│   ├── eva.py                # Code execution sandbox
│   └── campbell.py           # Workflow orchestrator
├── kg/                        # Knowledge Graph
│   ├── triplets/             # MCNP domain knowledge (RDF)
│   └── loader/               # Neo4j loader
├── frontend/                  # Web interface (Flask)
├── examples/                  # Usage examples (NEW)
│   ├── basic_usage.py        # Programmatic API example
│   └── README.md             # Examples documentation
├── data/                      # Sample PTRAC files
├── tests/                     # Unit tests
├── doc/                       # Documentation
├── pyproject.toml            # Python package config (NEW)
├── docker-compose.yml        # Docker deployment
├── app.py                    # Web app entry point
└── README.md                 # This file
```

---

## 🎓 Usage Examples

### Web Interface

1. Start DECIMA with Docker (see [Quick Start](#-quick-start))
2. Open [http://localhost:5050](http://localhost:5050)
3. Click "Load PTRAC File" or use the sample file
4. Enter your query in natural language (English or French)
5. Choose your LLM model (gpt-4o-mini or gpt-4o)
6. Toggle "Add context" to use Knowledge Graph
7. Submit and view generated code + results

### Python API

See [examples/basic_usage.py](examples/basic_usage.py) for a complete example:

```python
from decima import DECIMA

# Initialize
analyzer = DECIMA(
    openai_api_key='your-key',
    neo4j_uri='bolt://localhost:7687',  # Optional
    neo4j_user='neo4j',                 # Optional
    neo4j_password='decima123'          # Optional
)

# Analyze
result = analyzer.analyze(
    ptrac_path='path/to/file.ptrac',
    query='Your natural language question',
    use_context=True  # Use Knowledge Graph context
)

# Access results
print(result['explanation'])  # LLM explanation
print(result['code'])         # Generated Python code
print(result['stdout'])       # Execution output
print(result['output_files']) # Generated plots
```

### Verbose Mode

See detailed workflow execution:

```bash
# Docker
docker compose run --rm --service-ports app python app.py -v

# Python
python examples/basic_usage.py  # Already verbose by default
```

Output shows:
- QUIET focus detection
- EMMA Knowledge Graph entities
- OTACON LLM prompt and response
- EVA execution results

---

## 🧪 Demo Mode

Test DECIMA without an OpenAI API key:

**Setup:** Set `DEMO_MODE=true` in `.env.docker`

**What it does:**
- Runs without external API calls
- Returns pre-written collision analysis example
- Useful for testing and validation

**Limitations:**
- Ignores your actual query
- Returns fixed response only

**For full functionality:** Set a valid `OPENAI_API_KEY` and `DEMO_MODE=false`

---

## 🔬 Technology Stack

### Core Technologies
- **Python 3.10+**
- **OpenAI API** (gpt-4o, gpt-4o-mini)
- **Neo4j 5.19** (Knowledge Graph)
- **MCNPTools** (PTRAC parsing)
- **LangGraph** (Agent orchestration)
- **Flask** (Web interface)
- **RestrictedPython** (Secure code execution)

### Key Libraries
- `openai` - LLM interaction
- `neo4j` - Graph database driver
- `langchain-core` - Agent framework
- `matplotlib` - Visualization
- `numpy` - Numerical computing
- `flask` - Web framework
- `python-dotenv` - Environment config

---

## 📖 Documentation

- **Installation Guide:** [INSTALL_new.md](INSTALL_new.md)
- **API Examples:** [examples/README.md](examples/README.md)
- **Architecture Details:** [doc/architecture_decima.md](doc/architecture_decima.md)
- **Research Paper:** [paper.md](paper.md)

---

## 🧑‍💻 Development

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Specific test modules
pytest tests/test_quiet.py
pytest tests/test_emma.py
pytest tests/test_otacon_api.py
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 Citation

If you use DECIMA in your research, please cite:

```bibtex
@software{decima2025,
  title = {DECIMA: Data Extraction \& Contextual Inference for MCNP Analysis},
  author = {Ducasse, Quentin and Almuhisen, Feda},
  year = {2025},
  url = {https://github.com/quentinducasse/decima},
  version = {1.2.0},
  license = {Apache-2.0}
}
```

---

## 👥 Authors

**Quentin Ducasse**
- LinkedIn: [Quentin Ducasse](https://www.linkedin.com/in/quentin-ducasse/)
- GitHub: [@quentinducasse](https://github.com/quentinducasse)

**Feda Almuhisen**
- LinkedIn: [Feda Almuhisen](https://www.linkedin.com/in/feda-almuhisen/)

---

## 📜 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

**Key points:**
- ✅ Free to use, modify, and distribute
- ✅ Commercial use allowed
- ✅ Patent rights granted
- ⚠️ Must include license and copyright notice
- ⚠️ Must state significant changes made

---

## 🙏 Acknowledgments

- **MCNPTools** by Los Alamos National Laboratory
- **OpenAI** for GPT models
- **Neo4j** for graph database technology
- **Metal Gear Solid** for agent naming inspiration
- The nuclear engineering and AI research communities

---

## 🔗 Related Projects

- **MCNPTools**: [GitHub](https://github.com/lanl/mcnptools)
- **OpenAI Python SDK**: [GitHub](https://github.com/openai/openai-python)
- **LangGraph**: [Documentation](https://python.langchain.com/docs/langgraph)
- **Neo4j**: [Official Site](https://neo4j.com/)

---

## 📞 Support & Community

- **Issues:** [GitHub Issues](https://github.com/quentinducasse/decima/issues)
- **Discussions:** [GitHub Discussions](https://github.com/quentinducasse/decima/discussions)
- **Email:** See author LinkedIn profiles

---

## 🗺️ Roadmap

### Current Version (1.2.0)
- ✅ Web interface with Flask
- ✅ Python package API
- ✅ Knowledge Graph integration
- ✅ Docker deployment
- ✅ Demo mode

### Future Plans
- 🔄 Support for additional LLM providers (Anthropic, local models)
- 🔄 Enhanced visualization capabilities
- 🔄 MCTAL file support
- 🔄 Batch analysis mode
- 🔄 Export to common formats (CSV, Excel, HDF5)
- 🔄 Plugin system for custom analysis
- 🔄 REST API for remote access

---

## ⚠️ Limitations & Known Issues

- **PTRAC Format:** Currently optimized for standard MCNP6 PTRAC output
- **Memory:** Large PTRAC files (>1GB) may require batching
- **LLM Accuracy:** Generated code quality depends on query clarity
- **Neo4j Required:** Full functionality requires Neo4j running
- **Windows:** Some path handling may need adjustments

See [GitHub Issues](https://github.com/quentinducasse/decima/issues) for current bugs and feature requests.

---

**Made with ❤️ for the nuclear engineering community**
