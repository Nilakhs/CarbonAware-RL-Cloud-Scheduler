# P02 — Google Carbon-Aware Computing (Virtual Capacity Curves)

**Full citation:** Ana Radovanović, Ross Koningstein, Ian Schneider, Bokan Chen, Alexandre Duarte, Binz Roy, Diyue Xiao, Maya Haridasan, Patrick Hung, Nick Care, Saurav Talukdar, Eric Mullen, Kendal Smith, MariEllen Cottman, and Walfredo Cirne, "Carbon-Aware Computing for Datacenters", *IEEE Transactions on Power Systems*, Vol. 38, No. 2, pp. 1270–1280, March 2023 (published online May 2022).  
**DOI / link:** [https://doi.org/10.1109/TPWRS.2022.3173250](https://doi.org/10.1109/TPWRS.2022.3173250) (also [arXiv:2106.11750](https://arxiv.org/abs/2106.11750))  
**Type:** Journal     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5 [production system; data open, proprietary Borg control code], Q8: 1.0)*  

---

## 1. Problem addressed
Hyperscale cloud data centers consume significant electrical power, and their carbon footprint depends heavily on hourly grid generation mixes that vary by geography and time of day. Most cloud workloads are run carbon-agnostically, missing opportunities to absorb intermittent renewable power during clean energy surplus periods. The operational challenge is to shape the electricity consumption of large-scale datacenter clusters dynamically without degrading user-facing latency or violating completion guarantees for massive daily batch pipelines.  [Source: Sec. I, pp. 1270–1271]

## 2. Approach (the core idea)
The authors describe Google's production **Carbon-Intelligent Compute Management System**. The core mechanism is the daily generation of **Virtual Capacity Curves (VCCs)** for each datacenter cluster. A VCC imposes dynamic, risk-aware hourly limits on non-urgent, flexible computing capacity: restricting cluster capacity during hours when the local power grid is carbon-intensive, and expanding capacity when renewable energy generation is abundant, while mathematically guaranteeing that total 24-hour compute allocation meets aggregate workload demand.  [Source: Sec. II & III, pp. 1271–1275]

## 3. Methodology
- **Scheduling decision:** When and resource size (temporal shaping and capacity throttling per cluster; spatial workload rebalancing across clusters is discussed as multi-cluster extension).
- **Workload type:** Mixed production cloud workloads partitioned into:
  - Latency-sensitive serving (user-facing search, video serving, maps);
  - Flexible batch computing (indexing, large-scale ML model training, video transcoding).
- **Dynamic or online?** Yes; day-ahead optimization updated with intraday real-time tracking adjustments.
- **For non-RL papers (Heuristic / Optimization used):**
  - Formulated as a constrained convex optimization problem with probabilistic chance constraints. It solves for hourly capacity allocations $c_t$ over a 24-hour horizon:
    $$\min_{\{c_t\}} \sum_{t=1}^{24} I_t \cdot P(c_t) \quad \text{s.t.} \quad \sum_{t=1}^{24} c_t \ge D_{total}, \quad c_{min} \le c_t \le c_{max}$$
    where $I_t$ is forecasted hourly marginal/average carbon intensity, and $P(c_t)$ is the estimated cluster power consumption function.
- **Carbon data source and region:** Day-ahead hourly carbon intensity signals provided by external carbon data partner (Tomorrow / Electricity Maps) across global Google data center regions (US ISOs and Europe).
- **Workload trace / dataset:** Production telemetry and cluster resource traces from Google's global Borg infrastructure over multiple seasons.
- **Simulator or real system:** Deployed operational production system running across Google's worldwide datacenter fleet.
- **Baselines compared:** 
  - Flat/unshaped baseline (running flexible computing load constantly across all 24 hours).
  - Business-as-usual unconstrained datacenter operation.  
[Source: Sec. II & III, pp. 1272–1276]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon-aware load shifting | Successfully shifts gigawatt-hours of flexible computing capacity away from carbon peaks to clean valleys globally | Unshaped flat allocation baseline | Sec. IV, Fig. 5 & 6, pp. 1277–1278 |
| Power reduction during peak carbon hours | Power consumption of flexible compute curtailed by tens of megawatts per cluster during high-carbon periods | Normal unconstrained peak power | Sec. IV, Fig. 7, p. 1278 |
| SLA / deadline violations | Zero daily throughput loss; 100% of planned daily flexible computing demand met over 24-hour cycles | Standard daily SLA targets | Sec. IV, p. 1277 |
| Latency / completion time | Serving workloads experience zero latency degradation; flexible batch completion delayed within acceptable 24h limits | Baseline serving SLAs | Sec. IV-A, p. 1277 |
| Energy / cost | Net daily compute energy conserved or neutral; operational carbon footprint reduced | Carbon-agnostic execution | Sec. IV-B, pp. 1278–1279 |

## 5. Gap
- **Gap stated by the authors:**
  "Our current formulation primarily relies on day-ahead carbon and workload forecasts. Intra-hour prediction errors, sudden renewable curtailment events, and fast-ramping peaker plants can lead to divergence between planned and realized carbon savings... Further work is required to integrate real-time fine-grained dynamic feedback control at sub-hourly resolution."  [Source: Sec. V, p. 1279]
- **Gap we observe:**
  The system uses day-ahead convex optimization based on coarse aggregate cluster capacity curves (macro-level throttling) rather than online, per-job scheduling decisions. Individual job queue dynamics, task dependencies (DAGs), and fine-grained resource allocations are left to local Borg schedulers, which can lead to localized queue build-ups when capacity is throttled.

## 6. Relevance to our project
P02 is the definitive industrial benchmark proving that large-scale temporal load shifting works in production. We can adapt its concept of flexible vs. serving workload partitioning and use its mathematical model of capacity throttling under deadline guarantees as a baseline for our online RL scheduler.
