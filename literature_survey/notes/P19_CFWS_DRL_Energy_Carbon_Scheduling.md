# P19 — CFWS: DRL-Based Framework for Energy Cost and Carbon Footprint Optimization in Cloud Data Centers

**Full citation:** Da-Ming Zhao, Jian-Tao Zhou, and Ke-Qin Li, "CFWS: DRL-Based Framework for Energy Cost and Carbon Footprint Optimization in Cloud Data Centers", in *IEEE Transactions on Sustainable Computing*, Vol. 10, No. 1, pp. 95–107, Jan.–March 2025 (Published Early Access: 22 April 2024).  
**DOI / link:** [https://doi.org/10.1109/TSUSC.2024.3391791](https://doi.org/10.1109/TSUSC.2024.3391791)  
**Type:** Journal     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)  
**Quality score:** 6.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 0.5, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 0.5)*  
*(Note on score reconciliation: Reconciled from preliminary screening score of 7.5 to 6.5 following rigorous primary-source audits of Q3 [regional U.S. Department of Energy (DOE) Electricity Emission Factors / regional Carbon Footprint Rate (CFR) applied to brown energy without dynamic grid carbon intensity API time series: 0.5], Q7 [closed-source code: 0.5], and Q8 [partial discussion of constraints and trade-offs: 0.5]. If Q3 is credited at 1.0 for empirical U.S. Department of Energy (DOE) regional carbon factors and NREL wind traces, the score is 7.0/8. Note on Q3: Scored 0.5 under strict G3 rubric rules because although CFWS integrates empirical wind speed traces from NREL [converted to power via a simulated wind-turbine model] alongside regional U.S. Department of Energy (DOE) Electricity Emission Factors / regional Carbon Footprint Rate (CFR), it models carbon emissions via static regional emission factors applied to brown grid energy consumption rather than consuming dynamic, real-time third-party grid carbon-intensity time series [$g\text{CO}_2/\text{kWh}$ from Electricity Maps or WattTime]. Note on Q7: Scored 0.5 because although mathematical formulations, network structures, and simulation configurations are detailed in the paper text, source code and trained model weights are not hosted on a public open repository [GitHub/Zenodo]. Note on Q8: Scored 0.5 (Partly) because while the authors discuss operational cost–migration trade-offs in Section V and identify concrete future research directions in Section VI (including renewable energy generation forecasting, dynamic electricity pricing models, and multi-cloud/edge computing extensions), the paper does not include a dedicated, self-critical discussion of its own structural limitations or failure modes).*  

---

## 1. Problem addressed
The rapid proliferation of cloud computing and cloud data centers (CDCs) has triggered immense electrical energy consumption, resulting in steep operational electricity costs and significant greenhouse gas emissions. While integrating on-site Renewable Energy Sources (RES)—specifically wind turbines—offers a pathway toward green cloud computing, intermittent green generation coupled with volatile electricity pricing creates severe operational challenges.

Traditional cloud workload management and virtual machine (VM) consolidation techniques focus primarily on performance guarantees or static power efficiency, giving rise to major limitations:
1. **Uncoordinated Brown Energy Reliance:** Workload scheduling without awareness of temporal wind generation or spatial grid carbon intensity differences causes data centers to consume expensive and carbon-intensive "brown energy" from the conventional power grid.
2. **Virtual Machine (VM) Migration Overhead and Thrashing:** Consolidating workloads to power down underutilized servers can reduce energy usage, but aggressive or poorly timed VM migrations trigger substantial network bandwidth overhead, CPU throttling, and degraded user quality of service.
3. **Inaccurate Host Overload Detection:** Conventional host overload detection mechanisms rely on fixed static thresholds (e.g., 80% CPU utilization) or simple statistical heuristics (IQR, MAD, LR), failing to capture dynamic workload temporal trends. This causes either delayed migrations that lead to severe Service Level Agreement (SLA) violations or premature migrations that incur unnecessary migration penalties.
4. **Action Space Explosion in Multi-DC Environments:** As the numbers of data centers, physical machines (PMs), and virtual machines grow, the joint multi-dimensional decision space for VM migration and placement expands exponentially, rendering standard reinforcement learning algorithms intractable.  [Source: Sec. I, pp. 95–97; Sec. III, pp. 97–99]

## 2. Approach (the core idea)
The authors propose **CFWS** (**C**arbon **F**ootprint-aware **W**orkload **S**cheduling), a Deep Reinforcement Learning (DRL)-based framework designed to jointly optimize energy costs and carbon footprints across geographically distributed cloud data centers:

- **Geo-Distributed Hybrid Energy Management:** Coordinates workload allocation and VM placement across geographically distributed data centers powered by a combination of on-site renewable energy sources (RES: simulated wind turbines converting empirical NREL wind speed traces to electrical power) and conventional grid power ("brown energy").
- **TCN-MAD Adaptive Overload Detection:** Combines a Temporal Convolutional Network (TCN) with Median Absolute Deviation (MAD) to dynamically predict physical machine overload probabilities based on historical workload sequences. This allows the system to proactively adjust utilization thresholds, preventing unnecessary VM migrations and reducing SLA violations.
- **Flattened Action Space Representation:** Formulates the combinatorial migration decision space—selecting which VM to migrate, to which destination data center, and to which specific physical machine—into a single 1D flattened index representation, drastically reducing action space dimensionality and accelerating DRL training convergence.
- **Multi-Objective Deep Q-Network (DQN) Scheduling:** Utilizes a DQN agent with experience replay and target networks to learn an optimal policy balancing brown energy costs, carbon emissions, SLA violation penalties, and VM migration overheads.  [Source: Sec. I, pp. 96–97; Sec. III & IV, pp. 97–102]

## 3. Methodology
- **System role:** Global and local cloud resource manager coordinating virtual machine placement, host overload detection, and inter-datacenter VM migration across geo-distributed cloud facilities.
- **Scheduling decision:** Multi-dimensional spatio-temporal placement and migration:
  1. *VM Selection:* Identifying which virtual machines should be migrated away from overloaded or underutilized physical machines.
  2. *Target Host & Data Center Placement:* Mapping selected VMs to optimal destination physical machines across local or remote data centers based on renewable wind energy availability and electricity pricing.
- **Workload type:** Heterogeneous cloud computing workloads drawn from the real-world **Google Cluster Dataset** (an empirical workload trace from an infrastructure of approximately **12,500 machines**), exhibiting stochastic task arrival patterns and dynamic CPU/memory resource utilization.
- **Dynamic or online?** Yes; fully online dynamic scheduling where decisions are made sequentially in real time without future knowledge of workload bursts or weather patterns.
- **For RL papers:**
  - **Algorithm:** Deep Q-Network (DQN) with experience replay memory and target network updates, integrated with the TCN-MAD predictive overload detection module.
  - **State ($S_t$):** Captures multi-datacenter operational and environmental telemetry:
    - Current CPU and memory utilization levels across physical machines (PMs).
    - Overload probability indicators output by the TCN-MAD module for each PM.
    - Available on-site renewable wind energy generation (converted from empirical wind speed traces via a simulated wind-turbine model) at each data center site.
    - Real-time regional grid electricity prices.
    - Resource demand profiles of active virtual machines.  [Source: Sec. III & IV, pp. 97–101]
  - **Action ($A_t$):** Flattened index action representation:
    - Instead of mapping decisions across a Cartesian product of $(\text{VM}_i \times \text{PM}_{\text{source}} \times \text{DC}_{\text{target}} \times \text{PM}_{\text{target}})$, CFWS maps allowable migration pairs into a single 1D flattened index. This avoids action space explosion and reduces the computational complexity of the action selection step.  [Source: Sec. IV, pp. 100–102]
  - **Reward ($R_t$):** Multi-objective negative cost formulation balancing economic expenditure, carbon emissions, SLA violations, and migration overheads:
    $$R_t = - \left( \alpha \cdot \text{Cost}_{\text{brown}}(t) + \beta \cdot \text{Emission}_{\text{carbon}}(t) + \eta \cdot \text{SLAV}(t) + \lambda \cdot \text{Mig}_{\text{overhead}}(t) \right)$$
    where:
    - $\text{Cost}_{\text{brown}}(t)$ represents the financial expenditure of consuming grid brown electricity when server power demands exceed on-site green energy generation.
    - $\text{Emission}_{\text{carbon}}(t)$ represents the carbon footprint computed by applying regional U.S. Department of Energy (DOE) Electricity Emission Factors / regional Carbon Footprint Rate (CFR) to brown energy consumption.
    - $\text{SLAV}(t)$ denotes the Service Level Agreement Violation penalty, combining SLA violation time per active host (SLATAH) and performance degradation due to migration (PDM).
    - $\text{Mig}_{\text{overhead}}(t)$ penalizes the number of VM migrations to suppress thrashing and avoid excessive inter-DC network traffic.
    - $\alpha, \beta, \eta, \lambda$ are weighting hyperparameters balancing economic, environmental, QoS, and operational stability objectives.  [Source: Sec. III & IV, pp. 98–101]
  - **TCN-MAD Architecture:**
    - The Temporal Convolutional Network (TCN) extracts temporal correlations from historical CPU utilization sequences using dilated causal convolutions.
    - TCN predicts future PM utilization and computes the probability of host overload.
    - Median Absolute Deviation (MAD) dynamically calculates upper utilization thresholds from predicted patterns, adapting thresholds dynamically to avoid premature or delayed migrations.  [Source: Sec. IV, pp. 99–101]
  - **Training Setup & Hyperparameters:**
    - Deep Q-Network trained with fully connected hidden layers, experience replay buffer, and periodic target network synchronization.
    - Exploration handled via an $\epsilon$-greedy policy decaying over training episodes.
    - Evaluated over multi-step simulation episodes under dynamic workload traces.  [Source: Sec. IV & V, pp. 101–103]
- **Carbon / energy data source and region:**
  - *Data Center Locations:* 4 geo-distributed cloud data centers located in distinct U.S. climatic and grid regions: **Arizona, California, Oregon, and Louisiana**.
  - *Renewable Wind Energy Input:* Empirical wind speed traces obtained from the **National Renewable Energy Laboratory (NREL)** Western and Eastern datasets (the study focuses specifically on wind energy; no solar traces or photovoltaic panels are modeled).
  - *Wind-Turbine Power Output Model:* Physical wind-turbine generation model converting empirical NREL wind speeds into electrical power output based on turbine power curve parameters (cut-in speed, rated wind speed, cut-out speed, and rated turbine power), clearly distinguishing actual trace inputs (NREL empirical wind speed traces) from the simulated power conversion model (turbines converting wind speed to electrical power).
  - *Electricity Pricing:* Real-world regional wholesale electricity prices from local power markets.
  - *Carbon Emission Factors:* Regional grid carbon emission factors based on the **U.S. Department of Energy (DOE) Electricity Emission Factors** and regional **Carbon Footprint Rate (CFR)** applied to brown energy consumption across the four data center regions.
  - *(Note on public carbon API traceability: The case study integrates empirical NREL wind speed traces and U.S. DOE regional emission factors [CFR], but does not query an external dynamic carbon intensity API [such as Electricity Maps or WattTime] or provide dynamic marginal carbon-intensity time series; regional CFR values are regional/static factors, maintaining the strict Q3 score of 0.5).*  [Source: Sec. V, pp. 102–104]
- **Workload trace / dataset:** Real-world **Google Cluster Dataset**, an empirical workload trace from an infrastructure of **12,500 machines**, from which heterogeneous job resource requests and dynamic CPU/memory utilization profiles are drawn.  [Source: Sec. V, pp. 102–104]
- **Simulator or real system:** Simulation testbed developed on an extended **CloudSim** framework, modeling geo-distributed data centers, heterogeneous physical servers, dynamic wind turbine power generation, and VM migration overheads. It is evaluated in simulation and is **not** deployed on bare-metal hardware.  [Source: Sec. V, pp. 102–104]
- **Hardware & Physical Machine Profile:**
  - 4 simulated geo-distributed data centers with **varying numbers of physical machines (PMs)** across the four regions (Arizona, California, Oregon, Louisiana)—rather than a flat 100 PMs each or 400 total PMs—while the driving Google Cluster trace contains 12,500 machines.
  - Server hardware modeled on **HP ProLiant ML110 G4** and **HP ProLiant ML110 G5** servers.
  - Power profiles calibrated using the **SPECpower_ssj2008** benchmark across CPU utilization levels from 0% to 100%.  [Source: Sec. V, pp. 102–104]
- **Baselines compared:**
  - **Main Workload-Shifting Baselines:**
    1. *Greenpacker:* Renewable- and fragmentation-aware VM placement heuristic designed to maximize green energy consumption and minimize resource fragmentation.
    2. *LECC (Location, Energy, Carbon, and Cost-aware VM placement):* Multi-objective heuristic placement baseline designed for geo-distributed clouds balancing carbon, electricity price, and renewable availability.
    3. *ADVMC (Adaptive DRL-based VM Consolidation):* Adaptive reinforcement learning baseline optimizing VM consolidation based on cost and load metrics.
    4. *ADVMC-RES:* Extension of the ADVMC baseline incorporating multiple Renewable Energy Sources (RES) across distributed facilities.
  - **Host Overload-Detection Comparisons (evaluated specifically for host overload prediction within/against TCN-MAD, not as main workload-shifting baselines):**
    - *LSTM-MAD:* Overload prediction model combining Long Short-Term Memory networks with Median Absolute Deviation, evaluated strictly as an overload-detection model comparison against TCN-MAD (not a main workload-shifting baseline).
    - *MAD (Median Absolute Deviation):* Standard statistical dispersion heuristic for adaptive host overload detection.
    - *IQR (Interquartile Range):* Statistical interquartile dispersion heuristic based on CPU utilization interquartile range.
    - *LR (Local Regression):* Regression-based adaptive CPU threshold heuristic.
    - *THR (Static Threshold):* Fixed static CPU utilization threshold baseline (e.g., 80% threshold).  [Source: Sec. V, pp. 102–105]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Brown energy consumption reduction | **5.67% to 13.22%** reduction in brown energy consumption | Main workload-shifting baselines (Greenpacker, LECC, ADVMC, ADVMC-RES) | Sec. V, pp. 103–105; Fig. 4 / Table II |
| Virtual machine (VM) migration reduction | **Up to 86.53%** reduction in VM migrations | Main workload-shifting baselines (Greenpacker, LECC, ADVMC, ADVMC-RES) | Sec. V, pp. 104–105; Fig. 5 / Table III |
| Service Level Agreement Violations (SLAV) | Substantially lower SLAV rates across varying workload intensities | Main workload-shifting baselines (Greenpacker, LECC, ADVMC, ADVMC-RES); in host overload detection, TCN-MAD significantly outperforms overload-detection baselines (LSTM-MAD, THR, MAD, IQR, LR) | Sec. V, pp. 104–106; Fig. 6 |
| Renewable wind energy utilization | Maximizes on-site wind power utilization across Arizona, California, Oregon, and Louisiana facilities | Main workload-shifting baselines lacking joint spatio-temporal renewable/carbon-aware migration | Sec. V, pp. 103–105; Fig. 4 |
| Computational execution runtime | Accelerates decision speed and reduces computational overhead due to 1D flattened-index action space | Unflattened combinatorial DRL action spaces | Sec. IV & V, pp. 101–105 |

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  1. *Migration Overhead vs. Energy/Carbon Optimization Trade-Off (Sec. V, pp. 103–105):* Aggressive consolidation maximizes brown energy savings and renewable energy utilization but triggers frequent VM migrations, which incur network bandwidth overhead and risk SLA violations; conservative migration policies reduce network traffic but result in higher brown energy consumption.
  2. *Threshold Sensitivity in TCN-MAD (Sec. V, pp. 103–105):* The performance of adaptive overload detection depends closely on threshold sensitivity and prediction accuracy; mispredictions can lead either to delayed migrations causing transient host overloads or premature migrations that incur unnecessary migration costs.
  3. *Author-Stated Future Research Directions (Sec. VI, pp. 106–107):* In Section VI, the authors explicitly identify three concrete future research directions: (i) incorporating renewable energy generation forecasting models into the scheduling decision loop, (ii) integrating dynamic electricity pricing forecasting, and (iii) extending the framework to multi-cloud and edge computing continuum environments.
- **Gap we observe:**
  1. *Absence of Dedicated Limitations Section:* While the authors discuss operational trade-offs in Section V and outline future research directions in Section VI, the paper lacks a dedicated, self-critical limitations section analyzing the method's own structural assumptions or failure modes (e.g., reliance on static regional emission factors rather than live carbon signals, or single-agent DRL scalability boundaries).
  2. *Regional Static Emission Factors vs. Dynamic Carbon API:* While the case study incorporates dynamic empirical wind speed traces from NREL alongside regional wholesale electricity prices, carbon emissions are calculated using regional U.S. Department of Energy (DOE) Electricity Emission Factors / regional Carbon Footprint Rates (CFR) applied to brown energy rather than real-time dynamic grid carbon intensity time series ($g\text{CO}_2/\text{kWh}$ from APIs such as Electricity Maps or WattTime). These static regional factors strictly warrant maintaining the Q3 score of 0.5.
  3. *Closed-Source Implementation:* The neural network source code, TCN-MAD implementation, and simulation configuration scripts are not publicly hosted on an open repository (GitHub/Zenodo), hindering direct independent experimental reproduction.
  4. *Simulation-Centric Evaluation on Legacy Server Profiles:* Validation is conducted entirely within an extended CloudSim simulator with varying PM counts across 4 data centers using legacy server profiles (HP ProLiant ML110 G4 and G5 from SPECpower_ssj2008) driven by the 12,500-machine Google Cluster trace, leaving performance unverified on modern multi-core, heterogeneous GPU/accelerator cloud nodes or bare-metal production clusters.
  5. *Separation of Workload-Shifting vs. Overload-Detection Benchmarks:* The evaluation tests macro workload-shifting against heuristics and DRL baselines (Greenpacker, LECC, ADVMC, ADVMC-RES) while evaluating host overload detection separately (TCN-MAD vs. LSTM-MAD, MAD, IQR, LR, THR), leaving combined end-to-end interactions with modern dynamic grid orchestration tools unexamined.
  6. *Absence of On-Site Battery Energy Storage (BESS):* The framework relies strictly on spatial-temporal workload shifting and does not integrate on-site Battery Energy Storage Systems (BESS) to buffer surplus wind generation for calm periods or peak grid hours.

## 6. Relevance to our project
P19 provides critical architectural insights for Group G3 (RL / DRL for carbon-aware cloud workload scheduling) that directly inform our college project:
1. **Flattened Action Space Design:** P19's method of flattening multi-dimensional placement and migration decisions into 1D discrete indices provides an effective design pattern to solve the action space explosion problem in multi-host/multi-DC RL schedulers.
2. **Predictive Overload Mitigation (TCN-MAD):** Demonstrates that pairing deep temporal feature extraction (TCN) with statistical thresholding (MAD) proactively mitigates server overloads (demonstrated to outperform host overload-detection baselines such as LSTM-MAD, MAD, IQR, LR, and THR), preventing thrashing and keeping SLA violations low during carbon-driven consolidation.
3. **Demand-Side RES Integration & Workload-Shifting Benchmarks:** Confirms that aligning computing workload execution with local wind power availability across geographically distributed data centers yields tangible brown energy and carbon reductions (up to 13.22% over workload-shifting baselines Greenpacker, LECC, ADVMC, and ADVMC-RES).
4. **Targeting the Open-Source Gap:** Because P19 remains closed-source and tested only in simulation, our project directly fills an important gap by delivering an open-source, fully reproducible carbon-aware scheduler with real-time carbon API integration.
