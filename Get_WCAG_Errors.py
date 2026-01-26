# Get_WCAG_Errors.py
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional


@dataclass
class WcagIssue:
    rule_id: str
    severity: str           # "info" | "minor" | "major" | "critical"
    message: str
    evidence: Optional[str] = None
    supporting_rag: Optional[List[Dict[str, Any]]] = None  # top rag snippets


@dataclass
class ElementIssues:
    element_id: str
    source_path: str
    issues: List[WcagIssue]


def _heuristic_checks(content: str) -> List[WcagIssue]:
    c = content.lower()
    issues: List[WcagIssue] = []

    if "<img" in c and "alt=" not in c:
        issues.append(
            WcagIssue(
                rule_id="1.1.1",
                severity="major",
                message="Image appears to be missing alt text.",
                evidence=content.strip()[:240],
            )
        )

    if "<input" in c and ("aria-label" not in c and "aria-labelledby" not in c and "label" not in c):
        issues.append(
            WcagIssue(
                rule_id="1.3.1",
                severity="major",
                message="Form control may be missing an accessible label.",
                evidence=content.strip()[:240],
            )
        )

    if "<button" in c and "</button>" in c:
        inner = content.split(">", 1)[-1].rsplit("</button>", 1)[0].strip()
        if len(inner) == 0 and "aria-label" not in c:
            issues.append(
                WcagIssue(
                    rule_id="4.1.2",
                    severity="major",
                    message="Button may be missing an accessible name (no text and no aria-label).",
                    evidence=content.strip()[:240],
                )
            )

    return issues


def _attach_rag_support(issue: WcagIssue, rag_hits: Optional[List[Dict[str, Any]]], top_n: int = 3) -> WcagIssue:
    if not rag_hits:
        return issue
    # Keep small, relevant, JSON-friendly
    issue.supporting_rag = [
        {
            "score": h.get("score"),
            "metadata": h.get("metadata", {}),
            "text_snippet": (h.get("text", "") or "")[:350],
        }
        for h in rag_hits[:top_n]
    ]
    return issue


def get_wcag_errors(rag_elements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results: List[ElementIssues] = []

    for el in rag_elements:
        issues = _heuristic_checks(el["content"])
        rag_hits = el.get("rag_hits")  # list[{text, score, metadata}]

        issues = [_attach_rag_support(i, rag_hits, top_n=3) for i in issues]

        results.append(
            ElementIssues(
                element_id=el["id"],
                source_path=el["source_path"],
                issues=issues,
            )
        )

    return [asdict(r) for r in results]
