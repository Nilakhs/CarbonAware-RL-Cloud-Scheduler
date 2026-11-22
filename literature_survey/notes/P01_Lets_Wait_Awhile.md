# P01 — Let's Wait Awhile (Temporal Workload Shifting)

**Full citation:** Philipp Wiesner, Ilja Behnke, Dominik Scheinert, Kordian Gontarska, and Lauritz Thamsen, "Let's Wait Awhile: How Temporal Workload Shifting Can Reduce Carbon Emissions in the Cloud", in *Proceedings of the 22nd International Middleware Conference (Middleware '21)*, Virtual Event, Canada, ACM, pp. 260–272, December 2021.  
**DOI / link:** [https://doi.org/10.1145/3464298.3493399](https://doi.org/10.1145/3464298.3493399) (also [arXiv:2110.13234](https://arxiv.org/abs/2110.13234))  
**Type:** Conference     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 8.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*  

---

## 1. Problem addressed
The carbon intensity of public electricity grids fluctuates heavily over time due to time-varying demand and intermittent renewable power generation such as wind and solar. Cloud computing data centers traditionally execute delay-tolerant background jobs immediately upon arrival or at fixed nighttime hours regardless of grid conditions, incurring avoidable operational carbon emissions. While prior work predominantly emphasizes geographic spatial workload migration across regions, the standalone potential and operational dynamics of temporal workload shifting remain under-characterized across diverse energy markets.  [Source: Sec. 1, pp. 260–261]

## 2. Approach (the core idea)
The authors formulate and simulate temporal workload shifting policies for flexible cloud compute jobs (periodic maintenance/testing and ad-hoc batch processing). Schedulers ingest short-term carbon intensity forecasts to defer or advance task execution to predicted local carbon minima within user-defined flexibility windows ($\pm \Delta t$), evaluating the trade-offs between allowed delay, forecast uncertainty, and realized carbon emission reductions.  [Source: Sec. 1 & Sec. 3, pp. 261–264]

## 3. Methodology
- **Scheduling decision:** When (pure temporal shifting within local cluster/region; no spatial migration).
- **Workload type:** Batch and periodic workloads (Scenario 1: Periodic recurring tasks such as CI/CD nightly builds and backups; Scenario 2: Ad-hoc batch tasks such as ML model training and scientific simulations).
- **Dynamic or online?** Yes; online scheduling based on rolling forecast windows and arrival triggers.
- **For non-RL papers (Heuristic / Optimization used):**
  - Evaluates heuristic scheduling rules: (1) Immediate execution (FCFS baseline); (2) Fixed nighttime execution (02:00 local time); (3) Carbon-optimal planning under perfect foresight; and (4) Forecast-driven heuristic that schedules tasks at predicted lowest carbon intensity intervals within deadline boundaries $[t_{arr}, t_{arr} + \Delta t]$.
- **Carbon data source and region:** Real grid carbon intensity traces for the entire year 2020 (hourly resolution) across four regions:
  - Germany (DE) — ENTSO-E transparency platform / Agora Energiewende.
  - Great Britain (GB) — National Grid ESO carbon API.
  - France (FR) — RTE / eco2mix.
  - California (CA) — California ISO (CAISO) OASIS platform.
- **Workload trace / dataset:** Synthesized periodic service runs (lengths 1h to 4h) and ad-hoc job arrival traces derived from empirical batch workload distributions.
- **Simulator or real system:** Event-driven Python simulation framework (`simulate.py` / `leaf`), open-sourced at GitHub repository `dos-group/lets-wait-awhile`.
- **Baselines compared:** 
  - Immediate execution (greedy First-Come-First-Served upon job arrival).
  - Fixed-time scheduling (executing during fixed nighttime low-demand valley at 02:00).
  - Perfect foresight upper bound.  
[Source: Sec. 3, 4 & 5, pp. 263–268]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon reduction (Germany, $\pm 8$h flexibility) | 11.2% lower carbon emissions | Immediate execution baseline | Sec. 5.1, p. 267 |
| Carbon reduction (California, semi-weekly flexibility) | Up to 33.7% lower carbon emissions | Immediate execution baseline | Sec. 5.2, Fig. 6, p. 268 |
| Regional carbon reduction range | 2.5% to 18.9% (up to 33.7% in CA) across scenarios | Immediate execution baseline | Sec. 5.1 & 5.2, pp. 266–268 |
| Forecast error impact | 5% forecast error reduces emission savings by less than 1.5 percentage points compared to perfect foresight | Perfect foresight baseline | Sec. 5.3, Fig. 8, p. 269 |
| SLA / deadline violations | 0% (all tasks guaranteed to finish within flexibility window $\Delta t$) | Strict deadline limit | Sec. 3.2, p. 264 |
| Latency / completion time | Jobs delayed up to maximum window size ($\Delta t = 4h, 8h, 24h$) | Immediate completion | Sec. 5.1, p. 266 |
| Energy / cost | Total compute energy unchanged (pure load shifting without scaling) | Unshifted compute | Sec. 3.1, p. 263 |

## 5. Gap
- **Gap stated by the authors:**
  "We do not consider spatial workload shifting across multiple geographically distributed datacenters... In addition, we assume tasks have fixed, non-malleable execution durations and cannot adaptively adjust resource allocations (e.g., CPU cores or frequencies) dynamically in response to transient carbon spikes during execution."  [Source: Sec. 6, p. 270]
- **Gap we observe:**
  The heuristic relies on static thresholding or greedy forecast selection, lacking adaptive learning capabilities when grid forecast errors are non-stationary or severe. It models fixed task execution times and ignores server queue contention, resource interference, and dynamic arrival rate surges that occur in real multi-tenant cloud clusters.

## 6. Relevance to our project
Demonstrates that temporal shifting alone delivers double-digit carbon reductions (11%–34%) without requiring costly cross-region network migrations. Provides real 2020 grid datasets (DE, GB, FR, CA) and evaluation protocols that we can adopt to benchmark our RL scheduler.
