---
title: "Raft Leader Election"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/raft-consensus-algorithm-2026-07-08.md]
confidence: high
---

## Summary
Raft uses heartbeat-based leader election with term numbers for safety.

## What
Raft divides time into *terms* (numbered integers). Each term begins with an election; if a candidate wins, it becomes leader for that term. If no candidate wins, the term ends with no leader and a new election begins.

## Key Rules
- Servers start as **followers**
- Leader sends **heartbeats** to all followers; if follower receives no heartbeat for **election timeout** → becomes candidate
- Candidate votes for itself and requests votes from all other servers
- Server votes for first candidate that arrives (within its election timeout window)
- Candidate wins if it receives votes from a **majority** of servers

## Election Safety
A server can only win election if its log is at least as up-to-date as any majority of servers it asks for votes.

## Hermes Relevance
- [[hermes-messaging-gateway]] has no leader election → single point of failure
- If Hermes adopted Raft, the gateway could have a leader for cross-platform message ordering
- The tri-role pipeline's [[hermes-hindsight]] could use Raft-style consensus for memory writes

## Related
- [[raft-log-replication]] — leader handles all writes; replicates to followers
- [[raft-safety]] — safety guaranteed even with split-brain elections


## Source
- [[raw/papers/raft-consensus-algorithm-2026-07-08.md]]

## Related Concepts
