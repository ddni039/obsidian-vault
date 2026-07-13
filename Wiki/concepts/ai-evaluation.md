---
title: AI Evaluation Methodology
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [ai-engineering, evaluation, llm, metrics, ai-as-judge]
sources: [raw/articles/aie-book-chapter-summaries-2025.md, raw/articles/aie-book-resources-2025.md]
confidence: high
---

# AI Evaluation Methodology

## Overview
Foundation models are harder to evaluate than traditional ML models because their outputs are open-ended and probabilistic. Chip Huyen dedicates two chapters (Ch3 + Ch4) to evaluation — the most critical and under-invested area of AI engineering.

## Language Modeling Metrics

### Perplexity
Measures how surprised a model is by test data. Lower = better.
- Interpretation: If perplexity = 20, the model is as uncertain as if it had to choose uniformly among 20 options
- Used for: comparing models on the same benchmark, tracking training progress

### Cross-Entropy
Measures the average number of bits needed to encode each token. Related to perplexity:
```
perplexity = 2^(cross-entropy)
```

### Bits-per-Character / Bits-per-Byte
Alternative to perplexity, measuring compression efficiency of text.

## Three Evaluation Approaches

### 1. Exact Evaluation
**Objective, deterministic.** Used when there is a single correct answer.
- **Functional correctness**: pass/fail on code execution, math answers
- **Similarity scores**: BLEU, ROUGE (n-gram overlap), BERTScore (semantic similarity)
- **Embedding distance**: cosine similarity between response and reference embeddings

### 2. AI-as-a-Judge
**Subjective, model-dependent.** A stronger model evaluates a weaker model's outputs.
- Pros: scalable, captures nuance, handles open-ended tasks
- Cons: judge bias, position bias (favors first/last), verbosity bias
- Best practices: Use reference answers, compare pairs, iterate on judge prompts
- [[^1]](https://arxiv.org/abs/2306.05685) MT-Bench + Chatbot Arena

### 3. Comparative Evaluation
**Pairwise ranking.** Which of two models is better?
- Chess-style ELO ranking (used by Chatbot Arena)
- Challenge: expensive preference data collection
- Preference models: specialized AI judges trained to predict user preference

## Evaluation Pipeline Design (Ch4)

### Step 1: Evaluate All Components
Break the system into components and evaluate each:
- Retriever quality (recall, precision, MRR)
- Generator quality
- End-to-end quality

### Step 2: Create an Evaluation Guideline
Written document specifying:
- What "good" looks like for each criterion
- How to score (1-5 scale, binary, etc.)
- Edge cases and known failure modes

### Step 3: Define Methods and Data
- Real production data (best signal, but sensitive)
- Synthetic data (cheap, scalable, but may miss edge cases)
- Public benchmarks (useful for filtering, not for final selection)

## Key Insight: No Single Metric

> "It's impossible to capture the ability of a high-dimensional system using one- or few-dimensional scores." — *AIE* Ch4

Combine approaches:
- Exact eval + AI-as-a-Judge + human eval = most reliable
- Always use multiple complementary metrics

## Public Benchmarks: Caveats

- **Contamination risk**: benchmark data in training data
- **Leaderboard aggregation**: unclear how benchmarks are selected/weighted
- **Not application-specific**: benchmarks weed out bad models but don't find the best for your use case

→ Build a **private leaderboard** with application-specific test cases.

## Hallucination Detection

Hallucinations = model generating plausible but false/ungrounded information. Key causes:
- Probabilistic nature of sampling
- Knowledge cutoff (missing information)
- Conflicting knowledge in training data

Mitigation strategies (from *AIE*):
1. Retrieval-augmented generation (RAG) — ground outputs in external knowledge
2. Factual consistency scoring — compare generated claims against retrieved evidence
3. Uncertainty quantification — flag low-confidence generations

## See Also
- [[ai-engineering-framework]] — The framework this concept lives in
- [[prompt-engineering]] — Evaluation of prompt quality
- [[llm-agent]] — Evaluating agent systems (Ch6)
- [[embedding-vector-database]] — Retrieval quality metrics (MRR, Recall@k)
