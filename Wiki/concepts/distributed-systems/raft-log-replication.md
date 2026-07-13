---
title: "Raft Log Replication"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/raft-consensus-algorithm-2026-07-08.md]
confidence: high
---

## Summary
Leader takes client requests, appends to local log, replicates to majority, then applies.

## What
1. Client sends command to leader
2. Leader appends command to its local log
3. Leader sends AppendEntries RPCs to all followers in parallel
4. When entry is replicated to **majority** → entry is **committed**
5. Leader notifies clients of committed entries

## Log Compaction (Snapshotting)
Once logs grow large, the leader takes a snapshot of the current state, discards all prior log entries, and continues. This is how Raft manages long-running systems.

## Hermes Relevance
- [[hermes-hindsight]] could adopt log-structured memory: every session state change is a WAL entry
- Snapshotting maps to periodic memory checkpointing
- [[hermes-messaging-gateway]] message delivery could use a WAL + committed log pattern

## Related
- [[raft-leader-election]] — only the leader can accept client writes
- [[raft-safety]] — committed entries are never overwritten


## Source
- [[raw/papers/raft-consensus-algorithm-2026-07-08.md]]

## Related Concepts
