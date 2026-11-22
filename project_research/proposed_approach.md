# Proposed Approach: Carbon-Aware Reinforcement Learning Scheduler

> [!IMPORTANT]
> **Status: Conceptual Research Direction (Pre-Implementation)**  
> This document outlines the proposed architectural direction derived from our Systematic Literature Review (SLR) findings across Groups G1, G2, and foundational literature. Final implementation details and algorithm selection will be established upon completion of the full 30-paper survey and candidate gap approval.

---

## 1. High-Level Concept
The proposed system aims to act as an intelligent, online workload dispatching and temporal buffering layer for cloud clusters. Positioned between incoming workload submission queues (e.g., Kubernetes admission or Slurm job queue) and physical/virtual computing nodes across one or more regions, the scheduler dynamically determines:
1. **When to execute** (temporal shifting within a permitted deadline flexibility window $\Delta t^{\max}$).
2. **Where to execute** (spatial routing to the cleanest available cluster among eligible regions).
3. **Resource provisioning level** (dynamic scaling or resource allocation to match low-carbon energy windows).

```text
[Incoming Cloud Workload Stream]
           │
           ▼
┌────────────────────────────────────────────────────────┐
│     Carbon-Aware RL Scheduling Agent (Policy π)        │
│                                                        │
│  State Inputs:                                         │
│  • Arriving Task Features (CPU/GPU, duration, deadline)│
│  • Current & Rolling Forecast Grid Carbon Intensity    │
│  • Cluster Queue Length & Server Utilization           │
│                                                        │
│  Decision Output:                                      │
│  • Action: [Defer by Δt] OR [Dispatch to Region m]    │
└────────────────────────────────────────────────────────┘
           │
           ├─────────────────────────────┐
           ▼                             ▼
┌───────────────────────┐   ┌──────────────────────────┐
│ Delay Buffer / Queue  │   │ Target Cloud Facility    │
│ (Holds flexible jobs  │   │ (Cluster 1 .. Cluster M) │
│  until carbon drops)  │   │ (Executes active jobs)   │
└───────────────────────┘   └──────────────────────────┘
```

---

## 2. Markov Decision Process (MDP) Modeling

### 2.1 State Space ($\mathcal{S}$)
At decision epoch $t$, state vector $s_t \in \mathcal{S}$ captures:
- **Workload Queue State:** Current backlog of pending flexible tasks, remaining time-to-deadline for each task ($d_i - t$), and resource demands ($\mathbf{r}_i$).
- **Carbon Intensity Signals:** Current marginal carbon intensity $C_m(t)$ across all candidate regions $m \in \mathcal{M}$, alongside short-term forecast delta vectors ($\hat{C}_m(t + \tau) - C_m(t)$ for $\tau \in \{1, 2, \dots, H\}$).
- **Cluster Resource State:** Real-time CPU, GPU, and memory utilization across active servers in each cluster.

### 2.2 Action Space ($\mathcal{A}$)
Depending on final architectural choice (discrete vs. continuous/parameterized action space):
- **Discrete Formulation (DQN / PPO):** Selecting an action tuple $a_t = \langle \text{Decision}, m \rangle$, where $\text{Decision} \in \{\text{Hold}_{\Delta t}, \text{Dispatch}\}$ and $m$ denotes target cluster.
- **Hierarchical Formulation:** A high-level agent determines the temporal flexibility window (how long to hold), and a low-level agent selects node/cluster mapping.

### 2.3 Reward Function ($\mathcal{R}$)
To balance competing objectives, the reward function penalizes operational emissions and latency/SLA breaches:
$$R_t = - \left( w_c \cdot \text{Emissions}_{\text{step}}(t) + w_d \cdot \text{Penalty}_{\text{deadline}}(t) + w_m \cdot \text{Cost}_{\text{migration}}(t) \right)$$
- If a task finishes cleanly within its flexibility window during a low-carbon valley, carbon emissions are minimized and deadline penalty is zero.
- If the agent defers a task too long and risks breaching the deadline, $\text{Penalty}_{\text{deadline}}$ grows steeply, forcing timely execution.

---

## 3. Candidate RL Algorithms Under Consideration
Derived from our analysis of Groups G2 and G3:
1. **Proximal Policy Optimization (PPO):** Stable on-policy actor-critic algorithm well-suited for high-dimensional, continuous-discrete state features and multi-objective rewards (demonstrated effective in P09).
2. **Double Deep Q-Network (Double DQN):** Value-based approach with action decomposition for discrete dispatching and queuing decisions (demonstrated effective in P08 and F04).
3. **Hierarchical / Multi-Agent RL (H-MARL):** Coarse-grained regional selection decoupled from fine-grained local server scheduling.

---

## 4. Planned Validation Framework
- **Simulation Environment:** Discrete-event simulation using **Vessim** (Wiesner et al., HotCarbon '24) or **CloudSim Plus**, enabling direct ingestion of real-world carbon traces.
- **Carbon Data:** Historical 2020–2024 hourly and 5-minute carbon intensity traces from CAISO (California), ENTSO-E (Germany/France), and National Grid ESO (UK).
- **Workload Traces:** Google Borg 2019/2020 cluster traces and Alibaba 2021 microservice traces.
- **Baselines for Benchmarking:**
  - Standard FIFO / Immediate execution (carbon-agnostic).
  - Fixed-window nighttime heuristic (static temporal shifting).
  - Single/Double Threshold carbon heuristics (ST/DT from P07).
  - Perfect foresight optimal upper bound.
