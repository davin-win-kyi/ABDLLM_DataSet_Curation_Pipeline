#!/usr/bin/env python3
"""
Thresholded RAG + reranking helper using LlamaIndex + ChromaDB.

Features:
- Uses cosine similarity with a similarity cutoff
  -> "no good docs, don't use anything" if nothing passes the threshold.
- Uses an LLM-based reranker (LLMRerank).
- Returns top-k results with text, score, metadata, and embedding.
- Two entry points:
    * from_chroma(...)  -> work with an existing local ChromaDB collection.
    * from_texts(...)   -> work with an in-memory list of strings.
- main() sets all parameters directly in code (no argparse / CLI flags).
- Can use either OpenAI GPT or Google Gemini (via Google GenAI) for reranking,
  controlled by a simple provider flag.
"""

from typing import List, Dict, Any, Optional, Literal

import chromadb

from llama_index.core import (
    VectorStoreIndex,
    Document,
    Settings,
    StorageContext,
)
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.postprocessor import (
    SimilarityPostprocessor,
    LLMRerank,
)
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.llms.google_genai import GoogleGenAI  # Gemini via Google GenAI

# Use this to load environment variables if needed (OPENAI_API_KEY, GOOGLE_API_KEY, etc.)
import os
from dotenv import load_dotenv

load_dotenv()

# read init_profile.json
import json


LLMProvider = Literal["openai", "gemini"]


def make_llm(provider: LLMProvider, model_name: str):
    """
    Factory to build an LLM instance for reranking.

    provider: "openai" -> OpenAI GPT
              "gemini" -> Google GenAI (Gemini models)
    """
    if provider == "openai":
        # Uses OPENAI_API_KEY from env by default
        return OpenAI(model=model_name)
    elif provider == "gemini":
        # Uses GOOGLE_API_KEY from env by default
        return GoogleGenAI(model=model_name)
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")


class ThresholdedRAGReranker:
    """
    RAG helper that can work with:
      - a local ChromaDB collection (e.g. 'wcag_docs'), OR
      - an in-memory list of strings.

    Pipeline:
        1) Retrieve with cosine similarity (dense embedding search).
        2) Drop nodes whose similarity < similarity_cutoff.
        3) Rerank remaining nodes via LLMRerank.
        4) Return up to final_top_k items with:
            - text
            - score
            - metadata
            - embedding (list[float])

    If no nodes pass the cutoff (or reranker returns nothing), returns [].
    """

    def __init__(
        self,
        index: VectorStoreIndex,
        embed_model: HuggingFaceEmbedding,
        llm,  # can be OpenAI or GoogleGenAI (or any LlamaIndex LLM)
        similarity_cutoff: float = 0.7,
        retrieve_top_k: int = 20,
        final_top_k: int = 5,
    ):
        self.index = index
        self.embed_model = embed_model
        self.llm = llm
        self.similarity_cutoff = similarity_cutoff
        self.retrieve_top_k = retrieve_top_k
        self.final_top_k = final_top_k

        # Set global defaults (optional but convenient)
        Settings.embed_model = embed_model
        Settings.llm = llm

        # Retriever: dense similarity search (cosine under the hood)
        self.retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=self.retrieve_top_k,
        )

        # Postprocessor 1: drop low-similarity nodes
        self.similarity_pp = SimilarityPostprocessor(
            similarity_cutoff=self.similarity_cutoff
        )

        # Postprocessor 2: LLM-based reranker (GPT or Gemini depending on llm)
        self.reranker = LLMRerank(
            top_n=self.final_top_k,
            llm=self.llm,
            choice_batch_size=5,
        )

    # ------------------------------------------------------------------
    # ctor 1: from LOCAL CHROMA DB (e.g. wcag_docs)
    # ------------------------------------------------------------------
    @classmethod
    def from_chroma(
        cls,
        persist_dir: str,
        collection_name: str = "wcag_docs",
        similarity_cutoff: float = 0.7,
        retrieve_top_k: int = 20,
        final_top_k: int = 5,
        embedding_model_name: str = "all-MiniLM-L6-v2",
        llm_model_name: str = "gpt-5",  # or "gemini-2.5-pro", etc.
        llm_provider: LLMProvider = "openai",  # "openai" or "gemini"
    ) -> "ThresholdedRAGReranker":
        """
        Connect to an existing local ChromaDB collection (e.g. 'wcag_docs').

        Args:
            persist_dir: path to Chroma's persistent directory (e.g. ./wcag_chroma).
            collection_name: Chroma collection name (e.g. 'wcag_docs').
            similarity_cutoff: cosine similarity cutoff in [0,1].
            retrieve_top_k: initial # of candidates to retrieve before reranking.
            final_top_k: final # returned after reranking.
            embedding_model_name: HF / SentenceTransformers model name
                                  (e.g. 'all-MiniLM-L6-v2').
            llm_model_name: model used by LLMRerank ("gpt-5", "gemini-2.5-pro", etc).
            llm_provider: "openai" or "gemini".
        """

        # Normalize HF model name (accept both "all-MiniLM-L6-v2" and
        # "sentence-transformers/all-MiniLM-L6-v2").
        if "/" not in embedding_model_name:
            hf_model_name = f"sentence-transformers/{embedding_model_name}"
        else:
            hf_model_name = embedding_model_name

        # 1) Embedding model (must match what you used when adding docs to Chroma)
        embed_model = HuggingFaceEmbedding(model_name=hf_model_name)

        # 2) LLM used by the reranker (GPT or Gemini depending on provider)
        llm = make_llm(llm_provider, llm_model_name)

        # 3) Tell LlamaIndex to use THESE modules globally before building the index
        Settings.embed_model = embed_model
        Settings.llm = llm

        # 4) Chroma client + collection
        chroma_client = chromadb.PersistentClient(path=persist_dir)
        collection = chroma_client.get_or_create_collection(collection_name)

        # 5) Wrap collection with LlamaIndex ChromaVectorStore
        vector_store = ChromaVectorStore(chroma_collection=collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # 6) Build a VectorStoreIndex on top of that vector store
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            storage_context=storage_context,
        )

        return cls(
            index=index,
            embed_model=embed_model,
            llm=llm,
            similarity_cutoff=similarity_cutoff,
            retrieve_top_k=retrieve_top_k,
            final_top_k=final_top_k,
        )

    # ------------------------------------------------------------------
    # ctor 2: from a LIST OF STRINGS (no Chroma)
    # ------------------------------------------------------------------
    @classmethod
    def from_texts(
        cls,
        texts: List[str],
        metadata_list: Optional[List[Dict[str, Any]]] = None,
        similarity_cutoff: float = 0.7,
        retrieve_top_k: int = 20,
        final_top_k: int = 5,
        embedding_model_name: str = "all-MiniLM-L6-v2",
        llm_model_name: str = "gpt-5.1-mini",
        llm_provider: LLMProvider = "openai",
    ) -> "ThresholdedRAGReranker":
        """
        Build an in-memory index from a list of strings.

        Args:
            texts: list of document strings.
            metadata_list: optional list of metadata dicts per text.
            llm_provider: "openai" or "gemini".
        """
        if metadata_list is None:
            metadata_list = [{} for _ in texts]

        if "/" not in embedding_model_name:
            hf_model_name = f"sentence-transformers/{embedding_model_name}"
        else:
            hf_model_name = embedding_model_name

        docs = [
            Document(text=t, metadata=m)
            for t, m in zip(texts, metadata_list)
        ]

        # 1) Embedding + LLM
        embed_model = HuggingFaceEmbedding(model_name=hf_model_name)
        llm = make_llm(llm_provider, llm_model_name)

        # 2) Use these modules for index construction
        Settings.embed_model = embed_model
        Settings.llm = llm

        # 3) Index using these settings
        index = VectorStoreIndex.from_documents(docs)

        return cls(
            index=index,
            embed_model=embed_model,
            llm=llm,
            similarity_cutoff=similarity_cutoff,
            retrieve_top_k=retrieve_top_k,
            final_top_k=final_top_k,
        )

    # ------------------------------------------------------------------
    # Common RAG method
    # ------------------------------------------------------------------
    def query(self, query_str: str) -> List[Dict[str, Any]]:
        """
        Run retrieval-only RAG:

        1) Retrieve top-N candidates by cosine similarity.
        2) Drop anything below similarity_cutoff.
        3) Rerank remaining nodes with LLMRerank.
        4) Return up to final_top_k items, each with:
           - text
           - score
           - metadata
           - embedding (list[float])

        Returns [] if:
          - no nodes pass the similarity cutoff, or
          - reranker returns nothing.
        """

        # Step 1: retrieve candidates (NodeWithScore objects)
        nodes = self.retriever.retrieve(query_str)

        # Step 2: similarity cutoff ("no good docs" filter)
        nodes = self.similarity_pp.postprocess_nodes(nodes)
        if not nodes:
            return []  # "no good docs → don't use anything"

        # Step 3: rerank with LLM (GPT or Gemini)
        nodes = self.reranker.postprocess_nodes(nodes, query_str=query_str)
        if not nodes:
            return []

        # Step 4: compute embeddings for each final node
        results: List[Dict[str, Any]] = []
        for nws in nodes:
            node = nws.node
            score = nws.score

            text = node.get_content()
            metadata = dict(node.metadata or {})

            # Embedding for this node's content (same model as Chroma expects)
            embedding = self.embed_model.get_text_embedding(text)

            results.append(
                {
                    "text": text,
                    "score": score,
                    "metadata": metadata,
                    "embedding": embedding,
                }
            )

        return results


def build_prompt_from_profile(profile: Dict[str, Any]) -> str:
    """
    Turn init_profile.json into a single query string for RAG.
    Expects:
    {
      "intial_profile": {
        "user_description": [...],
        ...
      }
    }
    """
    # NOTE: key is 'intial_profile' (no second 'i'), matching your JSON
    intial = profile.get("intial_profile", {})
    desc_list = intial.get("user_description", [])

    if isinstance(desc_list, list):
        desc_part = ", ".join(desc_list)
    else:
        desc_part = str(desc_list)

    # Simple query string; adjust wording however you like
    return f"User has the following accessibility needs: {desc_part}"


def main() -> List[str]:
    # ======= CONFIG =======
    PERSIST_DIR = "./wcag_chroma"       # Chroma DB directory
    COLLECTION_NAME = "wcag_docs"       # Chroma collection name
    EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

    # Choose your reranker LLM here:
    LLM_PROVIDER: LLMProvider = "openai"      # "openai" or "gemini"
    LLM_MODEL_NAME = "gpt-5"                  # or "gemini-2.5-pro", etc.

    SIMILARITY_CUTOFF = 0.3             # cosine sim threshold [0,1]
    FINAL_TOP_K = 10                    # final top-k after reranking
    RETRIEVE_TOP_K = max(FINAL_TOP_K * 3, 10)
    PROFILE_PATH = "init_profile.json"  # input JSON
    OUTPUT_PATH = "rag_output.json"     # output JSON
    # ======================

    # 1) Build RAG helper from local ChromaDB
    rag = ThresholdedRAGReranker.from_chroma(
        persist_dir=PERSIST_DIR,
        collection_name=COLLECTION_NAME,
        similarity_cutoff=SIMILARITY_CUTOFF,
        retrieve_top_k=RETRIEVE_TOP_K,
        final_top_k=FINAL_TOP_K,
        embedding_model_name=EMBEDDING_MODEL_NAME,
        llm_model_name=LLM_MODEL_NAME,
        llm_provider=LLM_PROVIDER,
    )

    # 2) Load profile JSON once
    with open(PROFILE_PATH, "r") as f:
        profile = json.load(f)

    # 3) Build user_description string from the JSON
    user_description = build_prompt_from_profile(profile)

    # 4) Make a single RAG call using user_description as the prompt
    results = rag.query(user_description)

    # 5) Collect TEXT of the top results (strings corresponding to top embeddings)
    top_texts: List[str] = [r["text"] for r in results] if results else []

    # 6) Build output JSON structure
    output_data = {
        **profile,  # keep everything that was in init_profile.json
        "user_description": user_description,
        "top_embeddings": top_texts,  # text of top chunks
    }

    # 7) Save to rag_output.json
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output_data, f, indent=2)

    # 8) Return the list of top strings so callers can use it
    return top_texts


if __name__ == "__main__":
    top_wcag_strings = main()
    # If you want to see them when run as a script:
    print(json.dumps(top_wcag_strings, indent=2))
