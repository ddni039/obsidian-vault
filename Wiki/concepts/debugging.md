---
title: Debugging
created: 2026-07-09
updated: 2026-07-09
type: concept
tags: [debugging, troubleshooting, root-cause, quality]
sources: [raw/articles/debugging-wikipedia-2026-07-09.md]
confidence: high
---

# Debugging

## Definition
Debugging is finding the root cause, workarounds, and possible fixes for bugs in software or engineering systems.

## Etymology
- **Bug** (defect): Thomas Edison used "little faults and difficulties" as "Bugs" in 1878
- **First computer bug**: 1947, Harvard Mark II — moth found stuck in relay, taped to log book
- **Debugging**: used in aeronautics before computing (J. Robert Oppenheimer, 1944)

## Core Debugging Techniques

### Wolf Fence Algorithm (Edward Gauss, 1982)
"There's one wolf in Alaska; how do you find it? First build a fence down the middle of the state, wait for the wolf to howl, determine which side. Repeat."

→ **Implemented in `git bisect`** — find which commit introduced a bug through binary search

### Delta Debugging
Automated test case simplification. Isolate the minimal input that triggers the failure.

### Record and Replay / Time Travel Debugging
- **rr** (Mozilla): execution recording for reversible debugging
- **Undo LiveRecorder**: step backward through program history
- **git bisect**: find regression commit

### Fault Localization
Automated identification of program elements (statements, methods, components) likely to contain faults. Modern ML approaches improving accuracy.

### Post-Mortem Debugging
Debugging after crash. Techniques:
- Examining log files
- Outputting call stack on crash
- Memory dump / core dump analysis

### Interactive Debugging
Debugger tools: step-by-step execution, breakpoints, watchpoints, catchpoints.

### Print Debugging / Tracing
Trace statements showing execution flow and data progression. "TRON" (Trace On) in BASIC.

## Key Insight: Zero-Defects Anti-Pattern
"An impact assessment can be made to determine if changes to remove an anomaly would be cost-effective... Basing decisions on acceptability of anomalies avoids a culture of a 'zero-defects' mandate, where people might be tempted to deny the existence of problems."

→ Not every "bug" must be fixed. Impact assessment before debugging.

## Anti-Pattern: Shotgun Debugging
Making largely undirected source code modifications to fix a bug — often creates more problems.

## Language-Specific Considerations
- **High-level (Java)**: Exception handling + type checking make bugs easier to spot
- **C/Assembly**: Memory corruption causes silent problems → need memory debugger tools
- **Static analysis tools** (e.g., `lint`): catch specific known problem patterns; false positives common

## Hermes-Specific Debugging Patterns

| Technique | Hermes Implementation |
|-----------|---------------------|
| Log analysis | `hermes logs --follow` |
| Post-mortem | `gateway.error.log`, `errors.log` |
| Record/replay | `session_search` for conversation history |
| Fault localization | `systematic-debugging` skill (4-phase root cause) |
| Regression hunting | `git bisect` |
| Test isolation | subprocess-per-test-file via `run_tests_parallel.py` |

## See Also
- [[software-testing-fundamentals]] — testing before debugging
- [[software-testing-maintenance]] — testing legacy code
- `systematic-debugging` skill — Hermes 4-phase debugging workflow
