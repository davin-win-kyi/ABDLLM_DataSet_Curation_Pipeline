#!/usr/bin/env python3
"""
Overview: this file is provided WCAG preferences from users
and will index the the WCAG failures chosen by the user for 
dataset curation. 
"""

from __future__ import annotations
import json
import shutil
import re
from pathlib import Path
from typing import Dict, Any, Optional

# wcag dataset curation configuration variables==============================
WCAG_DIR = "wcag_techniques"
OUT_DIR = "out"

"""
Potential WCAG filtering modes for indexing: 
- non functional 
- functional
- both
"""
WCAG_FILTER_MODE = "non_functional"

# Limits for WCAG dataset curation size
FIRST_K_FUNCTIONAL_CODES: Optional[int] = 5
FIRST_K_NON_FUNCTIONAL_CODES: Optional[int] = 5
# ===========================================================================


NON_FUNCTIONAL_WCAG_FAILURES = {
    "F1", "F3", "F4", "F7", "F8", "F13", "F14", "F15",
    "F22", "F23", "F24", "F25", "F26", "F30", "F31",
    "F32", "F33", "F34",
    "F43", "F46", "F48", "F49", "F50",
    "F52", "F53", "F58", "F59",
}

FUNCTIONAL_WCAG_FAILURES = {
    "F10", "F12", "F16", "F19", "F20", "F21",
    "F40", "F42", "F54", "F55", "F56",
    "F63", "F65", "F66", "F67",
    "F69", "F70", "F73", "F75",
    "F78", "F79", "F80", "F84",
}

# Regular expression to filter out failures only
WCAG_CODE_RE = re.compile(r"^(F\d+)", re.IGNORECASE)


def extract_wcag_content(filename: str) -> Optional[str]:
    # extract only faliure WCAG rules
    m = WCAG_CODE_RE.match(filename)
    return m.group(1).upper() if m else None


def read_text(path: Path) -> str:
    # extract text for indexing of WCAG failures
    return path.read_text(encoding="utf-8", errors="replace")

def code_sort_key(code: str) -> int:
    # sorting the indexing of the WCAG failures
    try:
        return int(code[1:])
    except Exception:
        return 10**9

def main() -> None:
    wcag_dir = Path(WCAG_DIR).expanduser().resolve()
    out_dir = Path(OUT_DIR).expanduser().resolve()
    out_rules_dir = out_dir / "wcag_common_failures"
    out_rules_dir.mkdir(parents=True, exist_ok=True)

    if not wcag_dir.exists():
        raise FileNotFoundError(f"WCAG directory not found: {wcag_dir}")

    rules: list[Dict[str, Any]] = []

    for p in sorted(wcag_dir.rglob("*")):
        if not p.is_file():
            continue

        wcag_content = extract_wcag_content(p.name)
        if wcag_content is None:
            continue

        # copying file contents
        index_wcag = out_rules_dir / p.name
        shutil.copy2(p, index_wcag)

        # Get the id
        technique_id = index_wcag.stem    

        # Technique path for indexing
        technique_path = index_wcag.relative_to(Path.cwd()).as_posix()

        entry: Dict[str, Any] = {
            "rule_id": technique_id,
            "error_class": WCAG_FILTER_MODE,
            "file": p.name,                      
            "path": technique_path,                            
            "content": read_text(index_wcag),
        }

        rules.append(entry)

    index = {
        "wcag_dir": WCAG_DIR,
        "out_dir": OUT_DIR,
        "output_rules_dir": "out/wcag_common_failures",
        "filter_mode": WCAG_FILTER_MODE,
        "rule_count": len(rules),
        "rules": rules,
    }

    out_index = out_dir / f"wcag_common_failures.json"
    out_index.write_text(json.dumps(index, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
