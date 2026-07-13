---
title: Prompt Engineering (Lilian Weng)
source: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
author: Lilian Weng
date: 2023-03
type: concept
tags: [llm, prompt-engineering, chain-of-thought, few-shot, zero-shot, cot, tool-use, retrieval-augmented]
summary: LLM in-context prompting methods — zero-shot, few-shot, CoT, self-consistency, automatic prompt design, augmented LMs with retrieval/programming/external-APIs
related:
  - llm-agent
  - chain-of-thought
  - toolformer
  - react
---

# Prompt Engineering

> Source: [Lilian Weng — Prompt Engineering (Mar 2023)](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)

## Core Concept

**Prompt Engineering** (In-Context Prompting) = methods for communicating with LLM to steer behavior **without updating model weights**. Empirical science — effects vary widely across models.

## Zero-Shot vs Few-Shot

### Zero-Shot
Simply feed the task text to the model and ask for results.

```
Text: i'll bet the video game is a lot more fun than the film.
Sentiment:
```

### Few-Shot
Present a set of high-quality demonstrations (input + desired output). Model better understands intent → better performance, at the cost of more tokens and context length pressure.

**Key finding** (Zhao et al. 2021): three biases degrade few-shot performance:
1. **Majority label bias** — unbalanced label distribution
2. **Recency bias** — model repeats label at the end
3. **Common token bias** — model produces common tokens more often than rare tokens

### Few-Shot Example Selection
- k-NN clustering in embedding space (Liu et al. 2021)
- Graph-based diverse selection (Su et al. 2022)
- Contrastive learning for ICL sample selection (Rubin et al. 2022)
- Q-Learning (Zhang et al. 2022)
- Active learning via disagreement/entropy (Diao et al. 2023)

### Few-Shot Example Ordering
- Keep examples diverse, relevant, and **randomly ordered**
- Increasing model size does NOT reduce variance across permutations

## Instruction Prompting

Instead of few-shot demonstrations → describe the task instruction directly. (InstructGPT / RLHF fine-tuning makes models better follow instructions.)

Best practices:
- Be **specific and precise**
- Avoid "not do something" — specify what TO do
- Explain desired audience

## Self-Consistency Sampling

(Wang et al. 2022a) Sample multiple outputs with temperature > 0, then **majority vote**. For tasks with unit tests, verify correctness programmatically.

## Chain-of-Thought (CoT)

(Wei et al. 2022) Generate reasoning chains (short sentences describing step-by-step reasoning) before final answer. Most effective for:
- **Complicated reasoning tasks**
- **Large models (>50B parameters)**

### Two Types
1. **Few-shot CoT** — demonstrations with manually written reasoning chains
2. **Zero-shot CoT** — `"Let's think step by step"` then `"Therefore, the answer is"`

### Key Extensions
- **Self-consistency** — majority vote across multiple chains
- **STaR** — keep only chains leading to correct answers; fine-tune
- **Self-Ask** — iteratively prompt model to ask follow-up questions (answered by search)
- **ReAct** — interleaves CoT with Wikipedia/API retrieval
- **Tree of Thoughts** (Yao et al. 2023) — explore multiple reasoning branches at each step

## Automatic Prompt Design

### Gradient-Based
Treat prompts as trainable parameters, optimize via gradient descent on embedding space:
- AutoPrompt (Shin et al. 2020)
- Prefix-Tuning (Li & Liang 2021)
- P-tuning (Liu et al. 2021)
- Prompt-Tuning (Lester et al. 2021)

### APE (Automatic Prompt Engineer)
1. LLM generates instruction candidates from input-output pairs
2. Score via execution accuracy or log probability
3. Monte Carlo search to improve candidates

### Auto-CoT (Shum et al. 2023)
1. Augment: generate pseudo-chains with few-shot or zero-shot CoT
2. Prune: keep only chains where answer matches ground truth
3. Select: variance-reduced policy gradient over selected examples

## Augmented Language Models

### With Retrieval
- TF-IDF cosine similarity ranking of retrieved paragraphs
- RAG style: `p(ai|q) = Σ ptf-idf(pi|q) · pLM(ai|q,pi)`
- Noisy channel inference: `p(q|ai,pi) · pLM(ai|pi) / pLM(q|pi)`
- Product-of-Experts (PoE) combines all probabilities

### With Programming Language
- **PAL** (Program-aided LMs) / **PoT** (Program of Thoughts) — offload reasoning to Python interpreter
- Decouples complex computation from reasoning

### With External APIs
- **TALM** (Tool Augmented Language Models) — self-play bootstrapping of tool-use examples
- **Toolformer** (Schick et al. 2023) — self-supervised LM that learns to call external APIs:
  - Calculator, Q&A system, Search engine, Translation, Calendar
  - Format: `<API>tool_name(input)</API>` → `<API>tool_name(input) → result</API>`
  - Filter: only keep calls where adding results improves token prediction

## Key Papers

| Paper | Year | Contribution |
|-------|------|-------------|
| Wei et al. — CoT | 2022 | Chain-of-thought prompting |
| Wang et al. — Self-consistency | 2022 | Majority vote across CoT samples |
| Kojima et al. — Zero-shot CoT | 2022 | `"Let's think step by step"` |
| Yao et al. — ReAct | 2023 | Reasoning + Acting with external tools |
| Fu et al. — Complexity-based | 2023 | Prefer complex chains in majority vote |
| Zhou et al. — APE | 2022 | Automatic Prompt Engineer |
| Shum et al. — Auto-CoT | 2023 | Automatic chain-of-thought |

## Citation

```
@article{weng2023prompt,
  title   = "Prompt Engineering",
  author  = "Weng, Lilian",
  journal = "lilianweng.github.io",
  year    = 2023,
  month   = "Mar",
  url     = "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/"
}
```
