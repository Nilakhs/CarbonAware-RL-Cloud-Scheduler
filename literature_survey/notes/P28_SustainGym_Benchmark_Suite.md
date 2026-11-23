# P28 — SustainGym: Reinforcement Learning Environments for Sustainable Energy Systems

**Full citation:** Christopher Yeh, Victor Li, Rajeev Datta, Julio Arroyo, Nicolas Christianson, Chi Zhang, Yize Chen, Mohammad Mehdi Hosseini, Azarang Golmohammadi, Yuanyuan Shi, Yisong Yue, and Adam Wierman, "SustainGym: Reinforcement Learning Environments for Sustainable Energy Systems", in *Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS 2023) Track on Datasets and Benchmarks*, New Orleans, LA, USA, December 2023.
**DOI / link:** [https://doi.org/10.48550/arXiv.2311.04481](https://doi.org/10.48550/arXiv.2311.04481) (NeurIPS entry: `https://proceedings.neurips.cc/paper_files/paper/2023/hash/ba74855789913e5ed36f87288af79e5b-Abstract-Datasets_and_Benchmarks.html`)
**Open-source repository:** [https://github.com/chrisyeh96/sustaingym](https://github.com/chrisyeh96/sustaingym) (Documentation: `https://chrisyeh96.github.io/sustaingym/`)
**Type:** Conference (NeurIPS '23 Datasets & Benchmarks)     **Group:** G5 (Simulators, testbeds, and cloud traces)
**Quality score:** 8.0 / 8
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*
*(Note on score and primary source audit: Full 18-page NeurIPS 2023 proceedings publication downloaded from the official conference portal at `literature_survey/papers/P28_Yeh_SustainGym.pdf`; converted to structured Markdown at `literature_survey/markdown_papers/P28.md`; Python package inspected via GitHub `chrisyeh96/sustaingym`.
- **Q1 (1.0):** Formulates standardized, reproducible RL environments for sustainability applications following the Gymnasium API (single-agent) and PettingZoo Parallel API (multi-agent), defining realistic physical constraints, reward structures, and explicit distribution shift evaluation protocols.
- **Q2 (1.0):** Comprehensive description of the five constituent environments—including detailed specification of the carbon-aware `DatacenterEnv` (27-dimensional observation space, continuous Virtual Capacity Curve action space, composite carbon-delay reward, and 24-hour MOER lookahead).
- **Q3 (1.0):** Uses empirical marginal operating emissions rate (MOER) time-series traces from WattTime across US grid regions (e.g., CAISO), capturing dynamic temporal carbon intensity variations.
- **Q4 (1.0):** `DatacenterEnv` replays authentic production workload traces from Google Borg clusters (May 2019 dataset).
- **Q5 (1.0):** Benchmarks multiple baseline classes: heuristic and random policies, classical control (Model Predictive Control, MPC), and modern deep RL algorithms (PPO, SAC, DDPG, Multi-Agent PPO, Multi-Agent SAC, with continuous and discretized action variants).
- **Q6 (1.0):** Full quantitative comparative performance reported across environments under both in-distribution training and out-of-distribution temporal distribution shifts (2019 vs. 2021 profiles).
- **Q7 (1.0):** Gold standard open science: open-source Python library published under CC BY 4.0, complete documentation website, and automated test suites on GitHub.
- **Q8 (1.0):** Dedicated limitations section critically discussing Scope 1/2 focus (omission of water and embodied carbon), binary distribution shift testing, simulation-to-hardware gaps, and single-datacenter limitations [leaving multi-datacenter spatial migration to future extensions]).*

---

## 1. Problem addressed
Reinforcement learning (RL) has achieved tremendous success in toy simulations and games (e.g., Atari, Go, MuJoCo), but applying RL to real-world infrastructure and sustainability systems encounters a severe **realism gap**:
1. **Lack of Standardized Benchmarks:** Unlike computer vision (ImageNet) or general robotics (OpenAI Gym), sustainable energy systems lack standardized, reproducible benchmarks. Researchers frequently develop ad-hoc, private simulators, preventing fair comparative evaluation.
2. **Neglect of Physical Constraints:** Standard RL benchmarks assume soft penalty environments where constraint breaches merely reduce reward. In real-world physical systems (power grids, EV charging networks, co-generation plants), violating physical constraints (transformer ratings, voltage bounds) can damage physical infrastructure.
3. **Temporal Distribution Shift:** Sustainability applications operate in non-stationary environments where weather patterns, renewable penetration, electricity prices, and grid carbon intensities shift drastically across seasons and years. Existing RL agents overfit to historical training windows and degrade when deployed under shifted conditions.
4. **Multi-Agent Coordination & Competition:** Realistic sustainability settings involve multiple interacting entities (e.g., competing battery storage systems in wholesale markets or cooperative EV chargers). Standard single-agent benchmarks fail to model these dynamics.

---

## 2. Approach (the core idea)
The authors present **SustainGym**, a standardized, open-source benchmark suite of realistic reinforcement learning environments for sustainable energy systems:
- **Comprehensive Environment Suite:** Covers five diverse sustainability domains:
  1. `EVChargingEnv`: Managing a network of electric vehicle charging stations under transformer capacity limits and dynamic electricity/carbon costs.
  2. `ElectricityMarketEnv`: Bidding a battery energy storage system into a wholesale day-ahead electricity market.
  3. `DatacenterEnv`: Carbon-aware workload scheduling in a cloud data center using virtual capacity throttling.
  4. `CogenEnv`: Managing a multi-train combined-cycle gas turbine cogeneration plant meeting steam and electricity demands.
  5. `BuildingEnv`: Controlling HVAC heating/cooling in commercial buildings to minimize energy and maintain thermal comfort.
- **Standardized API Integration:** Implements the modern Farama Foundation **Gymnasium API** for single-agent tasks and the **PettingZoo Parallel API** for multi-agent tasks, enabling seamless integration with Stable-Baselines3 and Ray RLlib.
- **Realistic Physical Modeling & Distribution Shift Protocol:** Each environment integrates empirical data traces (WattTime MOER, Google cluster traces, ACN EV data) and features a formal **distribution shift benchmark**, testing whether agents trained on historical conditions (e.g., 2019 data) remain robust when evaluated on shifted future data (e.g., 2021 data).

---

## 3. Focus on `DatacenterEnv` (Methodology Details)
- **System role:** Cloud batch job scheduler dynamically adjusting data center capacity to minimize carbon emissions while meeting workload deadlines.
- **Scheduling mechanism (VCC):** Modeled after Google's carbon-aware computing platform (Radovanovic et al. 2021 [P02]). Uses a **Virtual Capacity Curve (VCC)** to throttle total cluster compute capacity. When the VCC is set low, low-priority delay-tolerant batch jobs wait in a priority queue; when the VCC is raised during low-carbon grid hours, deferred jobs execute.
- **Decision epoch:** 1-hour timesteps; month-long episodes (720 hours).
- **Workload type:** Real low-priority, delay-tolerant batch jobs sampled from the **Google Cluster Trace (May 2019)**.
- **Observation Space ($s(t) \in \mathbb{R}^{27}$):**
  1. Active VCC from the previous time step: $a(t-1) \in [0, 1]$.
  2. Currently running compute load: $d_t$.
  3. Number of jobs waiting in the queue: $n$.
  4. Forecasted Marginal Operating Emissions Rate (MOER) for the next 24 hours: $\hat{m}_{t:t+23|t} \in \mathbb{R}^{24}$.
- **Action Space:** Continuous scalar $a(t) \in [0, 1]$, representing the fraction of the data center's maximum capacity ($C$) allowed to be allocated by the scheduler at the next time step.
- **Reward Function:**
  $$r(t) = - \left( d_t \cdot m_t + \mathbb{I}[t \% 24 = 0] \max\left(0, 0.97 w_t - C \sum_{h=0}^{23} a(t-h)\right) \right)$$
  - *Carbon Term ($d_t \cdot m_t$):* Penalizes emissions produced by running compute load $d_t$ under marginal carbon intensity $m_t$.
  - *SLA Delay Penalty:* Checked every 24 hours; penalizes the agent if the cumulative scheduled capacity fails to serve at least 97% of the total enqueued job-hours ($w_t$).
- **Carbon Data:** Hourly Marginal Operating Emissions Rate (MOER) from **WattTime** (US CAISO balancing authority).
- **Distribution Shift:** Tested by training agents on 2019 MOER traces and evaluating them on 2021 MOER traces.
- **Baselines compared:**
  - *Model Predictive Control (MPC):* Model-based controller with 24-hour lookahead.
  - *Model-Free RL Algorithms:* PPO (Proximal Policy Optimization), SAC (Soft Actor-Critic), DDPG (Deep Deterministic Policy Gradient), Random baseline, and action-discretized variants.

---

## 4. Key Experimental Findings (copied from Section 3 & 4)
- **High Variance Across RL Algorithms:** In `DatacenterEnv` (Figure 4c), Model Predictive Control (MPC) consistently outperforms off-the-shelf model-free RL algorithms (PPO, SAC, DDPG), demonstrating that classic control methods often handle lookahead horizons and constraints more reliably than unconstrained RL.
- **Performance Under Distribution Shift:**
  - In `DatacenterEnv`, the shift in MOER values between 2019 and 2021 had a relatively minor impact on agent performance compared to other environments, indicating that diurnal solar/wind cycles retain sufficient periodic structure across years.
  - However, in environments with complex thermodynamics (`CogenEnv`), agents trained on shifted data unexpectedly performed worse than agents trained on original data due to high environment variance.
- **Superiority of Multi-Agent PPO (MA-PPO):** In multi-agent environments (`EVChargingEnv` and `CogenEnv`), MA-PPO significantly outperformed single-agent policies and off-policy SAC, demonstrating that factorized action spaces and non-stationary training improve robustness.

---

## 5. Gap
- **Author-discussed constraints and limitations:**
  - *Single-Datacenter Scope:* `DatacenterEnv` currently models a single data center performing temporal load shifting via VCC throttling; multi-datacenter geographic spatial migration across diverse ISO grids is left for future extensions.
  - *Environmental Metric Scope:* Focuses exclusively on operational energy and carbon dioxide emissions ($\text{CO}_2$), omitting data center water consumption, embodied Scope 3 manufacturing emissions, and electronic waste.
  - *Binary Distribution Shift Protocol:* Currently tests binary pairs of original vs. shifted environments rather than continuous non-stationary drift.
- **Gap we observe:**
  - *Coarse Job Representation:* Workload is abstracted as aggregate job-hours ($w_t$) throttled by a scalar VCC fraction, rather than scheduling individual heterogeneous tasks, GPU containers, or directed acyclic graph (DAG) dependencies.
  - *No Cooling Power Modeling:* Total power is directly equated to compute load ($d_t$), omitting dynamic PUE, server inlet temperatures, and chiller dynamics (which are modeled in P24).

---

## 6. Relevance to our project
SustainGym is a benchmark cornerstone for Group G5:
1. **Gold-Standard RL Environment:** Establishes the modern Gymnasium standard for carbon-aware RL cloud computing, directly implementing Google's Virtual Capacity Curve (VCC) mechanism.
2. **Direct Benchmark Comparison:** Provides established baseline performance figures for MPC, PPO, SAC, and DDPG under real WattTime MOER traces and Google cluster logs.
3. **Formalizing Distribution Shift:** Demonstrates the necessity of testing carbon schedulers across multiple historical years (e.g., 2019 vs. 2021) to evaluate policy generalization under shifting grid conditions.
