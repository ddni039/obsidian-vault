---
title: Talk-to-Your-Data
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, workflow, research]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md]
confidence: high
---

# Talk-to-Your-Data

## Definition
Enterprise application pattern where users query internal databases, documents, and policies using natural language. The LLM translates NL → query language, executes, then translates results → NL response.

**Chip Huyen's observation**: "The most popular enterprise application (so far) as of April 2023."

## Canonical 4-Step Pipeline

```
1. Organize data → Database
   (SQL DB, graph DB, vector DB, or text DB)

2. NL Input → Query Language [LLM]
   (SQL, SPARQL, ANN query, or search query)

3. Execute query → Results [Database]

4. Results → Natural Language [LLM]
```

## Example: Talk-to-Database
User asks: *"How many unique merchants are in Phoenix and what are their names?"*

Pipeline:
1. LLM converts NL → SQL: `SELECT DISTINCT merchant_name FROM transactions WHERE city = 'Phoenix'`
2. SQL executor runs query
3. LLM converts results → natural language response

## Vertical Applications
| Vertical | Data Type | Example |
|----------|-----------|---------|
| Legal | Contracts | "Which contracts have auto-renewal clauses?" |
| HR / Resume | Job applications | "Find candidates with 5+ years ML experience" |
| Financial | Market data | "What was AAPL's revenue in Q3 2023?" |
| Customer Support | FAQs, policies | "Can I return an item after 30 days?" |
| Codebase | GitHub, Jira | "Find all bugs closed last sprint" |

## Knowledge Base Approaches

### Vector Database (Semantic Search)
1. Embed all documents with `text-embedding-ada-002`
2. Store in Chroma/Pinecone/Qdrant/Weaviate
3. Retrieve top-k chunks by cosine similarity to user query
4. Inject retrieved chunks into LLM prompt → generate answer

### Talk-to-Your-Data + RAG
Retrieval-Augmented Generation: Retrieve relevant documents → feed as context → LLM answers.

OpenAI tutorial: [chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin)

## Defensibility Concern (Chip's Warning)
> "I've seen startups building applications to let users query Google Drive or Notion in NL... it feels like a feature Google Drive or Notion can implement in a week."

Long-term moat requires: proprietary data, domain-specific fine-tuning, or superior UX.

## LLMs for Data Analysis (Limits)
- Small data (fits in prompt): LLMs can detect patterns
- Large data (>prompt context): Requires database query first, then LLM summarization
- Chip tried: input CSV data → GPT-3.5-turbo → detected some patterns
- Not production-ready for large datasets without query step

## Relationship to Other Concepts
- [[embedding-vector-database]] — Vector DB is the retrieval layer
- [[llm-agents-tool-use]] — Talk-to-data is a 3-task sequential agent
- [[finetuning-vs-prompting]] — Domain-specific use cases may warrant fine-tuning
- [[mcp-model-context-protocol]] — MCP enables LLMs to connect to live data sources

## See Also
- [[chip-huyen]] — Source author who identified it as the top enterprise use case
- [[hermes-agent]] — Hermes's skill system and memory plugins are infrastructure for building such agents
