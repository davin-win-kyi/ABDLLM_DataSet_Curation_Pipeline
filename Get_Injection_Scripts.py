# Get_injection_Scripts.py
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class InjectionCandidate:
    element_id: str
    source_path: str
    issue_rule_id: str
    issue_message: str
    injection_script: str
    website_content: str
    supporting_rag: List[Dict[str, Any]]


def _script_for_issue(rule_id: str) -> str:
    """
    Broad, safe-ish default scripts. Next step is generating selectors
    so you patch only the *specific* element.
    """
    if rule_id == "1.1.1":
        return (
            "(() => {\n"
            "  const imgs = document.querySelectorAll('img:not([alt])');\n"
            "  imgs.forEach(img => {\n"
            "    // TODO: replace with meaningful alt text based on surrounding context\n"
            "    img.setAttribute('alt', 'Image');\n"
            "  });\n"
            "})();"
        )

    if rule_id == "1.3.1":
        return (
            "(() => {\n"
            "  const fields = document.querySelectorAll('input, select, textarea');\n"
            "  fields.forEach(el => {\n"
            "    const hasLabel = el.id && document.querySelector(`label[for=\"${el.id}\"]`);\n"
            "    const hasAria = el.getAttribute('aria-label') || el.getAttribute('aria-labelledby');\n"
            "    if (!hasLabel && !hasAria) {\n"
            "      // TODO: replace with meaningful label, ideally derived from nearby text\n"
            "      el.setAttribute('aria-label', 'Input');\n"
            "    }\n"
            "  });\n"
            "})();"
        )

    if rule_id == "4.1.2":
        return (
            "(() => {\n"
            "  const buttons = document.querySelectorAll('button');\n"
            "  buttons.forEach(btn => {\n"
            "    const hasText = (btn.textContent || '').trim().length > 0;\n"
            "    const hasAria = !!btn.getAttribute('aria-label');\n"
            "    if (!hasText && !hasAria) {\n"
            "      // TODO: replace with meaningful accessible name\n"
            "      btn.setAttribute('aria-label', 'Button');\n"
            "    }\n"
            "  });\n"
            "})();"
        )

    return "// No injection rule implemented for this issue.\n"


def build_injection_candidates(
    rag_elements: List[Dict[str, Any]],
    element_issues: List[Dict[str, Any]],
) -> Dict[str, Any]:
    element_by_id = {e["id"]: e for e in rag_elements}

    candidates: List[InjectionCandidate] = []

    for ei in element_issues:
        el = element_by_id.get(ei["element_id"])
        if not el:
            continue

        for issue in ei["issues"]:
            rule_id = issue["rule_id"]
            script = _script_for_issue(rule_id)

            candidates.append(
                InjectionCandidate(
                    element_id=ei["element_id"],
                    source_path=ei["source_path"],
                    issue_rule_id=rule_id,
                    issue_message=issue["message"],
                    injection_script=script,
                    website_content=el["content"],
                    supporting_rag=issue.get("supporting_rag") or [],
                )
            )

    return {
        "metadata": {
            "num_elements": len(rag_elements),
            "num_candidates": len(candidates),
        },
        "candidates": [asdict(c) for c in candidates],
    }
