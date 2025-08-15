<p align="center">
  <img src="decima_logo.png" width="250"/>
</p>

# DECIMA
**Data Extraction & Contextual Inference for MCNP Analysis**

> Powered by LLMs, Knowledge Graphs, and MCNPTools  
## 🧠 About DECIMA

**DECIMA** (Data Extraction & Contextual Inference for MCNP Analysis) is an intelligent assistant that helps you parse, analyze, and interpret MCNP **PTRAC files** using natural language queries. It integrates a contextual Knowledge Graph (Neo4j), a secure execution sandbox, and a powerful LLM backend for **automated code generation and data analysis**.

Designed for nuclear engineers and researchers, DECIMA makes particle tracking **transparent, accessible, and no-code friendly**.

---

## 🚀 Features

- 💬 Ask queries in natural language (English or French)
- 🧠 Auto-detection of particle events, data, and reaction types
- 📚 Context enrichment via a structured **Knowledge Graph**
- 🤖 Code generation via **LLM** (OpenAI GPT, ASI1, etc.)
- 🔐 Secure code execution in sandboxed Python environment
- 🖼️ Plotting and data visualization (ASCII or image output)
- 🧪 Tested with both ASCII and Binary PTRAC files via `mcnptools`

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
```

### 2. Create and activate a virtual environment

```bash
python -m venv decima_env
source decima_env/bin/activate  # or decima_env\Scripts\activate on Windows
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file at the project root

```env
OPENAI_API_KEY=sk-...
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=yourpassword
```

---

## 🧠 Load the Knowledge Graph

Before starting the app, load DECIMA's Knowledge Graph into Neo4j:

```bash
python kg/loader/neo4j_loader.py
```

---

## 💻 Run the Web App

```bash
python app.py
```

Then open your browser at [http://127.0.0.1:5050](http://127.0.0.1:5050)

---

## ✨ Example Use

1. Upload your `.ptrac` file (ASCII or binary)
2. Ask a query, such as:

```text
What is the energy and position of all electrons crossing surface 30?
```

3. DECIMA will:
    - Parse your query via QUIET
    - Enrich context using EMMA (Knowledge Graph)
    - Generate code with OTACON (LLM)
    - Execute it safely with EVA
    - Return answers + plots (if applicable)

---

## 🧩 Architecture Overview

DECIMA uses a modular LangGraph-based agent system:

- `QUIET`: Language detection & focus extraction
- `EMMA`: Knowledge Graph contextual retrieval
- `OTACON`: LLM-based response & code generation
- `EVA`: Code execution & output retrieval
- `CAMPBELL`: Main orchestrator (LangGraph)
- `Frontend`: Flask web interface (JS/HTML/CSS)

All communication is orchestrated via the `campbell.py` pipeline.

---

## 📁 Project Structure

```
├── app.py                 # Flask backend entry point
├── modules/               # QUIET, EMMA, OTACON, EVA, CAMPBELL
├── kg/                    # Neo4j KG and triplets
├── frontend/              # HTML/CSS/JS interface
├── data/                  # Example files (PTRAC/MCTAL)
├── uploads/               # User PTRAC uploads
├── utils/                 # Keywords, lexicons, LLM prompts
├── tests/                 # Test suites
├── tools/                 # Secure sandbox for execution
├── requirements.txt
└── .env                   # API keys (not committed)
```

---

## 📖 Documentation

See full user and technical docs in the [`doc/`](doc/) folder:

- `DECIMA Project Technical Documentation.md`
- `DECIMA Project User Documentation.md`

---

## 🔖 License

This project is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.  
Feel free to use, adapt and cite — but **credit the original authors**.

For citation and DOI, see next section.

---

## 📚 How to Cite DECIMA

> Ducasse Q., *DECIMA – An LLM-based assistant for MCNP particle tracking analysis*, v1.0.0, GitHub, 2025-08-15.  
> Available: [https://github.com/quentinducasse/decima](https://github.com/quentinducasse/decima)

You may generate a DOI via **Zenodo** for formal citation.

---

## 🤝 Acknowledgements

DECIMA is a personal research project developed by [@quentinducasse](https://github.com/quentinducasse), with guidance from nuclear AI specialists. The project uses:

- `mcnptools` (Los Alamos) for PTRAC parsing
- OpenAI / ASI1 for LLM code generation
- Neo4j for Knowledge Graph inference

---

## 💡 Roadmap

- [ ] Add support for MCNP input/output parsing
- [ ] Include MCTAL viewer (FORTUNE) in frontend
- [ ] Deploy public version with limited LLM calls
- [ ] Connect Zenodo for version DOI tracking

---

## 🐛 Issues / Suggestions

Feel free to open issues or pull requests. For private collaboration, contact the project author.

---

