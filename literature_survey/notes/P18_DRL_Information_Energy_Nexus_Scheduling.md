# P18 — Online Job Scheduling for Low-Carbon Data Centers: An Information and Energy Nexus Perspective

**Full citation:** Wenyu Liu, Yuejun Yan, Yimeng Sun, Hongju Mao, Ming Cheng, Peng Wang, and Zhaohao Ding, "Online job scheduling scheme for low-carbon data center operation: An information and energy nexus perspective", in *Applied Energy*, Vol. 338, Article No. 120918, pp. 1–13, 15 May 2023.  
**DOI / link:** [https://doi.org/10.1016/j.apenergy.2023.120918](https://doi.org/10.1016/j.apenergy.2023.120918)  
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)  
**Quality score:** 7.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 0.5)*  
*(Note on score reconciliation: Reconciled from preliminary screening score of 8.0 to 7.0 following rigorous primary-source audits of Q7 [closed-source code: 0.5] and Q8 [partial discussion of constraints: 0.5]. Note on Q3: Scored 1.0 because the case study integrates real-world dynamic regional electricity prices and time-varying carbon emission rates [$kg\text{CO}_2/\text{kWh}$] derived from power system generation outputs and regional emission factors alongside on-site photovoltaic generation; however, no named public carbon API [such as Electricity Maps or WattTime] or raw downloadable carbon trace is documented in the paper text, so under a stricter interpretation requiring open third-party API traceability, Q3 could be evaluated as 0.5 [yielding 6.5/8]. Note on Q7: Scored 0.5 because although the mathematical formulations, network architecture, and reward scaling algorithm are fully documented in the paper, the source code and model weights are not hosted on a public open repository [GitHub/Zenodo] and are available only on request from the authors. Note on Q8: **Q8 = 0.5 — Partly.** The authors discuss the operational cost–latency trade-off of their proposed scheduler in Section 5.3. However, the paper does not explicitly identify broader unresolved limitations or present a clear future-work agenda in its conclusion. The score reflects partial discussion of the method’s constraints, rather than a formal author-stated limitations section).*  

---

## 1. Problem addressed
The rapid expansion of cloud computing and digital services has driven huge electrical power consumption and carbon emissions across data centers. Traditionally, electrical power systems treat data centers as rigid, inflexible electricity consumers. Concurrently, data center job schedulers typically dispatch computing workloads to optimize purely computational performance metrics—such as job response time, latency, and resource utilization—without considering the dynamic operational conditions of the power grid.

The authors address this disconnect by adopting an **information and energy nexus** perspective, recognizing that computing tasks possess operational flexibility that can be exploited for demand-side energy and carbon management. However, coordinating workload scheduling with power grid dynamics introduces acute challenges:
1. **The Information-Energy Nexus Disconnect:** Power grids face increasing integration of intermittent renewable energy generation, causing time-varying carbon emission intensities and fluctuating electricity market prices. Uncoordinated computing task execution fails to leverage clean power periods, incurring unnecessarily high carbon footprints and electricity expenditures.
2. **Workload Dependencies and Execution Constraints:** Enterprise computing jobs are structured as Directed Acyclic Graphs (DAGs) with strict precedence constraints. Deferring or reordering subtasks to align with green energy must respect parent-child dependencies to avoid workflow stalls and deadline violations.
3. **Job and Server Heterogeneity:** Tasks arrive with heterogeneous demands for multi-dimensional computational resources (CPU and memory), while data center servers exhibit heterogeneous capacities and power consumption characteristics.
4. **Quality of Service (QoS) and Latency Limits:** Delaying flexible tasks to capture lower electricity prices or cleaner grid power must be carefully bounded so that user QoS and Service Level Agreements (SLAs) are strictly maintained.
5. **High Reward Variance in DRL Training:** Fluctuating external electricity prices, dynamic grid carbon emission rates, and stochastic job arrivals inject severe exogenous variance into reinforcement learning reward feedback, destabilizing training gradients and impairing policy convergence.  [Source: Sec. 1 (Introduction), pp. 1–3; Sec. 2 (Problem Description), pp. 3–4]

## 2. Approach (the core idea)
The authors propose an **online job scheduling scheme for low-carbon data center operation** from an information and energy nexus perspective, formulating online task allocation as a Markov Decision Process (MDP) and solving it using Deep Reinforcement Learning (DRL) with an adaptive reward scaling mechanism:

- **Information and Energy Nexus Modeling:** Bridges the information domain (job arrival queues, DAG execution dependencies, multi-resource requirements, QoS limits) with the energy domain (time-varying electricity prices, dynamic grid carbon emission rates, and on-site photovoltaic generation).
- **Temporal Workload Shifting ("Computing Follows Green Energy"):** The scheduler identifies delay-tolerant tasks within incoming DAGs and defers their execution to time windows characterized by high solar photovoltaic generation, low grid carbon intensity, or lower electricity prices, while scheduling urgent tasks promptly to protect QoS.
- **Reward Scaling Scheme (Algorithm 1):** To eliminate the training instability caused by exogenous environmental fluctuations (such as sudden shifts in grid carbon emission rates or electricity tariffs that are independent of scheduling actions), the authors design an adaptive reward scaling algorithm. Algorithm 1 scales the raw environmental reward by dividing it by the running standard deviation of rolling discounted returns without subtracting the running mean ($R'_t = R_t / (\sigma_t + \epsilon)$), stabilizing policy gradients without shifting the reward baseline.
- **Online DRL-Based Job Scheduling Policy (Algorithm 2):** An actor-critic deep neural network architecture observes the system state over a window of $m = 20$ candidate tasks and outputs online dispatch decisions in real time without requiring future foresight of workloads or grid conditions.  [Source: Sec. 1, p. 2; Sec. 2 & 3, pp. 3–6; Sec. 4, pp. 6–8; Algorithm 1 & Algorithm 2]

## 3. Methodology
- **System role:** Centralized online data center job scheduler and workload manager coordinating multi-resource server allocation and grid demand response.
- **Scheduling decision:** Sequential discrete decision at each time step:
  1. *Task Selection & Placement:* Selecting ready tasks from the job waiting queue and assigning them to available heterogeneous physical servers.
  2. *Temporal Deferral:* Deciding to delay execution of flexible tasks to subsequent time slots to await cleaner or cheaper energy.
- **Workload type:** Heterogeneous batch and cloud computing jobs modeled as Directed Acyclic Graphs (DAGs), where vertices represent computational subtasks with specific CPU and memory resource demands and directed edges specify execution precedence dependencies.
- **Dynamic or online?** Yes; fully online dynamic scheduling where jobs arrive continuously without advance knowledge of future arrivals, weather, or electricity prices.
- **For RL papers:**
  - **Algorithm:** Deep Reinforcement Learning (DRL) online scheduling policy (Algorithm 2) integrated with Reward Scaling (Algorithm 1).
  - **State ($S_t$):** Formulated in Section 3 to capture the information-energy nexus:
    - *Workload & Queue Status:* Status of an observation window of $m = 20$ ready tasks, including their CPU demands, memory demands, execution durations, DAG dependency flags, and remaining deadline slack.
    - *Server Status:* Current allocation, remaining resource capacity (available CPU and memory), and busy/available states across servers.
    - *Energy Telemetry:* Current grid electricity price ($p_t$), real-time grid carbon emission rate ($e_t$, in $kg\text{CO}_2/\text{kWh}$), and instantaneous on-site photovoltaic generation.  [Source: Sec. 3, pp. 4–5]
  - **Action ($A_t$):** Discrete action selection determining which ready task from the observed window of $m = 20$ tasks is assigned to which target server, or choosing to defer/wait.  [Source: Sec. 3, pp. 5–6]
  - **Reward ($R_t$):** Multi-objective negative cost function balancing electricity cost, carbon emission cost, and QoS penalties:
    $$R_t = - \left( C_{\text{electricity}}(t) + C_{\text{carbon}}(t) + C_{\text{QoS}}(t) \right)$$
    where:
    - $C_{\text{electricity}}(t) = p_t \cdot P_{\text{total}}(t) \cdot \Delta t$ represents operational electricity expenditure under time-varying price $p_t$.
    - $C_{\text{carbon}}(t) = e_t \cdot P_{\text{total}}(t) \cdot \Delta t$ represents operational carbon emission cost under time-varying grid carbon emission rate $e_t$.
    - $C_{\text{QoS}}(t)$ penalizes task waiting times, queuing delays, and deadline overruns.
    - *Reward Scaling (Algorithm 1):* The raw reward is scaled by dividing it by the running standard deviation of rolling discounted returns (the running mean is not subtracted):
      $$R'_t = \frac{R_t}{\sigma_t + \epsilon}$$
      where $\sigma_t$ tracks the running standard deviation of the rolling discounted sum of rewards (returns), and $\epsilon$ prevents division by zero.  [Source: Sec. 4.1, p. 7; Algorithm 1]
  - **Training Setup & Hyperparameters (Sec. 4 & 5):**
    - *Neural Network Architecture:* Fully connected deep neural network with **3 hidden layers** consisting of **64, 32, and 16 neurons**, respectively.
    - *Activation Function:* **ReLU** across hidden layers.
    - *Optimizer:* **Adam**.
    - *Learning Rate:* **0.005**.
    - *Discount Factor:* **$\gamma = 1$** (undiscounted cumulative cost formulation over finite horizons).
    - *Observation Window:* **$m = 20$** candidate tasks observed simultaneously.
    - *Training Iterations & Scale:* Trained over **300 iterations** across **10 episodes**.  [Source: Sec. 4 & 5, pp. 7–9]
- **Carbon / energy data source and region:**
  - *Electricity Pricing:* Real-world regional time-of-use / dynamic spot market electricity prices ($p_t$).
  - *Carbon Emission Rates:* Dynamic time-varying carbon emission rates ($e_t$, in $kg\text{CO}_2/\text{kWh}$) calculated from power system generation unit outputs and regional fuel-mix emission factors.
  - *Renewable Generation:* Local solar photovoltaic (PV) power generation curves.
  - *(Note on public API traceability: The paper incorporates real regional price and emission curves, but does not document a named public API [such as Electricity Maps or WattTime] or provide a downloadable timestamped carbon trace).*  [Source: Sec. 5, pp. 8–10]
- **Workload trace / dataset:** Real-world enterprise cloud cluster traces logging computing jobs with heterogeneous execution times, CPU/memory resource profiles, and DAG precedence constraints (Alibaba cluster trace ecosystem).  [Source: Sec. 5, pp. 8–10]
- **Simulator or real system:** Trace-driven discrete-event simulation testbed modeling multi-server compute clusters, dynamic task queues, on-site solar generation, and power grid interactions. It is evaluated within simulated scenarios and is **not** released as an open-source production software artifact.  [Source: Sec. 5, pp. 8–11]
- **Baselines compared:**
  - *Tetris Algorithm:* Classical multi-resource packing cluster scheduler [Ref: Grandl et al., SIGCOMM 2014] that assigns tasks based on dot-product alignment between task resource requirements and available server capacities.
  - *FIFO (First-In, First-Out):* Conventional rule-based queue scheduler executing tasks strictly in arrival sequence without carbon or price awareness.
  - *Offline Model Predictive Control (MPC):* Theoretical optimization benchmark with complete rolling lookahead knowledge of future job arrivals, electricity prices, and renewable generation.
  - *Ablation Benchmark (DRL without Reward Scaling):* Identical DRL architecture trained without Algorithm 1's reward scaling to isolate the effect of reward normalization.  [Source: Sec. 5, pp. 9–11]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Combined operational cost reduction | **30% lower** combined electricity and carbon emission costs | Tetris multi-resource packing algorithm | Sec. 5, pp. 9–11; Table 1 / Fig. 6 |
| Task execution latency (QoS cost) | **18% lower** average task processing latency | Tetris multi-resource packing algorithm | Sec. 5, pp. 10–11; Fig. 7 |
| Electricity cost optimization (Textual claim) | **37%** reduction in electricity costs | Baseline / uncoordinated scheduling | Sec. 5, p. 10; Abstract |
| Carbon emission cost optimization (Textual claim) | **14%** reduction in carbon emission costs | Baseline / uncoordinated scheduling | Sec. 5, p. 10; Abstract |
| Electricity cost (Table I numerical values) | **$9,753 $\to$ $7,103** | FIFO baseline scheduling $\to$ Proposed DRL scheme *(Note: Calculated reduction is 27.2%, which does not match the textual claim of 37%)* | Sec. 5, Table 1, p. 10 |
| Carbon emission cost (Table I numerical values) | **$2,096 $\to$ $1,832** | FIFO baseline scheduling $\to$ Proposed DRL scheme *(Note: Calculated reduction is 12.6%, which does not match the textual claim of 14%)* | Sec. 5, Table 1, p. 10 |
| Average task latency (Table I numerical values) | **3.9 $\to$ 4.1** | FIFO baseline scheduling $\to$ Proposed DRL scheme *(Slight latency increase as scheduler trades small delays for energy/carbon savings; in contrast to the 18% lower latency achieved against the multi-resource packing heuristic Tetris in Fig. 7)* | Sec. 5, Table 1, p. 10 |
| Energy/electricity cost difference vs. offline MPC | Within **1.6%** of ideal offline MPC benchmark | Ideal offline Model Predictive Control (MPC) with perfect future lookahead | Sec. 5, p. 11; Fig. 8 |
| Carbon emission cost difference vs. offline MPC | Within **1.8%** of ideal offline MPC benchmark | Ideal offline Model Predictive Control (MPC) with perfect future lookahead | Sec. 5, p. 11; Fig. 8 |
| Latency difference vs. offline MPC | Within **2.6%** of ideal offline MPC benchmark | Ideal offline Model Predictive Control (MPC) with perfect future lookahead | Sec. 5, p. 11; Fig. 8 |
| Training convergence stability | Stabilizes policy learning, eliminates large reward oscillations, and accelerates convergence speed | Ablation baseline (DRL without Algorithm 1 Reward Scaling) | Sec. 4 & 5, pp. 7–8, 10–11; Fig. 5 |

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  1. *Operational Cost–Latency Trade-Offs (Sec. 5.3, pp. 10–11):* The authors discuss the operational cost–latency trade-off of their proposed scheduler in Section 5.3. When the QoS penalty weight is set to a smaller value, the scheduler aggressively delays tasks to wait for low-carbon and low-price periods, which leads to increased task latency; conversely, prioritizing latency limits achievable carbon and electricity savings.
- **Gap we observe:**
  1. *Absence of Dedicated Limitations or Future-Work Section:* The paper does not explicitly identify broader unresolved architectural limitations or present a clear future-work agenda in its conclusion (Sec. 6, pp. 11–12); the analysis in Section 5.3 covers operational trade-offs rather than a formal, self-critical limitations section.
  2. *Workload Flexibility Constrained by Serial DAG Precedence:* In complex workflows with deep serial critical paths, temporal deferral of parent tasks compresses the remaining deadline slack for all downstream dependent subtasks, limiting the scheduler's temporal shifting window under strict QoS requirements.
  3. *Single-Facility Centralized Scope (Lack of Spatial Flexibility):* The framework is formulated and evaluated strictly for a single data center with local on-site PV and temporal shifting, leaving geo-distributed multi-datacenter spatial workload migration and power-flow network constraints unaddressed.
  4. *Closed-Source Implementation:* The codebase, neural network weights, and exact training scripts are not publicly released on an open repository (GitHub/GitLab/Zenodo), limiting independent experimental reproducibility.
  5. *Absence of Public API Carbon Documentation:* Although the case study incorporates dynamic carbon emission rates ($kg\text{CO}_2/\text{kWh}$), it does not document an accessible public API connection (such as Electricity Maps or WattTime) or provide raw timestamped carbon traces for public benchmarking.
  6. *Simulation-Centric Evaluation:* The evaluation is performed in a trace-driven discrete simulation rather than an end-to-end bare-metal Kubernetes cluster with physical power-meter measurements.
  7. *Absence of Energy Storage (BESS):* The framework relies exclusively on demand-side workload flexibility and does not incorporate Battery Energy Storage Systems (BESS) to capture surplus midday solar generation.
  8. *Discrepancy Between Textual and Tabular Metrics:* As documented in Section 4, the paper states textual claims of a 37% electricity cost reduction and 14% carbon cost reduction, whereas direct calculations from Table I ($9,753 $\to$ $7,103 and $2,096 $\to$ $1,832) yield 27.2% and 12.6%, respectively.

## 6. Relevance to our project
P18 is a core anchor paper for Group G3 (RL / DRL for carbon-aware cloud workload scheduling) that provides foundational architectural and mathematical insights for our college project:
1. **The Information-Energy Nexus Framework:** P18 formally establishes the concept of coupling IT workload scheduling with power grid dynamics, proving that data centers can serve as demand-side resources to absorb fluctuating green energy without degrading computational QoS.
2. **Reward Scaling for Volatile Carbon Signals:** Its demonstration that external volatility in carbon emission rates and electricity prices corrupts raw RL gradients—and its solution via Algorithm 1 ($R'_t = R_t / (\sigma_t + \epsilon)$)—provides an essential design pattern for our project's RL reward engineering when processing volatile real-world grid signals.
3. **Multi-Resource DAG Dependency Management:** Demonstrates that DRL can respect complex DAG precedence constraints and multi-resource limits (CPU, memory) while significantly outperforming classic packing heuristics like Tetris.
4. **Targeting the Open-Source Gap:** Because P18 remains closed-source without public reproducible code, our project fills a vital research need by delivering a fully open-source, reproducible carbon-aware RL scheduler with documented hyperparameters and accessible carbon-intensity API connectors.
