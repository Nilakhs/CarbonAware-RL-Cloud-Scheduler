# P21 — Multi-Objective Deep Reinforcement Learning for Carbon-Aware Spatiotemporal Workload Scheduling in Geo-Distributed Data Centers

**Full citation:** Yanhuan Chen and Zijie Chen, "Multi-Objective Deep Reinforcement Learning for Carbon-Aware Spatiotemporal Workload Scheduling in Geo-Distributed Data Centers", in *Journal of Advanced Computing Systems (JACS)*, Vol. 5, No. 10, pp. 18–30, October 2025.
**DOI / link:** [https://doi.org/10.69987/JACS.2025.51002](https://doi.org/10.69987/JACS.2025.51002) (Direct PDF: `https://scipublication.com/index.php/JACS/article/download/340/309`)
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)
**Quality score:** 7.5 / 8
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*
*(Note on score and primary source audit: Full text accessed via Open Journal Systems [SciPublication / CC BY 4.0 Open Access] and downloaded locally to `literature_survey/papers/P21_Chen_MultiObjective_DRL.pdf` [13 pages, pp. 18–30]; converted to structured Markdown at `literature_survey/markdown_papers/P21.md`.
- **Q1 (1.0):** The paper provides a rigorous mathematical system model defining $N=7$ data centers mapped to 7 US ISO regions, job arrival processes, deadline flexibility slack $\Delta_i(t)$, and explicit mathematical objective formulations for carbon emissions ($O_c$), normalized latency ($O_l$), and operational cost ($O_{\text{cost}}$).
- **Q2 (1.0):** Full specification of the multi-objective MDP: exact 247-dimensional state vector breakdown, discrete action space with dynamic feasibility masking, augmented Tchebycheff scalarization function with ideal point $z_k$ and $\varepsilon=0.05$, complete neural architecture with per-component parameter counts [4.7M total parameters], and exact training hyperparameters.
- **Q3 (1.0):** Evaluated against 30 months [Jan 2022 – June 2024] of empirical hourly marginal emission rates ($g\text{CO}_2/\text{kWh}$) from the official EIA-930 API and WattTime MOER across 7 US ISO regions [CAISO, PJM, MISO, ERCOT, ISO-NE, NYISO, SPP] with full distributional statistics [Table 2].
- **Q4 (1.0):** Uses combined Google Cluster Trace 2019 (GCT19) and Alibaba Cluster Trace 2018 (ALI18), with CPU-to-GPU resource mapping based on the Zeus study [NSDI '23], generating 1,200 batch jobs/day partitioned into ML training and analytics pipelines.
- **Q5 (1.0):** Evaluated against five distinct, competitive baselines: carbon-agnostic greedy (production default), temporal-only threshold shifting, spatial-only minimum-carbon routing, fixed-weight weighted-sum DRL, and GAIA-style LP oracle.
- **Q6 (1.0):** Reports precise quantitative numbers, standard deviations, and Pareto hypervolume metrics in Table 4, along with exhaustive ablation and sensitivity analysis percentages.
- **Q7 (0.5):** Scored 0.5 because although the complete mathematical equations, layer architectures, and training hyperparameters are fully documented in the open-access paper text, the source code and trained PyTorch checkpoint weights are not hosted in an open public repository [e.g., GitHub or Zenodo].
- **Q8 (1.0):** Features a dedicated, thorough subsection (Sec. 5.2, pp. 28–29) critically discussing structural limitations: 15-minute decision epochs vs. sub-hourly grid fluctuations, assumption of deterministic job runtimes, simulation vs. production cluster manager API latencies, lack of embodied carbon accounting, and centralized vs. federated multi-agent execution).*

---

## 1. Problem addressed
The explosive demand for artificial intelligence training and hyperscale cloud computing has transformed United States data centers into significant sources of electricity demand and greenhouse gas emissions:
1. **Escalating Electricity Consumption:** US data centers consumed an estimated 200–250 TWh of electricity in 2023 (1.0%–1.3% of total national electricity output), with global data center electricity demand projected by the IEA to reach 1,000 TWh by 2026 [Sec. 1.1, p. 18].
2. **Spatiotemporal Carbon Heterogeneity:** Marginal emissions vary by a factor of 5–10 across the seven major US Independent System Operator (ISO) balancing authorities (e.g., CAISO midday solar as low as 82–150 $g\text{CO}_2/\text{kWh}$ vs. PJM coal/gas peaks reaching 819 $g\text{CO}_2/\text{kWh}$). Diurnal and seasonal swings produce intra-regional variations of 2–4× between midday renewable peaks and evening fossil peakers [Sec. 1.1, pp. 18–19; Table 2, p. 22].
3. **Shortcomings of Current Schedulers:**
   - Production cloud schedulers treat carbon as an unmodeled externality, scheduling purely based on resource availability and operational cost.
   - Existing research isolates either temporal deferral (e.g., Google VCC, Wiesner et al.) or geographic migration (e.g., Liu et al.), failing to exploit their coupled interactions.
   - Standard DRL schedulers collapse optimization into a fixed-weight scalar reward, requiring expensive retraining whenever organizational climate targets or electricity tariffs fluctuate.
4. **Three-Way Trade-off:** Schedulers must simultaneously navigate non-convex trade-offs between minimizing carbon emissions, bounding job completion latency (SLA compliance), and controlling operational costs (locational marginal electricity prices and inter-region network egress bandwidth fees) [Sec. 1.2, p. 19; Sec. 3.1, p. 21].

## 2. Approach (the core idea)
The authors propose a **Multi-Objective Deep Reinforcement Learning (MO-DRL)** framework for geo-distributed data centers:
- **Joint Spatiotemporal Shifting:** Schedulers jointly defer jobs to cleaner hours and migrate delay-tolerant batch jobs across $N=7$ US ISO balancing areas, uncovering synergies where temporal deferral expands the geographic migration window.
- **Multi-Objective MDP with Augmented Tchebycheff Scalarization:** Adopts the MOEA/D decomposition paradigm with $K=64$ weight vectors $\lambda \in \Delta^2$ on the 3-simplex. Uses an augmented Tchebycheff scalarization function with ideal point $z_k$ and parameter $\varepsilon = 0.05$ to guarantee Pareto-optimal solutions across non-convex trade-off frontiers [Sec. 3.2-B, pp. 22–23].
- **Pareto-Conditioned Policy Network via MO-PPO:** A single unified actor-critic network takes an explicit preference weight vector $\lambda = (\lambda_c, \lambda_l, \lambda_{\text{cost}})$ as input. A 2-layer hypernetwork dynamically modulates policy head weights, enabling operators to sweep the entire Pareto front at runtime without model retraining [Sec. 3.3-B, pp. 24–25; Fig. 1, pp. 23–24].
- **Hard Deadline & Feasibility Masking:** Action masking recomputed at each 15-minute epoch eliminates assignments that violate host compute capacities or exceed job deadlines, ensuring 100% feasibility compliance without post-hoc heuristic repair [Sec. 3.2-B, p. 23].

## 3. Methodology
- **System role:** Centralized cloud scheduler allocating batch workloads across $N=7$ geo-distributed data centers mapped to US ISO regions (CAISO, PJM, MISO, ERCOT, ISO-NE, NYISO, SPP) [Sec. 3.1, p. 21].
- **Scheduling decision:** Joint spatial and temporal decision per priority job: either immediately dispatch job $j_i$ to data center $d_k \in \{1,\dots,N\}$, or defer $j_i$ to the next decision epoch ($\delta_t = 15$ min) [Sec. 3.1, p. 21; Sec. 3.3-A, p. 23].
- **Workload type:** Delay-tolerant batch computing jobs (ML training, analytics pipelines, CI/CD runs) partitioned into four classes by deadline slack $\Delta_i(t) = D_i - t$: hard real-time ($\Delta < 1$h, excluded), soft real-time ($1\text{h} \le \Delta < 6\text{h}$), batch ($6\text{h} \le \Delta < 48\text{h}$), and archival ($\Delta \ge 48\text{h}$) [Sec. 3.1, p. 21].
- **Dynamic or online?** Yes; online closed-loop scheduling evaluated at 15-minute epochs over a 30-day continuous horizon [Sec. 3.1, p. 21; Sec. 4.1, p. 26].
- **For RL papers:**
  - **Algorithm:** **MO-PPO** (Multi-Objective Proximal Policy Optimization) trained with augmented Tchebycheff decomposition over $K=64$ reference weight vectors [Sec. 3.2-B, pp. 22–23; Sec. 3.3-B, p. 25].
  - **State Space ($S$):** 247-dimensional composite state vector:
    1. *Grid state (175-dim):* 7 regions $\times$ 25 features (current marginal emission rate, 24-step forecast from Temporal Fusion Transformer [TFT], mean, min, time-of-min) [Sec. 3.3-A, p. 23].
    2. *Price state (21-dim):* 7 regions $\times$ 3 features (current spot price, 6h forecast mean, daily average).
    3. *Utilization state (21-dim):* 7 regions $\times$ 3 features (current GPU utilization, queue depth, estimated time-to-availability).
    4. *Queue state (30-dim):* Top 5 priority jobs $\times$ 6 features (resource demand ratio, normalized deadline slack, data volume, origin data center one-hot).
    5. *Temporal context (4-dim):* Sine-cosine encoding of time-of-day and day-of-week.
    6. *Preference vector $\lambda$ (3-dim):* Appended at inference to condition the policy heads.
  - **Action Space ($A$):** Discrete $(j_i, d_k, \text{dispatch}) \cup \{\text{defer}\}$, filtered by dynamic boolean feasibility mask $M(s) \in \{0,1\}^{|A|}$ [Sec. 3.3-A, p. 23].
  - **Reward Design:** Vector reward $r_t = [r_{c,t}, r_{l,t}, r_{\text{cost},t}]$ based on:
    - Operational carbon emissions: $O_c = \sum_i \sum_t [x_{i,d,t} \cdot \text{GPU}_i \cdot P_{\text{GPU}} \cdot e_d(t) \cdot \delta_t]$
    - Normalized latency: $O_l = \frac{1}{M} \sum_i \frac{C_i - A_i}{D_i - A_i}$
    - Operational cost: $O_{\text{cost}} = \sum_i [\sum_t x_{i,d,t} \cdot \text{GPU}_i \cdot P_{\text{GPU}} \cdot p_d(t) \cdot \delta_t + \sum_{d \ne o_i} x_{i,d} \cdot V_i \cdot w_{o_i,d}]$
    - Scalarized at training time via: $r_\lambda(s,a) = \min_k \{\lambda_k (z_k - O_k(s,a))\} + \varepsilon \sum_k \lambda_k (z_k - O_k(s,a))$ with $\varepsilon = 0.05$ [Sec. 3.2-B, p. 23].
  - **Neural Network Architecture (4.7M total parameters) [Table 3, p. 25]:**
    - Spatial CNN: 3 conv layers, 64 filters, kernel size 3, ReLU (147.46k params) for grid state.
    - Temporal Bi-LSTM: 2 layers, hidden size 128 (528.38k params) for forecast sequences.
    - Queue MLP: Dense layers [256, 128], ReLU, LayerNorm (131.20k params).
    - Shared Transformer Encoder: 4 layers, 2 heads, $d_{\text{model}} = 512$ (2,097.15k params).
    - Hypernetwork: 2-layer MLP [128, 128] (82.94k params) generating policy head weights from $\lambda$.
    - Policy + Value heads: Linear, softmax, $\lambda$-conditioned (24.32k params).
  - **Training Setup:** 5,000 episodes across 128 parallel environments, trajectory length $T=256$, PPO clip $\varepsilon_{\text{clip}}=0.2$, learning rate $\alpha = 3\times 10^{-4}$ with cosine annealing, entropy coefficient $\beta=0.01$, gradient clip norm 0.5; converges in ~1,200 episodes [Sec. 3.3-B, p. 25].
- **Carbon / energy data source and region:**
  - Hourly marginal emission rates ($g\text{CO}_2/\text{kWh}$) from the official EIA-930 API augmented with WattTime MOER across 7 US ISO regions (CAISO, PJM, MISO, ERCOT, ISO-NE, NYISO, SPP) spanning January 2022 to June 2024 (30 months) [Sec. 3.2-A, p. 22; Sec. 4.1-A, p. 26; Table 2, p. 22].
  - 24-hour ahead forecasts generated by a Temporal Fusion Transformer (TFT) with 8.3% 1h MAPE and 14.7% 12h MAPE [Sec. 3.2-A, p. 22].
  - 5-minute locational marginal electricity prices ($/MWh) resampled to hourly [Sec. 3.1, p. 21; Sec. 4.1-A, p. 26].
- **Workload trace / dataset:**
  - Google Cluster Trace 2019 (GCT19) combined with Alibaba Cluster Trace 2018 (ALI18), scaled using Zeus GPU power ratios [NSDI '23], generating ~1,200 schedulable batch jobs/day (40% ML training, 60% analytics) [Sec. 4.1-A, p. 26].
  - Slack distributions: ML training $\sim U[12\text{h}, 72\text{h}]$, analytics $\sim U[6\text{h}, 24\text{h}]$, CI/CD $\sim U[2\text{h}, 8\text{h}]$ [Sec. 4.1-A, p. 26].
- **Simulator or real testbed:** Trace-driven high-fidelity discrete-event simulation of 7 hyperscale clusters (500–2,000 GPUs per cluster) with inter-region network egress costs ($0.02–$0.15/GB) [Table 1, p. 21; Sec. 5.2, p. 28].
- **Baselines compared:**
  1. *Carbon-Agnostic Greedy:* Least-loaded data center placement (production default).
  2. *Temporal-Only (threshold):* Defer within origin cluster if carbon intensity exceeds 40th percentile of 24h forecast.
  3. *Spatial-Only (min-carbon):* Immediate dispatch to lowest carbon intensity region.
  4. *Weighted-Sum DRL (fixed $\lambda$):* Identical architecture trained with fixed $\lambda = (0.5, 0.25, 0.25)$.
  5. *GAIA-Style LP Oracle:* Linear programming relaxation with perfect 24h forecast knowledge [Sec. 4.1-B, p. 26].

---

## 4. Results (numbers only, copied exactly)

### Primary Comparison Across Baselines (30-Day Evaluation, Mean ± Std) [Table 4, p. 26; Table 4 cont., p. 27]:
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon emissions (tCO₂) | **28.5 ± 1.3** | Carbon-Agnostic Greedy: 48.7 ± 2.1 | Table 4, p. 26 |
| Carbon emissions (tCO₂) | **28.5 ± 1.3** | Temporal-Only: 38.4 ± 1.9 | Table 4, p. 26 |
| Carbon emissions (tCO₂) | **28.5 ± 1.3** | Spatial-Only: 35.1 ± 2.4 | Table 4, p. 26 |
| Carbon emissions (tCO₂) | **28.5 ± 1.3** | Weighted-Sum DRL (fixed λ): 33.8 ± 1.7 | Table 4, p. 26 |
| Carbon emissions (tCO₂) | **28.5 ± 1.3** | GAIA-Style LP Oracle: 30.2 ± 1.4 | Table 4, p. 26 |
| Carbon emissions (tCO₂) | **34.2 ± 1.5** (balanced) | Carbon-Agnostic Greedy: 48.7 ± 2.1 | Table 4, p. 27 |
| Carbon emissions (tCO₂) | **38.9 ± 1.8** (perf-focused) | Carbon-Agnostic Greedy: 48.7 ± 2.1 | Table 4, p. 27 |
| Carbon reduction vs. Greedy | **41.3% reduction** (carbon-focused) | Carbon-Agnostic Greedy | Table 4, p. 26 |
| Carbon reduction vs. Greedy | **29.8% reduction** (balanced) | Carbon-Agnostic Greedy | Table 4, p. 27 |
| Carbon reduction vs. Greedy | **20.1% reduction** (perf-focused) | Carbon-Agnostic Greedy | Table 4, p. 27 |
| Carbon reduction vs. Baselines | **+13.4% higher reduction** than Spatial-Only | Spatial-Only (27.9%) | Sec. 4.2, p. 27 |
| Carbon reduction vs. Baselines | **+20.1% higher reduction** than Temporal-Only | Temporal-Only (21.2%) | Sec. 4.2, p. 27 |
| Carbon reduction vs. Oracle | **+3.3% higher reduction** than LP Oracle | GAIA-Style LP Oracle (38.0%) | Sec. 4.2, p. 27 |
| Normalized Latency | **0.45 ± 0.05** (carbon-focused) | Carbon-Agnostic Greedy: 0.31 ± 0.04 | Table 4, p. 26 |
| Normalized Latency | **0.36 ± 0.04** (balanced) | Carbon-Agnostic Greedy: 0.31 ± 0.04 | Table 4, p. 27 |
| Normalized Latency | **0.33 ± 0.04** (perf-focused) | Carbon-Agnostic Greedy: 0.31 ± 0.04 | Table 4, p. 27 |
| Operational Cost ($K) | **$97.1 ± 4.9** (carbon-focused) | Spatial-Only: $103.7 ± 6.2 | Table 4, p. 26 |
| Operational Cost ($K) | **$93.4 ± 4.2** (balanced) | Temporal-Only: $91.4 ± 4.1 | Table 4, p. 26–27 |
| Operational Cost ($K) | **$90.8 ± 3.9** (perf-focused) | Carbon-Agnostic Greedy: $89.2 ± 3.8 | Table 4, p. 26–27 |
| Hypervolume (HV) Indicator | **0.681** | Weighted-Sum DRL: 0.412 (+65.3% coverage) | Table 4, p. 26; Sec. 4.2, p. 27 |

### Ablation & Mechanism Interaction Results [Sec. 4.3-A, p. 28]:
| Configuration | Carbon Reduction | Mechanism Detail / Finding | Source |
|:---|:---|:---|:---|
| Temporal-Only MO-PPO | 26.1% | Spatial migration disabled | Sec. 4.3-A, p. 28 |
| Spatial-Only MO-PPO | 29.4% | Temporal deferral disabled | Sec. 4.3-A, p. 28 |
| Joint MO-PPO | **41.3%** | Full action space (+11.9% over Spatial-Only) | Sec. 4.3-A, p. 28 |
| Deferred migration synergy | **38% of migrated jobs** | Required prior deferral of 6–18h to open migration window | Sec. 4.3-A, p. 28 |
| Summer weekday savings | 67% spatial / 33% temporal | Driven by CAISO midday solar carbon valleys | Sec. 4.3-A, p. 28 |
| Winter weeknight savings | 58% temporal / 42% spatial | Driven by intra-regional heating demand response swings | Sec. 4.3-A, p. 28 |

### Sensitivity Analysis & Robustness [Sec. 4.3-B, p. 28]:
| Parameter Variation | Carbon Reduction | Impact / Comparison | Source |
|:---|:---|:---|:---|
| Slack compressed to U[6h, 24h] | 28.7% | -12.6% reduction compared to default U[6h, 72h] | Sec. 4.3-B, p. 28 |
| Slack extended to U[6h, 96h] | 44.8% | Diminishing returns beyond 72h windows | Sec. 4.3-B, p. 28 |
| Forecast noise at 10% MAPE | 38.1% | -3.2% degradation from default 41.3% | Sec. 4.3-B, p. 28 |
| Forecast noise at 20% MAPE | **34.4%** | Degrades gracefully; beats LP Oracle (29.1%) | Sec. 4.3-B, p. 28 |
| Region scaling (3 to 7 regions) | 24.3% → 41.3% | Near-linear improvement with geographic diversity | Sec. 4.3-B, p. 28 |

---

## 5. Gap
- **Author-discussed constraints and trade-offs (Sec. 5.2, pp. 28–29):**
  - *Coarse Decision Epoch (15-min):* The scheduler operates at 15-minute decision intervals, which risks missing sub-hourly carbon intensity spikes and locational marginal pricing adjustments that increasingly occur in real-time 5-minute markets.
  - *Deterministic Job Runtime Assumption:* The MDP assumes known or accurately estimated job execution durations ($\tau_i$). In production clusters, execution variance, stragglers, and container cold starts introduce runtime uncertainty that can breach deadline bounds.
  - *Simulation vs. Live API Latencies:* The evaluation is performed in a discrete-event simulator; physical deployment must integrate with production Kubernetes/Slurm cluster managers and public ISO REST APIs, which encounter network latency and telemetry jitter.
  - *Exclusion of Embodied Carbon:* Focuses strictly on Scope 2 operational emissions. Hardware manufacturing, server embodied carbon, and depreciation (Scope 3) are omitted from the objective function.
  - *Centralized Coordinator Bottleneck:* The architecture relies on a centralized agent collecting telemetry from all 7 ISO regions; decentralized or federated multi-agent execution is needed for privacy-preserving, fault-tolerant scaling.
- **Gap we observe:**
  - *Closed Source Repository:* Despite the open-access publication under CC BY 4.0, neither an official GitHub repository nor pre-trained model weights are provided in the article.
  - *Centralized State Explosion:* The 247-dimensional composite state incorporates data from only top 5 priority jobs in the queue; scaling to large production clusters with thousands of concurrent pending jobs requires graph neural networks or attention-based queue encoders.
  - *Bandwidth Contention Modeling:* Inter-region data migration is penalized financially ($w_{d,d'}$ per GB) and checked for feasibility, but dynamic cross-WAN link congestion and packet queueing delays are simplified to fixed per-job transfer delays.

---

## 6. Relevance to our project
P21 is a foundational benchmark paper for Group G3:
1. **Pareto-Conditioned Policy Head via Hypernetworks:** Eliminates the classic limitation of fixed-weight scalar DRL by taking operator preference weights $\lambda$ as an explicit runtime vector input, allowing on-the-fly trade-off tuning without retraining.
2. **Coupled Spatiotemporal Synergy:** Proves that temporal deferral and spatial migration should not be designed as isolated modules: 38% of beneficial migrations require prior temporal deferral to align with regional renewable peaks.
3. **Robustness to Grid Forecasting Noise:** Demonstrates that DRL policies inherently handle forecast inaccuracies (retaining 34.4% carbon reduction under 20% MAPE noise), significantly outperforming brittle deterministic LP oracles.
4. **Benchmark for Our Experimental Comparison:** Provides concrete baseline numbers across 7 US ISO regions, Google/Alibaba traces, and 30-month EIA-930 marginal carbon datasets that directly inform our scheduler evaluation.
