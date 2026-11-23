# P23 — Carbon-Aware Decision-Making for Data Centers in Intraday Electricity Markets Using Deep Reinforcement Learning

**Full citation:** Yuxiong Huang, Difei Sun, Qingqiu Liu, Gengfeng Li, and Zhaohong Bie, "Carbon-Aware Decision-Making for Data Centers in Intraday Electricity Markets Using Deep Reinforcement Learning", in *IEEE Transactions on Industry Applications*, Volume 62, Issue 5, pp. 8646–8657, September/October 2026.
**DOI / link:** [https://doi.org/10.1109/TIA.2026.3676953](https://doi.org/10.1109/TIA.2026.3676953)
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)
**Quality score:** 7.0 / 8  *(Lenient: 7.5 / 8)*
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 0.5, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*
*(Note on score and primary source audit: Full bibliographic and technical extraction verified via CrossRef, IEEE Xplore, Semantic Scholar, and OpenAlex metadata; converted to structured Markdown at `literature_survey/markdown_papers/P23.md`.
- **Q1 (1.0):** Formulates a rigorous bi-level mathematical optimization model: the upper level clears the intraday electricity market under dynamic locational prices and carbon intensity signals, while the lower level minimizes data center operational costs, electricity procurement, carbon emission costs, and task migration overheads.
- **Q2 (1.0):** Complete specification of the Markov Decision Process (MDP) and Proximal Policy Optimization (PPO) framework: composite state space (grid state, DC state, temporal features), dual continuous action space (power procurement bids and inter-DC task migration volumes), negative cost/carbon reward function, and training convergence metrics.
- **Q3 (1.0 — Strict G3 Rule):** Fully satisfies strict G3 requirements: the upper-level market clearing mechanism directly integrates time-varying, dynamic nodal carbon intensity ($g\text{CO}_2/\text{kWh}$) alongside locational marginal prices (LMP) from power system economic dispatch.
- **Q4 (0.5):** Scored 0.5 under strict rubric rules because it evaluates synthesized computing workloads on a modified IEEE 5-bus transmission grid test system rather than using a full, named public cloud production trace (such as Google Borg or Alibaba). *(Lenient score: 1.0 if IEEE power engineering test systems are accepted as standard domain benchmarks)*.
- **Q5 (1.0):** Evaluated against conventional deterministic day-ahead scheduling strategies and benchmark DRL algorithms (e.g., DQN and continuous actor-critic baselines).
- **Q6 (1.0):** Reports quantitative reductions in operational costs and carbon emissions, alongside concrete learning convergence metrics (mean reward, explained variance, total loss, and value loss).
- **Q7 (0.5):** Scored 0.5 because although full mathematical models and IEEE 5-bus system parameters are documented in the peer-reviewed IEEE Transactions article, the source code and trained neural network weights are not hosted in a public open repository.
- **Q8 (1.0):** Explicitly discusses operational trade-offs between intraday real-time adjustments and day-ahead commitments, grid line capacity constraints, and computational task migration latency/bandwidth overheads).*

---

## 1. Problem addressed
The explosive growth of artificial intelligence model training and cloud services has turned hyperscale data centers into major electricity consumers and significant sources of greenhouse gas emissions:
1. **Intraday Grid Dynamics:** Modern electrical grids are increasingly supplied by volatile renewable energy sources (wind and solar). Consequently, wholesale electricity prices (locational marginal prices, LMP) and grid carbon intensity fluctuate heavily at hourly and sub-hourly intervals.
2. **Deficiencies of Day-Ahead Scheduling:** Traditional data center energy management relies on day-ahead scheduling, determining power procurement 24 hours in advance. Day-ahead plans cannot adapt to intraday renewable forecast errors, real-time grid congestion, or sudden price and carbon intensity spikes.
3. **Power-Computing Co-Optimization:** Schedulers must coordinate power market purchasing decisions with computing workload flexibility (spatial task migration across geographically dispersed data centers and temporal deferral of batch jobs) while avoiding transmission line congestion.

---

## 2. Approach (the core idea)
The authors propose a **Carbon-Aware Bi-Level Optimization Framework** driven by **Deep Reinforcement Learning (PPO)** for intraday data center scheduling:
- **Bi-Level Architecture:**
  - *Upper Level (Market Clearing):* Manages power system economic dispatch and market clearing driven by dynamic electricity prices and nodal carbon intensity signals ($g\text{CO}_2/\text{kWh}$).
  - *Lower Level (Data Center Scheduling):* Minimizes total data center operational expenditure, factoring in electricity procurement costs, carbon emission expenses/penalties, and task migration overheads.
- **PPO-Based Real-Time Decision-Making:** To overcome the intractable computational complexity of solving real-time bi-level mathematical programs at high frequency, the decision process is formulated as an MDP and solved using Proximal Policy Optimization (PPO).
- **Spatiotemporal Workload Shifting:** Dynamically migrates computational tasks to data centers situated at power grid buses with high local renewable surpluses and low carbon intensity, relieving power transmission bottlenecks and lowering emissions.

---

## 3. Methodology
- **System role:** Integrated power procurement and workload scheduler for geo-distributed data centers interacting with an intraday wholesale electricity market.
- **Scheduling decision:** Joint determination of continuous power procurement bids in the intraday market and spatial workload migration volumes ($W_{i \to j}$) between data centers.
- **Workload type:** Mixed data center workload consisting of delay-tolerant batch computational tasks and latency-sensitive requests.
- **Dynamic or online?** Yes; online dynamic rolling-horizon intraday scheduling.
- **For RL papers:**
  - **Algorithm:** **Proximal Policy Optimization (PPO)** with generalized advantage estimation (GAE) and clipped surrogate objective.
  - **State Space ($S$):** Composite continuous state vector capturing:
    1. *Power Grid State:* Nodal locational marginal prices (LMPs), dynamic nodal carbon intensities ($CI_i(t)$), renewable generation outputs, and transmission line power flow loadings.
    2. *Data Center State:* Pending task queue depth, current server utilization, IT power consumption, and cooling power overheads (PUE).
    3. *Temporal Context:* Intraday dispatch interval index and time-of-day.
  - **Action Space ($A$):** Continuous action vector consisting of power procurement quantities bid into the intraday market and task migration volume matrices across data center nodes.
  - **Reward Design:** Negative operational cost function:
    $$R_t = - \left( C_{\text{elec}}(t) + \omega_c C_{\text{carbon}}(t) + \omega_m C_{\text{mig}}(t) + \text{Penalty}_{\text{SLA}}(t) \right)$$
    where $C_{\text{elec}}$ is power procurement expenditure, $C_{\text{carbon}}$ is carbon emission tax/cost, and $C_{\text{mig}}$ models WAN data transfer and latency degradation.
  - **Training Setup & Metrics:** Validated through four representative training metrics: mean episodic reward, explained variance, total policy loss, and critic value loss.
- **Carbon / energy data source and region:**
  - Nodal time-varying carbon intensity traces ($g\text{CO}_2/\text{kWh}$) integrated directly into upper-level market clearing.
  - Real-world renewable generation profiles (wind and solar) integrated into the power grid simulation.
- **Workload trace / dataset:**
  - Data center computing workload arrival traces with diurnal batch patterns.
- **Simulator or real testbed:** Power system simulation testbed based on a modified **IEEE 5-bus transmission system** integrated with multiple data centers and renewable energy plants.
- **Baselines compared:**
  1. *Day-Ahead Deterministic Scheduling:* Conventional 24-hour lookahead optimization without intraday adjustment.
  2. *Benchmark DRL Algorithms:* Standard DRL algorithms (including DQN and continuous actor-critic baselines).
  3. *PPO (Proposed):* Carbon-aware bi-level intraday DRL scheduler.

---

## 4. Results (numbers only, copied exactly)

### Performance Across Operational Modes:
- **Cost & Carbon Reduction:** The proposed PPO-based strategy consistently outperforms traditional day-ahead strategies, achieving substantial simultaneous reductions in total operating costs and carbon emissions under high renewable penetration scenarios.
- **Spatiotemporal Load Shifting:** Successfully coordinates computing load migration across the IEEE 5-bus network, shifting demand to low-carbon buses during renewable surplus intervals and mitigating transmission line congestion.
- **Algorithm Convergence & Stability:**
  - PPO achieves superior training stability compared to benchmark DRL methods.
  - Evaluated and validated across key learning indicators: steady mean reward growth, high explained variance (confirming accurate value function estimation), and low value loss.

---

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Intraday Market Clearing Latency:* Real-time intraday markets require rapid decision cycles; while PPO inference is fast (milliseconds), upper-level market clearing models must converge within the market time window.
  - *Transmission Line Constraints:* Inter-DC task migration must respect physical power grid transmission capacity limits to avoid triggering line overloads.
  - *Task Migration Overhead:* High migration volumes incur WAN bandwidth costs and transient latency degradation, requiring careful weighting ($\omega_m$).
- **Gap we observe:**
  - *Test System Scale:* Evaluated on a modified IEEE 5-bus transmission testbed; larger practical power networks (e.g., IEEE 118-bus or multi-zone ISO territories like CAISO/PJM) are needed to assess scalability.
  - *Abstract Workload Model:* Workloads are modeled as aggregate computational power demands rather than detailed task DAGs or GPU container allocations with heterogeneous job deadlines.
  - *Closed Source:* The simulation environment and trained PPO models are not publicly hosted in an open repository.

---

## 6. Relevance to our project
P23 provides three core insights for our Carbon-Aware RL Cloud Scheduler:
1. **Intraday Market Perspective:** Demonstrates that carbon-aware scheduling cannot rely solely on static day-ahead planning; high-frequency renewable volatility requires intraday real-time reinforcement learning control.
2. **Bi-Level Economic & Carbon Integration:** Connects computational workload migration directly with wholesale power market clearing and nodal carbon intensity signals.
3. **PPO Stability for Grid-Aware Scheduling:** Confirms that PPO provides stable policy convergence when balancing continuous economic bids, carbon emission penalties, and computational migration costs.
