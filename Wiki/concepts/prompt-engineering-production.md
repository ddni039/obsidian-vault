---
title: Prompt Engineering in Production
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [llm, tool, research]
sources: [raw/articles/chip-huyen-llm-engineering-2023.md]
confidence: high
---

# Prompt Engineering in Production

## Definition
Systematic techniques for making LLM outputs reliable, consistent, and cost-effective in production environments. Extends beyond "cool demo" prompting to engineering-grade prompt systems.

## Key Techniques

### Fewshot Learners
Provide examples in the prompt so the LLM generalizes to new inputs.
```
Given a text, give it a controversy score from 0 to 10.
Examples:
1 + 1 = 2 → Controversy score: 0
Starting April 15th, only verified accounts on Twitter will be eligible... → Controversy score: 5
```
**Evaluation checklist** (from Chip Huyen):
1. Does the LLM correctly output the same labels given the same examples in the prompt?
2. Does the LLM overfit to the fewshot examples? (Test on held-out examples)

### Chain-of-Thought (CoT)
Prompt the model to explain its reasoning step-by-step before giving the final answer.
- Paper: Wei et al. 2022 (arXiv:2201.11903)
- **Tradeoff**: Increases both latency and cost (more output tokens)

### Self-Consistency
- Generate many outputs for the same input
- Pick final output by majority vote (Wang et al. 2023, arXiv:2203.11171)
- OpenAI API: pass `n` parameter to generate multiple responses

### Prompt Optimization Strategies
1. Break one big prompt into smaller, simpler prompts → compose with control flows
2. Ask the model to give examples for which it would assign a certain label
3. Explicitly specify output format in the prompt (though no guarantee)

### Prompt Versioning
- Git version control for prompts
- Track performance per prompt version
- Treat prompts like code: code review, CI, regression tests

## Production Failure Modes

### Silent Failures
Code changes → compiler/runtime error (loud failure).  
Prompt changes → runs without error but gives wrong output (silent failure).

### Ambiguous Output Format
Downstream apps expect structured output (JSON, specific fields). LLMs don't guarantee format even when explicitly instructed.

### Inconsistent User Experience
temperature > 0 → same input → different output → users lose trust.  
**Fix**: Set `temperature = 0` (mostly solves consistency; doesn't solve format ambiguity).

## See Also
- [[llmops]] — The broader discipline
- [[chip-huyen]] — Author who systematized these techniques
- [[karpathy-think-before-coding]] — Similar "don't guess, verify" engineering ethos
