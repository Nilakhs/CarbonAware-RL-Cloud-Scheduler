# P09 — GNN-PPO (Edge-Cloud Workflow Scheduling)

**Full citation:** Kaige Zhu, Zhenjiang Zhang, Sherali Zeadally, and Feng Sun, "Learning to Optimize Workflow Scheduling for an Edge–Cloud Computing Environment", in *IEEE Transactions on Cloud Computing*, Vol. 12, No. 3, pp. 897–912, July–September 2024.  
**DOI / link:** [https://doi.org/10.1109/TCC.2024.3408006](https://doi.org/10.1109/TCC.2024.3408006)  
**Type:** Journal     **Group:** G2 (RL scheduling for cloud workloads with energy, cost, or performance objectives)  
**Quality score:** 7.5 / 8  
*(Q1: 1.0, Q2: 1.0, Q3: 0.5, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*  

---

## 1. Problem addressed
Modern IoT and smart city applications increasingly submit complex computational workflows with interdependent tasks modeled as Directed Acyclic Graphs (DAGs) to hybrid edge-cloud systems. Scheduling these workflows requires balancing the low-latency but resource-constrained edge servers with high-capacity but communication-delayed remote cloud data centers. Traditional heuristics (such as HEFT) make static, pre-runtime decisions that degrade under dynamic continuous workflow arrivals, while conventional Reinforcement Learning methods struggle with the combinatorial action space and sparse, delayed feedback of multi-stage DAGs.  [Source: Sec. 1, pp. 897–899]

## 2. Approach (the core idea)
The authors develop an online learning-based workflow scheduler combining Graph Neural Networks (GNN) and Proximal Policy Optimization (PPO). The GNN automatically embeds topological dependencies and latent structural information from workflow DAGs into low-dimensional feature vectors. A PPO actor-critic network then maps these embeddings and edge-cloud system states to node placement decisions. To tackle sparse delayed rewards, the framework incorporates an intrinsic reward mechanism that provides immediate step-level feedback to steer policy learning toward makespan and energy minimization.  [Source: Sec. 3 & 4, pp. 900–906]

## 3. Methodology
- **System role:** Online DRL workflow scheduler and graph representation learner.
- **Scheduling decision:** Where (spatial task placement across heterogeneous edge nodes and central cloud data centers; sequential task dispatching according to DAG topological order).
- **Workload type:** Complex scientific and enterprise workflows represented as Directed Acyclic Graphs (DAGs) with precedence constraints and heterogeneous task data dependencies.
- **Dynamic or online?** Yes; online scheduling under continuous, steady workflow arrivals and fluctuating edge network conditions.
- **For RL papers:**
  - **Algorithm:** Proximal Policy Optimization (PPO) with GNN (Graph Neural Network) task embedding and an intrinsic reward generation module.
  - **State:** Composite state vector comprising: (1) GNN node embedding of ready tasks (instruction count, input/output data sizes, depth, child degree); (2) resource availability of edge nodes (CPU, memory, power draw); (3) cloud server queue length; and (4) network link bandwidth and transmission latencies.
  - **Action:** Discrete action selecting a target computing node (edge node $i \in \{1, \dots, M\}$ or central cloud) for the currently prioritized ready task.
  - **Reward:** Augmented multi-objective reward combining extrinsic and intrinsic signals:
    $$R_t = R_{\text{ext}}(t) + \beta \cdot R_{\text{int}}(t)$$
    where $R_{\text{ext}}(t) = - \left( \alpha \cdot \text{Makespan}_{\text{step}} + (1 - \alpha) \cdot \text{Energy}_{\text{step}} \right)$, and $R_{\text{int}}(t)$ evaluates instantaneous policy improvement to counter delayed terminal feedback.
  - **Training setup:** PPO with clipped surrogate objective ($\epsilon = 0.2$), generalized advantage estimation (GAE), actor-critic networks trained over 1,500 workflow batches with learning rate $3 \times 10^{-4}$.
- **Carbon / energy data source and region:** Power and energy consumption modeled across physical server specifications (CPU active/idle power coefficients); grid carbon intensity is not explicitly modeled.
- **Workload trace / dataset:** Standard Pegasus scientific workflow benchmark traces (Montage, CyberShake, LIGO, Epigenomics) with varying task counts (from 20 to 100 tasks per DAG).
- **Simulator or real system:** Custom distributed edge-cloud discrete-event simulation testbed written in Python.
- **Baselines compared:** 
  - **HEFT (Heterogeneous Earliest Finish Time):** Classical static heuristic for DAG scheduling.
  - **PSO (Particle Swarm Optimization):** Metaheuristic optimization algorithm.
  - **GA (Genetic Algorithm):** Evolutionary search baseline.
  - **Standard DQN:** Deep Q-Network without graph embeddings.
  - **Vanilla PPO:** PPO without GNN structural embeddings or intrinsic reward feedback.  
[Source: Sec. 4 & 5, pp. 904–909]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Makespan reduction vs. HEFT | 14.8% to 22.3% relative reduction in overall workflow completion time | HEFT heuristic baseline | Sec. 5.3, Fig. 6 & 7, p. 908 |
| Makespan reduction vs. PSO / GA | 18.5% to 26.1% relative reduction in workflow makespan | Metaheuristic baselines (PSO and GA) | Sec. 5.3, Fig. 6, p. 908 |
| Energy consumption reduction vs. HEFT | 12.1% to 19.4% relative reduction in total computing and network energy | HEFT heuristic baseline | Sec. 5.4, Fig. 8, p. 909 |
| Energy consumption reduction vs. DQN | 15.6% relative reduction in energy consumption | Standard DQN baseline | Sec. 5.4, Fig. 8, p. 909 |
| Scheduling decision time | $< 12\text{ ms}$ per task dispatch decision | PSO/GA metaheuristics ($> 450\text{ ms}$) | Sec. 5.5, Table 4, p. 910 |
| Training convergence speed | Reached optimal reward convergence in 450 episodes | Vanilla PPO baseline without intrinsic reward ($> 1,100$ episodes) | Sec. 5.2, Fig. 5, p. 907 |
| SLA / deadline violation rate | Not stated in paper (evaluated as continuous makespan minimization rather than strict deadline drop) | Soft deadline target | Sec. 5.3, pp. 907–908 |

## 5. Gap
- **Gap stated by the authors:**
  "Our current model does not consider the temporal variability of electricity prices or renewable energy supply across distributed computing sites... In addition, for extremely large workflows ($> 500$ tasks), the GNN message-passing mechanism incurs noticeable graph embedding latency that must be optimized."  [Source: Sec. 6, p. 911]
- **Gap we observe:**
  The framework optimizes solely for latency (makespan) and physical hardware energy consumption, lacking any awareness of operational carbon emissions, marginal emissions rates (MOER), or grid carbon intensity forecasting. It also does not evaluate temporal deferral of delay-tolerant workflow tasks.

## 6. Relevance to our project
Presents an advanced, robust DRL methodology (GNN task embedding combined with PPO and intrinsic rewards) that solves the delayed-feedback problem for complex interdependent cloud tasks. This GNN+PPO architecture can be directly adopted and extended in our project by replacing or augmenting the reward function with real-time carbon intensity signals.