# P29 — Vessim: A Testbed for Carbon-Aware Applications and Systems

**Full citation:** Philipp Wiesner, Ilja Behnke, Paul Kilian, Marvin Steinke, and Odej Kao, "Vessim: A Testbed for Carbon-Aware Applications and Systems", in *Proceedings of the 3rd Workshop on Sustainable Computer Systems (HotCarbon ’24)*, Santa Cruz, CA, USA, July 2024, 8 pages.
**DOI / link:** [https://doi.org/10.48550/arXiv.2306.09774](https://doi.org/10.48550/arXiv.2306.09774) (HotCarbon '24 entry: ACM Digital Library)
**Open-source repository:** [https://github.com/dos-group/vessim](https://github.com/dos-group/vessim) (also mirrored at `https://github.com/vessim/vessim`)
**Type:** Workshop Paper (HotCarbon '24)     **Group:** G5 (Simulators, testbeds, and cloud traces)
**Quality score:** 7.5 / 8  *(Lenient: 8.0 / 8)*
*(Q1: 1.0, Q2: 1.0, Q3: 0.5, Q4: 1.0, Q5: 1.0, Q6: 1.0, Q7: 1.0, Q8: 1.0)*
*(Note on score and primary source audit: Full 8-page HotCarbon '24 / arXiv:2306.09774 preprint downloaded to `literature_survey/papers/P29_Wiesner_Vessim.pdf`; converted to structured Markdown at `literature_survey/markdown_papers/P29.md`; Python architecture and code examples verified directly against the published text and open-source repository).*

---

## 1. Overview & Core Motivation
- **Context & Problem Statement:**
  - Modern data centers and cloud systems are increasingly powered by hybrid microgrids comprising intermittent on-site renewables (solar PV, wind) and battery energy storage systems (BESS).
  - To minimize carbon footprints, *carbon-aware computing* coordinates workload execution with the availability of clean energy via temporal shifting, spatial migration, and dynamic resource throttling.
  - However, research in carbon-aware applications and interfaces between IT systems and energy grids is severely hampered by the **scarcity of standardized testing environments**:
    1. Almost all prior works evaluate algorithms on custom, ad-hoc, in-house simulation scripts (replaying solar traces or carbon intensity series without physical dynamics).
    2. Ad-hoc scripts lead to redundant engineering efforts and zero reproducibility or comparability across papers.
    3. Constructing hardware microgrid testbeds is prohibitively expensive, dangerous, inflexible, and unscalable for geo-distributed evaluations over multi-week or multi-month horizons.
- **Key Contributions of Vessim:**
  - **Co-Simulation Framework:** Built on top of Mosaik (a discrete-event smart-grid co-simulator), Vessim introduces a modular architecture that interconnects domain-specific simulators for renewable power generation, energy storage, public power grids, and real-time IT systems.
  - **Software- and Hardware-in-the-Loop (SIL/HIL):** Enables actual software applications (running in containers, VMs, or physical nodes like NVIDIA Jetson or x86 servers) to interact with simulated energy systems in real time.
  - **First-Class Carbon & Forecast APIs:** Exposes RESTful APIs (following the Ecovisor virtualization philosophy) providing visibility (real-time grid carbon intensity, solar forecasts) and control (battery charge policies, compute throttling, islanding mode).
  - **Integrated Datasets:** Bundles empirical traces from WattTime (Marginal Operating Emissions Rate — MOER), Solcast (solar irradiance across 10 global and 10 German cities), and NREL System Advisor Model (SAM) wind turbines.

---

## 2. Core Methodology & Architecture

### 2.1 Microgrid Co-Simulation Architecture
Vessim abstracts distributed computing systems into one or more parallel `Microgrid` instances managed by Mosaik. Each microgrid orchestrates four distinct co-simulation components:
1. **Actors ($A$):**
   - Entities representing power producers ($p_t^a > 0$) or power consumers ($p_t^a < 0$).
   - Can be pure trace-replaying actors (e.g., historical solar/wind profiles), mathematical power models, or live physical/virtual hardware queried over HTTP/REST or monitoring daemons.
2. **Grid Simulator:**
   - Aggregates power flows at step $t$:
     $$\Delta p_t = \sum_{a \in A} p_t^a$$
   - Can default to an idealized balance node or delegate to high-fidelity power system solvers like **pandapower** or **PyPSA** to compute AC power flow, transmission losses, line congestion, and nodal voltages across complex bus topologies.
3. **Energy Storage ($S$):**
   - Models charging/discharging dynamics between step $t-1$ and $t$ with duration $d$:
     - Receives $\Delta p_t$ and resolves net power flow against current state-of-charge ($SoC$).
     - Returns unserved energy deficit ($e_{t-1} < 0$) or excess generation fed to the public grid ($e_{t-1} > 0$).
     - If no storage is configured, $e_{t-1} = \Delta p_{t-1} \cdot d$.
   - Supports multiple fidelity levels:
     - *SimpleBattery:* Lossless linear battery with capacity limits and min/max SoC.
     - *C/L/C Battery:* Lithium-ion model accounting for round-trip efficiency and linear charge/discharge rate constraints (Kazhamiaka et al., 2019).
     - *PyBaMM Interface:* High-fidelity physics-based electrochemical battery simulation using partial differential equations for lithium-ion dynamics, thermal effects, and degradation.
4. **Controllers ($C$):**
   - Execute at step $t$ with full state visibility: $\text{state}_t^a$ for all $a \in A$, grid balance $\Delta p_t$, storage state $\text{state}_t^s$, prior energy balance $e_{t-1}$, and external signals (carbon intensity, weather forecasts).
   - Can log state (`Monitor`), execute optimization logic (MPC, heuristic rules, RL policies), or serve an asynchronous REST API to external computing systems.

### 2.2 Software- and Hardware-in-the-Loop (SIL/HIL) Real-Time Synchronization
- **Real-Time Constraint:** When real physical nodes or software processes run in the loop, the co-simulation must advance in synchronized wall-clock real time. All simulation steps must compute in less time than the physical step duration ($\Delta t_{\text{sim}} \le \Delta t_{\text{real}}$).
- **Decoupled API Server with Buffer & Cache:**
  - High-frequency API calls from client applications (e.g., thousands of microservices requesting carbon state or updating virtual battery configurations) could overload the Mosaik event queue and cause real-time drift.
  - Vessim implements an **asynchronous buffer and cache**:
    - **GET requests (Visibility):** Answered instantly from an in-memory cache populated at each simulation step without blocking Mosaik.
    - **SET requests (Control):** Queued in an input buffer and aggregated/batched for atomic application at the next discrete simulation step.

---

## 3. Carbon & Energy Modeling

### 3.1 Grid Carbon Intensity
- **Data Source:** WattTime Marginal Operating Emissions Rate (MOER) in $\text{gCO}_2/\text{kWh}$.
- **Geographic Coverage:** Embedded historical traces for `CAISO_NORTH` (California ISO Northern Zone, 2022) with direct compatibility with WattTime and Electricity Maps live/historical APIs.
- **Forecast Mechanisms:**
  - Built-in utilities support:
    1. *Perfect foresight:* Accesses actual future historical time series.
    2. *Replayed historical forecasts:* Replays authentic operational forecasts issued by grid operators/WattTime at historical decision epochs.
    3. *Dynamic predictive models:* User-supplied machine learning forecast models (e.g., CarbonCast / DACF models).

### 3.2 Renewable Generation & Weather Datasets
- **Solar PV Modeling:**
  - Solcast global dataset: 10 geographically diverse cities worldwide (including San Francisco, Sydney, Berlin) and 10 proximate German cities (for localized microgrid spatial correlation).
  - Traces provide surface solar irradiance ($W/m^2$), scaled by panel surface area and efficiency (15%–20%), with optional temperature and tilt angle derating.
- **Wind Energy Modeling:**
  - Integrates the National Renewable Energy Laboratory (NREL) **System Advisor Model (SAM)**, simulating single wind turbines or commercial wind farms based on wind speed, rotor diameter, blade pitch, and hub height.

### 3.3 IT Power Modeling & Hardware Support
- **Physical Nodes:** Directly interfaces with power meters (e.g., networked Power Distribution Units via HTTP/SNMP) or onboard sensors (Intel RAPL, NVIDIA NVML).
- **Virtual Nodes:** Translates CPU/memory utilization metrics from Prometheus or cAdvisor into estimated power using linear, polynomial, or empirical SPECpower benchmark curves.
- **Facility Overhead:** Incorporates static or dynamic Power Usage Effectiveness ($\text{PUE}(t)$) models to capture chiller and UPS overhead.

---

## 4. Empirical Evaluation & Key Results

### 4.1 HotCarbon '24 Example Demonstration: Edge Computing Node with Solar & Battery
- **Experimental Setup:**
  - **Actor 1 (Physical IT Node):** NVIDIA Jetson TX2 running a compute stress test at continuous full load (~15 W baseline), measured via a networked PDU over HTTP (`vs.HttpPowerMeter`).
  - **Actor 2 (Renewable Generation):** 50 W peak solar panel replaying Solcast 2022 San Francisco irradiance.
  - **Storage:** SimpleBattery with 250 Wh capacity, initial $\text{SoC} = 60\%$, minimum allowable $\text{SoC} = 50\%$.
  - **Grid Signal:** WattTime 2022 MOER for CAISO_NORTH.
  - **Step Size:** $\Delta t = 60\text{ s}$ (1 minute), evaluated across a 24-hour cycle.
- **Controller Execution Dynamics:**
  1. *Solar Surplus Phase (09:00–15:00):* Solar output peaks above 40 W; excess power charges the battery towards 100% SoC while powering the Jetson entirely off clean energy.
  2. *Forecast-Driven Deep Discharge (15:00–17:00):* As solar output declines, battery reaches the 50% minimum SoC. The controller queries upcoming solar and carbon forecasts, detects that the public grid is dirty ($\text{MOER} > 400\text{ gCO}_2/\text{kWh}$), and dynamically relaxes the minimum SoC down to 30%, preventing fossil-heavy grid imports.
  3. *Grid-Assisted Pre-Charging (17:00–18:00):* Grid carbon intensity drops dramatically ($\text{MOER} < 60\text{ gCO}_2/\text{kWh}$). The controller purchases clean grid electricity at 40 W constant charging to replenish the battery before nighttime.
  4. *Island Mode & Hardware Throttling (18:00–24:00):* At 18:00, the microgrid switches to island mode. At 20:00, to prevent battery depletion before sunrise, the controller activates the low-power mode on the NVIDIA Jetson TX2, cutting power draw from ~15 W to ~7.5 W.
- **Key Takeaway:** Demonstrates seamless end-to-end software/hardware control loops where grid carbon signals, weather forecasts, battery chemistry, and compute power modes interact safely in real time.

---

## 5. Limitations, Constraints & Research Gaps

### 5.1 Author-Identified Limitations
- **Real-Time Overrun in Complex SIL/HIL Runs:** Real-time simulation requires that all discrete sub-models complete within their physical step duration. Highly complex physics simulators (e.g., PyBaMM with dense finite-element grids or large Pandapower networks) risk falling behind wall-clock time on standard workstations.
- **Physical Validation & Calibration:** Initial prototype models were calibrated against specifications and literature values; full empirical calibration against commercial megawatt-scale datacenter microgrids remains an ongoing milestone.
- **Multi-Resource Scope:** Focuses primarily on electricity and carbon; does not yet model cooling fluid water consumption or server heat recapture (district heating networks).

### 5.2 Our Independent Critical Gaps
- **Workload Granularity in Provided Examples:** The paper illustrates proof-of-concept controllers using simple threshold heuristics and stress-test loops rather than multi-tenant Kubernetes cluster schedulers or production cloud microservice topologies.
- **No Native RL Wrapper Out-of-the-Box:** While Vessim's controller architecture easily interfaces with RL agents (as later demonstrated in FedZero), it relies on custom user code to map states and actions into OpenAI Gym/Gymnasium spaces, unlike SustainGym (P28) which natively exports Gym environments.

---

## 6. Relevance to Our Project & Quality Score Breakdown

### 6.1 Relevance to Project
Vessim is a foundational engineering reference for Group G5:
1. **Co-Simulation Standard for Carbon-Aware Computing:** Provides the architectural blueprint for connecting carbon intensity time series, renewable microgrid battery models, and cloud scheduling algorithms.
2. **Standardized Carbon & Forecast Interfaces:** Demonstrates how carbon APIs should structure perfect forecasts, historical replayed forecasts, and real-time carbon telemetry for RL schedulers.
3. **Decoupled Architecture for Real-Time Execution:** Proves the necessity of asynchronous buffering and caching to prevent cloud scheduling workloads from stalling simulation event loops.

### 6.2 Quality Score Breakdown (7.5 / 8.0, Lenient: 8.0 / 8.0)

| Rubric Item | Score | Evidence & Justification |
| :--- | :---: | :--- |
| **Q1: Relevance to Carbon-Aware Cloud Scheduling** | **1.0** | Purpose-built co-simulation testbed explicitly designed for carbon-aware systems, renewable microgrids, and workload adaptation. |
| **Q2: Problem Formulation & Technical Rigor** | **1.0** | Mathematically rigorous discrete-event co-simulation formulation on Mosaik; formalizes actor power flows, net grid balance, and battery energy equations. |
| **Q3: Carbon Modeling & Trace Grounding** | **0.5** | **0.5 under strict dynamic grid-carbon rule** (Vessim bundles an exemplary sample slice of WattTime CAISO_NORTH 2022 MOER data to demonstrate its API in a 24h single-node demo, but does not provide an extensive empirical grid carbon evaluation; Lenient: 1.0). |
| **Q4: Energy/Workload & Systems Grounding** | **1.0** | Features genuine Hardware-in-the-Loop with NVIDIA Jetson TX2, metered PDU, and Intel RAPL/SPECpower virtual node modeling. |
| **Q5: Baseline & Experimental Comparison** | **1.0** | Evaluated against established state-of-the-art simulators (Ecovisor, Mosaik, PyBaMM, pandapower); proves functional completeness across multiple domains. |
| **Q6: Clarity of Results & Empirical Findings** | **1.0** | Comprehensive multi-trace time-series analysis (Figure 3) tracking power, delta power, battery SoC, grid draw, MOER, and accumulated emissions over 24 hours. |
| **Q7: Open Science, Artifacts & Reproducibility** | **1.0** | Completely open-source under MIT license at `github.com/dos-group/vessim`; installable via PyPI (`pip install vessim`); comprehensive documentation and example notebooks provided. |
| **Q8: Critical Assessment, Constraints & Gaps** | **1.0** | Transparently analyzes real-time SIL execution bottlenecks, buffer/cache requirements, computational complexity of electrochemical battery models, and water/cooling exclusions. |
| **Total Quality Score** | **7.5 / 8.0** | **Strict Score: 7.5 / 8.0 (Lenient: 8.0 / 8.0). High-impact open-source co-simulation testbed for reproducible sustainable computing.** |
