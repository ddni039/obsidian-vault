---
title: "SQL Anti-Patterns"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/the-art-of-sql-2026-07-08.md]
confidence: high
---

## Summary
常見 SQL 反模式：黑暗法則、指標分散、更新失控。

## Faroult's "Dark Matters"
1. **Fear of NULL**: treating NULL as 0 or empty string; not using proper NULL semantics
2. **Fear of Counting**: over-using COUNT(*) when EXISTS or LIMIT 1 suffices
3. **Fear of Joining**: denormalizing to avoid joins (creates update anomalies)
4. **Fear of Proper Types**: storing dates as strings, numbers as VARCHAR

## Pointer Chasing (The Scourge of SQL)
Fetching one row, then looping to get related rows = N+1 query problem.
Fix: use JOIN or subquery to fetch the entire related set in one query.

## Update Anomalies from Denormalization
Same fact stored in multiple places → UPDATE must touch all copies → inconsistency risk.
Fix: normalize, use foreign keys, let the optimizer handle joins.

## Phantom Reads Across Transactions
Reading data that another transaction will roll back = wrong decisions.
Fix: use appropriate isolation levels (SERIALIZABLE for critical reads).

## The "Everything in One Query" Trap
Overly complex queries that no optimizer can efficiently plan.
Fix: break into CTEs or temp tables, index intermediate results.

## Hermes Relevance
- [[hermes-hindsight]] updates must avoid pointer chasing on entity edges
- [[hermes-messaging-gateway]] session state must avoid the same UPDATE anomaly pattern

## Related
- [[sql-strategic-writing]] — the corrective perspective
- [[sql-query-structure]] — structural patterns for maintainable SQL


## Source
- [[raw/papers/the-art-of-sql-2026-07-08.md]]

## Related Concepts
