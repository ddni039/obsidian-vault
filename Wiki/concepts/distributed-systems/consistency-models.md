---
title: "Consistency Models"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/designing-data-intensive-applications-2026-07-08.md]
confidence: high
---

## Summary
Trade-offs between consistency, availability, and partition tolerance in distributed systems.

## CAP Theorem (Brewer's Theorem)
Pick 2 of 3: **C**onsistency, **A**vailability, **P**artition tolerance. Since partitions will happen, the real trade-off is C vs A.

## Consistency Spectrum
Strongest → Weakest:
1. **Linearizability**: every operation appears instantaneous across all nodes
2. **Sequential consistency**: operations appear in some total order, respecting each node's program order
3. **Causal consistency**: causally related operations appear in order; unrelated can be concurrent
4. **Eventual consistency**: given no new updates, all replicas will eventually agree
5. **Read-your-writes**: client always sees its own previous writes (a specific form of consistency)

## Hermes Relevance
- [[hermes-messaging-gateway]] must guarantee at least read-your-writes for session continuity
- [[hermes-hindsight]] knowledge graph: eventual consistency is acceptable (knowledge grows, contradictions flagged)
- [[hermes-skills-system]]: skill installs must be strongly consistent (SSoT)

## Related
- [[data-replication]] — replication strategy determines the consistency model
- [[distributed-transactions]] — 2PC enables strong consistency across nodes


## Source
- [[raw/papers/designing-data-intensive-applications-2026-07-08.md]]

## Related Concepts
