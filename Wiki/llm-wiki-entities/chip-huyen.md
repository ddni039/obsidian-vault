---
title: Chip Huyen
created: 2026-07-11
updated: 2026-07-11
uid: e-638ef6f3d7c5
type: entity
tags: [person, author, llm, mlops, ai-engineering]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md, raw/articles/aie-book-toc-2025.md, raw/articles/aie-book-chapter-summaries-2025.md]
confidence: high
---

# Chip Huyen

## Overview
Vietnamese-American author and ML/AI engineer. Known for two O'Reilly books that bookend the LLM era: *Designing Machine Learning Systems* (2022, traditional ML) and *AI Engineering* (2025, foundation model applications).

## Key Facts
| Fact | Detail |
|------|--------|
| *Designing ML Systems* | O'Reilly, 2022 — traditional ML systems (feature engineering, training, deployment) |
| *AI Engineering* | O'Reilly, 2025 — building applications with foundation models (prompt, RAG, agents, finetuning, inference) |
| Free essay | "Building LLM Applications for Production" (April 2023) — 130K+ chars, introduced term **LLMOps** |
| Previous affiliation | Snorkel AI |
| Current | Writing full-time |
| Languages | Vietnamese, English; book translated into 10+ languages |

## The Two Books Are Companion Volumes

| | *DMLS* (2022) | *AIE* (2025) |
|---|---|---|
| **Focus** | Traditional ML (tabular data, feature engineering, model training) | Foundation models (prompting, context, PEFT) |
| **Key techniques** | Annotation, feature eng, model selection | Prompt engineering, RAG, agents, finetuning |
| **Data** | Curated, structured | Found, unstructured, synthetic |
| **Overlap** | Some evaluation, data quality | Both self-contained and modular |

> "A real-world system often involves both traditional ML models and foundation models, so knowledge about working with both is often necessary." — *AIE* Ch1

## *AI Engineering* — Chapter Structure

*AIE* is organized as a framework for adapting foundation models to real-world problems:

| Part | Chapters | Core Question |
|------|----------|---------------|
| Evaluation | Ch3, Ch4 | How do I know if my application works? |
| Adaptation | Ch5, Ch6, Ch7 | How do I make the model do what I want? |
| Infrastructure | Ch8, Ch9, Ch10 | How do I build and maintain the system? |

**10 Key Questions the Book Answers:**
1. Should I build this AI application?
2. How do I evaluate my application?
3. What causes hallucinations? How do I detect and mitigate them?
4. Best practices for prompt engineering?
5. Why does RAG work? Strategies for RAG?
6. What's an agent? How do I build and evaluate one?
7. When to finetune? When not to?
8. How much data do I need?
9. How do I make my model faster, cheaper, and secure?
10. How do I create a feedback loop?

## Key Thematic Contributions

### 1. The Probabilistic Nature of AI (Ch2)
All AI model outputs are probabilistic — this is the **root cause of hallucinations and inconsistency**. The entire book is about building systematic workflows around this fundamental uncertainty.

### 2. The AI Engineering Stack (Ch1)
Three-layer stack: **Applications → Models → Infrastructure**. AI engineering sits between applications and models, focusing on adaptation rather than training.

### 3. Evaluation as the Foundation
- AI-as-a-Judge (Ch3): using models to evaluate other models' outputs
- Evaluation pipeline design (Ch4): 3-step process for systematic eval
- Comparative evaluation: pairwise ranking vs absolute scoring

### 4. RAG vs Agents (Ch6)
- RAG = retrieval as a tool; agents = full planning + tool use
- RAG can be seen as a "special case of agent where the retriever is a tool"
- Both address context window limitations; agents go further

### 5. Finetuning Decision Framework (Ch7)
Never finetune first. The sequence: **Simple prompting → RAG → Finetuning**. Finetuning is memory-intensive; PEFT (LoRA, QLoRA) makes it accessible.

### 6. Inference Optimization (Ch9)
- **TTFT** (Time to First Token) vs **TPOT** (Time Per Output Token)
- Key tradeoffs: latency vs throughput vs cost
- Most impactful: quantization, tensor parallelism, KV cache, attention optimization

### 7. Architecture as Feedback Loop (Ch10)
Application architecture is not static — it's a feedback loop with user feedback driving continuous model improvement (the **data flywheel**).

## Reception
- Luke Metz (co-creator of ChatGPT, ex-OpenAI): "Drawing on her deep expertise, *AI Engineering* is a comprehensive and holistic guide to building generative AI applications in production."
- swyx: "The definitive segue into AI Engineering from one of the greats of ML Engineering."
- Andrei Lopatenko (Director Search & AI, Neuron7): "Every AI engineer building real-world applications should read this book."

## Relationship to Other Entities
- [[hermes-agent]] — Hermes faces the same LLMOps/AIE challenges (context management, tool orchestration)
- [[anthropic-ai-agents-framework]] — Anthropic's agent patterns complement the AIE framework
- [[mcp-model-context-protocol]] — MCP is a concrete answer to the tool-use challenge in AIE Ch6
- [[llm-agent]] — AIE Ch6 provides the theoretical framework for tool-using agents
- [[prompt-engineering]] — AIE Ch5 is the definitive production-focused prompt engineering reference
- [[finetuning-vs-prompting]] — AIE Ch7 provides the definitive decision framework
- [[karpathy-think-before-coding]] — Both emphasize engineering rigor over demo-culture
- [[llmops]] — The discipline Chip named and systematized

## See Also
- [[llm-agent]] — Agents (Ch6)
- [[prompt-engineering-production]] — Production prompt engineering (Ch5)
- [[talk-to-your-data]] — RAG pattern (Ch6)
- [[finetuning-vs-prompting]] — When to finetune (Ch7)
- [[llmops]] — The operational discipline surrounding AI engineering
