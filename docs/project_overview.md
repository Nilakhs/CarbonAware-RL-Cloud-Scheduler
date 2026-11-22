# Project Overview: Carbon-Aware Reinforcement Learning Scheduler for Dynamic Cloud Workloads

## 1. Executive Summary
This academic research project investigates how **Reinforcement Learning (RL)** and **Deep Reinforcement Learning (DRL)** can be formulated and applied to schedule dynamic cloud computing workloads under time-varying, regionally heterogeneous grid carbon intensity signals. As global cloud computing infrastructures expand, their electricity consumption and associated greenhouse gas emissions have become major environmental challenges. While traditional cloud workload schedulers optimize primarily for operational cost, resource utilization, and Service Level Agreement (SLA) deadlines, carbon-aware schedulers dynamically modulate execution timing (**temporal shifting**) and execution location (**spatial shifting**) to maximize clean, low-carbon electricity utilization without breaching contractual performance bounds.

This repository hosts the **Systematic Literature Review (SLR)**, architectural scoping, empirical synthesis, and subsequent experimental framework developed as part of our college Cloud Computing course project.

---

## 2. Motivation and Background

### 2.1 The Cloud Decarbonization Imperative
Hyperscale data centers account for roughly 1% to 1.5% of worldwide electricity consumption, a figure accelerating with the proliferation of foundation AI model training, real-time inferencing, and large-scale data analytics. The environmental impact of this electricity consumption depends directly on the **grid carbon intensity**—the mass of equivalent carbon dioxide emitted per kilowatt-hour of electricity generated ($gCO_2/kWh$).

### 2.2 Grid Carbon Dynamics: Two Dimensions of Variance
Grid carbon intensity varies across two fundamental dimensions:
1. **Temporal Fluctuation:** Due to the diurnal cycles of solar irradiance and the intermittency of wind power, carbon intensity within a single electricity grid region fluctuates substantially throughout a 24-hour cycle. Peaker plants (often coal- or natural gas-fired) are dispatched during peak demand intervals, driving carbon spikes, while midday solar surges or nocturnal wind surplus yield low-carbon "valleys."
2. **Spatial Heterogeneity:** Different geographical regions feature distinct power generation mixes. For example, grids dominated by nuclear or hydroelectric energy (e.g., France, Quebec, or Ontario) maintain consistently low average carbon intensities ($< 50\text{ }gCO_2/kWh$), whereas fossil-heavy grids (e.g., portions of the US Midwest, Australia, or Poland) often exceed $400\text{ }gCO_2/kWh$.

### 2.3 Limitations of Conventional and Static Schedulers
Conventional cloud resource orchestrators (e.g., Kubernetes, Apache Mesos, OpenStack) are completely carbon-agnostic, dispatching tasks immediately upon arrival or consolidating virtual machines purely to minimize physical server count or network communication latency. 

Recent research has explored static heuristics (such as threshold-based waiting or fixed nighttime dispatching) and mathematical programming (such as Mixed-Integer Linear Programming / MILP). However, these non-learning approaches suffer from severe limitations:
- **Heuristic brittleness:** Schedulers tuned for one region fail when deployed to grids with different diurnal profiles.
- **Forecast vulnerability:** Static rules fail or breach deadlines when grid forecasts contain typical prediction errors ($10\%$–$30\%$).
- **Dynamic arrival mismatch:** Static optimizers require global knowledge or solve offline formulations that cannot scale to stochastic, sub-second online task arrivals.

---

## 3. The Reinforcement Learning Opportunity
Reinforcement Learning offers a principled framework for sequential decision-making under uncertainty:
- **Markov Decision Process (MDP):** The scheduler acts as an autonomous agent interacting with a stochastic cloud environment, observing arriving job profiles, server queue states, and dynamic carbon signals.
- **Adaptive Multi-Objective Balancing:** The agent learns a closed-loop policy that balances multiple competing objectives—minimizing operational carbon footprints while preserving task deadlines, minimizing migration latencies, and controlling monetary energy costs.
- **Continuous Adaptation:** Unlike static heuristics, an RL agent can adapt to non-stationary grid conditions and stochastic workload arrival distributions without manual hyperparameter retuning.

---

## 4. Current Status and Project Phases

| Phase | Description | Current Status | Notes & Evidence |
|:---:|:---|:---:|:---|
| **Phase 1** | Project Setup & SLR Protocol Definition | **COMPLETED** | Protocol defined in [`research_methodology.md`](research_methodology.md) |
| **Phase 2** | Systematic Discovery & Verification Audit | **COMPLETED** | Verified in [`../literature_survey/Audit_Report.md`](../literature_survey/Audit_Report.md) |
| **Phase 3** | Data Extraction: Group G1 (Non-RL Carbon Schedulers) | **COMPLETED** | Notes P01–P07 extracted; G1 synthesis complete |
| **Phase 4** | Data Extraction: Group G2 (RL for Energy/Cost/QoS) | **IN PROGRESS** | Notes P08–P09 extracted; P10 candidate replacement pending review |
| **Phase 5** | Data Extraction: Group G3 (RL for Carbon-Aware Schedulers) | **PLANNED** | 10 core papers (P15–P24) targeted |
| **Phase 6** | Data Extraction: Groups G4 & G5 (Data, Forecasting, Simulators) | **PLANNED** | 6 core papers (P25–P30) targeted |
| **Phase 7** | Cross-Group Synthesis & Candidate Gap Substantiation | **PLANNED** | Comprehensive comparison tables and survey report |
| **Phase 8** | Scheduler Formulation & Simulation Implementation | **PLANNED** | Testbed selection (e.g. Vessim / CloudSim) and evaluation |

> [!IMPORTANT]
> This project is currently in the **Systematic Literature Review and Research Scoping Phase**. No simulator, agent implementation, or empirical experiment is claimed as completed. All technical frameworks described beyond the literature survey represent planned research directions.
