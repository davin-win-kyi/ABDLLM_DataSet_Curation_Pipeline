# RAG_Components.py
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any
from pathlib import Path
import uuid
import json

from rag_tool import ThresholdedRAGReranker, build_prompt_from_profile  # from your rag_tool.py


# Stable namespace so UUIDs stay consistent across runs/projects
_UUID_NAMESPACE = uuid.UUID("12345678-1234-5678-1234-567812345678")


@dataclass
class RagHit:
    text: str
    score: float
    metadata: Dict[str, Any]


@dataclass
class RagElement:
    id: str
    source_path: str
    kind: str                 # "line" | "file_block" (extend later)
    content: str
    start_line: Optional[int] = None
    end_line: Optional[int] = None

    # Attached RAG context for this element
    rag_query: Optional[str] = None
    rag_hits: Optional[List[RagHit]] = None


def content_uuid(text: str) -> str:
    """Stable ID: same content -> same UUID (UUIDv5)."""
    normalized = " ".join(text.strip().split())
    return str(uuid.uuid5(_UUID_NAMESPACE, normalized))


def extract_elements_from_text(
    text: str,
    source_path: str,
    *,
    mode: str = "line",
    min_len: int = 20,
) -> List[RagElement]:
    elements: List[RagElement] = []
    lines = text.splitlines()

    if mode == "line":
        for idx, line in enumerate(lines, start=1):
            if len(line.strip()) < min_len:
                continue
            eid = content_uuid(line)
            elements.append(
                RagElement(
                    id=eid,
                    source_path=source_path,
                    kind="line",
                    content=line,
                    start_line=idx,
                    end_line=idx,
                )
            )
    else:
        eid = content_uuid(text)
        elements.append(
            RagElement(
                id=eid,
                source_path=source_path,
                kind="file_block",
                content=text,
                start_line=1,
                end_line=len(lines),
            )
        )

    return elements


def _load_profile(profile_path: str) -> Dict[str, Any]:
    with open(profile_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _make_element_query(user_description: str, element_content: str) -> str:
    """
    Build a query string that includes the user's needs + the element snippet.
    You can tune this prompt later.
    """
    snippet = element_content.strip().replace("\n", " ")
    if len(snippet) > 500:
        snippet = snippet[:500] + "..."
    return (
        f"{user_description}\n\n"
        f"Given this UI/code element, what WCAG guidance applies and what fixes are recommended?\n"
        f"Element:\n{snippet}"
    )


def enrich_elements_with_rag(
    elements: List[RagElement],
    *,
    persist_dir: str = "./wcag_chroma",
    collection_name: str = "wcag_docs",
    embedding_model_name: str = "all-MiniLM-L6-v2",
    llm_provider: str = "openai",          # "openai" or "gemini"
    llm_model_name: str = "gpt-5",
    similarity_cutoff: float = 0.3,
    retrieve_top_k: int = 30,
    final_top_k: int = 10,
    profile_path: str = "init_profile.json",
) -> List[RagElement]:
    """
    Build ONE rag instance, then query per element.
    """
    profile = _load_profile(profile_path)
    user_description = build_prompt_from_profile(profile)

    rag = ThresholdedRAGReranker.from_chroma(
        persist_dir=persist_dir,
        collection_name=collection_name,
        similarity_cutoff=similarity_cutoff,
        retrieve_top_k=retrieve_top_k,
        final_top_k=final_top_k,
        embedding_model_name=embedding_model_name,
        llm_model_name=llm_model_name,
        llm_provider=llm_provider,  # type: ignore
    )

    for el in elements:
        q = _make_element_query(user_description, el.content)
        results = rag.query(q)  # list[{text, score, metadata, embedding}]
        el.rag_query = q
        el.rag_hits = [
            RagHit(
                text=r.get("text", ""),
                score=float(r.get("score") or 0.0),
                metadata=dict(r.get("metadata") or {}),
            )
            for r in (results or [])
        ]

    return elements


def build_rag_components(
    source_path: str,
    file_text: str,
    *,
    extract_mode: str = "line",
    rag_enabled: bool = True,
    rag_kwargs: Optional[Dict[str, Any]] = None,
) -> List[RagElement]:
    elements = extract_elements_from_text(file_text, source_path, mode=extract_mode)
    if rag_enabled:
        elements = enrich_elements_with_rag(elements, **(rag_kwargs or {}))
    return elements


def elements_to_dict(elements: List[RagElement]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for e in elements:
        d = asdict(e)
        # dataclasses in nested hits are already dictable, but ensure plain dicts
        if d.get("rag_hits") is not None:
            d["rag_hits"] = [asdict(h) for h in e.rag_hits or []]
        out.append(d)
    return out
