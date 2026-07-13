---
title: "SQL Strategic Writing"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/the-art-of-sql-2026-07-08.md]
confidence: high
---

## Summary
從策略而非語法切入 SQL：避免程序化思維，用聲明式方式表達意圖。

## Core Principle
SQL is a **declarative** language: you describe *what* you want, not *how* to get it. The optimizer decides how.

## The Problem
Most SQL performance issues come from developers who think imperatively:
- Writing application code patterns (loops, conditionals) in SQL
- Fetching raw data to application memory and filtering there
- Over-normalizing to avoid "duplication" at the cost of joins

## The Solution
Think in **sets** and **relations**:
- "Give me all orders where the customer has more than 3 orders" → `WHERE EXISTS (SELECT 1 FROM orders o2 WHERE o2.cust_id = o.cust_id HAVING COUNT(*) > 3)`
- "Give me the latest order per customer" → `RANK() OVER (PARTITION BY cust_id ORDER BY order_date DESC) = 1`

## Common Anti-Patterns
- **Cursor loops in SQL**: use set operations instead
- **Client-side joining**: database can join more efficiently with proper indexes
- **NULL as a value**: use NOT NULL constraints aggressively

## Hermes Relevance
- [[hermes-hindsight]] queries must be written as set operations, not Python loops
- [[hermes-skills-system]] skill discovery: prefer declarative queries over procedural filtering

## Related
- [[sql-anti-patterns]] — specific patterns to avoid
- [[sql-query-structure]] — structuring queries for performance and maintainability


## Source
- [[raw/papers/the-art-of-sql-2026-07-08.md]]

## Related Concepts
