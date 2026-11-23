# P25 — CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity

**Full citation:** Diptyaroop Maji, Ramesh K. Sitaraman, and Prashant Shenoy, "CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity", in *Proceedings of the 9th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys '22)*, November 9–10, 2022, Boston, MA, USA, pp. 198–207.
**DOI / link:** [https://doi.org/10.1145/3563357.3564079](https://doi.org/10.1145/3563357.3564079) (Direct PDF: `https://groups.cs.umass.edu/ramesh/wp-content/uploads/sites/3/2022/09/buildsys2022-final282.pdf`)
**Open-source repository:** [https://github.com/carbonfirst/CarbonCast](https://github.com/carbonfirst/CarbonCast) (also `https://github.com/UMassLIDS/CarbonCast`)
**Type:** Conference (ACM BuildSys '22)     **Group:** G4 (Carbon intensity forecasting & grid data)
**Quality score:** 8.0 / 8
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*
*(Note on score and primary source audit: Full 10-page conference publication downloaded and audited at `literature_survey/papers/P25_Maji_CarbonCast.pdf`; converted to structured Markdown at `literature_survey/markdown_papers/P25.md`; complete Python/TensorFlow code and datasets audited at `github.com/carbonfirst/CarbonCast`.
- **Q1 (1.0):** Rigorous mathematical formulation of regional electricity generation mix, direct vs. lifecycle carbon emission factors (CEF), hourly average carbon intensity, and multi-day lookahead forecasting objectives.
- **Q2 (1.0):** Comprehensive architectural design: modular two-tier hierarchy decoupling per-source generation models (Tier 1 ANNs) from aggregate carbon intensity prediction (Tier 2 hybrid 1D-CNN + LSTM), sliding-window rolling training, feature vectors, and hyperparameter tables.
- **Q3 (1.0):** Ingests official hourly electricity generation source data from the US Energy Information Administration (EIA-930), CAISO OASIS, and ENTSO-E across six diverse electrical grids in North America and Europe.
- **Q4 (1.0):** Evaluated over three continuous historical years (2019 to 2021) of empirical hourly generation records combined with NOAA National Centers for Environmental Prediction (NCEP) Global Forecast System (GFS ds084.1) 96-hour numerical weather predictions.
- **Q5 (1.0):** Compared against state-of-the-art baselines: SARIMA univariate time-series decomposition (SOTA 1), single-tier equation-based DACF (SOTA 2), and non-hierarchical ablations under missing data.
- **Q6 (1.0):** Exhaustive numerical results reported across all 6 regions in Tables 3, 4, 5, and 6: mean, median, 90th, and 95th percentile MAPE, day-by-day forecast horizons (Day 1 through Day 4), and inference runtimes.
- **Q7 (1.0):** Exemplary open science: full source code, pre-trained models, scraping scripts, and evaluation datasets publicly hosted and actively maintained on GitHub.
- **Q8 (1.0):** Dedicated discussion analyzing forecast degradation over multi-day horizons, error correlation with solar/wind penetration, sub-hourly extension trade-offs, and omitted inter-grid transmission exchanges).*

---

## 1. Problem addressed
Carbon-aware computing systems (e.g., cloud batch schedulers, demand-response workloads, electric vehicle charging) require accurate forecasts of grid carbon intensity to shift electricity demand to cleaner hours. However, existing carbon forecasting solutions face severe practical limitations:
1. **Short Forecast Horizon:** Prior academic and commercial solutions (such as DACF, Tomorrow/Electricity Maps, and National Grid ESO) focus almost exclusively on short-term day-ahead (0–24 hours) or 48-hour forecasts. Cloud computing tasks (such as distributed foundation model training, genomic pipelines, and scientific simulations) frequently run over multiple days and require 96-hour or longer forecast horizons.
2. **Proprietary & Region-Locked Tools:** Commercial carbon APIs (e.g., Tomorrow/Electricity Maps, WattTime) use closed-source proprietary models behind paid subscription paywalls. Open APIs (such as National Grid ESO) are locked to a single geographical jurisdiction (the United Kingdom).
3. **Fragility of Analytical Equation-Based Methods:** Prior systems like DACF predict individual generation sources (coal, gas, solar, wind) and then apply an analytical weighted-sum equation:
   $$\text{CI}(t) = \sum_{s} \frac{\text{Gen}_s(t)}{\sum \text{Gen}} \times \text{CEF}_s$$
   When source production telemetry is delayed, missing, or noisy—or as forecast errors compound over multiple days—analytical equations assign fixed weights to erroneous inputs, causing catastrophic error cascades.
4. **Intermittent Renewable Volatility:** Solar and wind generation fluctuate heavily with weather patterns and seasonal diurnal cycles, making multi-day grid carbon intensity non-linear and difficult to predict with univariate statistical models.

---

## 2. Approach (the core idea)
The authors present **CarbonCast**, the first open-source, multi-day (up to 96-hour) grid carbon intensity forecasting framework based on a **hierarchical two-tiered machine learning architecture**:
- **Tier 1 (Per-Source Generation Forecasting):** For each electricity-producing source in a region (solar, wind, natural gas, coal, hydro, nuclear, etc.), a dedicated Artificial Neural Network (ANN) predicts hourly electricity production for the next 96 hours using historical generation, calendar features (hour-of-day, hour-of-year, weekday/weekend), and 96-hour numerical weather forecasts.
- **Tier 2 (Hybrid CNN-LSTM Carbon Synthesis):** Rather than passing Tier 1 generation predictions into a rigid analytical formula, Tier 2 feeds the multi-source generation forecasts into a deep learning model combining **two 1D-CNN layers** (which extract short-term temporal features across fuel sources) with an **LSTM layer** (which captures long-term multi-day temporal dependencies). Tier 2 also ingests historical carbon intensity and NOAA weather variables.
- **Dynamic Re-weighting & Resiliency:** Because Tier 2 uses deep neural networks, it dynamically re-adjusts feature weights:
  - *Missing Data Resiliency:* If telemetry for a major fuel source (e.g., solar in California) drops out, Tier 2 automatically compensates using historical carbon intensity and solar irradiance forecasts.
  - *Noise Robustness:* As Tier 1 generation forecasts degrade over days 2, 3, and 4, Tier 2 dampens noisy inputs, outperforming analytical equation approaches.
- **Dual Emission Accounting:** Supports both **direct** (combustion-only, Scope 1/2) and **lifecycle** (upstream extraction, transport, manufacturing, Scope 3) carbon emission factors.

---

## 3. Methodology
- **System role:** Machine learning forecasting service providing multi-day (96-hour) hourly average grid carbon intensity forecasts ($g\text{CO}_2/\text{kWh}$) to carbon-aware schedulers and facility managers.
- **Scheduling decision / Forecast horizon:** Generates a continuous 96-hour rolling forecast updated every 24 hours (or dynamically on demand).
- **Target metric:** Hourly average grid carbon intensity ($g\text{CO}_2/\text{kWh}$), evaluated with both direct and lifecycle emission factors.
- **Model Architecture:**
  - **Tier 1 (Source Production Forecasters):** Independent 3-layer fully connected dense neural networks for each fuel source:
    - Layer 1: Dense (50 units, ReLU).
    - Layer 2: Dense (34 units, ReLU).
    - Layer 3: Dense (24 units outputting day-ahead hourly generation).
    - Rolled forward autoregressively 24 hours at a time to cover 96 hours.
  - **Tier 2 (Carbon Intensity Forecaster):** Hybrid 1D-CNN + LSTM:
    - 1D-CNN Layer 1: 4 filters of kernel size $4 \times 4$ with padding.
    - Max-Pooling Layer.
    - 1D-CNN Layer 2: 16 filters of kernel size $4 \times 4$.
    - LSTM Layer: 24 hidden units with dropout rate 0.1.
    - Output Dense Layer: 24 units predicting hourly carbon intensity, rolled forward across 96 hours.
- **Input Features:**
  - *Tier 1:* Past 24 hours historical generation from the target source, hour-of-day (sine/cosine), hour-of-year, weekday/weekend flag, and weather forecasts (for renewables).
  - *Tier 2:* 96-hour forecasted generation from all regional sources, past 24 hours historical carbon intensity, date-time features, and 96-hour NOAA weather forecasts.
- **Carbon / energy data source and region:**
  - Evaluated across six major balancing authorities in the United States and Europe:
    1. **CAISO (CISO):** California, USA (solar-heavy).
    2. **PJM:** Mid-Atlantic, USA (coal and natural gas baseload).
    3. **ERCOT (ERCO):** Texas, USA (high wind penetration).
    4. **ISO-NE (ISNE):** New England, USA (natural gas and nuclear).
    5. **Sweden (SE):** Europe (hydro, nuclear, wind).
    6. **Germany (DE):** Europe (wind, solar, coal mix).
  - Generation source data: US EIA Hourly Electric Grid Monitor and ENTSO-E Transparency Platform (2019–2021).
  - Weather forecasts: NOAA NCEP Global Forecast System (GFS ds084.1) 96-hour numerical forecasts (10m u/v wind speeds, 2m temperature, 2m dewpoint, surface downward short-wave radiation flux [DSWRF], total precipitation).
- **Training Setup:** Trained on 2019 data; evaluated on 2020–2021 data (50% train, 25% validation, 25% test) with periodic 6-month model re-training. Loss function: RMSE; Evaluation metric: Mean Absolute Percentage Error (MAPE).
- **Baselines compared:**
  1. *SOTA 1 (Bokde et al. / SARIMA):* Univariate time-series decomposition into trend, seasonality, and noise, extended to 96 hours.
  2. *SOTA 2 (DACF, Maji et al. '22):* Single-tier neural generation forecasting combined with the analytical CEF equation.
  3. *Non-Hierarchical Ablation:* Direct analytical equation under missing generation source data.

---

## 4. Results (numbers only, copied exactly)

### 96-Hour Forecast Performance Across Regions (Table 4 & Table 5, p. 8):
| Electrical Grid Region | Direct CEF Mean MAPE | Direct CEF Median MAPE | Lifecycle CEF Mean MAPE | Lifecycle CEF Median MAPE | Primary Grid Characteristics |
|:---|:---:|:---:|:---:|:---:|:---|
| **PJM (US)** | **4.80%** | 4.04% | **5.29%** | 4.51% | Fossil baseload (low volatility) |
| **ISO-NE (US)** | **6.46%** | 5.55% | **6.41%** | 5.50% | Gas / nuclear / hydro |
| **Sweden (SE)** | **10.07%** | 8.54% | **5.78%** | 5.12% | Hydro & wind dominant |
| **ERCOT (US)** | **11.13%** | 8.76% | **11.14%** | 8.40% | High wind volatility |
| **CAISO (US)** | **13.37%** | 11.96% | **11.45%** | 9.91% | High solar duck-curve |
| **Germany (DE)** | **13.93%** | 11.30% | **11.72%** | 9.16% | Complex multi-fuel mix |
| **Overall Average** | **9.96%** | — | **8.63%** | — | **Across all 6 regions** |

### Day-by-Day Forecast Comparison (Lifecycle CEF, MAPE) [Table 6, p. 9]:
| Region | Day 1 SOTA 1 (SARIMA) | Day 1 SOTA 2 (DACF) | **Day 1 CarbonCast** | Day 2 DACF | **Day 2 CarbonCast** | Day 3 DACF | **Day 3 CarbonCast** | Day 4 DACF | **Day 4 CarbonCast** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CAISO** | 10.71% | **6.45%** | 8.08% | 12.26% | **11.19%** | 16.02% | **12.93%** | 17.22% | **13.62%** |
| **PJM** | 4.27% | **3.08%** | 3.69% | 5.51% | **4.93%** | 7.06% | **5.87%** | 8.15% | **6.67%** |
| **ERCOT** | 14.09% | **7.87%** | 9.78% | 12.74% | **10.93%** | 14.94% | **11.61%** | 16.21% | **12.23%** |
| **ISO-NE** | 5.54% | **4.32%** | 5.10% | 9.23% | **6.33%** | 10.69% | **6.97%** | 11.57% | **7.25%** |
| **Sweden** | 5.10% | **3.28%** | 4.29% | 5.92% | **5.64%** | 6.79% | **6.43%** | 7.33% | **6.74%** |
| **Germany** | 15.54% | **7.21%** | 7.81% | 11.82% | **10.69%** | 13.95% | **12.80%** | 16.57% | **15.55%** |

### Resiliency Against Missing Data (California Missing Solar Experiment) [Table 3, p. 6]:
| Forecast Horizon | Hierarchical CarbonCast (All Sources) | **Hierarchical CarbonCast (No Solar Data)** | Non-Hierarchical Equation (All Sources) | Non-Hierarchical Equation (No Solar Data) | Degradation Impact |
|:---|:---:|:---:|:---:|:---:|:---|
| **Day 1** | 9.40% | **9.53%** (+0.13%) | 7.51% | 33.54% (+26.03%) | Equation degrades **4.5×**; CarbonCast unaffected |
| **Day 2** | 13.23% | **12.24%** (-0.99%) | 14.15% | 34.05% (+19.90%) | Equation degrades **2.4×**; CarbonCast unaffected |
| **Day 3** | 15.09% | **13.99%** (-1.10%) | 18.34% | 36.31% (+17.97%) | Equation degrades **2.0×**; CarbonCast unaffected |
| **Day 4** | 15.75% | **14.98%** (-0.77%) | 19.76% | 37.27% (+17.51%) | Equation degrades **1.9×**; CarbonCast unaffected |

### Overall SOTA Improvement & Computational Overhead:
- **Error Reduction:** Achieves an average 96-hour MAPE reduction of **14.38%** (direct CEF) and **11.91%** (lifecycle CEF) compared to SOTA.
- **Runtime:** Tier 1 training takes $\le 4$ minutes (parallelizable across sources); Tier 2 training takes $\le 15$ minutes (total training $\sim 20$ minutes).
- **Inference Speed:** Generating a full 96-hour hourly forecast takes only **0.5 seconds**.

---

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Renewable Penetration Error Correlation:* Forecasting error correlates positively with the fraction of intermittent solar and wind on the grid; fossil-dominated grids (PJM) achieve $\sim 4.8\%$ MAPE, whereas renewable-heavy grids (CAISO, Germany) experience $11\%–14\%$ MAPE.
  - *Inter-Grid Power Exchanges:* CarbonCast treats each regional balancing authority as an isolated system, omitting physical cross-border electricity imports and exports.
  - *Hourly Time Granularity:* Forecasts are produced at 1-hour resolution; sub-hourly 5-minute or 15-minute dispatch markets are not supported in the initial release.
- **Gap we observe:**
  - *Average vs. Marginal Carbon Intensity:* CarbonCast predicts **average carbon intensity** (Scope 2 carbon accounting), whereas real-time workload scheduling decisions require **marginal operating emissions rates (MOER)** to identify the specific generator displaced by incremental cloud compute demand.
  - *Point Forecasts without Uncertainty Bounds:* The core 2022 BuildSys paper outputs deterministic point forecasts without formal prediction intervals or conformal quantile bounds (addressed later by Li et al. in P27).

---

## 6. Relevance to our project
CarbonCast is a cornerstone paper in Group G4 with immense direct utility:
1. **Multi-Day Lookahead for Batch Schedulers:** Enables carbon-aware RL schedulers to defer long-running training jobs (e.g., 24–72 hours) with high predictive confidence across the entire execution window.
2. **Two-Tier Neural Robustness:** Demonstrates why learning-based synthesis (1D-CNN + LSTM) is fundamentally superior to analytical weighted-sum equations when dealing with missing telemetry or compounding multi-day forecast noise.
3. **Open-Source Artifacts for Simulation:** The public `carbonfirst/CarbonCast` repository provides pre-processed EIA/ENTSO-E datasets and trained neural checkpoints that directly provide empirical carbon forecast signals for our scheduler testbed.
