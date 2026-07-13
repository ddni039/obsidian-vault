---
title: "Database Index"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/sql-performance-explained-2026-07-08.md]
confidence: high
---

## Summary
B-tree索引：減少資料庫讀取次數的核心結構，決定查詢速度上限。

## What
An index is a data structure that allows the database to find rows without scanning the entire table. The most common is the **B-tree** (balanced tree).

## How B-tree Works
- Logarithmic depth: even with millions of rows, B-tree depth rarely exceeds 4-5 levels
- Each level fits in memory page (typically 4-16 KB)
- Index traversal: root → branch → leaf → row location (typically 3-4 I/O operations)

## Column Selection (SQL Performance Explained Ch2)
- Index column order matters: equality conditions first, range last
- Most selective column first = fewer rows to filter at each level
- Partial indexes: index only rows that satisfy a condition (e.g., `WHERE active = 1`)

## Index Types Beyond B-tree
- **Bitmap**: good for low-cardinality columns (gender, status)
- **Hash**: O(1) lookup for equality predicates; no range queries
- **GiST/GIN**: full-text search, geometric data, JSON

## Hermes Relevance
- [[hermes-hindsight]] memory store benefits from B-tree indexes on timestamp and entity_id
- Skills index should use composite index on (domain_tag, updated_timestamp)
- Session history query speed = index on session_id + timestamp range

## Related
- [[sql-execution-plan]] — use EXPLAIN to see which index is chosen
- [[sql-covering-index]] — avoid table lookups entirely with covering index


## Source
- [[raw/papers/sql-performance-explained-2026-07-08.md]]

## Related Concepts
