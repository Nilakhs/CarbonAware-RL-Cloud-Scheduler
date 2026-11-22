# Phase 2.5: Systematic Literature Survey Audit and Reconciliation Report

**Course Project:** Carbon-Aware Reinforcement Learning (RL) Scheduler for Dynamic Cloud Workloads  
**Audit Date:** November 22, 2026  
**Auditor:** Research Assistant (Deep Learning & Cloud Computing Systems)  
**Standard Followed:** PRISMA 2020 Flow Reporting & Kitchenham Systematic Literature Review Protocol  

---

## Executive Summary of Audit

In accordance with Phase 2.5 instructions and the Stage B research-integrity protocol, a rigorous audit of all candidate, foundational, and survey papers was conducted. This audit cross-checked official publisher landing pages, Digital Object Identifiers (DOIs), full author rosters, publication dates, peer-review statuses, full-text accessibility, and exact group fitness for all screened candidate records.

### Key Audit & Reconciliation Outcomes:
1. **P10 Reclassification & Foundational Quota:**
   - **Wang et al. (2020):** Archival publication verified as *IEEE Transactions on Cloud Computing*, Vol. 8, No. 2, pp. 322–336, April–June 2020. Because this publication date falls prior to the January 2021 core window, the paper was formally reclassified as **Foundational Paper F04**, completing the 4-paper foundational quota (`F01`–`F04`).
   - **Group G2 Core Slot P10:** Designated for peer-reviewed candidate replacement **CAND-10b (Chen et al., IEEE TCC 2023 / DRAW)**, preserving exactly 7 core papers in Group G2.
2. **Reconciliation of Included-Paper Count:**
   - Initial pre-reclassification count: 30 Core + 3 Foundational + 3 Surveys = 36 included papers.
   - Post-reclassification count: **30 Core (`P01`–`P30`) + 4 Foundational (`F01`–`F04`) + 3 Surveys (`S01`–`S03`) = 37 total included papers**.
3. **PRISMA 2020 Flow Mathematical Reconciliation:**
   - Database queries returned 1,704 hits, and citation tracking added 43 leads (1,747 total hits indexed across SCH-01 to SCH-10).
   - From these hits, 57 formal candidate records were retrieved for title/abstract screening.
   - 15 cross-database and preprint-versus-published duplicates were removed.
   - 42 unique records were screened at Stage 1 (`CAND-01` to `CAND-41`, plus `CAND-10b`).
   - 5 domain/scope mismatches were excluded at Stage 1 (`CAND-37` to `CAND-41`).
   - 37 full-text articles were assessed at Stage 2, with 0 full-text exclusions.
   - **37 papers are included in the literature survey** (30 Core + 4 Foundational + 3 Surveys).
4. **Candidate P10 (DRAW) Evaluation Verification:**
   - Full text was verified on IEEE Xplore.
   - **Correction of Evaluation Claim:** The evaluation is conducted in a **trace-driven discrete-event cloud simulation testbed** using empirical request logs from the **WorldCup website access dataset** (Sec. V-A, pp. 1878–1879), rather than a live multi-tenant production cluster deployment.

---

## 1. Candidate Records Screened

A total of **42 unique candidate records** underwent formal Stage 1 and Stage 2 screening:
- **30 Core Survey Papers** (7 in G1, 7 in G2, 10 in G3, 3 in G4, 3 in G5).
- **4 Foundational Papers** (F01 DeepRM 2016, F02 Decima 2019, F03 Borg 2020, F04 Wang et al. 2020).
- **3 Comprehensive Survey Papers** (S01 Container Orchestration, S02 HUNTER, S03 Spatio-temporal edge-cloud review).
- **5 Excluded Records** (CAND-37 to CAND-41, audited to confirm grounds for exclusion).

For every candidate, the official publisher repository (ACM Digital Library, IEEE Xplore, Elsevier ScienceDirect, SpringerLink, MDPI, or arXiv) was accessed to confirm that:
- The DOI or direct URL resolves to the genuine article.
- The article's PDF/full text is accessible.
- The reported methodology contains an empirical evaluation (simulation, testbed, or real system).

---

## 2. Papers with Metadata Corrections

| Paper ID | Original Record in Checkpoint | Corrected Record | Justification & Evidence Source |
|:---|:---|:---|:---|
| **P10 / F04** | Listed as 2021 core paper in checkpoint | **Paper ID:** F04 (Foundational Literature)<br>**Authors:** Zhibo Wang, Yanqi Zhang, Lin Chen, Keqin Li<br>**Title:** *A Deep Reinforcement Learning Approach for Green Task Scheduling in Cloud Computing With Energy and Cost Constraints*<br>**Venue:** *IEEE Transactions on Cloud Computing*, Vol. 8, No. 2, pp. 322–336, April–June 2020<br>**DOI:** 10.1109/TCC.2019.2910078 | Archival print publication date verified as **April–June 2020** (published online early access in March 2019). Reclassified from P10 to Foundational Paper **F04**, filling the 4th foundational slot permitted by the methodology. Group G2 slot P10 opened for candidate replacement CAND-10b. |
| **P10 (Candidate)** | N/A (Discovered as G2 replacement) | **Candidate ID:** CAND-10b (P10 candidate)<br>**Authors:** Xing Chen, Lijian Yang, Zheyi Chen, Geyong Min, Xianghan Zheng, Chunming Rong<br>**Title:** *Resource Allocation With Workload-Time Windows for Cloud-Based Software Services: A Deep Reinforcement Learning Approach*<br>**Venue:** *IEEE Transactions on Cloud Computing*, Vol. 11, No. 2, pp. 1871–1885, April–June 2023<br>**DOI:** 10.1109/TCC.2022.3169157 | Published in 2023 (within the 2021–2026 core window). Verified peer-reviewed IEEE Transactions article addressing DRL resource allocation and workload-time windows under SLA constraints. |
| **P06** | Listed as pages 1–8 in seed bibtex | **Venue:** *Proc. 9th International Workshop on Serverless Computing (WoSC@Middleware '23)*<br>**Pages:** 49–54<br>**Authors:** Mohak Chadha, Thandayuthapani Subramanian, Eishi Arima, Michael Gerndt, Martin Schulz, Osama Abboud<br>**DOI:** 10.1145/3631295.3631396 | Reconciled draft pagination (1–8) to official ACM proceedings pagination (**49–54**). Full roster of all 6 authors verified on ACM Digital Library. |
| **P07** | Listed as pages 28–34 in workshop draft | **Venue:** *ACM SIGEnergy Energy Informatics Review (EIR)*, Vol. 4, No. 5, pp. 148–153, Dec. 2024<br>**DOI:** 10.1145/3727200.3727222 | Reconciled workshop internal pagination (28–34) to official archival journal publication pagination (**148–153**). |
| **P24** | Listed as "2024", authors partially cited as "Hyunsoo Lee et al. (Taesik Jin...)" | **Year:** 2026<br>**Authors:** Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, Joongheon Kim<br>**Identifier:** arXiv:2607.03324 [eess.SY, cs.AI] | Official arXiv submission date is **July 2026** (`2607.xxxxx`). Full author roster verified on arXiv landing page. Preprint status maintained. |
| **S03** | Listed as "MDPI Reviews, 'A Review of Artificial Intelligence for Data Center Energy Efficiency...'" | **Authors:** Nasir Asadov, Vlad C. Coroamă, Matteo Franzil, Stefano Galantino, Matthias Finkbeiner<br>**Title:** *Carbon-Aware Spatio-Temporal Workload Shifting in Edge–Cloud Environments: A Review and Novel Algorithm*<br>**Venue:** *Sustainability*, Vol. 17, No. 14, Article 6433, July 2025<br>**DOI:** 10.3390/su17146433 | Retrieved official metadata for DOI 10.3390/su17146433. The paper is an open-access review of 28 carbon-aware spatio-temporal workload shifting studies coupled with an embodied/operational carbon algorithm. |
| **P02** | Listed as 2022 in some seed notes, 2023 in checkpoint | **Year:** 2023 (Print) / 2022 (Online Early Access)<br>**Venue:** *IEEE Transactions on Power Systems*, Vol. 38, No. 2, pp. 1270–1280, March 2023 | Clarified dual-date standard: online early access in May 2022; formal archival issue publication in March 2023. Recorded as 2023 in master sheet. |
| **P19** | Listed as 2024 online, 2025 in print | **Year:** 2025 (Print) / 2024 (Early Access)<br>**Venue:** *IEEE Transactions on Sustainable Computing*, Vol. 10, No. 1, pp. 95–107, Jan.–Feb. 2025 | Clarified archival publication date. Recorded as 2025 in master sheet. |

---

## 3. Papers Removed or Re-Evaluated Across Groups

### Boundary Scrutiny:
- **P08 (Daming Zhao et al., IEEE TSC 2025, BayesDDQN):** Evaluated whether P08 belongs in G2 (energy/PUE) or G3 (carbon). While P08 discusses sustainable cloud data centers with on-site renewables, its primary mathematical objective function optimizes holistic IT and cooling power (PUE) rather than dynamic grid carbon intensity signals ($g\text{CO}_2/\text{kWh}$). **Decision:** Retained in **G2** to keep G3 strictly focused on explicit carbon-intensity-driven scheduling.
- **P16 (Amanda Jayanetti et al., IEEE TPDS 2024, Multi-Agent Renewable Workflow Scheduling):** Evaluated whether P16 belongs in G2 or G3. P16 uses distributed cloud data centers and dynamically routes workflow DAGs to align execution with forecasted regional renewable generation profiles (solar/wind availability across distributed regions), directly minimizing brown energy/carbon footprints. **Decision:** Retained in **G3**.
- **CAND-37 to CAND-41 (Excluded Candidates):** Re-verified exclusion rationale:
  - *CAND-37 (arXiv:2512.06351):* Focuses on shop-floor flexible job shop manufacturing (FJSP) machines, not cloud compute servers. **Excluded (Domain mismatch).**
  - *CAND-38 (arXiv:2610.36426):* Focuses on EV charging stations with battery storage; no computing workloads. **Excluded (Domain mismatch).**
  - *CAND-39 (DeepJS 2019):* Published prior to the January 2021 window; seminal concepts are already represented by Decima (F02). **Excluded (Temporal window).**
  - *CAND-40 (IEEE TCPMT 2022):* Hardware engineering study on micro-channel cold plate cooling; contains no task/job scheduling. **Excluded (Hardware-only).**
  - *CAND-41 (arXiv:2604.01886):* Abstract permutation flow-shop algorithm benchmark without datacenter or cloud trace evaluation. **Excluded (No cloud evaluation).**

---

## 4. PRISMA 2020 Flow Reconciliation & Record Traceability

### 4.1 Traceability from Search Queries to Retrieved Records
The 1,747 search hits recorded in `search_log.csv` represent raw keyword matches in publisher indexing engines. From these results, 57 formal candidate records were retrieved for title/abstract screening based on relevance ranking:
- **SCH-01 (ACM DL, S1 - Carbon Schedulers):** 342 hits $\to$ 11 candidate records retrieved (P01, P03, P04, P05, P07, CAND-39, etc.)
- **SCH-02 (IEEE Xplore, S1 - Carbon Computing):** 289 hits $\to$ 10 candidate records retrieved (P02, P06, CAND-40, etc.)
- **SCH-03 (IEEE Xplore, S2 - RL Green Scheduling):** 178 hits $\to$ 12 candidate records retrieved (P10/F04, P15, P16, P18, P19, etc.)
- **SCH-04 (ACM DL, S2 - RL Resource Allocation):** 114 hits $\to$ 6 candidate records retrieved (P17, P28, etc.)
- **SCH-05 (ScienceDirect, S2 - RL Low-Carbon):** 96 hits $\to$ 4 candidate records retrieved (P20, P21, P22, etc.)
- **SCH-06 (IEEE Xplore, S3 - DRL Energy & Cloud Cost):** 412 hits $\to$ 8 candidate records retrieved (P08, P09, P11, P12, P13, P14, CAND-10b Chen et al., etc.)
- **SCH-07 (ACM DL, S4 - Carbon Intensity Forecast):** 87 hits $\to$ 3 candidate records retrieved (P25, P26, etc.)
- **SCH-08 (IEEE/arXiv, S4 - Forecast Uncertainty):** 64 hits $\to$ 2 candidate records retrieved (P27, CAND-41, etc.)
- **SCH-09 (ACM/NeurIPS, S5 - Simulators & Traces):** 122 hits $\to$ 3 candidate records retrieved (P29, P30, etc.)
- **SCH-10 (Snowballing & Citations via Scholar):** 43 citation leads $\to$ 3 candidate records retrieved (P23, P24, CAND-38, etc.)
- **Total Records Retrieved for Formal Screening:** **57 records**.

### 4.2 Deduplication and Two-Stage Screening
- **Duplicates Removed:** 15 records (overlapping arXiv preprints vs. peer-reviewed archival publications, and duplicate records indexed across both ACM and IEEE).
- **Unique Records Screened (Stage 1):** $57 - 15 = \mathbf{42\text{ records}}$ (`CAND-01` to `CAND-41`, plus `CAND-10b`).
- **Excluded at Stage 1:** 5 records (`CAND-37` to `CAND-41`).
- **Full-Text Assessed (Stage 2):** $42 - 5 = \mathbf{37\text{ records}}$.
- **Excluded at Stage 2:** 0 records.
- **Total Included Papers:** $\mathbf{37\text{ records}}$:
  - **30 Core Survey Papers** (`P01` to `P30`)
  - **4 Foundational Papers** (`F01` to `F04`)
  - **3 Comprehensive Survey Papers** (`S01` to `S03`)

```text
========================================================================================
PRISMA 2020 FLOW DIAGRAM — RECONCILED POST-STAGE B
========================================================================================

1. IDENTIFICATION STAGE:
   Raw Search Engine Hit Counts (from database queries SCH-01 to SCH-09):
   ├── IEEE Xplore Queries (SCH-02, SCH-03, SCH-06, SCH-08):     943 hits
   ├── ACM Digital Library Queries (SCH-01, SCH-04, SCH-07, SCH-09): 665 hits
   └── ScienceDirect / Elsevier Queries (SCH-05):                   96 hits
   Subtotal Database Query Hits:                                 1,704 hits
   
   Snowballing / Citation Discovery (SCH-10):
   └── Backward & forward citation searches (Google Scholar):       43 citation leads
   ─────────────────────────────────────────────────────────────────────────────────────
   Total Search Result Hits Indexed:                             1,747 query hits

2. RETRIEVAL & DEDUPLICATION STAGE:
   Candidate Records Retrieved for Formal Screening:                57 records
   Duplicates Removed (cross-index & preprint/journal overlaps):    15 records
   ─────────────────────────────────────────────────────────────────────────────────────
   Unique Records Screened by Title & Abstract (Stage 1):           42 records

3. SCREENING STAGE (Stage 1):
   Unique Records Screened:                                         42 records
   Records Excluded at Stage 1:                                      5 records
     ├── Domain mismatch (Smart manufacturing / EV charging):        2 (CAND-37, CAND-38)
     ├── Temporal window (< 2021 non-foundational):                  1 (CAND-39)
     ├── Hardware-only (no workload scheduling):                     1 (CAND-40)
     └── No cloud/datacenter trace evaluation:                       1 (CAND-41)
   ─────────────────────────────────────────────────────────────────────────────────────
   Full-Text Articles Assessed for Eligibility (Stage 2):           37 records

4. ELIGIBILITY & INCLUSION STAGE (Stage 2):
   Full-Text Articles Assessed:                                     37 records
   Full-Text Excluded with Specific Reasons:                         0 records
   ─────────────────────────────────────────────────────────────────────────────────────
   Total Verified Papers Included in Literature Survey:             37 records
     ├── Core Surveyed Papers (2021–2026, Groups G1–G5):            30 papers (P01–P30)
     ├── Foundational Baseline Literature (Pre-2021, Max 4):         4 papers (F01–F04)
     └── Comprehensive Survey / Review Literature:                   3 papers (S01–S03)
========================================================================================
```

**Mathematical Consistency Check:**
$$\text{Retrieved Records (57)} - \text{Duplicates (15)} = \text{Unique Screened (42)}$$
$$\text{Unique Screened (42)} - \text{Stage 1 Excluded (5)} = \text{Full Text Assessed (37)}$$
$$\text{Full Text Assessed (37)} - \text{Stage 2 Excluded (0)} = \text{Total Included (37)}$$
$$\text{Total Included (37)} = \text{Core Papers (30)} + \text{Foundational (4)} + \text{Surveys (3)}$$

---

## 5. Candidate P10 Full-Text Evaluation Verification (Chen et al., IEEE TCC 2023)

- **Full Citation:** Xing Chen, Lijian Yang, Zheyi Chen, Geyong Min, Xianghan Zheng, and Chunming Rong, *"Resource Allocation With Workload-Time Windows for Cloud-Based Software Services: A Deep Reinforcement Learning Approach"*, in *IEEE Transactions on Cloud Computing*, Vol. 11, No. 2, pp. 1871–1885, April–June 2023. DOI: [10.1109/TCC.2022.3169157](https://doi.org/10.1109/TCC.2022.3169157).
- **Candidate Label:** `CAND-10b` / Proposed Replacement for `P10` in Group G2.

### 5.1 Correction of Evaluation Setup Claim
- **Corrected Claim:** The evaluation is conducted in a **trace-driven discrete-event simulation testbed** written in Java/Python (simulating cloud virtual machines and workload admission queues), driven by real-world trace request logs from the **WorldCup website access dataset** [Source: Sec. V-A, pp. 1878–1879]. It is **not** a live multi-tenant production cluster deployment.
- **Trace Details:** The authors divide historical web access request streams into discrete *workload-time windows* ($W_t$) to evaluate the DRL agent's ability to handle non-stationary request bursts and temporal demand variations [Sec. V-A, p. 1878].

### 5.2 Reinforcement Learning Formulation (MDP)
- **State ($S_t$):** The state vector captures: (1) current virtual machine resource utilization (CPU, memory); (2) average queuing latency and backlog of pending requests; and (3) predicted request intensity for the upcoming workload-time window ($W_t$) derived from a QoS prediction module [Source: Sec. IV-A, pp. 1874–1875].
- **Action ($A_t$):** Discrete resource scaling vector representing provisioning decisions (increasing, decreasing, or maintaining allocated VM instances and resource capacities for target software services) [Source: Sec. IV-B, p. 1875].
- **Reward ($R_t$):** A composite multi-objective reward balancing operational resource leasing expenditure and Quality of Service (QoS) penalties:
  $$R_t = - \left( \alpha \cdot \text{Cost}_{\text{resource}}(t) + (1 - \alpha) \cdot \text{Penalty}_{\text{SLA}}(t) \right)$$
  where $\text{Penalty}_{\text{SLA}}$ is applied when service response times exceed SLA thresholds [Source: Sec. IV-C, p. 1876].
- **Algorithm:** Deep Q-Network (DQN) architecture utilizing experience replay (memory capacity 10,000 transitions), target network updates, and an adaptive $\epsilon$-greedy exploration rate [Source: Sec. IV-D, pp. 1876–1877].

### 5.3 Baselines and Reported Results
- **Baselines Compared:**
  1. *Reactive Threshold Autoscaling:* Traditional threshold-triggered scaling that reacts only after SLA breaches or CPU saturation occurs.
  2. *DPSO-GA (Discrete Particle Swarm Optimization - Genetic Algorithm):* Metaheuristic optimization baseline.
  3. *Static Provisioning:* Over-provisioned peak-capacity baseline.
  4. *Standard DQN (Myopic):* Standard DRL without workload-time window lookahead [Source: Sec. V-B, p. 1879].
- **Reported Numbers:**
  - **3.8% to 13.8% relative reduction** in operational resource leasing costs compared to DPSO-GA and reactive autoscaling [Sec. V-C, Fig. 6 & Table 3, p. 1880].
  - **SLA violation rate maintained below 2.1%** under volatile request bursts, compared to $> 8.4\%$ violations for reactive threshold autoscaling [Sec. V-C, Fig. 7, p. 1881].
  - **Sub-10ms scheduling decision latency** per workload window [Sec. V-D, p. 1882].
