---
title: "SQL Covering Index (Index-Only Scan)"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/sql-performance-explained-2026-07-08.md]
confidence: high
---

## Summary
所有查詢欄位都在索引中 → 無需讀取資料表，Index-Only Scan。

## What
A covering index includes all columns needed by a query — not just the WHERE clause columns. The database can satisfy the query entirely from the index without touching the table at all.

## Example
Query: `SELECT email, name FROM users WHERE last_name = 'Smith'`
Covering index: `CREATE INDEX idx_covering ON users(last_name, email, name);`

Without covering index: ① Find rows by index → ② Random I/O to fetch email, name from table
With covering index: ① Find rows by index → done (email, name already in index leaf)

## Trade-offs
- Index size grows: more columns = larger index = slower writes
- Not always worth it: if table is small or query selectivity is high, full scan may be faster

## When to Use
- Frequently executed queries on large tables
- Columns with high fan-out (many rows per index entry)
- OLAP workloads with predictable, repetitive queries

## Hermes Relevance
- [[hermes-hindsight]] observation queries: if we always query (entity_id, timestamp, observation_text), a covering index eliminates table I/O
- Skills lookup: `SELECT skill_name, domain FROM skills WHERE domain = 'ai-agent'` → covering index on (domain, skill_name, domain_tag)

## Related
- [[database-index]] — covering index is just an index with all necessary columns
- [[sql-execution-plan]] — "Index Only Scan" in EXPLAIN confirms covering index usage


## Source
- [[raw/papers/sql-performance-explained-2026-07-08.md]]

## Related Concepts
