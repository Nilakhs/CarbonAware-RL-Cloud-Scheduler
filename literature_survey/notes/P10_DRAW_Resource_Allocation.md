# P10 — DRAW: Deep Reinforcement Learning for Resource Allocation With Workload-Time Windows

**Full citation:** Xing Chen, Lijian Yang, Zheyi Chen, Geyong Min, Xianghan Zheng, and Chunming Rong, "Resource Allocation With Workload-Time Windows for Cloud-Based Software Services: A Deep Reinforcement Learning Approach", in *IEEE Transactions on Cloud Computing*, Vol. 11, No. 2, pp. 1871–1885, April–June 2023 (published online May 2022).  
**DOI / link:** [https://doi.org/10.1109/TCC.2022.3169157](https://doi.org/10.1109/TCC.2022.3169157)  
**Type:** Journal     **Group:** G2 (RL scheduling for cloud workloads with energy, cost, or performance objectives)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*  

---

## 1. Problem addressed
Cloud-based software services experience dynamic, non-stationary, and bursty request arrivals. Cloud service providers face a critical dilemma: static over-provisioning or traditional reactive threshold auto-scalers result either in excessive operational leasing expenditure during off-peak periods or severe Service Level Agreement (SLA) response-time violations during sudden workload surges. Standard heuristic and point-by-point myopic reinforcement learning models optimize provisioning actions at isolated time instants without accounting for upcoming workload trends within finite planning horizons, leading to frequent sub-optimal scaling oscillations.  [Source: Sec. I, pp. 1871–1872]

## 2. Approach (the core idea)
The authors propose **DRAW** (Deep reinforcement learning-based Resource Allocation with Workload-time windows). The approach introduces a workload-time window mechanism ($W_t$) to partition continuous non-stationary request streams into manageable evaluation windows, couples it with a QoS prediction module, and formulates the dynamic resource provisioning problem as a Markov Decision Process (MDP). A Deep Q-Network (DQN) with experience replay and target networks learns proactive scaling policies that optimize the trade-off between operational resource leasing cost and SLA satisfaction.  [Source: Sec. III & IV, pp. 1873–1877]

## 3. Methodology
- **System role:** Cloud resource provisioning and auto-scaling controller for web and software services.
- **Scheduling decision:** Resource scaling vector determining the number and capacity of virtual machine (VM) instances allocated to services.
- **Workload type:** Web requests and transactional cloud software service requests with bursty arrival rates.
- **Dynamic or online?** Yes; online control loop operating over consecutive workload-time windows ($W_t$).
- **For RL papers:**
  - **Algorithm:** Deep Q-Network (DQN) with target network updates and experience replay buffer.
  - **State ($S_t$):** State vector capturing: (1) current VM resource utilization (CPU and memory); (2) average request response time and queuing backlog; and (3) predicted request arrival intensity for the upcoming workload-time window ($W_t$) obtained from the QoS prediction module.  [Source: Sec. IV-A, pp. 1874–1875]
  - **Action ($A_t$):** Discrete scaling action vector representing adjustments to allocated VM resources (scale up, scale down, or maintain instance count and capacity).  [Source: Sec. IV-B, p. 1875]
  - **Reward ($R_t$):** Multi-objective composite reward function balancing resource expenditure against SLA infraction penalties:
    $$R_t = - \left( \alpha \cdot \text{Cost}_{\text{resource}}(t) + (1 - \alpha) \cdot \text{Penalty}_{\text{SLA}}(t) \right)$$
    where $\alpha \in [0, 1]$ is a weighting parameter balancing monetary leasing expenditure and SLA penalties incurred when response times exceed threshold $T_{\text{SLA}}$.  [Source: Sec. IV-C, p. 1876]
  - **Training setup:** DQN parameterized with fully connected hidden layers, experience replay memory capacity of 10,000 transitions, discount factor $\gamma = 0.9$, decaying $\epsilon$-greedy exploration rate, and target network parameter synchronization every $C = 100$ steps.  [Source: Sec. IV-D, pp. 1876–1877]
- **Carbon / energy data source and region:** Not applicable. The paper focuses strictly on monetary resource leasing cost and SLA violation penalties; grid carbon intensity and energy telemetry are not modeled.  [Source: Sec. IV-C, p. 1876]
- **Workload trace / dataset:** Real-world empirical request logs from the **WorldCup 1998 website access trace** combined with synthetic workload streams generated via Pareto distributions to simulate peak burst traffic.  [Source: Sec. V-A, p. 1878]
- **Simulator or real system:** **Trace-driven discrete-event cloud simulation testbed** implemented in Java/Python (simulating cloud VM instances, request queuing, and provisioning latency). It is **not** a live multi-tenant production cluster deployment.  [Source: Sec. V-A, pp. 1878–1879]
- **Baselines compared:**
  - *Reactive Threshold Autoscaling:* Traditional threshold-triggered scaling that reacts only after SLA breaches or CPU saturation occurs.
  - *DPSO-GA (Discrete Particle Swarm Optimization - Genetic Algorithm):* Metaheuristic resource optimization baseline.
  - *Static Provisioning:* Over-provisioned peak-capacity baseline.
  - *Standard DQN (Myopic):* Standard DRL scheduler without workload-time window lookahead.  [Source: Sec. V-B, p. 1879]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Operational resource cost | 3.8% to 13.8% relative reduction in resource leasing cost | DPSO-GA and reactive threshold autoscaling | Sec. V-C, Fig. 6 & Table 3, p. 1880 |
| SLA violation rate | Maintained below 2.1% under heavy traffic bursts | Reactive threshold autoscaling ($> 8.4\%$ SLA violation rate) | Sec. V-C, Fig. 7, p. 1881 |
| Resource utilization efficiency | Average CPU utilization improved by 11.2% | Static peak provisioning | Sec. V-C, Fig. 8, p. 1881 |
| Decision latency | Sub-10ms scheduling decision latency per workload window | DPSO-GA (which required $> 1.2\text{s}$ per decision) | Sec. V-D, p. 1882 |
| Policy convergence | Stable convergence achieved within 600 training episodes | Standard DQN without window prediction ($> 1,100$ episodes) | Sec. V-C, Fig. 5, p. 1880 |

## 5. Gap
- **Gap stated by the authors:**
  "Our current model considers resource allocation for software services based on standard VM instances with homogeneous configurations, without considering heterogeneous containerized microservices or fine-grained serverless function invocations... Furthermore, the current framework operates within a single cloud provider environment without multi-cloud or geo-distributed workload dispatching."  [Source: Sec. VI, p. 1883]
- **Gap we observe:**
  The formulation does not model carbon emissions, grid carbon intensity ($g\text{CO}_2/\text{kWh}$), or energy efficiency. Its relevance to our project is strictly algorithmic: demonstrating proactive DRL resource allocation under SLA response-time constraints using temporal window lookaheads. The experimental evaluation is conducted entirely in a discrete-event simulation testbed rather than a physical cluster.

## 6. Relevance to our project
P10 provides a well-formulated baseline for Group G2 on how DRL agents can incorporate workload-time window lookaheads to prevent reactive SLA violations during bursty traffic. While carbon-agnostic, its MDP reward structure—explicitly penalizing SLA response-time infractions against resource leasing costs—informs how we can penalize SLA breaches alongside carbon emissions in our multi-objective carbon-aware RL scheduler.
