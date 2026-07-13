---
title: RAG and Agents
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [ai-engineering, rag, agents, llm, retrieval, tool-use]
sources: [raw/articles/aie-book-chapter-summaries-2025.md, raw/articles/aie-book-resources-2025.md]
confidence: high
---

# RAG and Agents

## Overview
Two complementary patterns for extending LLM capabilities beyond their built-in knowledge and context limitations. *AIE* Ch6 covers both, with the key insight that **RAG is a special case of agents where the retriever is a tool**.

## RAG — Retrieval-Augmented Generation

### Why RAG?
- Models have finite context windows and knowledge cutoffs
- RAG enables models to access external knowledge at inference time
- Also enables more efficient use of information (cheaper than fine-tuning)

### Two-Step Process
1. **Retrieve** relevant documents from external knowledge base
2. **Generate** response conditioned on retrieved context

### Retrieval Algorithms

| Type | Examples | Pros | Cons |
|------|----------|------|------|
| Term-based | BM25, Elasticsearch | Fast, interpretable, strong baseline | Can't handle synonyms, miss semantic matches |
| Embedding-based | Vector search (HNSW, FAISS, ScaNN) | Captures semantic similarity | Slower, requires vector DB, less interpretable |
| Hybrid | Combine both | Best of both worlds | More complex |

### Key Insight: Chunking Strategy Matters
How you split documents dramatically affects retrieval quality:
- Too small → loses context
- Too large → noise, exceeds context window
- Overlap → preserves cross-chunk relationships

### RAG Beyond Text
- Tables (structured data)
- Codebases (entire repository context)
- Multi-modal (images + text)

## Agents

### Definition
An agent = **planner** (model) + **tools** + **environment**. The model acts as the brain that:
1. Analyzes the given task
2. Considers different solutions
3. Picks the most promising one

### Components

**Tools** extend what the model can do:
- Web search, code execution, file operations, API calls
- Tool use exposes agents to security risks (prompt injection, etc.)

**Planning** enables multi-step reasoning:
- Task decomposition: break complex tasks into simpler subtasks
- Reflection: self-correction based on intermediate results
- Memory: track progress across long horizons

**Memory** manages information beyond context:
- Short-term: conversation history, scratchpad
- Long-term: external storage, retrieval

### Agent Failure Modes (AIE Ch6)
1. Tool selection errors — wrong tool for the task
2. Tool use errors — incorrect parameters or API calls
3. Planning failures — incorrect task decomposition
4. Hallucination in tool outputs
5. Cascading failures — small error compounds across steps

## RAG vs Agents vs Finetuning

| | RAG | Agents | Finetuning |
|---|---|---|---|
| **What it extends** | Knowledge | Capabilities | Behavior |
| **When to use** | Missing knowledge | Complex multi-step tasks | Specific style/format |
| **Data needed** | Document corpus | Tool definitions | Training dataset |
| **Cost** | Low (no training) | Medium | High (GPU training) |
| **Maintenance** | Vector DB | Tool definitions | Retraining loop |

> "Both RAG and agents are prompt-based methods — they influence the model's quality solely through inputs without modifying the model itself." — *AIE* Ch6

## Key References
- RAG: Lewis et al. (2020), Gao et al. (2023 survey)
- Agents: Chameleon (2023), Toolformer (Schick et al.), Generative Agents (Park et al.)
- Function calling: Berkeley Function Calling Leaderboard, Gorilla paper

## See Also
- [[ai-engineering-framework]] — The framework this fits into
- [[llm-agent]] — Broader LLM agent concept
- [[llm-agents-tool-use]] — Tool use for agents
- [[talk-to-your-data]] — RAG as enterprise use case
- [[mcp-model-context-protocol]] — Standardized tool definitions for agents
- [[embedding-vector-database]] — Vector search powering RAG
