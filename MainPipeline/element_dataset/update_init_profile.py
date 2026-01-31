#!/usr/bin/env python3
"""
update_init_profile.py

Fifth method + class:
- Load init_profile.json
- Load element_dataset.json
- Use both to update "user_description" via a GPT call that must return JSON:
    { "updated_list": [ ... ] }
- Write updated list back to init_profile.json ("intial_profile.user_description")

Requirements:
- pip install openai>=1.0.0
- Env var: OPENAI_API_KEY

Usage:
  export OPENAI_API_KEY=sk-...
  python update_init_profile.py \
      --init init_profile.json \
      --elements element_dataset.json \
      --model gpt-5 \
      --dry-run
"""

import os
import json
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from openai import OpenAI


@dataclass
class UpdateConfig:
    init_profile_path: Path
    elements_path: Path
    model: str = "gpt-5"
    dry_run: bool = False
    max_elements_for_prompt: int = 150  # cap to keep prompts sane
    max_feedback_per_element: int = 5   # cap per element
    dedupe_casefold: bool = True        # dedupe user_description strings by lowercase


class UpdateInitProfile:
    """
    Read init_profile.json + element_dataset.json, ask GPT to synthesize an updated
    user_description list (add/remove/revise), then write back to init_profile.json.
    Strict mode: no heuristic fallback—errors if model output is invalid.
    """

    def __init__(self, cfg: UpdateConfig):
        self.cfg = cfg
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment.")
        self.client = OpenAI(api_key=api_key)

    # ---------- Public API ----------
    def update_user_description(self) -> List[str]:
        profile = self._load_json(self.cfg.init_profile_path)
        elements = self._load_json(self.cfg.elements_path)

        current_desc = self._get_current_user_description(profile)
        elem_feedback = self._extract_element_feedback(elements)

        updated_list = self._call_gpt_for_updated_list(
            current_desc=current_desc,
            elem_feedback=elem_feedback,
        )

        # Validate strictly (no fallback)
        if not isinstance(updated_list, list) or not all(isinstance(s, str) for s in updated_list):
            raise RuntimeError(
                "Model did not return a valid {\"updated_list\": [str, ...]}. "
                "Enable --dry-run and inspect logs, or adjust your model/prompt."
            )

        # Optional: dedupe + strip
        updated_list = self._dedupe_and_strip(updated_list, casefold=self.cfg.dedupe_casefold)

        # Persist
        if self.cfg.dry_run:
            print("[DRY RUN] New user_description would be:\n", json.dumps(updated_list, indent=2))
        else:
            self._persist_user_description(profile, updated_list)

        return updated_list

    # ---------- IO Helpers ----------
    @staticmethod
    def _load_json(path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _persist_user_description(self, profile: Dict[str, Any], updated: List[str]) -> None:
        if "intial_profile" not in profile or not isinstance(profile["intial_profile"], dict):
            raise ValueError('Expected top-level key "intial_profile" in init_profile.json')

        profile["intial_profile"]["user_description"] = updated

        with self.cfg.init_profile_path.open("w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)

        print(f"[OK] Wrote updated user_description to {self.cfg.init_profile_path}")

    # ---------- Data Prep ----------
    @staticmethod
    def _get_current_user_description(profile: Dict[str, Any]) -> List[str]:
        try:
            desc = profile["intial_profile"]["user_description"]
        except Exception as e:
            raise ValueError('init_profile.json must contain intial_profile.user_description (list[str])') from e

        if not isinstance(desc, list) or not all(isinstance(s, str) for s in desc):
            raise ValueError("intial_profile.user_description must be a list of strings.")
        return desc

    def _extract_element_feedback(self, elements_doc: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Return a compact list of element feedback entries with:
        - id
        - type
        - descriptor
        - feedback (subset)
        """
        items: List[Dict[str, Any]] = []
        raw = elements_doc.get("Elements", [])
        if not isinstance(raw, list):
            return items

        for el in raw[: self.cfg.max_elements_for_prompt]:
            if not isinstance(el, dict):
                continue
            items.append({
                "id": el.get("ID"),
                "type": el.get("Element_type"),
                "descriptor": el.get("Element_descriptor"),
                "feedback": list(el.get("Element feedback", []))[: self.cfg.max_feedback_per_element],
            })
        return items

    # ---------- GPT Call ----------
    def _call_gpt_for_updated_list(
        self,
        current_desc: List[str],
        elem_feedback: List[Dict[str, Any]],
    ) -> List[str]:
        """
        Ask GPT for a JSON object strictly shaped as:
            { "updated_list": [ <strings> ] }
        The model may add/remove/rewrite entries to better reflect user needs implied
        by element descriptors + feedback, preserving meaning when possible.
        """
        system = (
            "You are an accessibility and HCI assistant. "
            "Given a current user description and observed UI element feedback "
            "(element descriptors and feedback texts), return ONLY a strict JSON object:\n"
            '{ "updated_list": [ ... ] }\n'
            "Rules:\n"
            "- Output must be strictly valid JSON (no commentary, no trailing commas).\n"
            "- The list should be short, descriptive tags/phrases about the user's needs/preferences.\n"
            "- You MAY add, remove, or revise entries. Avoid duplicates and vague phrases.\n"
            "- Prefer actionable, concrete statements (e.g., 'prefers high contrast', "
            "'needs larger touch targets', 'uses screen reader: VoiceOver').\n"
        )

        compact_feedback = []
        for s in elem_feedback:
            compact_feedback.append({
                "id": s.get("id"),
                "type": s.get("type"),
                "descriptor": s.get("descriptor"),
                "feedback": s.get("feedback"),
            })

        user_payload = {
            "current_user_description": current_desc,
            "element_feedback_sample": compact_feedback,
            "instruction": (
                "Return JSON ONLY in the shape {\"updated_list\": [ ... ]}. "
                "Consider both current_user_description and element_feedback_sample. "
                "If feedback suggests changes (e.g., struggles with small text, "
                "needs larger hit areas, prefers condensed content, needs captions, "
                "motion sensitivity, etc.), incorporate or refine accordingly."
                "Also consider the surronding context such as neighboring elements for the user description."
            ),
        }

        # Strict JSON mode using response_format
        resp = self.client.chat.completions.create(
            model=self.cfg.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
            ],
        )
        content = resp.choices[0].message.content

        try:
            data = json.loads(content)
        except Exception as e:
            raise RuntimeError(f"Model returned non-JSON content: {e}\nRaw:\n{content}") from e

        updated = data.get("updated_list", None)
        if not isinstance(updated, list) or not all(isinstance(s, str) for s in updated):
            raise RuntimeError(
                "Model JSON missing valid 'updated_list': list[str]. "
                f"Received: {json.dumps(data, ensure_ascii=False)}"
            )
        return updated

    # ---------- Utilities ----------
    @staticmethod
    def _dedupe_and_strip(items: List[str], casefold: bool = True) -> List[str]:
        seen = set()
        out = []
        for s in items:
            if not isinstance(s, str):
                continue
            t = s.strip()
            if not t:
                continue
            key = t.casefold() if casefold else t
            if key not in seen:
                seen.add(key)
                out.append(t)
        return out


def parse_args() -> UpdateConfig:
    p = argparse.ArgumentParser(description="Update init_profile.json user_description using element_dataset.json + GPT (strict).")
    p.add_argument("--init", default="QueryEnhancement/init_profile.json", type=Path, help="Path to init_profile.json")
    p.add_argument("--elements", default="element_dataset.json", type=Path, help="Path to element_dataset.json")
    p.add_argument("--model", default="gpt-5", help="Model name (default: gpt-5)")
    p.add_argument("--dry-run", action="store_true", help="Print updated_list without writing file")
    args = p.parse_args()

    return UpdateConfig(
        init_profile_path=args.init,
        elements_path=args.elements,
        model=args.model,
        dry_run=args.dry_run,
    )


def main():
    cfg = parse_args()
    updater = UpdateInitProfile(cfg)
    updated = updater.update_user_description()
    print(json.dumps({"updated_list": updated}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
