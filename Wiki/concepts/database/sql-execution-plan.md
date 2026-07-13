---
title: "SQL Execution Plan"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/sql-performance-explained-2026-07-08.md]
confidence: high
---

## Summary
EXPLAIN 輸出分析：資料庫如何執行你的查詢，索引選擇依據。

## What
The query optimizer chooses an execution plan: the sequence of operations to retrieve or modify data. Use `EXPLAIN` (or `EXPLAIN ANALYZE`) to inspect it.

## Key Scan Types (from worst to best)
1. **Full Table Scan**: reads every row — avoid on large tables
2. **Index Scan**: reads entire index, then fetches rows (2 I/Os per row)
3. **Index-Only Scan**: reads only the index, no table lookup — ideal
4. **Index Range Scan**: reads a range of index entries (B-tree range query)

## WHERE Clause → Access Path
- `column = value` → index lookup (fast)
- `column > value` → index range scan
- `column LIKE 'prefix%'` → index range scan (prefix wildcard)
- `column LIKE '%suffix'` → full table scan (can't use index)
- `column IS NULL` → some engines use index, some don't

## Join Strategies
- **Nested Loop Join**: O(n*m) — good if one side is small and has index
- **Hash Join**: O(n+m) — good for large equi-joins, requires memory
- **Merge Join**: O(n+m) — good for pre-sorted inputs

## Hermes Relevance
- When diagnosing slow KB queries, `EXPLAIN` on the Hindsight SQLite file reveals missing indexes
- [[hermes-skills-system]] skill search: verify index is used on domain_tag

## Related
- [[database-index]] — proper indexing is the prerequisite for good plans
- [[sql-join-strategies]] — join order and strategy selection


## Source
- [[raw/papers/sql-performance-explained-2026-07-08.md]]

## Related Concepts
