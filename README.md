# ASL MRI Artifact Dictionary & Quality Control Foundations

## Introduction

This repository is developed as part of my preparation for **GSoC 2026**, aligned with **Project #7 – Quality Check Toolbox (ASL/DCE-related work)**.

The goal of this project is to build **foundational, reusable components for automated Quality Control (QC) in ASL MRI**, starting from a structured artifact knowledge base and evolving toward interactive, scalable tooling.

Rather than focusing on isolated scripts, this work emphasizes **standardization, reproducibility, and extensibility**, which are critical for research-grade QC systems.

The idea is to conceptually connect the two GSoC directions (AURA and the QC Toolbox), but without depending on the completion of Project 4. To ensure the platform remains functional and independent, I plan to implement a lightweight, integration-focused QC layer within my own project.

---

## Project Idea (In Brief)

Quality Control in ASL MRI relies heavily on expert interpretation of artifacts such as motion, labeling failure, low SNR, and background suppression issues.  
However, this expertise is often undocumented, inconsistent, or scattered across literature.

This project addresses that gap by:

- Creating a **standardized artifact dictionary** for ASL MRI  
- Building **tooling to explore, search, and export artifact knowledge**  
- Laying the groundwork for **automation-ready QC pipelines**  

The repository is intentionally designed as a **core knowledge and interaction layer**, rather than a one-off implementation.

---

## Tasks Overview

The work is structured into **eight incremental tasks**, each building toward a scalable QC system:

1. Artifact Dictionary Design  
2. Artifact Browser & Search System  
3. Artifact Diagnosis Mode  
4. Artifact Comparison Tool  
5. Data Visualisation  
6. Machine-Readable Artifact Mapping  
7. QC Metric Integration  
8. Extensible QC Tooling & Reporting  

At present, **Task 1, 2 and 3 are fully implemented**, with later tasks planned.

---

## Task 1: ASL MRI Artifact Dictionary (Detailed)

### Description
Task 1 focuses on building a **structured and standardized artifact dictionary** for ASL MRI.

Each artifact is represented as a dedicated folder containing an `info.txt` file with consistent fields, including:

- Artifact name and category  
- Imaging modality  
- Visual appearance in ASL images  
- Primary causes  
- Clinical and QC impact  
- Severity level  
- Common mitigation strategies  

### Uniqueness of Task 1

Unlike informal documentation or ad-hoc notes, this artifact dictionary:

- Enforces **uniform structure across all artifacts**  
- Is **version-controlled and reproducible**  
- Separates **domain knowledge from code**, enabling reuse  
- Is designed to be **automation-ready**, not just descriptive  
- Acts as a **knowledge layer** that can plug into QC pipelines  

This makes the dictionary suitable for:  
- Automated QC systems  
- Benchmarking and validation workflows  
- Educational and documentation use  
- Future machine-readable transformations (JSON/YAML)  

---

## Task 2: Artifact Browser & Search System (Detailed)

### Description
Task 2 introduces an **interactive artifact browser and search engine** that operates directly on the artifact dictionary.

The system allows users to:

- Browse available artifacts dynamically  
- View structured artifact descriptions  
- Search artifacts using multiple logical modes  
- Export selected results in reproducible formats  

### Search Engine Capabilities
The search system supports:

- **AND logic search** – all keywords must match  
- **OR logic search** – any keyword may match  
- **Regex-based search** – expert-level pattern querying  

Search results are **scored and ranked by relevance**, not simply matched.

### Uniqueness of Task 2

This is not a basic file or keyword search.

Key distinguishing aspects include:

- Searches both **artifact names and full descriptions**  
- Supports **logical and regex-based querying**  
- Implements **relevance scoring and ranking**  
- Maintains a **uniform workflow** across all modes  
- Enables **structured export (JSON)** for downstream automation  
- Enables **human-readable export (PDF)** for reporting  

The system is designed as an **interaction layer**, bridging static artifact knowledge and future automated QC logic.

---

## Task 3: Artifact Diagnosis Mode (Detailed)

### Description

Task 3 introduces an interactive **Artifact Diagnosis Mode**. This feature enables users to **upload ASL MRI data** and receive **guided insights on potential artifacts** present in the scan.

Key functionalities include:

- **Upload & Analyze:** Users can upload individual ASL MRI scans in standard formats.  
- **Automated Detection Hints:** The system cross-references the scan with the artifact dictionary to **highlight possible artifact types**, severity, and typical causes.  
- **Visual Guidance:** Displays affected regions or slices alongside textual artifact descriptions for easier interpretation.  
- **Structured Feedback:** Provides a report that can be exported in **JSON** or **PDF** for QC tracking or research documentation.  

### Uniqueness of Artifact Diagnosis Mode

- **Integration with the standardized artifact dictionary**  
- **Automation-ready insights** compatible with downstream QC  
- **Interactive and reproducible** results for benchmarking  
- **Supports expert interpretation** without memorization  
- **Extensible for future ML integration**  

### Website / Frontend / Backend Status

- **Frontend Ready:** Fully developed interface for browsing, searching, and accessing Artifact Diagnosis Mode.  
- **Backend Ready:** Handles file uploads, dictionary querying, artifact scoring, and report generation.  
- **Fully Working End-to-End Pipeline:** Users can perform **upload → diagnosis → report export** without external dependencies.  

---

## Current Status

- ✅ 20 ASL MRI artifacts documented in a standardized format  
- ✅ Fully functional artifact browser  
- ✅ Multi-mode search engine (AND / OR / Regex)  
- ✅ Relevance-ranked results  
- ✅ JSON and PDF export support  
- ✅ Clean, uniform workflow across all modes
- ✅ Artifact Diagnosis Mode implemented
- ✅ Frontend and backend fully integrated and functional

---

## Focused Artifacts

- B₀ inhomogeneity effects  
- B₁ inhomogeneity effects  
- RF interferences  
- Chemical shift artifacts  
- Ghosting artifacts  
- Parallel imaging artifacts  
- Arterial artifacts  

---

## Planned Extensions (Tasks 4-8)

- Conversion of artifact knowledge into machine-readable schemas  
- Mapping artifacts to quantitative QC metrics  
- Integration with Quality Check Toolbox pipelines  
- Inclusion of example MRI data and detection heuristics  
- Automated QC reporting and dashboards  
- Web-based interface for broader accessibility  

---

## Closing Note

This repository is intentionally designed as a **foundation**, not a final product.

The emphasis is on:

- Clean structure  
- Reproducibility  
- Scalability  
- Research-grade design principles  

These components are meant to evolve into a comprehensive QC system for ASL MRI, aligned with open-source research workflows.

---

## Author

**Harshita Sharma**  
GSoC 2026 Aspirant  
Interests: Python development, reproducible systems, medical imaging quality control
