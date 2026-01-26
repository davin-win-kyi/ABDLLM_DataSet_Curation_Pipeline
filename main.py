# main.py
from __future__ import annotations

import argparse
import json
from pathlib import Path

from RAG_Components import build_rag_components, elements_to_dict
from Get_WCAG_Errors import get_wcag_errors
from Get_injection_Scripts import build_injection_candidates
from Injection import review_candidates, save_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the file to analyze (HTML/JSX/etc.)")
    parser.add_argument("--out_dir", default="outputs", help="Output directory")
    parser.add_argument("--extract_mode", default="line", choices=["line", "block"], help="Element extraction mode")
    parser.add_argument("--no_review", action="store_true", help="Skip human review and output all candidates")

    # RAG config (matches your rag_tool.py expectations)
    parser.add_argument("--persist_dir", default="./wcag_chroma")
    parser.add_argument("--collection_name", default="wcag_docs")
    parser.add_argument("--embedding_model_name", default="all-MiniLM-L6-v2")
    parser.add_argument("--llm_provider", default="openai", choices=["openai", "gemini"])
    parser.add_argument("--llm_model_name", default="gpt-5")
    parser.add_argument("--similarity_cutoff", type=float, default=0.3)
    parser.add_argument("--retrieve_top_k", type=int, default=30)
    parser.add_argument("--final_top_k", type=int, default=10)
    parser.add_argument("--profile_path", default="init_profile.json")

    args = parser.parse_args()

    in_path = Path(args.input)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    file_text = in_path.read_text(encoding="utf-8", errors="replace")

    rag_kwargs = {
        "persist_dir": args.persist_dir,
        "collection_name": args.collection_name,
        "embedding_model_name": args.embedding_model_name,
        "llm_provider": args.llm_provider,
        "llm_model_name": args.llm_model_name,
        "similarity_cutoff": args.similarity_cutoff,
        "retrieve_top_k": args.retrieve_top_k,
        "final_top_k": args.final_top_k,
        "profile_path": args.profile_path,
    }

    # 1) Extract + attach RAG hits (per element)
    rag_elements = build_rag_components(
        str(in_path),
        file_text,
        extract_mode=args.extract_mode,
        rag_enabled=True,
        rag_kwargs=rag_kwargs,
    )
    rag_elements_dict = elements_to_dict(rag_elements)
    (out_dir / "rag_elements.json").write_text(json.dumps(rag_elements_dict, indent=2), encoding="utf-8")

    # 2) WCAG issues (with RAG support attached)
    element_issues = get_wcag_errors(rag_elements_dict)
    (out_dir / "wcag_issues.json").write_text(json.dumps(element_issues, indent=2), encoding="utf-8")

    # 3) Candidate injection scripts
    candidates_json = build_injection_candidates(rag_elements_dict, element_issues)
    (out_dir / "injection_candidates.json").write_text(json.dumps(candidates_json, indent=2), encoding="utf-8")

    # 4) Review
    if args.no_review:
        final_json = {
            "metadata": {**candidates_json.get("metadata", {}), "num_accepted": len(candidates_json.get("candidates", []))},
            "accepted_injections": candidates_json.get("candidates", []),
        }
    else:
        final_json = review_candidates(candidates_json)

    # 5) Save final
    save_json(final_json, str(out_dir / "final_injections.json"))
    print(f"\nDone. Outputs written to: {out_dir.resolve()}")


if __name__ == "__main__":
    main()
