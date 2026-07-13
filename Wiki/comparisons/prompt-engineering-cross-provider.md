---
title: Prompt Engineering Cross-Provider Comparison
created: 2026-07-11
updated: 2026-07-11
type: comparison
tags: [llm, prompt-engineering, research, meta]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md, raw/articles/anthropic-prompting-best-practices-2026.md, raw/articles/openai-prompt-engineering-2026.md]
confidence: high
---

# Prompt Engineering: Cross-Provider Comparison

## Overview

Three authoritative sources on LLM prompting, from different eras and providers:

| Source | Year | Provider | Focus |
|--------|------|----------|-------|
| [[chip-huyen]] | 2023 | Independent (Huyen) | Production LLMOps challenges, cost/latency, tool-use patterns |
| [[anthropic-prompt-engineering]] | 2026 | Anthropic (Claude) | Clarity, XML structure, role prompting, adaptive thinking, agentic safety |
| [[openai-prompt-engineering]] | 2026 | OpenAI (GPT-5) | Message roles, fewshot, RAG, reasoning vs GPT model selection |

## Dimension-by-Dimension Comparison

### 1. Philosophy: How to Think About Prompting

| Provider | Philosophy |
|---------|-----------|
| Chip Huyen | Prompting is **engineering**, not art. Apply MLOps rigor: version, eval, unit-test prompts. Ambiguity is the core problem. |
| Anthropic | Prompting is **communication**. Be clear and direct. "Show your prompt to a colleague" = golden rule. Model is a brilliant but new employee. |
| OpenAI | Prompting is **instruction hierarchy**. `developer` > `user` > `assistant` roles create clear authority levels. |

**Synthesis**: Chip focuses on *process* (engineering discipline), Anthropic focuses on *clarity* (communication), OpenAI focuses on *structure* (role hierarchy). All three agree on the fundamental problem: natural language is ambiguous.

### 2. Examples and Fewshot

| Provider | Approach |
|---------|---------|
| Chip Huyen | 4 examples max. Evaluate: (1) does LLM reproduce same labels? (2) does it overfit? Ask model to generate counter-examples. |
| Anthropic | **3–5 examples** — use `<example>` XML tags. Ensure **diverse** and **relevant** to actual use case. Can ask Claude to evaluate example quality. |
| OpenAI | 3–5 examples — structured with XML tags in `developer` message. Diverse range of possible inputs. |

**Synthesis**: All three converge on **3–5 examples**, XML-structured, diverse. Anthropic is most explicit about `<example>` tag format and diversity checking.

### 3. Role Prompting

| Provider | Approach |
|---------|----------|
| Chip Huyen | Role prompting = useful but not highlighted as a core technique. |
| Anthropic | **Single sentence in system prompt** = noticeable behavior change. Example: "You are a helpful coding assistant specializing in Python." |
| OpenAI | **Explicit role hierarchy**: `developer` (highest authority) > `user` > `assistant`. `instructions` param = high-priority behavior instructions. |

**Synthesis**: OpenAI has the most structured/architectural view of roles. Anthropic treats role as a lightweight communication tool. Chip treats it as one technique among many.

### 4. Output Format Control

| Provider | Approach |
|---------|----------|
| Chip Huyen | Explicit format instruction but "no guarantee" — this is a core production challenge. Set `temperature=0` for consistency. |
| Anthropic | Tell model **what to do** not what *not* to do. "Write in flowing prose paragraphs" > "Do not use markdown." Match prompt style to desired output style. |
| OpenAI | `structured_outputs` parameter guarantees JSON schema conformance. Prompt style matching influences output style. |

**Synthesis**: Anthropic gives the most nuanced guidance ("what to do vs. not to do"). OpenAI offers a deterministic solution (structured_outputs). Chip honestly acknowledges the guarantee problem.

### 5. Tool Use / Action Orientation

| Provider | Approach |
|---------|----------|
| Chip Huyen | **Agents = tasks + tools + control flows**. Tools: SQL executor, search, browser, bash, calculator. Control flows: sequential, parallel, if, for loop. ReAct pattern. |
| Anthropic | Be **explicit** about wanting implementation vs. suggestion. `<default_to_action>` = proactive; `<do_not_act_before_instructions>` = conservative. Parallel tool calling is default. |
| OpenAI | `functions.run` / tool calls with explicit examples. Explicit role = "software engineering agent" for coding tasks. Testing and validation required. |

**Synthesis**: All three agree explicit > implicit for tool use. Anthropic provides the most granular control (proactive vs. conservative). Chip provides the theoretical framework (control flows). OpenAI emphasizes testing/validation.

### 6. Thinking / Reasoning Control

| Provider | Approach |
|---------|----------|
| Chip Huyen | **Chain-of-Thought (CoT)** = prompt model to explain step-by-step. Tradeoff: increases latency + cost. Self-consistency = majority vote across multiple generations. |
| Anthropic | **Adaptive thinking** = dynamic, `effort` parameter controls depth. Thinking always on (Fable 5) or adaptive (Opus 4.7+). Overthinking control via targeted prompting. |
| OpenAI | **Reasoning models** (o-series) = internal CoT for complex tasks. **GPT models** = direct response for well-defined tasks. Senior vs. junior co-worker analogy. |

**Synthesis**: All three acknowledge reasoning/CoT but differ: Chip treats it as a prompt technique, Anthropic treats it as a model capability (`effort`), OpenAI treats it as a model *type* (reasoning vs. GPT). The field is moving from "prompt for thinking" → "model natively thinks."

### 7. Agentic Patterns

| Provider | Patterns |
|---------|---------|
| Chip Huyen | Sequential (NL→SQL→NL), parallel, if/conditional, for/loop. Composability gap (sub-tasks right but final answer wrong). |
| Anthropic | Long-horizon state tracking, context awareness, multi-window workflows, subagent orchestration. Safety/confirm before destructive actions. |
| OpenAI | Agent = persistent, decompose task, use TODO, confirm completion. Preambles for tool transparency. Subagent when parallel/isolated context needed. |

**Synthesis**: Anthropic has the most *mature* agentic guidance (subagent orchestration, safety rails, multi-window). OpenAI is similar but less granular. Chip's framework is older but still foundational.

### 8. Error Prevention / Hallucination

| Provider | Approach |
|---------|----------|
| Chip Huyen | Unit-test prompts with eval examples. Version control for prompts. |
| Anthropic | `<investigate_before_answering>`: "Never speculate about code you have not opened." Self-check prompt: "Verify against test criteria." |
| OpenAI | "Never hard-code values or create solutions that only work for specific test inputs." Focus on general algorithm, not test-passing. |

**Synthesis**: Anthropic is most specific (exact tag to use). OpenAI focuses on algorithmic correctness over test-passing. Chip focuses on process (versioning + eval).

### 9. Prompt Versioning / Production Discipline

| Provider | Approach |
|---------|----------|
| Chip Huyen | **Critical**: Git version control for prompts. Track performance per version. Unit-test with eval examples. |
| Anthropic | Not emphasized as core technique in the best practices guide. |
| OpenAI | **Deprecating prompt objects** (`v1/prompts` shut down Nov 2026). Store prompts in code for typed inputs, code review, tests, feature flags. |

**Synthesis**: Chip and OpenAI both push for code-based prompt management. OpenAI is actively forcing this with API deprecation. Anthropic focuses more on prompt *content* quality than lifecycle management.

### 10. Model Selection

| Provider | Guidance |
|---------|---------|
| Chip Huyen | GPT-3.5 vs. GPT-4 cost/latency tradeoff. Embedding models for search. No structured model taxonomy. |
| Anthropic | Claude Opus (complex tasks), Sonnet (balanced), Haiku (fast). Thinking models vs. non-thinking. Effort parameter. |
| OpenAI | **Reasoning models** (complex planning) vs. **GPT models** (precise, fast). gpt-5.6 as default. Size = capability trade-off. |

**Synthesis**: OpenAI has the clearest decision framework (reasoning vs. GPT). Anthropic offers a capability tier system (Opus > Sonnet > Haiku). Chip focuses on the cost/performance tradeoff at the API level.

## Key Insights

### Where All Three Agree
1. **Be explicit** — vague prompts → unpredictable outputs
2. **3–5 examples** for fewshot learning
3. **XML tags** for structuring complex prompts
4. **Don't rely on prompting alone for critical production systems** — eval, test, version
5. **Reasoning/thinking** is valuable for complex tasks

### Where They Diverge

| Dimension | Most Opinionated Source |
|-----------|----------------------|
| Role hierarchy | OpenAI (architectural) |
| Thinking mode | Anthropic (adaptive as native feature) |
| Production discipline | Chip (LLMOps lifecycle) |
| Output format guarantees | OpenAI (structured_outputs) |
| Agent safety rails | Anthropic (most granular) |
| Cost/latency framing | Chip (only source addressing economics) |

### Field Evolution: 2023 → 2026

| 2023 (Chip) | 2026 (Anthropic + OpenAI) |
|-------------|--------------------------|
| "Prompt engineer your way to reliability" | "Model natively supports reasoning + structured outputs" |
| "Agents = control flows + tools" | "Agents = native subagent orchestration + safety rails" |
| "temperature=0 for consistency" | "Model architecture handles this" |
| "LLMOps is new and chaotic" | "Structured tooling: effort params, prompt caching, structured outputs" |
| "Vector DBs are emerging" | "Vector DBs are mature; RAG is standard" |

## Practical Decision Guide

```
Need precise output format?
├─ Yes → OpenAI structured_outputs
└─ No → Continue

Need complex multi-step reasoning?
├─ Yes → Use reasoning model (OpenAI o-series or Anthropic Opus with adaptive thinking)
└─ No → Continue

Need production prompt lifecycle management?
├─ Yes → Chip's LLMOps + OpenAI code-based prompts
└─ No → Continue

Need granular action safety control?
├─ Yes → Anthropic <default_to_action> / <do_not_act_before_instructions>
└─ No → Continue

Use Anthropic or OpenAI or both?
├─ Anthropic Claude → anthropic-prompt-engineering + anthropic-adaptive-thinking
├─ OpenAI GPT → openai-prompt-engineering
└─ Both → understand reasoning model differences (see reasoning-models)
```

## See Also
- [[chip-huyen]] — Original LLMOps systematizer
- [[llmops]] — Production discipline across providers
- [[anthropic-prompt-engineering]] — Anthropic's full guidance
- [[openai-prompt-engineering]] — OpenAI's full guidance
- [[anthropic-adaptive-thinking]] — Anthropic's reasoning implementation
- [[reasoning-models]] — Cross-provider reasoning model comparison
- [[prompt-engineering-production]] — Chip's production-grade techniques
- [[llm-agents-tool-use]] — Chip's agent framework (foundational)
