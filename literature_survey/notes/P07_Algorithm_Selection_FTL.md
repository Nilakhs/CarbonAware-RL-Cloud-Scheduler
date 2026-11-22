# P07 — Data-Driven Algorithm Selection (FTL Meta-Algorithm)

**Full citation:** Roozbeh Bostandoost, Walid A. Hanafy, Adam Lechowicz, Noman Bashir, Prashant J. Shenoy, and Mohammad Hajiesmaili, "Data-driven Algorithm Selection for Carbon-Aware Scheduling", in *ACM SIGEnergy Energy Informatics Review (EIR)*, Vol. 4, No. 5, pp. 28–34, December 2024 (originally presented at the 3rd Workshop on Sustainable Computer Systems, *HotCarbon '24*).  
**DOI / link:** [https://doi.org/10.1145/3727200.3727222](https://doi.org/10.1145/3727200.3727222)  
**Type:** Journal / Workshop     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 7.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 0.5)*  

---

## 1. Problem addressed
A variety of carbon-aware scheduling heuristics have been proposed for delay-tolerant batch computing, ranging from simple single-threshold rules to sophisticated double-threshold and forecast-driven policies. However, the performance of each heuristic depends heavily on localized grid dynamics, fluctuating carbon intensity distributions, and specific job duration distributions. A heuristic tuned to achieve optimal carbon savings in one geographic region or season often performs poorly in another, requiring continuous manual hyperparameter re-tuning.  [Source: Sec. 1, pp. 28–29]

## 2. Approach (the core idea)
The authors formulate carbon-aware scheduling as an online algorithm selection problem. They introduce FTL (Follow the Leader), a lightweight data-driven meta-algorithm that tracks the recent historical performance of a candidate pool of carbon-aware scheduling algorithms over a rolling window. At runtime, FTL dynamically selects and executes the specific heuristic that yielded the lowest carbon emissions over the recent past, adapting seamlessly to regional energy variations without hyperparameter retuning.  [Source: Sec. 2 & 3, pp. 29–31]

## 3. Methodology
- **System role:** Meta-algorithmic online optimizer and algorithm selector.
- **Scheduling decision:** When (temporal workload shifting within a single region; batch task execution deferred within deadline bounds).
- **Workload type:** Delay-tolerant batch computing workloads with defined deadlines and varying job durations.
- **Dynamic or online?** Yes; online meta-algorithm running at decision epochs with a sliding historical performance observation window.
- **For non-RL papers (Heuristic / Optimization used):**
  - FTL (Follow the Leader) meta-algorithm inspired by online learning theory.
  - Candidate algorithm pool consists of parameterized heuristic rules:
    - *Single-Threshold (ST[X]):* Executes tasks only when carbon intensity drops below percentile threshold $X$.
    - *Double-Threshold (DT[X, Y]):* Postpones execution until carbon drops below $X$; forces execution if time runs out or carbon exceeds safety threshold $Y$.
- **Carbon data source and region:** 
  - Real hourly grid carbon intensity traces spanning multiple diverse geographic regions:
    - Ontario, Canada (IESO) — nuclear and hydro dominant grid.
    - California, USA (CAISO) — solar-heavy grid with pronounced duck curve.
    - France (RTE) — nuclear baseline grid with low baseline volatility.
    - New South Wales, Australia (AEMO) — coal and intermittent wind/solar mix.
- **Workload trace / dataset:** Batch job arrival distributions and task duration profiles synthesized from standard cluster batch processing logs.
- **Simulator or real system:** Trace-driven Python simulation framework evaluating multi-region scheduling over annual carbon traces.
- **Baselines compared:** 
  - **Carbon-Agnostic Scheduling:** Immediate FCFS execution upon job arrival.
  - **Static Heuristics:** Individual fixed heuristics evaluated across all regions without adaptive switching (e.g., ST[35], DT[40, 60]).
  - **Closest Static Runner-Up:** The best single static heuristic identified via post-hoc grid-search for each specific region.  
[Source: Sec. 3 & 4, pp. 30–33]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon reduction vs. Best Runner-Up | 8.2% relative reduction in carbon emissions | Closest static runner-up heuristic | Sec. 4, p. 32 |
| Carbon reduction vs. Carbon-Agnostic | 14.0% relative reduction in carbon emissions | Carbon-agnostic immediate execution | Sec. 4, p. 32 |
| Regional adaptability | Outperformed static heuristics across all 4 regions (Ontario, California, France, NSW) without regional parameter retuning | Fixed single-threshold heuristics (e.g., ST[35]) | Sec. 4, Fig. 2 & 3, pp. 31–32 |
| SLA / deadline violations | 0% (all candidate heuristics in the selection pool enforce strict task deadlines) | Maximum allowed deadline | Sec. 3.1, p. 30 |
| Latency / makespan | Workloads deferred up to task deadline limits; trade-off bounded by user-configured flexibility | Immediate execution | Sec. 3.1, p. 30 |
| Energy consumption | Total compute energy identical (temporal shifting changes timing, not compute power) | Unshifted compute baseline | Sec. 3, p. 30 |

## 5. Gap
- **Gap stated by the authors:**
  "FTL relies on recent historical performance to predict near-future algorithm efficacy, which can result in switching lag when abrupt, unseasonal weather shifts suddenly alter grid carbon profiles... Furthermore, our evaluation is confined to independent batch jobs and does not evaluate multi-stage interdependent DAG workflows or interactive cloud microservices."  [Source: Sec. 5, p. 34]
- **Gap we observe:**
  The algorithm selection pool is restricted to simple static heuristics (ST and DT); it does not evaluate whether a Reinforcement Learning agent could dynamically synthesize hybrid scheduling policies that surpass all fixed heuristics, nor does it consider spatial shifting or dynamic resource scaling.

## 6. Relevance to our project
Confirms that no single heuristic dominates across varying regional electricity grids and that meta-adaptation yields an additional 8.2% carbon reduction over the best fixed heuristic. Supports our RL scheduler thesis: learning-based adaptability is essential for multi-region or temporally volatile cloud environments.