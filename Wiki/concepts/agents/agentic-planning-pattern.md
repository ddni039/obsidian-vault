---
title: "Agentic Planning Pattern"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai-agent, concept]
sources: [raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]
confidence: high
---

## Summary
Agents decompose complex goals into ordered sub-tasks and execute them sequentially.

## What
Given a complex, multi-step goal, the agent breaks it into a plan: an ordered sequence of sub-tasks. Each sub-task is executed; plan may be revised mid-flight based on results.

## Approaches
- **Hierarchical planning**: top-level goal → sub-goals → primitive actions
- **Linear planning**: flat sequence with preconditions and effects
- **Re-planning**: agent revises plan when a step fails or new info arrives

## Hermes Relevance
- [[hermes-skills-system]] encodes pre-built plans as skills (procedural memory)
- The tri-role pipeline C→B→H is itself a planning pattern: C (文謀) sets strategy, B (匠) defines execution plan
- Cron job system is mechanical planning with scheduled triggers

## Related Patterns
- [[agentic-reflection-pattern]] — reflection on partial results drives re-planning
- [[agentic-multiagent-pattern]] — multi-agent systems require coordinated cross-agent planning


## Source
- [[raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]]

## Related Concepts
