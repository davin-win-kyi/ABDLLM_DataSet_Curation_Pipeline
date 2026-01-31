# WCAG RAG → Issues → Injection Pipeline

This repository contains a modular, end-to-end pipeline for **WCAG accessibility analysis and remediation**, combining:

- Element extraction from source files
- Thresholded RAG + LLM reranking (LlamaIndex + ChromaDB)
- Heuristic WCAG issue detection
- Candidate JavaScript injection generation
- Human-in-the-loop review before producing a final remediation JSON

The system is designed to be **inspectable, auditable, and extensible**, with stable element IDs and explicit intermediate artifacts at each stage.

---

## High-Level Flow

```
Input File
   ↓
[RAG_Components.py]
   - Extract elements
   - Assign stable UUIDs
   - Attach RAG context per element
   ↓
[Get_WCAG_Errors.py]
   - Detect WCAG issues per element
   - Attach supporting RAG evidence
   ↓
[Get_injection_Scripts.py]
   - Generate candidate injection scripts
   - Bundle scripts + context into JSON
   ↓
[Injection.py]
   - Human review (yes/no per script)
   ↓
Final JSON (approved injections)
```

---

## Repository Structure

```
.
├── rag_tool.py
├── RAG_Components.py
├── Get_WCAG_Errors.py
├── Get_injection_Scripts.py
├── Injection.py
├── main.py
├── init_profile.json
├── wcag_chroma/            
└── outputs/                
```

---

## File Overview

### `rag_tool.py`
Thresholded RAG + reranking helper built on **LlamaIndex + ChromaDB**.

Key features:
- Dense cosine similarity retrieval with a configurable cutoff
- “No good docs → return nothing” behavior
- LLM-based reranking (`LLMRerank`)
- Supports both OpenAI and Google Gemini rerankers
- Works with:
  - Local ChromaDB collections (`from_chroma`)
  - In-memory text lists (`from_texts`)

Primary class:
- `ThresholdedRAGReranker`

Primary method:
- `query(query_str) -> List[{text, score, metadata, embedding}]`

Also includes:
- `build_prompt_from_profile(profile_json)` for building user-context queries.

---

### `RAG_Components.py`
Handles **element extraction and RAG enrichment**.

Responsibilities:
- Extract elements from source files (currently line-based)
- Assign **stable UUIDv5 IDs** derived from normalized content
- Build a single `ThresholdedRAGReranker`
- Query WCAG documents once per element
- Attach:
  - `rag_query`
  - `rag_hits` (top WCAG chunks + scores)

Output artifact:
- `rag_elements.json`

---

### `Get_WCAG_Errors.py`
Runs **heuristic WCAG checks** over extracted elements.

Current checks include:
- Images missing `alt` text (WCAG 1.1.1)
- Inputs missing accessible labels (WCAG 1.3.1)
- Buttons missing accessible names (WCAG 4.1.2)

Each issue includes:
- Rule ID
- Severity
- Evidence snippet
- Supporting RAG excerpts

Output artifact:
- `wcag_issues.json`

---

### `Get_injection_Scripts.py`
Generates **candidate JavaScript injection scripts** from detected issues.

Responsibilities:
- Create one candidate per element + issue
- Attach:
  - Proposed injection script
  - Original element content
  - Supporting RAG evidence

⚠️ Current scripts are **broad/global** (e.g., patch all `img:not([alt])`).
Future work should generate **selector-targeted** injections.

Output artifact:
- `injection_candidates.json`

---

### `Injection.py`
Human-in-the-loop **CLI reviewer**.

For each candidate:
- Displays issue details
- Shows element snippet
- Shows supporting RAG context
- Shows proposed injection script
- Prompts `y/n` for inclusion

Produces:
- `final_injections.json` containing only approved injections

---

### `main.py`
Pipeline orchestrator.

Execution order:
1. Extract elements + attach RAG context
2. Detect WCAG issues
3. Generate injection candidates
4. Optionally review candidates
5. Save final output

---

## Setup

### 1. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
```

---

### 2. Install Dependencies

```bash
pip install chromadb python-dotenv \
  llama-index \
  llama-index-vector-stores-chroma \
  llama-index-embeddings-huggingface \
  llama-index-llms-openai \
  llama-index-llms-google-genai
```

---

### 3. Environment Variables

Create a `.env` file or export variables.

```bash
OPENAI_API_KEY=...
GOOGLE_API_KEY=...
```

---

## Running the Pipeline

```bash
python main.py --input path/to/file.html
```

Outputs are written to `./outputs/`.

---

## Design Philosophy

- Explicit intermediate artifacts
- Stable IDs for reproducibility
- RAG as supporting evidence, not blind authority
- Human review before mutating content
