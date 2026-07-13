---
title: "Agentic Reflection Pattern"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai-agent, concept]
sources: [raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]
confidence: high
---

## Summary
Agent critiques and improves its own outputs through a self-evaluation loop.

## What
The Reflection pattern enables an agent to examine its own generated outputs, identify gaps or errors, and regenerate improved responses — without external supervision.

## How It Works
1. Agent produces an initial output (code, text, plan)
2. A secondary review step evaluates output quality
3. If quality < threshold → regenerate with targeted feedback
4. Loop until quality meets criteria or max iterations reached

## Hermes Relevance
- Directly maps to the [[hermes-hindsight]] re-evaluation loop
- The tri-role pipeline (C→B→H→E) embodies reflection: E (御史) = explicit critique phase
- Memory re-writing uses similar self-critique to improve future outputs

## Related Patterns
- [[agentic-tool-use-pattern]] — reflection often triggers tool re-calls
- [[planning-pattern]] — reflection on partial plans improves next-step accuracy


## Source
- [[raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]]

## Related Concepts
