# P04 — Ecovisor (Virtual Energy System)

**Full citation:** Abel Souza, Noman Bashir, Jorge Murillo, Walid Hanafy, Qianlin Liang, David Irwin, and Prashant Shenoy, "Ecovisor: A Virtual Energy System for Carbon-Efficient Applications", in *Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS '23), Volume 2*, Vancouver, Canada, ACM, pp. 252–265, March 2023.  
**DOI / link:** [https://doi.org/10.1145/3575693.3575709](https://doi.org/10.1145/3575693.3575709) (also [arXiv:2210.04951](https://arxiv.org/abs/2210.04951))  
**Type:** Conference     **Group:** G1 (Carbon-aware scheduling without RL)  
**Quality score:** 8.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*  

---

## 1. Problem addressed
As modern computing systems increasingly draw power from intermittent renewable sources (solar and wind), the underlying energy supply becomes highly variable and unreliable. Traditional computer systems mask this physical power variability behind hardware abstractions (e.g., power supplies and backup generators), presenting a static, infinite-capacity energy illusion to software. Consequently, software applications cannot inspect real-time grid carbon intensity or dynamically adjust their execution policies, preventing them from optimizing application-specific **carbon-efficiency** (useful computation achieved per unit of carbon emitted).  [Source: Sec. 1 & 2, pp. 252–254]

## 2. Approach (the core idea)
The authors design, implement, and evaluate **Ecovisor**, a system virtualization layer that abstracts physical energy devices (grid power feeds, on-site solar panels, battery storage, and dynamic server power caps) into software-defined **virtual energy systems (vES)**. Much like a hypervisor multiplexes physical hardware among virtual machines, Ecovisor securely multiplexes physical energy infrastructure among untrusted containerized applications, exposing software APIs for real-time carbon signal visibility and energy control (e.g., virtual power limits, battery charging/discharging priorities, and workload pausing).  [Source: Sec. 3 & 4, pp. 254–259]

## 3. Methodology
- **Scheduling decision:** When and resource size (temporal throttling, server power capping via DVFS/RAPL, and virtual energy allocation per container).
- **Workload type:** Multi-tenant heterogeneous workloads:
  - Latency-sensitive interactive web services (HTTP server processing requests);
  - Delay-tolerant batch processing (scientific computations and data analytics);
  - Machine learning inference pipelines.
- **Dynamic or online?** Yes; real-time online virtualization operating at second-level time scales.
- **For non-RL papers (Heuristic / Optimization used):**
  - Linear virtual energy allocation model. Each application container is assigned a vES with time-varying virtual power capacity $P_v(t)$, battery storage slice $B_v(t)$, and carbon attribution $C_v(t)$. Applications run custom application-level adaptation policies (e.g., load shedding, service degradation, or temporal buffering) based on exposed carbon signals.
- **Carbon data source and region:** Real-time and historical marginal and average grid carbon intensity traces from ISO New England (ISO-NE) and CAISO, combined with on-site solar generation traces from an experimental solar array.
- **Workload trace / dataset:** Real traces from Wikipedia request access logs (interactive web traffic) and synthetic batch compute traces running on real hardware.
- **Simulator or real system:** Functional prototype implemented in Linux using cgroups, Docker, and hardware sensors (WattsUp power meters, programmable DC power supplies, and battery arrays).
- **Baselines compared:** 
  - Standard carbon-agnostic OS/container execution.
  - Uniform, system-wide power capping without application virtualization.
  - Static priority-based energy allocation.  
[Source: Sec. 4, 5 & 6, pp. 257–262]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Multi-tenant carbon-efficiency improvement | Up to 3.2x higher carbon-efficiency (work completed per gram of CO2) across heterogeneous apps | Carbon-agnostic execution baseline | Sec. 6.2, Fig. 8, p. 262 |
| Carbon emission reduction | Enables delay-tolerant batch applications to reduce carbon footprint by 38%–45% during low-renewable periods | Baseline unthrottled execution | Sec. 6.3, Fig. 10, p. 263 |
| Virtualization overhead | Ecovisor CPU overhead is less than 1.5% and scheduling control loop latency is under 5 ms | Direct bare-metal execution | Sec. 6.1, Table 1, p. 261 |
| SLA / deadline violations | Web serving applications maintain 99th-percentile latency SLO compliance under variable green power by dynamically shedding batch slices | Uniform power capping baseline | Sec. 6.2, Fig. 9, p. 262 |
| Battery lifetime preservation | Reduces unnecessary battery micro-cycling by 28% through software-directed charging priorities | Hardware-only battery management | Sec. 6.4, p. 264 |

## 5. Gap
- **Gap stated by the authors:**
  "Ecovisor provides the virtualization mechanisms and control APIs, but it delegates the actual scheduling policies to individual applications... Developing automated, intelligent policies that can optimize complex scheduling across multiple distributed servers remains an open challenge."  [Source: Sec. 7, p. 264]
- **Gap we observe:**
  Ecovisor is an enabling system abstraction (an OS/middleware hypervisor for energy), not an intelligent scheduling algorithm. Application developers are forced to write manual, heuristic control loops to respond to Ecovisor's signals. This makes Ecovisor an ideal execution runtime for an online Reinforcement Learning agent, which can learn optimal control policies over Ecovisor's virtualized energy APIs.

## 6. Relevance to our project
P04 provides the fundamental systems justification for our work. It proves that software-level control of energy and carbon is feasible in Linux containers with negligible overhead (<1.5%). Our RL scheduler can be conceptualized as the intelligent policy engine that sits on top of such virtualized energy interfaces.
