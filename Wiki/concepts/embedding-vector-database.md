---
title: Embedding and Vector Database
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, tool, research]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md]
confidence: high
---

# Embedding and Vector Database

## Definition
Using LLMs to generate dense vector embeddings for text, then storing/retrieving them via vector databases for semantic search, recommendations, and "talk-to-your-data" applications.

## Embedding Models and Costs (as of April 2023)

| Model | Cost per 1K tokens | $1 buys |
|-------|-------------------|---------|
| text-embedding-ada-002 | $0.0004 | ~10K items |
| text-embedding-ada-002 | $0.0004 | $100 per 1M items |

Assuming average item = 250 tokens (≈187 words).

## Why Embeddings Are Different from Traditional ML Features
1. **One-time generation**: Embed each item once, not per query
2. **Real-time queries**: Generate embedding for user query on-the-fly
3. **Semantic search**: Retrieve by cosine similarity, not keyword match
4. **Composable**: Combine with traditional BM25 for hybrid search

## Vector Databases (2023 Landscape)
Chip's observation: *"If 2021 was the year of graph databases, 2023 is the year of vector databases."*

| Database | Type | Notes |
|----------|------|-------|
| **Chroma** | Open-source | Local-first, Pythonic, used by this wiki's ChromaDB |
| Pinecone | Managed | Cloud-native, production-grade |
| Qdrant | Open-source | Rust-based, high performance |
| Weaviate | Open-source | Graph + vector hybrid |
| Faiss | Meta (Meta) | In-memory, no persistence |
| Redis | Managed | Redis Stack with vector modules |
| Milvus | Open-source | CNCF project |
| ScaNN | Google | Research-grade, high recall |

## Embedding-Only Models vs. General LLMs
- **Embedding models** (text-embedding-ada-002): Specialized for vector generation, cheap, fast
- **General LLMs** (GPT-4): Can also embed, but overkill and expensive for pure retrieval

## SGPT (Muennighoff, 2022)
GPT-style embeddings that outperform DNN-trained dense embeddings on certain benchmarks. See [Muennighoff/sgpt](https://github.com/Muennighoff/sgpt).

## Relationship to Other Concepts
- [[llmops]] — Embeddings are a major cost/processing component of LLMOps
- [[talk-to-your-data]] — The canonical use case: embed documents → retrieve → generate
- [[mcp-model-context-protocol]] — MCP provides tool retrieval; vector DB provides knowledge retrieval

## See Also
- [[chip-huyen]] — Source for cost analysis and landscape survey
