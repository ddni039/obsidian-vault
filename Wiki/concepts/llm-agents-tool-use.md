---
title: LLM Agents and Tool Use
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [agent, llm, tool, research]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md]
confidence: high
---

# LLM Agents and Tool Use

## Definition
An **LLM Agent** = an LLM application that executes multiple tasks according to a **control flow**, where each task may leverage one or more **tools** (SQL executor, search, browser, bash, calculator, etc.).

Chip Huyen's framework from "Building LLM Applications" Part 2.

## Tool Examples
| Tool | Purpose |
|------|---------|
| SQL executor | Query structured databases |
| Search (Google/Bing API) | Real-time web information |
| Web browser | Fetch and parse web page content |
| Bash executor | Run shell commands |
| Calculator | Arithmetic for generated code |
| Third-party APIs | CRM, Slack, email, etc. |

**Tools vs. Plugins**: Same concept. Plugins = tools submitted to the OpenAI plugin store.

## Control Flows

### Sequential
Task B executes after Task A completes, because B depends on A's output.
```
NL → SQL query [LLM] → Execute [SQL executor] → NL response [LLM]
```

### Parallel
Tasks A and B execute simultaneously (independence).
- Update Aug 2024: Parallel function calling is now critical for many use cases.

### If / Conditional
Execute Task A or Task B based on input classification determined by LLM.
```
User input → [LLM: classify intent] → routing decision → relevant tool
```

### For Loop
Repeat a task until a condition is met.
```
[Fetch webpage] → [Extract links] → [For each link: fetch again] → until "sufficient information"
```

## ReAct Pattern (from Chip's Essay)
Reasoning + Action pattern. The LLM produces:
```
Thought: { reasoning }
Action: { tool_name }
Action Input: { tool_input }
Observation: { tool_output }
```
Then loops until the final answer.

## Control Flow with LLM-Decided Conditions
Even the *condition* of a control flow can be determined by prompting:
```
You have access to three tools: Search, SQL executor, Chat.
- Search when users want current events or products
- SQL executor when users want queryable data
- Chat when users want general information
```

## Testing Agents
Two failure modes (from Chip, referencing Press et al. 2022):

1. **Component failure**: One or more tasks fail individually
   - Control flow error: wrong tool chosen
   - Task produces incorrect results

2. **Composability gap**: All components work correctly but the overall solution is wrong
   - = fraction of compositional questions answered incorrectly even when sub-answers are correct

**Mitigation**: Unit test each component + integration test the full control flow. Define `(input, expected output)` pairs per task.

## Relationship to Other Concepts
- [[agentic-tool-use-pattern]] — Hermes's version of this pattern
- [[agentic-planning-pattern]] — Planning is a specific control flow pattern
- [[mcp-model-context-protocol]] — MCP is the *infrastructure* for implementing tool-use in agents
- [[anthropic-ai-agents-framework]] — Anthropic defines the same four core patterns (Tool Use, Reflection, Planning, Multi-Agent)
- [[talk-to-your-data]] — A canonical 3-task sequential agent: NL→SQL→NL

## See Also
- [[chip-huyen]] — Source author
- [[hermes-agent]] — Hermes implements tool-use via its skill system and messaging gateway
