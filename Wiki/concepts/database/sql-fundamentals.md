---
title: "SQL Fundamentals"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/learning-sql-3rd-2026-07-08.md]
confidence: high
---

## Summary
SELECT/FROM/WHERE/GROUP BY/HAVING/ORDER BY/LIMIT — SQL 核心語法。

## Core Clauses (Execution Order)
1. `FROM` — load data
2. `WHERE` — filter rows (before grouping)
3. `GROUP BY` — aggregate
4. `HAVING` — filter groups (after grouping)
5. `SELECT` — project columns
6. `ORDER BY` — sort
7. `LIMIT/OFFSET` — paginate

## Aggregation
- `COUNT/SUM/AVG/MIN/MAX` — single-value aggregations
- `GROUP_CONCAT` — aggregate strings
- `COUNT(DISTINCT col)` — unique count
- Window functions: `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`

## Set Operations
- `UNION` / `UNION ALL` — combine results (ALL preserves duplicates)
- `INTERSECT` / `EXCEPT` — intersection and difference

## Conditional Logic in SQL
- `CASE WHEN ... THEN ... ELSE ... END`
- `NULLIF(col, val)` — returns NULL if col = val
- `COALESCE(col1, col2, ...)` — first non-NULL

## Hermes Relevance
- All [[hermes-hindsight]] queries build on these fundamentals
- [[hermes-skills-system]] skill search uses GROUP BY on domain tags

## Related
- [[sql-data-modification]] — INSERT/UPDATE/DELETE
- [[sql-schema-design]] — creating the schema these queries run against


## Source
- [[raw/papers/learning-sql-3rd-2026-07-08.md]]

## Related Concepts
