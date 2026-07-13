---
title: "Distributed Transactions"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/designing-data-intensive-applications-2026-07-08.md]
confidence: high
---

## Summary
ACID properties across multiple database nodes or services.

## ACID Properties
- **Atomicity**: all steps commit or all abort
- **Consistency**: invariants always true
- **Isolation**: concurrent transactions don't interfere
- **Durability**: committed writes survive failure

## 2PC (Two-Phase Commit)
- Phase 1 (Prepare): coordinator asks all participants to vote commit or abort
- Phase 2 (Commit): if all voted yes → coordinator sends commit; else sends abort
- **Problem**: coordinator failure can leave participants blocked

## Sagas (Alternative to 2PC)
Instead of atomic commit across services, each service publishes an event/action that the next service reacts to. Compensation (reverse action) on failure. No blocking.

## Hermes Relevance
- The tri-role pipeline C→B→H→H′→E is a saga pattern: each role's output is an event for the next role; compensation on failure
- [[hermes-hindsight]] knowledge graph writes could use saga for multi-entity updates
- [[hermes-messaging-gateway]] cross-platform delivery is essentially a saga

## Related
- [[raft-safety]] — Raft is a consensus protocol used inside distributed transactions
- [[consistency-models]] — isolation levels determine how transactions interact


## Source
- [[raw/papers/designing-data-intensive-applications-2026-07-08.md]]

## Related Concepts
