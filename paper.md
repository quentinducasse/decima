---
title: 'DECIMA: Data Extraction & Contextual Inference for MCNP Analysis'
tags:
  - nuclear simulation
  - Monte Carlo
  - MCNP
  - PTRAC
  - MCTAL
  - knowledge graph
  - large language models
authors:
  - name: Quentin Ducasse
    orcid: 0000-000X-XXXX-XXXX
    affiliation: "1"
  - name: Feda Alumhisen
    orcid: 0000-000X-XXXX-XXXX
    affiliation: "2"
affiliations:
  - name: Institut de Radioprotection et de Sûreté Nucléaire (IRSN), France
    index: 1
  - name: Artificial Intelligence Research Group, France
    index: 2
date: 18 September 2025
bibliography: paper.bib
---

# Summary

DECIMA (**Data Extraction & Contextual Inference for MCNP Analysis**) is an open-source framework
for the analysis of Monte Carlo N-Particle (MCNP) outputs. It integrates **MCNPTools** for access to
binary `PTRAC` and `MCTAL` files, a **Neo4j knowledge graph** for contextual reasoning, and **Large Language Models (LLMs)**
to enable natural language querying in English or French.  
DECIMA automatically translates user queries into executable Python code, runs them securely in a sandbox, and returns
structured results with explanations. A modular architecture inspired by *Metal Gear Solid* (QUIET, EMMA, OTACON, EVA, CAMPBELL)
ensures transparency, extensibility, and safe execution.  
The project is distributed under a dual license (MIT for academic use, with optional commercial licensing).

# Statement of need

MCNP is a widely used Monte Carlo transport code in nuclear engineering and physics. Its outputs
(`PTRAC`, `MCTAL`) contain detailed information on particle histories and tallies, but parsing and
analyzing them requires substantial coding effort and expertise. Existing solutions such as **MCNPTools**
[@mcnptools2022], **Easy-PTRAC** [@easyptrac2018], and community packages like **PyNE** [@pyne2019],
**SANDY** [@sandy2021], **F4Enix** [@f4enix2021], and **mc-tools** [@mctools2020] provide valuable
low-level access, but they impose a steep learning curve and can lead to fragmented workflows.

DECIMA addresses this challenge by introducing an integrated assistant that combines:
1. **Natural language query interpretation (QUIET)**,  
2. **Knowledge graph context for entity disambiguation (EMMA)**,  
3. **LLM-based reasoning and code synthesis (OTACON)**,  
4. **Secure execution of generated code (EVA)**,  
5. **Workflow orchestration and web interface (CAMPBELL)**.  

With this pipeline, DECIMA lowers the barrier for students, engineers, and researchers, making advanced
analyses of MCNP outputs reproducible, auditable, and accessible.

# Software description

DECIMA follows a modular design:

- **QUIET**: Extracts entities and focus events from user queries (FR/EN).  
- **EMMA**: Provides contextual knowledge from a Neo4j graph populated with MCNPTools triplets.  
- **OTACON**: Generates explanations and Python code using LLMs (OpenAI, ASI1).  
- **EVA**: Executes code securely in a sandbox.  
- **CAMPBELL**: Orchestrates the workflow and exposes a web interface (Flask + JS).  

Deployment is simplified via **Docker**. A **demo mode** is included, allowing reviewers and users to run DECIMA
without API keys (using a fixed example script).

![DECIMA architecture](decima_logo.png)

# Example usage

After installation:

```bash
git clone https://github.com/quentinducasse/decima.git
cd decima
docker compose up -d
see README.txt for complete walkthrough
```

Access the web interface at http://localhost:5050

. Example queries:

    “Display x, y, z positions and energies of neutrons crossing surface 12.”

    “How many secondary photons are emitted in inelastic scattering?”

    “What is the energy spectrum of fission neutrons?”

DECIMA returns:

    An explanation,

    Executable Python code using mcnptools,

    Results (stdout, stderr, plots).

Related work

Several tools support MCNP output processing:

    MCNPTools (LANL) [@mcnptools2022]: reference C++/Python library for parsing MCTAL, MESHTAL, PTRAC.

    Easy-PTRAC (IRSN) [@easyptrac2018]: GUI for filtering particle histories and exporting results.

    mc-tools (community, GitHub) [@mctools2020]: Python converters (mctal2root, mctal2txt).

    F4Enix (Fusion for Energy) [@f4enix2021]: modular Python package for MCNP input/output workflows.

    SANDY [@sandy2021]: parses MCTAL tallies into pandas DataFrames.

    PyNE [@pyne2019]: includes MCNP mesh tally parsers and a PtracReader.

    MCNPy [@mcnpy2022]: Python API for MCNP input deck manipulation.

    Easy-PERT [@easypert2020]: perturbation tool combining MCNPTools and Faust.

DECIMA builds on these but is unique in combining Knowledge Graph reasoning and LLM-based interaction, enabling
human-like queries, automatic code generation, and safe execution.
Acknowledgements

We thank the MCNPTools developers at LANL, the IRSN LMDN group for providing access to Easy-PTRAC,
and collaborators in AI-assisted neutron metrology. This project also acknowledges Neo4j, OpenAI, and ASI1.
References