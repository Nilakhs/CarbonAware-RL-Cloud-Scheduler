"""
PDF-to-Markdown Conversion Utility for Academic Literature Survey
=================================================================
Converts research paper PDFs into structured, clean GitHub-flavored Markdown
optimized for LLM analysis, preserving headings, tables, equations, citations,
and exact page markers while stripping repeated running headers/footers.

Default Engine: pymupdf4llm (Lightweight, fast, zero heavy OCR models needed).
Optional Engine: docling (if installed).
"""

import os
import re
import sys
import argparse
from pathlib import Path

# Try importing pymupdf4llm and fitz
try:
    import pymupdf4llm
    import fitz  # PyMuPDF
    PYMUPDF4LLM_AVAILABLE = True
except ImportError:
    PYMUPDF4LLM_AVAILABLE = False

# Try importing tiktoken for exact token measurement
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False


def clean_running_noise(text: str) -> str:
    """
    Remove repetitive running headers, footers, and copyright banners
    commonly found in IEEE, ACM, Springer, and Elsevier papers.
    """
    # Remove IEEE download/permission banners
    text = re.sub(
        r'Authorized licensed use limited to:.*?Downloaded on.*?at.*?UTC from IEEE Xplore.*?Restrictions apply\.',
        '', text, flags=re.DOTALL | re.IGNORECASE
    )
    text = re.sub(
        r'Authorized licensed use limited to:.*?(?=\n\n|\Z)',
        '', text, flags=re.DOTALL | re.IGNORECASE
    )

    # Remove page number banners like "Page X of Y" or solitary page numbers
    text = re.sub(r'^\s*Page\s+\d+\s+of\s+\d+\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)

    # Remove running header strings like "IEEE TRANSACTIONS ON..." or "ACM Trans. on..." on isolated lines
    text = re.sub(r'^\s*IEEE TRANSACTIONS ON\s+[A-Z\s,]+VOL\.\s*\d+.*$', '', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\s*©\s*\d{4}\s*IEEE\..*$', '', text, flags=re.MULTILINE | re.IGNORECASE)

    # Clean up excessive blank lines (more than 2 consecutive newlines)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text.strip()


def convert_pdf_to_markdown(
    pdf_path: str,
    output_path: str = None,
    clean_noise: bool = True,
    insert_page_markers: bool = True,
    engine: str = "pymupdf4llm"
) -> str:
    """
    Convert a single PDF file to structured Markdown.
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if engine == "pymupdf4llm":
        if not PYMUPDF4LLM_AVAILABLE:
            raise ImportError(
                "pymupdf4llm is not installed. Install via:\n"
                "  pip install pymupdf4llm"
            )

        if insert_page_markers:
            # Extract page-by-page chunks to embed explicit page dividers
            page_chunks = pymupdf4llm.to_markdown(str(pdf_file), page_chunks=True)
            formatted_pages = []

            for idx, chunk in enumerate(page_chunks, start=1):
                page_num = chunk.get("metadata", {}).get("page_number", idx)
                page_text = chunk.get("text", "")

                if clean_noise:
                    page_text = clean_running_noise(page_text)

                page_md = (
                    f"\n\n<!-- ==================== Page {page_num} ==================== -->\n"
                    f"**[Page {page_num}]**\n\n"
                    f"{page_text}\n"
                )
                formatted_pages.append(page_md)

            full_md = "".join(formatted_pages).strip()
        else:
            full_md = pymupdf4llm.to_markdown(str(pdf_file))
            if clean_noise:
                full_md = clean_running_noise(full_md)

    elif engine == "docling":
        try:
            from docling.document_converter import DocumentConverter
            converter = DocumentConverter()
            result = converter.convert(str(pdf_file))
            full_md = result.document.export_to_markdown()
            if clean_noise:
                full_md = clean_running_noise(full_md)
        except ImportError:
            raise ImportError(
                "Docling is not installed. Install via:\n"
                "  pip install docling"
            )
    else:
        raise ValueError(f"Unsupported conversion engine: {engine}")

    # Add header metadata block
    doc = fitz.open(str(pdf_file))
    total_pages = len(doc)
    doc.close()

    header_block = (
        f"<!--\n"
        f"CONVERTED RESEARCH PAPER\n"
        f"Source PDF: {pdf_file.name}\n"
        f"Total Pages: {total_pages}\n"
        f"Conversion Engine: {engine}\n"
        f"-->\n\n"
    )
    final_md = header_block + full_md

    if output_path:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(final_md, encoding="utf-8")
        print(f"Successfully converted: {pdf_file.name} -> {out_file}")

    return final_md


def compute_metrics(text: str, encoding_name: str = "cl100k_base") -> dict:
    """
    Compute char count, word count, and exact token count using tiktoken if available.
    """
    chars = len(text)
    words = len(text.split())
    if TIKTOKEN_AVAILABLE:
        enc = tiktoken.get_encoding(encoding_name)
        tokens = len(enc.encode(text))
    else:
        # Fallback estimation: ~4 chars per token for English text
        tokens = int(chars / 4)

    return {"chars": chars, "words": words, "tokens": tokens, "exact_tokens": TIKTOKEN_AVAILABLE}


def benchmark_conversion(pdf_path: str, engine: str = "pymupdf4llm") -> dict:
    """
    Compare raw PDF extracted text vs converted Markdown text and measure token reduction.
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    # 1. Raw extraction using fitz (PyMuPDF plain text)
    doc = fitz.open(str(pdf_file))
    raw_pages = [page.get_text() for page in doc]
    raw_text = "\n".join(raw_pages)
    total_pages = len(doc)
    doc.close()

    raw_metrics = compute_metrics(raw_text)

    # 2. Converted Markdown extraction
    md_text = convert_pdf_to_markdown(
        str(pdf_file),
        clean_noise=True,
        insert_page_markers=True,
        engine=engine
    )
    md_metrics = compute_metrics(md_text)

    # Calculate token delta
    token_delta = md_metrics["tokens"] - raw_metrics["tokens"]
    token_pct = (token_delta / raw_metrics["tokens"]) * 100 if raw_metrics["tokens"] > 0 else 0

    return {
        "paper_name": pdf_file.name,
        "total_pages": total_pages,
        "raw": raw_metrics,
        "markdown": md_metrics,
        "token_delta": token_delta,
        "token_pct": token_pct
    }


def main():
    parser = argparse.ArgumentParser(description="Convert PDF research papers to Markdown for LLM analysis.")
    parser.add_argument("--input-pdf", "-i", type=str, help="Path to input PDF file.")
    parser.add_argument("--output-md", "-o", type=str, help="Path to output Markdown file.")
    parser.add_argument("--paper-id", "-p", type=str, help="Paper ID (e.g., P15, P21) located in literature_survey/papers/.")
    parser.add_argument("--papers-dir", type=str, default="literature_survey/papers", help="Directory containing PDF papers.")
    parser.add_argument("--output-dir", type=str, default="literature_survey/markdown_papers", help="Directory to save converted markdown.")
    parser.add_argument("--engine", type=str, default="pymupdf4llm", choices=["pymupdf4llm", "docling"], help="Conversion engine.")
    parser.add_argument("--benchmark", "-b", action="store_true", help="Run token and character benchmark.")
    parser.add_argument("--no-clean", action="store_true", help="Do not clean running headers/footers.")
    parser.add_argument("--no-page-markers", action="store_true", help="Do not insert page dividers.")

    args = parser.parse_args()

    input_pdf = None
    output_md = None

    if args.input_pdf:
        input_pdf = Path(args.input_pdf)
        if args.output_md:
            output_md = Path(args.output_md)
        else:
            output_md = Path(args.output_dir) / f"{input_pdf.stem}.md"
    elif args.paper_id:
        papers_dir = Path(args.papers_dir)
        matching_pdfs = list(papers_dir.glob(f"{args.paper_id}*.pdf"))
        if not matching_pdfs:
            print(f"Error: No PDF matching '{args.paper_id}*.pdf' found in {papers_dir}")
            sys.exit(1)
        input_pdf = matching_pdfs[0]
        output_md = Path(args.output_dir) / f"{args.paper_id}.md"
    else:
        parser.print_help()
        sys.exit(1)

    if args.benchmark:
        print(f"Running benchmark on: {input_pdf} ...")
        res = benchmark_conversion(str(input_pdf), engine=args.engine)
        print("\n" + "=" * 60)
        print(f"BENCHMARK RESULTS: {res['paper_name']} ({res['total_pages']} pages)")
        print("=" * 60)
        print(f"Raw Text Extracted:    {res['raw']['chars']:,} chars | {res['raw']['words']:,} words | {res['raw']['tokens']:,} tokens")
        print(f"Structured Markdown:   {res['markdown']['chars']:,} chars | {res['markdown']['words']:,} words | {res['markdown']['tokens']:,} tokens")
        print(f"Token Difference:      {res['token_delta']:+,} tokens ({res['token_pct']:+.1f}%)")
        print("=" * 60 + "\n")

    convert_pdf_to_markdown(
        str(input_pdf),
        output_path=str(output_md),
        clean_noise=not args.no_clean,
        insert_page_markers=not args.no_page_markers,
        engine=args.engine
    )


if __name__ == "__main__":
    main()
