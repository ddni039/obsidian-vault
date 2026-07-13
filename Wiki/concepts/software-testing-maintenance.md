---
title: Software Testing and Maintenance
created: 2026-07-09
updated: 2026-07-09
type: concept
tags: [testing, maintenance, legacy-code, refactoring, quality, technical-debt]
sources: [raw/articles/software-testing-wikipedia-2026-07-09.md, raw/articles/debugging-wikipedia-2026-07-09.md]
confidence: medium
---

# Software Testing and Maintenance

## Core Problem
How do you safely change, test, and maintain software — especially code with little or no existing test coverage?

## Legacy Code Definition (Michael Feathers)
"Legacy code is code that we don't have tests for."

The problem isn't age — it's absence of tests. You can't safely refactor without a safety net.

## Key Strategies

### 1. Sensing and Separation
Before changing code, you must be able to **sense** what it's doing. Add logging, extract interfaces, introduce seams where behavior can be observed without modification.

### 2. Characterisation Tests
Write tests that capture the **current behavior** of code — even if that behavior is "wrong." This documents the system as-is and prevents regressions during refactoring.

### 3. Dependency Breaking Techniques
- **Expose Static Methods** — extract to make testable
- **Pull Up Dependency** — pass as parameter instead of calling directly
- **Subclass and Override** — mock behavior through inheritance
- **Adapt Parameter** — wrap external dependencies

### 4. Test-Drived Changes (TDD Applied to Legacy)
1. Write a failing test for the behavior you want to change
2. Make the change
3. Refactor
4. Green → Red → Refactor cycle

### 5. Impact Assessment Before Debugging
Not every bug must be fixed. From [[debugging]]:
"An impact assessment can be made to determine if changes to remove an anomaly would be cost-effective."

→ Evaluate: Is this safety-critical? Mission-critical? Will fixing it break more than it solves?

## Hermes Maintenance Patterns

### Test Isolation (Hermes Practice)
Hermes uses subprocess-per-test-file isolation (`run_tests_parallel.py`). Each test file runs in a fresh Python subprocess with:
- Temp HERMES_HOME
- Unset credential env vars
- TZ=UTC, LANG=C.UTF-8

This prevents cross-contamination between test files.

### No Change-Detector Tests
Hermes explicitly avoids tests that assert on expected-to-change values:
- ❌ `assert "gemini-2.5-pro" in _PROVIDER_MODELS["gemini"]`
- ❌ `assert len(_PROVIDER_MODELS["huggingface"]) == 8`
- ✅ `assert "gemini" in _PROVIDER_MODELS` — behavior contract
- ✅ `assert all(m.lower() in DEFAULT_CONTEXT_LENGTHS for m in catalog)` — invariant

### Systematic Debugging Skill
Hermes has a `systematic-debugging` skill (4-phase root cause analysis):
1. Understand the bug
2. Isolate to minimal reproducible case
3. Find root cause
4. Verify fix

### Maintenance SOP: `sop-design-maintenance-errors`
Skill that records SOP design errors and maintenance lessons — prevents recurrence.

## Key Books in This Domain

| Book | Author | Core Value for Hermes |
|------|--------|----------------------|
| Working Effectively with Legacy Code | Michael Feathers | Dependency breaking, characterisation tests |
| Debug It! | Paul Butcher | Reproduce → Isolate → Root Cause → Fix |
| The Pragmatic Programmer | Thomas/Hunt | Software craftsmanship, maintenance mindset |
| Software Testing and Analysis | Pezzè/Young | Test strategy taxonomy |
| xUnit Test Patterns | Gerard Meszaros | Test坏味道, refactoring patterns |

## See Also
- [[software-testing-fundamentals]] — testing fundamentals
- [[debugging]] — finding and fixing bugs
- [[hermes-skills-system]] — Hermes skill testing patterns
- `systematic-debugging` skill — Hermes 4-phase workflow
- `sop-design-maintenance-errors` skill — maintenance lesson capture
