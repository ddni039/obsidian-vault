---
title: "SQL Query Structure"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/the-art-of-sql-2026-07-08.md]
confidence: high
---

## Summary
查詢結構設計：子查詢與 JOIN 選擇、代價估算與執行計劃。

## Structure Principles

### Prefer JOIN over Subquery (Usually)
Most optimizers handle joins and subqueries similarly, but JOIN is more readable and flexible.
Exception: correlated subqueries with aggregate are sometimes faster.

### Use CTEs (Common Table Expressions) for Clarity
```sql
WITH high_value AS (
    SELECT cust_id FROM orders WHERE total > 1000
)
SELECT c.name, o.order_date
FROM customers c
JOIN orders o ON c.id = o.cust_id
WHERE c.cust_id IN (SELECT cust_id FROM high_value)
```

### Filter Early, Reduce Early
Push predicates down to the earliest stage possible. Each row filtered early = fewer rows to process later.

### Prefer EXISTS over IN for Subquery Membership Tests
```sql
-- Bad: builds full set in memory
WHERE cust_id IN (SELECT cust_id FROM big_table)

-- Good: stops at first match
WHERE EXISTS (SELECT 1 FROM big_table WHERE big_table.cust_id = outer_t.cust_id)
```

## Hermes Relevance
- [[hermes-hindsight]] graph traversal queries benefit from CTE-based structure
- [[hermes-skills-system]] skill matching queries should use EXISTS not IN

## Related
- [[sql-anti-patterns]] — patterns to actively avoid
- [[sql-execution-plan]] — verify the structure you write matches what the optimizer plans


## Source
- [[raw/papers/the-art-of-sql-2026-07-08.md]]

## Related Concepts
