# Carbon-Aware Reinforcement Learning (RL) Scheduler for Dynamic Cloud Workloads

[![Survey Standard](https://img.shields.io/badge/Methodology-Kitchenham%20%2F%20PRISMA%202020-blue.svg)](#8-systematic-literature-survey-methodology)
[![Progress](https://img.shields.io/badge/SLR%20Progress-15%2F30%20Core%20Papers-orange.svg)](#10-current-research-progress)
[![Group Status](https://img.shields.io/badge/Status-G1%20%26%20G2%20Complete%20%7C%20G3%20In%20Progress-brightgreen.svg)](#9-five-literature-groups)
[![Status](https://img.shields.io/badge/Project%20Stage-Literature%20Review%20%26%20Scoping-yellow.svg)](#10-current-research-progress)

A systematic research project and experimental investigation into **Carbon-Aware Reinforcement Learning (RL) Schedulers for Dynamic Cloud Workloads**, conducted as part of a college Cloud Computing course project.

---

## Table of Contents
- [1. Project Motivation and Background](#1-project-motivation-and-background)
- [2. Problem Statement](#2-problem-statement)
- [3. Why Carbon-Aware Cloud Scheduling Matters](#3-why-carbon-aware-cloud-scheduling-matters)
- [4. Project Objectives](#4-project-objectives)
- [5. Research Questions](#5-research-questions)
- [6. Proposed Research Direction](#6-proposed-research-direction)
- [7. Proposed Technology Stack](#7-proposed-technology-stack)
- [8. Systematic Literature Survey Methodology](#8-systematic-literature-survey-methodology)
- [9. Five Literature Groups](#9-five-literature-groups)
- [10. Current Research Progress](#10-current-research-progress)
- [11. Repository Directory Structure](#11-repository-directory-structure)
- [12. Expected Outcomes](#12-expected-outcomes)
- [13. Contributors & Course Information](#13-contributors--course-information)
- [14. References & Documentation Links](#14-references--documentation-links)
- [15. License](#15-license)

---

## 1. Project Motivation and Background
Hyperscale data centers supporting modern cloud infrastructure, large-scale data analytics, and generative AI workloads consume over 1% of global electricity. Crucially, the environmental impact of this power consumption is not uniform: the **grid carbon intensity**—measured in grams of $\text{CO}_2$ emitted per kilowatt-hour ($g\text{CO}_2/\text{kWh}$)—fluctuates substantially across hours of the day (due to diurnal solar cycles and intermittent wind availability) and across geographical regions (due to localized electricity generation mixes).

Conventional cloud schedulers (such as Kubernetes, Borg, Slurm, or OpenStack) operate in a **carbon-agnostic** manner. They optimize strictly for operational costs, server utilization, and makespan. Consequently, flexible batch jobs are often executed during carbon-intensive periods (when fossil peaker plants fire) or in high-carbon regions, missing significant decarbonization opportunities.

---

## 2. Problem Statement
The central research challenge is to formulate, design, and evaluate an online **Carbon-Aware Reinforcement Learning (RL) Scheduler** capable of dynamically coordinating:
- **When to execute** (*temporal workload shifting* within a permitted flexibility window $\Delta t^{\max}$),
- **Where to execute** (*spatial workload shifting* across geographically distributed clusters), and
- **Resource provisioning levels** (*elastic scaling* matching green energy availability),

subject to dynamic, stochastic task arrivals, time-varying grid carbon intensity forecasts, and strict Service Level Agreement (SLA) deadlines.

*Detailed formal formulation:* [`docs/problem_statement.md`](docs/problem_statement.md).

---

## 3. Why Carbon-Aware Cloud Scheduling Matters
1. **Double-Digit Carbon Reductions Without Hardware Changes:** Peer-reviewed literature demonstrates that temporal and spatial shifting alone can achieve 10% to 34% relative reductions in operational emissions without requiring hardware replacements.
2. **Complementing Green Power Purchase Agreements (PPAs):** Annualized renewable certificates (PPAs) do not match hourly grid consumption; true 24/7 carbon-free computing requires runtime operational synchronization with real-time grid signals.
3. **Overcoming Heuristic Brittleness:** Static heuristics (e.g., fixed nighttime execution or static thresholding) degrade under non-stationary weather conditions and localized forecast errors ($10\%–30\%$). Reinforcement learning provides an adaptive mechanism capable of generalizing across volatile conditions.

---

## 4. Project Objectives
- **Primary:** Synthesize and evaluate an online RL scheduler that minimizes operational carbon emissions while guaranteeing zero or bounded SLA deadline violations.
- **Secondary:**
  1. Complete a rigorous 30-paper Systematic Literature Review adhering to PRISMA 2020 and Kitchenham guidelines.
  2. Map state-of-the-art scheduler architectures across five literature groups (G1 through G5).
  3. Formalize dynamic cloud workload scheduling as a discrete-time Markov Decision Process (MDP).
  4. Design multi-objective reward shaping mechanisms balancing carbon reduction against latency and migration penalties.
  5. Validate policies empirically using trace-driven simulation testbeds (e.g., Vessim, CloudSim Plus) with real-world Google/Alibaba traces and CAISO/ENTSO-E carbon data.

*Detailed objectives breakdown:* [`docs/objectives.md`](docs/objectives.md).

---

## 5. Research Questions
Directly derived from our Systematic Literature Review protocol ([`docs/research_methodology.md`](docs/research_methodology.md)):
- **RQ1 (State of the Art & Trends):** How have scheduling methodologies evolved across non-RL heuristics, energy-centric RL, and carbon-aware RL between 2021 and 2026?
- **RQ2 (Comparative Efficacy & Trade-Offs):** What carbon emission reductions are achievable via temporal shifting versus spatial shifting, and what are the trade-offs in makespan, latency, and SLA infractions?
- **RQ3 (Handling Environmental Uncertainty):** How effectively do existing carbon-aware RL schedulers handle dynamic job arrivals coupled with volatile, erroneous carbon forecasts?
- **RQ4 (Multi-Objective SLA Preservation):** How can RL reward functions be shaped to prevent policy collapse during extreme renewable lulls without causing SLA deadline breaches?
- **RQ5 (Feasible Research Scope):** Which substantiated research gap represents a viable, novel contribution that can be implemented and evaluated within a single-semester course timeline?

---

## 6. Proposed Research Direction
Based on completed literature extraction, the proposed scheduler functions as an online dispatching layer:
- **Environment:** Trace-driven discrete-event simulation environment implementing cluster queues, server power models, and real-time regional carbon feeds.
- **Agent Policy:** Deep Reinforcement Learning policy (evaluating PPO and Double DQN) that observes task resource demands, queue states, and carbon forecast vectors to make discrete dispatch and delay decisions.
- **Reward Formulation:** Multi-objective composite reward penalizing operational carbon emissions, task deadline violations, and inter-region migration latencies.

*Detailed architectural specification:* [`project_research/proposed_approach.md`](project_research/proposed_approach.md).

---

## 7. Proposed Technology Stack

> [!NOTE]
> All software modules are clearly classified by their current development status:

| Component / Layer | Technology | Status | Justification / Role |
|:---|:---|:---:|:---|
| **SLR & Verification** | Python 3.10+, Pandas, BibTeX, GitHub Markdown | **IMPLEMENTED** | Systematic literature logging, PRISMA tracking, and verification audits |
| **RL Formulation & Agent** | PyTorch, Stable-Baselines3, Gymnasium | **PLANNED** | Reinforcement learning policy networks (PPO / Double DQN) |
| **Simulation Testbed** | Vessim / CloudSim Plus / SimGrid | **PLANNED** | Discrete-event cloud datacenter and carbon co-simulation |
| **Workload Traces** | Google Borg Traces (2019/2020), Alibaba (2021) | **SCOPED** | Realistic multi-task arrival patterns and resource profiles |
| **Carbon Intensity Telemetry** | Electricity Maps API, WattTime API, CAISO OASIS | **SCOPED** | Real marginal and average carbon intensity traces |

---

## 8. Systematic Literature Survey Methodology
This project strictly follows established guidelines for systematic literature reviews in software engineering and distributed systems:
- **Kitchenham & Charters (2007):** Systematic review protocol, inclusion/exclusion criteria, data extraction fields, and 8-point Quality Assessment (QA) scoring.
- **PRISMA 2020 Statement (Page et al., 2021):** Traceable four-phase flow diagram (Identification $\to$ Retrieval $\to$ Screening $\to$ Inclusion).
- **Wohlin (2014) Snowballing:** Backward reference checking and forward Google Scholar citation tracking.

*Full review protocol:* [`docs/research_methodology.md`](docs/research_methodology.md)  
*Phase 2.5 Audit & Reconciliation Report:* [`literature_survey/Audit_Report.md`](literature_survey/Audit_Report.md)

---

## 9. Five Literature Groups

| Group | Focus Area | Core Target | Status | Highlights / Key Citations |
|:---:|:---|:---:|:---:|:---|
| **G1** | Carbon-Aware Scheduling **without** RL | 7 | **COMPLETE (7/7 Confirmed)** | *Let's Wait Awhile* (P01), Google Fleet (P02), *Carbon Explorer* (P03), *Ecovisor* (P04), *CarbonScaler* (P05), *GreenCourier* (P06), *FTL Meta-Algorithm* (P07) |
| **G2** | RL / DRL for Cloud Energy, Cost, and QoS | 7 | **COMPLETE (7/7)** | *BayesDDQN* (P08), *GNN-PPO Workflow* (P09), *DRAW* (P10), *Actor-Critic* (P11), *ADVMC* (P12), *DeepEE PADQN* (P13), *Federated DRL* (P14) |
| **G3** | RL / DRL for **Carbon-Aware** Scheduling (Core) | 10 | **IN PROGRESS (1/10 Extracted)** | Core focus: P15–P24 covering multi-agent, actor-critic, and hierarchical carbon schedulers (P15 extracted) |
| **G4** | Carbon-Intensity Data and Forecasting | 3 | **PLANNED (3 Confirmed)** | P25 (*CarbonCast*), P26 (*DACF*), P27 (*HotCarbon '24* conformal prediction) |
| **G5** | Simulators, Datasets, and Workload Traces | 3 | **PLANNED (3 Confirmed)** | P28 (*SustainGym*), P29 (*Vessim*), P30 (*Alibaba 2021 trace*) |
| **F** | Foundational Baseline Literature (Pre-2021) | Max 4 | **COMPLETE (4/4 Confirmed)** | *DeepRM* (F01), *Decima* (F02), *Borg Trace* (F03), *Wang et al. DRL-Green* (F04) |
| **S** | Comprehensive Survey & Review Literature | 2–4 | **COMPLETE (3/3 Confirmed)** | Container Orchestration (S01), *HUNTER* (S02), Spatio-Temporal Review (S03) |

---

## 10. Current Research Progress

```text
Systematic Literature Review Progress:
[████████████████████░░░░░░░░░░░░] 50% Core Target (15/30 Core + 1 Foundational Extracted)

G1: Non-RL Carbon Schedulers   [████████████████████] 100% (7/7 extracted: P01–P07)
G2: RL for Energy/Cost/QoS     [████████████████████] 100% (7/7 extracted: P08–P14)
G3: RL for Carbon Schedulers   [██░░░░░░░░░░░░░░░░░░]  10% (1/10 extracted: P15; Target: P15–P24)
G4: Data and Forecasting       [░░░░░░░░░░░░░░░░░░░░]   0% (Target: 3 papers: P25–P27)
G5: Simulators and Traces      [░░░░░░░░░░░░░░░░░░░░]   0% (Target: 3 papers: P28–P30)
```

- **Completed Deliverables:**
  - Full SLR protocol, search log, retrieval log (`retrieval_log.csv`), and screening logs mathematically reconciled.
  - Standardized paper extraction notes for `P01` through `P15` and foundational paper `F04`.
  - Comprehensive metadata audit verifying DOIs, proceedings pagination, and author rosters.
  - Pre-implementation research scoping documents (`problem_statement.md`, `existing_approaches.md`, `candidate_research_gaps.md`).
- **Next Milestone:** Controlled extraction of Group G3 (`P16`–`P24`, Core Carbon-Aware RL Schedulers).

---

## 11. Repository Directory Structure

```text
CarbonAware-RL-Cloud-Scheduler/
│
├── README.md                          # Repository overview and academic project portal
├── CONTRIBUTING.md                    # Review protocol, extraction guide & QA rubric
├── .gitignore                         # Git ignore rules (protects against PDFs, venvs, binaries)
│
├── docs/                              # Project scoping and SLR methodology documentation
│   ├── project_overview.md            # High-level context, goals, and decarbonization motivation
│   ├── problem_statement.md           # Formal mathematical problem statement and constraints
│   ├── objectives.md                  # Primary/secondary objectives and research questions
│   └── research_methodology.md        # Full systematic literature review protocol (Kitchenham/PRISMA)
│
├── literature_survey/                 # Systematic Literature Review assets and databases
│   ├── README.md                      # Guide to survey progress, group distribution & workflow
│   ├── Literature_Survey_Report.md    # Living synthesis report across all 11 standard sections
│   ├── Audit_Report.md                # Phase 2.5 audit and reconciliation findings
│   ├── papers_master.csv              # Master database (37 confirmed included papers with QA scores)
│   ├── retrieval_log.csv              # Enumeration of all 57 retrieved records (RET-01 to RET-57)
│   ├── search_log.csv                 # Detailed audit trail of all database queries & hits
│   ├── screening_log.csv              # Two-stage PRISMA screening decisions and exclusion reasons
│   ├── verification_log.csv           # DOI, full-text, and bibliographic verification checklist
│   ├── references.bib                 # Verified BibTeX citations with standardized keys
│   │
│   ├── notes/                         # Standardized paper extraction notes
│   │   ├── P01_Lets_Wait_Awhile.md
│   │   ├── ...
│   │   ├── P14_Federated_DRL_Cloud_Edge_Scheduling.md
│   │   ├── P15_Sustainable_AIGC_Scheduling_MARL.md
│   │   └── F04_Wang_DRL_Green_Task_Scheduling.md
│   │
│   ├── grouped_papers/                # Cross-paper comparative tables per group (G1–G5)
│   ├── research_gaps/                 # Working directory mapping identified research gaps
│   └── screening/                     # Supporting screening documentation
│
├── project_research/                  # Pre-implementation architectural synthesis
│   ├── existing_approaches.md         # Taxonomic summary of non-RL vs RL schedulers
│   ├── candidate_research_gaps.md     # 3 candidate research gaps with paper citations
│   └── proposed_approach.md           # Proposed RL formulation, state/action/reward direction
│
├── datasets/                          # Dataset & trace documentation
│   └── README.md                      # Traces catalog (Google Borg, Alibaba, CAISO, WattTime)
│
├── architecture/                      # System architecture specifications
│   └── README.md                      # Candidate MDP formulation & Gym interface specification
│
└── reports/                           # Milestones and progress reports
    └── README.md                      # Phase checkpoints and course deliverables tracking
```

---

## 12. Expected Outcomes
1. **Academic Survey Report:** A comprehensive Systematic Literature Survey paper synthesized across 30 core peer-reviewed papers.
2. **Reproducible Experimental Testbed:** A discrete-event cloud scheduling simulation environment integrated with Farama Gymnasium.
3. **Validated RL Agent:** An empirically evaluated reinforcement learning policy delivering verifiable carbon reductions against baseline schedulers without SLA degradation.
4. **Course Project Report & Presentation:** Complete academic report documenting methodologies, mathematical formulations, baseline benchmarks, and open research questions.

---

## 13. Contributors & Course Information
- **Course:** Cloud Computing Course Project
- **Lead Researcher / Maintainer:** Nilakhs ([@Nilakhs](https://github.com/Nilakhs))
- **Role:** Systematic Literature Review, Problem Formulation & Simulation Architecture

---

## 14. References & Documentation Links
- **Survey Methodology:** [`docs/research_methodology.md`](docs/research_methodology.md)
- **Detailed Problem Statement:** [`docs/problem_statement.md`](docs/problem_statement.md)
- **SLR Master Database:** [`literature_survey/papers_master.csv`](literature_survey/papers_master.csv)
- **BibTeX Citations:** [`literature_survey/references.bib`](literature_survey/references.bib)
- **PRISMA Audit Report:** [`literature_survey/Audit_Report.md`](literature_survey/Audit_Report.md)

---

## 15. License
Licensing terms for this project are currently being confirmed with course faculty and contributors. A formal license file will be added once approved.
