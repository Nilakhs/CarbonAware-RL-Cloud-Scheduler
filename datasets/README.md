# Datasets and Trace Documentation

> [!NOTE]
> **Status: Scoping & Trace Documentation (Pre-Implementation)**  
> This directory catalogs the empirical workload traces, simulator inputs, and grid carbon intensity datasets identified during Group G4 and G5 of our Systematic Literature Review. No proprietary or multi-gigabyte trace files are stored directly in this repository.

---

## 1. Planned Workload Traces (Group G5)

1. **Google Borg Cluster Traces (2019 / 2020):**
   - *Source:* Muhammad Tirmazi et al., *"Borg: the Next Generation"*, ACM EuroSys '20 (`F03`).
   - *Description:* Detailed production cluster traces from Google data centers capturing dynamic job arrivals, task resource demands (CPU, memory), and execution durations across multi-machine cells.
   - *Public Repository:* [https://github.com/google/cluster-data](https://github.com/google/cluster-data)

2. **Alibaba Cluster Trace (2021):**
   - *Source:* Shutian Luo et al., *"Characterizing Microservice Dependency and Performance: Alibaba Trace Analysis"*, ACM SoCC '21 (`P30`).
   - *Description:* Large-scale trace capturing microservice dependency graphs, container allocations, and invocation patterns across thousands of nodes.
   - *Public Repository:* [https://github.com/alibaba/clusterdata](https://github.com/alibaba/clusterdata)

3. **FunctionBench Serverless Traces:**
   - *Source:* Used in *GreenCourier* (Chadha et al., WoSC '23, `P06`).
   - *Description:* Standard benchmark workloads (image processing, video rendering, compression, ML inference) for Function-as-a-Service (FaaS) scheduling.

---

## 2. Regional Grid Carbon Intensity Data (Group G4)

1. **California ISO (CAISO):**
   - *Source:* CAISO OASIS API / Electricity Maps.
   - *Profile:* High daytime solar generation creating a prominent "duck curve" with midday carbon valleys ($< 150\text{ }g\text{CO}_2/\text{kWh}$) and nocturnal carbon peaks.

2. **ENTSO-E Transparency Platform (Europe):**
   - *Source:* European Network of Transmission System Operators for Electricity.
   - *Profiles:*
     - Germany (DE): Highly volatile wind/solar generation mix.
     - France (FR): Nuclear baseline with steady, low carbon intensity ($< 60\text{ }g\text{CO}_2/\text{kWh}$).

3. **National Grid ESO (United Kingdom):**
   - *Source:* UK National Grid ESO Carbon Intensity API.
   - *Profile:* Offshore wind surges providing periodic deep decarbonization intervals.

4. **CarbonCast Forecast Dataset:**
   - *Source:* Diptyaroop Maji et al., *"CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity"*, ACM BuildSys '22 (`P25`).
   - *Description:* Evaluated dataset providing historical actuals and multi-day forecasts for US ISO regions.

---

## 3. Storage and Reproducibility Policy
- Large trace files ($> 10\text{ MB}$) must not be committed to GitHub.
- Preprocessing scripts and data download scripts will be placed here during the experimental implementation phase.
