---
title: Reasoning Models
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, model, research]
sources: [raw/articles/openai-prompt-engineering-2026.md, raw/articles/anthropic-prompting-best-practices-2026.md]
confidence: high
---

# Reasoning Models

## Definition
LLM variants trained to generate an internal chain-of-thought before producing final outputs. They explicitly reason through problems step-by-step, enabling better performance on complex, multi-step tasks.

Distinguished from **base/GPT models** which respond more directly.

## OpenAI's Classification

| Model Type | Characteristics | Best For |
|-----------|----------------|---------|
| **Reasoning models** | Internal CoT, slower, more expensive | Complex multi-step planning, analysis |
| **GPT models** | Fast, cost-efficient, need explicit instructions | Well-defined tasks, precise outputs |

### Reasoning Model Examples (OpenAI)
- `o-series` models (o1, o3, etc.)

### GPT Model Examples (OpenAI)
- `gpt-5.6`, `gpt-4.1`, etc.

**Analogy** (OpenAI):
- Reasoning model = **senior co-worker** — give a goal, trust them to work out details
- GPT model = **junior co-worker** — needs precise instructions for best results

## Anthropic's Classification

| Model Type | Thinking Mode | Best For |
|-----------|--------------|---------|
| **Claude Opus 4.7+, Fable 5** | Adaptive thinking (always on) | Complex multi-step tool use, agentic loops |
| **Claude Opus 4.6** | Adaptive thinking | Complex reasoning, agentic coding |
| **Claude Sonnet 5, Haiku 4.5** | Context-aware adaptive thinking | Long-horizon sessions |
| **Older models** | Extended thinking (`budget_tokens`) | Legacy compatibility |

## Thinking Modes

### Adaptive Thinking (Claude Opus 4.7+, Fable 5)
```
thinking: {type: "adaptive"}
```
Claude dynamically decides *when* and *how much* to think, calibrated by:
- `effort` parameter (low/medium/high)
- Query complexity

On Fable 5 and Mythos 5: thinking is **always on**.

### Extended Thinking (Older Claude)
```
thinking: {type: "enabled", budget_tokens: 10000}
```
Claude generates visible reasoning tokens before final output. Deprecated on Opus 4.7+.

### Disabling Thinking
On Opus 4.6 and earlier, omit `thinking` parameter to turn it off. Claude responds directly on easy queries.

## Effort Parameter (Anthropic)

Controls thinking depth:
- `low` — minimal reasoning, fast response
- `medium` — balanced (default for most models)
- `high` — extensive reasoning, slower but more thorough

On Fable 5/Mythos 5: effort controls the *calibration* of thinking, not whether thinking happens.

## Chain-of-Thought (CoT)

### Explicit CoT (Manual)
Ask the model to think step-by-step:
```
Solve this problem: [problem]
Think through it step by step before giving your answer.
```
Use structured tags: `<thinking>` and `<answer>` to separate reasoning from final output.

### Implicit CoT (Built-in Reasoning Models)
Models generate internal chain-of-thought automatically — not visible in output but drives better reasoning.

## Self-Consistency (Multi-Path Reasoning)

Generate multiple reasoning paths for the same input → pick the most common final answer.
- Wang et al. 2023 (arXiv:2203.11171)
- OpenAI API: pass `n` parameter for multiple generations

## Overthinking Control

### Anthropic Guidance
Claude Opus 4.6 does extensive upfront exploration at high `effort`. If too thorough:
1. Replace blanket defaults with targeted instructions
2. Remove "If in doubt, use tool" prompting (causes overtriggering)
3. Lower `effort` setting

### Prompt to Constrain Reasoning
```
When deciding how to approach a problem, choose an approach and commit to it.
Avoid revisiting decisions unless new information directly contradicts your reasoning.
```

## When to Use Reasoning vs. GPT Models

| Scenario | Recommended Model Type |
|---------|----------------------|
| Complex multi-step planning | Reasoning model |
| Math / proofs / logic | Reasoning model |
| Well-defined, precise output needed | GPT model |
| High-volume, low-latency | GPT model |
| Simple classification / extraction | GPT model |
| Code generation (straightforward) | GPT model |
| Code generation (complex architecture) | Reasoning model |

## See Also
- [[anthropic-prompt-engineering]] — Adaptive thinking, effort parameter details
- [[openai-prompt-engineering]] — OpenAI reasoning model guidance
- [[prompt-engineering-production]] — Chain-of-thought as a production technique
