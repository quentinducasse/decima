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

```bash
# 2. Create a .env file at the project root (REQUIRED)
```
At the root of the project, create a .env file that will contain your API key and Neo4j settings.
You can do it manually, or by running the following command in your terminal:

Example `.env`:
```env
echo "# LLM (OTACON)" >> .env
echo "LLM_PROVIDER=openai" >> .env
echo "OPENAI_API_KEY=sk-..." >> .env
echo "" >> .env
echo "# Neo4j (EMMA)" >> .env
echo "NEO4J_URI=bolt://localhost:7687" >> .env
echo "NEO4J_USER=neo4j" >> .env
echo "NEO4J_PASSWORD=decima123" >> .env
```
You can replace OPENAI_API_KEY=sk-... with your own OpenAI API key.

> ⚠️ This file is **required** before launching the app.

---

### 🐳 3. Run DECIMA via Docker

```bash
docker compose up --build -d
```

This will automatically:
- Start a **Neo4j** container (port 7687 + web UI on 7474)
- Build the app container with:
  - Python 3.10
  - Flask, MCNPTools (compiled from source)
  - All required Python dependencies
- Launch the Flask web interface (port 5050)

---

### 🌐 Access the Web App

- DECIMA interface → [http://localhost:5050](http://localhost:5050)
- Neo4j Web UI → [http://localhost:7474](http://localhost:7474)

Login credentials:
```
Username: neo4j
Password: decima123
```

---

## 🧠 Load the Knowledge Graph

Once the containers are running, load the graph data by executing:

```bash
docker exec -it decima-app-1 python kg/loader/neo4j_loader.py
```

---

## ✨ Example Use

1. Upload your `.ptrac` file (ASCII or binary)
2. Ask a question like:

```text
What is the energy and position of all electrons crossing surface 30?
```

3. DECIMA will:
   - Parse your request using **QUIET**
   - Retrieve relevant nodes from **EMMA** (Neo4j KG)
   - Use **OTACON** (LLM) to generate Python code
   - Execute that code in a secure **EVA** sandbox
   - Display structured results and plots

---

## 🧠 Features

- 💬 Multilingual interface (EN / FR)
- 🔍 Smart PTRAC parsing (via MCNPTools)
- 📚 Graph-powered inference engine
- 🤖 LLM-driven code generation (OpenAI, ASI:One, etc.)
- 🔐 Secure sandbox execution (Python only)
- 📈 Data visualization (ASCII or graphical)

---

## 🧰 MCNPTools Integration (C++ + Python)

DECIMA includes MCNPTools **compiled locally inside the image**, with Boost, HDF5, and SWIG.  
No manual installation is needed.

Example usage in Python:

```python
from mcnptools import Ptrac
ptrac = Ptrac("myfile.ptrac")
ptrac.ReadHistories(10000)
```

---

## 📁 Project Structure

```
├── app.py                 # Main Flask backend
├── docker-compose.yml     # Docker orchestration
├── Dockerfile             # Docker image build
├── .env.docker            # Default Docker env vars
├── modules/               # QUIET, EMMA, OTACON, EVA
├── kg/                    # KG triplets and graph loader
│   └── loader/
│       └── neo4j_loader.py
├── mcnptools/             # Local clone from LANL (required)
├── frontend/              # HTML / CSS / JS interface
├── uploads/               # User-submitted files
├── tools/                 # Code execution sandbox
├── utils/                 # Keywords, prompts
├── data/                  # Sample MCNP files
├── .env                   # LLM + Neo4j credentials
└── requirements.txt       # Python dependencies
```

---

## 📖 Documentation

See the [`doc/`](doc/) folder for:

- `DECIMA Project Technical Documentation.md`
- `DECIMA Project User Documentation.md`

---

## 📚 Citation

> Ducasse Q., *DECIMA – An LLM-based assistant for MCNP particle tracking analysis*, v1.0.0, GitHub, 2025-08-15.  
> [https://github.com/quentinducasse/decima](https://github.com/quentinducasse/decima)

---

## 🔖 License

**CC-BY 4.0** – Free to use, adapt, and redistribute **with attribution**.  
Please cite the original author in any derived publication or tool.

---

## 🤝 Acknowledgments

- [MCNPTools](https://github.com/lanl/mcnptools) (LANL)
- [OpenAI](https://openai.com/) & [ASI:One](https://asi.one/)
- [Neo4j](https://neo4j.com/)
- [Boost](https://www.boost.org/) + [HDF5](https://portal.hdfgroup.org/display/support)

---

## 🧭 Roadmap

- [x] 🐳 Docker support with MCNPTools prebuilt
- [x] KG loader integration inside container
- [x] OpenAI + ASI support via .env
- [ ] MCTAL file visualization (FORTUNE)
- [ ] Batch PTRAC processing
- [ ] Public online version (API key restricted)
- [ ] MCNP6/6.2 + alternative file formats

---