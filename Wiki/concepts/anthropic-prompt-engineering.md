---
title: Anthropic Prompt Engineering
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, prompt-engineering, anthropic, research]
sources: [raw/articles/anthropic-prompt-engineering-overview-2026.md, raw/articles/anthropic-prompting-best-practices-2026.md]
confidence: high
---

# Anthropic Prompt Engineering

## Definition
Anthropic's official prompt engineering guidance for Claude models. Covers general principles, tool use, thinking/reasoning, and agentic systems.

## Key Principles

### Be Clear and Direct
Claude responds well to explicit, specific instructions. Think of Claude as a brilliant but new employee who lacks context on your norms.

**Golden Rule**: Show your prompt to a colleague with minimal context on the task. If they'd be confused, Claude will be too.

### Add Context
Explaining *why* behind instructions helps Claude deliver more targeted responses. Claude can generalize from explanations.

### Use Examples Effectively
- **3–5 examples** for best results
- Examples should be: **relevant** (mirror actual use case), **diverse** (cover edge cases), **structured** (wrap in `<example>` XML tags)
- Ask Claude to evaluate examples for relevance/diversity or generate additional ones

### Structure with XML Tags
XML tags help Claude parse complex prompts unambiguously:
- `<instructions>`, `<context>`, `<input>` — separate content types
- `<document>` with `<document_content>` and `<source>` for multi-document tasks
- **Best practice**: Put long documents at the top of the prompt, queries at the end (up to 30% quality improvement)

### Give Claude a Role
Even a single sentence in the system prompt focuses behavior and tone.

## Output and Formatting

### What vs. What Not to Do
- **Prefer**: "Write in flowing prose paragraphs"
- **Avoid**: "Do not use markdown"
- Telling Claude *what to do* > *what not to do*

### Formatting Style Matching
The formatting style of your prompt influences output style. Removing markdown from prompt → reduces markdown in output.

### LaTeX
Claude's latest models default to LaTeX for math expressions. Add explicit instruction to get plain text:
```
Format your response in plain text only. Do not use LaTeX, MathJax, or any markup notation.
```

## Tool Use (Anthropic)

### Explicit Action Instructions
Claude Opus 4.6 may suggest changes when you want implementation. Be explicit:
```
"can you suggest some changes?" → sometimes just suggests, doesn't implement
```

### Proactive Action Prompt
```
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is
unclear, infer the most useful likely action and proceed, using tools to discover any
missing details instead of guessing.
</default_to_action>
```

### Conservative Action Prompt
```
<do_not_act_before_instructions>
Do not jump into implementation or change files unless clearly instructed to make changes.
When the user's intent is ambiguous, default to providing information, doing research,
and providing recommendations rather than taking action.
</do_not_act_before_instructions>
```

### Parallel Tool Calling
Claude runs independent tool calls in parallel. To maximize:
```
<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between the tool calls,
make all of the independent tool calls in parallel.
</use_parallel_tool_calls>
```

## Thinking and Reasoning

### Adaptive Thinking (Claude Opus 4.7+, Fable 5)
`thinking: {type: "adaptive"}` — Claude dynamically decides when/how much to think based on `effort` parameter and query complexity.

### Extended Thinking (older models)
`thinking: {type: "enabled", budget_tokens: 10000}` → deprecated on Opus 4.7+ and Fable 5.

### Overthinking Control
Claude Opus 4.6 does extensive upfront exploration at high `effort` settings. Control with:
- **Targeted instructions** instead of blanket defaults
- **Remove over-prompting**: older "If in doubt, use tool" → now causes overtriggering
- **Effort as fallback** if thinking still too aggressive

### Self-Check Prompt
```
Before you finish, verify your answer against [test criteria].
```

## Agentic Systems

### Long-Horizon State Tracking
Claude maintains orientation across extended sessions via incremental progress, context awareness, and external state tools.

### Context Awareness (Claude Sonnet 5, Haiku 4.5)
Claude tracks remaining token budget throughout conversation → manages context more effectively.

### Multi-Context Window Workflows
1. First context window: set up framework (write tests, create init scripts)
2. Future windows: iterate via structured TODO lists
3. Use structured test formats (e.g., `tests.json`)
4. Create setup scripts (`init.sh`) for graceful restarts
5. Claude 4.7+ can start fresh from filesystem effectively

### Subagent Orchestration
Claude Opus 4.6+ can natively recognize when tasks benefit from subagents. To prevent overuse:
```
Use subagents when tasks can run in parallel, require isolated context, or involve
independent workstreams. For simple tasks, sequential operations, or single-file edits,
work directly rather than delegating.
```

### Balancing Autonomy and Safety
```
Consider the reversibility and potential impact of your actions. For actions that are hard
to reverse or affect shared systems (deleting files, git push --force, posting externally),
ask the user before proceeding.
```

## Key Technique Summary
| Technique | When to Use |
|-----------|------------|
| Fewshot examples | Need format/tone/structure steering |
| XML tags | Complex multi-section prompts |
| Role prompting | Focused behavior/tone needed |
| Adaptive thinking | Complex multi-step reasoning |
| Parallel tool calling | Multiple independent tools |
| Self-check | Coding/math tasks |
| `<default_to_action>` | Want proactive Claude |

## See Also
- [[llm-agents-tool-use]] — Chip Huyen's older framework for agent tools/control flows
- [[anthropic-ai-agents-framework]] — Anthropic's official agent patterns (Reflection, Planning, Tool Use, Multi-Agent)
- [[prompt-engineering-production]] — Chip Huyen's production-grade prompt engineering
- [[chip-huyen]] — Source of LLMOps context
