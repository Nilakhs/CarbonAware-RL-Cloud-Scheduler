# Problem Statement: Carbon-Aware Reinforcement Learning Scheduler for Dynamic Cloud Workloads

## 1. Context and Motivation
Data center electricity demand has surged due to the rapid growth of large-scale cloud services, big data analytics, and generative AI workloads. Grid carbon intensity—the mass of CO2 emitted per unit of electricity generated ($gCO_2/kWh$)—fluctuates significantly across hours of the day (temporal variance driven by solar and wind availability) and across geographic regions (spatial variance driven by local grid generation mixes). 

Traditional cloud schedulers optimize primarily for:
- Resource utilization (CPU, memory, storage)
- Task completion time / makespan
- Operating cost and power usage effectiveness (PUE)
- Service Level Agreements (SLAs) and strict deadline compliance

However, carbon-agnostic scheduling results in running energy-intensive batch jobs during peak carbon-intensity hours (e.g., when coal or natural gas peaker plants are dispatched) or in carbon-intensive geographical zones.

## 2. Research Problem Formulation
The goal of this research project is to design, implement, and evaluate an online, **Carbon-Aware Reinforcement Learning (RL) Scheduler** capable of dynamically dispatching arriving cloud workloads across time (temporal shifting) and/or across heterogeneous clusters/regions (spatial shifting).

### Key Dynamics and Complexities:
1. **Dynamic Job Arrivals:** Workloads arrive stochastically without full a priori knowledge of future arrival rates, durations, or resource profiles.
2. **Volatile Carbon Intensity:** Regional grid carbon signals vary dynamically; while forecasts exist (e.g., Electricity Maps, WattTime), forecast errors can lead naive schedulers to miss greener windows.
3. **Multi-Objective Trade-Offs:** Minimizing total carbon emissions frequently conflicts with quality-of-service metrics:
   - Delaying batch workloads reduces carbon but risks deadline violations and queue buffer overflows.
   - Migrating jobs across geographic regions incurs network transfer overheads, latency penalties, and data-residency compliance boundaries.
4. **Action Space & Online Feasibility:** Reinforcement learning agents must operate on realistic state representations (queue length, current carbon intensity, forecast delta, node utilization) and output valid scheduling actions (dispatch node, delay duration, scaling factor) within millisecond decision bounds.

## 3. Scope of the College-Level Course Project
This literature survey will establish:
- Which formulations (MDP / POMDP / MARL) have been rigorously tested.
- What realistic simulation environments (e.g., CloudSim, SimGrid, Vessim, Grid5000) and real workload traces (e.g., Google Cluster Traces, Alibaba Trace, Azure Functions) enable fair empirical comparison.
- Which research gaps are both significant and technically feasible to execute within a single-semester course timeline.
