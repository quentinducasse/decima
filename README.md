<p align="center">
  <img src="decima_logo.png" width="250"/>
</p>

# DECIMA
**Data Extraction & Contextual Inference for MCNP Analysis**

> Powered by LLMs, Knowledge Graphs, and MCNPTools

---

## 📦 Installation

Choose one of the following:

- [🔵 Windows (via `.bat` script)](#option-1--windows)
- [🟢 Linux/macOS (via terminal)](#option-2--linux--macos)
- [🐳 Docker (all platforms)](#option-3--docker)

---

### 🔵 OPTION 1 – Windows

> **🔧 Recommended for Windows users**

```bash
# 1. Clone the repository
git clone https://github.com/quentinducasse/decima.git
cd decima
```

```bash
# 2. Create a .env file at the root of the project (REQUIRED)
```

Example `.env` file:
```env
OPENAI_API_KEY=sk-...
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123
```

# 3. Install Neo4j Desktop

- Download Neo4j Desktop: https://neo4j.com/download
- Create a database named `decima graph` and start it
- Default credentials (editable in the `.env` file created in the previous step):
  - URI: `bolt://localhost:7687`
  - Username: `neo4j`
  - Password: `decima123`

```bash
# 4. Run:
decima_start.bat
```

This script will:
- Check for Python and the virtual environment
- Open Neo4j Desktop (if installed in default location)
- Prompt you to start the Neo4j DBMS (e.g., `decima graph`)
- Load the Knowledge Graph
- Launch the DECIMA web app at http://127.0.0.1:5050

> ⚠️ You must create the `.env` file **before running the script**  
> You can reuse `decima_start.bat` each time you start DECIMA.

---

### 🟢 OPTION 2 – Linux / macOS

> **🔧 Recommended for Unix/macOS users**

```bash
# 1. Clone the repository
git clone https://github.com/quentinducasse/decima.git
cd decima

# 2. Create and activate a virtual environment
python3 -m venv decima_env
source decima_env/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Create a .env file at the project root
```

Example `.env` file:
```env
OPENAI_API_KEY=sk-...
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=yourpassword
```

```bash
# 5. Launch Neo4j Desktop and start your database (e.g., decima graph)

# 6. Load the Knowledge Graph into Neo4j
python kg/loader/neo4j_loader.py

# 7. Start the DECIMA web app
python app.py
```

Then open your browser at [http://127.0.0.1:5050](http://127.0.0.1:5050)

---

### 🐳 OPTION 3 – Docker (All Platforms)

> **💻 Recommended for advanced users and developers**

```bash
# 1. Clone the repository
git clone https://github.com/quentinducasse/decima.git
cd decima

# 2. Copy and edit the .env file
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```env
OPENAI_API_KEY=sk-...
```

```bash
# 3. Launch DECIMA with Docker
docker-compose up --build
```

This will:
- Start a Neo4j container (port 7687)
- Build and run the DECIMA app (port 5050)

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

## 🧠 Features

- 💬 Ask queries in natural language (English or French)
- 🧠 Auto-detection of particle events, data, and reaction types
- 📚 Context enrichment via a structured **Knowledge Graph**
- 🤖 Code generation via **LLM** (OpenAI GPT, ASI1, etc.)
- 🔐 Secure code execution in sandboxed Python environment
- 🖼️ Plotting and data visualization (ASCII or image output)
- 🧪 Tested with both ASCII and Binary PTRAC files via `mcnptools`

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

---

## 📚 How to Cite DECIMA

> Ducasse Q., *DECIMA – An LLM-based assistant for MCNP particle tracking analysis*, v1.0.0, GitHub, 2025-08-15.  
> Available: [https://github.com/quentinducasse/decima](https://github.com/quentinducasse/decima)

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