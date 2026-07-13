---
source_url: https://en.wikipedia.org/wiki/Debugging
ingested: 2026-07-09
---

# Debugging — Wikipedia

## Definition
In engineering, debugging is the process of finding the root cause, workarounds, and possible fixes for bugs.

For software, debugging tactics include:
- Interactive debugging
- Control flow analysis
- Log file analysis
- Application/system-level monitoring
- Memory dumps
- Profiling

## Etymology
- **Bug** (defect): dates back to at least 1878, Thomas Edison wrote "little faults and difficulties" as "Bugs"
- **First actual case**: 1947, Harvard Mark II — moth found stuck in relay
- **Debugging**: aeronautics term before computers (J. Robert Oppenheimer, 1944)

## Key Debugging Techniques

### Interactive Debugging
Debugger tools allow program's execution to be processed one step at a time. Breakpoints, watchpoints, catchpoints.

### Print Debugging / Tracing
Watching live or recorded trace statements. "TRON" (Trace On) in BASIC.

### Wolf Fence Algorithm (Edward Gauss, 1982)
"There's one wolf in Alaska; how do you find it? First build a fence down the middle of the state, wait for the wolf to howl, determine which side. Repeat."

→ Implemented as `git bisect`

### Record and Replay Debugging
Creating execution recording (e.g. Mozilla's `rr`) for reversible debugging.

### Time Travel Debugging
Stepping back in time through source code. (Undo LiveRecorder)

### Delta Debugging
Automating test case simplification.

### Saff Squeeze
Isolating failure within test using progressive inlining.

### Shotgun Debugging
Making largely undirected source code modifications — anti-pattern.

### Fault Localization
Automated technique of identifying program elements likely to contain faults. Machine learning improving localization accuracy.

## Key Insight: Zero-Defects Anti-Pattern
"An impact assessment can be made to determine if changes to remove an anomaly would be cost-effective... Basing decisions on acceptability of anomalies avoids a culture of a 'zero-defects' mandate, where people might be tempted to deny the existence of problems."

## Language-Specific Debugging
- **High-level languages** (Java): Exception handling + type checking make debugging easier
- **C/Assembly**: Memory corruption can cause silent problems; memory debugger tools needed

## Static Code Analysis
Tools (e.g. `lint`) look for known problems — data flow semantics, not just syntax. Can have false positives.

## For Hermes Context
- Log file analysis → Hermes `hermes logs` command
- Post-mortem debugging → `gateway.error.log` analysis
- Record/replay → session_search for conversation history
- Fault localization → systematic-debugging skill (4-phase root cause)
- Delta debugging → git bisect for regression hunting

## Source
https://en.wikipedia.org/wiki/Debugging
Published: 2002-06-10
