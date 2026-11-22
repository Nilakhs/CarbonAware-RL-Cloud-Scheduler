# P13 — DeepEE: Parameterized Deep Reinforcement Learning for Data Center Energy Efficiency

**Full citation:** Yong-Yi Ran, Han Hu, Yong-Gang Wen, and Xiaoxia Zhou, "Optimizing Energy Efficiency for Data Center via Parameterized Deep Reinforcement Learning", in *IEEE Transactions on Services Computing*, Vol. 16, No. 2, pp. 1162–1174, March–April 2023 (published online June 2022).  
**DOI / link:** [https://doi.org/10.1109/TSC.2022.3184835](https://doi.org/10.1109/TSC.2022.3184835)  
**Type:** Journal     **Group:** G2 (RL scheduling for cloud workloads with energy, cost, or performance objectives)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*  

---

## 1. Problem addressed
Modern data centers consume massive amounts of electrical power across two interdependent subsystems: IT computing servers and facility cooling infrastructure (CRAC units and chillers). Traditional data center management operates these subsystems in isolation: IT workloads are scheduled without thermal feedback, while cooling units reactively maintain conservative, overcooled static setpoints. This decoupled control causes severe energy waste and localized server thermal hotspots. However, joint optimization poses a fundamental **hybrid action space** challenge: IT task dispatching requires discrete selections (which physical host/rack receives a job), whereas cooling control requires continuous parameters (adjusting chilled water temperatures, supply air temperatures, and fan speeds). Furthermore, IT workloads fluctuate at millisecond-to-second scales, whereas thermal cooling loops exhibit inertia requiring minutes to stabilize.  [Source: Sec. 1, pp. 1162–1163]

## 2. Approach (the core idea)
The authors present **DeepEE**, an end-to-end data center energy optimization framework powered by a **Parameterized Action-space based Deep Q-Network (PADQN)**. PADQN natively models the hybrid action space by pairing each discrete task allocation choice with a continuous vector of cooling setpoint parameters. To bridge the operational time-scale divergence between rapid IT workload shifts and slow thermal dynamics, DeepEE incorporates a dynamic time factor mechanism (**PADQN-D**) that enables multi-time-scale hierarchical control.  [Source: Sec. 3 & 4, pp. 1164–1169]

## 3. Methodology
- **System role:** Joint IT workload dispatcher and data center cooling controller.
- **Scheduling decision:** Joint discrete task mapping (which server executes the job) and continuous cooling regulation (CRAC supply temperature and airflow setpoints).
- **Workload type:** Multi-tenant heterogeneous batch jobs and interactive cloud service requests.
- **Dynamic or online?** Yes; online two-time-scale closed-loop control system.
- **For RL papers:**
  - **Algorithm:** Parameterized Action-space Deep Q-Network (PADQN) augmented with dynamic time factor control (PADQN-D).
  - **State ($S_t$):** State vector capturing: (1) server CPU and memory utilization levels; (2) task waiting queue backlogs; (3) rack inlet temperatures and server chassis thermal profiles; (4) outdoor ambient temperature; and (5) current CRAC operational parameters.  [Source: Sec. 4.1, pp. 1165–1166]
  - **Action ($A_t$):** Parameterized action tuple $(k, x_k)$, where $k \in \{1, 2, \dots, K\}$ denotes the discrete server assignment action, and $x_k \in \mathcal{X}_k$ is a continuous parameter vector specifying CRAC fan airflow rate and chilled water temperature.  [Source: Sec. 4.2, p. 1166]
  - **Reward ($R_t$):** Multi-objective reward function formulated to minimize total data center power consumption while penalizing thermal safety violations and job response delays:
    $$R_t = - \left( P_{\text{IT}}(t) + P_{\text{cooling}}(t) + \alpha \cdot \text{Penalty}_{\text{temp}}(t) + \beta \cdot \text{Delay}(t) \right)$$
    where $\text{Penalty}_{\text{temp}}$ penalizes rack inlet temperatures exceeding the $25^\circ\text{C}$ safety threshold, and $\alpha, \beta$ are scaling weights.  [Source: Sec. 4.3, p. 1167]
  - **Training setup:** Dual-network architecture combining an action-value Q-network and a continuous parameter actor network, optimized via deterministic policy gradients and experience replay (buffer capacity 10,000 steps).  [Source: Sec. 4.4, pp. 1167–1168]
- **Carbon / energy data source and region:** Server power calculated via SPECpower curves; cooling power modeled using thermodynamic heat exchange models. Grid carbon intensity signals ($g\text{CO}_2/\text{kWh}$) are **not** modeled.  [Source: Sec. 5.1, pp. 1169–1170]
- **Workload trace / dataset:** Real-world workload trace logs from **Google Cluster Data** and **Alibaba Cloud traces** representing heterogeneous task arrival patterns.  [Source: Sec. 5.1, p. 1170]
- **Simulator or real system:** **Trace-driven thermodynamic cloud data center simulation testbed** validated against empirical CFD (Computational Fluid Dynamics) thermal recirculation measurements. It is **not** a physical bare-metal cluster deployment.  [Source: Sec. 5.1, pp. 1169–1170]
- **Baselines compared:**
  - *Siloed Heuristic Baselines:* Round-Robin, First Fit, and Best Fit task scheduling with fixed static CRAC cooling.
  - *Siloed DRL Baselines:* Standard DQN with discretized cooling actions and DeepRM.
  - *Joint Continuous Baselines:* DDPG with continuous-relaxed task allocation.  [Source: Sec. 5.2, p. 1170]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Total energy consumption | 15.2% relative reduction in overall data center energy | Siloed heuristic baselines (Best Fit with static cooling) | Sec. 5.3, Table 2 & Fig. 6, p. 1171 |
| Joint optimization gain | 9.8% to 11.4% relative energy savings | Standard joint optimization baselines without dynamic time factor | Sec. 5.3, Fig. 7, p. 1171 |
| Power Usage Effectiveness (PUE) | PUE reduced from 1.48 to 1.29 under fluctuating workloads | Traditional siloed baseline operations | Sec. 5.3, Fig. 8, p. 1172 |
| Thermal safety compliance | Zero hotspot violations (inlet temperatures maintained $< 25^\circ\text{C}$) | Reactive cooling baselines ($> 3.8\%$ hotspot occurrences) | Sec. 5.4, Fig. 9, p. 1172 |
| Actuator oscillation reduction | Cooling control fluctuations reduced by over 40% via PADQN-D | Standard single-time-scale PADQN | Sec. 5.5, Fig. 11, p. 1173 |

## 5. Gap
- **Gap stated by the authors:**
  "DeepEE models a single-hall data center environment; multi-room chilled water loop distribution delays and campus-level building cooling dynamics are not considered... In addition, our model assumes steady electricity supply and does not incorporate time-varying grid electricity pricing or dynamic carbon emission intensity."  [Source: Sec. 6, p. 1173]
- **Gap we observe:**
  The framework optimizes facility energy and PUE rather than operational carbon emissions. It operates entirely within a single physical facility without temporal shifting of flexible batch jobs or multi-datacenter spatial shifting. The evaluation is conducted in a thermodynamic simulation testbed rather than in a production cloud environment.

## 6. Relevance to our project
P13 is a foundational reference for addressing hybrid action spaces in cloud computing. In carbon-aware scheduling, schedulers may need to simultaneously make discrete decisions (which server/datacenter to dispatch to) and continuous decisions (how much power or CPU cap to allocate). PADQN's architecture provides a proven mechanism for structuring such hybrid policy networks.
