# DECIMA Installation Guide

This guide covers the installation and setup of DECIMA using Docker.

---

## Prerequisites

### Required Software
- **Docker**: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

### API Keys (Recommended)
- **OpenAI API Key**: Get one at [OpenAI Platform](https://platform.openai.com/api-keys)
- **Note**: There is a demo mode available without API key (see below)

### Important Notes
> **Linux Users:** You might need to run Docker commands with `sudo` unless you've added your user to the Docker group. See: [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/)

---

## Docker Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
```

### Step 2: Configure Environment

Copy the Docker environment template:

**Unix systems:**
```bash
cp .env.docker.example .env.docker
```

**Windows systems:**
```bash
copy .env.docker.example .env.docker
```

Edit `.env.docker` with your configuration:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here        # ← Insert your API key

NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=decima123

# Demo mode flag (set to true for fallback without API key)
DEMO_MODE=false
```

### Step 3: Build and Launch

Before running these commands:
- **Windows** → Start Docker Desktop
- **Linux** → Ensure the Docker daemon is running

```bash
# Build the containers (first time only)
docker compose build app

# Start all services
docker compose up -d
```

This will automatically:
- Start a Neo4j container (ports 7474 + 7687)
- Start the DECIMA web server (port 5050)
- Mount your local source code into the container

### Step 4: Load the Knowledge Graph

```bash
docker compose exec app python kg/loader/neo4j_loader.py
```

### Step 5: Access the Application

After all containers are running, you can access DECIMA:

- **DECIMA Web App**: [http://localhost:5050](http://localhost:5050)
- **Neo4j Browser**: [http://localhost:7474](http://localhost:7474)

**Neo4j Login Credentials** (for information):
- Username: `neo4j`
- Password: `decima123`

---

## Daily Usage

### Standard Mode

Start the entire DECIMA stack:
```bash
docker compose up -d
```

Load or reload the Knowledge Graph (required after Neo4j restarts):
```bash
docker compose exec app python kg/loader/neo4j_loader.py
```

Stop all services when done:
```bash
docker compose down
```

### Debug/Verbose Mode

Start only Neo4j in the background:
```bash
docker compose up -d neo4j
```

Load the Knowledge Graph:
```bash
docker compose run --rm app python kg/loader/neo4j_loader.py
```

Run the application with detailed logs:
```bash
docker compose run --rm --service-ports app python app.py -v
```

**Debug mode provides:**
- Full logs and debug information
- Context sent to the LLM is visible
- Detailed workflow inspection

---

## Troubleshooting

### Docker Issues

**Permission denied (Linux):**
```bash
# Option 1: Use sudo
sudo docker compose up -d

# Option 2: Add user to docker group
sudo usermod -aG docker $USER
# Then logout and login again
```

**Port conflicts:**
```bash
# Check what's using the ports
netstat -tulpn | grep :5050
netstat -tulpn | grep :7474
netstat -tulpn | grep :7687

# Stop conflicting services or change ports in docker-compose.yml
```

**Build failures:**
```bash
# Clean rebuild
docker compose down
docker compose build --no-cache app
docker compose up -d
```

### Neo4j Issues

**Connection refused:**
```bash
# Check if Neo4j is running
docker compose ps

# Check Neo4j logs
docker compose logs neo4j

# Restart Neo4j
docker compose restart neo4j
```

**Knowledge Graph not loading:**
```bash
# Reload the KG
docker compose exec app python kg/loader/neo4j_loader.py

# If that fails, check Neo4j browser at http://localhost:7474
```

### API Key Issues

**Invalid API key error:**
- Verify your OpenAI API key is correct
- Check you have sufficient credits on your OpenAI account
- Ensure no extra spaces in `.env.docker`

**Want to test without API key:**
```bash
# Set demo mode in .env.docker
DEMO_MODE=true
OPENAI_API_KEY=

# Or leave OPENAI_API_KEY empty for automatic demo mode
```

---

## Next Steps

After successful installation, you should see the DECIMA interface when you visit [http://localhost:5050](http://localhost:5050).

### Getting Started

**1. Test with Sample Data**
- Use the provided PTRAC file: `data/ptrac_samples/basic_ptrac_example_decima_ascii.ptrac`
- This ASCII format file is ready to use immediately for validation

**2. Load Your Own PTRAC File**
- Click the "Load PTRAC File" button
- Supports both binary and ASCII PTRAC formats
- File will be uploaded and ready for analysis

**3. Try Example Queries**

Use one of the suggested queries from the interface:

```text
Print x y z positions and energies of all the particles entering the Water moderator (cell 502)
```

```text
How many secondary photons are emitted and what is their process of termination?
```

```text
Plot the z-axis direction cosine (W) distribution of emitted source particles and display their average energy
```

**4. Experiment with Your Own Questions**
- Ask in natural language (English or French)
- Be specific about what data you want to extract
- DECIMA will generate Python code and execute it for you

**5. Explore Advanced Features**
- Toggle "Add context" to see how the Knowledge Graph affects responses
- Switch between `gpt-4o-mini` and `gpt-4o` models
- Use verbose mode for debugging: `docker compose run --rm --service-ports app python app.py -v`

### Understanding the Interface

- **OTACON Character**: Your AI assistant for PTRAC analysis
- **Model Selection**: Choose between OpenAI models
- **Add Context**: Toggle Knowledge Graph context injection
- **Example Queries**: Pre-written questions to get you started
- **Chat Area**: Where conversations and code appear
- **Execution Results**: Output from the generated Python code

---

## Getting Help

For support and questions:
- Check the troubleshooting section above
- Review the documentation in `doc/`
- Contact the development team via LinkedIn (see main README)