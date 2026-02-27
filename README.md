# ASL MRI Artifact Dictionary & Quality Control Foundations

## Overview
This repository is part of my preparation for **GSoC 2026 (Project #7 – Quality Check Toolbox / ASL-DCE related work)**.  
The project focuses on building a **structured and standardized artifact dictionary for ASL MRI**, intended to serve as a foundational component for automated Quality Control (QC) pipelines.

The repository documents common ASL MRI artifacts in a consistent, reproducible, and extensible format, enabling future integration with QC metrics, automated detection systems, and benchmarking frameworks.

---

## Motivation
Arterial Spin Labeling (ASL) MRI is highly sensitive to acquisition and physiological artifacts such as motion, labeling failure, low signal-to-noise ratio, and background suppression issues.  
Currently, artifact-related knowledge is scattered across research papers and informal documentation, making automation and standardization difficult.

This project aims to:
- Centralize ASL MRI artifact knowledge
- Standardize artifact definitions and descriptions
- Enable reproducible and scalable QC workflows
- Support future automation and validation efforts

---

## Repository Structure
```
Artifacts/
│
├── Motion_Artifact/
│ └── info.txt
├── Labeling_Failure/
│ └── info.txt
├── Low_Signal_to-Noise_Ratio_(Low_SNR)/
│ └── info.txt
├── Background_Suppression_Failure/
│ └── info.txt
├── Aliasing_Artifact/
│ └── info.txt
├── Susceptibility_Artifact/
│ └── info.txt
├── Partial_Volume_Effect/
│ └── info.txt
├── Vascular_Artifact/
│ └── info.txt
├── Calibration_Error/
│ └── info.txt
├── Coil_Sensitivity_Variation/
│ └── info.txt
```
Each artifact folder contains an `info.txt` file describing:
- Artifact name and category
- Imaging modality
- Visual appearance in ASL images
- Primary causes
- Clinical impact
- Severity level
- Common mitigation or correction strategies

---

## Current Status
- ✅ 10 ASL MRI artifacts documented
- ✅ Consistent and structured artifact format
- ✅ Version-controlled and publicly available
- ✅ Ready for extension into automated QC pipelines

---

## Planned Extensions
- Conversion of artifact descriptions into machine-readable formats (JSON/YAML)
- Mapping artifacts to measurable QC metrics (motion parameters, spatial CoV, M0 checks)
- Integration with Quality Check Toolbox pipelines
- Addition of visual examples and detection heuristics
- Support for automated QC reporting and dashboards

---

## Scope & Relevance
This artifact dictionary is designed to act as a **core knowledge layer** for Quality Control systems in ASL MRI.  
It can be reused across:
- Research benchmarking
- Automated QC toolchains
- Clinical validation pipelines
- Educational and documentation purposes

---

## Author
**Harshita Sharma**  
GSoC 2026 Aspirant  
Interests: Python development, reproducible systems, medical imaging quality control
