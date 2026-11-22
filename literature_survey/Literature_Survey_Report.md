# Systematic Literature Survey: Carbon-Aware Reinforcement Learning Scheduler for Dynamic Cloud Workloads

**Course Project:** Carbon-Aware Reinforcement Learning (RL) Scheduler for Cloud Workloads (Dynamic)  
**Survey Period:** 2021 – 2026 (plus foundational and survey literature)  
**Methodology Standard:** Kitchenham & Charters (2007) / PRISMA 2020 / Wohlin (2014) Snowballing  

---

## Executive Summary
*(To be populated after detailed extraction of selected core papers)*

---

## 1. Introduction
- Motivation: Environmental footprint of hyperscale cloud datacenters
- Grid carbon intensity variations ($gCO_2/kWh$) across temporal and geographic dimensions
- Limitations of traditional carbon-agnostic and static scheduling heuristics
- Problem Formulation: Dynamic online scheduling using Reinforcement Learning under SLA constraints

## 2. Background and Key Concepts
- **Grid Carbon Intensity:** Marginal vs. average emissions, renewable intermittency
- **Workload Shifting Paradigms:** Temporal postponement vs. spatial multi-region migration
- **Reinforcement Learning Foundations in Cloud Resource Management:** Markov Decision Processes (MDPs), state spaces, action spaces, reward shaping for multi-objective optimization (carbon vs. SLA/performance)

## 3. Systematic Survey Methodology
- Research questions (RQs)
- Search strategy: Databases, exact search strings (S1–S5), date ranges
- Inclusion and exclusion criteria (Stage 1 & Stage 2)
- PRISMA 2020 flow diagram and selection statistics
- Quality assessment framework (8-point QA scoring)

## 4. Research Taxonomy
- Categorization across Groups G1 to G5:
  - **G1:** Carbon-Aware Scheduling Without RL (Optimization, Heuristics)
  - **G2:** RL / DRL for Cloud Resource Management (Energy, Cost, Performance)
  - **G3:** RL / DRL for Carbon-Aware Workload Scheduling (Core Focus)
  - **G4:** Carbon-Intensity Data and Forecasting
  - **G5:** Simulators, Datasets, and Workload Traces
- Sub-label classifications (DQN, PPO, Actor-Critic, MARL, Single vs Multi-Objective, Temporal vs Spatial)

## 5. Group Analysis and Literature Synthesis
### 5.1 Group G1: Carbon-Aware Scheduling Without RL
### 5.2 Group G2: RL for Cloud Energy, Cost, and Performance
### 5.3 Group G3: RL for Carbon-Aware Cloud Scheduling
### 5.4 Group G4: Carbon-Intensity Data and Forecasting
### 5.5 Group G5: Simulators, Datasets, and Workload Traces
### 5.6 Foundational Literature and Comprehensive Surveys

## 6. Comprehensive Comparison Tables
*(Comparison tables for G1, G2, G3, G4, and G5)*

## 7. Research Trends and Evolution (2021–2026)
- Evolution from static heuristics to deep reinforcement learning
- Transition from energy-only objectives to real-time grid carbon signals
- Emerging trends in multi-agent coordination and forecast-informed RL

## 8. Critical Analysis of Common Limitations
- Handling of dynamic stochastic job arrivals
- Rigorous SLA/deadline constraint handling vs. carbon trade-offs
- Real-world carbon signal volatility vs. forecast uncertainty
- Ecological cost of RL training vs. operational emissions savings
- Transferability and policy generalization across heterogeneous regional grids

## 9. Candidate Research Gaps for Course Project
- Detailed justification of 2–3 selected feasible research gaps
- Mapping to specific surveyed papers and experimental validation strategies

## 10. Threats to Validity
- Internal, external, construct, and conclusion validity considerations

## 11. References
*(Linked to references.bib)*
