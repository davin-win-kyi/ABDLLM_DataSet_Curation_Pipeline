#!/usr/bin/env python3
"""
Overview:
Given the source code of target websites and indexed WCAG techniques,
generate JavaScript injection scripts highlighting WCAG errors.

This version:
- Removes ALL JavaScript-related content from HTML
- Keeps full static DOM context
- Hard-caps HTML to avoid model context overflows
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from openai import OpenAI
import load_dotenv
from bs4 import BeautifulSoup

load_dotenv.load_dotenv()

# --------------------------------------------------------------------------
# Configuration
DEFAULT_MODEL = "gpt-5.2"
MAX_HTML_CHARS = 12_000       # safe cap after JS removal
SLEEP_BETWEEN_CALLS_S = 0.25
# --------------------------------------------------------------------------


# ----------------------------- Utilities ----------------------------------

def extract_json_object(text: str) -> Dict[str, Any]:
    """Extract the first JSON object from model output."""
    if not text:
        raise ValueError("Empty model output; expected JSON.")

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Could not locate JSON object in model output:\n{text[:500]}")

    return json.loads(text[start:end + 1])


# ---------------------- WCAG helpers --------------------------------------

def get_techniques(wcag_obj: Dict[str, Any]) -> List[Dict[str, Any]]:
    if isinstance(wcag_obj.get("techniques"), list):
        return wcag_obj["techniques"]
    if isinstance(wcag_obj.get("rules"), list):
        return wcag_obj["rules"]
    return []


def get_technique_id(t: Dict[str, Any]) -> Optional[str]:
    tid = t.get("technique_id") or t.get("rule_id")
    return str(tid).strip().upper() if tid else None


def get_technique_text(t: Dict[str, Any]) -> str:
    return (t.get("content") or "").strip()


# --------------------- JavaScript stripping --------------------------------

def strip_all_javascript(html: str) -> str:
    """
    Return a static HTML snapshot by removing all JavaScript content.

    Removes:
      - <script> tags (inline + external)
      - <noscript> blocks
      - inline JS handlers (onclick, onload, ...)
      - javascript: URLs

    Preserves:
      - Full DOM structure
      - Parent/sibling context
      - Semantic HTML
      - CSS classes and inline styles
    """
    soup = BeautifulSoup(html, "lxml")

    # Remove script sources
    for tag in soup.find_all(["script", "noscript"]):
        tag.decompose()

    # Remove inline JS handlers and javascript: URLs
    for tag in soup.find_all(True):
        for attr in list(tag.attrs.keys()):
            if attr.lower().startswith("on"):
                del tag.attrs[attr]

        if tag.has_attr("href") and isinstance(tag["href"], str):
            if tag["href"].strip().lower().startswith("javascript:"):
                tag["href"] = "#"

        if tag.has_attr("src") and isinstance(tag["src"], str):
            if tag["src"].strip().lower().startswith("javascript:"):
                del tag.attrs["src"]

    return str(soup)


# ------------------------- Prompting --------------------------------------

def build_prompt(url: str, html: str, technique_id: str, technique_text: str) -> str:
    static_html = strip_all_javascript(html)
    if len(static_html) > MAX_HTML_CHARS:
        static_html = static_html[:MAX_HTML_CHARS] + "\n<!-- TRUNCATED -->"

    return f"""
    You are generating a JavaScript injection snippet for accessibility research.

    ABSOLUTE RULES (must follow):
    1) You MUST modify ONLY existing elements already present in the page.
    2) You MUST NOT create any new elements or UI.
    - Do NOT use: document.createElement, innerHTML=, insertAdjacentHTML, appendChild, prepend, insertBefore.
    - Do NOT inject overlays, banners, popups, tooltips, or fixed-position panels.
    3) Prefer a small number of edits (1–3 elements max).
    4) Idempotent:
    - Do nothing if the chosen target element already has data-wcag-injected="{technique_id}".
    5) Add data-wcag-injected="{technique_id}" to every element you modify.
    6) Preserve reversibility:
    - Before changing an attribute/style/text, store the previous value in a data-wcag-original-* attribute.

    Targeting requirements:
    - Choose a stable CSS selector that matches existing elements in this page.
    - Your script must:
    a) querySelector/querySelectorAll for candidates
    b) if none found, gracefully do nothing and set notes explaining "no suitable target found"
    c) modify an existing element in a way that introduces failure technique {technique_id}

    URL: {url}

    Static HTML snapshot (JavaScript removed):
    <<<HTML
    {static_html}
    HTML>>>

    Technique description:
    <<<TECHNIQUE
    {technique_text}
    TECHNIQUE>>>

    Return ONLY valid JSON (no markdown, no commentary), exactly:
    {{
    "injection_js": "...",
    "notes": "..."
    }}
    """.strip()



def gpt_generate_injection(
    client: OpenAI,
    model: str,
    url: str,
    html: str,
    technique_id: str,
    technique_text: str,
) -> Dict[str, Any]:
    prompt = build_prompt(url, html, technique_id, technique_text)

    resp = client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}],
    )

    return extract_json_object(resp.output_text)


# ----------------------------- CLI ----------------------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()

    ap.add_argument("--source_code_json", type=str, required=True)
    ap.add_argument("--index_wcag_techniques", type=str, required=True)
    ap.add_argument("--out_json", type=str, required=True)

    ap.add_argument("--model", type=str, default=DEFAULT_MODEL)
    ap.add_argument("--max_sites", type=int, default=0)
    ap.add_argument("--max_techniques", type=int, default=0)
    ap.add_argument("--limit_per_site", type=int, default=0)
    ap.add_argument("--sleep_s", type=float, default=SLEEP_BETWEEN_CALLS_S)

    return ap


def main() -> None:
    args = build_arg_parser().parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY environment variable not set.")

    source_path = Path(args.source_code_json).expanduser().resolve()
    wcag_path = Path(args.index_wcag_techniques).expanduser().resolve()
    out_path = Path(args.out_json).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    src_obj = json.loads(source_path.read_text(encoding="utf-8"))
    wcag_obj = json.loads(wcag_path.read_text(encoding="utf-8"))

    sources: List[Dict[str, Any]] = src_obj.get("source_code_list", [])
    techniques: List[Dict[str, Any]] = get_techniques(wcag_obj)

    if args.max_sites > 0:
        sources = sources[: args.max_sites]
    if args.max_techniques > 0:
        techniques = techniques[: args.max_techniques]

    client = OpenAI()

    injections: List[Dict[str, Any]] = []
    failures: List[Dict[str, Any]] = []

    for s_idx, site in enumerate(sources):
        url = site.get("Url")
        html = site.get("Source_code") or ""
        if not url:
            continue

        used = 0
        for tech in techniques:
            technique_id = get_technique_id(tech)
            if not technique_id:
                continue

            technique_text = get_technique_text(tech)
            print(f"[{s_idx+1}/{len(sources)}] {url} × {technique_id}")

            try:
                gen = gpt_generate_injection(
                    client=client,
                    model=args.model,
                    url=url,
                    html=html,
                    technique_id=technique_id,
                    technique_text=technique_text,
                )

                injections.append({
                    "url": url,
                    "WCAG_technique": {
                        "technique_id": technique_id,
                        "technique_text": technique_text,
                    },
                    "injection": gen,
                })

            except Exception as e:
                failures.append({
                    "url": url,
                    "technique_id": technique_id,
                    "error": str(e),
                    "timestamp_unix": time.time(),
                })
                print(f"[WARN] Failed {url} × {technique_id}: {e}")

            used += 1
            if args.limit_per_site > 0 and used >= args.limit_per_site:
                break

            if args.sleep_s > 0:
                time.sleep(args.sleep_s)

    out_path.write_text(
        json.dumps({"injections": injections, "failures": failures}, indent=2),
        encoding="utf-8",
    )

    print(f"Wrote {len(injections)} injections → {out_path}")


if __name__ == "__main__":
    main()
