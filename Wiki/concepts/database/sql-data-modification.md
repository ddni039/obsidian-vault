---
title: "SQL Data Modification"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/learning-sql-3rd-2026-07-08.md]
confidence: high
---

## Summary
INSERT/UPDATE/DELETE + 交易控制（COMMIT/ROLLBACK）。

## Modification Statements
```sql
INSERT INTO table (col1, col2) VALUES (val1, val2);
INSERT INTO table SELECT ...;  -- bulk insert from query
UPDATE table SET col = val WHERE ...;
DELETE FROM table WHERE ...;
```

## Transactions
```sql
START TRANSACTION;
-- multiple statements
COMMIT;  -- make permanent
-- OR
ROLLBACK;  -- undo all
```

## ACID in Practice
- **Atomicity**: all-or-nothing modification
- **Durability**: committed writes survive power loss (if storage is healthy)
- **Isolation**: controls visibility of uncommitted changes to other connections
- **Consistency**: enforced by constraints (PK, FK, NOT NULL, CHECK)

## Isolation Levels (Real-World Impact)
| Level | Dirty Read | Non-Repeatable Read | Phantom |
|-------|-----------|--------------------|---------|
| READ UNCOMMITTED | Possible | Possible | Possible |
| READ COMMITTED | Prevented | Possible | Possible |
| REPEATABLE READ | Prevented | Prevented | Possible |
| SERIALIZABLE | Prevented | Prevented | Prevented |

## Hermes Relevance
- [[hermes-hindsight]] knowledge graph writes: wrap multi-entity updates in transactions
- [[hermes-skills-system]] skill installation: transactional update of skill metadata

## Related
- [[sql-fundamentals]] — SELECT is the basis for understanding modification
- [[sql-schema-design]] — schema constraints enforce consistency


## Source
- [[raw/papers/learning-sql-3rd-2026-07-08.md]]

## Related Concepts
