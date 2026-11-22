# P15 — Sustainable AIGC Scheduling via Multi-Agent Soft Actor-Critic (MASAC)

**Full citation:** Siyue Zhang, Minrui Xu, Wei Yang Bryan Lim, and Dusit Niyato, "Sustainable AIGC Workload Scheduling of Geo-Distributed Data Centers: A Multi-Agent Reinforcement Learning Approach", in *Proceedings of the 2023 IEEE Global Communications Conference (GLOBECOM '23)*, Kuala Lumpur, Malaysia, December 4–8, 2023, pp. 3500–3505.  
**DOI / link:** [https://doi.org/10.1109/GLOBECOM54140.2023.10437617](https://doi.org/10.1109/GLOBECOM54140.2023.10437617) (also [arXiv:2304.07948](https://arxiv.org/abs/2304.07948))  
**Type:** Conference     **Group:** G3 (RL / DRL for carbon-aware cloud workload scheduling)  
**Quality score:** 8.0 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*  

---

## 1. Problem addressed
Recent breakthroughs in Generative AI / AI-Generated Content (AIGC)—such as ChatGPT and Diffusion Models—have unleashed an unprecedented surge in computational demand for machine learning (ML) training and downstream task fine-tuning. Training large models incurs staggering carbon footprints and electricity expenditures; for example, training GPT-3 consumed 1,287 MWh of electricity and emitted 552 tonnes $\text{CO}_2\text{eq}$, while Diffusion Models require hundreds of GPU days (150–1,000 V100 days). Crucially, grid carbon intensities and electricity prices fluctuate dramatically across global geographic regions (e.g., Singapore at $483\text{ gCO}_2\text{eq}/\text{kWh}$ and 301 USD/MWh from natural gas versus Ontario, Canada at $67\text{ gCO}_2\text{eq}/\text{kWh}$ and 22 USD/MWh from baseload hydropower). However, scheduling ML workloads across geo-distributed data centers is an NP-hard multi-objective problem challenged by gang-scheduling constraints, exclusive GPU memory allocations, wide-area network (WAN) data migration latencies, and user delay tolerances.  [Source: Sec. I, pp. 3500–3501 / pp. 1–2]

## 2. Approach (the core idea)
The authors propose **MASAC** (Multi-Agent Soft Actor-Critic), a decentralized carbon- and cost-aware scheduling framework that coordinates job placement across geo-distributed cloud data centers. To circumvent bandwidth bottlenecks and raw data privacy concerns, the framework adopts a Model-as-a-Service (MaaS) architecture where foundation models are pre-cached across data centers; local user data is preprocessed once using input layers, and only intermediate feature activations and fine-tuning weight updates are migrated across WAN links. The dispatching problem is formulated as a Multi-Agent Markov Decision Process (MAMDP) where each data center operates an autonomous Soft Actor-Critic (SAC) agent that learns to execute locally, postpone, or migrate AIGC jobs to maximize global system utility—balancing GPU execution revenues against electricity bills, idle power waste, carbon taxation, and migration overheads.  [Source: Sec. I & III, pp. 3501–3503 / pp. 2–4]

## 3. Methodology
- **System role:** Decentralized multi-datacenter spatial and temporal workload dispatcher for GPU clusters.
- **Scheduling decision:** Discrete decision per queuing job: execute locally ($A_n^k = n$), postpone by one time slot ($A_n^k = 0$), or migrate to a remote data center ($A_n^k = d, d \notin \{0, n\}$).
- **Workload type:** AI-Generated Content (AIGC) fine-tuning workloads spanning three categories: image generation (GANs/Diffusion), text generation (Masked LMs/Transformers), and text-to-image generation (Stable Diffusion).
- **Dynamic or online?** Yes; online time-slotted dispatching with dynamic job arrivals, real-time electricity prices, and time-varying grid carbon signals.
- **For RL papers:**
  - **Algorithm:** Multi-Agent Soft Actor-Critic (MASAC) with maximum entropy regularization and double critic networks ($Q_{\phi_n}, Q_{\phi'_n}$).
  - **State ($S^k$):** Global system state observed by agents:
    $$S^k = \{ \langle J_n^k, R_n^k, Q_n^k, V_n^k \rangle \mid \forall n \in [1, N] \} \quad \text{[Sec. III, p. 3502 / p. 3]}$$
    where $J_n^k = \langle r_{j_n^k}, d_{j_n^k}, d'_{j_n^k} \rangle$ represents the current job's demanded GPUs, execution duration, and allowable delay slack; $R_n^k$ is available idle GPUs; $Q_n^k$ is total GPU demand of waiting jobs in queue $Q_n$; and $V_n^k = \langle P_n(t), I_n(t) \rangle$ is local electricity price and carbon intensity.
  - **Action ($A_n^k$):** Discrete action $A_n^k \in \{0, 1, \dots, N\}$ for agent $n$ selecting postpone ($0$), local execution ($n$), or migration destination ($d$).  [Source: Sec. III, p. 3502 / p. 3]
  - **Reward ($R_n^k$):** Cooperative incremental system utility:
    $$R_n^k = \Delta U^k = U^{k+1} - U^k, \quad \forall n \in [1, N] \quad \text{[Sec. III, p. 3502 / p. 3]}$$
    where overall system utility is defined as:
    $$U = U_1 - U_2 - U_3 - U_4 - U_5 \quad \text{[Sec. II, Eq. 7a, p. 3502 / p. 3]}$$
    - $U_1$ (GPU Profit): $\sum_{t=1}^T \sum_{n=1}^N (\alpha - \eta_n \rho P_n(t)) \sum_{j_m \in \Theta_n} R_{j_m}(t)$ [Eq. 2]
    - $U_2$ (Idle GPU Power Cost): $\sum_{t=1}^T \sum_{n=1}^N \eta_n \beta \rho (R_n^{\max} - \sum_{j_m \in \Theta_n} R_{j_m}(t)) P_n(t)$ [Eq. 3]
    - $U_3$ (Carbon Emission Cost): $\sum_{t=1}^T \sum_{n=1}^N \mu \eta_n \rho ((1 - \beta) \sum_{j_m \in \Theta_n} R_{j_m}(t) + \beta R_n^{\max}) I_n(t)$ [Eq. 4]
    - $U_4$ (Job Migration Overhead & Carbon): $\sum_{k=1}^K \sum_{n=1}^N [c_{e_l}(s_{j_n^k} + s'_{j_n^k}) + \mu o_{e_l}(s_{j_n^k} + s'_{j_n^k})]$ [Eq. 5]
    - $U_5$ (Result Retrieval Overhead & Carbon): $\sum_{j_m \in J'^+} [c_{e_l}(s'_{j_m}) + \mu o_{e_l}(s'_{j_m})]$ [Eq. 6]
    *(Parameters: GPU revenue $\alpha = \$0.05/\text{GPU-hr}$; carbon tax $\mu = \$100/\text{ton CO}_2$; idle ratio $\beta = 10\%$; PUE $\eta_n$; GPU power $\rho$: Not stated in paper).*
  - **Training setup:** 10 parallel environments, 100 epochs, batch size 256, discount factor $\gamma = 0.99$, max episode steps $K_{\max} = 12,000$. Actor learning rate $1 \times 10^{-5}$, critic learning rate $5 \times 10^{-4}$, target network update cadence $G = 1,000$ steps, hidden layers `[256, 256]`. Replay buffer capacity: Not stated in paper.  [Source: Sec. IV-A, Table I, p. 3504 / p. 5]
- **Carbon / energy data source and region:** Real-world hourly electricity prices ($P_n(t)$) and carbon intensities ($I_n(t)$) sourced from Electricity Maps across 5 global regions: South Australia (AUS-SA), West Australia (AUS-WA), Ontario Canada (CA-ON), Poland (PL), and Singapore (SG).  [Source: Sec. IV-A, p. 3503 / p. 4]
- **Workload trace / dataset:** Job arrival patterns from the **Alibaba GPU Cluster Trace 2020** combined with task profiles for image, text, and text-to-image AIGC models; arrival rate scaled by regional demand coefficients $\delta_n = [0.01, 0.02, 0.01, 0.025, 0.03]$, deliberately loading Singapore and Poland beyond local capacity.  [Source: Sec. IV-A, Table I, p. 3504 / p. 5]
- **Simulator or real system:** **Trace-driven discrete-event simulation testbed** implemented in Python operating at 1-minute time steps. It is **not** a physical bare-metal cluster deployment.  [Source: Sec. IV-A, p. 3503 / p. 4]
- **Baselines compared:**
  - *S0: Local Computing (FCFS):* Non-migratory baseline processing jobs locally First-Come-First-Served.
  - *S1: Price Greedy:* Local execution first; migrates to lowest-price data center if local GPUs are exhausted.
  - *S2: Carbon Greedy:* Local execution first; migrates to lowest-carbon data center if local GPUs are exhausted.
  - *S3: MADQN:* Multi-Agent Deep Q-Network baseline under identical MAMDP formulation.  [Source: Sec. IV-A, p. 3504 / p. 5]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Overall system utility improvement | Up to 28.6% relative improvement in cumulative system utility | S0 (Local Computing baseline) | Abstract; Sec. IV-B, Fig. 4b, p. 3504 / p. 5 |
| GPU compute throughput (testing) | Up to 15.6% higher GPU time revenue ($\sim 2.07 \times 10^4$ GPU hours) | Other baseline algorithms (S0: $\sim 1.78 \times 10^4$; S1/S2: $\sim 1.95 \times 10^4$) | Sec. IV-B, Fig. 6b, p. 3505 / p. 6 |
| Training convergence speed | Stabilizes within ~10 epochs | S3 (MADQN, which requires ~40 epochs and oscillates) | Sec. IV-B, Fig. 4a, p. 3504 / p. 5 |
| Step reward magnitude | Average step reward $\sim 0.22$ ($2\times$ higher) | S3 (MADQN step reward $\sim 0.11$) | Sec. IV-B, Fig. 4a, p. 3504 / p. 5 |
| Testing cumulative reward | $\sim 5.35 \times 10^2$ USD | S0: $\sim 3.95 \times 10^2$; S1: $\sim 4.65 \times 10^2$; S2: $\sim 4.60 \times 10^2$; S3: $\sim 4.85 \times 10^2$ USD | Sec. IV-B, Fig. 6a, p. 3505 / p. 6 |
| Cost efficiency | $\sim 1.13 \times 10^{-2}$ USD per GPU hour | S0 baseline ($\sim 1.30 \times 10^{-2}$ USD per GPU hour) | Sec. IV-B, Fig. 6c, p. 3505 / p. 6 |
| Carbon efficiency | $\sim 1.32 \times 10^2\text{ gCO}_2$ per GPU hour | S0 baseline ($\sim 1.44 \times 10^2\text{ gCO}_2$ per GPU hour) | Sec. IV-B, Fig. 6d, p. 3505 / p. 6 |
| Datacenter load balancing | Balanced utilization maintained between ~65% and 75% across all 5 DCs | S0 (SG/PL overloaded at 80%–85%, CA-ON underutilized at 15%–20%) | Sec. IV-B, Fig. 5, p. 3505 / p. 6 |
| Transmission overhead trajectory | Monotonically decreasing WAN transmission cost over training epochs | S3 (MADQN, exhibiting erratic high-volume migrations) | Sec. IV-B, p. 3505 / p. 6 |

## 5. Gap
- **Gap stated by the authors:**
  "As the job details such as training data and model sizes are not available in the trace, we generate job characteristics based on three types of AIGC fine-tuning tasks... A homogeneous GPU architecture is considered as cloud providers typically purchase GPUs in bulk."  [Source: Sec. II & IV-A, pp. 3501–3503 / pp. 2–4]
  *(Note: The conclusion in Sec. V does not provide a formal limitations discussion).*
- **Gap we observe:**
  1. *Simulation Only:* The framework is validated purely within a discrete-event Python simulator (1-minute resolution) and is not tested on live Kubernetes, Slurm, or multi-region cloud testbeds.
  2. *Simplified Network Model:* WAN transfer delay is modeled as a linear function ($\tau = s / \xi_{i,j}$) without dynamic packet drop, congestion, or inter-datacenter bandwidth contention.
  3. *Instantaneous Carbon Telemetry:* The state vector captures only instantaneous carbon intensity ($I_n(t)$) without leveraging predictive multi-day forecasts (e.g., CarbonCast) to anticipate future green windows.
  4. *Hardware Homogeneity:* Modern cloud AI clusters feature heterogeneous accelerators (V100, A100, H100) with non-linear power-to-throughput scaling, which is omitted here.
  5. *Combinatorial Scalability:* The discrete action space $(N+1)^N$ may face scaling limits beyond the evaluated 5-datacenter topology.

## 6. Relevance to our project
P15 is the premier core anchor paper for Group G3. It provides an explicit mathematical blueprint for multi-objective carbon-aware scheduling that directly balances compute revenue, idle power waste, carbon emissions, and data migration penalties. Methodologically, it demonstrates that Soft Actor-Critic (SAC) substantially outperforms DQN in multi-datacenter environments because its entropy regularization prevents action hesitation and queue collapse. This multi-objective utility formulation serves as a primary foundation for designing the reward structure of our carbon-aware RL scheduler.
