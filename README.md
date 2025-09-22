
<p align="center">
  <img src="decima_logo.png" width="250"/>
</p>

# DECIMA
**Data Extraction & Contextual Inference for MCNP Analysis**

> Powered by LLMs, Knowledge Graphs, and MCNPTools  
> Simple. Portable. Ready-to-run via Docker.

---
## 📦 Features

- Modular architecture inspired by *Metal Gear Solid* agents:
  - **QUIET**: Query Interpreter for natural language analysis  
  - **EMMA**: Knowledge Graph manager (Neo4j backend)  
  - **OTACON**: Central LLM agent for PTRAC reasoning and code generation  
  - **EVA**: Safe sandbox for executing generated Python code  
  - **CAMPBELL**: Orchestrator coordinating all modules  

- Full support for MCNP `PTRAC` files via `mcnptools`  
- Knowledge Graph context injection (Neo4j)  
- Verbose debug mode with detailed workflow + LLM context inspection  
- Web interface (Flask + Bootstrap)  

---

## 🔑 API Key Requirement

To run LLM-based queries, you must provide a valid **OpenAI API key**.  
Currently supported models are:  
- **gpt-4o-mini** (default)  
- **gpt-4o**  

From my own experience, **gpt-4o-mini** is very cost-effective — around **10 queries for 1 cent**.  

👉 For testing purposes, I can provide a **temporary free API key** (limited in time and usage).  
If you are interested, please contact me directly via [LinkedIn](#-contact).

---

## 🔧 Demo Mode (for testing without API key)

DECIMA includes a **demo mode** for reviewers and first-time users.

- If no API key is provided, or if `DEMO_MODE=true` is set in your `.env.docker` file,  
  DECIMA runs in a fallback mode.

- In this mode, the system always returns a **fixed example**: positions (x,y,z) and energies  
  of collision events from the uploaded PTRAC file.  
  This ensures that DECIMA remains executable even without access to external LLM APIs.

⚠️ Demo mode is **limited**: it ignores your actual query and does not call the LLM.

To unlock the full functionality, set your `OPENAI_API_KEY` in `.env.docker`  
and set `DEMO_MODE=false`.

⚠️ Important:
- If `OPENAI_API_KEY` is **valid** → DECIMA runs in full mode.
- If `OPENAI_API_KEY` is **empty** → DECIMA runs in Demo Mode (fallback).
- If `OPENAI_API_KEY` is **set but invalid** → DECIMA will raise an error 
  (`[ERROR:INVALID_API_KEY]`) and **will not fallback** to Demo Mode.

---


## 📦 Installation (via Docker)

### ✅ 0. Prerequisites

Make sure you have installed **Docker**:  
👉 [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

> 🐧 **Linux Users:**  
> You might need to run Docker commands with `sudo` unless you’ve added your user to the Docker group.  
> See: [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/)

---

### 🚀 1. Setup Steps

```bash
# Clone the repository
git clone https://github.com/quentinducasse/decima.git
cd decima
```

---

### 🛠️ 2. Configure your environment

Copy the Docker env template and fill in your API key:
Under Unix systems: 

```bash
cp .env.docker.example .env.docker
```
Under DOS systems: 
```bash
copy .env.docker.example .env.docker
```

Edit `.env.docker` with:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=        # ← Insert your API key

NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123
```

> ⚠️ Do **not** use `localhost` for `NEO4J_URI` — use the internal Docker service name (`neo4j`).

---

### 🐳 3. Build and launch DECIMA
Before running these commands:

- Windows / macOS → Start Docker Desktop.
- Linux → Ensure the Docker daemon is running (type 'sudo systemctl start docker' if needed).

Build and launch the containers

```bash
docker compose build app   # Only needed the first time, or if Dockerfile/requirements.txt change
docker compose up -d
```

This will automatically:
- Start a Neo4j container (ports 7474 + 7687)
- Start the DECIMA web server (port 5050)
- Mount your local source code into the container (`.:/app`) → any local code change is immediately visible

Load the Knowledge Graph:

```bash
docker compose exec app python kg/loader/neo4j_loader.py
```

---

### 🌐 4. Access the Interfaces

- Web App (DECIMA): [http://localhost:5050](http://localhost:5050)
- Neo4j Browser: [http://localhost:7474](http://localhost:7474)

> Log in with:  
> **Username:** `neo4j`  
> **Password:** `decima123`

---

## ▶️ After Installation: How to Use

### ▶️ Daily usage

### 1. Launch DECIMA in **normal mode** 

```bash
# Start the stack (Neo4j + DECIMA app)
docker compose up -d

# Load or reload the Knowledge Graph
# (this step must be repeated after each Neo4j rebuild or restart)
docker compose exec app python kg/loader/neo4j_loader.py

# Stop all services
docker compose down
```

> Use `sudo` in front of the commands above if you get a permission error on Linux.

Then open your browser and go to: [http://localhost:5050](http://localhost:5050)

---

### 1 (alternative). Launch DECIMA in **debug/verbose mode** 
 

```bash
# Start Neo4j only (in background)
docker compose up -d neo4j

# Load or reload the Knowledge Graph (inside the app container)
docker compose run --rm app python kg/loader/neo4j_loader.py

# Run the app with detailed logs
docker compose run --rm --service-ports app python app.py -v
```

- neo4j must be up before running the app  
- `--service-ports` ensures port `5050` is exposed  
- `-v` enables **verbose mode** (full logs, debug info, context sent to the LLM)  

➡️ Access the app at [http://localhost:5050](http://localhost:5050)  
---

## ✨ Example Usage

1. A sample PTRAC file is already provided in the repository for quick testing: 
This file is in **ASCII format** and can be used immediately to validate your installation.
The sample PTRAC file is located under the `data/ptrac_samples/` directory of your DECIMA installation:
`<DECIMA_INSTALL_DIR>/data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac`

2. Upload it or your own `.ptrac` file if desired. DECIMA currently supports **binary** and **ASCII** formats.  
*(Future releases will also support **HDF5 format**, commonly used for parallelized MCNP calculations.)*


3. Ask a natural language question like:

```text
Print x y z positions and energies of all events for the 20 first histories
```

4. DECIMA will:
   - Analyze the query
   - Use the KG for context
   - Generate and run code
   - Return structured results

---

## 📁 Project Structure

```
├── app.py
├── docker-compose.yml
├── Dockerfile
├── modules/        # QUIET, OTACON, EMMA, EVA...
├── kg/             # Knowledge Graph (triplets, loader)
├── frontend/       # Web interface (HTML/JS)
├── uploads/        # PTRAC files + plots
├── tools/          # Sandboxed code execution
├── mcnptools/      # Local copy of MCNPTools
├── data/           # Sample files
├── .env.docker.example
└── requirements.txt
```

---

## 📖 Documentation

See the [`doc/`](doc/) folder for:

- `DECIMA Project Technical Documentation.md`
- `DECIMA Project User Documentation.md`

---

## 📚 Citation

If you use DECIMA in your work, please cite the software as follows:

> Almuhisen F. and Ducasse Q., *DECIMA – Data Extraction & Contextual Inference for MCNP Analysis*,  
> Version v1.2.0, GitHub repository, 2025.  
> Available at: [https://github.com/quentinducasse/decima](https://github.com/quentinducasse/decima)

📌 A JOSS paper submission is in preparation. Once published, please update your citation to use the official DOI.

---

## 📜 License

DECIMA is distributed under the **Apache License 2.0 (OSI-approved, open source)**.  
See the [LICENSE](LICENSE) file for details.

📌 If you use DECIMA in academic work, please cite the upcoming JOSS paper (DOI pending).

DECIMA relies on third-party libraries distributed under permissive OSI-approved licenses (MIT, BSD, Apache, EPL). See NOTICE for details.

---

Author: Feda Almuhisen & Quentin Ducasse  
Project: DECIMA — Data Extraction & Contextual Inference for MCNP Analysis  
Year: 2025  

For commercial licensing inquiries (e.g., integration into a product, for-profit application), please contact the authors to discuss custom licensing terms.

---

## 🤝 Acknowledgments

- [MCNPTools (LANL)](https://github.com/lanl/mcnptools)
- [OpenAI](https://openai.com/)
- [Neo4j](https://neo4j.com/)

---

## 🚧 Roadmap

- [ ] **MCTAL analysis and plotting module**  
  Extend parsing to MCNP tally outputs with visualization.  

- [ ] **Batch processing**  
  Enable multiple PTRAC/MCTAL files to be analyzed in a single session for comparative studies.  

- [ ] **MCNP6+ compatibility**  
  Ensure robust parsing of outputs generated by the latest MCNP versions and HDF5 compatibility.  

- [ ] **Advanced reasoning features**  
  Integrate improved context handling, entity disambiguation, and domain-specific inference.  

- [ ] **… and extended features for much more precise answers 😉**  

---

## 📬 Contact

For questions, collaborations, or temporary API key requests, feel free to reach out on **LinkedIn**:  
👉 [Quentin Ducasse](https://www.linkedin.com/in/quentin-ducasse-a65410124/)  
👉 [Feda Almuhisen](https://www.linkedin.com/in/feda-almuhisen/)  