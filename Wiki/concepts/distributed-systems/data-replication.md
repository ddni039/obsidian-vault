---
title: "Data Replication"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/designing-data-intensive-applications-2026-07-08.md]
confidence: high
---

## Summary
Keeping the same data on multiple machines to survive failures.

## Why
Single node failure should not lose data or stop service. Replication provides fault tolerance.

## Strategies
| Strategy | Consistency | Write availability | Latency |
|----------|-------------|-------------------|---------|
| Single-leader | Strong (from leader) | Degraded if leader down | Low for reads |
| Multi-leader | Eventual | High (any leader) | Higher (conflict resolution) |
| Leaderless | Eventual | Highest | Highest |

## Conflict Resolution (Multi-leader / Leaderless)
- **Last-write-wins (LWW)**: timestamp-based, loses writes
- **CRDTs**: data structures that merge automatically (e.g., sets, counters)
- **Application-level**: prompt user or apply business rules

## Hermes Relevance
- [[hermes-messaging-gateway]] currently single-leader (gateway = sole broker)
- [[hermes-hindsight]] knowledge graph could use CRDTs for conflict-free concurrent writes
- [[hermes-learning-loop]] session history could be multi-replicated

## Related
- [[consistency-models]] — replication always involves a consistency model
- [[distributed-transactions]] — 2PC/3PC provides atomic replication


## Source
- [[raw/papers/designing-data-intensive-applications-2026-07-08.md]]

## Related Concepts
