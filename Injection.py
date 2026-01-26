# Injection.py
from __future__ import annotations
import json
from typing import Dict, Any, List


def review_candidates(injection_json: Dict[str, Any]) -> Dict[str, Any]:
    """
    CLI reviewer: prompts user yes/no per candidate.
    Produces final JSON with accepted injections only.
    """
    candidates: List[Dict[str, Any]] = injection_json.get("candidates", [])
    accepted: List[Dict[str, Any]] = []

    for idx, c in enumerate(candidates, start=1):
        print("\n" + "=" * 80)
        print(f"[{idx}/{len(candidates)}] Element: {c['element_id']}  Rule: {c['issue_rule_id']}")
        print(f"Issue: {c['issue_message']}")
        print("-" * 80)
        print("Website content snippet:")
        print(c["website_content"][:300])
        print("-" * 80)
        print("Injection script:")
        print(c["injection_script"])
        print("=" * 80)

        while True:
            ans = input("Include this injection? (y/n) ").strip().lower()
            if ans in ("y", "n"):
                break
            print("Please enter 'y' or 'n'.")

        if ans == "y":
            accepted.append(c)

    return {
        "metadata": {
            **injection_json.get("metadata", {}),
            "num_accepted": len(accepted),
        },
        "accepted_injections": accepted,
    }


def save_json(obj: Dict[str, Any], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

