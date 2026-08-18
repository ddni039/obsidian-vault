---
title: "Stream Processing"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [distributed-systems, concept]
sources: [raw/papers/designing-data-intensive-applications-2026-07-08.md]
confidence: high
---

## Summary
Processing unbounded data streams in real-time: Kafka, watermarks, stateful windows.

## What
Instead of batch processing finite datasets, stream processing operates on infinite event streams. Each event is processed as it arrives.

## Key Concepts
- **Watermark**: a timestamp that marks "all events before time T have arrived"
- **Window**: a time or count range over which to aggregate (tumbling, sliding, session)
- **State**: persistent memory within a stream processor (e.g., running totals)
- **Exactly-once semantics**: event is processed once even with failures (via WAL + idempotency)

## Frameworks
- Apache Kafka: distributed log as the streaming substrate
- Apache Flink: stateful stream processing with fault tolerance
- AWS Kinesis: managed version of similar ideas

## Hermes Relevance
- [[hermes-messaging-gateway]] is itself a stream processor: messages → gateway → delivery
- Session activity log is a stream; could use Kafka-style partitioning by session_id
- [[hermes-hindsight]] observation events could be processed as a stream

## Related
- [[data-replication]] — stream processing requires a replicated log (Kafka uses Raft-style replication)
- [[data-partitioning]] — streams are partitioned for parallelism


## Source
- [[raw/papers/designing-data-intensive-applications-2026-07-08.md]]

## Related Concepts
