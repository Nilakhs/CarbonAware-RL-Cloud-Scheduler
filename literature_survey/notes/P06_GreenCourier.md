# P06 — GreenCourier (Serverless Carbon-Aware Scheduling)

**Full citation:** Mohak Chadha, Thandayuthapani Subramanian, Eishi Arima, Michael Gerndt, Martin Schulz, and Osama Abboud, "GreenCourier: Carbon-Aware Scheduling for Serverless Functions", in *Proceedings of the 9th International Workshop on Serverless Computing (WoSC@Middleware '23)*, Bologna, Italy, ACM, pp. 49–54, December 2023.  
**DOI / link:** [https://doi.org/10.1145/3631295.3631396](https://doi.org/10.1145/3631295.3631396) (also [arXiv:2310.20375](https://arxiv.org/abs/2310.20375))  
**Type:** Conference     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*  

---

## 1. Problem addressed
Serverless Function-as-a-Service (FaaS) platforms execute short-lived, event-driven functions on behalf of cloud users, but existing schedulers (such as the default Kubernetes scheduler) place invocations based solely on cluster resource availability or geographic proximity without considering regional carbon intensity. Electricity grids powering geographically distributed data centers exhibit sharp temporal and spatial variations in carbon intensity. Conventional latency-driven placement misses significant opportunities to route flexible serverless requests to regions currently powered by low-carbon energy.  [Source: Sec. 1, pp. 49–50; arXiv Sec. 1, p. 1]

## 2. Approach (the core idea)
GreenCourier is a runtime infrastructure framework and scheduling plugin built natively into the Kubernetes Scheduling Framework. When a Knative serverless function pod is triggered, GreenCourier queries real-time regional marginal carbon intensity via the Carbon-Aware SDK and dynamically routes the pod across geographically dispersed Kubernetes clusters peered through Liqo (using Virtual Kubelets), prioritizing low-carbon regions while balancing execution latency.  [Source: Sec. 3, pp. 50–51; arXiv Sec. 3, pp. 2–3]

## 3. Methodology
- **System role:** Runtime infrastructure framework and spatial scheduling plugin (integrating Kubernetes Scheduling Framework, Knative FaaS, and Liqo multi-cluster virtualization).
- **Scheduling decision:** Where (spatial workload shifting across geographically distributed regional Kubernetes clusters; no temporal delay).
- **Workload type:** Serverless FaaS (Function-as-a-Service) functions adapted from the FunctionBench benchmark suite (image processing, data analysis, web serving, video generation).
- **Dynamic or online?** Yes; online invocation-time scheduling evaluated under production serverless arrival traces.
- **For non-RL papers (Heuristic / Optimization used):**
  - Custom Kubernetes Scheduling Framework plugin implementing the Score and Filter extension points.
  - Candidate clusters are filtered based on memory/CPU capacity and scored inversely proportional to the real-time Marginal Operating Emissions Rate (MOER) obtained from WattTime.
- **Carbon data source and region:** 
  - Real-time marginal carbon intensity (MOER) from WattTime via the Green Software Foundation Carbon-Aware SDK.
  - Evaluated across four European cloud regions: Spain (ES), France (FR), Belgium (BE), and the Netherlands (NL).
- **Workload trace / dataset:** 
  - FunctionBench benchmark suite functions implemented using Knative serving with gRPC invocation triggers.
  - Invocations driven by realistic serverless request patterns derived from public cloud production traces.
- **Simulator or real system:** Real testbed deployment on Google Kubernetes Engine (GKE) comprising 4 regional clusters federated via Liqo.
- **Baselines compared:** 
  - **Default Kubernetes Scheduler:** Standard round-robin / resource-balanced pod placement within the local initiating cluster without carbon awareness.
  - **GeoAware Scheduler:** Geographically closest region routing policy designed purely to minimize network propagation latency without carbon consideration.  
[Source: Sec. 3 & 4, pp. 50–53; arXiv Sec. 3 & 4, pp. 2–5]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Average carbon emission reduction | 13.25% relative reduction in carbon emissions per invocation | Baseline average across all tested functions | Sec. 4.3, p. 53; arXiv p. 4 |
| Carbon reduction vs. Default Scheduler | 8.7% relative reduction in carbon emissions per invocation | Default Kubernetes Scheduler | Sec. 4.3, p. 53; arXiv p. 4 |
| Carbon reduction vs. GeoAware Scheduler | 17.8% relative reduction in carbon emissions per invocation | GeoAware Scheduler (latency-optimized) | Sec. 4.3, p. 53; arXiv p. 4 |
| Execution slowdown vs. Default Scheduler | 10.26% relative increase in geometric mean execution time | Default Kubernetes Scheduler | Sec. 4.3, p. 53; arXiv p. 5 |
| Execution slowdown vs. GeoAware Scheduler | 16.24% relative increase in geometric mean execution time | GeoAware Scheduler | Sec. 4.3, p. 53; arXiv p. 5 |
| Speedup of GeoAware over Default | 4.2% relative speedup (lower latency) | Default Kubernetes Scheduler | Sec. 4.3, p. 53; arXiv p. 5 |
| Scheduling scoring latency | 539 ms average scoring and scheduling time per pod | Default Kubernetes Scheduler (515 ms) | Sec. 4.2, Fig. 4, p. 52; arXiv p. 4 |
| Pod binding latency | 8.28 s average binding time across multi-cluster Liqo virtual kubelets | Single-cluster local worker binding (4.53 s) | Sec. 4.2, p. 52; arXiv p. 4 |
| SLA / deadline violations | Not stated in paper (functions executed best-effort; latency measured without explicit deadline drop) | Strict deadline limit | Sec. 4.3, pp. 52–53 |

## 5. Gap
- **Gap stated by the authors:**
  "Routing function invocations to remote clusters incurs additional network latency for container creation and data transfers... Additionally, cold-start penalties are exacerbated when pods are initialized in newly targeted remote regions. The framework currently relies synchronously on external carbon API availability and does not incorporate local forecast caching or predictive pre-warming."  [Source: Sec. 5, p. 54; arXiv Sec. 5, p. 5]
- **Gap we observe:**
  GreenCourier relies exclusively on reactive spatial routing and greedy instantaneous MOER scoring; it contains no temporal shifting mechanism to delay delay-tolerant functions, no reinforcement learning to balance latency-carbon trade-offs dynamically, and suffers from a significant cross-cluster binding overhead of 8.28 seconds via Liqo virtual kubelets.

## 6. Relevance to our project
Provides empirical evidence from a real GKE Kubernetes/Knative testbed showing that spatial routing alone achieves 8.7% to 17.8% relative carbon reductions at the expense of a 10.3% to 16.2% geometric mean latency increase. Serves as a key real-system baseline for serverless workload dispatching.