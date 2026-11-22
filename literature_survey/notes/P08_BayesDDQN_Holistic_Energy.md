# P08 — BayesDDQN (Holistic Energy & Cooling Co-Optimization)

**Full citation:** Daming Zhao, Jiantao Zhou, Jidong Zhai, and Keqin Li, "A Reinforcement Learning Based Framework for Holistic Energy Optimization of Sustainable Cloud Data Centers", in *IEEE Transactions on Services Computing*, Vol. 18, No. 1, pp. 15–28, January–February 2025 (published online December 2024).  
**DOI / link:** [https://doi.org/10.1109/TSC.2024.3495495](https://doi.org/10.1109/TSC.2024.3495495)  
**Type:** Journal     **Group:** G2 (RL scheduling for cloud workloads with energy, cost, or performance objectives)  
**Quality score:** 8.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*  

---

## 1. Problem addressed
Modern sustainable cloud data centers are increasingly powered by hybrid energy sources, combining intermittent on-site Renewable Energy Sources (RES, such as solar and wind) with commercial power grids. In such facilities, IT workload management (e.g., virtual machine placement and migration) and cooling infrastructure (e.g., Computer Room Air Conditioning / CRAC) are typically controlled independently. This decoupling causes substantial energy waste, overcooling, and localized thermal hotspots because IT workload consolidation generates concentrated thermal heat that traditional cooling systems cannot dynamically anticipate.  [Source: Sec. 1, pp. 15–16]

## 2. Approach (the core idea)
The authors design a closed-loop holistic energy optimization framework governed by Deep Reinforcement Learning (DRL). The architecture combines a Multi-Task Learning LSTM (MTL-LSTM) network to predict PM inlet temperatures and power states with BayesDDQN—a Double Deep Q-Network augmented by Bayesian Optimization—to handle the complex hybrid action space of discrete VM migrations and continuous CRAC temperature adjustments, incorporating proactive pre-cooling during renewable energy peaks.  [Source: Sec. 3 & 4, pp. 17–22]

## 3. Methodology
- **System role:** Holistic co-optimization framework and DRL scheduler (coordinating IT workload allocation and facility cooling infrastructure).
- **Scheduling decision:** Both IT allocation (where: VM migration across physical machines) and facility cooling control (CRAC supply temperature and airflow setpoints).
- **Workload type:** Multi-tenant cloud Virtual Machine (VM) workloads with dynamic CPU and memory utilization patterns.
- **Dynamic or online?** Yes; online closed-loop MAPE (Monitor-Analyze-Plan-Execute) control loop operating at discrete scheduling epochs.
- **For RL papers:**
  - **Algorithm:** BayesDDQN (Double Deep Q-Network with Bayesian Optimization for hybrid continuous-discrete action spaces) coupled with MTL-LSTM for state feature extraction.
  - **State:** Vector containing: (1) real-time CPU and memory utilization of physical machines (PMs); (2) current and predicted PM inlet and ambient temperatures; (3) available on-site renewable energy generation; and (4) grid electricity price.
  - **Action:** Hybrid action tuple: discrete selection of VM migration pairs (source PM $\to$ destination PM) combined with continuous adjustments to CRAC supply air temperature and fan speeds.
  - **Reward:** Multi-objective reward function formulated to minimize total operational expenditure:
    $$R_t = - \left( w_1 \cdot E_{\text{brown}}(t) + w_2 \cdot P_{\text{cooling}}(t) + w_3 \cdot \text{Cost}_{\text{grid}}(t) + \lambda \cdot \text{Penalty}_{\text{hotspot}}(t) \right)$$
    where penalties grow exponentially if any PM inlet temperature exceeds the safety threshold ($T_{\text{inlet}} > 25^\circ\text{C}$).
  - **Training setup:** Trained over 2,000 simulation episodes using experience replay memory (capacity 10,000 transitions), target network update frequency of 100 steps, and Bayesian Optimization for hyperparameter exploration.
- **Carbon / energy data source and region:** Empirical solar and wind renewable generation profiles combined with time-of-use industrial electricity pricing data.
- **Workload trace / dataset:** Real-world cloud VM workload traces from Google cluster data and PlanetLab VM traces.
- **Simulator or real system:** Custom thermal-aware cloud data center simulation testbed incorporating computational fluid dynamics (CFD) heat recirculation matrices and server power models.
- **Baselines compared:** 
  - **Heuristic Baseline:** First-Fit VM allocation with static CRAC cooling setpoints.
  - **Standalone DQN:** Standard Deep Q-Network without Bayesian optimization or temperature prediction.
  - **DVFS-Heuristic:** Dynamic Voltage and Frequency Scaling with reactive threshold-based cooling.  
[Source: Sec. 4 & 5, pp. 20–26]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Holistic energy consumption reduction | 2.83% relative reduction in total data center energy | Heuristic baseline controller | Sec. 5.3, Table 3, p. 25 |
| Brown energy reduction | 4.74% relative reduction in non-renewable grid energy | Heuristic baseline controller | Sec. 5.3, Table 3, p. 25 |
| Cooling energy reduction | 13.48% relative reduction in CRAC cooling energy | Heuristic baseline controller | Sec. 5.3, Table 3, p. 25 |
| Thermal hotspot occurrences | Near-zero violations ($< 0.1\%$ of total operational hours) | Standalone DQN baseline ($> 4.2\%$ violations) | Sec. 5.4, Fig. 7, p. 26 |
| Inlet temperature prediction accuracy (MTL-LSTM) | RMSE $< 0.42^\circ\text{C}$ in multi-PM temperature estimation | Standalone LSTM ($0.78^\circ\text{C}$) | Sec. 5.2, Table 2, p. 24 |
| Convergence stability | Stable policy convergence within 800 episodes | Standalone DQN ($> 1,500$ episodes with high variance) | Sec. 5.3, Fig. 5, p. 24 |

## 5. Gap
- **Gap stated by the authors:**
  "The Bayesian optimization process introduces noticeable computational overhead during the action selection phase, making high-frequency sub-second re-scheduling difficult... In addition, our model assumes that renewable energy can be consumed locally or buffered, but does not model dynamic grid-level carbon emission intensity factors or multi-datacenter geographic migration."  [Source: Sec. 6, p. 27]
- **Gap we observe:**
  The objective function targets brown energy and electricity cost reduction rather than explicit real-time grid carbon intensity signals (such as MOER). While it coordinates IT and cooling within a single facility, it does not explore temporal shifting of delay-tolerant batch jobs or multi-datacenter spatial shifting.

## 6. Relevance to our project
Demonstrates how DRL (specifically Double DQN with Bayesian optimization) can successfully resolve complex multi-objective trade-offs between IT computing workloads and physical facility energy. The pre-cooling and thermal safety formulations provide valuable mechanisms for our scheduler when modeling server hardware constraints.