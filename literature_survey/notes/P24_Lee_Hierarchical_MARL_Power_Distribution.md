# P24 — Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems

**Full citation:** Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, and Joongheon Kim, "Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems", *arXiv preprint arXiv:2607.03324*, July 2026.
**DOI / link:** [https://doi.org/10.48550/arXiv.2607.03324](https://doi.org/10.48550/arXiv.2607.03324)
**Type:** Preprint (arXiv)     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)
**Quality score:** 7.0 / 8  *(Lenient: 7.5 / 8)*
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 0.5, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*
*(Note on score and primary source audit: Archival PDF downloaded directly from arXiv (`arXiv:2607.03324`, 16 pages, 2.99 MB) and stored at `literature_survey/papers/P24_Lee_Hierarchical_MARL_AIDC.pdf`; converted to structured Markdown at `literature_survey/markdown_papers/P24.md`.
- **Q1 (1.0):** Formulates a comprehensive physical-cyber mathematical system model coupling distribution power flow (DistFlow equations), Carbon Emission Flow (CEF) tracking, AIDC power consumption (IT servers and CRAC-chiller-cooling tower loops), and heterogeneous AI job queues.
- **Q2 (1.0):** Detailed Multi-Agent Transformer (MAT) architecture with autoregressive decoding order (WM agent acts first $\rightarrow$ local AIDC agents act conditioned on WM decisions), exact state/action formulations, largest remainder rule for continuous-to-integer action projection, and action space cardinality proofs.
- **Q3 (1.0 — Strict G3 Rule):** Strictly meets G3 carbon standards: ingests dynamic Nodal Carbon Intensity (NCI in $kg\text{CO}_2/\text{kWh}$) calculated from physical Carbon Emission Flow (CEF) embedded in distribution network power flows and gas-turbine emissions.
- **Q4 (0.5):** Scored 0.5 under strict rubric rules because it simulates stochastic AI workload arrival patterns calibrated to neural scaling laws (LLM, VAE, DeepResearch, Search) rather than replaying public production cluster traces (such as Google Borg or Alibaba). *(Lenient score: 1.0 if calibrated neural scaling models are accepted)*.
- **Q5 (1.0):** Benchmarked against multiple baseline paradigms: MAPPO (MLP policies), Transformer (parallel attention without shared encoder), MAT-Dec (decentralized decoders), static allocation baselines (S-MAT1, S-MAT2), and carbon-agnostic Power Mode ablations.
- **Q6 (1.0):** Full quantitative reporting in Table II and figures: training/inference throughput in TOPS, electricity purchase cost in $, carbon emissions in $\text{tonCO}_2$, dropped jobs, carbon efficiency in $\text{MWh}/\text{tonCO}_2$, and average PUE.
- **Q7 (0.5):** Scored 0.5 because although all mathematical formulations, network dimensions, parameters, and algorithms are fully documented in the open-access preprint, the source code repository URL is not stated in the paper text.
- **Q8 (1.0):** Features exhaustive sensitivity and trade-off analyses: economic-environmental weighting ($c_2/c_3$), carbon penalty parameter $\lambda$, timescale separation (1-min agent vs. 15-min DSO), and action space complexity reductions).*

---

## 1. Problem addressed
The rapid proliferation of generative artificial intelligence and large language models (LLMs) has turned Artificial Intelligence Data Centers (AIDCs) into multi-megawatt electricity consumers with substantial carbon footprints:
1. **Power Distribution System Stress:** Connecting multi-megawatt AIDCs to regional power distribution systems causes voltage drops, line overloads, and steep ramping demand.
2. **Nodal Carbon Variations in Distribution Grids:** Due to localized renewable generation (solar/wind) and localized gas-turbine (GT) peakers, carbon emission intensity is not uniform across a distribution grid; it varies significantly across physical distribution network nodes depending on power flow directions (Carbon Emission Flow, CEF).
3. **Coupled IT and Thermal Management:** An AIDC's total power consumption comprises IT server power and computer room air conditioning (CRAC) cooling power. Prior schedulers treat job scheduling and cooling control independently, missing the opportunity to co-optimize computing schedules with cooling chiller efficiency.
4. **Action Space Combinatorial Explosion:** Jointly optimizing global spatial workload routing across multiple AIDCs, local temporal deferral, GPU block allocation, and CRAC temperature setpoints across $N$ facilities creates an astronomically large joint action space (exceeding $10^{39}$ states for 3 AIDCs) that causes standard flat multi-agent RL algorithms to fail.

---

## 2. Approach (the core idea)
The authors propose a **Hierarchical Carbon-Aware Multi-Agent Reinforcement Learning (CA-MARL)** framework based on a **Multi-Agent Transformer (MAT)** architecture:
- **Hierarchical Two-Layer Coordination:**
  - *Workload Manager (WM) Agent (Global Aggregator):* Sits at the top layer. Observes global distribution system nodal carbon intensities (NCI) and time-of-use (TOU) electricity prices, spatially distributing incoming AI training and inference jobs among all regional AIDCs.
  - *Local AIDC Agents (Local Operators):* Sit at the lower layer. Conditioned on the WM agent's spatial allocation, each local AIDC agent executes four coordinated tasks:
    1. Temporal shifting of delay-tolerant training jobs.
    2. Spatial allocation of training GPU blocks.
    3. Allocation of inference GPUs.
    4. Control of CRAC supply air temperature to minimize chiller/cooling tower power.
- **Autoregressive Multi-Agent Transformer (MAT):** Employs an encoder-decoder Transformer that processes agent observations through a shared encoder and samples decisions autoregressively: the WM agent always decodes first, and local AIDC agents decode sequentially conditioned on preceding actions. This converts the joint action search complexity from $O(N^{M\Gamma} |A^{\text{AIDC}}|^N)$ to $O(N^{M\Gamma} + N|A^{\text{AIDC}}|)$, reducing action cardinality by $1.85 \times 10^{28}\times$ for 3 AIDCs.
- **Carbon Emission Flow (CEF) Integration:** Ingests dynamic Nodal Carbon Intensity (NCI, $w_{i,t}$ in $kg\text{CO}_2/\text{kWh}$) calculated by the Distribution System Operator (DSO) via virtual carbon flow equations, providing physically accurate locational carbon accounting.
- **Largest Remainder Rule Projection:** Projects continuous ratio policy outputs into exact, non-negative integer job allocations while bounding quantization errors to less than one job per variable.

---

## 3. Methodology
- **System role:** Hierarchical aggregator and facility operator coordinating spatial workload distribution, local temporal shifting, GPU allocation, and thermal CRAC management across regional AIDCs.
- **Scheduling decision:** Multi-level coordinated decisions: spatial inter-AIDC job placement ratios ($\pi_{m,i,t}^k$), local temporal deferral fractions ($q_{m,i,t}^h$), training GPU block allocations ($u_{m,i,t}$), inference GPU allocations ($v_{m,i,t}$), and CRAC supply air temperature ($T_{i,t}^{\text{CRAC,sup}}$).
- **Workload type:** Heterogeneous AI workloads parameterized via neural scaling laws:
  - *Training jobs:* LLM and VAE (delay-tolerant, bursty arrivals, deadline slacks up to $\tau_m^{\text{train}}$).
  - *Inference jobs:* DeepResearch and Search (delay-sensitive, high-frequency, strict FIFO queues).
- **Dynamic or online?** Yes; online dynamic closed-loop control evaluated at 1-minute scheduling intervals under 15-minute DSO NCI signal updates.
- **For RL papers:**
  - **Algorithm:** **Hierarchical Carbon-Aware Multi-Agent Reinforcement Learning (CA-MARL)** trained via **Multi-Agent Transformer (MAT)** with clipped PPO surrogate loss and GAE advantage estimation.
  - **State Space:**
    - *WM Agent State ($s_t^{\text{WM}}$):* TOU price $\kappa_t$, NCI vector $\mathbf{w}_t$, per-AIDC status vectors (training backlogs, inference queues, power, available GPU ratio $\phi_{i,t}^{\text{free}}$), arrival vectors ($\mathbf{N}_t^{\text{train}}, \mathbf{N}_t^{\text{inf}}$), and time $t$.
    - *AIDC Agent State ($s_{i,t}^{\text{AIDC}}$):* Local TOU price and deferral vectors, local backlog $\mathbf{B}_{i,t}$, local NCI $w_{i,t}$, previous power $P_{i,t-1}^{\text{AIDC}}$, available GPU ratio, allocated jobs from WM ($\mathbf{n}_{i,t}^{\text{train}}, \mathbf{n}_{i,t}^{\text{inf}}$), and time $t$.
  - **Action Space:**
    - *WM Action:* Continuous spatial distribution vector $\mathbf{a}_t^{\text{WM}} = [\pi_{m,i,t}^k]$ projected to integer job allocations.
    - *AIDC Action:* 4-tuple $\mathbf{a}_{i,t}^{\text{AIDC}} = (\mathbf{q}_{i,t}, \mathbf{u}_{i,t}, \mathbf{v}_{i,t}, T_{i,t}^{\text{CRAC,sup}})$.
  - **Reward Function:** Shared multi-objective global reward:
    $$R_t = c_1 R_{1,t} - c_2 R_{2,t} - c_3 R_{3,t} - c_4 R_{4,t} - c_5 R_{5,t}$$
    where $R_{1,t}$ is total throughput in TOPS, $R_{2,t}$ is electricity purchase cost, $R_{3,t}$ is carbon emissions ($\sum w_{i,t} P_{i,t}^{\text{AIDC}}$), and $R_{4,t}, R_{5,t}$ are dropped training and inference jobs.
- **Carbon / energy data source and region:**
  - Nodal Carbon Intensity (NCI, $kg\text{CO}_2/\text{kWh}$) calculated by solving the CEF-integrated DSO optimal power flow problem on an IEEE 33-node distribution system with gas turbine (GT) generation and substation power.
  - Time-of-use (TOU) electricity pricing profile: peak period [11 AM, 3 PM], off-peak period [7 PM, 11 PM].
- **Workload trace / dataset:**
  - Calibrated stochastic traffic generation based on neural scaling laws (LLM, VAE, DeepResearch, Search) capturing diurnal patterns, burstiness, and high-frequency queries.
- **Simulator or real testbed:** Simulation of an **IEEE 33-node power distribution system** (12.66 kV nominal voltage) integrating three gas turbines and three regional AIDCs (each consuming 8–12 MW, equipped with several hundred GPUs and CRAC cooling units).
- **Baselines compared:**
  1. *MAPPO:* Multi-Agent PPO with multi-layer perceptron policies.
  2. *Transformer:* Parallel self-attention policy without a shared encoder.
  3. *MAT-Dec:* Multi-Agent Transformer with decentralized decoders.
  4. *S-MAT1 & S-MAT2:* Static allocation baselines (fixed ratios 1:2:7 and 1:1:8).
  5. *Power Mode (Ablation):* Economic-only scheduling omitting carbon emission objectives ($c_3 = 0, \lambda = 0$).

---

## 4. Results (numbers only, copied exactly)

### Primary Comparison Across Algorithms (24-Hour Evaluation, 1,440 Steps) [Table II, p. 11]:
| Metric | MAPPO (Joint) | Transformer (Joint) | MAT-Dec (Joint) | **Proposed MAT (Joint)** | Proposed MAT (Power Mode) | Source |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Total Throughput [TOPS]** ($R_{1,t}$) | 59.86M | 54.24M | 64.60M | **65.67M** | 70.69M | Table II, p. 11 |
| **Electricity Purchase Cost [$]** ($R_{2,t}$) | $1,886.47 | $1,859.21 | $2,142.61 | **$2,084.77** | $2,554.95 | Table II, p. 11 |
| **Total Carbon Emissions [tonCO₂]** ($R_{3,t}$) | 10.54 | 10.58 | 10.01 | **9.77** | 12.09 | Table II, p. 11 |
| **Dropped Training + Inference Jobs** | 10,627 | 14,885 | 6,207 | **419** | 45 | Table II, p. 11 |
| **Carbon Emission Efficiency [MWh/tonCO₂]** | 1.65 | 1.68 | 1.67 | **1.69** | 1.67 | Table II, p. 11 |
| **Average PUE** | 1.16 | 1.15 | 1.13 | **1.08** | 1.39 | Table II, p. 11 |

### Carbon-Aware Joint Mode vs. Economic Power Mode:
- **Carbon Reduction:** Proposed MAT in joint mode reduces carbon emissions from **12.09 tonCO₂ to 9.77 tonCO₂** (**19.2% carbon reduction**).
- **Electricity Cost Reduction:** Reduces total cost from **$2,554.95 to $2,084.77** (**18.4% cost savings**).
- **Cooling PUE Improvement:** PUE improves from **1.39 down to 1.08** by co-optimizing CRAC supply air temperature with IT load distribution.

### Action-Space Cardinality Reduction [Table III, p. 15]:
| Number of AIDCs ($N$) | Non-Hierarchical Flat Cardinality | Hierarchical MAT Cardinality | Complexity Reduction Ratio | Source |
|:---:|:---:|:---:|:---:|:---|
| **$N = 2$** | $4.29 \times 10^{25}$ | $1.08 \times 10^{11}$ | **$3.96 \times 10^{14}\times$** | Table III, p. 15 |
| **$N = 3$** | $3.01 \times 10^{39}$ | $1.62 \times 10^{11}$ | **$1.85 \times 10^{28}\times$** | Table III, p. 15 |
| **$N = 4$** | $5.75 \times 10^{52}$ | $2.23 \times 10^{11}$ | **$2.57 \times 10^{41}\times$** | Table III, p. 15 |
| **$N = 5$** | $4.67 \times 10^{65}$ | $1.27 \times 10^{12}$ | **$3.67 \times 10^{53}\times$** | Table III, p. 15 |

---

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Economic vs. Environmental Trade-off:* Tuning weight ratio $c_2/c_3$ controls the Pareto trade-off; higher cost weighting reduces electricity purchases but increases carbon emissions. The authors select $c_2/c_3 = 0.02$ as a balanced operating point.
  - *Timescale Separation Constraint:* The DSO computes NCI at 15-minute intervals due to optimal power flow computational overhead, while AIDC agents act at 1-minute steps; sub-minute power fluctuations cannot be captured by the DSO model.
  - *Thermal Safety Constraints:* CRAC air temperature control must strictly respect server rack inlet limits ($T_{i,r,t}^{\text{inlet}} \le 27^\circ\text{C}$) to prevent hardware overheating.
- **Gap we observe:**
  - *Synthetic Workload Arrivals:* Uses a sinusoidal-plus-noise arrival model calibrated to neural scaling laws rather than replaying public production cluster traces (e.g., Google Borg, Alibaba).
  - *Distribution-Grid Scale Limitations:* Evaluated on an IEEE 33-node radial distribution system; wide-area transmission systems across multi-state ISOs (e.g., PJM, CAISO) are not modeled.
  - *Closed Source Codebase:* Neither a public GitHub repository nor pre-trained weights are provided in the paper text.

---

## 6. Relevance to our project
P24 offers four key takeaways for our Carbon-Aware RL Cloud Scheduler:
1. **Hierarchical Decomposition of Massive Action Spaces:** Demonstrates how separating global spatial allocation (Workload Manager) from local facility scheduling (AIDC operator) reduces action cardinality by over 28 orders of magnitude ($1.85 \times 10^{28}\times$), enabling tractable MARL.
2. **Coupled IT and Thermal CRAC Co-Optimization:** Proves that dynamically controlling cooling system supply temperatures alongside compute workloads dramatically improves facility PUE (from 1.39 to 1.08), eliminating cooling power waste.
3. **Physical Carbon Emission Flow (CEF) Grounding:** Connects cyber-workload scheduling directly to physical distribution network power flows and locational carbon intensities.
4. **Benchmark Baselines for MARL:** Provides concrete comparative numbers for MAPPO vs. Transformer vs. MAT architectures in sustainable data center coordination.
