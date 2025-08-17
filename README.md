<p align="center">
  <img src="decima_logo.png" width="250"/>
</p>

# DECIMA
**Data Extraction & Contextual Inference for MCNP Analysis**

> Powered by LLMs, Knowledge Graphs, and MCNPTools  
> Simple. Portable. Ready-to-run via Docker.

---

## 📦 Installation (via Docker)

### ✅ Prerequisites

Make sure you have installed **Docker Desktop**:  
👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

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

Then edit the file `.env.docker`:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...   # ← Insert your own API key

NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123
```

> ⚠️ Do **not** use `localhost` for `NEO4J_URI` — the app uses the internal Docker service name (`neo4j`).

---

### 🐳 3. Run DECIMA via Docker

```bash
docker compose up --build -d
```

This will automatically:
- Start a Neo4j container (port 7687 + web UI on 7474)
- Build a Docker image with all Python scripts and dependencies (including `mcnptools`)
- Launch the Flask web server (port 5050)

Then load the Knowledge Graph:

```bash
docker exec -it decima-app-1 python kg/loader/neo4j_loader.py
```

---

### 🌐 Access the Web App

- DECIMA interface: [http://localhost:5050](http://localhost:5050)
- Neo4j interface (Knowledge Graph): [http://localhost:7474](http://localhost:7474)

> Log in with:  
> **Username:** `neo4j`  
> **Password:** `decima123`

---

## ✨ Example Use

1. Upload your `.ptrac` file (ASCII or binary)
2. Ask a query like:

```text
What is the energy and position of all electrons crossing surface 30?
```

3. DECIMA will:
   - Analyze your query via QUIET
   - Extract context using EMMA (graph)
   - Generate Python code via OTACON (LLM)
   - Execute it safely via EVA
   - Return results + plots (if applicable)

---

## 🧠 Features

- 💬 Multilingual interface (EN / FR)
- 🔍 Intelligent PTRAC file analysis
- 📚 MCNP Knowledge Graph (Neo4j)
- 🤖 LLM-based Python code generation
- 🔐 Secure sandbox execution
- 📈 ASCII and graphical visualizations

---

## 📁 Project Structure

```
├── app.py                 # Main Flask backend
├── docker-compose.yml     # Docker orchestration
├── Dockerfile             # Docker image build
├── modules/               # QUIET, EMMA, OTACON, EVA, etc.
├── kg/                    # KG triplets and graph files
├── frontend/              # HTML / CSS / JS
├── uploads/               # User PTRAC files
├── tools/                 # Sandbox code execution
├── utils/                 # Keyword and prompt files
├── data/                  # Sample MCNP files
├── .env.docker.example    # Sample Docker environment file
└── requirements.txt       # Python dependencies
```

---

## 📖 Documentation

See the [`doc/`](doc/) folder for more:

- `DECIMA Project Technical Documentation.md`
- `DECIMA Project User Documentation.md`

---

## 📚 Citation

> Ducasse Q., *DECIMA – An LLM-based assistant for MCNP particle tracking analysis*, v1.0.1, GitHub, 2025-08-17.  
> [https://github.com/quentinducasse/decima](https://github.com/quentinducasse/decima)

---

## 🔖 License

**CC-BY 4.0** – Free to use, adapt, and redistribute **with attribution**.  
Please credit the original author in any derived publication or tool.

---

## 🤝 Acknowledgments

- [MCNPTools](https://github.com/lanl/mcnptools) (LANL)
- [OpenAI](https://openai.com/) & [ASI:One](https://asi.one/)
- [Neo4j](https://neo4j.com/)

---

## 🚧 Roadmap

- [ ] MCTAL integration (FORTUNE)
- [ ] Batch mode for processing multiple files
- [ ] Public web interface (key-restricted)
- [ ] MCNP6/6.2 and alt formats support

---