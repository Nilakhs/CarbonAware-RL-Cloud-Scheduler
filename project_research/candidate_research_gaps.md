# Candidate Research Gaps

*Note: Initial candidate research gaps identified during preliminary scoping and candidate paper discovery. These will be substantiated and refined following full paper extraction and verification.*

## Gap 1: Robust RL Scheduling Under Non-Stationary Carbon Intensity and Forecast Uncertainty
- **Observation:** Most current carbon-aware schedulers assume deterministic or perfect future carbon intensity forecasts. In operational grids, forecast errors (especially around renewable ramps) can exceed 20–30%. When carbon forecasts are erroneous, greedy or brittle heuristic schedulers either miss clean generation periods or cause severe SLA violations.
- **Research Opportunity:** Developing an RL scheduler (e.g., using robust RL, distributional RL, or reward shaping that penalizes forecast divergence) that explicitly treats future carbon signals as uncertain stochastic variables while maintaining strict deadline guarantees.

## Gap 2: Joint Temporal and Spatial Dynamic Scheduling for Multi-Tenant Cloud Environments
- **Observation:** Existing G1/G3 works frequently evaluate temporal shifting in isolation (delaying batch tasks within one datacenter) or spatial shifting in isolation (migrating tasks between regions at static intervals). Few RL formulations jointly optimize real-time temporal buffering with geographic dispatching under dynamic queue arrivals and network egress/latency constraints.
- **Research Opportunity:** A multi-action or hierarchical RL framework capable of deciding simultaneously *whether to defer* (temporal) and *where to dispatch* (spatial) under heterogeneous carbon grids and variable network migration costs.

## Gap 3: Generalization Across Heterogeneous Regional Grids Without Full Retraining
- **Observation:** RL schedulers trained on one specific regional grid profile (e.g., CAISO with strong midday solar peaks) often fail or experience severe policy collapse when deployed on grids with completely different dynamics (e.g., ERCOT with wind-dominant nighttime peaks, or UK National Grid).
- **Research Opportunity:** Investigating transfer learning, domain randomization, or meta-reinforcement learning approaches that allow a carbon-aware scheduler to adapt rapidly to distinct grid carbon profiles with minimal fine-tuning.
