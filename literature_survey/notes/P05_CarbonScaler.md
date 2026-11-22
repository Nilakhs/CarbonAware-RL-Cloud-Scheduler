# P05 — CarbonScaler (Workload Elasticity Scaling)

**Full citation:** Walid A. Hanafy, Qianlin Liang, Noman Bashir, David Irwin, and Prashant Shenoy, "CarbonScaler: Leveraging Cloud Workload Elasticity for Optimizing Carbon-Efficiency", *Proceedings of the ACM on Measurement and Analysis of Computing Systems (POMACS)*, Vol. 7, No. 3, Article 57, 28 pages, December 2023 (presented at ACM SIGMETRICS '23).  
**DOI / link:** [https://doi.org/10.1145/3626788](https://doi.org/10.1145/3626788) (also [arXiv:2306.07474](https://arxiv.org/abs/2306.07474))  
**Type:** Journal     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 8.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0 [code and trace datasets open source], Q8: 1.0)*  

---

## 1. Problem addressed
Existing carbon-aware scheduling methods for cloud applications predominantly treat tasks as binary all-or-nothing units: they either run at a fixed server allocation or are completely suspended/deferred until greener hours. However, modern cloud applications exhibit horizontal elasticity—they can dynamically scale the number of allocated parallel instances (e.g., workers, pods, or VM instances) up or down during runtime. Relying solely on binary pause/resume mechanisms leads to underutilized server capacity during intermediate carbon periods and incurs significant performance degradation and checkpointing overhead.  [Source: Sec. 1 & 2, pp. 1–4]

## 2. Approach (the core idea)
The authors present **CarbonScaler**, a carbon-aware autoscaling framework that leverages cloud workload elasticity to optimize carbon-efficiency. Rather than simply delaying or pausing execution, CarbonScaler dynamically modulates an application's allocated compute parallelism in direct proportion to real-time grid carbon intensity signals: scaling out (allocating more workers) when carbon intensity is low to accelerate progress, and scaling in (reducing worker count to a minimal viable baseline) when carbon intensity is high, subject to strict user-defined completion deadlines and budget limits.  [Source: Sec. 3 & 4, pp. 4–11]

## 3. Methodology
- **Scheduling decision:** Resource size and when (dynamic horizontal elasticity scaling: determining the number of active parallel workers/nodes $N(t)$ at each time interval).
- **Workload type:** Elastic batch workloads with scalable parallelism:
  - Distributed machine learning model training (PyTorch / Horovod distributed data-parallel training);
  - Big data batch analytics (Apache Spark data processing pipelines);
  - Scalable video encoding and transcoding.
- **Dynamic or online?** Yes; online dynamic scaling adapting to incoming carbon forecasts and workload execution progress.
- **For non-RL papers (Heuristic / Optimization used):**
  - Formulated as a non-linear integer optimization problem that minimizes cumulative operational carbon emissions:
    $$\min_{\{N(t)\}} \sum_{t=1}^{T} I(t) \cdot P(N(t)) \cdot \Delta t \quad \text{s.t.} \quad \sum_{t=1}^{T} W(N(t)) \ge W_{target}, \quad N_{min} \le N(t) \le N_{max}$$
    where $I(t)$ is marginal carbon intensity, $P(N)$ is non-linear cluster power scaling, and $W(N)$ is the sub-linear scaling speedup model (accounting for Amdahl's law and distributed communication overhead). Solved online using a rolling-horizon dynamic programming heuristic.
- **Carbon data source and region:** Hourly marginal carbon intensity (MOER) data from WattTime and CAISO across multiple US grid balancing authorities (California/CAISO, Texas/ERCOT, Midcontinent/MISO).
- **Workload trace / dataset:** Production cluster traces from Alibaba cluster datasets and empirical execution profiles of real distributed ML benchmarks (BERT, ResNet-50) and Spark workloads.
- **Simulator or real system:** Validated on a physical cloud cluster testbed on Chameleon Cloud and scaled across trace-driven simulations.
- **Baselines compared:** 
  - Carbon-agnostic execution (running with static worker allocation $N_{static}$ to finish as fast as possible).
  - State-of-the-art suspend-resume policy (binary pausing when carbon intensity exceeds a threshold).
  - Best static scaling policy (fixed sizing chosen offline).  
[Source: Sec. 4 & 5, pp. 8–18]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon reduction (vs. Carbon-Agnostic) | 51% carbon savings | Standard carbon-agnostic execution baseline | Abstract & Sec. 6.1, Fig. 9, p. 19 |
| Carbon reduction (vs. Suspend-Resume) | 37% carbon savings | State-of-the-art suspend-resume policy | Abstract & Sec. 6.1, p. 19 |
| Carbon reduction (vs. Best Static) | 8% carbon savings | Best offline static scaling baseline | Abstract & Sec. 6.1, p. 19 |
| Scaling efficiency / Amdahl overhead | Exploits sub-linear scaling curves to prevent allocating workers in diminishing-returns regions during high carbon | Linear scaling assumption | Sec. 5.2, Fig. 6, p. 15 |
| SLA / deadline violations | 0% deadline violations across all evaluated workload benchmarks | User-specified deadline constraints | Sec. 6.2, p. 20 |
| Latency / completion time | Workload completion is delayed closer to the deadline boundary to maximize low-carbon compute absorption | Carbon-agnostic makespan | Sec. 6.2, Fig. 11, p. 21 |
| Energy / cost | Total financial cost is reduced by up to 22% alongside carbon cuts when dynamic electricity pricing is correlated | Static execution cost | Sec. 6.4, Table 3, p. 23 |

## 5. Gap
- **Gap stated by the authors:**
  "CarbonScaler assumes known application scaling models $W(N)$ (the relationship between worker count and speedup). For black-box or non-stationary applications whose scaling efficiency changes dynamically during runtime, profiling models may be inaccurate... Additionally, CarbonScaler currently operates within a single cloud cluster without spatial migration across datacenters."  [Source: Sec. 7, p. 24]
- **Gap we observe:**
  The dynamic programming rolling-horizon solver requires an explicit mathematical speedup function $W(N)$ and assumes carbon forecasts are reasonably accurate. When applications exhibit complex, non-deterministic performance scaling (e.g., varying batch sizes, straggler nodes) or volatile grid carbon prediction errors, the optimization can diverge. This makes elasticity control a compelling candidate for model-free Reinforcement Learning, which learns scaling policies directly from environment observations without requiring prior profiling.

## 6. Relevance to our project
P05 provides clear evidence that horizontal elasticity (varying instance counts) achieves dramatically higher carbon savings (51%) than simple binary temporal shifting (suspend-resume). This directly informs our RL state and action space design: our RL agent can output a continuous or discrete scaling action (number of pods/VMs) rather than just a binary "wait or run" decision.
