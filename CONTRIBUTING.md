# Contributing Guidelines: Systematic Literature Survey and Research Repository

Thank you for contributing to our Cloud Computing course project on **Carbon-Aware Reinforcement Learning (RL) Schedulers for Dynamic Cloud Workloads**. 

To maintain academic credibility, reproducibility, and rigorous adherence to the **Kitchenham & Charters (2007)** and **PRISMA 2020** protocols, all contributors must strictly follow the workflow outlined in this document.

---

## 1. Paper Identification & Naming Conventions

### 1.1 Paper ID Scheme
Every surveyed work is assigned an immutable, zero-padded identifier:
- **`P01` to `P30`:** Core Survey Papers (published between **January 2021 and November 2026**). Must include an empirical evaluation (simulation, testbed, or real system).
- **`F01` to `F04`:** Foundational Papers (older than 5 years; seminal background literature; maximum of 4 allowed).
- **`S01` to `S04`:** Survey and Review Papers (used for taxonomic cross-checking; not counted among the 30 core papers).

### 1.2 Note File Naming
Individual extraction notes must be placed in `literature_survey/notes/` using the format:
```text
literature_survey/notes/<ID>_<ShortMethodName>.md
```
*Example:* `literature_survey/notes/P06_GreenCourier.md`, `literature_survey/notes/F04_Wang_DRL_Green_Task_Scheduling.md`.

---

## 2. Literature Group Assignments

Every paper must be assigned to **exactly one primary group**:

| Group | Scope & Inclusion Criteria |
|:---:|:---|
| **G1** | **Carbon-Aware Scheduling Without RL:** Heuristics, integer linear programming (ILP/MILP), threshold-based rules, spatial/temporal shifting, or OS-level virtualization. |
| **G2** | **RL for Cloud Scheduling with Energy, Cost, or Performance Goals:** DRL/RL applied to VM consolidation, DVFS, cluster scheduling, or makespan/cost minimization (without explicit grid carbon signals). |
| **G3** | **RL for Carbon-Aware Cloud Scheduling (Core Focus):** DRL/RL where the scheduling agent explicitly optimizes for carbon emissions reduction or dynamically responds to grid carbon intensity ($g\text{CO}_2/\text{kWh}$). |
| **G4** | **Carbon-Intensity Data and Forecasting:** Regional grid data sources, marginal vs. average emission models, and short-term or multi-day carbon forecasting algorithms. |
| **G5** | **Simulators, Datasets, and Workload Traces:** Simulation testbeds (e.g., Vessim, SustainGym), cluster traces (Google Borg, Alibaba), and benchmarking suites. |

---

## 3. Strict Verification & Integrity Protocol

### 3.1 Verification Checklist
Before creating or updating an extraction note, verify the paper against official sources:
1. **DOI / Landing Page:** The DOI or official URL must open the genuine article on IEEE Xplore, ACM Digital Library, ScienceDirect, SpringerLink, or arXiv.
2. **Metadata Accuracy:** Confirm exact title, author roster and order, publication year, volume, issue, and peer-reviewed venue.
3. **Full-Text Review:** Open and read the actual publisher PDF. **Never write notes based solely on abstracts, AI summaries, or search snippets.**
4. **No Fabrication Rule:** Never invent or extrapolate numerical findings, carbon reduction percentages, state/action representations, or citations. If a metric is omitted in the paper, write:  
   `"Not stated in paper"`
5. **Exact Source Location:** Every key claim, number, and limitation must cite the specific section, page, table, or figure (e.g., `[Source: Sec. 4.2, Table 3, p. 25]`).

### 3.2 Handling Author-Stated vs. Observed Gaps
Maintain a clear separation between:
- **Gap Stated by the Authors:** Specific limitations, non-modeled factors, or future work explicitly acknowledged by the authors (quote or closely paraphrase with exact section citation).
- **Gap We Observe:** Our own critical analysis of what the paper lacks (e.g., absence of dynamic arrival queuing, lack of carbon forecast error modeling, lack of multi-region spatial routing).

---

## 4. Standard Extraction Note Template

Every note in `literature_survey/notes/` must strictly follow this markdown structure:

```markdown
# PXX — <Short Name of Method>

**Full citation:** Authors, "Title", *Venue*, Vol.__, No.__, pp.__, Month Year.  
**DOI / link:** https://doi.org/...  
**Type:** Journal / Conference / Preprint     **Group:** G1–G5  
**Quality score:** __ / 8  
*(Q1: _, Q2: _, Q3: _, Q4: _, Q5: _, Q6: _, Q7: _, Q8: _)*  

---

## 1. Problem addressed
What exact problem they solve, in 2–4 sentences.  [Source: Sec __, p. __]

## 2. Approach (the core idea)
The main idea in 2–4 sentences.  [Source: Sec __]

## 3. Methodology
- **System role:** Scheduler / Optimizer / Infrastructure Framework / Simulator
- **Scheduling decision:** When / Where / Both / Resource sizing
- **Workload type:** Batch / Interactive / Scientific workflows / Serverless / Mixed
- **Dynamic or online?** Yes / No, and how
- **For RL papers:**
  - **Algorithm:**
  - **State:**
  - **Action:**
  - **Reward:**
  - **Training setup:**
- **For non-RL papers:** Heuristic or optimization technique used
- **Carbon data source and region:**
- **Workload trace / dataset:**
- **Simulator or real system:**
- **Baselines compared:**
[Source: Sec __, p. __]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:---|:---|:---|:---|
| Carbon reduction | e.g. "X.X% relative reduction" | Baseline name | Table __ / Fig __ |
| SLA / deadline violations | | | |
| Latency / makespan | | | |
| Energy / cost | | | |

## 5. Gap
- **Gap stated by the authors:** Quote or close text.  [Source: Sec __]
- **Gap we observe:** Our own reasoned critique.

## 6. Relevance to our project
1–2 sentences on what we can reuse, adopt, or improve.
```

---

## 5. Quality Assessment (QA) Rubric

Score every paper using the 8-point rubric (**1.0 = Yes, 0.5 = Partly, 0.0 = No**):

| # | Question | Scoring Criteria |
|:---:|:---|:---|
| **Q1** | Is the problem clearly defined? | 1.0 if problem boundaries, cloud workload context, and motivation are unambiguous. |
| **Q2** | Is the method fully described? | 1.0 if algorithms/heuristics are complete; for RL: state, action, reward, and model architecture must all be explicitly defined. |
| **Q3** | Does it use real carbon or energy data? | 1.0 for real grid carbon traces (Electricity Maps, WattTime, CAISO, ENTSO-E) or empirical power traces; 0.5 for synthetic power models. |
| **Q4** | Does it use a real workload trace or testbed? | 1.0 for real cluster traces (Google Borg, Alibaba, Azure) or physical testbeds; 0.5 for purely synthetic arrival distributions. |
| **Q5** | Does it compare against clear baselines? | 1.0 if benchmarked against standard heuristics (FCFS, HEFT, Min-Min) or state-of-the-art schedulers. |
| **Q6** | Are results reported as numbers? | 1.0 if quantitative numbers with explicit comparison baselines are reported (% reduction, latency, SLA infractions). |
| **Q7** | Are code/data available or reproducible? | 1.0 for public GitHub repo or detailed hyperparameters; 0.5 for reproducible description without public repo. |
| **Q8** | Do the authors discuss their limitations? | 1.0 if explicit limitations and future research avenues are discussed. |

- **Threshold:** Papers scoring $< 4.0 / 8$ are relegated to low-quality background and excluded from primary synthesis.

---

## 6. Updating Survey Logs (Step-by-Step)

When adding or revising a paper:
1. **Check for Duplicates:** Search `literature_survey/papers_master.csv` by DOI, title, and first author.
2. **Update `papers_master.csv`:** Ensure columns (`Paper_ID`, `Citation`, `DOI_or_URL`, `Year`, `Venue`, `Publication_Type`, `Group`, `Sub_Label`, `Quality_Score`, `Included`) match the master schema.
3. **Update `search_log.csv`:** If a new query was used, record the database, exact string, date, and hit count.
4. **Update `screening_log.csv`:** Record candidate ID, Stage 1 (title/abstract) and Stage 2 (full-text) decisions and reasons.
5. **Update `verification_log.csv`:** Record official URL, verification status, and date checked.
6. **Update `references.bib`:** Add standard BibTeX entry using key `<ID>_<author><year><keyword>`.

---

## 7. Git & Commit Hygiene
- **Commit Messages:** Use conventional commit formatting:
  - `docs(survey): add extraction note for P08 (BayesDDQN)`
  - `fix(bib): correct pagination for P06 GreenCourier`
  - `chore(repo): update .gitignore and dataset documentation`
- **No Large Binaries / PDFs:** Never commit publisher PDFs, virtual environments (`.venv`), or multi-gigabyte trace files.
- **Review Diffs:** Run `git diff` before staging to verify that no unintended edits occurred.
