# P26 — DACF: Day-Ahead Carbon Intensity Forecasting of Power Grids Using Machine Learning

**Full citation:** Diptyaroop Maji, Ramesh K. Sitaraman, and Prashant Shenoy, "DACF: Day-Ahead Carbon Intensity Forecasting of Power Grids Using Machine Learning", in *Proceedings of the 13th ACM International Conference on Future Energy Systems (e-Energy '22)*, June 28–July 1, 2022, pp. 406–413.
**DOI / link:** [https://doi.org/10.1145/3538637.3538849](https://doi.org/10.1145/3538637.3538849) (Direct PDF: `https://raw.githubusercontent.com/carbonfirst/DACF/main/DACF.pdf`)
**Open-source repository:** [https://github.com/carbonfirst/DACF](https://github.com/carbonfirst/DACF) (also `https://github.com/UMass-LIDS/DACF`)
**Type:** Conference (ACM e-Energy '22)     **Group:** G4 (Carbon intensity forecasting & grid data)
**Quality score:** 7.5 / 8
*(Q1: 1.0, Q2: 1.0, Q3: 1.0, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 0.5)*
*(Note on score and primary source audit: Full 8-page conference PDF audited from the authors' repository at `literature_survey/papers/P26_Maji_DACF.pdf`; converted to structured Markdown at `literature_survey/markdown_papers/P26.md`; complete Python/TensorFlow code and datasets audited at `github.com/carbonfirst/DACF`.
- **Q1 (1.0):** Formulates the day-ahead hourly average grid carbon intensity forecasting problem, defining mathematical generation source mixes and emission factor weighted aggregations.
- **Q2 (1.0):** Comprehensive description of the per-source Artificial Neural Network (ANN) architecture, feature vectors (historical generation, temporal calendar encodings, day-ahead numerical weather variables), training with RMSE loss, early stopping, and periodic 6-month re-training.
- **Q3 (1.0):** Uses official real-world grid generation source data from the US Energy Information Administration (EIA-930), CAISO OASIS, and ENTSO-E across six balancing authority regions in the US and Europe.
- **Q4 (1.0):** Evaluated over a 3-year continuous historical period (2019 to 2021) combining hourly generation records with NOAA NCEP Global Forecast System (GFS ds084.1) weather forecasts.
- **Q5 (1.0):** Benchmarked against the state-of-the-art non-proprietary model by Leerbeck et al. (combining linear regression, splines, and ARIMA).
- **Q6 (1.0):** Exhaustive numerical results reported across all 6 regions in Tables 4 and 5: mean, median, 90th, and 95th percentile MAPE, plus head-to-head comparisons against SOTA.
- **Q7 (1.0):** Open science: full source code, datasets, and instructions publicly hosted on GitHub (`github.com/carbonfirst/DACF`).
- **Q8 (0.5):** Scored 0.5 because the paper briefly discusses operational constraints (limited to 24-hour horizon, dependency on individual generation telemetry, omission of transmission losses), but lacks an in-depth standalone threats-to-validity section [extended later in CarbonCast]).*

---

## 1. Problem addressed
Carbon-aware workload schedulers and smart energy systems rely on lookahead signals to shift computing and heating demand to periods of low carbon intensity. However, day-ahead carbon forecasting faces key hurdles:
1. **Uncertainty of Intermittent Renewables:** Increasing grid penetration of solar and wind energy causes rapid, non-linear swings in the grid's carbon intensity over the course of a day.
2. **Limitations of Univariate Forecasting:** Prior approaches treat carbon intensity as an isolated univariate time series (using statistical methods like ARIMA or simple regression), failing to model the underlying physical fuel generation mix (coal, gas, nuclear, hydro, wind, solar) that directly causes carbon emissions.
3. **Proprietary Commercial Tools:** Services like Tomorrow / Electricity Maps maintain proprietary forecasting models behind paid commercial APIs without open reproducibility.

---

## 2. Approach (the core idea)
The authors propose **DACF (Day-Ahead Carbon Intensity Forecasting)**, an open-source machine learning framework that forecasts regional grid carbon intensity 24 hours in advance by modeling electricity generation sources individually:
- **Per-Source Generation Modeling:** Decomposes grid generation into individual fuel sources (coal, natural gas, oil, nuclear, solar, wind, hydro, geothermal, biomass). A separate Artificial Neural Network (ANN) forecaster is trained for each active fuel source in the region.
- **Incorporating Future Knowledge (Weather Forecasts):** Unlike pure historical time-series predictors, DACF feeds day-ahead numerical weather predictions (wind speed, solar irradiance/DSWRF, temperature, precipitation) from NOAA into the renewable generation forecasters.
- **Analytical Carbon Synthesis:** Computes hourly average grid carbon intensity ($g\text{CO}_2/\text{kWh}$) by combining individual predicted source outputs ($\hat{P}_s(t)$) with their direct carbon emission factors ($\text{CEF}_s$):
  $$\text{CI}(t) = \frac{\sum_{s} \hat{P}_s(t) \cdot \text{CEF}_s}{\sum_{s} \hat{P}_s(t)}$$
- **Modular Plug-and-Play Design:** New sources, improved forecasters, or public ISO renewable forecasts (e.g., CAISO OASIS day-ahead wind/solar) can be plugged in without changing model hyperparameters across regions.

---

## 3. Methodology
- **System role:** Machine learning forecasting service providing 24-hour day-ahead hourly average grid carbon intensity signals.
- **Scheduling decision / Forecast horizon:** Day-ahead (24-hour) hourly forecasts updated once daily (at 00:00 hours) or rolling hourly.
- **Target metric:** Hourly average carbon intensity of grid electricity ($g\text{CO}_2/\text{kWh}$).
- **Model Architecture:**
  - Independent 3-layer feed-forward Artificial Neural Network (ANN) per generation source.
  - Layer 1: Dense (50 hidden units, ReLU).
  - Layer 2: Dense (34 hidden units, ReLU).
  - Output Layer: Dense (24 units outputting the 24-hour generation vector).
- **Input Features:**
  1. *Historical Generation:* Hourly electricity produced by that specific source over the preceding 24 hours.
  2. *Calendar/Temporal Context:* Hour-of-day, hour-of-year, and binary weekday/weekend indicator.
  3. *Day-Ahead Weather Forecasts:* For renewable sources (solar, wind, hydro): 10m wind speed ($m/s$), 2m temperature ($K$), 2m dewpoint ($K$), surface downward short-wave radiation flux ($W/m^2$), and total precipitation ($kg/m^2$).
- **Carbon / energy data source and region:**
  - Evaluated across six electrical grid regions:
    1. **California (CA / CAISO):** High solar penetration (duck curve).
    2. **PJM:** Fossil-dominated baseload (coal and natural gas).
    3. **Texas (TX / ERCOT):** High wind penetration.
    4. **New England (NE / ISO-NE):** Gas and nuclear mix.
    5. **Sweden (SE):** Hydro and nuclear dominant.
    6. **Germany (DE):** Mixed renewable and coal generation.
  - Historical generation: US EIA-930 Hourly Electric Grid Monitor and ENTSO-E Transparency Platform (2019–2021).
  - Weather forecasts: NOAA NCEP Global Forecast System (GFS ds084.1).
- **Training Setup:** Trained on 2019–2020 hourly data; tested on the last 6 months of 2021. Models are re-trained every six months to adapt to seasonal shifts. Loss function: RMSE with early stopping and model checkpointing; Evaluation metric: Mean Absolute Percentage Error (MAPE).
- **Baselines compared:**
  - *SOTA (Leerbeck et al. '20):* State-of-the-art non-proprietary model combining linear regression, splines, and ARIMA residual correction.

---

## 4. Results (numbers only, copied exactly)

### Day-Ahead Forecast Performance Across 6 Regions (Table 4, p. 4):
| Region | Mean MAPE | Median MAPE | 90th Percentile MAPE | 95th Percentile MAPE | Grid Context |
|:---|:---:|:---:|:---:|:---:|:---|
| **PJM (US)** | **3.30%** | 2.71% | 5.80% | 6.89% | Stable fossil baseload |
| **ISO-NE (NE, US)** | **4.44%** | 3.51% | 8.35% | 9.75% | Moderate volatility |
| **Sweden (SE)** | **6.47%** | 5.14% | 11.39% | 14.32% | Low carbon baseload |
| **California (CA)** | **7.41%** | 6.30% | 12.21% | 14.04% | Solar diurnal swing |
| **Texas (TX / ERCOT)** | **8.05%** | 6.40% | 14.55% | 20.76% | High wind volatility |
| **Germany (DE)** | **9.08%** | 6.44% | 19.84% | 24.86% | High renewable variability |
| **Corpus Average** | **6.46%** | — | — | — | **Across all 6 regions** |

### Head-to-Head Comparison Against SOTA (Table 5, p. 4):
| Region | SOTA (Leerbeck et al.) | **DACF (Proposed)** | MAPE Reduction |
|:---|:---:|:---:|:---:|
| **California (CA)** | 7.94% | **7.41%** | -0.53% |
| **PJM** | 3.59% | **3.30%** | -0.29% |
| **Texas (TX)** | 8.19% | **8.05%** | -0.14% |
| **New England (NE)** | 4.86% | **4.44%** | -0.42% |
| **Sweden (SE)** | 6.80% | **6.47%** | -0.33% |
| **Germany (DE)** | 9.91% | **9.08%** | -0.83% |
| **Average Improvement** | — | — | **6.4% average decrease (up to 8.6%)** |

---

## 5. Gap
- **Author-discussed constraints and trade-offs:**
  - *Short Forecast Horizon:* Limited strictly to 24-hour day-ahead predictions; cannot support multi-day workload planning (resolved later by CarbonCast in P25).
  - *Analytical Equation Sensitivity:* Directly applying Eq. 1 assumes complete and accurate generation telemetry for all fuel sources; if telemetry for a major source is missing or noisy, forecast accuracy degrades sharply.
  - *Lack of Inter-Grid Power Exchanges:* Treats each balancing authority as an island, ignoring cross-border transmission imports and exports.
- **Gap we observe:**
  - *Average vs. Marginal Carbon Intensity:* Forecasts **average carbon intensity** (useful for Scope 2 carbon accounting), rather than **marginal operating emissions rates (MOER)**, which dictate the true carbon impact of incremental cloud computing loads.
  - *No Uncertainty Quantification:* Outputs deterministic point forecasts without prediction intervals.

---

## 6. Relevance to our project
DACF is a foundational milestone in Group G4:
1. **Decomposed Source Modeling:** Pioneered the concept of predicting individual generation sources (coal, gas, wind, solar) before computing carbon intensity, establishing that future weather knowledge is essential for accurate grid forecasts.
2. **Direct Comparison with CarbonCast:** Serves as the day-ahead benchmark that CarbonCast (P25) builds upon and compares against.
3. **Open-Source Reproducibility:** The public `carbonfirst/DACF` repository provides clean historical EIA and ENTSO-E datasets that validate carbon signals used across our survey.
