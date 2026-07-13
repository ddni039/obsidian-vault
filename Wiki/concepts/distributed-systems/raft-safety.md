---
title: "Raft Safety"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/raft-consensus-algorithm-2026-07-08.md]
confidence: high
---

## Summary
Raft guarantees state machine safety: if a server applies an entry, no other server applies a different entry for the same index.

## Safety Property
If a leader has decided that a log entry is committed, that entry is present in the logs of all servers that could become future leaders.

## Election Restriction
A voter denies its vote if its own log is *more up-to-date* than the candidate's log. "More up-to-date" = higher last term or same last term with longer log.

## Implications
- Committed entries are never rolled back
- No two leaders can exist for the same term (majority vote prevents split-brain)
- Logs are eventually consistent across all servers

## Hermes Relevance
- Critical for [[hermes-messaging-gateway]] if made distributed: message ordering across instances
- [[hermes-hindsight]] knowledge graph writes need similar safety to avoid contradictory facts
- [[hermes-skills-system]] skill updates need atomic commit guarantees

## Related
- [[raft-leader-election]] — election safety is the foundation
- [[distributed-transactions]] — Raft is itself a distributed transaction protocol


## Source
- [[raw/papers/raft-consensus-algorithm-2026-07-08.md]]

## Related Concepts
