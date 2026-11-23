# Systematic Literature Survey Report: Carbon-Aware Reinforcement Learning Schedulers for Dynamic Cloud Workloads

**Course Project:** Carbon-Aware Reinforcement Learning (RL) Cloud Scheduler for Dynamic Workloads
**Survey Corpus:** 30 Core Papers (2021–2026), 4 Foundational Papers, 3 Comprehensive Survey Reviews
**Methodology Standards:** Kitchenham & Charters (2007) / PRISMA 2020 / Wohlin (2014) Snowballing
**Supporting Extraction Pipeline:** High-Fidelity PDF-to-Markdown Toolchain (`pymupdf4llm`)

---

## Executive Summary

Hyperscale cloud computing infrastructures contribute substantially to global greenhouse gas emissions. While early research focused on energy proportionality and static Power Usage Effectiveness (PUE) minimization, modern decarbonization demands **carbon-aware scheduling**—aligning the spatio-temporal execution of computational workloads with the real-time availability of clean, low-carbon electricity on regional power grids.

This Systematic Literature Review (SLR) provides a comprehensive, primary-source grounded analysis of **30 core research papers (P01–P30)** published between 2021 and 2026, structured across five analytical groups:
1. **Group G1 (P01–P07):** Carbon-Aware Cloud Scheduling without Reinforcement Learning (Heuristics, Integer Linear Programming, and OS Abstractions).
2. **Group G2 (P08–P14):** Reinforcement Learning for Cloud Energy, Cost, and QoS Optimization.
3. **Group G3 (P15–P24):** Reinforcement Learning for Carbon-Aware Cloud Workload Scheduling (Core Domain Focus).
4. **Group G4 (P25–P27):** Grid Carbon-Intensity Modeling, Multi-Day Forecasting, and Uncertainty Quantification.
5. **Group G5 (P28–P30):** Standardized RL Simulators, Co-Simulation Testbeds, and Production Microservice Traces.

Every surveyed paper has been evaluated against an 8-point Quality Assessment (QA) framework with a strict requirement on dynamic grid carbon time series grounding. Across the survey, joint spatio-temporal workload migration achieves up to **41.3% carbon reduction** (P21), hierarchical multi-agent transformers reduce coordination action-spaces by a factor of $1.85 \times 10^{28}$ (P24), and conformal forecast uncertainty bounds prevent up to 10.4 tons of accidental emissions in 20 MW clusters (P27).

---

## 1. Introduction & Research Motivation

Data centers currently account for 1%–2% of global electricity demand, with artificial intelligence (AI) and large language model (LLM) training accelerators rapidly accelerating power density. Traditional cloud resource schedulers are **carbon-agnostic**, optimizing strictly for economic cost, virtual machine consolidation, or tail latency.

However, regional electrical grids exhibit severe **temporal and geographic carbon intensity variance**:
- **Temporal Volatility:** Grid carbon intensity ($g\text{CO}_2/\text{kWh}$) fluctuates by over $4\times$ throughout a single day depending on solar irradiance curves, diurnal wind generation peaks, and fossil-fuel peaker plant activation.
- **Geographic Asymmetry:** Geographically separated data center regions (e.g., California CAISO vs. Midwest MISO or PJM) experience out-of-phase renewable generation peaks and disparate baseline generation mixes.

Reinforcement Learning (RL) has emerged as the premier algorithmic paradigm for carbon-aware scheduling due to its capacity to learn closed-loop control policies in non-stationary, stochastic cloud environments without requiring perfect long-term oracle foresight.

---

## 2. Background and Core Concepts

### 2.1 Carbon Intensity Telemetry: Marginal vs. Average
- **Average Carbon Intensity (ACI):** Total emissions divided by total generation across a grid balancing authority ($\text{gCO}_2/\text{kWh}$). Appropriate for retrospective Scope 2 greenhouse gas accounting.
- **Marginal Operating Emissions Rate (MOER):** Emissions rate of the specific generator that ramps up or down in response to a change in demand at a given minute. Essential for forward-looking cloud scheduling decisions; avoiding 1 kWh of load when dirty peaker plants are running displaces fossil fuel directly.

### 2.2 Workload Shifting Mechanisms
1. **Temporal Shifting (Delay / Postponement):** Deferring flexible, delay-tolerant batch jobs (e.g., model training, data indexing, video encoding) to future time windows with high renewable penetration.
2. **Spatial Migration (Geographic Shifting):** Routing incoming request traffic across distributed wide-area data centers to the lowest-carbon geographic region.
3. **Workload Elasticity & Throttling:** Dynamically scaling compute throughput or quality-of-service (e.g., Google Virtual Capacity Curves) based on available green power budgets.

---

## 3. Systematic Survey Methodology & PRISMA Flow

The review protocol adheres to Kitchenham & Charters (2007) guidelines and PRISMA 2020 standards:
- **Search Strategy:** Formal search strings (`S1` to `S5`) executed across five digital libraries: IEEE Xplore, ACM Digital Library, ScienceDirect (Elsevier), arXiv, and Google Scholar.
- **Corpus Selection:** 57 records retrieved (`RET-01` to `RET-57`), deduplicated down to 42 candidates, and evaluated across two-stage screening to confirm 30 core studies, 4 foundational baselines (`F01`–`F04`), and 3 surveys (`S01`–`S03`).
- **QA Scoring Framework (Q1–Q8):**
  - **Q1 (Problem Formulation):** Clarity and mathematical rigor of objectives and constraints.
  - **Q2 (Methodological Detail):** Complete specification of algorithm, state, action, and reward formulations.
  - **Q3 (Carbon Modeling & Trace Grounding):** Real dynamic grid carbon intensity time series ($g\text{CO}_2/\text{kWh}$ or MOER) from real ISOs/RTOs earns 1.0; meteorological renewable traces without grid carbon APIs earn 0.5; zero carbon data earns 0.0.
  - **Q4 (Workload Realism):** Grounded in authentic production cloud traces (Google Borg, Alibaba, Azure) or physical hardware testbeds.
  - **Q5 (Baseline Comparison):** Benchmarked against competitive non-trivial baselines.
  - **Q6 (Quantitative Metrics):** Concrete numerical reporting of carbon savings, latency, and SLA overhead.
  - **Q7 (Open Science & Reproducibility):** Public code, models, or datasets.
  - **Q8 (Critical Assessment):** Candid discussion of operational trade-offs, constraints, and failure modes.

---

## 4. Supporting Methodology: High-Fidelity PDF-to-Markdown Pipeline

To eliminate hallucination risks from proprietary OCR noise and complex two-column PDF layouts, the review team established a high-fidelity **PDF-to-Markdown extraction toolchain**:
- **Conversion Engine:** PyMuPDF (`pymupdf4llm`), preserving structural heading hierarchies, inline LaTeX mathematical notations, markdown tables, and figure captions.
- **Efficiency:** Achieved a **50.6% token reduction** compared to raw tokenized text while eliminating running headers, footers, and font glyph artifacts.
- **Workflow Artifacts:** Fully documented in [`PDF_TO_MARKDOWN_WORKFLOW.md`](./PDF_TO_MARKDOWN_WORKFLOW.md) and guided by the standardized [`PAPER_ANALYSIS_PROMPT.md`](./PAPER_ANALYSIS_PROMPT.md). All converted markdown files are cataloged in [`markdown_papers/`](./markdown_papers/).

---

## 5. Master Comparative Inventory (P01–P30)

| ID | Title / Citation | Venue / Year | Group | Scheduling Mechanism | Carbon Data Grounding | Workload / System Grounding | Strict QA Score | Primary Note Link |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :---: | :--- |
| **P01** | *Let's Wait Awhile* (Wiesner et al.) | ACM Middleware '21 | G1 | Temporal shifting / Carbon-delay heuristic | WattTime & Electricity Maps | Real trace / Synthetic delay models | **8.0** | [`P01 Note`](./notes/P01_Lets_Wait_Awhile.md) |
| **P02** | *Carbon-Aware Computing for Datacenters* (Radovanović et al.) | IEEE TPWRS '23 | G1 | Virtual Capacity Curves (VCC) / Fleet optimization | Google operational carbon metrics | Production Google compute fleet | **7.5** | [`P02 Note`](./notes/P02_Carbon_Aware_Datacenters_Google.md) |
| **P03** | *Carbon Explorer* (Acun et al.) | ACM ASPLOS '23 | G1 | Holistic carbon / Embodied & operational trade-off | National balancing authority traces | Hyperscale datacenter architecture | **7.5** | [`P03 Note`](./notes/P03_Carbon_Explorer.md) |
| **P04** | *Ecovisor* (Souza et al.) | ACM ASPLOS '23 | G1 | Virtual energy system / OS-level virtualization | Real-time WattTime API | Physical server testbed / Linux kernel | **8.0** | [`P04 Note`](./notes/P04_Ecovisor.md) |
| **P05** | *CarbonScaler* (Hanafy et al.) | ACM SIGMETRICS '23 | G1 | Workload elasticity / Predictive scaling | WattTime regional MOER signals | Production Kubernetes workloads | **8.0** | [`P05 Note`](./notes/P05_CarbonScaler.md) |
| **P06** | *GreenCourier* (Chadha et al.) | WoSC@Middleware '23 | G1 | Serverless FaaS spatial routing / Knative | Electricity Maps live intensity | Real Knative/Kubeedge testbed | **7.5** | [`P06 Note`](./notes/P06_GreenCourier.md) |
| **P07** | *Data-driven Algorithm Selection* (Bostandoost et al.) | HotCarbon '24 | G1 | Meta-algorithm selection / Follow-The-Leader | Multi-region ISO carbon traces | Empirical workload profiles | **7.0** | [`P07 Note`](./notes/P07_Algorithm_Selection_FTL.md) |
| **P08** | *Holistic Energy Optimization* (Zhao et al.) | IEEE TSC '25 | G2 | BayesDDQN / IT & cooling co-optimization | Energy/Power models (No grid carbon) | Real cloud datacenter telemetry | **8.0** | [`P08 Note`](./notes/P08_BayesDDQN_Holistic_Energy.md) |
| **P09** | *Workflow Scheduling for Edge-Cloud* (Zhu et al.) | IEEE TCC '24 | G2 | GNN task embedding + PPO / DAG scheduling | Hardware power profiles (No grid carbon) | Scientific workflow traces (Pegasus) | **7.5** | [`P09 Note`](./notes/P09_GNN_PPO_Workflow_EdgeCloud.md) |
| **P10** | *DRAW Resource Allocation* (Chen et al.) | IEEE TCC '23 | G2 | DRAW DQN / Workload-time windows & cost | Server power models (No grid carbon) | Real web service traffic traces | **7.5** | [`P10 Note`](./notes/P10_DRAW_Resource_Allocation.md) |
| **P11** | *Adaptive Resource Allocation* (Chen et al.) | IEEE TPDS '22 | G2 | Actor-Critic with Advantage / Continuous action | Dynamic server power models | Real cloud datacenter workloads | **7.5** | [`P11 Note`](./notes/P11_Actor_Critic_Cloud_Resource_Allocation.md) |
| **P12** | *Adaptive VM Consolidation* (Zeng et al.) | IEEE TPDS '22 | G2 | ADVMC DRL / VM consolidation & host sleep | Server power curves (No grid carbon) | PlanetLab & Google cluster traces | **7.0** | [`P12 Note`](./notes/P12_Adaptive_DRL_VM_Consolidation.md) |
| **P13** | *DeepEE Parameterized DRL* (Ran et al.) | IEEE TSC '23 | G2 | PADQN / Hybrid discrete-continuous IT+cooling | Physical thermal/energy equations | Real production datacenter traces | **7.5** | [`P13 Note`](./notes/P13_PADQN_Data_Center_Energy_Efficiency.md) |
| **P14** | *Federated DRL Cloud-Edge* (Zhu et al.) | IEEE TCC '23 | G2 | Federated DRL / Privacy-preserving scheduling | Power models (No grid carbon) | Synthetic edge-cloud workloads | **7.0** | [`P14 Note`](./notes/P14_Federated_DRL_Cloud_Edge_Scheduling.md) |
| **P15** | *Sustainable AIGC Scheduling* (Zhang et al.) | IEEE GLOBECOM '23 | G3 | Soft Actor-Critic (SAC) / Multi-region migration | Real WattTime MOER traces | Empirical AIGC generative workloads | **8.0** | [`P15 Note`](./notes/P15_Sustainable_AIGC_Scheduling_MARL.md) |
| **P16** | *MADRL Renewable Workflow* (Jayanetti et al.) | IEEE TPDS '24 | G3 | MADRL / Workflow DAG / Decentralized agents | Solar & Wind meteorological traces | Scientific workflow DAGs (Synthetic) | **6.5** | [`P16 Note`](./notes/P16_MADRL_Renewable_Workflow_Scheduling.md) |
| **P17** | *ERLFC Federated Cloud* (Wang et al.) | J. Cloud Comput. '23 | G3 | ERLFC Actor-Critic / Federated scheduling | Regional static emission factors | Synthetic federated tasks | **6.5** | [`P17 Note`](./notes/P17_ERLFC_Federated_Cloud_Scheduling.md) |
| **P18** | *Information-Energy Nexus* (Liu et al.) | Applied Energy '23 | G3 | DRL online scheduling / Energy-carbon nexus | Regional CFR emission factors | Real Google cluster trace | **7.0** | [`P18 Note`](./notes/P18_DRL_Information_Energy_Nexus_Scheduling.md) |
| **P19** | *CFWS Energy & Carbon* (Zhao et al.) | IEEE TSUSC '25 | G3 | DRL / Carbon footprint & electricity cost | Regional DOE CFR factors | Synthesized datacenter workloads | **6.5** | [`P19 Note`](./notes/P19_CFWS_DRL_Energy_Carbon_Scheduling.md) |
| **P20** | *Digital Twin Dual-Time-Scale* (Wu et al.) | IEEE TGCN '26 | G3 | MAPPO / Digital Twin / Dual-Time-Scale | Synthetic carbon emission model | Simulated computing power network | **5.0** | [`P20 Note`](./notes/P20_Digital_Twin_Dual_Time_Scale_Orchestration.md) |
| **P21** | *Multi-Objective DRL Spatiotemporal* (Chen & Chen) | JACS '25 | G3 | MO-PPO / Augmented Tchebycheff scalarization | EIA-930 hourly marginal across 7 ISOs | Real Google & Alibaba traces | **7.5** | [`P21 Note`](./notes/P21_MultiObjective_DRL_Spatiotemporal_Scheduling.md) |
| **P22** | *GAS-MARL Green HPC* (Chen et al.) | FGCS '25 | G3 | Multi-Action DRL / Job select + Green delay | Solar & Wind meteorological traces | Real HPC traces (Curie, Lublin, SDSC) | **7.5** | [`P22 Note`](./notes/P22_GAS_MARL_HPC_Scheduling.md) |
| **P23** | *Intraday Market Decision-Making* (Huang et al.) | IEEE TIA '26 | G3 | PPO / Bi-level market & task migration | Dynamic nodal carbon intensity ($g\text{CO}_2$) | Modified IEEE 5-bus network | **7.0** | [`P23 Note`](./notes/P23_Huang_Intraday_Market_PPO.md) |
| **P24** | *Hierarchical MARL for AI DCs* (Lee et al.) | arXiv '26 | G3 | Hierarchical MAT / Global MAT + Local AIDC | Carbon Emission Flow (CEF) on IEEE 33-node | Calibrated AI workload scaling (LLM/VAE) | **7.0** | [`P24 Note`](./notes/P24_Lee_Hierarchical_MARL_Power_Distribution.md) |
| **P25** | *CarbonCast Multi-Day Forecast* (Maji et al.) | ACM BuildSys '22 | G4 | Two-tier 1D-CNN + LSTM / 96-hr forecast | Dynamic intensity across 6 US/EU ISOs | Historical grid production & weather | **8.0** | [`P25 Note`](./notes/P25_CarbonCast_MultiDay_Forecast.md) |
| **P26** | *DACF Day-Ahead Forecast* (Maji et al.) | ACM e-Energy '22 | G4 | Per-source ANN regression / 24-hr day-ahead | Dynamic intensity across 6 ISO regions | Historical generation & NOAA weather | **7.5** | [`P26 Note`](./notes/P26_Maji_DACF_DayAhead_Forecast.md) |
| **P27** | *Uncertainty-Aware Decarbonization* (Li et al.) | HotCarbon '24 | G4 | Conformal prediction (SPCI) / Uncertainty bounds | Dynamic forecasts from US ISO grids | 20 MW cluster operational profiles | **7.5** | [`P27 Note`](./notes/P27_Li_Uncertainty_Aware_Decarbonization.md) |
| **P28** | *SustainGym Benchmark Suite* (Yeh et al.) | NeurIPS '23 | G5 | Gymnasium benchmark suite / `DatacenterEnv` | Real WattTime MOER traces (2019 vs 2021) | Google Virtual Capacity Curves trace | **8.0** | [`P28 Note`](./notes/P28_SustainGym_Benchmark_Suite.md) |
| **P29** | *Vessim Co-Simulation Testbed* (Wiesner et al.) | HotCarbon '24 | G5 | Mosaik co-simulation / Software-in-the-loop | WattTime 2022 sample slice (CAISO_NORTH) | Physical Jetson TX2 + metered PDU | **7.5** | [`P29 Note`](./notes/P29_Wiesner_Vessim_Testbed.md) |
| **P30** | *Alibaba Microservice Trace* (Luo et al.) | ACM SoCC '21 | G5 | 10B call trace analysis / InfoGraph modeling | Pure compute trace (Zero carbon data) | 10,000+ bare-metal hosts / Kata Containers | **7.0** | [`P30 Note`](./notes/P30_Alibaba_Microservice_Trace_Analysis.md) |

---

## 6. Group-by-Group Literature Synthesis

### 6.1 Group G1: Carbon-Aware Scheduling Without Reinforcement Learning
- **Core Focus:** Establishing the foundational bounds of carbon reduction using deterministic heuristics, mathematical programming (ILP/QP), and operating system abstractions.
- **Key Findings:**
  - *P01 (Let's Wait Awhile):* Proves that simple temporal postponement heuristics using carbon-intensity thresholds achieve **11%–34% carbon reduction** across major cloud regions without hardware modifications.
  - *P02 (Google VCC):* Demonstrates hyperscale fleet coordination, mapping virtual compute capacity curves to regional carbon intensity to shift hundreds of megawatts of non-urgent batch computation globally.
  - *P04 (Ecovisor):* Introduces software-defined energy virtualization, allowing container runtimes to directly query battery state-of-charge and marginal carbon signals via standard Linux APIs.
  - *P05 (CarbonScaler):* Exploits application-level elasticity (horizontal autoscaling) to dynamically adjust container replicas in response to carbon price signals.

### 6.2 Group G2: RL/DRL for Cloud Energy, Cost, and QoS Optimization
- **Core Focus:** Deep reinforcement learning for continuous resource allocation, virtual machine consolidation, and physical cooling infrastructure control.
- **Key Findings:**
  - *P08 (BayesDDQN):* Co-optimizes server compute frequencies and CRAC chiller setpoints, achieving up to **23.8% energy savings** while maintaining server inlet temperatures within ASHRAE thermal compliance envelopes.
  - *P09 (GNN+PPO):* Utilizes Graph Neural Networks to embed directed acyclic graph (DAG) task dependencies, demonstrating that policy-gradient RL can schedule complex dependent workflows with minimal makespan degradation.
  - *P11 & P13 (Actor-Critic / PADQN):* Address hybrid discrete-continuous action spaces, managing continuous CPU power limits alongside discrete host power on/off states.
- **Limitation:** G2 frameworks optimize purely for physical energy (kWh) or electricity billing ($), ignoring that electricity consumed during peaker-plant operation emits substantially more carbon than off-peak renewable power.

### 6.3 Group G3: RL/DRL for Carbon-Aware Cloud Workload Scheduling
- **Core Focus:** Direct optimization of carbon emissions ($\text{tonCO}_2$) via reinforcement learning policies that ingest real-time or forecasted grid emissions telemetry.
- **Key Findings:**
  - *P15 (Sustainable AIGC / Soft Actor-Critic):* Coordinates generative AI workload migration across geo-distributed data centers using multi-agent SAC, achieving **+28.6% system utility** and **+15.6% GPU throughput** under dynamic WattTime MOER traces.
  - *P21 (MO-PPO Spatiotemporal):* Solves the Pareto conflict between carbon minimization, electricity cost, and job completion time (JCT) using multi-objective PPO and augmented Tchebycheff scalarization. Demonstrates that joint spatio-temporal migration reduces carbon by **41.3%** (exceeding temporal-only at 26.1% and spatial-only at 29.4%) with latency overhead bounded within 15%.
  - *P22 (GAS-MARL):* Introduces a decoupled two-action reinforcement learning framework (Action 1 = Job Selection, Action 2 = Timing/Delay Decision) paired with Green-Backfilling, eliminating head-of-line blocking in green HPC clusters.
  - *P24 (Hierarchical MAT):* Implements a Multi-Agent Transformer with autoregressive decoding order (Workload Manager $\rightarrow$ local data centers $\rightarrow$ CRAC cooling), reducing action space cardinality by **$1.85 \times 10^{28}\times$** and achieving **19.2% carbon reduction** on an IEEE 33-node distribution network.

### 6.4 Group G4: Carbon-Intensity Data, Forecasting, and Uncertainty
- **Core Focus:** Generating accurate forward-looking carbon intensity predictions and quantifying forecast errors that degrade scheduling policies.
- **Key Findings:**
  - *P25 (CarbonCast):* Develops the first open-source 96-hour multi-day carbon forecasting framework, using a two-tier hybrid 1D-CNN + LSTM architecture to achieve a **9.96% direct MAPE** across 6 US/EU balancing authorities and outperforming prior methods by 14.38%.
  - *P26 (DACF):* Proves that day-ahead per-source ANN regression driven by numerical weather forecasts achieves a **6.4% mean MAPE** across diverse grids.
  - *P27 (Uncertainty Decarbonization):* Critically proves that naive scheduling on point forecasts causes **5%–14% accidental emissions increases** due to asymmetric forecast errors. Implements Sequentially Predictive Conformal Inference (SPCI) to generate dynamic prediction intervals, guaranteeing true emissions reductions.

### 6.5 Group G5: Standardized Simulators, Testbeds, and Cloud Traces
- **Core Focus:** Reproducible experimental testbeds, Gymnasium environments, and empirical workload drivers.
- **Key Findings:**
  - *P28 (SustainGym):* Establishes the modern Gymnasium benchmark standard for sustainable energy RL, implementing Google's Virtual Capacity Curve in `DatacenterEnv` across multi-year non-stationary distribution shifts (2019 vs. 2021).
  - *P29 (Vessim):* Delivers a modular Mosaik co-simulation testbed connecting physical hardware (NVIDIA Jetson TX2, metered PDUs) and simulated microgrids (PyBaMM batteries, Solcast solar) with decoupled asynchronous buffering to prevent real-time simulation overrun.
  - *P30 (Alibaba Trace Analysis):* Documents production microservice behavior across **10B calls on 10,000+ bare-metal hosts**, demonstrating that microservices are **critically sensitive to CPU contention** (30% host CPU increases latency by 20%) but robust against memory contention.

---

## 7. Research Trends and Evolution (2021–2026)

1. **From Static Heuristics to Deep Multi-Agent RL:** Early literature (P01, P02) relied on fixed carbon-delay thresholds or linear programming. Modern schedulers (P21, P24) leverage Multi-Agent Reinforcement Learning and Transformer-based policies capable of handling dynamic pricing and non-stationary grid emissions.
2. **From Single-Dimension to Joint Spatio-Temporal Migration:** Isolated temporal shifting is constrained by user deadline tolerances; isolated spatial migration is constrained by WAN bandwidth. Joint optimization (P21) captures cross-regional diurnal diversity to achieve substantially higher carbon savings (41.3%).
3. **From Point Forecasts to Uncertainty-Aware Risk Management:** P27 demonstrated that deterministic carbon forecasting leads to policy failure; future carbon schedulers must incorporate conformal prediction intervals or distributional RL to avoid shifting loads into dirty grid spikes.

---

## 8. Common Limitations & Research Gaps

Across the 30 surveyed papers, four critical research gaps persist:
1. **Neglect of Carbon Forecast Uncertainty in RL Rewards:** Existing RL schedulers (P15, P18, P21) ingest point carbon forecasts or historical traces directly into the reward function, assuming perfect or near-perfect predictability. Incorporating conformal prediction intervals (P27) into RL policy optimization remains unaddressed.
2. **Simplified Workload Abstractions in Grid Schedulers:** Papers with high grid fidelity (P23, P24) treat data center workloads as abstract continuous power blocks ($MW$), omitting container launch overheads, DAG dependencies, and microservice tail-latency sensitivity (P30).
3. **Embodied vs. Operational Carbon Myopia:** Most carbon schedulers focus exclusively on operational emissions (Scope 2), ignoring that frequent aggressive workload shifting and rapid battery cycling accelerate hardware degradation and embodied carbon amortization (Scope 3, highlighted in P03).

---

## 9. Conclusion

The systematic literature review confirms that carbon-aware reinforcement learning represents a transformative paradigm for hyperscale cloud decarbonization. By coupling authentic dynamic grid carbon intensity signals (EIA-930, WattTime) with multi-agent reinforcement learning (MO-PPO, MAT) and robust empirical microservice traces (Alibaba 2021), the stage is set for developing our project's production-grade Carbon-Aware RL Cloud Scheduler.

---

## 10. References
All individual citation records, extraction notes, and BibTeX entries are maintained in [`papers_master.csv`](./papers_master.csv), [`references.bib`](./references.bib), and individual files in [`notes/`](./notes/).
