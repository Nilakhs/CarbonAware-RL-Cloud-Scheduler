# Systematic Literature Survey (SLR)

This directory contains all assets, data extraction notes, screening logs, and synthesis documents for the **Systematic Literature Review (SLR)** on *Carbon-Aware Reinforcement Learning (RL) Schedulers for Dynamic Cloud Workloads*.

---

## 1. SLR Framework & Methodology Standards
The literature review follows established computer science systematic review protocols:
- **Kitchenham & Charters (2007):** Systematic Literature Review protocol in software and systems engineering.
- **PRISMA 2020 (Page et al., 2021):** Systematic reporting of study identification, screening, eligibility, and inclusion.
- **Wohlin (2014):** Backward and forward snowballing discovery using Google Scholar and Semantic Scholar citations.
- **PDF-to-Markdown Extraction Workflow:** Standardized high-fidelity conversion pipeline utilizing PyMuPDF (`pymupdf4llm`) and structured rubric prompts to eliminate PDF extraction noise and preserve mathematical formulations, tables, and figures.

The complete review plan and protocol instructions are available in [`docs/research_methodology.md`](../docs/research_methodology.md). Supporting workflow documentation is available in [`PDF_TO_MARKDOWN_WORKFLOW.md`](./PDF_TO_MARKDOWN_WORKFLOW.md) and [`PAPER_ANALYSIS_PROMPT.md`](./PAPER_ANALYSIS_PROMPT.md).

---

## 2. Systematic Literature Inventory Status (30/30 Core Complete)

The survey covers the full target of **30 core papers** (published between January 2021 and November 2026), supplemented by 4 foundational baselines and 3 comprehensive surveys:

| Group | Category & Focus | Target | Screened / Included | Extraction Status |
|:---:|:---|:---:|:---:|:---:|
| **G1** | Carbon-Aware Scheduling **without** RL (Heuristics, Optimization, ILP) | **7** | 7 Confirmed Included | **COMPLETE** (7/7: P01–P07) |
| **G2** | RL / DRL for Cloud Scheduling with **Energy, Cost, or QoS** Objectives | **7** | 7 Confirmed Included | **COMPLETE** (7/7: P08–P14) |
| **G3** | RL / DRL for **Carbon-Aware** Cloud Workload Scheduling (Core Focus) | **10** | 10 Confirmed Included | **COMPLETE** (10/10: P15–P24) |
| **G4** | Carbon-Intensity **Data and Forecasting** (Inputs for schedulers) | **3** | 3 Confirmed Included | **COMPLETE** (3/3: P25–P27) |
| **G5** | **Simulators, Datasets, and Workload Traces** for Cloud Scheduling | **3** | 3 Confirmed Included | **COMPLETE** (3/3: P28–P30) |
| **F** | **Foundational Literature** (Seminal pre-2021 RL/cloud papers, max 4) | **Up to 4** | 4 Confirmed Included | **COMPLETE** (F01 DeepRM, F02 Decima, F03 Borg, F04 Wang et al.) |
| **S** | **Comprehensive Survey / Review Literature** | **2–4** | 3 Confirmed Included | **COMPLETE** (S01, S02, S03) |
| | **Total Confirmed Inventory** | **30 Core Target** | **37 Confirmed Included Papers** | **30 Core + 1 Foundational (F04) Extracted** |

---

## 3. Directory Contents and Key Files

- [`Literature_Survey_Report.md`](./Literature_Survey_Report.md): Primary systematic survey synthesis report structured across all 11 standard PRISMA sections with comparative cross-group analysis.
- [`Audit_Report.md`](./Audit_Report.md): Comprehensive Phase 2.5 audit reconciling metadata, publisher DOIs, author attributions, and PRISMA statistics.
- [`papers_master.csv`](./papers_master.csv): Master database of all 37 surveyed papers with publication metadata, group tags, and verified 8-point Quality Assessment (QA) scores.
- [`PDF_TO_MARKDOWN_WORKFLOW.md`](./PDF_TO_MARKDOWN_WORKFLOW.md): Supporting methodology documentation describing the automated conversion pipeline, token efficiency, and OCR handling.
- [`PAPER_ANALYSIS_PROMPT.md`](./PAPER_ANALYSIS_PROMPT.md): Standardized 6-section extraction prompt guiding primary-source analysis.
- [`markdown_papers/`](./markdown_papers/): Clean Markdown conversions (`P15.md`, `P21.md`–`P30.md`) used for primary-source audit and LLM synthesis.
- [`papers/`](./papers/): Repository of verified full-text publisher and open-access research PDFs.
- [`notes/`](./notes/): Individual, standardized 6-section extraction notes for each paper (`P01` through `P30`, `F04`).
- [`references.bib`](./references.bib): BibTeX database with standardized citation keys corresponding to all paper IDs (`P01`–`P30`, `F01`–`F04`, `S01`–`S03`).
- [`retrieval_log.csv`](./retrieval_log.csv): Formal enumeration of all retrieved records (`RET-01` to `RET-57`) linking query hits, deduplication decisions, and screening outcomes.
- [`search_log.csv`](./search_log.csv): Audit trail of formal database queries executed across IEEE Xplore, ACM DL, ScienceDirect, arXiv, and Google Scholar.
- [`screening_log.csv`](./screening_log.csv): Complete two-stage PRISMA screening record documenting inclusion decisions and specific exclusion rationales.
- [`verification_log.csv`](./verification_log.csv): Rigorous verification checklist tracking official publisher URLs, full-text access, group relevance, and reviewer notes.

---

## 4. Master Inventory of Surveyed Papers (P01–P30)

| ID | Title / Citation | Venue / Year | Group | Method / Key Concept | Strict Score | Primary Literature Note |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **P01** | *Let's Wait Awhile: How Temporal Workload Shifting Can Reduce Carbon Emissions* | ACM Middleware '21 | G1 | Temporal shifting / Carbon delay heuristic | **8.0** | [`P01_Lets_Wait_Awhile.md`](./notes/P01_Lets_Wait_Awhile.md) |
| **P02** | *Carbon-Aware Computing for Datacenters* | IEEE TPWRS '23 | G1 | Virtual Capacity Curves (VCC) / Google fleet | **7.5** | [`P02_Carbon_Aware_Datacenters_Google.md`](./notes/P02_Carbon_Aware_Datacenters_Google.md) |
| **P03** | *Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters* | ACM ASPLOS '23 | G1 | Holistic carbon / Embodied & operational trade-off | **7.5** | [`P03_Carbon_Explorer.md`](./notes/P03_Carbon_Explorer.md) |
| **P04** | *Ecovisor: A Virtual Energy System for Carbon-Efficient Applications* | ACM ASPLOS '23 | G1 | Energy virtualization / Software-defined grid | **8.0** | [`P04_Ecovisor.md`](./notes/P04_Ecovisor.md) |
| **P05** | *CarbonScaler: Leveraging Cloud Workload Elasticity for Carbon-Efficiency* | ACM SIGMETRICS '23 | G1 | Workload elasticity / Predictive autoscaling | **8.0** | [`P05_CarbonScaler.md`](./notes/P05_CarbonScaler.md) |
| **P06** | *GreenCourier: Carbon-Aware Scheduling for Serverless Functions* | WoSC@Middleware '23 | G1 | Spatial shifting / Serverless FaaS Knative | **7.5** | [`P06_GreenCourier.md`](./notes/P06_GreenCourier.md) |
| **P07** | *Data-driven Algorithm Selection for Carbon-Aware Scheduling* | HotCarbon '24 | G1 | Meta-algorithm selection / Follow-The-Leader | **7.0** | [`P07_Algorithm_Selection_FTL.md`](./notes/P07_Algorithm_Selection_FTL.md) |
| **P08** | *Holistic Energy Optimization of Sustainable Cloud Data Centers* | IEEE TSC '25 | G2 | BayesDDQN / IT & cooling co-optimization | **8.0** | [`P08_BayesDDQN_Holistic_Energy.md`](./notes/P08_BayesDDQN_Holistic_Energy.md) |
| **P09** | *Workflow Scheduling for an Edge-Cloud Computing Environment* | IEEE TCC '24 | G2 | GNN + PPO / Graph workflow scheduling | **7.5** | [`P09_GNN_PPO_Workflow_EdgeCloud.md`](./notes/P09_GNN_PPO_Workflow_EdgeCloud.md) |
| **P10** | *Resource Allocation With Workload-Time Windows for Cloud Services* | IEEE TCC '23 | G2 | DRAW DQN / Workload-time windows & cost | **7.5** | [`P10_DRAW_Resource_Allocation.md`](./notes/P10_DRAW_Resource_Allocation.md) |
| **P11** | *Adaptive and Efficient Resource Allocation in Cloud Datacenters* | IEEE TPDS '22 | G2 | Actor-Critic with Advantage / Continuous allocation | **7.5** | [`P11_Actor_Critic_Cloud_Resource_Allocation.md`](./notes/P11_Actor_Critic_Cloud_Resource_Allocation.md) |
| **P12** | *Adaptive DRL-Based Virtual Machine Consolidation in Cloud Data Centers* | IEEE TPDS '22 | G2 | ADVMC DRL / VM consolidation & host shutdown | **7.0** | [`P12_Adaptive_DRL_VM_Consolidation.md`](./notes/P12_Adaptive_DRL_VM_Consolidation.md) |
| **P13** | *Optimizing Energy Efficiency for Data Center via Parameterized DRL* | IEEE TSC '23 | G2 | DeepEE PADQN / Hybrid discrete-continuous control | **7.5** | [`P13_PADQN_Data_Center_Energy_Efficiency.md`](./notes/P13_PADQN_Data_Center_Energy_Efficiency.md) |
| **P14** | *A Federated Deep Reinforcement Learning Model for Cloud-Edge Scheduling* | IEEE TCC '23 | G2 | Federated DRL / Privacy-preserving scheduling | **7.0** | [`P14_Federated_DRL_Cloud_Edge_Scheduling.md`](./notes/P14_Federated_DRL_Cloud_Edge_Scheduling.md) |
| **P15** | *Sustainable AIGC Workload Scheduling of Geo-Distributed Data Centers* | IEEE GLOBECOM '23 | G3 | Soft Actor-Critic (SAC) / Spatial shifting / WattTime | **8.0** | [`P15_Sustainable_AIGC_Scheduling_MARL.md`](./notes/P15_Sustainable_AIGC_Scheduling_MARL.md) |
| **P16** | *Renewable Energy-Aware Workflow Scheduling on Distributed Data Centers* | IEEE TPDS '24 | G3 | MADRL / Workflow DAG / Solar & Wind traces | **6.5** | [`P16_MADRL_Renewable_Workflow_Scheduling.md`](./notes/P16_MADRL_Renewable_Workflow_Scheduling.md) |
| **P17** | *Task Scheduling for Environmentally Sustainable Federated Cloud Computing* | J. Cloud Comput. '23 | G3 | ERLFC Actor-Critic / Regional emission factors | **6.5** | [`P17_ERLFC_Federated_Cloud_Scheduling.md`](./notes/P17_ERLFC_Federated_Cloud_Scheduling.md) |
| **P18** | *Online Job Scheduling: An Information and Energy Nexus Perspective* | Applied Energy '23 | G3 | DRL online scheduling / Energy-carbon nexus | **7.0** | [`P18_DRL_Information_Energy_Nexus_Scheduling.md`](./notes/P18_DRL_Information_Energy_Nexus_Scheduling.md) |
| **P19** | *CFWS: DRL-Based Framework for Energy Cost and Carbon Optimization* | IEEE TSUSC '25 | G3 | DRL / Day-ahead carbon & electricity cost | **6.5** | [`P19_CFWS_DRL_Energy_Carbon_Scheduling.md`](./notes/P19_CFWS_DRL_Energy_Carbon_Scheduling.md) |
| **P20** | *Digital Twin-Driven Dual-Time-Scale Orchestration for Synergistic Systems* | IEEE TGCN '26 | G3 | MAPPO / Digital Twin / Dual-Time-Scale | **5.0** | [`P20_Digital_Twin_Dual_Time_Scale_Orchestration.md`](./notes/P20_Digital_Twin_Dual_Time_Scale_Orchestration.md) |
| **P21** | *Multi-Objective DRL for Carbon-Aware Spatiotemporal Workload Scheduling* | JACS '25 | G3 | MO-PPO / Tchebycheff scalarization / EIA-930 ISOs | **7.5** | [`P21_MultiObjective_DRL_Spatiotemporal_Scheduling.md`](./notes/P21_MultiObjective_DRL_Spatiotemporal_Scheduling.md) |
| **P22** | *GAS-MARL: Green-Aware Job Scheduling Algorithm for HPC Clusters* | FGCS '25 | G3 | Multi-Action DRL / Job selection + Green delay | **7.5** | [`P22_GAS_MARL_HPC_Scheduling.md`](./notes/P22_GAS_MARL_HPC_Scheduling.md) |
| **P23** | *Carbon-Aware Decision-Making in Intraday Electricity Markets Using DRL* | IEEE TIA '26 | G3 | PPO / Bi-level market clearing & task migration | **7.0** | [`P23_Huang_Intraday_Market_PPO.md`](./notes/P23_Huang_Intraday_Market_PPO.md) |
| **P24** | *Hierarchical MARL for Carbon-Aware AI Data Centers in Power Systems* | arXiv '26 | G3 | Hierarchical MAT / Global MAT + Local AIDC agents | **7.0** | [`P24_Lee_Hierarchical_MARL_Power_Distribution.md`](./notes/P24_Lee_Hierarchical_MARL_Power_Distribution.md) |
| **P25** | *CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity* | ACM BuildSys '22 | G4 | Hierarchical CNN-LSTM / 96-hr multi-day forecast | **8.0** | [`P25_CarbonCast_MultiDay_Forecast.md`](./notes/P25_CarbonCast_MultiDay_Forecast.md) |
| **P26** | *DACF: Day-Ahead Carbon Intensity Forecasting of Power Grids* | ACM e-Energy '22 | G4 | Per-source ANN regression / 24-hr day-ahead | **7.5** | [`P26_Maji_DACF_DayAhead_Forecast.md`](./notes/P26_Maji_DACF_DayAhead_Forecast.md) |
| **P27** | *Uncertainty-Aware Decarbonization for Datacenters* | HotCarbon '24 | G4 | Conformal inference (SPCI) / Carbon risk bounds | **7.5** | [`P27_Li_Uncertainty_Aware_Decarbonization.md`](./notes/P27_Li_Uncertainty_Aware_Decarbonization.md) |
| **P28** | *SustainGym: Reinforcement Learning Environments for Sustainable Energy* | NeurIPS '23 | G5 | Gymnasium benchmark suite / DatacenterEnv / WattTime | **8.0** | [`P28_SustainGym_Benchmark_Suite.md`](./notes/P28_SustainGym_Benchmark_Suite.md) |
| **P29** | *Vessim: A Testbed for Carbon-Aware Applications and Systems* | HotCarbon '24 | G5 | Mosaik co-simulation / Hardware-in-the-loop | **7.5** | [`P29_Wiesner_Vessim_Testbed.md`](./notes/P29_Wiesner_Vessim_Testbed.md) |
| **P30** | *Characterizing Microservice Dependency & Performance: Alibaba Trace* | ACM SoCC '21 | G5 | Alibaba 2021 microservice trace / CPU sensitivity | **7.0** | [`P30_Alibaba_Microservice_Trace_Analysis.md`](./notes/P30_Alibaba_Microservice_Trace_Analysis.md) |
| **F04** | *A DRL Approach for Green Task Scheduling in Cloud Computing* | IEEE TCC '20 | Foundational | DRL green task scheduling under uncertainty | **7.5** | [`F04_Wang_DRL_Green_Task_Scheduling.md`](./notes/F04_Wang_DRL_Green_Task_Scheduling.md) |

---

## 5. Rubric Scoring Framework (Q1–Q8)
Every paper is evaluated strictly against an 8-point quality assessment framework:
- **Q1 (Problem Formulation):** Is the cloud scheduling problem clearly and mathematically formulated?
- **Q2 (Methodological Rigor):** Is the optimization / RL method fully specified (state space, action space, reward function, algorithm)?
- **Q3 (Carbon Modeling & Grounding):** Does the study use authentic dynamic grid carbon intensity time series ($g\text{CO}_2/\text{kWh}$ or MOER) from real balancing authorities (ISOs/RTOs)? *(Meteorological renewable traces without grid carbon APIs receive 0.5; zero carbon data receives 0.0)*.
- **Q4 (Workload Realism):** Does the study use authentic production cluster workload traces (e.g., Google Borg, Alibaba, Azure) or a real hardware testbed?
- **Q5 (Baseline Comparison):** Is the method benchmarked against rigorous, non-trivial baselines (heuristics, LP solvers, or alternative DRL algorithms)?
- **Q6 (Quantitative Results):** Are empirical results reported with concrete numerical metrics (carbon reduction %, SLA violation %, latency overhead)?
- **Q7 (Open Science & Reproducibility):** Are code, models, or datasets open-sourced or sufficiently detailed for independent replication?
- **Q8 (Limitations & Critical Assessment):** Do the authors explicitly analyze operational trade-offs, scalability boundaries, or real-world constraints?
