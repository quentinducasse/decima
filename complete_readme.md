<p align="center">
  <img src="decima_logo.png" width="250"/>
</p>

# DECIMA
**Data Extraction & Contextual Inference for MCNP Analysis**

> AI-powered MCNP data analysis through natural language queries  
> Built with LLMs, Knowledge Graphs, and MCNPTools  
> Production-ready via Docker deployment

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Docker](https://img.shields.io/badge/Docker-20.10.13%2B-blue.svg)](https://docs.docker.com/get-docker/)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.19-green.svg)](https://neo4j.com/)

---

## 🎯 What is DECIMA?

DECIMA transforms how nuclear engineers and researchers interact with MCNP simulation data. Instead of writing complex analysis scripts, simply ask questions in natural language:

**"Show me collision positions and energies for the first 20 particle histories"**  
**"Plot the energy distribution of neutrons in cell 5"**  
**"Which materials have the highest interaction rates?"**

### Key Benefits
- 🗣️ **Natural Language Queries** - No more complex scripting for data extraction
- 🧠 **AI-Powered Analysis** - Leverages advanced LLMs for intelligent interpretation  
- 📊 **Automated Visualization** - Generates plots and charts automatically
- 🔗 **Knowledge Integration** - Uses domain-specific context for accurate results
- 🐳 **Easy Deployment** - One-command Docker setup

---

## 🏗️ Architecture

DECIMA uses a modular architecture inspired by *Metal Gear Solid* agents:

- **🤫 QUIET**: Natural language query interpreter
- **🧠 EMMA**: Knowledge graph manager (Neo4j backend) 
- **👨‍💻 OTACON**: Central LLM agent for reasoning and code generation
- **⚡ EVA**: Secure sandbox for Python code execution
- **📡 CAMPBELL**: System orchestrator coordinating all modules

### Supported Data Formats
- ✅ **MCNP PTRAC files** (ASCII and Binary)
- ✅ **Knowledge Graph integration** (Neo4j)
- 🔄 **MCTAL files** *(roadmap)*
- 🔄 **HDF5 format** *(roadmap)*

---

## 🚀 Quick Start

### Prerequisites
- Docker 20.10.13+ *(tested with 28.3.3)*
- 4GB+ RAM for Neo4j
- OpenAI API key *(optional - demo mode available)*

### One-Command Setup
```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
cp .env.docker.example .env.docker  # Add your OpenAI API key here
docker compose build app && docker compose up -d
docker compose exec app python kg/loader/neo4j_loader.py
```

**🌐 Access DECIMA:** [http://localhost:5050](http://localhost:5050)

---

## 📦 Detailed Installation

### ✅ Step 1: Prerequisites

<details>
<summary><strong>🐳 Docker Installation</strong></summary>

**Check existing installation:**
```bash
docker --version          # Should show 20.10.13+
docker compose version    # Should show Compose V2
docker run hello-world    # Test Docker works
```

**Install Docker if needed:**
- **Linux:** [Docker Engine install guide](https://docs.docker.com/engine/install/)
- **Windows/macOS:** [Docker Desktop](https://docs.docker.com/get-docker/)

**Linux users - avoid sudo:**
```bash
sudo usermod -aG docker $USER
# Log out and back in, then test: docker --version
```
</details>

<details>
<summary><strong>🔑 OpenAI API Key (Optional)</strong></summary>

**Get an API key:** [OpenAI Platform](https://platform.openai.com/api-keys)

**Supported models:**
- `gpt-4o-mini` *(default, ~10 queries per cent)*
- `gpt-4o` *(more capable, higher cost)*

**No API key?** DECIMA runs in demo mode with sample responses.

**Need a temporary key for testing?** Contact us on [LinkedIn](https://www.linkedin.com/in/quentin-ducasse-a65410124/)
</details>

### 🛠️ Step 2: Setup DECIMA

**1. Clone and configure:**
```bash
git clone https://github.com/quentinducasse/decima.git
cd decima

# Linux/macOS
cp .env.docker.example .env.docker

# Windows  
copy .env.docker.example .env.docker
```

**2. Edit `.env.docker`:**
```env
# LLM Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key-here    # ← Add your API key
DEMO_MODE=false                    # Set to 'true' for demo mode

# Database (don't modify these)
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123
```

**3. Build and start services:**
```bash
# Build application (first time only, ~5-10 minutes)
docker compose build app

# Start all services
docker compose up -d

# Verify services are running
docker compose ps
```

**4. Initialize knowledge graph:**
```bash
docker compose exec app python kg/loader/neo4j_loader.py
```

**Expected output:**
```
Loading knowledge graph...
✓ Connected to Neo4j
✓ Loaded XXX nodes and XXX relationships  
Knowledge graph ready!
```

### 🧪 Step 3: Test Installation

**1. Access web interfaces:**
- **DECIMA:** [http://localhost:5050](http://localhost:5050)
- **Neo4j Browser:** [http://localhost:7474](http://localhost:7474) *(user: neo4j, password: decima123)*

**2. Quick test:**
- Upload sample file: `data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac`
- Try query: *"Print x y z positions and energies of all events for the first 20 histories"*
- Verify you get structured results

---

## 💡 Usage Examples

### Basic Queries
```
Show me particle positions and energies for the first 10 histories
Plot energy distribution of neutrons
Which cells have the most interactions?
What's the average energy of particles in material 2?
```

### Advanced Analysis
```
Compare energy spectra between cells 1 and 2
Show collision positions colored by particle type
Generate a histogram of interaction depths
Calculate flux distributions across the geometry
```

### File Management
- **Supported formats:** `.ptrac` (ASCII/Binary)
- **Upload location:** Use the web interface
- **Sample data:** Pre-loaded in `data/ptrac_samples/`

---

## 🔧 Daily Operations

### Start/Stop DECIMA
```bash
# Start (daily use)
docker compose up -d

# Stop 
docker compose down

# Restart after changes
docker compose restart app
```

### Development Mode
```bash
# Start with verbose logging
docker compose up -d neo4j
docker compose run --rm app python kg/loader/neo4j_loader.py
docker compose run --rm --service-ports app python app.py -v
```

### Maintenance
```bash
# View logs
docker compose logs app
docker compose logs neo4j

# Rebuild after code changes  
docker compose build app --no-cache

# Reset Neo4j database
docker compose down
docker volume rm decima_neo4j-data
docker compose up -d
```

---

## 🐛 Troubleshooting

<details>
<summary><strong>❌ Installation Issues</strong></summary>

**"Permission denied" (Linux):**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

**"Port already in use":**
```bash
docker compose down
# Check what's using ports 5050/7474/7687
lsof -i :5050  # Linux/macOS
netstat -ano | findstr :5050  # Windows
```

**Neo4j won't start:**
```bash
# Check available memory (Neo4j needs ~2GB)
free -h

# Reset Neo4j data
docker volume rm decima_neo4j-data
docker compose up -d neo4j
```

**Build fails:**
```bash
# Clean rebuild
docker compose build app --no-cache --pull
```
</details>

<details>
<summary><strong>❌ Runtime Issues</strong></summary>

**"No module named mcnptools":**
```bash
docker compose build app --no-cache
docker compose up -d
```

**LLM queries fail:**
- Check API key in `.env.docker`
- Verify OpenAI account has credits
- Try demo mode: `DEMO_MODE=true`

**Knowledge graph empty:**
```bash
docker compose exec app python kg/loader/neo4j_loader.py
```

**File upload fails:**
- Check file is valid PTRAC format
- Try sample file first: `data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac`
</details>

<details>
<summary><strong>🔍 Getting Help</strong></summary>

**Debug information:**
```bash
docker compose ps              # Check service status
docker compose logs app       # Application logs  
docker compose logs neo4j     # Database logs
docker --version              # Verify Docker version
```

**Contact:**
- 💬 [Quentin Ducasse - LinkedIn](https://www.linkedin.com/in/quentin-ducasse-a65410124/)
- 💬 [Feda Almuhisen - LinkedIn](https://www.linkedin.com/in/feda-almuhisen/)
- 📝 [GitHub Issues](https://github.com/quentinducasse/decima/issues)
</details>

---

## 📁 Project Structure

```
decima/
├── app.py                 # Main Flask application
├── docker-compose.yml     # Container orchestration
├── Dockerfile            # Application container
├── requirements.txt      # Python dependencies
├── .env.docker.example   # Environment template
├── modules/              # Core DECIMA modules
│   ├── quiet/           # Query interpretation  
│   ├── otacon/          # LLM reasoning
│   ├── emma/            # Knowledge graph
│   └── eva/             # Code execution
├── kg/                   # Knowledge graph data
│   └── loader/          # Graph initialization
├── frontend/             # Web interface
├── uploads/             # User files and results
├── tools/               # Analysis utilities  
├── mcnptools/           # MCNPTools integration
├── data/                # Sample datasets
│   └── ptrac_samples/   # Example PTRAC files
└── doc/                 # Documentation
```

---

## 🚧 Roadmap

- [ ] **MCTAL file support** - Extend to MCNP tally outputs with visualization
- [ ] **Batch processing** - Analyze multiple files in comparative studies  
- [ ] **HDF5 compatibility** - Support parallel MCNP calculations
- [ ] **Advanced reasoning** - Enhanced context handling and domain inference
- [ ] **Extended visualization** - 3D plots, interactive dashboards
- [ ] **API endpoints** - REST API for programmatic access

---

## 📚 Citation

If you use DECIMA in your research, please cite:

```bibtex
@software{decima2025,
  author = {Almuhisen, Feda and Ducasse, Quentin},
  title = {DECIMA -- Data Extraction \& Contextual Inference for MCNP Analysis},
  version = {v1.2.0},
  year = {2025},
  url = {https://github.com/quentinducasse/decima}
}
```

📌 *JOSS paper submission in preparation - please update citation when published.*

---

## 📜 License & Acknowledgments

**License:** Apache License 2.0 (OSI-approved open source)

**Built with:**
- [MCNPTools (LANL)](https://github.com/lanl/mcnptools) - MCNP data parsing
- [OpenAI GPT](https://openai.com/) - Natural language processing
- [Neo4j](https://neo4j.com/) - Knowledge graph database
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Docker](https://docker.com/) - Containerization

**Commercial licensing:** Contact authors for enterprise/commercial use terms.

---

## 🤝 Contributing

We welcome contributions from the nuclear simulation community!

**Areas for contribution:**
- MCNP format support (MCTAL, newer PTRAC variants)
- Domain-specific analysis modules  
- Visualization enhancements
- Documentation improvements
- Bug reports and testing

**Development setup:**
```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
# Follow installation steps above
# Make changes and submit PR
```

---

**🔬 DECIMA: Making MCNP data analysis as simple as asking a question.**

*Authors: Feda Almuhisen & Quentin Ducasse | 2025*