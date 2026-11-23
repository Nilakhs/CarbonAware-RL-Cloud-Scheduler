# P20 — Digital Twin-Driven Dual-Time-Scale Orchestration for Synergistic Computing Power and Electric Power Systems

**Full citation:** Shuang Wu, Renchao Xie, Qinqin Tang, Hui Zhao, Wei Chen, Pasika Ranaweera, Madhusanka Liyanage, and Tao Huang, "Digital Twin-Driven Dual-Time-Scale Orchestration for Synergistic Computing Power and Electric Power Systems", in *IEEE Transactions on Green Communications and Networking*, Vol. 10, pp. 2789–2803, 2026.
**DOI / link:** [https://doi.org/10.1109/TGCN.2026.3687635](https://doi.org/10.1109/TGCN.2026.3687635) (IEEE Xplore Document: `11494859`)
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)
**Quality score:** 5.0 / 8 (Strict G3 Rubric: 4.5 / 8)
*(Q1: 1.0, Q2: 0.5, Q3: 0.0, Q4: 0.5, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 0.5)*
*(Note on score reconciliation and primary source audit: Reconciled following Phase 2.5 Stage B primary-source verification. **Full-Text Accessibility Status:** The archival publisher full text is **STRICTLY PAYWALLED** behind IEEE Xplore subscription. It is not open access; ResearchGate provides only a "Request full-text" option; and no open preprint exists on arXiv, TechRxiv, or author institutional websites. Verified facts below are derived strictly from official publisher metadata, CrossRef API reference indexing [36 canonical references], and the peer-reviewed abstract. Unverified elements due to paywall boundaries are explicitly disclosed.
- **Note on Q2 (0.5):** Scored 0.5 [Partly] because while the high-level architecture, hierarchical coupling, and PD-MAPPO algorithm are fully defined in publisher metadata and abstract, internal mathematical derivations and hyperparameter tables cannot be independently inspected behind the IEEE paywall.
- **Note on Q3 (0.0 strict / 0.5 lenient):** Scored 0.0 under strict G3 rubric rules because G3 explicitly requires real dynamic grid carbon-intensity time-series data [$g\text{CO}_2/\text{kWh}$ from Electricity Maps, WattTime, or regional ISOs]. The paper evaluates performance using empirical meteorological solar irradiance datasets [NOAA SURFRAD, Augustine et al., Refs. 32–33] to simulate renewable generation, rather than dynamic grid carbon-intensity API signals. Under a lenient proxy interpretation crediting empirical weather traces, Q3 is at most 0.5 [yielding 5.0/8].
- **Note on Q4 (0.5):** Scored 0.5 [Partly] because while the evaluation models computing workloads with latency/throughput QoS constraints in large-scale simulated deployments, the paper's 36 canonical references do not cite the Alibaba or Google cluster trace repositories, and the specific workload trace origin is unverified behind the paywall.
- **Note on Q7 (0.5):** Scored 0.5 because the digital-twin simulator models and source code are not hosted on a public open repository [GitHub/Zenodo].
- **Note on Q8 (0.5):** Scored 0.5 [Partly] because the abstract outlines trade-offs between computational throughput, latency, and carbon emissions under QoS constraints; however, specific limitations and future directions in Section VI cannot be independently inspected from paywalled text).*

---

## 1. Problem addressed
The deep integration of computing power networks (data centers / digital infrastructure) and modern electric power systems (smart grids) offers a vital pathway to manage escalating computational energy consumption and absorb intermittent renewable energy. However, synergistic orchestration faces two fundamental challenges:
1. **Temporal Heterogeneity:** Physical electric power systems operate with relatively slow physical dynamics (macro-level energy planning, generator dispatch, power-flow limits), whereas computing power networks handle volatile, real-time workload arrivals requiring rapid scheduling decisions (minute-to-second scale).
2. **Dual Stochastic Uncertainties:** Schedulers must simultaneously navigate unpredictable fluctuations in renewable energy generation (solar/wind intermittency) and stochastic cloud computing task arrivals. Uncoordinated operation causes power-flow violations, high carbon emissions from thermal generation, and degraded Quality of Service (QoS).  [Source: IEEE TGCN Abstract, 2026; CrossRef Metadata]

## 2. Approach (the core idea)
The authors establish a **Digital Twin (DT)-driven hierarchical architecture** for synergistic computing power and electric power systems:
- **High-Fidelity Virtual Mappings:** Employs digital twin technology to capture, analyze, and predict the coupled dynamics of both computing networks and power grids, providing safe state tracking and exploration.
- **Dual Time-Scale Interaction Mechanism:** Coordinates large time-scale energy planning (macro-level power allocation and baseline energy scheduling) to guide small time-scale adaptive task scheduling (real-time workload allocation and renewable tracking).
- **Optimization Formulation:** Formulates a joint optimization problem that maximizes carbon emission efficiency, capturing the multi-objective trade-off among computational throughput, latency, and carbon emissions under strict QoS constraints.
- **Algorithmic Solution (PD-MAPPO):** Solves the dual-time-scale control problem via **Prediction-Augmented Dual Time-Scale Multi-Agent Proximal Policy Optimization (PD-MAPPO)**.  [Source: IEEE TGCN Abstract, 2026]

## 3. Methodology
- **System role:** Hierarchical dual-time-scale coordinator managing coupled electric power grid dispatch and distributed cloud computing task allocation.
- **Scheduling decision:** Spatio-temporal multi-level decisions:
  1. *Large Time-Scale:* Macro energy planning and power generation coordination.
  2. *Small Time-Scale:* Adaptive computing task scheduling and real-time workload routing.
- **Workload type:** Computing tasks characterized by computational throughput demands, execution latency bounds, and QoS constraints.
- **Dynamic or online?** Yes; dual-time-scale online dynamic coordination where large-scale planning guides small-scale adaptive task scheduling.
- **For RL papers:**
  - **Algorithm:** **PD-MAPPO** (Prediction-Augmented Dual Time-Scale Multi-Agent Proximal Policy Optimization) using multi-agent reinforcement learning.
  - **State, Action, Reward, and Neural Architecture:** The framework optimizes carbon emission efficiency against latency and throughput under QoS constraints. Detailed mathematical equations and tensor dimensions are presented in Sections III–IV of the paper, which are paywalled behind IEEE Xplore.
  - **Prediction-Augmented Module:** Integrates predictive modeling of renewable generation and workload dynamics (drawing upon TCN/Transformer forecasting foundations cited in Refs. 11, 13, 19).
- **Carbon / energy data source and region:**
  - *Renewable Meteorological Datasets:* Real-world meteorological datasets, specifically utilizing NOAA's **SURFRAD** (National Surface Radiation Budget Network, Augustine et al., cited via canonical Refs. 32 and 33) for empirical solar irradiance time series.
  - *Carbon Modeling:* Carbon emissions are optimized within the power-compute cyber-physical framework (modeled via power generation dispatch / thermal generation offsets).
  - *(Paywall & Rubric Disclosure: The case study does NOT ingest real-time dynamic grid carbon-intensity API data [such as Electricity Maps or WattTime]. It models renewable absorption and power dispatch driven by empirical meteorological data).*
- **Workload trace / dataset:** Evaluated on simulated large-scale computing deployments with QoS constraints. *(Note: Specific workload trace repository is unverified from paywalled text; Alibaba cluster trace is not among the paper's 36 canonical references).*
- **Simulator or real system:** Trace-driven cyber-physical simulation platform integrating digital twin models of power and computing systems. Evaluated in simulation; not deployed on physical hardware.
- **Baselines compared:** Evaluated against multiple comparative baselines, including "the best-performing baseline in large-scale deployments" (as verified in Abstract), alongside established multi-agent and green computing scheduling literature cited in references (e.g., Jayanetti et al., TPDS 2024 [Ref. 9]; Yuan et al., TASE 2019 [Ref. 29]; Zhao et al., JPDC 2022 [Ref. 30]; Liu et al., TWC 2024 [Ref. 36]).

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon emissions reduction | **4.6% reduction** in carbon emissions | Best-performing baseline in large-scale deployments | IEEE TGCN Abstract, p. 2789 |
| Average service latency reduction | **3.3% reduction** in average service latency | Best-performing baseline in large-scale deployments | IEEE TGCN Abstract, p. 2789 |
| Carbon emission efficiency | Maximized under Quality of Service (QoS) constraints | Baseline schedulers | IEEE TGCN Abstract, p. 2789 |
| Multi-timescale robustness | Verified effective and robust across dual time scales | Comparative baselines in large-scale deployments | IEEE TGCN Abstract, p. 2789 |

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Trade-off Between Throughput, Latency, and Carbon (Abstract, p. 2789):* The authors explicitly state that optimizing carbon emission efficiency requires balancing the complex trade-off among computational throughput, latency, and carbon emissions under strict QoS constraints.
  - *Temporal Synchronization Challenge (Abstract, p. 2789):* Reconciling the slow physical inertia of power systems with real-time computing demands requires coordinating macro-level energy guidance without incurring excessive synchronization drift or latency violations.
  - *(Auditor Disclosure on Section VI Future Work: In previous informal drafts, specific future research directions—such as PINN [Physics-Informed Neural Network] integration, extreme-weather forecasting, and dynamic market bidding—were claimed. A rigorous audit reveals that these claims are **UNVERIFIED and were inferred without primary text verification**, as Section VI is paywalled and the paper's 36 canonical references contain zero works on PINNs, market bidding, or extreme-weather disasters. Honest academic reporting requires explicitly acknowledging that Section VI cannot be independently verified from open-access sources).*
- **Gap we observe:**
  - *Paywalled Implementation & Reproducibility Barrier:* The full text, internal mathematical formulations, and simulation artifacts are paywalled behind IEEE Xplore, with no open-access preprint or public code repository (GitHub/Zenodo), hindering independent experimental validation.
  - *Lack of Dynamic Real-Time Grid Carbon API Data:* Carbon reduction is achieved through simulated power-flow dispatch and renewable absorption based on meteorological irradiance data (SURFRAD), rather than integrating live third-party marginal grid carbon-intensity signals ($g\text{CO}_2/\text{kWh}$ from Electricity Maps or WattTime).
  - *Simulation-Only Validation:* The digital-twin dual-time-scale architecture is validated purely in software simulation without deployment on physical distribution grids or bare-metal Kubernetes server clusters.
  - *Digital Twin Telemetry & Synchronization Latency:* In real-world multi-datacenter grids, network latency and synchronization jitter between physical substations/servers and digital twin replicas could induce control divergence.

## 6. Relevance to our project
P20 provides conceptual and architectural insights for Group G3 (RL / DRL for carbon-aware cloud workload scheduling):
1. **Dual-Time-Scale Coordination Paradigm:** Demonstrates the conceptual necessity of decoupling slow physical energy dynamics from fast computing task dynamics to achieve stable, carbon-aware scheduling.
2. **Digital Twin for Risk-Free Exploration:** Highlights how virtual digital twin models allow reinforcement learning agents (PD-MAPPO) to explore state transitions safely without risking physical grid or SLA violations.
3. **Addressing the Closed-Source and Data Gap:** Because P20 is closed-source, paywalled, and reliant on meteorological proxies rather than live grid carbon intensity APIs, our project directly fills these gaps by delivering an open-source, fully reproducible scheduler integrated with dynamic carbon intensity time series.
