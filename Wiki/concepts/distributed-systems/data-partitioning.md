---
title: "Data Partitioning"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/designing-data-intensive-applications-2026-07-08.md]
confidence: high
---

## Summary
Splitting data across multiple machines (sharding) for scalability.

## Why
When data exceeds one machine's capacity, partition it across multiple nodes.

## Strategies
- **Key-range partitioning**: contiguous key ranges per node. Risk of hot spots.
- **Hash partitioning**: hash(key) mod N. Even distribution but no range queries.
- **Composite**: consistent hashing with virtual nodes for rebalancing.

## Rebalancing
When adding/removing nodes: minimize data movement. Use consistent hashing or splitting rather than remapping all keys.

## Cross-partition Queries
Range queries spanning multiple partitions are expensive. Design access patterns around partition boundaries.

## Hermes Relevance
- [[hermes-hindsight]] knowledge graph could be partitioned by entity type
- Session data partitioning by session_id for parallelization
- [[hermes-skills-system]] skills could be partitioned by domain tag

## Related
- [[data-replication]] — each partition is typically replicated too
- [[stream-processing]] — stream partitions map to worker parallelism


## Source
- [[raw/papers/designing-data-intensive-applications-2026-07-08.md]]

## Related Concepts
