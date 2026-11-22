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
| **G1** | Carbon-Aware Scheduling **without** RL (Heuristics, Optimization, ILP) | **7** | 7 Confirmed Included | **COMPLETE** (P01–P07 extracted) |
| **G2** | RL / DRL for Cloud Scheduling with **Energy, Cost, or QoS** Objectives | **7** | 7 Confirmed Included | **COMPLETE** (P08–P14 extracted) |
| **G3** | RL / DRL for **Carbon-Aware** Cloud Workload Scheduling (Core Focus) | **10** | 10 Confirmed Included | **IN PROGRESS** (2/10 extracted: P15, P16; P17–P24 planned) |
| **G4** | Carbon-Intensity **Data and Forecasting** (Inputs for schedulers) | **3** | 3 Confirmed Included | **PLANNED** (P25–P27) |
| **G5** | **Simulators, Datasets, and Workload Traces** for Cloud Scheduling | **3** | 3 Confirmed Included | **PLANNED** (P28–P30) |
| **F** | **Foundational Literature** (Seminal pre-2021 RL/cloud papers, max 4) | **Up to 4** | 4 Confirmed Included | **COMPLETE** (F01 DeepRM, F02 Decima, F03 Borg, F04 Wang et al.) |
| **S** | **Comprehensive Survey / Review Literature** | **2–4** | 3 Confirmed Included | **COMPLETE** (S01, S02, S03) |
| | **Total Confirmed Inventory** | **30 Core Target** | **37 Confirmed Included Papers** | **16 Core + 1 Foundational (F04) Extracted** |

---

## 3. Directory Contents and Key Files

- [`Literature_Survey_Report.md`](./Literature_Survey_Report.md): Living systematic survey synthesis report structured across all 11 standard sections.
- [`Audit_Report.md`](./Audit_Report.md): Comprehensive Phase 2.5 audit reconciling metadata, publisher DOIs, author attributions, and PRISMA statistics.
- [`papers_master.csv`](./papers_master.csv): Master database of all 37 surveyed papers with publication metadata, group tags, and 8-point Quality Assessment (QA) scores.
- [`retrieval_log.csv`](./retrieval_log.csv): Formal enumeration of all 57 retrieved records (`RET-01` to `RET-57`) linking query hits, deduplication decisions, and screening outcomes.
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
- [`P10_DRAW_Resource_Allocation.md`](./notes/P10_DRAW_Resource_Allocation.md): Chen et al., *IEEE TCC '23* (G2: DRAW DQN resource allocation with workload-time windows).
- [`P11_Actor_Critic_Cloud_Resource_Allocation.md`](./notes/P11_Actor_Critic_Cloud_Resource_Allocation.md): Chen et al., *IEEE TPDS '22* (G2: Actor-Critic with Advantage baseline for continuous datacenter allocation).
- [`P12_Adaptive_DRL_VM_Consolidation.md`](./notes/P12_Adaptive_DRL_VM_Consolidation.md): Zeng et al., *IEEE TPDS '22* (G2: ADVMC dynamic VM consolidation with LSTM state prediction).
- [`P13_PADQN_Data_Center_Energy_Efficiency.md`](./notes/P13_PADQN_Data_Center_Energy_Efficiency.md): Ran et al., *IEEE TSC '23* (G2: DeepEE PADQN parameterized action space for IT and cooling).
- [`P14_Federated_DRL_Cloud_Edge_Scheduling.md`](./notes/P14_Federated_DRL_Cloud_Edge_Scheduling.md): Zhu et al., *IEEE TCC '23* (G2: Federated DRL for distributed privacy-preserving cloud-edge scheduling).
- [`P15_Sustainable_AIGC_Scheduling_MARL.md`](./notes/P15_Sustainable_AIGC_Scheduling_MARL.md): Zhang et al., *IEEE GLOBECOM '23* (G3: Multi-Agent Soft Actor-Critic for geo-distributed AIGC scheduling; +28.6% utility, +15.6% GPU throughput).
- [`P16_MADRL_Renewable_Workflow_Scheduling.md`](./notes/P16_MADRL_Renewable_Workflow_Scheduling.md): Jayanetti et al., *IEEE TPDS '24* (G3: Multi-agent DRL for renewable energy-aware workflow DAG scheduling on distributed cloud DCs; up to 47% energy reduction).
- [`F04_Wang_DRL_Green_Task_Scheduling.md`](./notes/F04_Wang_DRL_Green_Task_Scheduling.md): Wang et al., *IEEE TCC '20* (Foundational: DRL green task scheduling under uncertainty).
