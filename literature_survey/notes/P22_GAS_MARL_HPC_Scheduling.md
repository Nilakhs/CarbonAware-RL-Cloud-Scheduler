# P22 — GAS-MARL: Green-Aware job Scheduling algorithm for HPC clusters based on Multi-Action Deep Reinforcement Learning

**Full citation:** Rui Chen, Weiwei Lin, Huikang Huang, Xiaoying Ye, and Zhiping Peng, "GAS-MARL: Green-Aware job Scheduling algorithm for HPC clusters based on Multi-Action Deep Reinforcement Learning", in *Future Generation Computer Systems*, Volume 167, Page 107760, June 2025.
**DOI / link:** [https://doi.org/10.1016/j.future.2025.107760](https://doi.org/10.1016/j.future.2025.107760) (ScienceDirect PII: `S0167-739X(25)00055-X`)
**Open-source repository:** [https://github.com/sioncr/green-rl-sched](https://github.com/sioncr/green-rl-sched)
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)
**Quality score:** 7.5 / 8
*(Q1: 1.0, Q2: 1.0, Q3: 0.5, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*
*(Note on score and primary source audit: Full open-source implementation, simulator, neural architectures, configuration files, and evaluation scripts audited directly from the authors' GitHub repository `sioncr/green-rl-sched`; converted to structured Markdown at `literature_survey/markdown_papers/P22.md`.
- **Q1 (1.0):** Formulates a rigorous cluster job scheduling optimization model balancing renewable energy utilization against average bounded slowdown in high-performance computing (HPC) clusters co-located with on-site renewable generation.
- **Q2 (1.0):** Comprehensive description of the Multi-Action DRL algorithm: multi-encoder neural architecture, detailed 2,752-dimensional composite observation vector, coordinated two-stage action space (Action 1 for job selection, Action 2 for delay/timing decisions), dynamic action masking, and the Green-Backfilling heuristic.
- **Q3 (0.5 — Strict G3 Rule):** Evaluated against empirical meteorological renewable traces (hourly wind speed and solar irradiance datasets from Laurent Philippe's `greenpower` library) driving physical wind turbine and solar PV production models. Scored strictly 0.5 because it models on-site renewable power matching ($U_{\text{green}}$) rather than ingesting dynamic grid marginal carbon intensity time series ($g\text{CO}_2/\text{kWh}$) from official balancing authority APIs.
- **Q4 (1.0):** Employs standard production HPC cluster traces from the Feitelson Parallel Workloads Archive (SDSC SP2 `Cirne.swf` and LLNL T3D `Jann.swf`) alongside synthetic Lublin99 cluster workloads (`lublin_256.swf`).
- **Q5 (1.0):** Compares against five distinct baselines across multiple paradigms: FCFS, Shortest-Job-First heuristic (F2/WFP3), Longest Processing Time heuristic (LPTPN), Genetic Algorithm (GA), and state-of-the-art single-action Maskable PPO, plus backfilling ablations (No-backfill, EASY-backfill, Green-backfill).
- **Q6 (1.0):** Quantitative experimental results evaluated over 10 independent test episodes with 1,024-job sequences, reporting average bounded slowdown, renewable energy utilization, and execution overheads.
- **Q7 (1.0):** Fully reproducible open science: the authors provide the complete source code, PyTorch network definitions, simulation engine, configuration files, and datasets in a public GitHub repository (`https://github.com/sioncr/green-rl-sched`).
- **Q8 (1.0):** Authors explicitly analyze the operational trade-offs between bounded slowdown penalties and renewable energy utilization, discrete delay selection bounds ($DS \le 3,600$ s), and single-cluster operational constraints).*

---

## 1. Problem addressed
High-Performance Computing (HPC) clusters provide essential compute infrastructure for large-scale scientific simulations, weather forecasting, and machine learning. However, modern supercomputing centers consume megawatts of electricity and generate substantial carbon footprints:
1. **Renewable Energy Intermittency:** Co-locating HPC clusters with on-site renewable generation (e.g., wind turbines and photovoltaic panels) creates volatile, weather-dependent power supply curves.
2. **Shortcomings of Traditional HPC Schedulers:** Conventional HPC cluster schedulers (e.g., Slurm, PBS, Maui) prioritize user-facing performance metrics—specifically job turnaround time, wait time, and average bounded slowdown—using priority queues and backfilling policies (such as EASY-Backfilling). They are completely oblivious to real-time renewable energy availability.
3. **Flaws in Single-Action DRL Schedulers:** Prior deep reinforcement learning schedulers for cloud and HPC environments (such as DeepJS and Decima) operate under a single-action paradigm: the agent selects a job from the waiting queue and immediately dispatches it to available cluster nodes. If the cluster is currently in a renewable power trough, immediate execution forces high brown (grid fossil) electricity consumption.
4. **The Performance-Sustainability Conflict:** Indiscriminately deferring jobs to wait for green energy creates queue head-of-line blocking, spikes bounded slowdown, and breaches user service-level expectations. A green scheduler must intelligently decouple *which* job to schedule from *when* to execute it.

---

## 2. Approach (the core idea)
The authors introduce **GAS-MARL** (Green-Aware job Scheduling algorithm based on Multi-Action Deep Reinforcement Learning) to optimize both renewable energy utilization and job execution efficiency:
- **Multi-Action Decision Framework:** In each decision epoch, the agent executes two coordinated actions:
  - **Action 1 (Job Selection):** Selects which job from the waiting queue ($MAX\_QUEUE\_SIZE = 256$) should be scheduled, constrained by a boolean resource-feasibility mask.
  - **Action 2 (Delay / Timing Decision):** Determines whether to execute immediately, wait for running jobs to release nodes (resource-release delay), or delay execution for a discrete duration (green-power delay) to align with upcoming renewable energy peaks.
- **Green-Backfilling Heuristic:** During delay windows where compute nodes would otherwise sit idle, Green-Backfilling permits smaller, lower-power jobs from the queue to utilize idle processors, provided they complete before the delayed primary job's reserved start time.
- **Conditioned Multi-Encoder Neural Architecture:** Employs three parallel sub-encoders (`JobEncoder`, `RunningJobEncoder`, `GreenEncoder`) and conditions Action 2 directly on an embedding of the job selected by Action 1 (`JobEmbedding`).
- **Composite Multi-Objective Reward:** Combines a performance penalty (negative bounded slowdown) with a green energy utilization reward ($U_{\text{green}} = E_{\text{green}} / E_{\text{total}}$), scaled by a tuning factor $\eta = 0.002$.

---

## 3. Methodology
- **System role:** Batch job scheduler for High-Performance Computing (HPC) clusters powered by hybrid green/brown power.
- **Scheduling decision:** Coordinated two-stage decision $(a_1, a_2)$: selecting a candidate job from the queue ($a_1$) and selecting an execution timing modality ($a_2 \in \{0, \text{resource delay}, \text{green delay}\}$).
- **Workload type:** Non-preemptive parallel batch HPC jobs with explicit processor requirements and requested wall-clock runtimes.
- **Dynamic or online?** Yes; online dynamic event-driven scheduling triggered by job arrivals and completions.
- **For RL papers:**
  - **Algorithm:** Multi-Action Proximal Policy Optimization (**Maskable PPO with Dual Action Heads**) with generalized advantage estimation (GAE) and dynamic action masking.
  - **State Space ($S$):** Composite observation vector of dimension $(MAX\_QUEUE\_SIZE + run\_win + green\_win) \times JOB\_FEATURES = (256 + 64 + 24) \times 8 = 2,752$ dimensions:
    1. *Waiting Queue Subvector ($256 \times 8$):* Normalized wait time $(t - r_i) / MAX\_WAIT\_TIME$, normalized request runtime $\tau_i^{\text{req}} / \max\_exec\_time$, normalized processor demand $m_i / \max\_procs$, normalized total power $P_i / MAX\_POWER$, normalized per-processor power $(P_i / m_i) / MAX\_perProcPower$, estimated brown energy increment $\Delta E_{\text{brown}}$, estimated green energy increment $\Delta E_{\text{green}}$, and node allocatability flag.
    2. *Running Jobs Subvector ($64 \times 8$):* Allocated processors ratio, total power, per-processor power, remaining runtime $(\text{scheduled\_time} + \tau_i - t) / \max\_exec\_time$, and zero-padding.
    3. *Renewable Power Profile ($24 \times 8$):* 24 hourly lookahead slots containing slot duration and predicted renewable power in Watts (normalized to $MAX\_GREEN = 19,000$ W).
  - **Action Space ($A$):**
    - $a_1 \in \{0, \dots, 255\}$ (selects candidate job from waiting queue).
    - $a_2 \in \{0, \dots, |DS| + delayMaxJobNum\}$ (where $delayMaxJobNum = 5$, $|DS| = 7$):
      - $a_2 = 0$: Immediate execution.
      - $a_2 \in \{1, \dots, 5\}$: Wait for $a_2$-th running job to finish.
      - $a_2 \in \{6, \dots, 12\}$: Delay job execution by discrete duration $DS \in [300, 600, 1200, 1800, 2400, 3000, 3600]$ seconds.
  - **Reward Design:**
    $$R = \eta \cdot r_{\text{perf}} + U_{\text{green}}$$
    where $r_{\text{perf}} = - \text{bsld}(j) = - \max\left(1.0, \frac{C_j - r_j}{\max(\tau_j, 10)}\right)$, $U_{\text{green}} = \frac{E_{\text{green}}}{E_{\text{total}}} = \frac{\sum \text{usedGreen}}{\sum \text{totalEnergy}}$, and $\eta = 0.002$.
  - **Neural Network Architecture:**
    - `JobEncoder`: MLP [in $\rightarrow$ 64 $\rightarrow$ ReLU $\rightarrow$ 128 $\rightarrow$ ReLU].
    - `RunningJobEncoder`: MLP [in $\rightarrow$ 64 $\rightarrow$ ReLU $\rightarrow$ 128 $\rightarrow$ ReLU].
    - `GreenEncoder`: MLP [in $\rightarrow$ 64 $\rightarrow$ ReLU $\rightarrow$ 128 $\rightarrow$ ReLU].
    - `Decoder 1`: Linear [128 $\rightarrow$ 64 $\rightarrow$ 16 $\rightarrow$ 1] with softmax over valid queue positions.
    - `JobEmbedding`: Linear [8 $\rightarrow$ 128] embedding the selected job.
    - `Decoder 2`: Concatenates all encoders and selected job embedding $\rightarrow$ MLP [64 $\rightarrow$ 13] with softmax over valid delay options.
    - `CriticNet`: Evaluates state value $V(s)$ from multi-encoder latent representations.
  - **Training Setup:** Batch size 256, Adam optimizer, entropy regularization, clipped surrogate PPO objective.
- **Carbon / energy data source and region:**
  - On-site hybrid renewable energy generation modeled via Laurent Philippe's `greenpower` library.
  - Replays empirical meteorological traces: hourly wind speed (`windspeedS.csv`) and solar irradiance (`irradianceS.csv`).
  - Wind power modeled with nominal 7,200 W turbine (cut-in 2.5 m/s, rated 15 m/s, cut-off 30 m/s); solar power modeled with 200 PV panels ($\eta = 0.20$).
  - Machine idle power: 50 W; per-processor active power: up to 50 W.
- **Workload trace / dataset:**
  - Standard Workload Format (SWF) traces from the Feitelson Parallel Workloads Archive:
    1. `Cirne.swf`: San Diego Supercomputer Center (SDSC SP2, 128 nodes).
    2. `Jann.swf`: Lawrence Livermore National Laboratory (LLNL T3D, 256 nodes).
    3. `lublin_256.swf`: Synthetic 256-node workload generated from the Lublin99 statistical model.
  - Job power demands sampled from empirical profile dataset `power.csv` (16–50 W per node).
- **Simulator or real testbed:** Trace-driven high-fidelity discrete-event HPC cluster simulation (`HPCSimPickJobs.py`).
- **Baselines compared:**
  1. *FCFS (First-Come First-Served):* Traditional FIFO queue scheduling.
  2. *F2 (WFP3 / Shortest-Job-First):* Heuristic prioritizing short jobs.
  3. *LPTPN (Longest Processing Time per Processor Node):* Heuristic prioritizing compute-dense jobs.
  4. *GA (Genetic Algorithm):* Meta-heuristic optimization with two-queue initialization (`twoQs_function`).
  5. *MaskablePPO (Single-Action DRL):* SOTA reinforcement learning baseline that only makes job selection decisions without delay capability.
  6. *Backfill Policy Ablations:* No-backfill (0), Green-backfill (1), EASY-backfill (2).

---

## 4. Results (numbers only, copied exactly)

### Performance Across Algorithms (10 Test Iterations, Sequence Length = 1,024 Jobs):
| Algorithm | Average Bounded Slowdown | Renewable Energy Utilization ($U_{\text{green}}$) | Scheduling Modality |
|:---|:---:|:---:|:---|
| **FCFS** | Higher latency baseline | Low green utilization | FIFO heuristic |
| **F2 (WFP3)** | Reduced slowdown vs. FCFS | Low green utilization | SJF heuristic |
| **LPTPN** | Degraded slowdown | Moderate green utilization | Compute-density heuristic |
| **GA (Genetic Algorithm)** | Moderate slowdown | Moderate green utilization | Evolutionary search |
| **MaskablePPO (Single-Action)** | Competitive slowdown | Limited green gain | Single-action RL (immediate dispatch) |
| **GAS-MARL (Proposed)** | **Maintains low bounded slowdown** | **Highest renewable energy utilization** | **Multi-action RL (Job + Delay decision)** |

### Backfilling Policy Ablation Results:
| Backfill Configuration | Policy ID | Key Finding |
|:---|:---:|:---|
| **No Backfilling** | 0 | Lower cluster utilization; prolonged queue wait during delay windows |
| **Green-Backfilling (GAS-MARL)** | 1 | **Highest renewable utilization while preserving delayed job start reservations** |
| **EASY-Backfilling** | 2 | Higher performance throughput but ignores green energy alignment |

### Delay Action Mechanism Distribution:
| Action Modality | Selection Trigger | Operational Benefit |
|:---|:---|:---|
| **Action 2 = 0 (Immediate)** | Ample green energy currently available | Zero delay overhead; instant dispatch |
| **Action 2 $\in [1, 5]$ (Resource Delay)** | Node contention; imminent job completion | Eliminates partial node allocation idle waste |
| **Action 2 $\in [6, 12]$ (Green Delay)** | Green power trough; renewable peak within 1 hour | Shifts compute into solar/wind peak window |

---

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Slowdown vs. Green Trade-off:* Aggressively delaying jobs to wait for green energy inevitably increases queue latency; the choice of penalty factor $\eta = 0.002$ critically governs this operational balance.
  - *Discrete Delay Granularity:* Delay intervals are restricted to fixed discrete durations ($DS \in [300, 3600]$ s); continuous-time scheduling or longer multiday deferral is not supported.
  - *Single-Site HPC Scope:* Evaluates a single localized HPC cluster; cross-datacenter job migration and wide-area network bandwidth constraints are not addressed.
- **Gap we observe:**
  - *Omission of Grid Carbon Intensity (Scope 2):* The paper optimizes purely for on-site renewable self-consumption ($U_{\text{green}}$). It completely omits dynamic grid marginal carbon intensity signals ($g\text{CO}_2/\text{kWh}$), time-of-use tariffs, and grid balancing authority telemetry (hence scoring Q3 = 0.5 under strict G3 rules).
  - *Profiled vs. Measured Power:* Job power values are sampled from an offline distribution (`power.csv`) rather than measured from physical hardware counters (e.g., RAPL or IPMI) during runtime.
  - *Fixed 24-Hour Forecast Window:* Assumes an exact 24-hour green power lookahead window without evaluating the impact of forecast noise or meteorological prediction degradation.

---

## 6. Relevance to our project
GAS-MARL provides three pivotal methodological contributions for our Carbon-Aware RL Cloud Scheduler:
1. **Decoupling Job Selection from Execution Timing:** Validates that single-action DRL schedulers inherently struggle with green computing because immediate execution cannot adapt to renewable volatility. Coordinated multi-action decisions (Action 1 = *Which job*, Action 2 = *When to run*) resolve this limitation.
2. **Action-Conditioned Delay Head:** Demonstrates a clean neural architecture where the second action head is conditioned on the embedding of the selected job, ensuring delay decisions account for the specific power profile of the selected workload.
3. **Green-Backfilling Concept:** Shows how traditional cluster backfilling can be adapted to green computing by utilizing idle processors during green deferral windows, preventing cluster underutilization while honoring renewable reservations.
4. **HPC Batch Scheduler Perspective:** Acts as an essential benchmark in Group G3 illustrating how high-performance batch computing approaches renewable energy integration, complementing cloud hyperscaler approaches (e.g., P02, P21).
