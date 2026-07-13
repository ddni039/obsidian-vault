---
title: OpenAI Prompt Engineering Guide
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, prompt-engineering, openai, research]
sources: [raw/articles/openai-prompt-engineering-2026.md]
confidence: high
---

# OpenAI Prompt Engineering Guide

## Definition
OpenAI's official prompt engineering guidance for the OpenAI API (Responses API and Chat Completions API). Covers message roles, fewshot learning, context management, reasoning models, and agentic patterns.

## Message Roles and Instruction Authority

OpenAI models interpret instructions with different priority levels:

| Role | Authority | Use Case |
|------|-----------|----------|
| `developer` | Highest | System rules, business logic |
| `user` | Medium | End-user inputs, arguments |
| `assistant` | Generated | Model outputs |

**Analogy**: `developer` = function definition, `user` = function arguments.

The `instructions` API parameter = high-authority instructions that take priority over `input` prompts.

## Prompt Versioning in Code

> "OpenAI is deprecating reusable prompt objects. `v1/prompts` shuts down November 30, 2026."

Best practice: Store prompts in application code (not the API prompt objects) so you can use:
- Typed function arguments/schemas
- Code review
- Tests and evaluation checks
- Feature flags / staged rollouts

## Message Formatting: Markdown + XML

### Recommended Structure (in order)
1. **Identity** — purpose, communication style, high-level goals
2. **Instructions** — rules, constraints, tool-use guidance
3. **Examples** — input/output pairs demonstrating desired behavior
4. **Context** — proprietary data, reference material (best near the end)

### XML Tags
Wrap distinct content types for unambiguous parsing by the model:
```
<user_query>...</user_query>
<assistant_response>...</assistant_response>
```

## Fewshot Learning

Include 3–5 examples that are:
- **Relevant**: Mirror actual use case closely
- **Diverse**: Cover edge cases
- **Structured**: Wrap in XML tags

```
<product_review id="example-1">Great sound quality!</product_review>
<assistant_response id="example-1">Positive</assistant_response>
```

## Context and RAG

Include proprietary or external data to ground responses. Called **Retrieval-Augmented Generation (RAG)**.

Context window planning:
- Different models have different context limits (100K–1M tokens for GPT-4.1)
- Place frequently-reused content at the **beginning** of the prompt AND early in the JSON body (enables prompt caching)
- Put queries at the **end** for complex multi-document inputs

## Reasoning Models vs. GPT Models

### Reasoning Models
- Generate internal chain-of-thought → analyze complex, multi-step planning
- Slower and more expensive
- Work well with **high-level guidance** (trust them to work out details)
- Analogy: senior co-worker — give a goal, trust them

### GPT Models
- Fast, cost-efficient, highly intelligent
- Need **precise, explicit instructions** for best results
- Analogy: junior coworker — detailed instructions required

### Model Selection Default
`gpt-5.6` — strong default for general-purpose text generation.

## Agentic Tasks (GPT-5.6)

For agentic/long-running tasks:

### Planning and Persistence
```
Remember, you are an agent - please keep going until the user's query is completely
resolved. Decompose into sub-tasks and confirm each completed. Only terminate when
the problem is solved.
```

### Preambles for Transparency
```
Before you call a tool explain why you are calling it.
```

### Progress Tracking
Use a TODO tool/rubric to enforce structured planning and avoid missed steps.

## Coding Best Practices (GPT-5.6)

1. **Define agent role**: Frame as software engineering agent with well-defined responsibilities
2. **Explicit tool use examples**: Concrete `functions.run` invocation examples
3. **Testing and validation**: Instruct to test with unit tests, validate patches carefully
4. **Markdown standards**: Clean, semantically correct markdown output

## Frontend Engineering (GPT-5.6)

Recommended libraries:
- **Styling/UI**: Tailwind CSS, shadcn/ui, Radix Themes
- **Icons**: Lucide, Material Symbols, Heroicons
- **Animation**: Motion

Zero-to-one web apps work from a single detailed prompt.

## Prompt Caching

**Key optimization**: Keep content used repeatedly at the **top** of your prompt AND **early in the JSON request body** (Chat Completions / Responses API) → maximizes prompt caching savings.

## Structured Outputs

Request JSON-mode via `response_format` or `structured_outputs` parameter. Guarantees valid JSON conforming to a schema.

## Key Technique Summary
| Technique | When to Use |
|-----------|------------|
| `developer` role | System rules, tone, constraints |
| `instructions` param | High-priority behavior instructions |
| Fewshot examples | Format/tone/structure steering |
| XML formatting | Mixed instructions + context + examples |
| Reasoning models | Complex multi-step planning |
| GPT models | Precise, well-defined tasks |
| Prompt caching | Repeated base context |

## See Also
- [[prompt-engineering-production]] — Chip Huyen's production prompt engineering
- [[anthropic-prompt-engineering]] — Anthropic's complementary guidance
- [[llm-agents-tool-use]] — Tool-use + control flow framework
- [[finetuning-vs-prompting]] — When to fine-tune vs. prompt
