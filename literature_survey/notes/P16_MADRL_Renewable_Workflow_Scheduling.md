# P16 — Multi-Agent Deep Reinforcement Learning for Renewable Energy-Aware Cloud Workflow Scheduling

**Full citation:** Amanda Jayanetti, Saman Halgamuge, and Rajkumar Buyya, "Multi-Agent Deep Reinforcement Learning Framework for Renewable Energy-Aware Workflow Scheduling on Distributed Cloud Data Centers", in *IEEE Transactions on Parallel and Distributed Systems*, Vol. 35, No. 4, pp. 604–615, April 2024.  
**DOI / link:** [https://doi.org/10.1109/TPDS.2024.3360448](https://doi.org/10.1109/TPDS.2024.3360448)  
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)  
**Quality score:** 6.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 0.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*  
*(Note on Q3: Scored 0.0 under strict methodology rubric enforcement because Q3 explicitly evaluates the use of real grid carbon-intensity time-series data [$g\text{CO}_2/\text{kWh}$ from Electricity Maps, WattTime, or regional balancing authorities], and the G2 real energy/power exception does not apply to G3. While P16 utilizes real empirical solar PV and wind generation traces from UQ Gatton alongside SPECpower benchmark server measurements, it models power consumption in kW/kWh without actual grid carbon-intensity factors. Under a broader interpretation where empirical renewable generation is credited as proxy environmental data, Q3 could be considered 0.5 [yielding 7.0/8]. Note on Q7: Scored 0.5 because simulation code is not publicly available and specific neural network training hyperparameters—such as exact learning rates, discount factor numerical scalar, batch size, and replay buffer dimensions—are Not stated in paper).*  

---

## 1. Problem addressed
The explosive growth of cloud computing has triggered massive electrical power consumption across geographically distributed data centers, generating unsustainable carbon footprints and severe operational expenses. While powering cloud data centers with on-site renewable energy sources (such as solar photovoltaic systems and wind turbines) presents an attractive path toward decarbonization, it introduces acute operational challenges:
1. **Renewable Intermittency and Spatial Heterogeneity:** Solar irradiance and wind speed fluctuate non-stationarily over time and vary dramatically across geographic regions, making continuous green energy matching highly uncertain.
2. **Workflow Precedence and Inter-Task Dependency Constraints:** Complex scientific and enterprise applications are structured as Directed Acyclic Graphs (DAGs) with strict execution precedence constraints and significant inter-task data transfer volumes, where task scheduling delays propagate across descendant workflows.
3. **NP-Hard Scalability and Curse of Dimensionality:** Scheduling multi-task workflow DAGs across distributed multi-cloud data centers with heterogeneous compute nodes, dynamic brown grid power, and intermittent green energy supplies is an NP-hard problem. Traditional heuristics (e.g., greedy approaches or genetic algorithms) cannot adapt to dynamic weather shifts, while centralized single-agent deep reinforcement learning (DRL) suffers from exponential state-action space explosion and communication bottlenecks.  [Source: Sec. I, pp. 604–605; Sec. III, pp. 606–608]

## 2. Approach (the core idea)
The authors propose a hierarchical **Multi-Agent Deep Reinforcement Learning (MADRL)** framework based on an Actor-Critic architecture that implements **Centralized Training with Decentralized Execution (CTDE)** and **localized observation sharing**. 

To tackle the combinatorial complexity of distributed workflow scheduling, the framework decomposes decision-making into two collaborative layers:
- **Global Scheduler (Macro-Spatial Level):** A global agent operates at the multi-cloud orchestrator tier, evaluating incoming workflow DAGs, network transfer overheads, and regional renewable generation forecasts to dispatch workflow tasks to candidate geographically distributed cloud data centers.
- **Local Schedulers (Micro-Temporal Level):** Autonomous local agents stationed at each individual data center receive assigned workflow tasks and perform fine-grained micro-temporal scheduling—mapping tasks onto specific physical servers/virtual machines (VMs) based on intra-datacenter host utilization, thermal profiles, and instantaneous localized renewable generation.
- **Localized Observation Sharing:** Agents exchange compact state observations strictly with neighboring entities rather than broadcasting global telemetry. This overcomes environmental non-stationarity, eliminates wide-area communication saturation, and dramatically accelerates multi-agent training convergence ($<100$ episodes vs. $\sim 500$ episodes for generic MADRL).  [Source: Sec. I, p. 605; Sec. IV, pp. 608–610]

## 3. Methodology
- **System role:** Hierarchical two-tier distributed cloud workflow orchestrator and resource scheduler coordinating geo-distributed data centers under intermittent renewable energy generation.
- **Scheduling decision:** Two-stage hierarchical decision:
  1. *Macro-spatial assignment:* Selecting candidate destination data center $DC_m \in \{DC_1, \dots, DC_M\}$ for each ready workflow task $v_k$ by the Global Scheduler.
  2. *Micro-temporal mapping:* Selecting physical host $H_j \in \{H_1, \dots, H_N\}$ / VM instance within the chosen data center and sequencing task execution start times by the Local Scheduler to maximize green energy consumption windows.
- **Workload type:** Scientific workflow applications modeled as Directed Acyclic Graphs (DAGs) $\mathcal{G} = (\mathcal{V}, \mathcal{E})$, where vertices $v_i \in \mathcal{V}$ represent computational tasks with specific instruction lengths (in Million Instructions, MI) and directed edges $e_{i,j} \in \mathcal{E}$ represent data dependency transfer volumes (in MB).
- **Dynamic or online?** Yes; online dynamic workflow scheduling where workflows arrive dynamically and scheduling adapts continuously to real-time renewable energy production.
- **For RL papers:**
  - **Algorithm:** Multi-Agent Actor-Critic framework utilizing Centralized Training with Decentralized Execution (CTDE) augmented with localized observation sharing between adjacent agents.
  - **State ($S_t$ / Local Observations):**
    - *Global Scheduler Observation ($o_{\text{global}}$):* Workload DAG topological structure (task runtime requirements, remaining workflow critical path, inter-task data dependencies, deadline slack), inter-datacenter WAN bandwidth/latency matrices, and renewable energy generation forecasts across all geo-distributed data centers.
    - *Local Scheduler Observation ($o_i(t)$ at Data Center $i$):* Local real-time solar and wind power output $P_{\text{green}, i}(t)$, active host CPU and memory utilization profiles, waiting task queue backlog $Q_i(t)$, server power consumption states, and localized shared feature vectors from adjacent agents.  [Source: Sec. IV-A & IV-B, pp. 608–609]
  - **Action ($A_t$):**
    - *Global Action ($a_{\text{global}, k}$):* Discrete datacenter routing decision mapping workflow task $v_k$ to candidate data center $i \in \{1, \dots, M\}$.
    - *Local Action ($a_{i, k}$):* Discrete resource assignment selecting physical host $j \in \{1, \dots, N_i\}$ and execution ordering within data center $i$.  [Source: Sec. IV-B, p. 609]
  - **Reward ($R_t$):** Formulated hierarchically in the Partially Observable Markov Game ($\mathcal{R}_i: \mathcal{S} \times \mathcal{A}_i \to \mathbb{R}$). In Algorithm 1, the total step reward is explicitly defined as:
    $$R_t = R_{\text{global}} + R_{\text{local}} \quad \text{[Sec. IV-B, p. 609]}$$
    where:
    - $R_{\text{global}}$ is evaluated by the Global Scheduler agent based on the green energy surplus/deficit at the selected candidate data center and feedback from the local host assignment.
    - $R_{\text{local}}$ is evaluated by the Local Scheduler agent based on host power efficiency, execution duration, and task completion progress.
    *(Note: While conceptually designed to maximize green energy consumption while penalizing brown grid energy and execution delays, explicit linear scalarized weight formulations—e.g., $R(t) = R_{\text{green}} - \alpha E_{\text{brown}} - \beta \text{Makespan}$—are interpretive representations; the explicit formula stated in the paper is $R_t = R_{\text{global}} + R_{\text{local}}$ [Sec. IV-B, pp. 608–610]).*
  - **Training setup & convergence acceleration:** Centralized training evaluates global and local value functions/critics using broader environmental information, while actor policies execute decentralized using localized observations [Sec. IV-B, pp. 608–610]. Neural networks are implemented using Keras integrated with CloudSim [Sec. V-A, p. 611]. The discount factor is formulated mathematically as $\gamma \in (0, 1)$ in the cumulative discounted return objective $J(\theta)$ [Sec. IV-A, p. 608]; its exact numerical value evaluated in simulations is **Not stated in paper**. Specific optimizer choice (e.g., Adam), learning rates, experience replay capacity, batch size, and hidden layer dimensions are **Not stated in paper**. Localized observation sharing restricts communication to adjacent data center neighborhoods, accelerating policy convergence by up to $5\times$ ($<100$ episodes vs. $\sim 500$ episodes for generic uncoordinated MADRL) [Sec. IV-C & V-C, pp. 610–612].
- **Carbon / energy data source and region:** Real-world empirical renewable energy generation traces combining solar photovoltaic (PV) generation traces (from on-site solar installations, such as the University of Queensland Gatton solar research facility) and real-world wind turbine generation data. Power consumption of heterogeneous physical servers is calibrated using the industry-standard **SPECpower_ssj2008** benchmark suite (modeling active power curves from 0% to 100% CPU utilization and idle power consumption for server architectures like Dell PowerEdge and HP ProLiant). *(Note on carbon intensity: The paper models electrical power consumption and on-site green power generation in kW/kWh; real-time regional grid carbon-intensity data [$g\text{CO}_2/\text{kWh}$ from Electricity Maps, WattTime, or regional balancing authorities] is Not utilized or modeled in the paper).*  [Source: Sec. V-A, pp. 610–611]
- **Workload trace / dataset:** Five standard real-world scientific workflow application benchmarks from the **Pegasus Workflow Management System**:
  1. **Montage:** Astronomy sky mosaic engine (I/O- and data-intensive).
  2. **CyberShake:** Earthquake hazard characterization (memory- and compute-intensive).
  3. **Epigenomics:** Genome sequence mapping pipeline (CPU-bound).
  4. **Inspiral (LIGO):** Gravitational wave detection analysis (compute-intensive).
  5. **SIPHT:** Bioinformatics small non-coding RNA search (high task parallelism).  
  Evaluated across multiple problem scales (25, 50, and 100 tasks per workflow DAG).  [Source: Sec. V-A, p. 611]
- **Simulator or real system:** **Trace-driven discrete-event simulation testbed extending CloudSim**, integrated with Python and Keras deep learning frameworks for neural network training and policy inference. Modeled an infrastructure of 10 distributed cloud data centers, each hosting 25 heterogeneous physical compute servers. It is **not** evaluated on physical bare-metal hardware or live production cloud clusters.  [Source: Sec. V-A, pp. 610–611]
- **Baselines compared:**
  - *Random:* Random assignment of workflow tasks across distributed data centers and internal compute servers.
  - *Green-Opt (Greedy Heuristic):* Greedy heuristic that dispatches tasks strictly to the data center exhibiting highest instantaneous green energy generation without lookahead or workflow dependency coordination.
  - *Generic DRL:* Single-agent centralized deep reinforcement learning scheduler attempting to manage both inter-datacenter routing and intra-datacenter host mapping simultaneously.
  - *Generic MADRL:* Standard multi-agent deep reinforcement learning baseline without hierarchical decomposition and localized observation sharing.  [Source: Sec. V-B, p. 611]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Electrical energy consumption reduction | Up to 47% reduction in energy consumption of workflow executions (Note: Refers strictly to electrical energy consumption in Joules/kWh, NOT carbon-emissions reduction) | Traditional and comparison baseline algorithms (Random, Green-Opt, Generic DRL) | Abstract; Sec. V-C, pp. 611–613 |
| Workflow makespan | Workflow makespan maintained on par / competitive with baseline algorithms (energy reduction is achieved without significant makespan inflation; formal SLA deadline violation rates are Not evaluated/stated in paper) | Baseline algorithms (Green-Opt, Generic DRL, Random) | Abstract; Sec. V-C, pp. 612–613 |
| Training convergence acceleration | Up to 5x faster convergence rate (stabilizes in <100 episodes) | Generic MADRL baseline with full observation broadcasting (which requires ~500 episodes to converge) | Abstract; Sec. V-C, pp. 611–612 |
| Green energy utilization | Substantially higher green energy consumption share across all 5 scientific workflows | Random and Green-Opt heuristics | Sec. V-C, Figs. 4–8, pp. 612–614 |
| Empirical performance across evaluated DAG scales | Energy efficiency gains over baselines maintained across tested scales of 25, 50, and 100 tasks | Generic DRL (which suffers severe degradation as DAG task count increases; formal theoretical scale-invariance is Not evaluated/stated in paper) | Sec. V-C, Table 3 & Figs. 6–8, pp. 612–614 |

## 5. Gap
- **Gap stated by the authors:**
  1. *Partial Observability and Information Latency:* Because local agents operate under localized observations, sudden wide-area network telemetry delays or temporary synchronization lag can lead to sub-optimal routing decisions during sharp workload surges.
  2. *Renewable Forecast Uncertainty:* While the model incorporates generation patterns, extreme meteorological volatility and unpredicted micro-climatic disruptions cause forecast mismatches, forcing temporary reliance on brown grid power.
  3. *Ultra-Dense Scalability Bounds:* Expanding beyond the evaluated 10-datacenter topology to hundreds of distributed edge nodes may increase inter-agent coordination complexity.  [Source: Sec. V-C & VI, pp. 613–615]
- **Gap we observe:**
  1. *Simulation-Only Evaluation:* The framework is validated entirely within an extended CloudSim discrete-event simulator; it has not been implemented or validated on physical bare-metal hardware, Kubernetes clusters, or multi-region public cloud testbeds.
  2. *Lack of Grid Marginal Carbon Intensity (MOER / AEF):* The optimization focuses on local on-site renewable energy matching ($E_{\text{green}}$ vs. $E_{\text{brown}}$) rather than querying real-time regional marginal emissions factors ($g\text{CO}_2/\text{kWh}$ from WattTime or Electricity Maps), missing opportunities to schedule into clean regional grids when on-site generation is absent.
  3. *Static Scientific Workloads:* Workloads are limited to static offline Pegasus DAG benchmarks (Montage, CyberShake, etc.); the model is not evaluated on streaming microservices, event-driven pipelines, or modern distributed Generative AI / Large Language Model fine-tuning workloads.
  4. *Absence of Battery Energy Storage Systems (BESS):* The framework does not incorporate on-site energy storage (batteries or thermal storage), preventing time-shifting of surplus renewable generation that exceeds current datacenter load.
  5. *Uniform Energy Cost (No Spot Pricing Arbitrage):* The objective function treats brown grid power uniformly and does not model real-time electricity spot market prices or locational marginal pricing (LMP).

## 6. Relevance to our project
P16 is a foundational anchor paper for Group G3 (RL / DRL for carbon-aware cloud workload scheduling). It addresses the crucial challenge of scheduling complex, dependency-constrained workflow DAGs across distributed data centers powered by fluctuating green energy. Methodologically, its hierarchical Centralized Training with Decentralized Execution (CTDE) architecture demonstrates how to decompose distributed scheduling into macro-spatial datacenter selection and micro-temporal host mapping, successfully overcoming the curse of dimensionality that cripples single-agent DRL. Furthermore, its localized observation sharing mechanism provides an architectural blueprint for scaling multi-agent RL schedulers with low communication overhead and rapid convergence, directly inspiring our project's scheduler design.
