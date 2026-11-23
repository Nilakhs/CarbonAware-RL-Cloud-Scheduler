# Research Paper PDF-to-Markdown Conversion Workflow

This workflow optimizes the literature survey pipeline for papers **P21–P30** by converting academic research PDFs into structured, clean Markdown before LLM analysis. This eliminates PDF rendering/vision token overhead, strips formatting noise, normalizes multi-column reading flows, and formats tables as standard Markdown tables while preserving exact page and equation citations.

---

## 1. Directory Structure & File Organization

```
literature_survey/
├── papers/                      # Original PDF papers (UNTOUCHED)
│   ├── P15_Zhang_Sustainable_AIGC.pdf
│   ├── P17_Wang_ERLFC.pdf
│   └── P21_...pdf               # Incoming PDFs for P21-P30
├── markdown_papers/             # Converted Markdown papers for LLM ingestion
│   ├── P15.md                   # Validated benchmark artifact
│   └── P21.md ... P30.md        # Converted target papers
├── scripts/
│   └── pdf_to_markdown.py       # Reusable conversion and benchmarking utility
├── notes/                       # Final 6-section literature survey notes
│   ├── P01_...md ... P20_...md
└── PAPER_ANALYSIS_PROMPT.md     # Reusable extraction prompt for LLM analysis
```

---

## 2. Environment Setup & Dependencies

The conversion utility is lightweight and requires Python 3.10+. It uses **`pymupdf4llm`** (backed by MuPDF C++ layout analysis) as its primary engine because it extracts multi-column text, tables, and math in seconds without needing gigabytes of deep-learning OCR weights. It also supports **`docling`** as an alternative engine.

### Installation Commands:
```bash
# Recommended lightweight engine (converts papers in 2–5 seconds, <25 MB install):
pip install pymupdf4llm tiktoken

# Optional deep-learning OCR engine (requires PyTorch, ~1.5 GB install):
pip install docling
```

*Note: In the current repository environment, Python 3.11 is located at:*
`C:\Users\nilak\AppData\Local\Python\bin\python3.11.exe`

---

## 3. How to Run the Conversion

### A. Convert a Specific Paper by ID:
```powershell
python literature_survey/scripts/pdf_to_markdown.py --paper-id P21
```
*Locates `P21*.pdf` in `literature_survey/papers/` and outputs `literature_survey/markdown_papers/P21.md`.*

### B. Convert an Arbitrary PDF File:
```powershell
python literature_survey/scripts/pdf_to_markdown.py -i path/to/paper.pdf -o literature_survey/markdown_papers/P21.md
```

### C. Run with Benchmarking & Token Measurement:
```powershell
python literature_survey/scripts/pdf_to_markdown.py --paper-id P15 --benchmark
```

---

## 4. Key Preservation & Cleaning Rules

The conversion script enforces:
1. **Section Heading Hierarchy:** Converts font size and weight into standard `#`, `##`, and `###` headers.
2. **Table Reconstruction:** Formats two-dimensional data grids into standard GitHub-flavored Markdown tables (`| Col1 | Col2 |`).
3. **Equation & Math Preservation:** Retains LaTeX notation (`$x$`, `$$x$$`), superscripts, and subscripts (`<sup>`, `<sub>`).
4. **Exact Page Markers:** Injects unambiguous page dividers:
   ```markdown
   <!-- ==================== Page 3 ==================== -->
   **[Page 3]**
   ```
   This guarantees that LLMs can cite exact page numbers for every extracted claim without needing the raw PDF open.
5. **Noise Removal:** Strips repetitive running headers (e.g., `Page X of Y`, `IEEE TRANSACTIONS ON...`) and publisher copyright banners (`Authorized licensed use limited to...`).

---

## 5. Token-Saving & Quality Benchmark Results

We validated the conversion utility across real academic papers in the survey:

| Paper ID | Description | Pages | Raw Extracted Text | Structured Markdown | Token Difference (cl100k_base) | Status & QA Assessment |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **P15** | *Zhang et al., IEEE TASE 2023* (Multi-column IEEE conference/journal) | 6 | 30,225 chars / 8,635 tokens | 35,425 chars / 10,115 tokens | +1,480 tokens (+17.1%)* | **PASS:** Tables converted to valid Markdown; equations (1)–(5) preserved; page markers injected. |
| **P17** | *Wang et al., J. Cloud Comput. 2023* (Long Springer Open journal) | 17 | 63,903 chars / 16,434 tokens | 66,516 chars / 15,581 tokens | **-853 tokens (-5.2%)** | **PASS:** Stripped 16 running header instances (`Page X of 17`); flattened two-column layout cleanly. |

*\*Note on Token Dynamics: In dense mathematical papers like P15, token count increases modestly compared to raw unformatted text because `pymupdf4llm` reconstructs HTML table tags (`<br>`), Markdown table borders (`|`), and math superscripts (`<sup>`), which prevent the classic LLM failure mode of misreading unaligned columns. In longer papers like P17, removing redundant page headers and normalizing whitespace produces a net token reduction.*

### Comparison Against Vision/Multimodal Ingestion:
If research PDFs are uploaded directly to an LLM as visual documents:
- A 17-page paper (e.g., P17) consumes **~20,400 to 25,500 visual tokens** (1,200–1,500 tokens/page).
- Converted Markdown consumes only **15,581 text tokens** (a **~25% to 40% reduction in token consumption**), with near-instantaneous processing and zero OCR misalignment.

---

## 6. How to Use Converted Markdown with the LLM Analysis Prompt

1. Convert incoming paper:
   ```powershell
   python literature_survey/scripts/pdf_to_markdown.py --paper-id P21
   ```
2. Feed `literature_survey/markdown_papers/P21.md` into the LLM alongside the instructions in:
   `literature_survey/PAPER_ANALYSIS_PROMPT.md`
3. The LLM extracts the 6-section note and evaluates Q1–Q8 with exact page citations.
4. If any diagram or complex matrix in the Markdown is ambiguous, consult the original PDF in `literature_survey/papers/`.
