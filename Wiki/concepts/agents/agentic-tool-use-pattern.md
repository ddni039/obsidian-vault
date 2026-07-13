---
title: "Agentic Tool Use Pattern"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai-agent, concept]
sources: [raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]
confidence: high
---

## Summary
Agents call external tools/APIs to extend capability beyond the LLM itself.

## What
Agents use tools (web search, code execution, file I/O, API calls) to interact with the real world. The LLM generates tool calls; tools return results that become context for the next LLM turn.

## Key Properties
- Tool definitions must be precise (name, description, parameter schema)
- Tool results must be faithfully represented to the LLM
- Error handling on tool failures is critical for robust agents

## Hermes Relevance
- Hermes uses [[mcp-model-context-protocol]] for tool orchestration
- The skill system is a declarative form of tool use: [[hermes-skills-system]]
- [[hermes-messaging-gateway]] is itself a "tool" that agents can invoke

## Related Patterns
- [[agentic-reflection-pattern]] — reflection decides *when* to call tools
- [[agentic-multiagent-pattern]] — coordination of tools across multiple agents


## Source
- [[raw/papers/anthropic-ai-agents-architecture-patterns-2026-07-08.md]]

## Related Concepts
