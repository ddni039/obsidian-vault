---
title: "Agentic Multi-Agent Pattern"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai-agent, concept]
sources: [raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]
confidence: high
---

## Summary
Multiple agents coordinate to solve problems no single agent can handle alone.

## What
Two or more agents work together with explicit roles, communication protocols, and shared context. Used when:
- Tasks require diverse expertise (e.g., coding + design + review)
- Workload must be parallelized across independent sub-tasks
- Quality gates require separate agents for execution vs. verification

## Hermes Relevance
- The [[agency-multi-agent-architecture]] (Agency 232-agent) provides a reference model
- Hermes tri-role pipeline: C→B→H→E is a 4-phase single-agent workflow, not multi-agent
- [[codex-obsidian-integration]] uses Codex + Obsidian as a 2-agent collaboration
- [[hermes-learning-loop]] involves multiple agents: producer + auditor

## Related Patterns
- [[agentic-planning-pattern]] — multi-agent systems need orchestration layer
- [[agentic-reflection-pattern]] — each agent in the system performs individual reflection


## Source
- [[raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]]

## Related Concepts
