---
title: Anthropic Adaptive Thinking
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, anthropic, reasoning, research]
sources: [raw/articles/anthropic-prompting-best-practices-2026.md]
confidence: high
---

# Anthropic Adaptive Thinking

## Definition
Claude's thinking mode where the model dynamically decides *when* to think and *how much* reasoning to apply, calibrated by the `effort` parameter and query complexity. Introduced in Claude Opus 4.7 / Claude Fable 5.

Replaces the older `budget_tokens`-based extended thinking approach.

## API Usage

### Adaptive Thinking (Current)
```python
client.messages.create(
    model="claude-opus-4-8",
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # low | medium | high
    messages=[...]
)
```

### Legacy Extended Thinking (Deprecated on Opus 4.7+)
```python
# DEPRECATED - returns 400 error on Opus 4.7+
client.messages.create(
    model="claude-opus-4-7",
    thinking={"type": "enabled", "budget_tokens": 10000},
    ...
)
```

## Effort Parameter

Controls the depth of thinking:

| Effort | Use Case |
|--------|---------|
| `low` | Simple queries, direct answers |
| `medium` | Default for most tasks |
| `high` | Complex multi-step reasoning, agentic tasks |

On Fable 5 / Mythos 5: thinking is always on; effort controls *calibration* (not whether thinking occurs).

## When Thinking Kicks In

- **Fable 5 / Mythos 5**: Always thinks (always on)
- **Opus 4.7+**: Thinking off by default; `adaptive` mode enables it dynamically
- **Opus 4.6**: Thinking off by default; use `extended` for explicit thinking
- **Sonnet 4.5 Haiku 4.5**: Adaptive via `thinking: {type: "adaptive"}`

## Guiding Thinking Behavior

### Encourage Reflection After Tool Use
```
After receiving tool results, carefully reflect on their quality and determine optimal
next steps before proceeding. Use your thinking to plan and iterate based on this new
information, and then take the best next action.
```

### Reduce Excessive Thinking
```
Extended thinking adds latency and should only be used when it will meaningfully improve
answer quality. When in doubt, respond directly.
```

### Step-by-Step Reasoning (When Thinking Off)
Use `<thinking>` and `<answer>` tags for visible chain-of-thought:
```
<thinking>
Step 1: Understand the problem...
Step 2: Identify the approach...
</thinking>
<answer>
[final answer]
</answer>
```

## Multishot Examples with Thinking

Include `<thinking>` tags in fewshot examples to show Claude the desired reasoning pattern:
```
<example>
<user_query>...</user_query>
<thinking>...Claude's reasoning...</thinking>
<assistant_response>...</assistant_response>
</example>
```

## Self-Check Pattern

Append to prompts for coding/math:
```
Before you finish, verify your answer against [test criteria].
```

This reliably catches errors, especially for code generation.

## Migrating from Extended Thinking

1. Remove `thinking: {type: "enabled", budget_tokens: N}`
2. Add `thinking: {type: "adaptive"}`
3. Set `output_config: {"effort": "high|medium|low"}` for budget control
4. `budget_tokens` returns 400 error on Opus 4.7+, Fable 5, Mythos 5

## Relationship to Other Concepts
- [[reasoning-models]] — Adaptive thinking is Anthropic's implementation of reasoning model capability
- [[anthropic-prompt-engineering]] — Thinking is one section of the broader prompting guide
- [[llm-agents-tool-use]] — Thinking helps agents plan after tool calls

## See Also
- [[anthropic-prompt-engineering]] — Full context on thinking guidance
