# P27 — Uncertainty-Aware Decarbonization for Datacenters

**Full citation:** Amy Li, Sihang Liu, and Yi Ding, "Uncertainty-Aware Decarbonization for Datacenters", in *Proceedings of the 3rd Workshop on Sustainable Computer Systems (HotCarbon '24)*, July 9, 2024, Santa Cruz, CA, USA, Article No. 13, pp. 1–7.
**DOI / link:** [https://doi.org/10.48550/arXiv.2407.02390](https://doi.org/10.48550/arXiv.2407.02390) (Workshop link: `https://hotcarbon.org/2024/`)
**Type:** Workshop (HotCarbon '24)     **Group:** G4 (Carbon intensity forecasting & grid data)
**Quality score:** 7.5 / 8
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 0.5, Q8: 1.0)*
*(Note on score and primary source audit: Full 7-page workshop paper downloaded and audited directly from arXiv (`arXiv:2407.02390`); converted to structured Markdown at `literature_survey/markdown_papers/P27.md`.
- **Q1 (1.0):** Formulates the formal mathematical problem of predictive uncertainty in carbon-aware load shifting, establishing coverage probability guarantees $P(y_t \in \hat{C}_{t-1}(x_t)) \ge 1 - \alpha$ and defining temporal and spatial predictive uncertainty.
- **Q2 (1.0):** Comprehensive description of the sequentially predictive conformal inference (SPCI) framework: nonconformity scoring via prediction residuals, rolling residual sets, quantile random forest residual estimation, and dynamic confidence interval updates.
- **Q3 (1.0):** Evaluated against empirical grid carbon intensity data from three major US balancing authorities: CAISO (CISO), ERCOT (ERCO), and ISO New England (ISNE).
- **Q4 (1.0):** Evaluated using real production cluster power traces from Google data centers (20 MW peak power facility).
- **Q5 (1.0):** Benchmarks the conformal uncertainty-aware policy against conventional deterministic point-prediction baselines (CarbonCast point estimates) across temporal and spatial load shifting scenarios.
- **Q6 (1.0):** Exhaustive numerical reporting: empirical coverage percentages across three significance levels ($\alpha=0.10, 0.05, 0.01$), proportions of misleading predictions (10.6%–16.8% temporal, 2.2%–7.8% spatial), emission increases from naive scheduling (4.3%–6.6% temporal, 2.7%–7.3% [up to 14%] spatial), and absolute tonnage savings (2.1 to 10.4 tons $\text{CO}_2\text{e}$ in a 20 MW cluster).
- **Q7 (0.5):** Scored 0.5 because although the mathematical formulation, SPCI algorithm (Algorithm 1), and evaluation parameters are fully documented in the open-access publication, the authors' specific evaluation scripts are not packaged into an independent open repository.
- **Q8 (1.0):** Dedicated analysis of system constraints, clarifying that case studies evaluate suspend-and-resume heuristic abstractions and discussing the trade-offs of conservative scheduling thresholds and confidence interval widths).*

---

## 1. Problem addressed
Carbon-aware cloud schedulers rely on forecasted grid carbon intensity to shift computational workloads across time (temporal deferral) and space (geographic migration). However, all prior carbon schedulers implicitly assume that carbon intensity forecasts are perfectly accurate:
1. **Pervasive Predictive Uncertainty:** Carbon intensity forecasts exhibit significant error and high predictive variance. Temporal uncertainty causes prediction errors to escalate over time (73–96h forecasts exhibit 1.2× to 1.8× higher MAPEs than 1–24h forecasts; seasonal forecast variance shifts by 2.1×). Spatial uncertainty creates heterogeneous prediction accuracies across different geographical balancing authorities (e.g., solar-heavy CAISO has much higher variance than baseload grids).
2. **Misleading Point Predictions:** Schedulers using point forecasts are frequently misled by forecast inversion:
   - *Temporal Misleading Rate:* In 10.6%–16.8% of cases, point forecasts predict that tomorrow will be cleaner than today, whereas in reality tomorrow is more carbon-intensive.
   - *Spatial Misleading Rate:* In 2.2%–7.8% of cases, point forecasts predict that Region B is cleaner than Region A, whereas true emissions are higher in Region B.
3. **Severe Carbon Penalty of Naive Decisions:** Making scheduling decisions based solely on point predictions often backfires:
   - Naive temporal shifting causes a **4.3%–6.6% increase** in carbon emissions.
   - Naive spatial migration causes a **2.7%–7.3% (and up to 14%) increase** in carbon emissions.
   - For a standard 20 MW data center cluster, naive shifting inadvertently emits **2.1 to 10.4 extra tons of $\text{CO}_2\text{e}$** per scheduling decision!

---

## 2. Approach (the core idea)
The authors introduce the first **Uncertainty-Aware Decarbonization Framework** for data centers based on **Conformal Prediction**:
- **Distribution-Free Uncertainty Quantification:** Rather than trusting point estimates $\hat{y}_t = \hat{f}(x_t)$ (e.g., from CarbonCast), the framework constructs confidence intervals $\hat{C}_{t-1}(x_t)$ that are theoretically guaranteed to contain the true carbon intensity with a user-specified probability $1 - \alpha$:
  $$P(y_t \in \hat{C}_{t-1}(x_t)) \ge 1 - \alpha$$
- **Sequentially Predictive Conformal Inference (SPCI):** Standard conformal prediction assumes exchangeable data, which fails in non-stationary time-series. The authors adapt SPCI, which maintains a sliding window of prediction residuals and trains quantile random forests autoregressively to predict future residual quantiles, encoding temporal dependencies directly into interval bounds.
- **Adaptive Confidence-Gated Scheduling:** Workloads are shifted temporally or migrated spatially **only when confidence intervals do not overlap** (i.e., when the upper bound of the target period/region is strictly lower than the lower bound of the source period/region). If intervals overlap (indicating low confidence), the scheduler conservatively remains in place, avoiding erroneous migrations.

---

## 3. Methodology
- **System role:** Predictive uncertainty quantification layer placed between grid carbon forecasters (e.g., CarbonCast) and cloud workload schedulers.
- **Scheduling decision:** Uncertainty-gated suspend-and-resume (WaitAWhile) scheduling across time and space.
- **Workload type:** Batch computing workloads executing on a hyperscale cluster with a peak power of 20 MW.
- **Dynamic or online?** Yes; online sequential updating of conformal residual sets and interval calibration at each discrete dispatch step.
- **Model Architecture (SPCI Framework):**
  - Point forecaster: Pre-trained CarbonCast multi-day model.
  - Residual calibration: Nonconformity score defined as $\hat{\epsilon}_t = y_t - \hat{y}_t$.
  - Quantile Random Forest: Predicts conditional quantiles $q_{\alpha/2}$ and $q_{1-\alpha/2}$ of unobserved residuals based on recent temporal error patterns.
  - Dynamic Confidence Interval:
    $$\hat{C}_{t-1}(x_t) = [\hat{y}_t + \hat{q}_{\alpha/2}, \hat{y}_t + \hat{q}_{1-\alpha/2}]$$
- **Carbon / energy data source and region:**
  - Hourly empirical grid carbon intensity data from three major US balancing authorities:
    1. **CAISO (CISO):** California ISO (solar-heavy, high diurnal variance).
    2. **ERCOT (ERCO):** Electric Reliability Council of Texas (high wind penetration).
    3. **ISO-NE (ISNE):** ISO New England (gas/nuclear mix).
  - Evaluated across six months of continuous operations (July to December 2022) covering summer, fall, and winter seasonal conditions.
- **Workload trace / dataset:**
  - Real normalized production cluster power traces from Google data centers scaled to a 20 MW peak power facility.
- **Simulator or real testbed:** Trace-driven discrete-event simulation comparing point-prediction scheduling with uncertainty-aware conformal interval scheduling.
- **Baselines compared:**
  1. *Groundtruth Optimal Oracle:* Perfect future carbon knowledge.
  2. *Deterministic Point Forecast (CarbonCast):* Scheduling based solely on predicted point carbon intensity values.
  3. *SPCI Conformal Scheduling (Proposed):* Uncertainty-aware scheduling across significance levels $\alpha \in \{0.10, 0.05, 0.01\}$.

---

## 4. Results (numbers only, copied exactly)

### Conformal Prediction Coverage Across Regions (Table 1, p. 4):
| Region | Target: 90% ($\alpha=0.10$) | Target: 95% ($\alpha=0.05$) | Target: 99% ($\alpha=0.01$) | Empirical Assessment |
|:---|:---:|:---:|:---:|:---|
| **CAISO (CISO)** | **92.41%** | **96.34%** | **99.28%** | Strictly meets and exceeds coverage bounds |
| **ERCOT (ERCO)** | **92.02%** | **96.02%** | **99.09%** | Strictly meets and exceeds coverage bounds |
| **ISO-NE (ISNE)** | **90.92%** | **95.74%** | **98.93%** | Strictly meets and exceeds coverage bounds |

### Temporal Load Shifting Case Study (Table 2 & Table 3, p. 5):
| Metric | CAISO (CISO) | ERCOT (ERCO) | ISO-NE (ISNE) | Source |
|:---|:---:|:---:|:---:|:---|
| **Proportion of Misleading Predictions** | **16.8%** of days | **10.6%** of days | **13.4%** of days | Table 2, p. 5 |
| **Emissions Increase from Naive Shifting** | **4.3%** increase | **6.6%** increase | **4.6%** increase | Table 2, p. 5 |
| **Specific Case (July 9–10, 2022, CISO)** | Day 1: True = 1.00, Pred = 1.13 | Day 2: True = 1.05, Pred = 0.96 | Point shift causes **+5% carbon** | Table 3, p. 5 |
| **Absolute Carbon Waste (20 MW Cluster)** | — | — | **2.1 tons $\text{CO}_2\text{e}$ wasted** | Sec. 4.2, p. 5 |
| **SPCI Uncertainty Outcome** | Day 1 CI: [0.83, 1.21] | Day 2 CI: [0.84, 1.20] | CIs overlap $\rightarrow$ **Shift avoided!** | Sec. 4.2, p. 5 |

### Spatial Load Shifting Case Study (Table 4 & Table 5, p. 6):
| Migration Path | Misleading Prediction Rate | Increased Emissions from Naive Shifting |
|:---|:---:|:---:|
| **CAISO $\to$ ERCOT** | 5.0% of days | +3.1% emissions |
| **CAISO $\to$ ISO-NE** | 7.8% of days | +5.8% emissions |
| **ERCOT $\to$ CAISO** | 2.2% of days | +2.7% emissions |
| **ERCOT $\to$ ISO-NE** | 5.0% of days | +3.5% emissions |
| **ISO-NE $\to$ CAISO** | 4.5% of days | +4.3% emissions |
| **ISO-NE $\to$ ERCOT** | 2.8% of days | **+7.3% emissions** |
| **Specific Case (July 4, 2022, ERCOT vs. ISNE)** | ERCOT: True = 1.00, Pred = 0.86; ISNE: True = 0.87, Pred = 0.90 | Point shift causes **+14% carbon** |
| **Absolute Carbon Waste (20 MW Cluster)** | Naive migration to ERCOT causes **10.4 tons $\text{CO}_2\text{e}$ extra emissions** | Table 5 & Sec. 4.2, p. 6 |
| **SPCI Uncertainty Outcome** | ERCOT CI: [0.86, 1.11]; ISNE CI: [0.83, 0.93] | ERCOT lower bound does not beat ISNE $\rightarrow$ **Migration aborted!** |

---

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Proof-of-Concept Load Shifting:* Evaluated using simulated suspend-and-resume heuristics; physical deployment on live Kubernetes or Slurm clusters requires accounting for network migration bandwidth, checkpointing overheads, and straggler tasks.
  - *Conservative Decision Bias:* Wide confidence intervals during volatile grid periods cause the scheduler to reject potentially beneficial load shifts, trading off aggressive carbon savings for risk avoidance.
  - *Significance Level Tuning:* The parameter $\alpha$ dictates interval width; selecting an optimal $\alpha$ involves an operational trade-off between coverage guarantees and interval sharpness.
- **Gap we observe:**
  - *No Direct Integration with DRL:* Conformal intervals are evaluated with rule-based suspend-and-resume thresholds rather than feeding uncertainty intervals directly into a Deep Reinforcement Learning state vector or reward formulation.
  - *Scope 2 Average Emissions Focus:* Evaluates average grid carbon intensity; extending conformal inference to real-time marginal operating emissions rates (MOER) with high-frequency 5-minute volatility is needed.

---

## 6. Relevance to our project
P27 is the critical link between carbon forecasting (G4) and carbon-aware RL scheduling (G3):
1. **Dispels the "Perfect Forecast" Illusion:** Mathematically and empirically proves that trusting point carbon forecasts leads to inverted scheduling decisions that worsen emissions by 5% to 14% (up to 10.4 tons $\text{CO}_2\text{e}$ per event).
2. **Conformal State Features for RL:** Proves that an RL state space should not just ingest predicted carbon intensity $\hat{y}_t$; it must also ingest prediction interval bounds $[q_{\text{low}}, q_{\text{high}}]$ to enable risk-sensitive reinforcement learning.
3. **Guardrails for Migration:** Provides a principled mathematical criterion for spatial migration: only migrate when the target region's upper carbon bound is strictly lower than the local lower bound.
