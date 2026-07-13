---
title: "SQL Join Strategies"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [database, concept]
sources: [raw/papers/sql-performance-explained-2026-07-08.md]
confidence: high
---

## Summary
Nested Loop / Hash / Merge JOIN 演算法：代價估算與適用場景。

## Three Main Strategies

### Nested Loop Join
```
for each row in outer_table:
    for each row in inner_table:
        if match: emit row
```
- Best when: inner table has index on join key and outer table is small
- Worst when: both large, no indexes → O(n×m) I/Os

### Hash Join
```
build: build hash table from smaller table's join keys
probe: for each row in larger table, probe hash table
```
- Best when: equi-join on large tables, no index available
- Requires: memory for hash table; spills to disk if too large
- Not usable for non-equi joins (<, >, BETWEEN)

### Merge Join
```
sort both inputs on join key
scan both in parallel, emit matches
```
- Best when: inputs already sorted (or can sort cheaply)
- Efficient for: range joins (e.g., `t1.id BETWEEN t2.start AND t2.end`)

## Join Order
The optimizer picks which table is outer/inner (or build/probe). Always put the smaller result set first when possible.

## Hermes Relevance
- [[hermes-hindsight]] knowledge graph traversal = recursive JOIN across entity edges
- [[hermes-skills-system]] skill search: verify join between skills table and tags table uses index

## Related
- [[sql-execution-plan]] — use EXPLAIN to see which join strategy was chosen
- [[database-index]] — index availability determines which strategies are viable


## Source
- [[raw/papers/sql-performance-explained-2026-07-08.md]]

## Related Concepts
