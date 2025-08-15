# Detailed Plan for Scientific Publication: DECIMA Project

**Title:** DECIMA: A Novel Framework for Natural Language-driven Analysis of MCNP PTRAC Data using Large Language Models

**Authors:** [Author Names]

**Abstract:**

This paper introduces DECIMA (Data Extraction & Contextual Inference for MCNP Analysis), a novel framework designed to automate the analysis of Monte Carlo N-Particle (MCNP) Particle Track (PTRAC) files through a natural language interface. The complexity and volume of data in PTRAC files present a significant barrier to entry for researchers and engineers who are not experts in both particle physics and programming. DECIMA addresses this challenge by leveraging a Large Language Model (LLM) to interpret user queries and generate executable Python code for data analysis using the `mcnptools` library. The system integrates a knowledge graph to provide the LLM with the necessary domain-specific context, thereby ensuring the generation of accurate and relevant analysis scripts. This approach democratizes access to complex simulation data, reduces the potential for manual errors, and significantly accelerates the data analysis workflow. We present the architecture of DECIMA, demonstrate its capabilities with use-case examples, and discuss its potential impact on the field of nuclear science and engineering.

**Keywords:** MCNP, PTRAC, Large Language Models, LLM, Monte Carlo, Natural Language Processing, Knowledge Graph, Automated Code Generation, Nuclear Engineering.

--- 

### **1. Introduction**

*   **1.1. The Challenge of MCNP Data Analysis:**
    *   Briefly introduce MCNP as a critical tool in nuclear science.
    *   Describe the nature and importance of PTRAC files for detailed particle history analysis.
    *   Highlight the difficulties in analyzing PTRAC files: large data volume, complex data structures, and the need for programming skills.

*   **1.2. The Rise of AI in Scientific Research:**
    *   Discuss the growing trend of applying AI, particularly LLMs, to automate and simplify complex scientific tasks.
    *   Mention existing work on LLMs in scientific domains and their potential for code generation and natural language interfaces.

*   **1.3. The DECIMA Solution:**
    *   Introduce the DECIMA project as a solution to the challenges mentioned.
    *   State the main objective: to enable researchers to query PTRAC data using natural language.
    *   Briefly outline the paper's structure.

### **2. Background and Related Work**

*   **2.1. Monte Carlo Simulations in Nuclear Physics:**
    *   Provide an overview of prominent Monte Carlo codes (MCNP, GEANT4, FLUKA, PHITS).
    *   Discuss their role in the nuclear industry and research.

*   **2.2. Existing Tools for MCNP Data Analysis:**
    *   Review existing tools for analyzing MCNP output files (e.g., PyNE, mcnptools, f4enix's, etc.).
    *   Identify their strengths and limitations, particularly in terms of user-friendliness and automation.

*   **2.3. Large Language Models in Scientific Code Generation:**
    *   Survey recent research on using LLMs to generate code for scientific applications.
    *   Discuss the challenges of ensuring accuracy and domain-specificity in LLM-generated code.
    *   Reference projects like AutoFLUKA to highlight the state-of-the-art.

### **3. The DECIMA Framework: An Architectural Overview**

*   **3.1. System Architecture:**
    *   Present a high-level diagram of the DECIMA architecture.
    *   Describe the modular design and the flow of information between components.

*   **3.2. Core Components (The AI Engine):**
    *   **QUIET:** Detail its role in query analysis and entity extraction.
    *   **EMMA:** Explain the knowledge graph integration and its importance for contextual enrichment.
    *   **OTACON:** Describe the LLM-based code generation, including prompt engineering and the use of contextual information.
    *   **EVA:** Detail the secure, sandboxed code execution environment.
    *   **CAMPBELL:** Explain the orchestration of the workflow using LangGraph.

### **4. The Physics Engine: MCNP PTRAC Analysis with `mcnptools`**

*   **4.1. The `mcnptools` Library:**
    *   Provide an overview of the `mcnptools` library and its capabilities for PTRAC file analysis.
    *   Explain the key classes and methods used by DECIMA.

*   **4.2. From Natural Language to Physics Analysis:**
    *   Present a case study showing how a user's natural language query is transformed into a specific physics analysis.
    *   Example: "What is the energy distribution of neutrons crossing surface 300?"
    *   Show the intermediate steps: QUIET's output, EMMA's context, OTACON's generated code.

*   **4.3. Validation and Verification:**
    *   Discuss the methods used to validate the correctness of the generated code and the analysis results.
    *   Compare results from DECIMA with manually written scripts for benchmark cases.

### **5. Results and Discussion**

*   **5.1. Performance Evaluation:**
    *   Assess the accuracy of the generated code across a range of queries with varying complexity.
    *   Evaluate the system's performance in terms of response time and resource usage.

*   **5.2. Innovations and Contributions:**
    *   Summarize the key innovations of the DECIMA project.
    *   Discuss how DECIMA advances the state-of-the-art in nuclear data analysis.

*   **5.3. Limitations and Future Work:**
    *   Acknowledge the current limitations of the system (e.g., complexity of supported queries, reliance on the underlying `mcnptools` library).
    *   Outline potential future developments, such as extending support to other MCNP output files (mctal), integrating other simulation codes, and enhancing the LLM's reasoning capabilities.

### **6. Conclusion**

*   Recap the main achievements of the DECIMA project.
*   Reiterate the significance of the work for the nuclear science and engineering community.
*   Provide a concluding vision for the future of AI-driven scientific discovery.

### **7. References**

*   A comprehensive list of all cited works in a standard academic format (e.g., IEEE, APA).

--- 

### **Appendices**

*   **Appendix A: The DECIMA User Interface:**
    *   Screenshots of the web interface.
    *   A brief description of the user workflow.

*   **Appendix B: Example of LLM Prompt and Output:**
    *   A complete example of the prompt provided to the OTACON module, including the system message, EMMA context, and user query.
    *   The corresponding raw output from the LLM, showing the natural language explanation and the generated Python code.

*   **Appendix C: Example of Generated Python Code:**
    *   A clean, well-commented example of a Python script generated by DECIMA for a specific analysis task.

*   **Appendix D: Knowledge Graph Schema:**
    *   A diagram or description of the schema used for the Neo4j knowledge graph, showing the different node types and relationships.


