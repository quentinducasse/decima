# Bibliographic Review: Large Language Models and Monte Carlo Simulations in Nuclear Science

## 1. Introduction

The intersection of artificial intelligence (AI), particularly Large Language Models (LLMs), and nuclear science simulations, especially those employing Monte Carlo methods, represents a rapidly evolving field with significant potential for innovation. This review explores the current landscape of LLM applications in nuclear engineering, the established Monte Carlo simulation tools, and the existing methodologies for analyzing their outputs. It aims to contextualize the DECIMA project within this framework, highlighting its novelty and contribution to the domain.

## 2. Large Language Models in Nuclear Simulations

Recent advancements in LLMs have opened new avenues for automating complex scientific workflows and enhancing human-computer interaction in specialized domains. In nuclear engineering, LLMs are being explored for their capacity to interpret natural language queries, generate code, and assist in data analysis, thereby democratizing access to sophisticated simulation tools. Projects like AutoFLUKA [1] demonstrate the feasibility of using LLM-based frameworks to automate Monte Carlo simulation workflows in codes like FLUKA. This approach leverages AI agents to streamline tasks that traditionally require extensive manual intervention and expert knowledge.

Research presented at workshops, such as the AI for Nuclear Energy workshop at Oak Ridge National Laboratory, further emphasizes the growing interest in integrating LLMs into nuclear research to accelerate fusion and fission studies [2]. The potential extends to various applications, from automating simulation setups to interpreting complex results and even aiding in the design of nuclear systems. The ability of LLMs to process and generate human-like text makes them ideal candidates for creating more intuitive interfaces for highly technical software.

However, the application of LLMs in critical fields like nuclear science also presents challenges, including ensuring the accuracy and reliability of generated content, mitigating biases, and addressing the potential for 


hallucinations. The focus is on developing robust frameworks that embed domain-specific knowledge into LLM agents, as seen in efforts to automate Monte Carlo simulations with domain knowledge-embedded LLM agents [3].

## 3. Monte Carlo Simulation Tools in Nuclear Physics

Monte Carlo (MC) methods are indispensable in nuclear physics and engineering for simulating particle transport phenomena. Codes such as MCNP, FLUKA, GEANT4, and PHITS are widely used for their ability to model complex geometries and particle interactions with high fidelity. These codes are essential for applications ranging from reactor physics and shielding design to medical physics and space radiation protection.

*   **FLUKA (FLUktuierende KAskade):** A general-purpose tool for calculations of particle transport and interaction with matter, covering a wide range of applications from proton therapy to cosmic ray showers. Its capabilities include hadronic and electromagnetic shower development, neutron transport, and radionuclide production. Recent developments, such as AutoFLUKA, aim to automate its complex workflows using AI [1].

*   **GEANT4 (GEometry ANd Tracking):** A comprehensive toolkit for simulating the passage of particles through matter. Written in C++, GEANT4 is highly modular and extensible, making it a popular choice for high-energy physics experiments, medical imaging, and space science. Comparisons between GEANT4 and other codes like PHITS and MCNP are common to validate their accuracy across various scenarios [4, 5, 6].

*   **MCNP (Monte Carlo N-Particle):** Developed at Los Alamos National Laboratory, MCNP is a general-purpose Monte Carlo code for simulating the transport of neutrons, photons, electrons, and other particles. It is renowned for its detailed geometry capabilities and extensive cross-section libraries. MCNP is a cornerstone for nuclear criticality safety, shielding analysis, and detector response simulations.

*   **PHITS (Particle and Heavy Ion Transport code System):** A general-purpose Monte Carlo particle transport code developed in Japan, capable of simulating the transport of various particles over a wide energy range. PHITS is often compared with FLUKA, GEANT4, and MCNP for benchmarking and validation purposes in diverse applications, including heavy ion transport and neutron spectra analysis [4, 5].

The inter-comparison and benchmarking of these codes are crucial for ensuring the reliability of simulation results across different nuclear applications [5, 6]. The continuous development of these tools, coupled with advancements in computational power, allows for increasingly accurate and complex simulations.

## 4. Analysis Tools for MCNP Outputs (mctal and ptrac)

MCNP simulations generate various output files, with `mctal` (Monte Carlo Tally) and `ptrac` (Particle Track) being among the most critical for detailed analysis. While `mctal` files contain summarized tally results, `ptrac` files provide detailed information about individual particle histories, including their position, energy, time, and event types. Analyzing these files often requires specialized tools due to their complex structure and large size.

Several tools and libraries have been developed to facilitate the post-processing and analysis of MCNP outputs:

*   **PyNE:** A comprehensive open-source nuclear engineering toolkit that includes functionalities for MCNP input and output interfaces. PyNE's `pyne.mcnp` module allows for parsing MCNP output data, making it a valuable resource for researchers [7].

*   **MCNPTools:** A C++ software library with Python bindings (via SWIG) specifically designed for streamlining MCNP runs, managing material definition data, and analyzing MCNP results. It offers capabilities to process MCNP outputs, including `ptrac` files, without the need for manual parsing [8, 9, 10]. The library's power lies in enabling users to write custom tools for specific analysis needs.

*   **f4enix's and other GitHub repositories:** The open-source community has contributed various scripts and tools for MCNP output analysis. Many GitHub repositories host Python scripts and other utilities for parsing `mctal` and `ptrac` files, performing data extraction, and visualizing results [11, 12, 13]. These often provide flexible solutions for specific analysis tasks.

*   **McTal:** A Python program designed to handle and visualize Monte Carlo data produced by MCNP, FLUKA, and PHITS. It provides an API to read data from `mctal` files, facilitating data manipulation and visualization [14].

*   **ptrac2root:** A converter that transforms MCNP `ptrac` output files into ROOT files, which are commonly used in high-energy physics for data analysis and visualization. This tool allows for leveraging the extensive analysis capabilities of the ROOT framework for MCNP `ptrac` data [15].

Despite the existence of these tools, the process of extracting specific information from `ptrac` files, especially in response to natural language queries, remains a challenge. This is where the DECIMA project introduces a significant innovation.

## 5. The DECIMA Project: Innovation and Integration

The DECIMA (Data Extraction & Contextual Inference for MCNP Analysis) project addresses the gap in intuitive and automated analysis of MCNP `ptrac` files. Its core innovation lies in transforming natural language user queries into executable Python code for data analysis, leveraging the `mcnptools` library. This approach significantly lowers the barrier to entry for engineers and researchers who may not have extensive programming expertise or in-depth knowledge of `ptrac` file structures.

DECIMA's innovative aspects include:

*   **Natural Language Interface:** By allowing users to pose questions in plain language, DECIMA democratizes access to complex simulation data, making advanced analysis accessible to a broader audience.
*   **LLM-driven Code Generation:** The integration of an LLM (OTACON module) to generate `mcnptools` Python code based on user queries and contextual information is a novel application in this domain. This automates the creation of analysis scripts, reducing manual coding effort and potential errors.
*   **Knowledge Graph Integration:** The EMMA module's use of a Neo4j Knowledge Graph to enrich queries with contextual information about `mcnptools` classes, enumerations, and relationships ensures that the LLM generates accurate and semantically relevant code. This contextual awareness is crucial for mitigating LLM hallucinations in a highly technical domain.
*   **Modular and Orchestrated Architecture:** DECIMA's modular design, orchestrated by CAMPBELL using LangGraph, provides a robust, flexible, and maintainable system. This architecture allows for easy integration of new functionalities or replacement of existing modules, ensuring future adaptability.
*   **Secure Execution Environment:** The EVA module's sandboxed execution of generated Python code ensures the security and reliability of the system, preventing unintended side effects or system compromises.

DECIMA integrates seamlessly into the existing ecosystem of nuclear simulation and analysis by enhancing the usability of `mcnptools` and similar libraries. It acts as an intelligent assistant, bridging the gap between user intent and the technical intricacies of `ptrac` file analysis. Its ability to automate data extraction and processing tasks, which are typically tedious and error-prone, represents a significant step forward in streamlining nuclear data analysis workflows.

## References

[1] AutoFLUKA: A Large Language Model Based Framework for Automating Monte Carlo Simulation Workflows in FLUKA. arXiv preprint arXiv:2410.15222.

[2] Almeldein, A., Alnaggar, M., Archibald, R., Beck, T., et al. (2025). Exploring the Capabilities of the Frontier Large Language Models for Nuclear Energy Research. arXiv preprint arXiv:2506.19863.

[3] Ndum, Z. N., Tao, J., Ford, J., & Liu, Y. (2025). Automating Monte Carlo simulations in nuclear engineering with domain knowledge-embedded large language model agents. Energy and AI, 6, 100127.

[4] Comparison between PHITS and GEANT4 Simulations of the Heavy Ion Transport in Water. PMC, 2021.

[5] Çelik, Y., Stankovskiy, A., Iwamoto, H., Iwamoto, Y., et al. (2025). Built-in physics models and proton-induced nuclear data validation using MCNP, PHITS, and FLUKA–Impact on the shielding design for proton accelerator facilities. Annals of Nuclear Energy.

[6] Blideanu, V., Besnard-Vauterin, C., Horvath, D., et al. (2024). Neutron spectra from photonuclear reactions: Performance testing of Monte-Carlo particle transport simulation codes. Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms, 552, 1-10.

[7] PyNE Documentation. MCNP Input and Output Interfaces – pyne.mcnp. Available at: https://pyne.io/pyapi/mcnp.html

[8] MCNPTools GitHub Repository. Available at: https://github.com/lanl/mcnptools

[9] Solomon, B., & Bates, B. (2017). The MCNPTools Package: Installation and Use. LANL Technical Report LA-UR-17-21779.

[10] Bolding, J., Kulesza, A., et al. (2021). Particle Track Output (PTRAC) Improvements, Parallelism, and Post-Processing. LANL Technical Report LA-UR-21-26562.

[11] sellitforcache/MCNPtools GitHub Repository. Available at: https://github.com/sellitforcache/MCNPtools

[12] ChiefInformationSecurityOfficer/Nuclear-engineering-toolbox/mcnp.py GitHub Repository. Available at: https://github.com/ChiefInformationSecurityOfficer/Nuclear-engineering-toolbox/blob/main/mcnp.py

[13] MCNP Devel GitHub Repository. Available at: https://github.com/MCNP-Devel

[14] Zakalek, P. McTal GitLab Repository. Available at: https://iffgit.fz-juelich.de/zakalek/mctal

[15] bl0x/ptrac2root GitHub Repository. Available at: https://github.com/bl0x/ptrac2root

