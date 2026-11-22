# P03 — Carbon Explorer (Holistic Datacenter Design)

**Full citation:** Bilge Acun, Benjamin C. Lee, Fiodar Kazhamiaka, Kiwan Maeng, Udit Gupta, Manoj Chakkaravarthy, David Brooks, and Carole-Jean Wu, "Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters", in *Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS '23), Volume 2*, Vancouver, Canada, ACM, pp. 118–132, March 2023.  
**DOI / link:** [https://doi.org/10.1145/3575693.3575754](https://doi.org/10.1145/3575693.3575754) (also [arXiv:2212.07340](https://arxiv.org/abs/2212.07340))  
**Type:** Conference     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5 [open-source framework at facebookresearch/CarbonExplorer; proprietary Meta hardware traces], Q8: 1.0)*  

---

## 1. Problem addressed
The tech sector is rapidly moving toward 24/7 Carbon-Free Energy (CFE), aiming to match hourly electricity demand directly with clean energy sources. However, existing cloud decarbonization studies evaluate either operational optimizations (e.g., workload shifting) or physical capacity expansions (e.g., on-site solar, wind, and battery storage) in isolation. Crucially, prior work ignores the massive **embodied carbon emissions** generated during the manufacturing and construction of solar panels, wind turbines, and energy storage batteries. Without a holistic framework, deploying excessive green infrastructure can inadvertently increase net lifetime carbon emissions.  [Source: Sec. 1 & 2, pp. 118–121]

## 2. Approach (the core idea)
The authors present **Carbon Explorer**, an open-source, end-to-end framework that jointly evaluates and co-optimizes operational and embodied carbon across three key dimensions: (1) renewable generation capacity sizing (solar and wind), (2) battery energy storage capacity, and (3) software workload scheduling (temporal delay and geographic spatial routing). It formulates a multi-objective trade-off space to identify the Pareto-optimal design configurations that maximize hourly 24/7 CFE while minimizing total lifetime carbon footprint and capital costs.  [Source: Sec. 3 & 4, pp. 121–126]

## 3. Methodology
- **Scheduling decision:** Both temporal shifting (delaying flexible workloads up to allowable deadlines) and spatial routing (distributing computing tasks across regions).
- **Workload type:** Hyperscale production workloads, including ML training, ML inference, and general compute services, categorized into latency-sensitive services and flexible batch jobs.
- **Dynamic or online?** Static/offline design exploration combined with hourly time-series simulation of dynamic operational traces.
- **For non-RL papers (Heuristic / Optimization used):**
  - Multi-variable constrained optimization using linear programming and heuristic parameter sweeps. Solves for generation capacity ($S_{solar}, S_{wind}$), storage capacity ($B_{batt}$), and hourly load-shifting factors ($L_t$) to maximize the Carbon-Free Energy (CFE) metric subject to battery degradation and task deadline constraints:
    $$\text{CFE} = \frac{\sum_{t} \min(D_t, R_t + B_t^{discharge})}{\sum_t D_t}$$
- **Carbon data source and region:** Hourly generation and grid carbon intensity profiles across diverse geographical regions (US East/PJM, US West/CAISO, and Northern Europe) using historical datasets from local transmission operators and Tomorrow / Electricity Maps.
- **Workload trace / dataset:** Production workload profiles and server power measurements from Meta's global datacenter infrastructure.
- **Simulator or real system:** Trace-driven simulation framework implemented in Python, open-sourced via GitHub (`facebookresearch/CarbonExplorer`).
- **Baselines compared:** 
  - Conventional carbon-agnostic datacenter baseline.
  - Sizing policies that ignore embodied carbon (pure operational minimization).
  - Isolated mitigation strategies (workload shifting alone vs. battery storage alone vs. generation sizing alone).  
[Source: Sec. 3, 4 & 5, pp. 122–128]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Hourly Carbon-Free Energy (CFE) | Increases hourly CFE score from ~50% up to 85%–93% across evaluated regions | Unoptimized baseline | Sec. 5.1, Fig. 5, p. 127 |
| Embodied vs. Operational trade-off | Accounting for embodied carbon alters optimal battery sizing by up to 40%–60%, avoiding large net emissions spikes | Operational-only optimization | Sec. 5.2, Fig. 7, p. 128 |
| Operational emission reduction | Workload shifting alone achieves 12%–28% operational carbon reduction depending on renewable penetration | Carbon-agnostic execution | Sec. 5.3, Fig. 9, p. 129 |
| SLA / deadline violations | Zero violations; flexible workload delays restricted within strict application delay tolerances ($\le 24$h) | Strict application deadlines | Sec. 4.3, p. 125 |
| Latency / completion time | Flexible compute delayed by up to 4h–12h during low renewable periods; interactive services unaffected | Flat execution | Sec. 5.3, p. 129 |
| Capital expenditure / cost | Reduces required battery capacity by up to 30% by substituting expensive batteries with software workload shifting | Pure battery storage strategy | Sec. 5.4, Fig. 11, p. 130 |

## 5. Gap
- **Gap stated by the authors:**
  "Carbon Explorer operates primarily at the datacenter design and capacity planning stage... It models aggregated hourly workload envelopes rather than individual queue-level task arrivals, container orchestration lifecycles, or runtime network transfer latencies across datacenters."  [Source: Sec. 6, p. 131]
- **Gap we observe:**
  The framework uses coarse-grained hourly simulation for strategic infrastructure planning. It does not provide an online, run-time scheduling policy capable of making sub-minute or dynamic task dispatching decisions under stochastic job arrivals and unpredictable real-time forecast errors.

## 6. Relevance to our project
P03 highlights an essential insight: software workload shifting reduces the need to over-provision costly, carbon-intensive physical battery systems. For our project, we can cite Carbon Explorer to motivate why an intelligent RL software scheduler provides a far more sustainable and economical path to decarbonization than hardware over-provisioning.
