
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

## 📦 Installation (via Docker)

### ✅ Prerequisites

Make sure you have installed **Docker**:  
👉 [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

> 🐧 **Linux Users:**  
> You might need to run Docker commands with `sudo` unless you’ve added your user to the Docker group.  
> See: [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/)

---

### 🚀 Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/quentinducasse/decima.git
cd decima
```

---

### 🛠️ 2. Configure your environment

Copy the Docker env template and fill in your API key:

```bash
cp .env.docker.example .env.docker
```

Edit `.env.docker` with:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...   # ← Insert your API key

NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123
```

> ⚠️ Do **not** use `localhost` for `NEO4J_URI` — use the internal Docker service name (`neo4j`).

---

### 🐳 3. Build and launch DECIMA

```bash
docker compose up --build -d
```

This will automatically:
- Start a Neo4j container (ports 7474 + 7687)
- Build the image with all Python tools and `mcnptools`
- Launch the web server (port 5050)

Load the Knowledge Graph:

```bash
docker exec -it decima-app-1 python kg/loader/neo4j_loader.py
```

---

### 🌐 Access the Interfaces

- Web App (DECIMA): [http://localhost:5050](http://localhost:5050)
- Neo4j Browser: [http://localhost:7474](http://localhost:7474)

> Log in with:  
> **Username:** `neo4j`  
> **Password:** `decima123`

---

## ▶️ After Installation: How to Use

### 1. Launch DECIMA (default: **silent mode**)  
```bash
# Start the containers
docker compose up -d

# Load or reload the KG
docker exec -it decima-app-1 python kg/loader/neo4j_loader.py


# Stop all services
docker compose down -v
```

> Use `sudo` in front of the commands above if you get a permission error on Linux.

Then open your browser and go to: [http://localhost:5050](http://localhost:5050)

---

### 2. Launch DECIMA in **verbose/debug mode**  
If you want to see **detailed logs, workflow steps, and full LLM context**, run:  

```bash
docker compose run --service-ports app python app.py -v
```

- `--service-ports` ensures port `5050` is exposed  
- `-v` enables **verbose mode** (full logs, debug info, context sent to the LLM)  

➡️ Access the app at [http://localhost:5050](http://localhost:5050)  
---

## ✨ Example Usage

1. Upload your `.ptrac` file
2. Ask a natural language question like:

```text
Print x y z positions and energies of neutrons entering surface 401 for the 20 first histories
```

3. DECIMA will:
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
├── uploads/        # PTRAC files
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

> Ducasse Q., *DECIMA – An LLM-based assistant for MCNP particle tracking analysis*, v1.0.1, GitHub, 2025-08-17.  
> [https://github.com/quentinducasse/decima](https://github.com/quentinducasse/decima)

---

Creative Commons Attribution-NonCommercial 4.0 International Public License (CC BY-NC 4.0)

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial 4.0 International Public License ("Public License").

You are free to:
✔ Share — copy and redistribute the material in any medium or format
✔ Adapt — remix, transform, and build upon the material

Under the following terms:
📌 Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
🚫 NonCommercial — You may not use the material for commercial purposes.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Full license text: https://creativecommons.org/licenses/by-nc/4.0/legalcode

---

Author: Quentin Ducasse  
Project: DECIMA — Data Extraction & Contextual Inference for MCNP Analysis  
Year: 2025  

For commercial licensing inquiries (e.g., integration into a product, for-profit application), please contact the author to discuss custom licensing terms.

---

## 🤝 Acknowledgments

- [MCNPTools (LANL)](https://github.com/lanl/mcnptools)
- [OpenAI](https://openai.com/) & [ASI:One](https://asi.one/)
- [Neo4j](https://neo4j.com/)

---

## 🚧 Roadmap

- [ ] MCTAL (FORTUNE) support
- [ ] Batch file processing
- [ ] Public access (key-restricted)
- [ ] MCNP6+ compatibility
