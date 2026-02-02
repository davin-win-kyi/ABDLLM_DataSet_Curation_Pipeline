#!/usr/bin/env python3
"""
Overview: Provided WCAG preferences from users,
index the WCAG failure techniques chosen by the user for dataset curation.
"""

from __future__ import annotations
import argparse
import json
import shutil
import re
from pathlib import Path
from typing import Dict, Any, Optional, Iterable, Set, List

# Regular expression to filter out failures only
WCAG_CODE_RE = re.compile(r"^(F\d+)", re.IGNORECASE)

NON_FUNCTIONAL_WCAG_FAILURES: Set[str] = {
    "F7", "F25", "F26", "F32", 
    # "F13", "F14", "F15",
    # "F22", "F23", "F24", "F25", "F26", "F30", "F31",
    # "F32", "F33", "F34",
    # "F43", "F46", "F48", "F49", "F50",
    # "F52", "F53", "F58", "F59",
}

FUNCTIONAL_WCAG_FAILURES: Set[str] = {
    "F10", "F12", "F16", "F19", "F20", "F21",
    "F40", "F42", "F54", "F55", "F56",
    "F63", "F65", "F66", "F67",
    "F69", "F70", "F73", "F75",
    "F78", "F79", "F80", "F84",
}


def extract_wcag_code(filename: str) -> Optional[str]:
    m = WCAG_CODE_RE.match(filename)
    return m.group(1).upper() if m else None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def code_sort_key(code: str) -> int:
    try:
        return int(code[1:])
    except Exception:
        return 10**9


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()

    ap.add_argument("--wcag_dir", type=str, required=True, help="Directory containing WCAG technique files")
    ap.add_argument("--out_dir", type=str, required=True, help="Output directory (e.g., out)")
    ap.add_argument(
        "--filter_mode",
        type=str,
        default="non_functional",
        choices=["non_functional", "functional", "both"],
        help="Which WCAG failure set to index",
    )
    # Hyperparameters
    ap.add_argument("--first_k_non_functional", type=int, default=0,
                    help="If >0, only include first K non-functional codes")
    ap.add_argument("--first_k_functional", type=int, default=0,
                    help="If >0, only include first K functional codes")

    return ap


def pick_allowed_codes(filter_mode: str,
                       first_k_non_functional: int,
                       first_k_functional: int) -> Set[str]:
    nf = sorted(NON_FUNCTIONAL_WCAG_FAILURES, key=code_sort_key)
    fn = sorted(FUNCTIONAL_WCAG_FAILURES, key=code_sort_key)

    if first_k_non_functional > 0:
        nf = nf[:first_k_non_functional]
    if first_k_functional > 0:
        fn = fn[:first_k_functional]

    if filter_mode == "non_functional":
        return set(nf)
    if filter_mode == "functional":
        return set(fn)
    return set(nf) | set(fn)


def main() -> None:
    args = build_arg_parser().parse_args()

    wcag_dir = Path(args.wcag_dir).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    out_rules_dir = out_dir / "wcag_common_failures"
    out_rules_dir.mkdir(parents=True, exist_ok=True)

    if not wcag_dir.exists():
        raise FileNotFoundError(f"WCAG directory not found: {wcag_dir}")

    allowed_codes = pick_allowed_codes(
        args.filter_mode,
        args.first_k_non_functional,
        args.first_k_functional,
    )

    rules: List[Dict[str, Any]] = []

    # Picking desired F WCAG files
    for p in sorted(wcag_dir.rglob("*")):
        if not p.is_file():
            continue

        wcag_code = extract_wcag_code(p.name)
        if not wcag_code:
            continue

        if wcag_code not in allowed_codes:
            continue

        # Copy file into curated folder
        index_wcag = out_rules_dir / p.name
        shutil.copy2(p, index_wcag)

        technique_id = index_wcag.stem
        technique_path = index_wcag.relative_to(Path.cwd()).as_posix()

        entry: Dict[str, Any] = {
            "rule_id": technique_id,
            "error_class": args.filter_mode,
            "file": p.name,
            "path": technique_path,
            "content": read_text(index_wcag),
        }
        rules.append(entry)

    index = {
        "wcag_dir": str(wcag_dir),
        "out_dir": str(out_dir),
        "output_rules_dir": out_rules_dir.relative_to(Path.cwd()).as_posix(),
        "filter_mode": args.filter_mode,
        "allowed_codes": sorted(list(allowed_codes), key=code_sort_key),
        "rule_count": len(rules),
        "rules": rules,
    }

    out_index = out_dir / "index_wcag_techniques.json"
    out_index.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"Wrote {len(rules)} rules -> {out_index}")


if __name__ == "__main__":
    main()
