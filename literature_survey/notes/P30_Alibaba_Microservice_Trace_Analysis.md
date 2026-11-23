# P30 — Characterizing Microservice Dependency and Performance: Alibaba Trace Analysis

**Full citation:** Shutian Luo, Huanle Xu, Chengzhi Lu, Kejiang Ye, Guoyao Xu, Liping Zhang, Yu Ding, Jian He, and Chengzhong Xu, "Characterizing Microservice Dependency and Performance: Alibaba Trace Analysis", in *Proceedings of the 2021 ACM Symposium on Cloud Computing (SoCC ’21)*, Seattle, WA, USA, November 2021, pp. 412–426. **(Best Paper Award)**
**DOI / link:** [https://doi.org/10.1145/3472883.3487003](https://doi.org/10.1145/3472883.3487003) (Open-access archival PDF at `literature_survey/papers/P30_Luo_Alibaba_Microservice_Trace.pdf`)
**Open-source dataset:** [https://github.com/alibaba/clusterdata/tree/master/cluster-trace-microservices-v2021](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-microservices-v2021)
**Type:** Conference (ACM SoCC '21 Best Paper)     **Group:** G5 (Simulators, testbeds, and cloud traces)
**Quality score:** 7.0 / 8  *(Lenient: 7.5 / 8)*
*(Q1: 1.0, Q2: 1.0, Q3: 0.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*
*(Note on score and primary source audit: Full 15-page ACM SoCC '21 Best Paper PDF downloaded to `literature_survey/papers/P30_Luo_Alibaba_Microservice_Trace.pdf` via SIAT author-archived repository; converted to structured Markdown at `literature_survey/markdown_papers/P30.md`; dataset schemas and trace repositories verified against Alibaba Cluster Data).*

---

## 1. Overview & Core Motivation
- **Context & Problem Statement:**
  - Modern cloud computing architectures have transitioned decisively from monolithic applications to loosely coupled, lightweight microservices deployed in containers.
  - While academic benchmarks (e.g., DeathStarBench, $\mu$Suite, Acme Air) provide useful testbeds, they are limited to tiny topologies (<40 services) with static call graphs and cannot capture the structural dynamics, traffic variance, and interference patterns of hyperscale production clusters.
  - Prior cloud trace releases (Google 2011/2019, Alibaba 2017/2018 batch traces, Azure Functions) focused primarily on batch tasks, virtual machines, or isolated function invocations without capturing **inter-service call graphs, RPC/MQ communication paradigms, and microservice-batch co-location dynamics**.
- **Key Contributions of the Paper:**
  - **First Large-Scale Production Microservice Trace:** Analyzes over **10 billion call traces** spanning **20,000+ microservices** deployed across **10,000+ bare-metal nodes** during a 12-hour production window in Alibaba Cloud.
  - **Graph Anatomy of Microservice Call Graphs:** Reveals fundamental topological differences between microservice call graphs and traditional batch Directed Acyclic Graphs (DAGs).
  - **Characterization of Inter-Service Dependencies:** Formalizes cyclic dependencies, strongly coupled invocations, and parallel dependency patterns.
  - **Runtime Performance & Resource Interference Analysis:** Demonstrates that microservice response times (RTs) are extraordinarily sensitive to CPU contention but robust against memory contention.
  - **Theoretical & Generative Call Graph Model:** Proposes a stochastic generative model based on graph learning (*InfoGraph*) and degree distributions with proven theorems on call depth and node count, reproducing authentic production graph properties.

---

## 2. Core Findings & Microservice Architecture

### 2.1 Microservice Architecture in Alibaba Production Clusters
- **Host Infrastructure:** Over 10,000 bare-metal physical hosts running Alibaba's Uniform Resource Management (URM).
- **Hybrid Co-location:** Online microservice containers are co-located with offline batch jobs on the same physical machines to maximize hardware utilization. Offline batch jobs run inside lightweight secure containers (Kata Containers / microVMs) to enforce kernel and hardware isolation.
- **Communication Paradigms:**
  1. *Inter-Process Communication (IP):* Direct, low-latency interaction typically between stateless frontends and local stateful caches (e.g., Memcached).
  2. *Remote Procedure Call (RPC):* Synchronous, two-way request-response communication (requires downstream microservice to reply to upstream microservice).
  3. *Message Queue (MQ):* Asynchronous, one-way indirect communication where the upstream microservice writes to a distributed queue and continues execution without blocking; downstream microservice consumes asynchronously.

### 2.2 Structural Divergence from Traditional Batch DAGs
1. **Heavy-Tailed Graph Size:**
   - Over 10% of microservice call graphs span more than **40 microservice stages**, with deep call chains extending up to 15+ tiers. Traditional big-data DAGs (e.g., Spark, MapReduce) typically consist of only 2–5 stages.
2. **Tree-Like Hierarchical Topology:**
   - In microservice call graphs, the vast majority of downstream microservices (DMs) have an **in-degree of exactly 1** (scattered invocation growing outward from the entering frontend service).
   - In contrast, batch DAGs feature numerous gather/shuffle stages where multiple parent tasks feed into a common reducer.
3. **Hot-Spot "Super Microservices":**
   - **5% of microservices handle 95% of total cluster invocations** and appear in nearly 90% of all call graphs. These centralized hub microservices (e.g., user authentication, payment processing, catalog routing) require massive multi-container scaling.
4. **Dynamic Multi-Topology Execution:**
   - Unlike static batch DAGs that execute a deterministic graph structure upon job submission, the exact call graph of a single online service fluctuates dynamically based on user state, input parameters (e.g., promotional coupons, cart contents), and cache hit/miss status. Over 10% of services exhibit **9 or more topologically distinct graph classes**.

---

## 3. Microservice Dependencies & Performance Interference

### 3.1 Inter-Service Dependency Patterns
- **Cyclic Dependencies:** 7.6% of RPC-RPC microservice pairs exhibit cyclic or reciprocal invocation patterns. Identifying these cycles enables co-locating interfaces or applying asynchronous timeouts to prevent cascading deadlocks.
- **Strongly Coupled Invocations:** Over 10% of microservice pairs exhibit high invocation frequency where the upstream service repeatedly calls the same downstream service. 17% of these pairs do not share the downstream service with any other microservice; co-locating or merging these interfaces eliminates network serialization overhead.
- **Message Queues in Deep Graphs:** As call depth increases beyond 4 tiers, the proportion of Message Queue (MQ) invocations rises sharply. MQ decouples downstream processing, preventing deep tail-latency amplification.

### 3.2 Performance Interference: CPU vs. Memory Sensitivity
- **CPU Sensitivity:** Microservice 75th-percentile Response Time (RT) is acutely degraded by CPU interference:
  - **A host CPU utilization increase from 10% to 30% causes a ~20% increase in average microservice RT.**
  - Microservice call rate per container (MCR) exhibits a strong positive Spearman correlation ($> 0.6$) with host CPU utilization, Young Generation Garbage Collection (GC) count, and Young GC pause time.
- **Memory Robustness:**
  - Memory utilization shows near-zero or negative correlation with MCR and request load.
  - Container memory footprints remain nearly constant at runtime (variance $< 10\%$). Memory interference from co-located batch tasks does not impact microservice RT until catastrophic out-of-memory swapping occurs.
- **Host CPU Variance & Scheduling Opportunity:**
  - The minute-by-minute variance in CPU utilization across physical hosts in the cluster reached **up to 20%**, indicating massive headroom for carbon- and latency-aware schedulers to balance load across underutilized servers.

---

## 4. Theoretical & Generative Graph Model

### 4.1 Generative Process
- **Node Classification:** Classifies microservices into 5 distinct roles: $\mathcal{L} = \{\text{database}, \text{Memcached}, \text{blackhole}, \text{relay}, \text{normal}\}$.
- **Iterative Growth:** Generates call graphs tier-by-tier using empirical branching distributions $F_h(j)$ (probability that node at tier $h$ spawns $j$ children) and communication assignment $G_{h+1}(\phi)$.
- **Graph Refinement:** Merges child nodes across parent pairs sharing the same functional label to accurately reflect the empirical multi-parent distribution $\Phi_h(m)$ without disrupting tree-like properties.

### 4.2 Theoretical Theorems
- **Theorem 6.1 (Call Depth Distribution):** Establishes the exact closed-form probability $\Gamma(k) = \Pr(h_s = k)$ that a generated graph has depth $k$, expressed as a product of non-termination probabilities across preceding tiers.
- **Theorem 6.2 (Node Count Distribution):** Derives the cumulative distribution of total microservices $N(G_s)$ across all graph tiers.
- **Validation:** Generated graphs achieve close agreement with empirical ground truth: **KL-divergence of 0.16 for call depth** and **0.05 for total microservice count**.

---

## 5. Limitations, Constraints & Research Gaps

### 5.1 Author-Identified Limitations
- **12-Hour Production Trace Window:** While spanning 10+ billion calls, the public trace covers a single 12-hour continuous production period, omitting multi-day diurnal patterns or seasonal shopping holidays (e.g., Singles' Day / Double 11).
- **Incomplete Call Tracing:** In a minor fraction of traces, downstream microservice identifiers were masked or omitted due to trace collector sampling thresholds.
- **Cross-Graph Node Sharing:** The generative model simulates individual service call graphs independently; global cross-graph multiplexing (sharing the identical 5% super-microservice nodes across diverse graphs) is left for future work.

### 5.2 Our Independent Critical Gaps
- **Lack of Native Carbon / Energy Telemetry:** The original Alibaba 2021 trace records CPU utilization, memory usage, and RPC response times, but does not natively record per-server energy consumption ($W$) or data center grid carbon intensity ($\text{gCO}_2/\text{kWh}$).
- **Integration with Carbon Schedulers:** Carbon-aware RL schedulers (such as P21, P24, and our project) must couple the Alibaba microservice execution graphs with server power models (e.g., SPECpower / RAPL) and regional grid carbon time series (e.g., EIA-930, WattTime) to evaluate carbon-performance tradeoffs.

---

## 6. Relevance to Our Project & Quality Score Breakdown

### 6.1 Relevance to Project
Alibaba Trace 2021 is the gold-standard cloud microservice dataset for Group G5:
1. **Canonical Workload Driver:** Provides authentic production-grade microservice call graphs and arrival rates to drive simulated cloud testbeds (e.g., Vessim, SustainGym).
2. **Empirical Grounding for Co-Location:** The paper's core finding—that co-located CPU contention degrades tail latency while memory contention does not—directly informs RL scheduling reward functions that balance green batch jobs against latency-sensitive microservices.
3. **Realistic DAG/Tree Heterogeneity:** Replaces oversimplified synthetic DAGs with empirical heavy-tailed, dynamic tree-structured microservice graphs.

### 6.2 Quality Score Breakdown (7.0 / 8.0, Lenient: 7.5 / 8.0)

| Rubric Item | Score | Evidence & Justification |
| :--- | :---: | :--- |
| **Q1: Relevance to Carbon-Aware Cloud Scheduling** | **1.0** | Foundational production cloud trace used directly by modern carbon-aware cloud schedulers to model realistic microservice execution and batch co-location. |
| **Q2: Problem Formulation & Technical Rigor** | **1.0** | Rigorous study analyzing 10+ billion calls, 20,000+ microservices, 10,000+ bare-metal hosts; formalizes graph learning embeddings and proves Theorems 6.1 and 6.2. |
| **Q3: Carbon Modeling & Trace Grounding** | **0.0** | **0.0 under strict dynamic grid-carbon rule** (P30 characterizes compute CPU, memory, and RPC call traces, but contains zero carbon intensity data, emissions calculations, or power/energy traces; Lenient proxy score: 0.5 as workload driver). |
| **Q4: Energy/Workload & Systems Grounding** | **1.0** | Grounded in massive production telemetry from 10,000+ Alibaba bare-metal hosts running Kata Containers, measuring CPU, memory, Young/Old GC, and RPC latencies. |
| **Q5: Baseline & Experimental Comparison** | **1.0** | Comprehensive comparison against DeathStarBench, $\mu$Suite, Acme Air, Google traces, and prior Alibaba batch traces; verifies generator with low KL-divergence (0.05–0.16). |
| **Q6: Clarity of Results & Empirical Findings** | **1.0** | Crystal-clear empirical discoveries: 10% of graphs have >40 stages, 5% super microservices handle 95% of calls, 30% CPU utilization degrades RT by 20%. |
| **Q7: Open Science, Artifacts & Reproducibility** | **1.0** | Best Paper Award at ACM SoCC '21; dataset fully open-sourced on GitHub at `alibaba/clusterdata`; detailed documentation, schemas, and processing scripts provided. |
| **Q8: Critical Assessment, Constraints & Gaps** | **1.0** | Candidly analyzes 12-hour trace sampling bounds, missing call identifiers, cross-graph node sharing constraints, and lack of direct power instrumentation. |
| **Total Quality Score** | **7.0 / 8.0** | **Strict Score: 7.0 / 8.0 (Lenient: 7.5 / 8.0). Essential empirical workload foundation for cloud microservices and datacenter scheduling.** |
