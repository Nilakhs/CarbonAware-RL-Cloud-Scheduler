# P14 — Federated Deep Reinforcement Learning for Cloud-Edge Scheduling

**Full citation:** Zhiqing Zhu, Sheng Wang, Yuxuan Zhang, and Yuchao Gao, "A Federated Deep Reinforcement Learning Model for Cloud–Edge Scheduling", in *IEEE Transactions on Cloud Computing*, Vol. 11, No. 3, pp. 1845–1858, July–September 2023 (published online August 2022).  
**DOI / link:** [https://doi.org/10.1109/TCC.2022.3199779](https://doi.org/10.1109/TCC.2022.3199779)  
**Type:** Journal     **Group:** G2 (RL scheduling for cloud workloads with energy, cost, or performance objectives)  
**Quality score:** 7.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.0, Q8: 1.0)*  

---

## 1. Problem addressed
The cloud-edge computing continuum enables low-latency computation by offloading tasks between resource-constrained edge servers and centralized high-capacity cloud datacenters. However, designing effective dynamic scheduling policies across distributed edge tiers poses severe architectural challenges:
1. **Communication and Privacy Bottlenecks:** Centralized DRL schedulers require distributed edge nodes to continuously upload raw execution states, task queues, and user request logs over wide-area networks (WAN) to the cloud, introducing massive communication overhead, high transmission latencies, and data privacy vulnerabilities.
2. **Local Policy Myopia:** Purely local, decentralized DRL agents operating independently at edge nodes suffer from restricted observation scopes and cannot generalize to non-stationary, bursty workload patterns that have not been observed locally.  [Source: Sec. I, pp. 1845–1846]

## 2. Approach (the core idea)
The authors propose a **Federated Deep Reinforcement Learning (FDRL)** framework for dynamic cloud-edge task offloading and resource scheduling. Distributed edge clusters maintain local DRL agents that train policies using local workload arrivals, queuing states, and execution latencies without sharing raw task data. Periodically, edge agents upload only their neural network weight parameters to a centralized cloud coordinator, which aggregates the distributed parameters (using Federated Averaging / FedAvg) to synthesize a generalized global scheduling policy. The global model is broadcast back to edge agents, enabling collective knowledge sharing while preserving edge data privacy and minimizing WAN bandwidth consumption.  [Source: Sec. III & IV, pp. 1847–1852]

## 3. Methodology
- **System role:** Distributed multi-tier cloud-edge task scheduling and offloading coordinator.
- **Scheduling decision:** Multi-tier task offloading target: deciding whether an arriving task should be executed on the local edge node, offloaded to a neighboring edge server, or dispatched to the remote centralized cloud datacenter.
- **Workload type:** Distributed mobile edge and IoT computing requests with heterogeneous CPU demands, data payloads, and deadline constraints.
- **Dynamic or online?** Yes; online decentralized task dispatching at edge nodes coupled with periodic asynchronous federated model updates.
- **For RL papers:**
  - **Algorithm:** Federated Deep Reinforcement Learning (FDRL) combining local Deep Q-Networks (DQN) with cloud-side Federated Averaging (FedAvg).
  - **State ($S_t^i$ at edge node $i$):** State vector capturing: (1) local edge node CPU and memory utilization; (2) queue backlog of pending tasks; (3) wireless and wired network latency and channel bandwidth to adjacent edge servers and the central cloud; and (4) resource requirements and deadline of the incoming task.  [Source: Sec. IV-A, pp. 1848–1849]
  - **Action ($A_t^i$):** Discrete offloading target selection $a_t^i \in \{\text{Local Edge}, \text{Neighbor Edge}_j, \text{Central Cloud}\}$ and local CPU frequency scaling level.  [Source: Sec. IV-B, p. 1849]
  - **Reward ($R_t^i$):** Multi-objective composite reward balancing task execution latency and energy consumption while penalizing deadline violations:
    $$R_t^i = - \left( \mu \cdot T_{\text{response}}(t) + (1 - \mu) \cdot E_{\text{total}}(t) + \eta \cdot \text{Penalty}_{\text{deadline}}(t) \right)$$
    where $\mu \in [0, 1]$ balances latency against energy, and $\eta$ is a penalty coefficient for SLA deadline violations.  [Source: Sec. IV-C, p. 1850]
  - **Training & Federated Aggregation:** Edge agents update local networks via experience replay; after $E$ local training epochs, weight matrices $w_i$ are uploaded to the cloud, aggregated via $w_{\text{global}} = \sum_{i} \frac{n_i}{N} w_i$, and synchronized.  [Source: Sec. IV-D, pp. 1850–1851]
- **Carbon / energy data source and region:** Energy consumption modeled across edge device transmission power and server CPU computing power. Dynamic grid carbon intensity signals ($g\text{CO}_2/\text{kWh}$) are **not** modeled.  [Source: Sec. V-A, p. 1852]
- **Workload trace / dataset:** Real-world task arrival traces from **Google Cluster Data** combined with real-world telecom edge user access patterns (Shanghai telecom base station trace).  [Source: Sec. V-A, p. 1853]
- **Simulator or real system:** **Trace-driven discrete-event cloud-edge network simulation testbed** modeling multiple edge base stations, edge micro-datacenters, wireless links, and a central cloud datacenter. It is **not** a physical wide-area testbed.  [Source: Sec. V-A, pp. 1852–1853]
- **Baselines compared:**
  - *Centralized DRL:* Single central DRL agent receiving all edge telemetry over WAN links.
  - *Local DRL:* Independent, isolated DRL agents training strictly on local observations without federated sharing.
  - *Heuristic Baselines:* Greedy local-first offloading, Round-Robin, and Genetic Algorithm (GA).  [Source: Sec. V-B, p. 1854]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| End-to-end task latency | 16.5% to 24.2% relative reduction in task completion time | Independent local DRL and heuristic offloading | Sec. V-C, Fig. 6 & Table 2, p. 1855 |
| Total energy consumption | 12.8% to 19.3% relative reduction in overall system energy | Heuristic offloading and centralized DRL | Sec. V-C, Fig. 7, p. 1855 |
| WAN communication overhead | Over 80% reduction in network telemetry traffic | Centralized DRL (which requires streaming continuous states) | Sec. V-D, Fig. 9, p. 1856 |
| SLA deadline violation rate | Maintained below 2.5% under volatile arrival bursts | Independent local DRL ($> 7.8\%$ violation rate) | Sec. V-C, Fig. 8, p. 1856 |
| Adaptation speed on new edge nodes | Near-optimal scheduling reached in $3\times$ fewer local steps | Cold-start DRL baseline | Sec. V-E, Fig. 11, p. 1857 |

## 5. Gap
- **Gap stated by the authors:**
  "The current federated framework assumes synchronous parameter aggregation rounds and reliable communication between edge nodes and the central cloud; the presence of communication stragglers or asynchronous parameter updates in unstable wireless channels is not fully explored... Furthermore, dynamic energy price fluctuations across time and regions are omitted."  [Source: Sec. VI, p. 1857]
- **Gap we observe:**
  The framework focuses entirely on execution latency, electrical energy, and communication overhead across cloud-edge tiers. It does not incorporate dynamic grid carbon intensity signals ($g\text{CO}_2/\text{kWh}$), renewable energy availability, or carbon-aware spatial shifting between regions. The evaluation is conducted in a discrete-event simulator rather than on a deployed physical cloud-edge infrastructure.

## 6. Relevance to our project
P14 illustrates how distributed reinforcement learning can be scaled across multi-tier topologies using federated learning principles. This architecture provides vital insights for scaling cloud schedulers across geographically distributed clusters: by aggregating policy parameters rather than streaming continuous raw telemetry, schedulers can coordinate regional carbon awareness while preserving privacy and minimizing inter-region network traffic.
