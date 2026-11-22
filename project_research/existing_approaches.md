# Existing Approaches in Carbon-Aware and RL Cloud Scheduling

*Note: This working document synthesizes the architectural paradigms identified across the survey groups (G1 through G5).*

## 1. Non-RL Carbon-Aware Schedulers (G1)
- **Heuristic Workload Shifting:** Delay-tolerant batch workloads are deferred based on static carbon thresholds or predicted carbon minimums (e.g., Wiesner et al., "Let's Wait Awhile", Middleware 2021).
- **Optimization and Mathematical Programming:** Formulation of workload scheduling as Integer Linear Programming (ILP) or Mixed Integer Linear Programming (MILP) to minimize carbon emissions subject to deadlines (e.g., Radovanović et al., Google 2022).
- **Virtualization & Abstraction Frameworks:** Frameworks that expose carbon cost to software stacks and orchestrate elastic scaling according to grid signals (e.g., Acun et al., Carbon Explorer, ASPLOS 2023; Hanafy et al., CarbonScaler, SIGMETRICS 2023).

## 2. RL for Cloud Resource Management (G2)
- **Energy and Cost Minimization:** Deep Q-Networks (DQN) and Policy Gradient (PPO, A3C) algorithms applied to VM placement, dynamic voltage and frequency scaling (DVFS), and server consolidation.
- **Performance-Centric Cluster Schedulers:** DeepRM (Mao et al., HotNets 2016) and Decima (Mao et al., SIGCOMM 2019) demonstrated that DRL can learn state-action mappings for complex DAG job graphs and heterogeneous clusters.

## 3. RL for Carbon-Aware Scheduling (G3)
- Emerging literature where the RL reward function explicitly incorporates carbon emissions alongside SLA penalties.
- Paradigms include:
  - Single-agent actor-critic models balancing carbon savings vs. completion times.
  - Multi-agent reinforcement learning (MARL) where distributed cluster managers negotiate workload migration.
  - Hierarchical RL combining coarse-grained temporal window selection with fine-grained node placement.

## 4. Carbon Forecasting and Data Sources (G4)
- Regional marginal vs. average carbon intensity signals (Electricity Maps API, WattTime API, national ISO/RTO feeds).
- Multi-day and short-term carbon forecasting models (e.g., Maji et al., CarbonCast, ACM BuildSys 2022).

## 5. Simulators and Workload Traces (G5)
- Standard cluster traces: Google Borg cluster traces, Alibaba cluster trace datasets, Azure VM/Functions traces.
- Carbon and energy simulators: Vessim, CloudSim Plus, SimGrid/BatSim, GreenCloud.
