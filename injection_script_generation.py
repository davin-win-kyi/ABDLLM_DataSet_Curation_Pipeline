#!/usr/bin/env python3
"""
Overview: Provided the source code of the target websites and the indexed 
WCAG techniques, generate the injection scripts which will be highlighting 
various WCAG errors on target websites
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
load_dotenv.load_dotenv()


# Injection generation configuration variables ---------------------------
DEFAULT_MODEL = "gpt-5.2"      
MAX_HTML_CHARS = 50_000       
SLEEP_BETWEEN_CALLS_S = 0.25
#--------------------------------------------------------------------------  


def extract_json_object(text: str) -> Dict[str, Any]:
    """
    Extract the first JSON object from a string.
    This helps if the model accidentally outputs extra text.
    """
    if not text:
        raise ValueError("Empty model output; expected JSON.")

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Could not locate JSON object in model output:\n{text[:500]}")

    return json.loads(text[start : end + 1])


def coalesce_techniques(wcag_obj: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Support either:
      - wcag_obj["techniques"] with "technique_id"
      - wcag_obj["rules"] with "rule_id" (older)
    """
    if isinstance(wcag_obj.get("techniques"), list):
        return wcag_obj["techniques"]
    if isinstance(wcag_obj.get("rules"), list):
        return wcag_obj["rules"]
    return []


def get_technique_id(t: Dict[str, Any]) -> Optional[str]:
    tid = t.get("technique_id") or t.get("rule_id")
    if not tid:
        return None
    return str(tid).strip().upper()


def get_technique_text(t: Dict[str, Any]) -> str:
    return (t.get("content") or "").strip()


def build_prompt(url: str, html: str, technique_id: str, technique_text: str) -> str:
    html_snippet = html

    return f"""
You are generating a JavaScript injection snippet for accessibility research.

Goal:
- Introduce WCAG failure technique {technique_id} in a minimal way.
- Do NOT break the entire site; prefer localized, subtle DOM/CSS edits.
- The snippet must be runnable with Selenium: driver.execute_script(...)
- Wrap everything in an IIFE + try/catch.
- Must be idempotent: safe to run multiple times.
- Mark changed/inserted elements with data-wcag-injected="{technique_id}".

URL: {url}

Rendered HTML (may be truncated):
<<<HTML
{html_snippet}
HTML>>>

Technique description (if available):
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

    obj = extract_json_object(resp.output_text)

    # Minimal validation
    if "injection_js" not in obj or not isinstance(obj["injection_js"], str) or not obj["injection_js"].strip():
        raise ValueError("Model output missing 'injection_js' (string).")
    if "notes" not in obj:
        obj["notes"] = ""

    return obj


# -----------------------------
# Main
# -----------------------------
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source_code_json", type=str, required=True, help="out/source_code_list.json")
    ap.add_argument("--index_wcag_techniques", type=str, required=True, help="out/index_wcag_techniques.json")
    ap.add_argument("--out_json", type=str, required=True, help="out/injections.json")

    ap.add_argument("--model", type=str, default=DEFAULT_MODEL)
    ap.add_argument("--max_sites", type=int, default=0, help="If >0, only first N sites")
    ap.add_argument("--max_techniques", type=int, default=0, help="If >0, only first N techniques")
    ap.add_argument("--limit_per_site", type=int, default=0, help="If >0, only generate N techniques per site")
    ap.add_argument("--sleep_s", type=float, default=SLEEP_BETWEEN_CALLS_S)
    args = ap.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY environment variable not set.")

    source_path = Path(args.source_code_json).expanduser().resolve()
    wcag_path = Path(args.index_wcag_techniques).expanduser().resolve()
    out_path = Path(args.out_json).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    src_obj = json.loads(source_path.read_text(encoding="utf-8"))
    wcag_obj = json.loads(wcag_path.read_text(encoding="utf-8"))

    sources: List[Dict[str, Any]] = src_obj.get("source_code_list", [])
    techniques: List[Dict[str, Any]] = coalesce_techniques(wcag_obj)

    if args.max_sites and args.max_sites > 0:
        sources = sources[: args.max_sites]
    if args.max_techniques and args.max_techniques > 0:
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
                    "website_source_code": html,
                    "WCAG_technique": {
                        "technique_id": technique_id,
                        "technique_text": technique_text,
                    },
                    "injection": {
                        "injection_js": gen["injection_js"],
                        "notes": gen.get("notes", ""),
                    }
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
            if args.limit_per_site and args.limit_per_site > 0 and used >= args.limit_per_site:
                break

            if args.sleep_s and args.sleep_s > 0:
                time.sleep(args.sleep_s)

    out_obj = {"injections": injections, "failures": failures}
    out_path.write_text(json.dumps(out_obj, indent=2), encoding="utf-8")

    print(f"[OK] Wrote {len(injections)} injections -> {out_path}")
    if failures:
        print(f"[WARN] {len(failures)} pairs failed; see 'failures' in output.")


if __name__ == "__main__":
    main()
