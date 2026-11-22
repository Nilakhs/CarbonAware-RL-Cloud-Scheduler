# P17 — Eco-Friendly Reinforcement Learning in Federated Cloud (ERLFC) Task Scheduling

**Full citation:** Zhibao Wang, Shuaijun Chen, Lu Bai, Juntao Gao, Jinhua Tao, Raymond R. Bond, and Maurice D. Mulvenna, "Reinforcement learning based task scheduling for environmentally sustainable federated cloud computing", in *Journal of Cloud Computing: Advances, Systems and Applications*, Vol. 12, Article No. 174, pp. 1–17, December 2023.  
**DOI / link:** [https://doi.org/10.1186/s13677-023-00553-0](https://doi.org/10.1186/s13677-023-00553-0)  
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)  
**Quality score:** 6.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 0.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 0.5)*  
*(Note on Q3: Scored 0.0 under strict methodology rubric enforcement because Q3 explicitly evaluates the use of real dynamic grid carbon-intensity time-series data [$g\text{CO}_2/\text{kWh}$ from Electricity Maps, WattTime, or regional balancing authorities], and the G2 real energy/power exception does not apply to G3. P17 defines static, unitless carbon emission ratios assigned to energy types in Table 2 [Fire: 0.6, Solar: 0.3, Wind: 0.1, Hydro: 0.3, Hydrogen: 0.2, Nuclear: 0.3] rather than empirical dynamic grid carbon-intensity time series. Under a broader sensitivity interpretation where static regional fuel-mix emission ratios are credited as proxy environmental data, Q3 could be scored 0.5 [yielding 7.0/8]. Note on Q7: Scored 1.0 because full Python/PyTorch source code, training scripts, datasets, and network configurations are publicly released on GitHub [Ref. 50: https://github.com/ShuaijunC/RL_BasedTaskSchedulingForEnvironmentallSustatinableFCC]. Note on Q8: Scored 0.5 because the authors discuss limitations regarding increased task waiting delays under large workloads in Section 17 and server shutdown/domain specialization in Section 18 [Conclusion], but do not include a dedicated, standalone limitations section).*  

---

## 1. Problem addressed
Massive electrical energy consumption across cloud data centers has become a critical contributor to global greenhouse gas emissions and operational expenditure. While cloud computing has seen widespread adoption due to elasticity and pay-per-use economics, traditional centralized cloud paradigms have reached an efficiency plateau characterized by resource contention, cooling overheads, and high carbon footprints.

The authors address the challenge of environmentally sustainable task scheduling in a **federated cloud (FC)** environment composed of multiple geographically distributed Cloud Service Providers (CSPs). Federated cloud scheduling introduces distinct optimization complexities:
1. **Multi-Tier Hierarchical Infrastructure:** A federated cloud system spans multiple autonomous cloud service providers ($DS_1, \dots, DS_n$), each operating data centers containing multiple server/machine rooms ($MH_1, \dots, MH_m$), which in turn house heterogeneous physical servers ($PM_1, \dots, PM_k$). Coordinating decisions across this multi-tier hierarchy is NP-hard.
2. **Workload Dependencies and Communication Overheads:** Complex computational jobs arrive as Directed Acyclic Graphs (DAGs) with strict execution precedence constraints. Arbitrary distribution of interdependent subtasks across wide-area networks incurs severe network transfer latency and data transfer energy penalties.
3. **Heterogeneous and Dynamic Cooling Systems:** Data center infrastructure energy is heavily dominated by cooling equipment. Server rooms deploy disparate cooling mechanisms—primarily forced air cooling and liquid cooling—whose power consumption varies non-linearly with server computation load. Switching cooling mechanisms dynamically introduces mechanical and electrical startup power overheads.
4. **Spatial Heterogeneity of Regional Energy Sources:** Geographically dispersed data centers operate on different regional power grids utilizing diverse energy sources (e.g., hydroelectric power in Norway vs. nuclear power in France vs. fossil fuels). Scheduling must exploit these geographic fuel-mix differences to minimize carbon emissions without violating service level agreements (SLAs).
5. **Real-Time Unbounded Task Arrivals:** In real-world environments, DAG tasks arrive dynamically without fixed time horizons or batch boundaries, requiring continuous online scheduling and load balancing.  [Source: Sec. 1 (Introduction), pp. 1–3; Sec. 7 (Methodology / Problem definition), pp. 4–5]

## 2. Approach (the core idea)
The authors propose **ERLFC** (**Eco-friendly Reinforcement Learning in Federated Cloud**), an intelligent, hierarchical two-tier scheduling framework combining deep reinforcement learning with classical heuristic mapping:

- **Macro-Spatial Scheduling via Actor-Critic (PPO):** An intelligent central agent utilizes an Actor-Critic architecture trained with Proximal Policy Optimization (PPO). The agent evaluates the dynamic state of each data center (including server room load, energy consumption, cooling methods, and regional carbon emission ratios) alongside incoming DAG task characteristics to assign each DAG task to an optimal server room in a specific data center (or defer assignment via a null action).
- **Subtask Co-Location to Eliminate Network Penalties:** Rather than scattering individual DAG subtasks across different data centers or server rooms, ERLFC assigns all interdependent subtasks of a given DAG to the same server room. This strategic co-location eliminates wide-area network data transmission energy consumption, avoids transmission latency, and allows overlapping computation and communication.
- **Micro-Temporal Subtask Mapping via HEFT:** Within the selected server room, the Heterogeneous Earliest Finish Time (HEFT) algorithm maps individual subtasks onto specific physical servers, ensuring that DAG dependency constraints are strictly respected and makespan is minimized.
- **Dynamic Cooling Modeling & Switching:** The framework explicitly incorporates the energy dynamics of forced air cooling (governed by blower fan laws, with cooling ratio $cr = 0.0005$) and liquid cooling ($cr = 0.2$), modeling dynamic switching based on real-time server compute load ($exe(server) \times P_{\text{peak}} \gtrless P_{\text{airPeak}}$) and factoring in startup energy overheads ($P_{\text{airStart}} = 0.525\text{ kW}$, $P_{\text{liquidStart}} = 1.5\text{ kW}$).
- **Event-Driven Watermark Advancement:** To simulate continuous, asynchronous real-time task execution without artificial discrete time-step synchronization, the authors implement an event-driven "watermark" mechanism ($wr = 0.25$) that advances simulation time based on minimum remaining server execution times.  [Source: Sec. 1, p. 2; Sec. 7, pp. 4–8; Figs. 1–4]

## 3. Methodology
- **System role:** Federated cloud broker / global orchestrator and resource scheduler managing workload distribution across geographically dispersed multi-provider data centers.
- **Scheduling decision:** Two-stage hierarchical decision:
  1. *Macro-spatial assignment (RL Agent):* Selecting the destination data center $DS_i$ and server room $MH_j$ for an incoming DAG task $DT_k$, or choosing not to assign to the current data center ($prob_{\text{nothing}}$).
  2. *Micro-temporal mapping (HEFT):* Mapping each individual subtask $task_m \in DT_k$ to a physical server $PM_l$ within the chosen room and sequencing execution to minimize makespan.
- **Workload type:** Real-world DAG workflows from the **Google Cluster dataset** [Ref. 55: Charles Reiss & John Wilkes, 2014]. Workloads are modeled as Directed Acyclic Graphs $\text{DT} = \{task_1, task_2, \dots, task_\partial\}$, where each subtask is characterized by start time $st$, execution duration $pt$, and parent dependency set $pre\_task$.
- **Dynamic or online?** Yes; dynamic online real-time task scheduling with continuous task arrivals governed by an event-driven watermark advance mechanism.
- **For RL papers:**
  - **Algorithm:** Actor-Critic reinforcement learning incorporating Proximal Policy Optimization (PPO) with clipped surrogate objective ($\epsilon = 0.2$).
  - **State ($S_t$, 39 dimensions):** Formulated as $S = (minWT_i, maxWT_i, TE_i, CT_i, TEN, TEM, ET, ER, CNT, CMET)$:
    - *Local Server Room Features (28 dimensions: $4 \times 7$ rooms):* For each server room $i \in \{1, \dots, 7\}$ in candidate data center: shortest waiting time $minWT_i$, longest waiting time $maxWT_i$, total energy consumption $TE_i$, and active cooling method $CT_i$ (air vs. liquid).
    - *Global Data Center Features (9 dimensions):* Total data center energy consumption $TEN = \sum TE_i$, total carbon emission $TEM = ER \times TEN$, energy type index $ET$, and static emission ratio $ER$.
    - *Task Features (2 dimensions):* Normalized subtask count $CNT = \partial / \max(h(\partial), \partial)$ and normalized maximum subtask execution duration $CMET = \max(pt) / \max(h(pt), \max(pt))$, where $h(\cdot)$ tracks historical maximums.  [Source: Sec. 7, pp. 5–7; Eqs. 7–12, 15–16]
  - **Action ($A_t$, 8 dimensions):** Discrete probability distribution over server room assignments:
    $$action = (prob_1, prob_2, \dots, prob_7, prob_{\text{nothing}})$$
    where $prob_i$ ($i \in \{1, \dots, 7\}$) represents the probability of assigning the DAG to room $i$, and $prob_{\text{nothing}}$ represents deferring assignment away from the current candidate data center. (Actor network output layer has 8 neurons, Table 1).  [Source: Sec. 7, p. 6; Eq. 13]
  - **Reward ($R_t$):** Delayed terminal reward evaluated when a scheduling episode/batch completes ($done = \text{true}$), formulated as relative multi-objective improvement over a baseline Round Robin + HEFT (RH) joint scheduler:
    $$reward = \begin{cases} \left(\frac{E(RH) - E(ERLFC)}{E(RH)} + \frac{EMI(RH) - EMI(ERLFC)}{EMI(RH)}\right) \times \vartheta & \text{if } done = \text{true} \\ 0 & \text{if } done = \text{false} \end{cases}$$
    where $E(\cdot)$ is total energy consumption, $EMI(\cdot)$ is total carbon emission, and $\vartheta$ is the reward amplification ratio (**Not stated in paper text; implemented as $\vartheta = 100$ in public source code**). The advantage function is evaluated by the critic as $A(\tau) = r_t - (V^{\pi_\theta}(s_t) - V^{\pi_\theta}(s_{t+1}))$.  [Source: Sec. 7, p. 6; Eq. 14]
  - **Neural Network Architecture & Training Details (Table 1):**
    - *Actor Network:* Fully connected layers: Input (39) $\to$ FC (64) $\to$ FC (128) $\to$ Output FC (8). Learning rate = $0.001$.
    - *Critic Network:* Fully connected layers: Input (39) $\to$ FC (64) $\to$ FC (128) $\to$ Output FC (1). Learning rate = $0.01$.
    - *Optimizer:* Adam. *Loss Function:* MSELoss.
    - *PPO Clipping Parameter:* $\epsilon = 0.2$ (Eq. 17).
    - *Discount Factor ($\gamma$):* Formulated in advantage function $A_t = r_t - (V(s_t) - V(s_{t+1}))$; implemented as $\gamma = 0.98$ in public source code (**Not stated in paper text**).
    - *Watermark Advance Rate ($wr$):* Formulated in Eq. 21; implemented as $wr = 0.25$ in public source code (**Not stated in paper text**).
- **Carbon / energy data source and region:**
  - *Server Power:* Single-server idle/standby power $P_{\text{idle}} = 0.15\text{ kW/h}$, single-server peak power $P_{\text{peak}} = 0.5\text{ kW/h}$ (Table 2).
  - *Cooling Power:* Air cooling ratio $cr = 0.0005$, liquid cooling ratio $cr = 0.2$; peak air cooling power $P_{\text{airPeak}} = 1.55\text{ kW/h}$; air-cooled starting power $P_{\text{airStart}} = 0.525\text{ kW}$; liquid cooling starting power $P_{\text{liquidStart}} = 1.5\text{ kW}$ (Table 2).
  - *Energy Sources & Static Emission Ratios ($ER$):* Modeled 6 data centers, each assigned a static primary energy type with a fixed, unitless carbon emission ratio:
    1. DC1: Fire energy (coal/thermal power), $ER = 0.6$
    2. DC2: Solar energy, $ER = 0.3$
    3. DC3: Wind energy, $ER = 0.1$
    4. DC4: Hydro energy, $ER = 0.3$
    5. DC5: Hydrogen energy, $ER = 0.2$
    6. DC6: Nuclear energy, $ER = 0.3$  [Source: Sec. 14 (Experimental setup), p. 8 / PDF p. 10; Table 2]
    *(Note on carbon intensity: The paper does not utilize dynamic grid carbon-intensity time series [$g\text{CO}_2/\text{kWh}$ from Electricity Maps, WattTime, or regional ISOs]; carbon emissions are calculated strictly via static multiplication $TEM = ER \times TEN$).*
- **Workload trace / dataset:** Real-world Google Cluster-usage traces [Ref. 55: Reiss & Wilkes, 2014], evaluated across three scales (Table 3, PDF p. 10):
  - *Dataset 1:* 1,633 DAG tasks, 43,940 subtasks (used for training and validation)
  - *Dataset 2:* 5,003 DAG tasks, 149,176 subtasks
  - *Dataset 3:* 15,195 DAG tasks, 472,658 subtasks
- **Simulator or real system:** Custom trace-driven discrete-event simulation testbed implemented in Python using PyTorch, modeling 6 geo-distributed data centers, 42 server rooms ($6 \times 7$), and 420 homogeneous physical servers ($6 \times 7 \times 10$). It is **not** evaluated on physical bare-metal hardware, production cloud instances, or Kubernetes clusters.
- **Baselines compared:**
  - *Round Robin (RR):* Round-robin selection of data centers and server rooms for task assignment.
  - *Random:* Random server room selection from a random data center (averaged over 10 iterations to ensure statistical stability).
  - *Snake Optimizer (SO):* Nature-inspired metaheuristic swarm optimization algorithm [Ref. 57: Hashim & Hussien, 2022] optimizing for energy, carbon emissions, and makespan.
  - *Golden Jackal Optimization (GJO):* Nature-inspired metaheuristic optimizer [Ref. 58: Chopra & Ansari, 2022] optimizing for energy, carbon emissions, and makespan.  [Source: Sec. 17, pp. 9–10 / PDF pp. 12–13]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Energy saving & emission reduction (Dataset 3: 15,195 DAGs) | Respective reductions of **1.09, 1.08, 1.21, and 1.26 times** in terms of energy saving and emission reduction | Round Robin, Random, SO, and GJO algorithms | Abstract, p. 1; Sec. 17, p. 10 / PDF p. 14; Sec. 18 (Conclusion), pp. 15–16 |
| Energy consumption ratio (Dataset 1: 1,633 DAGs) | Baseline algorithms consume **1.01, 1.06, 1.05, and 1.09 times** more energy compared to ERLFC | Round Robin (1.01x), Random (1.06x), SO (1.05x), GJO (1.09x) | Sec. 17, p. 10 / PDF pp. 13–14; Fig. 7 (p. 12) |
| Carbon emission ratio (Dataset 1: 1,633 DAGs) | Baseline algorithms emit **1.02, 1.06, 1.06, and 1.09 times** more carbon compared to ERLFC | Round Robin (1.02x), Random (1.06x), SO (1.06x), GJO (1.09x) | Sec. 17, p. 10 / PDF pp. 13–14; Fig. 7 (p. 12) |
| Energy consumption & emission ratio (Dataset 2: 5,003 DAGs) | Baseline algorithms consume and emit **1.10, 1.15, 1.24, and 1.26 times** more energy and emissions compared to ERLFC | Round Robin (1.10x), Random (1.15x), SO (1.24x), GJO (1.26x) | Sec. 17, p. 10 / PDF p. 14; Fig. 7 (p. 12) |
| Energy consumption & emission ratio (Dataset 3: 15,195 DAGs) | Baseline algorithms consume and emit **1.09, 1.08, 1.21, and 1.26 times** more energy and emissions compared to ERLFC | Round Robin (1.09x), Random (1.08x), SO (1.21x), GJO (1.26x) | Sec. 17, p. 10 / PDF p. 14; Fig. 7 (p. 12) |
| Workflow makespan | ERLFC achieves makespan performance competitive with/on par with baseline algorithms across all datasets; energy and emission reductions do not come at the expense of makespan | Round Robin, Random, SO, and GJO | Sec. 17, pp. 10–11 / PDF p. 13; Fig. 8 (p. 13) |
| Task delay / waiting time | Average task waiting times remain low under small workloads (Datasets 1 and 2); increases on Dataset 3 due to task concentration in low-emission data centers, but overall waiting time remains relatively small compared to baselines | Round Robin, Random, SO, and GJO | Sec. 17, pp. 11–12 / PDF pp. 14–15; Figs. 9–10 (pp. 14–15) |

## 5. Gap
- **Gap stated by the authors:**
  1. *Task Waiting Delay under Heavy Workload:* On large-scale workloads (Dataset 3 with 15,195 DAGs), the agent strategically concentrates tasks in data centers with lower energy consumption and carbon emission ratios, which leads to increased task queue waiting times.
  2. *Lack of Domain Specialization:* ERLFC is formulated as a general-purpose scheduler and is not yet tailored for specialized computing domains (such as AI model training, big-data pipelines, or graphics rendering).
  3. *Absence of Dynamic Server Shutdown / Sleep Modes:* The current infrastructure model assumes servers remain powered on in standby ($P_{\text{idle}} = 0.15\text{ kW}$) when idle; it does not implement dynamic power cycling, server sleep states, or server shutdown mechanisms in heterogeneous environments.  [Source: Sec. 17, pp. 11–12 / PDF pp. 14–15; Sec. 18 (Conclusion), p. 12 / PDF pp. 15–16]
- **Gap we observe:**
  1. *Synthetic, Static Carbon Emission Ratios:* The paper relies entirely on fixed, unitless carbon emission ratios (0.1–0.6) mapped statically to energy types rather than integrating empirical, time-varying grid marginal emissions factors ($g\text{CO}_2/\text{kWh}$ from Electricity Maps or WattTime).
  2. *Monolithic 100% Energy Source Assumptions:* Each data center is modeled as powered exclusively by a single energy source (e.g., DC2 is 100% solar, DC3 is 100% wind), completely ignoring diurnal intermittency, meteorological volatility, grid fuel-mix blending, and nighttime solar absence.
  3. *Simulation-Only Testbed:* The evaluation is conducted entirely inside a custom Python/PyTorch discrete simulation; it lacks validation on bare-metal clusters, production public clouds (AWS, GCP, Azure), or container orchestration platforms like Kubernetes.
  4. *Rigid Subtask Co-Location Constraint:* Mandating that all subtasks of a DAG must execute within a single server room eliminates inter-room networking costs, but creates severe resource bottlenecks and prevents multi-datacenter spatial parallelism for large enterprise DAGs whose resource footprint exceeds a single room's capacity (10 servers).
  5. *Homogeneous Server Hardware:* All 420 physical servers are modeled with identical CPU power characteristics ($P_{\text{idle}} = 0.15\text{ kW}$, $P_{\text{peak}} = 0.5\text{ kW}$), neglecting memory capacity limits, disk I/O contention, GPU/accelerator energy dynamics, and server architectural heterogeneity.
  6. *Absence of Energy Storage (BESS):* The framework does not incorporate Battery Energy Storage Systems (BESS) or thermal energy storage to store intermittent renewable energy during peak generation windows.

## 6. Relevance to our project
P17 is an essential core paper for Group G3 (RL / DRL for carbon-aware cloud workload scheduling) that demonstrates how multi-objective reinforcement learning can govern task scheduling across geographically distributed cloud federations. Key takeaways and methodological connections to our college project include:
1. **Multi-Tier Hierarchical Decision Making:** ERLFC proves that decoupling macro-spatial data center/room routing (via Actor-Critic RL) from micro-temporal server-level task assignment (via HEFT) prevents state-action space explosion while maintaining dependency awareness for DAG workflows.
2. **Co-Optimization of Compute and Infrastructure Cooling:** P17 highlights that IT compute power cannot be decoupled from cooling infrastructure energy, validating our project's inclusion of environmental and thermal factors.
3. **PPO for Cloud Scheduling Stability:** The use of clipped PPO ensures stable policy convergence even under irregular, bursty task arrivals from real-world Google traces.
4. **Concrete Research Gap to Exploit:** P17's primary limitation—reliance on static, unitless emission factors and 100% monolithic renewable allocations—provides direct motivation for our project. Our scheduler advances beyond P17 by querying real-time, dynamic marginal grid carbon-intensity time series ($g\text{CO}_2/\text{kWh}$) and accommodating fluctuating grid carbon dynamics in cloud scheduling decisions.
