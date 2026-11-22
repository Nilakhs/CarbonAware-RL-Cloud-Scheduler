# Project Objectives and Research Questions

## 1. Project Objectives

### 1.1 Primary Objective
To design, investigate, and systematically evaluate an online **Carbon-Aware Reinforcement Learning (RL) Scheduler** for dynamic cloud workloads that achieves measurable reductions in operational carbon emissions while strictly preserving user-defined Service Level Agreement (SLA) deadlines.

### 1.2 Secondary Objectives
1. **Systematic Literature Review (SLR):** Execute an evidence-based literature survey following the Kitchenham & Charters (2007) and PRISMA 2020 protocols across 30 core peer-reviewed papers (2021–2026), 4 foundational papers, and 3 comprehensive surveys.
2. **Taxonomic Grouping & Gap Identification:** Classify surveyed literature into five distinct groups (G1: Non-RL Carbon Schedulers, G2: RL for Energy/Cost, G3: RL for Carbon-Aware Schedulers, G4: Carbon Data & Forecasting, G5: Simulators & Traces) to pinpoint realistic research gaps feasible for a single-semester course project.
3. **Markov Decision Process (MDP) Modeling:** Formalize the dynamic cloud workload scheduling problem under stochastic job arrivals, multi-region grid carbon fluctuations, and deadline constraints as an MDP or POMDP.
4. **Reward Shaping for Multi-Objective Trade-Offs:** Develop and evaluate a balanced reward formulation that penalizes operational carbon emissions and SLA deadline infractions while managing migration latency and computational overhead.
5. **Simulation-Based Empirical Validation:** Benchmark the proposed RL scheduler against state-of-the-art heuristic and carbon-agnostic baselines using trace-driven simulation testbeds (e.g., Vessim, CloudSim Plus) with real-world trace inputs (Google/Alibaba cluster traces) and empirical carbon intensity data (Electricity Maps / WattTime / CAISO / ENTSO-E).

---

## 2. Research Questions (RQs)
The research questions governing this project are directly grounded in the questions formulated in our SLR methodology (`docs/research_methodology.md`, Sec. 9.3):

* **RQ1 (State of the Art & Trends):**  
  *How have scheduling methodologies evolved across non-RL heuristics (G1), energy-centric RL (G2), and carbon-aware RL (G3) between 2021 and 2026, and what representational paradigms dominate modern cloud resource managers?*

* **RQ2 (Comparative Efficacy & Trade-Offs):**  
  *What carbon emission reductions (% relative reduction) are achievable via temporal workload shifting versus spatial workload shifting, and what are the corresponding trade-offs in job makespan, SLA deadline violations, and queuing delay?*

* **RQ3 (Handling Environmental Uncertainty):**  
  *How effectively do existing carbon-aware RL schedulers handle the dual stochasticity of dynamic, unanticipated job arrivals and volatile, erroneous grid carbon intensity forecasts?*

* **RQ4 (Multi-Objective SLA Preservation):**  
  *How can reinforcement learning reward functions be formulated to prevent policy degradation under extreme renewable lulls without causing catastrophic SLA deadline breaches or cluster queue overflows?*

* **RQ5 (Feasible Research Scope):**  
  *Which substantiated research gap identified in the literature represents a novel, technically viable contribution that can be implemented and empirically evaluated within a semester-long course project?*

---

## 3. Scope Boundaries and Non-Goals
To ensure feasibility within academic course constraints:
- **In Scope:**
  - Discrete-time RL agent formulations (DQN, Double DQN, PPO, or Actor-Critic).
  - Open-source, trace-driven simulation frameworks with reproducible benchmark traces.
  - Delay-tolerant batch compute jobs, parameter-tuning jobs, and flexible cloud service requests.
- **Out of Scope (Non-Goals):**
  - Physical data center facility design (HVAC, chiller loops, liquid immersion cooling hardware).
  - Real-world production cluster deployments requiring root hypervisor or kernel modifications.
  - Interactive microsecond-critical RPC transactions (e.g., live web search queries or financial transaction processing) that admit zero temporal deferral.
