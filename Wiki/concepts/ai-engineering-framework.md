---
title: AI Engineering Framework
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [ai-engineering, framework, foundation-models, llm]
sources: [raw/articles/aie-book-toc-2025.md, raw/articles/aie-book-chapter-summaries-2025.md]
confidence: high
---

# AI Engineering Framework

## Overview
The discipline of adapting foundation models (LLMs and LMMs) to solve real-world problems. Defined by Chip Huyen in *AI Engineering* (O'Reilly, 2025) as the layer between Applications and Foundation Models.

## The Three-Layer AI Stack

```
┌─────────────────────┐
│   Applications      │  ← End users / Business logic
├─────────────────────┤
│  AI Engineering     │  ← Prompting, RAG, Agents, Finetuning, Eval
├─────────────────────┤
│ Foundation Models   │  ← OpenAI, Anthropic, Meta, Google, etc.
└─────────────────────┘
```

## The AI Engineering Framework (10-Chapter Structure)

Chip Huyen organizes AIE into three parts:

### Part 1: Evaluation (Ch3 + Ch4)
**Core question: How do I know if my application works?**
- Ch3 — Evaluation Methodology: perplexity, AI-as-a-Judge, comparative evaluation
- Ch4 — Evaluate AI Systems: criteria, model selection, evaluation pipeline design

### Part 2: Adaptation (Ch5 + Ch6 + Ch7)
**Core question: How do I make the model do what I want?**
- Ch5 — Prompt Engineering: in-context learning, best practices, defensive PE
- Ch6 — RAG and Agents: retrieval-augmented generation, agentic patterns
- Ch7 — Finetuning: PEFT, LoRA, QLoRA, model merging

### Part 3: Infrastructure (Ch8 + Ch9 + Ch10)
**Core question: How do I build and maintain the system?**
- Ch8 — Dataset Engineering: curation, synthesis, processing
- Ch9 — Inference Optimization: quantization, batching, parallelism
- Ch10 — Architecture and User Feedback: system design, feedback loops

## The 10 Key Questions Every AI Engineer Must Answer

1. Should I build this AI application?
2. How do I evaluate my application? Can I use AI to evaluate AI outputs?
3. What causes hallucinations? How do I detect and mitigate them?
4. What are the best practices for prompt engineering?
5. Why does RAG work? What are the strategies for doing RAG?
6. What's an agent? How do I build and evaluate an agent?
7. When to finetune a model? When not to finetune a model?
8. How much data do I need? How do I validate the quality of my data?
9. How do I make my model faster, cheaper, and secure?
10. How do I create a feedback loop to improve my application continually?

## Fundamental Insight: Probabilistic Nature

> "Working with AI models requires building your workflows around their probabilistic nature." — *AIE* Ch2

The probabilistic nature of LLMs is the **root cause of hallucinations and inconsistency**. Every technique in AI engineering — prompting, RAG, agents, finetuning — is a strategy for managing this uncertainty.

## Build vs Buy Framework

For each component, evaluate along 7 axes:
| Axis | Build | Buy |
|------|-------|-----|
| Data Privacy | Full control | Risk of exposure |
| Data Lineage | Complete | Dependent on provider |
| Performance | Tuned to needs | General-purpose |
| Functionality | Custom | Limited by API |
| Control | Full | Limited |
| Cost | CapEx (predictable) | OpEx (variable) |
| Maintenance | Own | Provider |

## The Adaptation Sequence

Never jump to the most complex solution. Chip's framework:

```
1. Start with prompting (Ch5) ← lowest cost, highest flexibility
   ↓ if insufficient
2. Try RAG (Ch6) ← add external knowledge
   ↓ if still insufficient
3. Consider finetuning (Ch7) ← highest commitment, most powerful
```

## Relationship to ML Engineering

|| | ML Engineering | AI Engineering |
|---|---|---|---|
| **Models** | Trained from scratch | Adapted via prompting |
| **Data** | Curated, structured | Found, unstructured |
| **Key skills** | Feature engineering | Prompt engineering |
| **Context** | Fixed at training | Variable at inference |
| **Output** | Deterministic | Probabilistic |

## Relationship to DMLS

AIE builds on [[designing-ml-systems-book]]'s foundations:
- **DMLS Ch2's four system requirements** (reliability/scalability/maintainability/adaptability) apply to all AI systems, including AIE
- AIE adds **probabilistic nature** as the fundamental challenge dimension not fully addressed by DMLS
- DMLS's data-centric philosophy → AIE's data engineering chapter (Ch8)

## See Also
- [[chip-huyen]] — Author of the framework
- [[prompt-engineering]] — Ch5
- [[llm-agent]] — Ch6 (Agents)
- [[talk-to-your-data]] — Ch6 (RAG)
- [[finetuning-vs-prompting]] — Ch7
- [[llmops]] — The surrounding operational discipline
