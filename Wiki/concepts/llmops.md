---
title: LLMOps
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, workflow, trend, research]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md]
confidence: high
---

# LLMOps

## Definition
LLMOps = **LLM Operations** — the discipline of making LLM applications production-ready. Coined/popularized by Chip Huyen's 2023 essay "Building LLM Applications for Production."

Equivalent to MLOps but specifically for prompting, inference, evaluation, and versioning of LLM-based systems rather than traditional trained models.

## Core Challenges (from Chip Huyen)

### 1. Ambiguity of Natural Languages
- **Silent failures**: prompt changes run without errors but produce different outputs
- **Ambiguous output format**: LLMs don't guarantee structured output even when explicitly instructed
- **Inconsistent UX**: temperature > 0 means same input → different output every time
- **Mitigation**: Apply engineering rigor; version + unit-test prompts like code

### 2. Cost and Latency
| Model | Input Cost | Output Cost |
|-------|-----------|-------------|
| GPT-4 (10k prompt + 200 out) | $0.06/1k | $0.12/1k → **$0.624/prediction** |
| GPT-3.5-turbo (4k+4k) | $0.0015/1k | $0.002/1k → **$0.004/prediction** |

DoorDash analogy: 10B predictions/day × $0.004 = **$40M/day** — prohibitively expensive at scale.
- Input tokens process in parallel (latency not proportional to input length)
- Output tokens generate sequentially (latency proportional to output length)
- GPT-3.5-turbo: 51 in + 1 out → ~500ms; 228 in + 26 out → ~1.5s

### 3. Prompt Versioning
Small prompt changes → large result changes. Need:
- Version control for prompts (git)
- Evaluation suites per prompt version
- Performance tracking over time

### 4. Backward/Forward Compatibility
- New model versions can break existing prompts
- No guarantee prompts optimized for GPT-3.5 work on GPT-4
- **Mitigation**: Unit-test all prompts with eval examples whenever switching models

### 5. Embeddings + Vector Databases
- text-embedding-ada-002: $0.0004/1k tokens → $1 per 10K items, $100 per 1M items
- 2023: "If 2021 was the year of graph databases, 2023 is the year of vector databases"
- Vector DBs: Pinecone, Qdrant, Weaviate, **Chroma**, Faiss, Redis, Milvus, ScaNN

## Relationship to Other Concepts
- [[prompt-engineering-production]] — LLMOps = engineering rigor applied to prompt engineering
- [[embedding-vector-database]] — The embeddings sub-discipline within LLMOps
- [[talk-to-your-data]] — The #1 enterprise LLMOps use case
- [[finetuning-vs-prompting]] — Cost/performance trade-off decision within LLMOps
- [[hermes-messaging-gateway]] — Hermes's multi-platform messaging is a form of LLMOps for agent communication

## See Also
- [[chip-huyen]] — Creator of the term and author of the seminal essay
- [[ai-engineering-framework]] — AIE book (2025) absorbed and structured the LLMOps framework; contains the "Simple → RAG → Finetuning" adaptation sequence
- [[mcp-model-context-protocol]] — Infrastructure for tool-use within LLMOps
