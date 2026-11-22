# Formal Problem Statement: Carbon-Aware Reinforcement Learning Scheduler for Dynamic Cloud Workloads

## 1. Context and Problem Scoping
Data center electricity demand has surged due to the rapid growth of large-scale cloud services, big data pipelines, and generative AI workloads. Electricity grid carbon intensity—the mass of equivalent $\text{CO}_2$ emitted per unit of electrical energy generated ($g\text{CO}_2/\text{kWh}$)—fluctuates substantially across temporal and geographic dimensions. 

Conventional cloud scheduling systems (such as Kubernetes, Slurm, or Borg) optimize primarily for:
- Cluster resource utilization (CPU, GPU, memory, disk I/O)
- Job makespan and queuing latency
- Operating expenditure and Power Usage Effectiveness (PUE)
- Service Level Agreements (SLAs) and strict deadline compliance

Because standard schedulers are carbon-agnostic, energy-intensive computational jobs are frequently scheduled during peak carbon-intensity intervals (e.g., when fossil peaker plants are activated) or dispatched to carbon-heavy geographic regions, incurring substantial avoidable operational emissions.

---

## 2. Mathematical Problem Formulation

### 2.1 System Model
Consider a distributed cloud environment comprising $M$ geographically separated computing facilities (clusters or regions) denoted by $\mathcal{M} = \{1, 2, \dots, M\}$. Each facility $m \in \mathcal{M}$ is connected to a local electrical grid characterized by time-varying marginal carbon intensity $C_m(t)$ ($g\text{CO}_2/\text{kWh}$) at time step $t$.

Workloads arrive dynamically as a sequence of computational tasks/jobs $\mathcal{J} = \{J_1, J_2, \dots\}$. Each job $J_i$ is formally defined by the tuple:
$$J_i = \langle a_i, d_i, w_i, \mathbf{r}_i, \Delta t_i^{\max}, \mathcal{L}_i \rangle$$
where:
- $a_i$: Arrival timestamp of the job.
- $d_i$: Strict completion deadline ($d_i \ge a_i + w_i$).
- $w_i$: Nominal execution duration under allocated hardware resources.
- $\mathbf{r}_i = \langle c_i, g_i, m_i \rangle$: Required computational resources (CPU cores, GPUs, memory).
- $\Delta t_i^{\max}$: Maximum permissible temporal delay/deferral flexibility window ($\Delta t_i^{\max} \le d_i - a_i - w_i$).
- $\mathcal{L}_i \subseteq \mathcal{M}$: Set of eligible geographic regions satisfying data-residency and network latency constraints.

### 2.2 Operational Carbon Emission Model
The instantaneous electrical power consumed by executing task $J_i$ in region $m$ at time $t$ is given by $P_{i,m}(t)$ (kW). The total operational carbon footprint $E_{\text{carbon}}$ of scheduling decision policy $\pi$ over time horizon $T$ is formulated as:
$$E_{\text{carbon}} = \sum_{t=1}^T \sum_{m \in \mathcal{M}} \sum_{J_i \in \mathcal{A}_m(t)} P_{i,m}(t) \cdot C_m(t) \cdot \Delta t$$
where $\mathcal{A}_m(t)$ is the set of active jobs executing in facility $m$ during interval $[t, t + \Delta t]$.

### 2.3 Optimization Objective
The objective is to synthesize a scheduling policy $\pi^*$ that minimizes total operational carbon emissions while bounding SLA deadline infractions and migration costs:
$$\min_{\pi} \left[ E_{\text{carbon}} + \lambda_{\text{SLA}} \sum_{J_i \in \mathcal{J}} \max(0, f_i - d_i) + \lambda_{\text{net}} \sum_{J_i \in \mathcal{J}} \text{Cost}_{\text{migration}}(J_i) \right]$$
subject to:
1. **Deadline and Flexibility Constraints:**
   $$f_i \le d_i, \quad \forall J_i \in \mathcal{J}_{\text{strict}}$$
   $$s_i \in [a_i, a_i + \Delta t_i^{\max}], \quad \forall J_i \in \mathcal{J}_{\text{flexible}}$$
   where $s_i$ is task start time and $f_i = s_i + w_i$ is task finish time.
2. **Cluster Capacity Constraints:**
   $$\sum_{J_i \in \mathcal{A}_m(t)} \mathbf{r}_i \le \mathbf{R}_m(t), \quad \forall m \in \mathcal{M}, \forall t$$
   where $\mathbf{R}_m(t)$ denotes total available resources in facility $m$.
3. **Data Residency and Network Latency Constraints:**
   $$m_i \in \mathcal{L}_i, \quad \forall J_i \in \mathcal{J}$$

---

## 3. Key Dynamics and Complexities

1. **Stochastic Job Arrivals:** Workloads arrive dynamically according to non-stationary distributions without full a priori foresight of future arrival rates, job lengths, or resource claims.
2. **Grid Carbon Non-Stationarity & Forecast Uncertainty:** While regional grid operators provide forecasts (e.g., via WattTime or Electricity Maps), real-world forecast errors frequently range from $10\%$ to $30\%$, particularly during rapid weather transitions affecting renewable ramps. Schedulers must be robust against forecast drift.
3. **Multi-Objective Trade-Off Conflicts:**
   - **Temporal Deferral vs. Queue Contention:** Postponing delay-tolerant batch tasks until green generation peaks can create severe resource contention and queue buffer overflows if arrival spikes coincide with renewable lulls.
   - **Spatial Migration vs. WAN Egress Overhead:** Migrating tasks across regions reduces operational carbon but introduces network transmission delays, WAN energy consumption, and egress bandwidth costs.
4. **Online Decision Feasibility:** The scheduling policy must execute within millisecond decision bounds per task arrival epoch, ruling out heavyweight global offline optimization (e.g., high-dimensional MILP) during runtime operation.

---

## 4. Scope and Feasibility Boundaries for the Course Project
This project deliberately bounds its scope to deliver rigorous, reproducible academic outcomes within a single academic semester:
- **Focus:** Online dynamic scheduling of batch and flexible cloud compute workloads.
- **Formulation:** Discrete-time Markov Decision Process (MDP) with reinforcement learning agents.
- **Evaluation:** Evaluated on realistic, trace-driven simulation testbeds (e.g., Vessim, CloudSim Plus) driven by empirical public cloud traces (Google Borg, Alibaba) and historical grid carbon traces (CAISO, ENTSO-E, RTE).
- **Exclusions:** Physical data center hardware modifications, liquid cooling infrastructure alterations, and live multi-cloud commercial cluster orchestration are out of scope.
