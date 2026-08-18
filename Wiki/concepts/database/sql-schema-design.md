---
title: "SQL Schema Design"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/learning-sql-3rd-2026-07-08.md]
confidence: high
---

## Summary
DDL + PRIMARY KEY/FOREIGN KEY + 視圖 + 觸發器基礎。

## Normalization (1NF through 3NF)
- **1NF**: atomic columns, no repeating groups
- **2NF**: no partial dependencies on composite keys
- **3NF**: no transitive dependencies (non-key columns depend only on PK)

## Keys
- **Primary Key (PK)**: uniquely identifies each row; NOT NULL + UNIQUE
- **Foreign Key (FK)**: references PK of another table; enforces referential integrity
- **Candidate Key**: any column that could be a PK
- **Surrogate Key**: auto-increment or UUID; used when natural key is inconvenient

## Indexes
- `PRIMARY KEY` → clustered index by default (in most engines)
- `UNIQUE` → non-clustered unique index
- Regular indexes for query performance

## Views
Virtual tables defined by a query. Can simplify complex joins, hide columns, provide encapsulation.

## Triggers
Code that runs automatically on INSERT/UPDATE/DELETE. Use sparingly — they make data flow opaque.

## Hermes Relevance
- [[hermes-hindsight]] schema: entities table with FK to observations = normalized design
- [[hermes-skills-system]] skills table: tags as separate junction table (normalized) vs. comma-separated (denormalized, faster for small scale)

## Related
- [[sql-fundamentals]] — the queries that run against the schema
- [[sql-data-modification]] — the writes that the schema receives


## Source
- [[raw/papers/learning-sql-3rd-2026-07-08.md]]

## Related Concepts
