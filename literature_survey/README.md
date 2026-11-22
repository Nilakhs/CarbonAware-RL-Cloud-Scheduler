# Systematic Literature Survey (SLR)

This directory contains all assets, data extraction notes, screening logs, and synthesis documents for the **Systematic Literature Review (SLR)** on *Carbon-Aware Reinforcement Learning (RL) Schedulers for Dynamic Cloud Workloads*.

---

## 1. SLR Framework & Methodology Standards
The literature review follows the established computer science systematic review protocol:
- **Kitchenham & Charters (2007):** Systematic Literature Review protocol in software and systems engineering.
- **PRISMA 2020 (Page et al., 2021):** Systematic reporting of study identification, screening, eligibility, and inclusion.
- **Wohlin (2014):** Backward and forward snowballing discovery using Google Scholar and Semantic Scholar citations.

The complete review plan and protocol instructions are available in [`docs/research_methodology.md`](../docs/research_methodology.md).

---

## 2. Target Literature Distribution

The survey covers a target of **30 core papers** (published between January 2021 and November 2026), supplemented by foundational baselines and comprehensive surveys:

| Group | Category & Focus | Target | Screened / Included | Extraction Status |
|:---:|:---|:---:|:---:|:---:|
| **G1** | Carbon-Aware Scheduling **without** RL (Heuristics, Optimization, ILP) | **7** | 7 / 7 | **COMPLETE** (P01–P07 extracted) |
| **G2** | RL / DRL for Cloud Scheduling with **Energy, Cost, or QoS** Objectives | **7** | 7 / 7 | **IN PROGRESS** (P08–P09 extracted; P10 candidate replacement pending review) |
| **G3** | RL / DRL for **Carbon-Aware** Cloud Workload Scheduling (Core Focus) | **10** | 10 / 10 | **PLANNED** (P15–P24) |
| **G4** | Carbon-Intensity **Data and Forecasting** (Inputs for schedulers) | **3** | 3 / 3 | **PLANNED** (P25–P27) |
| **G5** | **Simulators, Datasets, and Workload Traces** for Cloud Scheduling | **3** | 3 / 3 | **PLANNED** (P28–P30) |
| **F** | **Foundational Literature** (Seminal pre-2021 RL/cloud papers, max 4) | **Up to 4** | 4 / 4 | **COMPLETE** (F01 DeepRM, F02 Decima, F03 Borg, F04 Wang et al.) |
| **S** | **Comprehensive Survey / Review Literature** | **2–4** | 3 / 3 | **COMPLETE** (S01, S02, S03) |
| | **Total Core Surveyed Papers** | **30** | **30 / 30** | **10 / 30 Extracted** |

---

## 3. Directory Contents and Key Files

- [`Literature_Survey_Report.md`](./Literature_Survey_Report.md): Living systematic survey synthesis report structured across all 11 standard sections.
- [`Audit_Report.md`](./Audit_Report.md): Comprehensive Phase 2.5 audit reconciling metadata, publisher DOIs, author attributions, and PRISMA statistics.
- [`papers_master.csv`](./papers_master.csv): Master database of all 36 surveyed papers with publication metadata, group tags, and 8-point Quality Assessment (QA) scores.
- [`search_log.csv`](./search_log.csv): Audit trail of every formal database query executed (IEEE Xplore, ACM DL, ScienceDirect, arXiv, Google Scholar) with exact search strings and hit counts.
- [`screening_log.csv`](./screening_log.csv): Complete two-stage PRISMA screening record documenting inclusion decisions and specific exclusion rationales.
- [`verification_log.csv`](./verification_log.csv): Rigorous verification checklist tracking official publisher URLs, full-text access, group relevance, and reviewer notes.
- [`references.bib`](./references.bib): BibTeX database with standardized citation keys corresponding to all paper IDs (`P01`–`P30`, `F01`–`F04`, `S01`–`S03`).
- [`notes/`](./notes/): Individual, standardized extraction notes for each paper following the approved methodology template.
- [`grouped_papers/`](./grouped_papers/): Group-level synthesis directories (`G1/` through `G5/`) housing comparative cross-paper tables.
- [`research_gaps/`](./research_gaps/): Working directory mapping identified research gaps to specific empirical findings.
- [`screening/`](./screening/): Supporting screening materials and stage-level review artifacts.

---

## 4. Extraction Progress Summary

### Completed Extraction Notes (`notes/`)
- [`P01_Lets_Wait_Awhile.md`](./notes/P01_Lets_Wait_Awhile.md): Wiesner et al., *Middleware '21* (G1: Temporal shifting heuristic; 11%–34% carbon reduction).
- [`P02_Carbon_Aware_Datacenters_Google.md`](./notes/P02_Carbon_Aware_Datacenters_Google.md): Radovanović et al., *IEEE TPWRS '23* (G1: Google fleet optimization via Virtual Capacity Curves).
- [`P03_Carbon_Explorer.md`](./notes/P03_Carbon_Explorer.md): Acun et al., *ASPLOS '23* (G1: Holistic framework for embodied vs. operational carbon trade-offs).
- [`P04_Ecovisor.md`](./notes/P04_Ecovisor.md): Souza et al., *ASPLOS '23* (G1: Virtual energy system exposing carbon signals to software runtimes).
- [`P05_CarbonScaler.md`](./notes/P05_CarbonScaler.md): Hanafy et al., *ACM POMACS / SIGMETRICS '23* (G1: Workload elasticity scaling for carbon efficiency).
- [`P06_GreenCourier.md`](./notes/P06_GreenCourier.md): Chadha et al., *WoSC@Middleware '23* (G1: Kubernetes/Knative serverless spatial routing; 13.25% carbon reduction).
- [`P07_Algorithm_Selection_FTL.md`](./notes/P07_Algorithm_Selection_FTL.md): Bostandoost et al., *ACM SIGEnergy EIR / HotCarbon '24* (G1: Follow the Leader meta-algorithm over heuristics).
- [`P08_BayesDDQN_Holistic_Energy.md`](./notes/P08_BayesDDQN_Holistic_Energy.md): Zhao et al., *IEEE TSC '25* (G2: BayesDDQN IT and CRAC cooling co-optimization).
- [`P09_GNN_PPO_Workflow_EdgeCloud.md`](./notes/P09_GNN_PPO_Workflow_EdgeCloud.md): Zhu et al., *IEEE TCC '24* (G2: GNN DAG task embedding + PPO for edge-cloud workflow scheduling).
- [`F04_Wang_DRL_Green_Task_Scheduling.md`](./notes/F04_Wang_DRL_Green_Task_Scheduling.md): Wang et al., *IEEE TCC '20* (Foundational: DRL green task scheduling under uncertainty).
