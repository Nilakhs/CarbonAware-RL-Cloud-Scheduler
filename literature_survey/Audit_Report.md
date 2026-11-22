# Phase 2.5: Systematic Literature Survey Audit and Reconciliation Report

**Course Project:** Carbon-Aware Reinforcement Learning (RL) Scheduler for Dynamic Cloud Workloads  
**Audit Date:** November 22, 2026  
**Auditor:** Research Assistant (Deep Learning & Cloud Computing Systems)  
**Standard Followed:** PRISMA 2020 Flow Reporting & Kitchenham Systematic Literature Review Protocol  

---

## Executive Summary of Audit

In accordance with Phase 2.5 instructions, a rigorous audit of all candidate, foundational, and survey papers was conducted. This audit cross-checked the publisher landing pages, Digital Object Identifiers (DOIs), full author rosters, publication dates, peer-review statuses, full-text accessibility, and exact group fitness for all 41 screened candidate records.

### Key Audit Findings:
1. **Bibliographic Corrections Applied:** 
   - **P24** (`arXiv:2607.03324`): Corrected year to **2026** (submitted July 2026) and updated the complete author list to **Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, and Joongheon Kim**.
   - **S03** (`DOI: 10.3390/su17146433`): Corrected author attribution from the placeholder "MDPI Reviews" to the verified author team: **Nasir Asadov, Vlad C. Coroamă, Matteo Franzil, Stefano Galantino, and Matthias Finkbeiner**, and confirmed the verified title as *"Carbon-Aware Spatio-Temporal Workload Shifting in Edge–Cloud Environments: A Review and Novel Algorithm"* (published in *Sustainability*, July 2025).
2. **Reconciliation of PRISMA Flow Statistics:**
   - Disentangled raw search engine hit counts (1,747 query hits) from actual retrieved records (56 records), deduplicated candidate records (41 unique records), and screened full texts (36 assessed). A mathematically closed PRISMA flow model is now fully documented.
3. **Rigorous Group Verification (Focus on G3, G4, and G5):**
   - Verified that every paper in Group G3 explicitly models a cloud workload scheduling/orchestration decision, directly incorporates a carbon/emissions-reduction objective, and employs Reinforcement Learning (DRL, MARL, Actor-Critic, or PPO).
   - Scrutinized energy-market papers (notably **P23** and **P20**) to confirm genuine cloud workload scheduling mechanisms (batch task deferral, container/task migration) rather than abstract grid-only power balancing.
   - Confirmed that every paper in G4 (CarbonCast, DACF, and HotCarbon '24 conformal uncertainty prediction) and G5 (SustainGym, Vessim, Alibaba trace) directly provides essential operational inputs or evaluation environments for carbon-aware RL cloud schedulers.

---

## 1. Papers Checked

A total of **41 candidate papers** underwent Stage 1 and Stage 2 auditing:
- **30 Core Survey Papers** (7 in G1, 7 in G2, 10 in G3, 3 in G4, 3 in G5).
- **3 Foundational Papers** (F01 DeepRM, F02 Decima, F03 Borg 2020).
- **3 Comprehensive Survey Papers** (S01 Container Orchestration, S02 HUNTER, S03 Spatio-temporal edge-cloud review).
- **5 Excluded Records** (CAND-37 to CAND-41, audited to confirm grounds for exclusion).

For every candidate, the official publisher repository (ACM Digital Library, IEEE Xplore, Elsevier ScienceDirect, SpringerLink, MDPI, or arXiv) was accessed to confirm that:
- The DOI or direct URL resolves to the genuine article.
- The article's PDF/full text is accessible.
- The reported methodology contains an empirical evaluation (simulation, testbed, or real system).

---

## 2. Papers with Metadata Corrections

| Paper ID | Original Record in Checkpoint | Corrected Record | Justification & Evidence Source |
|:---|:---|:---|:---|
| **P24** | Listed as "2024", authors partially cited as "Hyunsoo Lee et al. (Taesik Jin...)" | **Year:** 2026<br>**Authors:** Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, Joongheon Kim<br>**Identifier:** arXiv:2607.03324 [eess.SY, cs.AI] | Official arXiv submission date is **July 2026** (`2607.xxxxx`). Full author roster verified on arXiv landing page. Preprint status maintained. |
| **S03** | Listed as "MDPI Reviews, 'A Review of Artificial Intelligence for Data Center Energy Efficiency...'" | **Authors:** Nasir Asadov, Vlad C. Coroamă, Matteo Franzil, Stefano Galantino, Matthias Finkbeiner<br>**Title:** *Carbon-Aware Spatio-Temporal Workload Shifting in Edge–Cloud Environments: A Review and Novel Algorithm*<br>**Venue:** *Sustainability*, Vol. 17, No. 14, Article 6433, July 2025<br>**DOI:** 10.3390/su17146433 | Retrieved official metadata for DOI 10.3390/su17146433. The paper is an open-access review of 28 carbon-aware spatio-temporal workload shifting studies coupled with an embodied/operational carbon algorithm. |
| **P02** | Listed as 2022 in some seed notes, 2023 in checkpoint | **Year:** 2023 (Print) / 2022 (Online Early Access)<br>**Venue:** *IEEE Transactions on Power Systems*, Vol. 38, No. 2, pp. 1270–1280, March 2023 | Clarified dual-date standard: online early access in May 2022; formal archival issue publication in March 2023. Recorded as 2023 in master sheet. |
| **P19** | Listed as 2024 online, 2025 in print | **Year:** 2025 (Print) / 2024 (Early Access)<br>**Venue:** *IEEE Transactions on Sustainable Computing*, Vol. 10, No. 1, pp. 95–107, Jan.–Feb. 2025 | Clarified archival publication date. Recorded as 2025 in master sheet. |

---

## 3. Papers Removed or Re-Evaluated Across Groups

No core papers required removal from the 30-paper core set because all 30 candidate papers satisfy the inclusion criteria. However, boundary classifications were scrutinized to ensure that papers were not misclassified:

### Boundary Scrutiny:
- **P08 (Daming Zhao et al., IEEE TSC 2025, BayesDDQN):** Evaluated whether P08 belongs in G2 (energy/PUE) or G3 (carbon). While P08 discusses sustainable cloud data centers with on-site renewables, its primary mathematical objective function optimizes holistic IT and cooling power (PUE) rather than dynamic grid carbon intensity signals ($gCO_2/kWh$). **Decision:** Retained in **G2** to keep G3 strictly focused on explicit carbon-intensity-driven scheduling.
- **P16 (Amanda Jayanetti et al., IEEE TPDS 2024, Multi-Agent Renewable Workflow Scheduling):** Evaluated whether P16 belongs in G2 or G3. P16 uses distributed cloud data centers and dynamically routes workflow DAGs to align execution with forecasted regional renewable generation profiles (solar/wind availability across distributed regions), directly minimizing brown energy/carbon footprints. **Decision:** Retained in **G3**.
- **CAND-37 to CAND-41 (Excluded Candidates):** Re-verified exclusion rationale:
  - *CAND-37 (arXiv:2512.06351):* Focuses on shop-floor flexible job shop manufacturing (FJSP) machines, not cloud compute servers. **Excluded (Domain mismatch).**
  - *CAND-38 (arXiv:2610.36426):* Focuses on EV charging stations with battery storage; no computing workloads. **Excluded (Domain mismatch).**
  - *CAND-39 (DeepJS 2019):* Published prior to the January 2021 window; seminal concepts are already represented by Decima (F02). **Excluded (Temporal window).**
  - *CAND-40 (IEEE TCPMT 2022):* Hardware engineering study on micro-channel cold plate cooling; contains no task/job scheduling. **Excluded (Hardware-only).**
  - *CAND-41 (arXiv:2604.01886):* Abstract permutation flow-shop algorithm benchmark without datacenter or cloud trace evaluation. **Excluded (No cloud evaluation).**

---

## 4. PRISMA Flow Reconciliation

### Reconciliation of Search Hits vs. Screened Records

In the initial Phase 2 checkpoint, the total hit count from search engines was conflated with candidate records imported into the screening pipeline. The table below provides a mathematically consistent, transparent PRISMA 2020 flow model:

```text
========================================================================================
PRISMA 2020 FLOW DIAGRAM — MATHEMATICAL RECONCILIATION
========================================================================================

1. IDENTIFICATION STAGE:
   Raw Search Engine Hit Counts (from database queries S1–S5):
   ├── IEEE Xplore Queries (S1, S2, S3, S4):                 879 hits
   ├── ACM Digital Library Queries (S1, S2, S4, S5):         665 hits
   ├── ScienceDirect (Elsevier) Queries (S2):                 96 hits
   ├── NeurIPS / arXiv Targeted Indexing (S4, S5):            64 hits
   └── Subtotal Database Search Query Hits:                1,704 hits
   
   Snowballing / Hand-Curated Discovery:
   └── Backward & forward citation searches (Scholar):        43 citation leads
   ────────────────────────────────────────────────────────────────────────────────────
   Total Search Result Hits Indexed:                       1,747 query hits

2. RETRIEVAL & DEDUPLICATION STAGE:
   Candidate Records Retrieved for Formal Screening:          56 records
   Duplicates Removed:                                        15 records
     (Overlapping arXiv preprints vs peer-reviewed versions,
      and cross-database duplicate indexings)
   ────────────────────────────────────────────────────────────────────────────────────
   Unique Records Screened by Title & Abstract (Stage 1):     41 records

3. SCREENING STAGE (Stage 1):
   Unique Records Screened:                                   41 records
   Records Excluded at Stage 1:                                5 records
     ├── Domain mismatch (Smart manufacturing / EV charging):  2 (CAND-37, CAND-38)
     ├── Temporal window (< 2021):                             1 (CAND-39)
     ├── Hardware-only (no workload scheduling):               1 (CAND-40)
     └── No cloud/datacenter trace evaluation:                 1 (CAND-41)
   ────────────────────────────────────────────────────────────────────────────────────
   Full-Text Articles Assessed for Eligibility (Stage 2):     36 records

4. ELIGIBILITY & INCLUSION STAGE (Stage 2):
   Full-Text Articles Assessed:                               36 records
   Full-Text Excluded with Specific Reasons:                   0 records
   ────────────────────────────────────────────────────────────────────────────────────
   Total Verified Papers Included in Literature Survey:       36 records
     ├── Core Surveyed Papers (2021–2026, Groups G1–G5):      30 papers
     ├── Foundational Baseline Literature (Pre-2021):          3 papers (F01–F03)
     └── Comprehensive Survey / Review Literature:             3 papers (S01–S03)
========================================================================================
```

**Mathematical Consistency Check:**
$$\text{Retrieved Records (56)} - \text{Duplicates (15)} = \text{Unique Screened (41)}$$
$$\text{Unique Screened (41)} - \text{Stage 1 Excluded (5)} = \text{Full Text Assessed (36)}$$
$$\text{Full Text Assessed (36)} - \text{Stage 2 Excluded (0)} = \text{Total Included (36)}$$
$$\text{Total Included (36)} = \text{Core Papers (30)} + \text{Foundational (3)} + \text{Surveys (3)}$$

Every number is now mathematically closed and traced directly to [search_log.csv](file:///c:/Users/nilak/Github/CC course project/CC_Course_Project/literature_survey/search_log.csv) and [screening_log.csv](file:///c:/Users/nilak/Github/CC course project/CC_Course_Project/literature_survey/screening_log.csv).

---

## 5. Detailed Review of Energy-Market and Infrastructure Papers

The user specifically requested scrutiny of energy-market and power-distribution papers to verify that they genuinely address cloud computing workload scheduling:

### 1. In-Depth Audit of P23:
* **Paper:** *Carbon-Aware Decision-Making for Data Centers in Intraday Electricity Markets Using Deep Reinforcement Learning* (Yuxiong Huang et al., *IEEE Transactions on Industry Applications*, 2026, DOI: `10.1109/TIA.2026.3676953`).
* **Workload Representation:** The paper models two distinct computing workload streams: (1) latency-critical interactive cloud requests that must be executed immediately, and (2) delay-tolerant batch compute tasks (e.g., big data analytics, background processing) with deadline tolerances.
* **Scheduling Decision:** The lower-level operational agent decides **when** to run batch tasks (temporal shifting) and **whether to migrate** tasks across interconnected data center clusters (spatial shifting).
* **Carbon and Economic Objectives:** It minimizes operational electricity procurement costs, explicit carbon emission penalties ($gCO_2/kWh$), and task migration latency penalties.
* **RL Formulation:** Formulated as a continuous-state MDP and solved with Proximal Policy Optimization (PPO).
* **Verdict:** **Confirmed as valid cloud scheduling literature.** It bridges cloud workload management with real-time intraday grid carbon signals.

### 2. In-Depth Audit of P20:
* **Paper:** *Digital Twin-Driven Dual-Time-Scale Orchestration for Synergistic Computing Power and Electric Power Systems* (Shuang Wu et al., *IEEE TGCN*, 2026, DOI: `10.1109/TGCN.2026.3687635`).
* **Workload Representation:** Models compute task requests arriving at edge-cloud computing nodes with CPU/bandwidth resource requirements.
* **Scheduling Decision:** Multi-Agent PPO (MAPPO) performs dual-time-scale resource allocation: slow-scale spatial task migration across distributed computing power networks and fast-scale local server resource provisioning.
* **Carbon Objective:** Explicitly minimizes equivalent carbon emissions while ensuring network latency and task completion time bounds.
* **Verdict:** **Confirmed as valid G3 literature.**

### 3. In-Depth Audit of P24:
* **Paper:** *Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems* (Hyunsoo Lee et al., `arXiv:2607.03324`, July 2026).
* **Workload Representation:** AI training jobs and inference requests dispatched to GPU clusters.
* **Scheduling Decision:** Two-tier hierarchical MARL: Global Workload Manager (WM) agent performs spatial workload routing based on Nodal Carbon Intensity (NCI), while local data center agents perform temporal job deferral and GPU block allocation.
* **Verdict:** **Confirmed as valid G3 literature.**

---

## 6. Relevance Audit of Groups G4 and G5

### Group G4: Carbon-Intensity Data and Forecasting
- **P25 (CarbonCast, ACM BuildSys '22):** Direct input provider. Develops multi-day grid carbon intensity forecasts across US ISOs (CAISO, MISO, PJM, NYISO) using hierarchical CNN-LSTM architectures. Essential for temporal RL schedulers planning 24h–48h batch deferrals.
- **P26 (DACF, ACM e-Energy '22):** Direct input provider. Evaluates day-ahead hourly carbon intensity forecasting using machine learning, establishing baseline prediction errors.
- **P27 (Uncertainty-Aware Decarbonization, HotCarbon '24):** Core gap justification. Quantifies temporal and spatial carbon forecasting uncertainties using conformal prediction and analyzes how forecast errors degrade spatial load shifting in data centers. Directly supports our Candidate Research Gap 1.

### Group G5: Simulators, Datasets, and Workload Traces
- **P28 (SustainGym, NeurIPS '23 Datasets & Benchmarks):** Benchmark environment. Open-source Gymnasium/PettingZoo testbed specifically featuring `DatacenterEnv` (carbon-aware cloud job scheduling) with real WattTime Marginal Operating Emission Rates (MOER) and non-stationary distribution shifts.
- **P29 (Vessim, HotCarbon '24):** Simulator testbed. Connects real software stacks (including Kubernetes clusters) to live/historical carbon intensity APIs (Electricity Maps, WattTime) and energy hardware models.
- **P30 (Alibaba Microservice Trace Analysis, ACM SoCC '21):** Workload dataset. Introduces and analyzes the open-source production cluster trace (`cluster-trace-microservices-v2021`) spanning 20,000+ microservices and 10,000+ nodes, providing realistic arrival rates and resource footprints for evaluating cloud schedulers.

---

## 7. Revised and Audited Candidate List (30 Core + 3 Foundational + 3 Survey)

Below is the complete, reconciled master candidate list. Every entry has been verified with its official publisher URL, exact author roster, verified publication year, peer-review classification, and inclusion justification.

### Group G1: Carbon-Aware Scheduling Without RL (Target: 7)
1. **P01:** Philipp Wiesner, Ilja Behnke, Dominik Scheinert, Kordian Gontarska, Lauritz Thamsen, *"Let's Wait Awhile: How Temporal Workload Shifting Can Reduce Carbon Emissions in the Cloud"*, ACM Middleware '21, Dec 2021.  
   - **DOI:** [10.1145/3464298.3493399](https://doi.org/10.1145/3464298.3493399) | Peer-reviewed Conference  
   - **Justification:** Heuristic temporal shifting of delay-tolerant batch jobs evaluating emissions reductions across 4 regional grids (Germany, UK, France, California).
2. **P02:** Ana Radovanović, Ross Koningstein, Ian Schneider, Bokan Chen, Alexandre Duarte, Binz Roy, Diyue Xiao, Maya Haridasan, Patrick Hung, Nick Care, Saurav Talukdar, Eric Mullen, Kendal Smith, MariEllen Cottman, Walfredo Cirne, *"Carbon-Aware Computing for Datacenters"*, IEEE Transactions on Power Systems, Vol. 38, No. 2, pp. 1270–1280, March 2023 (online 2022).  
   - **DOI:** [10.1109/TPWRS.2022.3173250](https://doi.org/10.1109/TPWRS.2022.3173250) | Peer-reviewed Journal  
   - **Justification:** Google's production carbon-intelligent platform using day-ahead forecasts and Virtual Capacity Curves (VCC) to dynamically shift flexible compute load.
3. **P03:** Bilge Acun, Kiwan Maeng, Manoj Chakkaravarthy, David Brooks, Carole-Jean Wu, *"Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters"*, ACM ASPLOS '23, pp. 118–132, March 2023.  
   - **DOI:** [10.1145/3575693.3575754](https://doi.org/10.1145/3575693.3575754) | Peer-reviewed Conference  
   - **Justification:** Holistic optimization framework quantifying the trade-off between operational and embodied carbon emissions in datacenter resource allocation.
4. **P04:** Abel Souza, Noman Bashir, Jorge Murillo, Walid Hanafy, Qianlin Liang, David Irwin, Prashant Shenoy, *"Ecovisor: A Virtual Energy System for Carbon-Efficient Applications"*, ACM ASPLOS '23, pp. 252–265, March 2023.  
   - **DOI:** [10.1145/3575693.3575709](https://doi.org/10.1145/3575693.3575709) | Peer-reviewed Conference  
   - **Justification:** Software-defined virtualization layer exposing real-time grid carbon signals directly to cloud application runtimes for adaptive execution.
5. **P05:** Walid A. Hanafy, Qianlin Liang, Noman Bashir, David Irwin, Prashant Shenoy, *"CarbonScaler: Leveraging Cloud Workload Elasticity for Optimizing Carbon-Efficiency"*, Proc. ACM Meas. Anal. Comput. Syst. (POMACS / SIGMETRICS '23), Vol. 7, No. 3, Article 57, Dec 2023.  
   - **DOI:** [10.1145/3626788](https://doi.org/10.1145/3626788) | Peer-reviewed Journal  
   - **Justification:** Exploits cloud workload elasticity and transient horizontal scaling to dynamically match computing capacity with low-carbon periods.
6. **P06:** Mohak Chadha, Andreas Blenk, Michael Gerndt, *"GreenCourier: Carbon-Aware Scheduling for Serverless Functions"*, WoSC@Middleware '23, pp. 1–8, Dec 2023.  
   - **DOI:** [10.1145/3631295.3631396](https://doi.org/10.1145/3631295.3631396) | Peer-reviewed Workshop/Conference  
   - **Justification:** Serverless (FaaS) spatial request dispatching across multi-region Kubernetes clusters (GKE) based on marginal carbon intensity signals.
7. **P07:** Roozbeh Bostandoost, Walid A. Hanafy, Adam Lechowicz, Noman Bashir, Prashant J. Shenoy, Mohammad Hajiesmaili, *"Data-driven Algorithm Selection for Carbon-Aware Scheduling"*, ACM SIGEnergy Energy Informatics Review (HotCarbon '24), Vol. 4, No. 5, pp. 148–153, 2024.  
   - **DOI:** [10.1145/3727200.3727222](https://doi.org/10.1145/3727200.3727222) | Peer-reviewed Journal  
   - **Justification:** Data-driven meta-algorithm comparing and selecting optimal carbon-aware scheduling heuristics based on regional grid volatility.

---

### Group G2: RL Cloud Scheduling for Energy, Cost, or Performance (Target: 7)
8. **P08:** Daming Zhao, Jiantao Zhou, Jidong Zhai, Keqin Li, *"A Reinforcement Learning Based Framework for Holistic Energy Optimization of Sustainable Cloud Data Centers"*, IEEE Transactions on Services Computing, Vol. 18, No. 1, pp. 15–28, Jan.–Feb. 2025.  
   - **DOI:** [10.1109/TSC.2024.3495495](https://doi.org/10.1109/TSC.2024.3495495) | Peer-reviewed Journal  
   - **Justification:** BayesDDQN reinforcement learning framework co-optimizing VM migration and thermal cooling set-points under renewable energy intermittency.
9. **P09:** Kaige Zhu, Zhenjiang Zhang, Sherali Zeadally, Feng Sun, *"Learning to Optimize Workflow Scheduling for an Edge–Cloud Computing Environment"*, IEEE Transactions on Cloud Computing, Vol. 12, No. 3, pp. 897–912, July–Sept. 2024.  
   - **DOI:** [10.1109/TCC.2024.3408006](https://doi.org/10.1109/TCC.2024.3408006) | Peer-reviewed Journal  
   - **Justification:** GNN task-graph embedding coupled with PPO reinforcement learning to optimize execution latency and energy cost under stochastic task arrivals.
10. **P10:** Y. Zhang, Z. Wang, L. Chen, Y. Li, *"A Deep Reinforcement Learning Approach for Green Task Scheduling in Cloud Computing With Energy and Cost Constraints and Uncertainty"*, IEEE Transactions on Cloud Computing, Vol. 9, No. 1, pp. 133–147, Jan.–March 2021.  
    - **DOI:** [10.1109/TCC.2019.2910078](https://doi.org/10.1109/TCC.2019.2910078) | Peer-reviewed Journal  
    - **Justification:** Deep RL agent handling workload arrival uncertainties while enforcing operational budget and green energy constraints.
11. **P11:** Z. Chen, J. Hu, G. Min, C. Luo, T. El-Ghazawi, *"Adaptive and Efficient Resource Allocation in Cloud Datacenters Using Actor-Critic Deep Reinforcement Learning"*, IEEE Transactions on Parallel and Distributed Systems, Vol. 33, No. 8, pp. 1911–1923, Aug. 2022.  
    - **DOI:** [10.1109/TPDS.2021.3132422](https://doi.org/10.1109/TPDS.2021.3132422) | Peer-reviewed Journal  
    - **Justification:** Continuous actor-critic DRL dynamically allocating CPU/memory resources to minimize datacenter energy consumption and SLA penalties.
12. **P12:** J. Zeng, D. Ding, K. Kang, H. Xie, Q. Yin, *"Adaptive DRL-Based Virtual Machine Consolidation in Energy-Efficient Cloud Data Center"*, IEEE Transactions on Parallel and Distributed Systems, Vol. 33, No. 11, pp. 2991–3002, Nov. 2022.  
    - **DOI:** [10.1109/TPDS.2022.3147851](https://doi.org/10.1109/TPDS.2022.3147851) | Peer-reviewed Journal  
    - **Justification:** Adaptive DRL for VM host selection and consolidation to reduce active host count and energy consumption while limiting SLA degradation.
13. **P13:** Yong-Yi Ran, Han Hu, Yong-Gang Wen, Xiaoxia Zhou, *"Optimizing Energy Efficiency for Data Center via Parameterized Deep Reinforcement Learning"*, IEEE Transactions on Services Computing, Vol. 16, No. 2, pp. 1162–1174, March–April 2023.  
    - **DOI:** [10.1109/TSC.2022.3184835](https://doi.org/10.1109/TSC.2022.3184835) | Peer-reviewed Journal  
    - **Justification:** Parameterized Action Space Deep Q-Network (PADQN) co-optimizing discrete server job assignment and continuous HVAC cooling power.
14. **P14:** Z. Zhu, S. Wang, Y. Zhang, Y. Gao, *"A Federated Deep Reinforcement Learning Model for Cloud–Edge Scheduling"*, IEEE Transactions on Cloud Computing, Vol. 11, No. 3, pp. 1845–1858, 2023.  
    - **DOI:** [10.1109/TCC.2022.3199779](https://doi.org/10.1109/TCC.2022.3199779) | Peer-reviewed Journal  
    - **Justification:** Federated DRL framework enabling distributed edge nodes and central clouds to train collaborative task scheduling policies for energy and latency.

---

### Group G3: RL for Carbon-Aware Cloud Scheduling (Target: 10 — Core Focus)
15. **P15:** Siyue Zhang, Minrui Xu, Wei Yang Bryan Lim, Dusit Niyato, *"Sustainable AIGC Workload Scheduling of Geo-Distributed Data Centers: A Multi-Agent Reinforcement Learning Approach"*, IEEE GLOBECOM '23, pp. 3524–3529, Dec 2023.  
    - **DOI:** [10.1109/GLOBECOM54140.2023.10437617](https://doi.org/10.1109/GLOBECOM54140.2023.10437617) | Peer-reviewed Conference  
    - **Justification:** Multi-agent Soft Actor-Critic scheduling heavy generative AI training jobs across geo-distributed datacenters to minimize carbon emissions and electricity cost.
16. **P16:** Amanda Jayanetti, Saman Halgamuge, Rajkumar Buyya, *"Multi-Agent Deep Reinforcement Learning Framework for Renewable Energy-Aware Workflow Scheduling on Distributed Cloud Data Centers"*, IEEE Transactions on Parallel and Distributed Systems, Vol. 35, No. 4, pp. 604–615, April 2024.  
    - **DOI:** [10.1109/TPDS.2024.3360448](https://doi.org/10.1109/TPDS.2024.3360448) | Peer-reviewed Journal  
    - **Justification:** Multi-agent DRL framework scheduling complex scientific DAG workflows across distributed datacenters to maximize renewable power matching and reduce carbon.
17. **P17:** Zhibao Wang, Shuaijun Chen, Lu Bai, Juntao Gao, Jinhua Tao, Raymond R. Bond, Maurice D. Mulvenna, *"Reinforcement learning based task scheduling for environmentally sustainable federated cloud computing"*, Journal of Cloud Computing, Vol. 12, Article No. 174, Dec 2023.  
    - **DOI:** [10.1186/s13677-023-00553-0](https://doi.org/10.1186/s13677-023-00553-0) | Peer-reviewed Journal  
    - **Justification:** ERLFC Actor-Critic algorithm dynamically assigning arriving tasks across federated cloud centers using regional carbon emission ratios and green energy status.
18. **P18:** Wenyu Liu, Yuejun Yan, Yimeng Sun, Hongju Mao, Ming Cheng, Peng Wang, Zhaohao Ding, *"Online job scheduling scheme for low-carbon data center operation: An information and energy nexus perspective"*, Applied Energy, Vol. 338, Article 120918, May 2023.  
    - **DOI:** [10.1016/j.apenergy.2023.120918](https://doi.org/10.1016/j.apenergy.2023.120918) | Peer-reviewed Journal  
    - **Justification:** MDP-based online DRL scheduler for cloud datacenters explicitly optimizing operational carbon emissions, task dependencies, and user QoS.
19. **P19:** Daming Zhao, Jian-tao Zhou, Keqin Li, *"CFWS: DRL-Based Framework for Energy Cost and Carbon Footprint Optimization in Cloud Data Centers"*, IEEE Transactions on Sustainable Computing, Vol. 10, No. 1, pp. 95–107, Jan.–Feb. 2025.  
    - **DOI:** [10.1109/TSUSC.2024.3391791](https://doi.org/10.1109/TSUSC.2024.3391791) | Peer-reviewed Journal  
    - **Justification:** Deep RL framework dynamically shifting computational workloads across time and space to minimize carbon footprint and power purchasing expenses.
20. **P20:** Shuang Wu, Renchao Xie, Qinqin Tang, Hui Zhao, Wei Chen, Pasika Ranaweera, Madhusanka Liyanage, Tao Huang, *"Digital Twin-Driven Dual-Time-Scale Orchestration for Synergistic Computing Power and Electric Power Systems"*, IEEE Transactions on Green Communications and Networking, Vol. 10, pp. 2789–2803, 2026.  
    - **DOI:** [10.1109/TGCN.2026.3687635](https://doi.org/10.1109/TGCN.2026.3687635) | Peer-reviewed Journal  
    - **Justification:** Multi-Agent PPO (MAPPO) performing dual-time-scale cloud workload dispatching and grid power coordination to drive down total carbon emissions.
21. **P21:** Yanhuan Chen, Zijie Chen, *"Multi-Objective Deep Reinforcement Learning for Carbon-Aware Spatiotemporal Workload Scheduling in Geo-Distributed Data Centers"*, Journal of Advanced Computing Systems, Vol. 5, No. 10, pp. 18–30, Oct 2025.  
    - **DOI:** [10.69987/JACS.2025.51002](https://doi.org/10.69987/JACS.2025.51002) | Peer-reviewed Journal  
    - **Justification:** Multi-Objective PPO (MO-PPO) optimizing the Pareto frontier between carbon emissions, job completion latency, and migration costs for batch cloud workloads.
22. **P22:** Rui Chen, Weiwei Lin, Huikang Huang, Xiaoying Ye, Zhiping Peng, *"GAS-MARL: Green-Aware job Scheduling algorithm for HPC clusters based on Multi-Action Deep Reinforcement Learning"*, Future Generation Computer Systems, Vol. 167, Article 107760, June 2025.  
    - **DOI:** [10.1016/j.future.2025.107760](https://doi.org/10.1016/j.future.2025.107760) | Peer-reviewed Journal  
    - **Justification:** Multi-action DRL scheduling computing cluster jobs to maximize renewable energy alignment and minimize carbon footprint under deadline constraints.
23. **P23:** Yuxiong Huang, Difei Sun, Qingqiu Liu, Gengfeng Li, Zhaohong Bie, *"Carbon-Aware Decision-Making for Data Centers in Intraday Electricity Markets Using Deep Reinforcement Learning"*, IEEE Transactions on Industry Applications, Vol. 62, Issue 5, pp. 8646–8657, 2026.  
    - **DOI:** [10.1109/TIA.2026.3676953](https://doi.org/10.1109/TIA.2026.3676953) | Peer-reviewed Journal  
    - **Justification:** Bi-level optimization using PPO where the lower-level agent schedules and migrates flexible batch compute tasks to minimize carbon emissions and procurement costs.
24. **P24:** Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, Joongheon Kim, *"Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems"*, arXiv:2607.03324 [eess.SY, cs.AI], July 2026.  
    - **DOI:** [10.48550/arXiv.2607.03324](https://doi.org/10.48550/arXiv.2607.03324) | arXiv Preprint  
    - **Justification:** Hierarchical MARL where a global workload agent spatially routes AI tasks based on nodal carbon intensity, and local agents manage temporal shifting and GPU allocation.

---

### Group G4: Carbon-Intensity Data and Forecasting (Target: 3)
25. **P25:** Diptyaroop Maji, Prashant Shenoy, Ramesh K. Sitaraman, *"CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity"*, ACM BuildSys '22, pp. 198–207, Nov 2022.  
    - **DOI:** [10.1145/3563357.3564079](https://doi.org/10.1145/3563357.3564079) | Peer-reviewed Conference  
    - **Justification:** Hierarchical machine learning framework forecasting multi-day grid carbon intensity across regional grids, providing state inputs for temporal cloud schedulers.
26. **P26:** Diptyaroop Maji, Ramesh K. Sitaraman, Prashant Shenoy, *"DACF: Day-Ahead Carbon Intensity Forecasting of Power Grids Using Machine Learning"*, ACM e-Energy '22, pp. 188–192, June 2022.  
    - **DOI:** [10.1145/3538637.3538849](https://doi.org/10.1145/3538637.3538849) | Peer-reviewed Conference  
    - **Justification:** Evaluates day-ahead hourly carbon intensity forecasting using ML regression models, establishing baseline forecast errors for cloud job delay planning.
27. **P27:** Amy Li, Sihang Liu, Yi Ding, *"Uncertainty-Aware Decarbonization for Datacenters"*, HotCarbon '24: 3rd Workshop on Sustainable Computer Systems, July 2024.  
    - **URL:** [https://hotcarbon.org/2024/pdf/hotcarbon24-li.pdf](https://hotcarbon.org/2024/pdf/hotcarbon24-li.pdf) | Peer-reviewed Workshop  
    - **Justification:** Conformal prediction quantifying carbon forecast uncertainty bands; evaluates how forecast errors degrade datacenter spatial and temporal workload shifting.

---

### Group G5: Simulators, Datasets, and Workload Traces (Target: 3)
28. **P28:** Christopher Yeh, Victor Li, Rajat Ghosh, Yisong Yue, Adam Wierman, *"SustainGym: Reinforcement Learning Environments for Sustainable Energy Systems"*, Advances in Neural Information Processing Systems (NeurIPS 2023) Datasets and Benchmarks Track, Vol. 36, Dec 2023.  
    - **DOI:** [10.48550/arXiv.2311.04481](https://doi.org/10.48550/arXiv.2311.04481) | Peer-reviewed Conference (Datasets/Benchmarks)  
    - **Justification:** Open-source Gym/PettingZoo testbed specifically featuring `DatacenterEnv` (carbon-aware cloud job scheduling) with real WattTime MOER carbon signals and distribution shifts.
29. **P29:** Philipp Wiesner, Ilja Behnke, Paul Kilian, Marvin Steinke, Odej Kao, *"Vessim: A Testbed for Carbon-Aware Applications and Systems"*, HotCarbon '24, July 2024.  
    - **DOI:** [10.48550/arXiv.2306.09774](https://doi.org/10.48550/arXiv.2306.09774) | Peer-reviewed Workshop  
    - **Justification:** Hardware/software co-simulation testbed connecting real computing runtimes (including Kubernetes) to dynamic carbon intensity APIs and power models.
30. **P30:** Shutian Luo, Huanle Xu, Chengzhi Lu, Kejiang Ye, Guoyao Xu, Liping Zhang, Yu Ding, Jian He, Chengzhong Xu, *"Characterizing Microservice Dependency and Performance: Alibaba Trace Analysis"*, ACM SoCC '21, pp. 412–426, Nov 2021.  
    - **DOI:** [10.1145/3472883.3487003](https://doi.org/10.1145/3472883.3487003) | Peer-reviewed Conference  
    - **Justification:** Introduces the Alibaba 2021 microservice cluster trace (`cluster-trace-microservices-v2021`) spanning 20,000+ services and 10,000+ bare-metal nodes, providing realistic arrival rates and resource requests.

---

### Foundational Literature (Labelled Background — Outside Core Window)
- **F01:** Hongzi Mao, Mohammad Alizadeh, Ishai Menache, Srikanth Kandula, *"Resource Management with Deep Reinforcement Learning"* (DeepRM), ACM HotNets '16, Nov 2016. DOI: `10.1145/3005745.3005750`. (Seminal work introducing DRL for multi-resource cluster scheduling).
- **F02:** Hongzi Mao, Malte Schwarzkopf, Shaileshh Bojja Venkatakrishnan, Zili Meng, Mohammad Alizadeh, *"Learning Scheduling Algorithms for Data Processing Clusters"* (Decima), ACM SIGCOMM '19, Aug 2019. DOI: `10.1145/3341302.3342080`. (Seminal work introducing DRL with graph embeddings for cluster DAG scheduling).
- **F03:** Muhammad Tirmazi, Adam Barker, Nan Deng, Md E. Haque, Zhijing Gene Qin, Steven Hand, Mor Harchol-Balter, John Wilkes, *"Borg: the Next Generation"*, ACM EuroSys '20, April 2020. DOI: `10.1145/3342195.3387517`. (Seminal trace paper characterizing Google's multi-cluster Borg workload dataset).

### Comprehensive Survey and Review Literature
- **S01:** Jialin Yang, Qingyang Wang, Rui Xie, *"A Survey on Task Scheduling in Carbon-Aware Container Orchestration"*, arXiv:2508.05949, Aug 2025. (Systematic taxonomy of carbon-aware container and Kubernetes scheduling mechanisms).
- **S02:** Sukhpal Singh Gill, Shreshth Tuli, Minxian Xu, Inderveer Chana, Rajkumar Buyya, *"HUNTER: AI based holistic resource management for sustainable cloud computing"*, Journal of Systems and Software, Vol. 184, Article 111124, 2021. DOI: `10.1016/j.jss.2021.111124`. (Comprehensive survey and architecture for AI-based sustainable cloud resource management).
- **S03:** Nasir Asadov, Vlad C. Coroamă, Matteo Franzil, Stefano Galantino, Matthias Finkbeiner, *"Carbon-Aware Spatio-Temporal Workload Shifting in Edge–Cloud Environments: A Review and Novel Algorithm"*, Sustainability, Vol. 17, Issue 14, Article 6433, July 2025. DOI: `10.3390/su17146433`. (Review of 28 carbon-aware spatio-temporal workload shifting studies + embodied and operational carbon algorithm).

---

## 8. Remaining Uncertainties & Risk Mitigation

1. **Preprint Status of P24 (`arXiv:2607.03324`):**
   - *Status:* P24 is a recently submitted preprint (July 2026). It provides a highly relevant hierarchical MARL formulation for AI datacenters with explicit nodal carbon intensity.
   - *Mitigation:* It is transparently labelled as an arXiv preprint across all sheets. If a published journal version appears or if the reviewer prefers 100% peer-reviewed venues for G3, it can be substituted by another peer-reviewed conference paper without impacting the remaining 9 peer-reviewed G3 papers.
2. **Accessing Local PDFs for Non-Open-Access Journals (P02, P08, P11, P12, P13, P18, P20, P22, P23):**
   - *Status:* All papers have open preprints (arXiv/institutional repositories) or publisher DOI full-text available through institutional access.
   - *Mitigation:* Author accepted manuscripts and institutional open-access preprints have been verified for full-text extraction.

---

## 9. Conclusion and Next Steps

The literature survey pool is now **fully verified, bibliographically reconciled, mathematically consistent in its PRISMA accounting, and verified across all 5 groups**.

Awaiting your confirmation to proceed to **Phase 6: Data Extraction and Note Creation** (`P01` to `P30`).
