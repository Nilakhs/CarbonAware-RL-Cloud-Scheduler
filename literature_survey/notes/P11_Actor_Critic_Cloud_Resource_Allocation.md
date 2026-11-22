# P11 — Actor-Critic Deep Reinforcement Learning for Cloud Resource Allocation

**Full citation:** Zheyi Chen, Jia Hu, Geyong Min, Chengqiang Luo, and Tarek El-Ghazawi, "Adaptive and Efficient Resource Allocation in Cloud Datacenters Using Actor-Critic Deep Reinforcement Learning", in *IEEE Transactions on Parallel and Distributed Systems*, Vol. 33, No. 8, pp. 1911–1923, August 2022 (published online December 2021).  
**DOI / link:** [https://doi.org/10.1109/TPDS.2021.3132422](https://doi.org/10.1109/TPDS.2021.3132422)  
**Type:** Journal     **Group:** G2 (RL scheduling for cloud workloads with energy, cost, or performance objectives)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*  

---

## 1. Problem addressed
Large-scale cloud datacenters face non-stationary workload arrivals and complex, heterogeneous physical server environments. Traditional static or rule-based scheduling heuristics (such as First Fit or Best Fit) cannot adapt dynamically to fluctuating resource demands, causing severe resource fragmentation, high server energy consumption, and degraded Quality-of-Service (QoS) through elongated job completion times and elevated job dismissal rates. Furthermore, standard value-based DRL algorithms (like standard DQN) suffer from high policy variance and slow convergence when scaling across high-dimensional server allocation spaces.  [Source: Sec. I, pp. 1911–1912]

## 2. Approach (the core idea)
The authors formulate dynamic cloud resource provisioning as a continuous Markov Decision Process and design an **Actor-Critic Deep Reinforcement Learning** framework. The **Actor network** parameterizes and optimizes the resource dispatching policy directly, while the **Critic network** evaluates the action values and computes an **Advantage function** ($A(s, a) = Q(s, a) - V(s)$). By subtracting the baseline state value $V(s)$, the advantage formulation significantly reduces the variance of the policy gradient updates, enabling rapid convergence toward an energy-efficient and latency-minimizing allocation policy.  [Source: Sec. III & IV, pp. 1913–1917]

## 3. Methodology
- **System role:** Centralized cloud datacenter resource scheduler and job dispatcher.
- **Scheduling decision:** Discrete mapping of incoming multi-resource jobs onto available physical servers (PMs).
- **Workload type:** Multi-resource cloud jobs with heterogeneous CPU and memory resource demands.
- **Dynamic or online?** Yes; online dispatching executed on dynamic job arrival events.
- **For RL papers:**
  - **Algorithm:** Actor-Critic DRL utilizing an Advantage policy gradient formulation.
  - **State ($S_t$):** State vector capturing: (1) real-time CPU and memory utilization vectors across all physical servers; (2) current job queue backlogs; and (3) resource requirements (CPU cores, memory capacity, duration) of the newly arriving job.  [Source: Sec. IV-A, pp. 1914–1915]
  - **Action ($A_t$):** Discrete action $a_t \in \{1, 2, \dots, M\}$ selecting the target physical server from $M$ available hosts to allocate the incoming job.  [Source: Sec. IV-B, p. 1915]
  - **Reward ($R_t$):** Multi-objective composite reward function penalizing server power consumption, job queuing latency, and job dismissals:
    $$R_t = - \left( w_e \cdot E_{\text{server}}(t) + w_l \cdot L_{\text{latency}}(t) + w_d \cdot D_{\text{dismiss}}(t) \right)$$
    where $w_e, w_l, w_d$ are positive weighting factors balancing energy conservation against latency and rejection penalties.  [Source: Sec. IV-C, p. 1916]
  - **Training setup:** Multi-layer fully connected neural networks for both Actor and Critic networks, optimized using Adam optimizer (learning rate $10^{-3}$), discount factor $\gamma = 0.95$, and batch gradient updates computed over trajectory episodes.  [Source: Sec. IV-D, p. 1917]
- **Carbon / energy data source and region:** Server electrical power modeled using real physical server power specifications (incorporating idle power of approximately 100W up to 250W peak at 100% CPU load). Grid carbon intensity signals are **not** modeled.  [Source: Sec. V-A, p. 1918]
- **Workload trace / dataset:** Real-world workload trace logs from **Google Cloud Datacenter Traces** (Google 2011/2019 cluster trace) containing heterogeneous job arrival timestamps and multi-resource requirements.  [Source: Sec. V-A, p. 1918]
- **Simulator or real system:** **Trace-driven discrete-event cloud datacenter simulator** modeling server host power curves and queue dynamics. It is **not** a physical cluster deployment.  [Source: Sec. V-A, pp. 1918–1919]
- **Baselines compared:**
  - *Heuristic Baselines:* First Fit (FF), Best Fit (BF), and Random allocation.
  - *DRL Baselines:* DeepRM (Mao et al., seminal 2016 work) and standard Policy Gradient (REINFORCE).  [Source: Sec. V-B, p. 1919]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Server energy consumption | 14.6% to 22.8% relative reduction in total datacenter energy | First Fit (FF) and Best Fit (BF) heuristics | Sec. V-C, Fig. 6 & Table 2, p. 1920 |
| Average job latency | 18.3% relative reduction in average response time | DeepRM baseline and First Fit heuristic | Sec. V-C, Fig. 7, p. 1920 |
| Job dismissal rate | Maintained below 1.2% under heavy workload traffic | First Fit and Best Fit heuristics ($> 5.8\%$ rejection rate) | Sec. V-C, Fig. 8, p. 1921 |
| Training convergence speed | Convergence achieved in $2.3\times$ fewer training iterations | Standard REINFORCE policy gradient baseline | Sec. V-D, Fig. 10, p. 1921 |
| Gradient variance | Gradient variance reduced by over 45% via Advantage baseline | Standard Actor-Critic without advantage subtraction | Sec. V-D, Fig. 11, p. 1922 |

## 5. Gap
- **Gap stated by the authors:**
  "The current model considers server-level resource allocation within a single cloud datacenter. Network bandwidth constraints and inter-rack communication latency are simplified... Moreover, the model does not consider workload migrations across geographically distributed datacenters."  [Source: Sec. VI, p. 1922]
- **Gap we observe:**
  The optimization objective is restricted to electrical power consumption and job latency; it does not model dynamic grid carbon intensity ($g\text{CO}_2/\text{kWh}$) or on-site renewable energy matching. The evaluation is conducted in a discrete-event simulator using Google traces rather than on a physical bare-metal or Kubernetes testbed.

## 6. Relevance to our project
P11 demonstrates the superior stability and sample efficiency of Actor-Critic DRL with an Advantage function compared to value-based DQN or naive REINFORCE in cloud scheduling. This Advantage Actor-Critic (A2C/PPO) formulation provides a direct architectural template for our carbon-aware scheduler when balancing multi-resource constraints against dynamic emissions.
