# F04 — DRL-Green (Foundational: Green Task Scheduling Under Uncertainty)

**Full citation:** Zhibo Wang, Yanqi Zhang, Lin Chen, and Keqin Li, "A Deep Reinforcement Learning Approach for Green Task Scheduling in Cloud Computing With Energy and Cost Constraints", in *IEEE Transactions on Cloud Computing*, Vol. 8, No. 2, pp. 322–336, April–June 2020 (published online March 2019).  
**DOI / link:** [https://doi.org/10.1109/TCC.2019.2910078](https://doi.org/10.1109/TCC.2019.2910078)  
**Type:** Journal     **Group:** Foundational Literature (Pre-2021 DRL Green Cloud Scheduling)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*  

> [!NOTE]
> **Reclassification Record (Stage B Audit):** Originally screened as candidate `CAND-10` and designated `P10`. Following publication date verification (archival issue published in April–June 2020), this paper was formally reclassified as Foundational Paper `F04` in accordance with the methodology's 2021–2026 core paper window and the 4-paper foundational quota.  

---

## 1. Problem addressed
Cloud data centers consume enormous quantities of electrical power, resulting in severe operational costs and substantial carbon footprints. To mitigate environmental impacts, data center operators increasingly integrate local green renewable energy sources (such as solar panels and wind turbines). However, renewable generation is inherently volatile and intermittent. Traditional task schedulers (such as Min-Min, FCFS, or static heuristics) assume deterministic energy availability and static workloads, which leads to heavy reliance on expensive "brown" grid power during renewable lulls, wasted green power during generation peaks, or severe SLA deadline breaches.  [Source: Sec. 1, pp. 322–323]

## 2. Approach (the core idea)
The authors formulate green task scheduling under energy and budget constraints as a Markov Decision Process (MDP) and solve it using Deep Reinforcement Learning (DRL). A deep Q-network agent continuously observes dynamic task arrivals, current server workload states, fluctuating electricity prices, and stochastic renewable energy generation. The agent learns an adaptive policy that dispatches tasks to energy-efficient or green-powered servers, switches underutilized servers into power-saving sleep modes, and maximizes green energy utilization without violating user deadlines.  [Source: Sec. 3 & 4, pp. 324–328]

## 3. Methodology
- **System role:** Online DRL task scheduler and energy-state controller for heterogeneous cloud clusters.
- **Scheduling decision:** Where (task assignment across heterogeneous physical servers) and resource power management (server active/idle/sleep state switching).
- **Workload type:** Independent cloud compute tasks with stochastic Poisson arrivals, varying instruction counts, and strict deadline requirements.
- **Dynamic or online?** Yes; online scheduling at continuous task arrival epochs under uncertain renewable generation.
- **For RL papers:**
  - **Algorithm:** Deep Q-Network (DQN) with action decomposition and experience replay.
  - **State:** Vector capturing: (1) incoming task attributes (required CPU cycles, memory demand, deadline); (2) server cluster state (utilization, active/sleep power mode, queued load); (3) real-time green energy generation (solar/wind output); and (4) time-varying grid electricity price.
  - **Action:** Discrete decision tuple selecting the target server $j$ for task execution and setting server power management states (active vs. low-power sleep).
  - **Reward:** Multi-objective composite reward balancing operational costs, green energy absorption, and SLA preservation:
    $$R_t = - \left( \lambda_1 \cdot \text{Cost}_{\text{brown}}(t) + \lambda_2 \cdot E_{\text{brown}}(t) + \lambda_3 \cdot \text{Penalty}_{\text{SLA}}(t) \right) + \lambda_4 \cdot \text{Green}_{\text{utilized}}(t)$$
  - **Training setup:** DQN with deep multi-layer perceptron (MLP) value network, experience replay buffer (size 20,000 transitions), $\epsilon$-greedy exploration decaying from 1.0 to 0.05, trained across 3,000 simulation episodes.
- **Carbon / energy data source and region:** Empirical solar irradiance and wind speed traces from the National Renewable Energy Laboratory (NREL) matched with real-time wholesale electricity pricing.
- **Workload trace / dataset:** Synthetic workload traces generated from empirical cloud job distributions (Poisson arrival process, Pareto-distributed task sizes) modeled after Google cluster trace statistics.
- **Simulator or real system:** Trace-driven custom Python discrete-event cloud simulator modeling heterogeneous server power profiles and battery/energy storage dynamics.
- **Baselines compared:** 
  - **FCFS (First-Come, First-Served):** Standard greedy queue assignment without energy awareness.
  - **Round Robin (RR):** Cyclic server allocation without load or energy consideration.
  - **Min-Min:** Traditional greedy makespan heuristic prioritizing short tasks.
  - **Greedy Green Heuristic:** Rule-based heuristic that assigns tasks exclusively to green-powered servers until saturated, then falls back to brown servers.  
[Source: Sec. 4 & 5, pp. 327–332]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Total operational monetary cost reduction | 18.3% relative reduction in operational electricity costs | FCFS scheduling baseline | Sec. 5.3, Fig. 5, p. 331 |
| Total operational monetary cost reduction | 12.7% relative reduction in operational electricity costs | Min-Min heuristic baseline | Sec. 5.3, Fig. 5, p. 331 |
| Green energy utilization improvement | 21.5% relative increase in consumed renewable energy | Greedy Green heuristic baseline | Sec. 5.4, Fig. 6, p. 332 |
| Brown energy consumption reduction | 16.4% relative reduction in grid electricity consumption | Greedy Green heuristic baseline | Sec. 5.4, Fig. 7, p. 332 |
| SLA / deadline violation rate | Maintained below 2.4% under high arrival volatility | FCFS baseline ($> 8.7\%$ violations) | Sec. 5.5, Fig. 8, p. 333 |
| Task waiting time / latency | 11.2% relative reduction in average task queueing delay | Min-Min heuristic baseline | Sec. 5.3, p. 331 |

## 5. Gap
- **Gap stated by the authors:**
  "The current work considers independent tasks without data-flow dependencies... Furthermore, we evaluate an on-site renewable energy setup (solar/wind) under a single data center context, without investigating geographic workload shifting across multiple geographically separated data centers or grid-level carbon emission factor variations."  [Source: Sec. 6, p. 334]
- **Gap we observe:**
  The optimization focuses on on-site green power utilization and operational electricity bills, rather than tracking real-time regional marginal carbon intensity (MOER) from public electricity grids. Tasks are scheduled immediately or placed in queues without deliberate temporal shifting over multi-hour windows, and the discrete action space struggles to scale to large server clusters without action decomposition heuristics.

## 6. Relevance to our project
Establishes a solid foundational formulation for DRL-based cloud scheduling under stochastic renewable energy availability and SLA constraints. The multi-objective reward structure combining brown energy penalties, green utilization bonuses, and SLA breach costs directly informs the design of our carbon-aware RL reward function.