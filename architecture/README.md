# System Architecture Documentation

> [!NOTE]
> **Status: Architectural Scoping & Specification (Pre-Implementation)**  
> This directory documents the candidate system architecture, interface specifications, and simulation testbed designs under evaluation for our carbon-aware reinforcement learning scheduler.

---

## 1. Candidate Architecture Overview
The scheduler is conceived as a modular, discrete-time controller operating across three primary decoupled modules:

```text
┌─────────────────────────────────────────────────────────────┐
│                   1. Workload Ingestion                     │
│  - Parses arriving task descriptors                         │
│  - Extracts resource demands (CPU/GPU/RAM) and deadlines    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│               2. Carbon Telemetry & Forecasting             │
│  - Ingests real-time marginal carbon signals (MOER)         │
│  - Computes forecast deltas over lookahead horizon H        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│             3. RL Decision Engine (Policy π)                │
│  - Evaluates current system state (Queue + Carbon + Nodes)  │
│  - Selects action: [Buffer Task] or [Dispatch to Cluster m] │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│             4. Cluster Execution / Simulation               │
│  - Manages server queues, active execution & completion     │
│  - Tracks energy draw, carbon emissions & SLA compliance    │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Key Interfaces (Proposed)

### 2.1 Task Submission Interface
- `submit_task(task_id, cpu_req, mem_req, duration, deadline, max_delay)`
- Enqueues incoming jobs into the scheduler's candidate buffer.

### 2.2 Carbon Oracle Interface
- `get_current_carbon(region_id) -> float`
- `get_carbon_forecast(region_id, horizon_steps) -> List[float]`
- Queries cached or live regional carbon intensity feeds.

### 2.3 RL Environment (Gymnasium Interface)
- `step(action) -> (observation, reward, terminated, truncated, info)`
- `reset() -> (observation, info)`
- Standardized reinforcement learning loop compliant with Farama Foundation Gymnasium.

---

## 3. Implementation Roadmap
Detailed module implementations, agent policy definitions, and test harness code will be placed in this directory upon completion and faculty approval of the Systematic Literature Review.
