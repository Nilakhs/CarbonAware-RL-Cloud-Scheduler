# Literature Survey: Method and Instructions

**Course project:** Carbon-Aware Reinforcement Learning (RL) Scheduler for Cloud Workloads (Dynamic)
**Task:** a literature survey of research papers from the last 5 years.
**Required for each paper:** the problem, the approach, the methodology, the results and the gap.
**Purpose of this document:** it is the plan we both follow. It says how to find papers, how many, how to read them, how to group them, how to check them, and what to hand over. The implementation part comes later and will be built on this survey, so accuracy matters more than speed.

---

## 1. Key terms (use these words the same way in every note)

| Term | Meaning in this survey |
|:--|:--|
| **Carbon intensity** | How much CO2 the electricity grid emits per unit of energy, in gCO2/kWh. It changes every hour with the energy mix (solar, wind, coal, gas). |
| **Carbon-aware scheduling** | Deciding **when** or **where** to run a job so that it uses low-carbon electricity. |
| **Temporal shifting** | Delaying a flexible job to a later time when carbon intensity is lower. |
| **Spatial shifting** | Running a job in another region or data center where carbon intensity is lower now. |
| **Dynamic (our problem)** | Jobs arrive over time, carbon intensity changes over time, and the scheduler decides at run time (online), not with a fixed plan made in advance. |
| **RL formulation** | How a paper turns scheduling into RL. **State** is what the agent sees, **action** is what it decides, and **reward** is what it is trying to maximise. |
| **RL algorithm** | For example DQN, Double DQN, A2C/A3C, PPO, DDPG, SAC, or multi-agent RL. |
| **Baseline** | The method a paper compares itself against, for example FIFO, round robin, a greedy carbon heuristic or a carbon-agnostic scheduler. |
| **SLA / deadline** | The service limit the job must meet, such as a finish-by time or maximum latency. Carbon savings usually trade against this. |

---

## 2. Method we follow

We follow the standard method for a **systematic literature review** in computer science. It is built from three well-known sources, so the steps below are not invented by us:

1. **Kitchenham & Charters (2007), "Guidelines for performing Systematic Literature Reviews in Software Engineering"**: the review protocol, inclusion and exclusion criteria, quality assessment and data extraction.
2. **PRISMA 2020 statement (Page et al., BMJ 2021)**: how to count and report papers at each stage (found → screened → read in full → included).
3. **Wohlin (2014), "Guidelines for snowballing in systematic literature studies" (EASE 2014)**: finding more papers through the reference lists (backward) and the citing papers (forward) of the papers already included.

The whole process has **6 steps**, described in sections 4 to 9.

---

## 3. How many papers

| | Count |
|:--|:--|
| **Core papers** (fully extracted and verified) | **30** (minimum 25) |
| Foundational papers (older than 5 years, allowed only as background, clearly labelled) | up to 4 |
| Survey / review papers (used to find papers and to check our grouping, not counted in the 30) | 2–4 |

**Time window for core papers:** January 2021 to November 2026.

**Target spread across groups** (details in section 9):

| Group | Topic | Target |
|:--|:--|:-:|
| G1 | Carbon-aware scheduling **without** RL (heuristics, optimisation, temporal and spatial shifting) | 7 |
| G2 | RL / deep RL for cloud scheduling with **energy, cost or performance** goals (not carbon) | 7 |
| G3 | RL / deep RL for **carbon-aware** scheduling (the core of our project) | 10 |
| G4 | Carbon-intensity **data and forecasting** (the input our scheduler needs) | 3 |
| G5 | **Simulators, datasets and workload traces** used to test schedulers | 3 |
| | **Total** | **30** |

**G3 is the most important group.** If fewer than 10 good G3 papers exist, write down how many you found and where you searched, and do not fill the gap with weak papers.

---

## 4. Step 1: Search

### 4.1 Where to search (use all of them)
- IEEE Xplore
- ACM Digital Library
- ScienceDirect (Elsevier)
- SpringerLink
- arXiv
- Google Scholar and Semantic Scholar (also to find the published version of an arXiv paper)

### 4.2 Search strings (adapt the syntax to each database)
```text
S1: ("carbon-aware" OR "carbon aware" OR "carbon intensity" OR "low-carbon")
    AND ("scheduling" OR "scheduler" OR "workload shifting")
    AND ("cloud" OR "data center" OR "datacenter")

S2: ("reinforcement learning" OR "deep reinforcement learning" OR "DQN" OR "PPO")
    AND ("carbon" OR "emission" OR "renewable" OR "green")
    AND ("scheduling" OR "task allocation" OR "resource allocation")
    AND ("cloud" OR "data center" OR "edge-cloud")

S3: ("reinforcement learning" OR "deep reinforcement learning")
    AND ("job scheduling" OR "task scheduling" OR "VM placement")
    AND ("energy-aware" OR "energy efficient" OR "cost")
    AND "cloud"

S4: ("carbon intensity" AND ("forecast" OR "prediction"))
    AND ("grid" OR "electricity")

S5: ("cluster trace" OR "workload trace" OR "simulator")
    AND ("carbon" OR "energy") AND "cloud scheduling"
```

### 4.3 Record every search
Keep a **search log** with one row per search: database, exact string, filters, date of search, and number of results. This is what makes the survey repeatable, and it gives the PRISMA counts.

### 4.4 Snowballing
For every included G3 paper, check:
- its **reference list** (backward snowballing);
- the papers that **cite it**, using Google Scholar's "Cited by" (forward snowballing).

Stop when one round of snowballing finds no new relevant papers.

### 4.5 Seed papers to start from
These are real, well-known papers. **Verify each one before using it**, the same as any other paper.
- Wiesner et al., *"Let's Wait Awhile: How Temporal Workload Shifting Can Reduce Carbon Emissions in the Cloud"*, ACM Middleware 2021 (G1).
- Radovanović et al., *"Carbon-Aware Computing for Datacenters"* (Google), IEEE Transactions on Power Systems (G1).
- Acun et al., *"Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters"*, ASPLOS 2023 (G1).
- Souza et al., *"Ecovisor: A Virtual Energy System for Carbon-Efficient Applications"*, ASPLOS 2023 (G1).
- Hanafy et al., *"CarbonScaler: Leveraging Cloud Workload Elasticity for Optimizing Carbon-Efficiency"*, ACM SIGMETRICS (G1).
- Maji et al., *"CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity"*, ACM BuildSys 2022 (G4).
- Foundational, outside the window: Mao et al., *"Resource Management with Deep Reinforcement Learning"* (DeepRM), HotNets 2016; and Mao et al., *"Learning Scheduling Algorithms for Data Processing Clusters"* (Decima), SIGCOMM 2019.

No G3 seed papers are listed on purpose. **Finding them is the main search task.**

---

## 5. Step 2: Screening (inclusion and exclusion)

### 5.1 Include a paper only if **all** of these hold
1. Published **2021–2026** (except the labelled foundational papers).
2. A **peer-reviewed** journal or conference paper. An arXiv preprint is allowed only if it is widely cited or has no published version yet; mark it "preprint".
3. In **English**, with the **full text** available to us.
4. About scheduling or placing **cloud, data-center or edge-cloud workloads**.
5. Fits one of the groups G1–G5.
6. Reports a **method and an evaluation** (experiment, simulation or real deployment). A paper with an idea but no results is not included (except the surveys in section 3).

### 5.2 Exclude
- Hardware-only papers (chip design, cooling hardware) with no scheduling.
- Papers about carbon in other fields (transport, buildings) with no compute workloads.
- Duplicates: keep the most complete version (usually the journal version over the conference version).
- Theses, blogs, white papers and slides.

### 5.3 Two-stage screening
- **Stage 1:** title and abstract. Mark each as include, exclude or unsure.
- **Stage 2:** full text for every "include" and "unsure".

For **every** excluded paper, write the reason in one line, such as "no evaluation" or "not cloud".

### 5.4 PRISMA counts (report these numbers at the end)
```text
Records found in databases:         ___
Records found by snowballing:       ___
Duplicates removed:                 ___
Screened by title/abstract:         ___   excluded: ___
Read in full text:                  ___   excluded: ___ (with reasons)
Included in the survey:             ___
```

---

## 6. Step 3: Quality assessment

Score every included paper with these 8 questions: **1 = yes, 0.5 = partly, 0 = no.**

| # | Question |
|:-:|:--|
| Q1 | Is the problem clearly defined? |
| Q2 | Is the method fully described? For RL papers: are the state, action, reward and algorithm all given? |
| Q3 | Does it use **real** carbon-intensity data (e.g. Electricity Maps, WattTime, national grid operators) and not only made-up values? (For G2, real energy or power data instead.) |
| Q4 | Does it use a **real** workload trace (e.g. Google, Alibaba or Azure traces) or a real system? |
| Q5 | Does it compare against clear baselines? |
| Q6 | Are the results reported as **numbers** (e.g. % carbon reduction, SLA violations, latency)? |
| Q7 | Are the code or data available, or is it described well enough to reproduce? |
| Q8 | Do the authors discuss their own limitations? |

- A paper with **total < 4** is still listed, but goes into a "lower quality" note. It is not used as a main source in the synthesis.
- Write the scores in the master sheet (section 10).

---

## 7. Step 4: Data extraction (the same fields for every paper)

Use **one note file per paper** with exactly these fields. **Every factual field must give where in the paper it comes from** (section number, page, table or figure).

```markdown
# P07 — <short name of the method>

**Full citation:** authors, title, venue, year
**DOI / link:** (must open the paper's publisher or arXiv page)
**Type:** journal / conference / preprint     **Group:** G1–G5
**Quality score:** __ / 8

## 1. Problem addressed
What exact problem they solve, in 2–4 sentences.  [Source: Sec __, p. __]

## 2. Approach (the core idea)
The main idea in 2–4 sentences.  [Source: Sec __]

## 3. Methodology
- Scheduling decision: when / where / both / resource size
- Workload type: batch / interactive / ML training / serverless / mixed
- Dynamic or online? yes/no, and how
- For RL papers:
  - Algorithm:
  - State:
  - Action:
  - Reward:
  - Training setup (episodes, simulator):
- For non-RL papers: optimisation / heuristic used
- Carbon data source and region:
- Workload trace / dataset:
- Simulator or real system:
- Baselines compared:
[Source: Sec __, p. __]

## 4. Results (numbers only, copied exactly)
| Metric | Their result | Compared to | Source |
|:--|:--|:--|:--|
| Carbon reduction | e.g. "x % lower" | baseline name | Table __ / Fig __ |
| SLA / deadline violations | | | |
| Latency / completion time | | | |
| Energy / cost | | | |

## 5. Gap
- **Gap stated by the authors** (limitations / future work), quoted or close to the text:  [Source: Sec __]
- **Gap we observe** (our own reasoning, clearly labelled as ours):

## 6. Relevance to our project
One or two lines: what we can reuse or improve.
```

**Rules for extraction:**
- If the paper does not give a value, write **"Not stated in paper"**. Never estimate or fill it in.
- Copy numbers **exactly** as the paper prints them, with the table or figure number.
- Keep "gap stated by authors" and "gap we observe" separate, so the reader knows which is which.

---

## 8. Step 5: Verification (required for every paper)

This is the step that makes the survey reliable. Tick all items for every paper:

- [ ] The **DOI or link opens the real paper**, and the title, authors, venue and year match exactly.
- [ ] The **PDF was opened and read**; the note is not written from the abstract alone.
- [ ] **Every number** in "Results" was checked against the table or figure it cites.
- [ ] **Every source location** (section or page) is correct.
- [ ] The RL formulation (state, action, reward) matches the paper's own definition.
- [ ] The venue is a real peer-reviewed venue. Check that the journal or conference exists on the publisher's site.

Record this in a **verification log** with one row per paper: paper ID, DOI checked (yes/no), numbers checked (yes/no), checked on (date), and notes.

**Cross-check:** when the work is done, I will pick **6 papers at random** (20 %) and check them against the PDFs myself. Please keep the PDFs and notes organised so this is quick.

### Using AI tools (allowed, with these rules)
AI tools are useful for this work if they are used in the right place:
- **Allowed:** uploading a PDF you have downloaded and asking for a summary of **that PDF**; helping to word your notes; helping to find search terms.
- **Not allowed as a source:** asking an AI to "list papers on X" and using that list directly. AI tools often produce titles, authors, DOIs or numbers that do not exist or are slightly wrong. Every paper must be found and opened on the publisher site, arXiv or Google Scholar.
- After an AI summarises a PDF, **check every number and claim against the PDF** before writing it in the note. The note is what we trust, so it must match the paper.

---

## 9. Step 6: Grouping and synthesis

### 9.1 Grouping
Put each paper in **one main group** (G1–G5, section 3). Inside the groups, add sub-labels so similar approaches sit together:
- **G1:** temporal shifting / spatial shifting / both / resource scaling.
- **G2 and G3:** value-based RL (DQN family) / policy-gradient RL (A2C, PPO) / actor-critic for continuous actions (DDPG, SAC) / multi-agent RL / RL combined with forecasting.
- **G3 also:** single objective (carbon only) / multi-objective (carbon + SLA / cost / latency).

If a paper fits two groups, choose the main one and mention the second in its note.

### 9.2 Comparison table per group
Make one table per group with one row per paper:

| ID | Year | Approach (1 line) | RL algorithm / method | Decision (when/where) | Dynamic? | Carbon data | Trace | Main result | Main gap |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|

### 9.3 Synthesis: what the survey must conclude
Write these sections in the final report, each based on the tables:
1. **What has been done:** the main trends per group and how they changed from 2021 to 2026.
2. **What works best and under which conditions,** using only the reported numbers.
3. **Common gaps across papers.** Questions to check for every G3 paper:
   - Does it handle **dynamic** job arrivals and changing carbon intensity together?
   - Does it balance carbon against **SLA or deadlines**, or only reduce carbon?
   - Does it use **real carbon data** and **real traces**?
   - Does it consider **forecast error** in carbon intensity?
   - Was it tested in a **real system** (e.g. Kubernetes) or only in simulation?
   - How much **training** does the RL agent need, and does it **generalise** to new regions or workloads?
4. **Candidate gaps for our project:** 2–3 gaps that a course project can realistically address, each linked to the papers that show the gap.

---

## 10. What to hand over

```text
CC_Course_project/
└── literature_survey/
    ├── Literature_Survey_Report.md   (the final report: sections in 10.1)
    ├── papers_master.csv             (one row per paper: ID, citation, DOI, year, venue, type, group, sub-label, quality score, included yes/no)
    ├── search_log.csv                (one row per search, section 4.3)
    ├── screening_log.csv             (every screened paper + include/exclude + reason)
    ├── verification_log.csv          (section 8)
    ├── references.bib                (all citations, same IDs as the master sheet)
    └── notes/
        ├── P01_<shortname>.md
        ├── P02_<shortname>.md
        └── ...
```
Keep the **PDFs in a local folder only** (e.g. `pdfs/`, not pushed to GitHub), because most papers are copyrighted. The notes and DOIs are enough to find them.

### 10.1 Sections of the final report
1. Introduction: the problem and why carbon-aware scheduling matters.
2. Background: carbon intensity, cloud scheduling, and RL basics (state, action, reward).
3. Survey method: databases, search strings, criteria, quality assessment and PRISMA counts (from this document).
4. Taxonomy: a diagram of the groups G1–G5 and their sub-labels.
5. One section per group: a short summary + the comparison table.
6. Synthesis: trends, what works, common gaps (section 9.3).
7. Gaps our project will address.
8. Threats to validity: the limits of our search (for example, papers behind paywalls we could not access, and the English-only rule).
9. References.

---

## 11. Order of work (6 steps)

1. Read this document and the key terms (section 1).
2. Run the searches and fill in the search log (section 4).
3. Screen the results and keep the screening log (section 5).
4. Read each included paper in full, score it, and write its note (sections 6 and 7).
5. Verify each note and fill in the verification log (section 8).
6. Group the papers, build the comparison tables and write the report (sections 9 and 10).

**Share progress after step 3** (the list of included papers, with group and DOI). Then we can agree on the final 30 before the detailed reading starts. This saves time if a paper needs to be swapped.
