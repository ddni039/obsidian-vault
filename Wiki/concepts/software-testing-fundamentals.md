---
title: Software Testing Fundamentals
created: 2026-07-09
updated: 2026-07-09
type: concept
tags: [testing, quality, methodology, verification]
sources: [raw/articles/software-testing-wikipedia-2026-07-09.md]
confidence: high
---

# Software Testing Fundamentals

## Core Definition
Software testing checks whether software meets its intended objectives and satisfies expectations. It provides objective, independent information about quality and risk of failure.

**Fundamental limitation:** Testing cannot determine correctness for all scenarios. Cannot find all bugs. [[debugging]]

## The Oracle Problem
An *oracle* is the mechanism that tells us whether the software behaved correctly. Examples:
- Specifications and contracts
- Comparable products / past versions
- User expectations and relevant standards

## Test Pyramid
```
        /\
       /  \   ← E2E (few)
      /────\
     /      \  ← Integration (medium)
    /────────\
   /          \ ← Unit Tests (many)
```

Most tests at unit level, fewest at E2E.

## Static vs Dynamic Testing

| Type | What | Examples |
|------|------|---------|
| **Static** | Verification without execution | Reviews, walkthroughs, inspections, lint |
| **Dynamic** | Validation with execution | Unit tests, integration tests |
| **Passive** | Log/traces without interaction | Runtime verification, log mining |

## White-Box vs Black-Box vs Grey-Box

- **White-box**: Tests internal structure/code paths. Requires programming skill. Usually unit level.
- **Black-box**: Tests functionality without internal knowledge.
- **Grey-box**: Hybrid — some internal knowledge, functional focus.

## Exploratory Testing (Cem Kaner, 1984)
"Style of software testing that emphasizes the personal freedom and responsibility of the individual tester to continually optimize the quality of his/her work."

→ Simultaneous: learning + test design + test execution + result interpretation

## Key Principles

1. **Testing cannot prove absence of bugs** — only presence
2. **The test oracle problem** — how do we know the expected behavior?
3. **NIST 2002**: Software bugs cost U.S. economy $59.5B/year; 1/3 avoidable with better testing
4. **Combinatorics** — pairwise testing maximizes coverage with minimal tests

## Relevance to Hermes

- Hermes has 17k+ tests across ~900 files
- Test runner: `scripts/run_tests.sh` — CI-parity isolation
- Subprocess-per-test-file isolation prevents cross-contamination
- No change-detector tests — behavior contracts over snapshots
- See [[hermes-skills-system]] for skill testing patterns

## See Also
- [[debugging]] — finding and fixing bugs
- Legacy code testing — [[software-testing-maintenance]]
