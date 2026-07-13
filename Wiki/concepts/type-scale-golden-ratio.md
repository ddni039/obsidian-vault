---
title: "Type Scale — Golden Ratio"
created: "2026-07-11"
updated: "2026-07-11"
type: concept
tags: [design, typography, type, scale, golden-ratio, lupton]
sources: [raw/papers/ellen-lupton-wikipedia-2026.md]
confidence: high
---

# Type Scale — Golden Ratio

Type size progressions derived from [[ellen-lupton]]'s *Thinking with Type* and [[robert-bringhurst]]'s traditional scale, unified via golden ratio φ = 1.618.

## Digital Type Scale (φ-progression)

| Level | Size | φ-Relationship |
|-------|------|----------------|
| Display | 34pt | φ² |
| Heading 1 | 21pt | φ |
| Heading 2 | 13pt | 1 (base) |
| Body | 10pt | 1/φ |
| Caption | 8pt | 1/φ² |

Note: 34/21 ≈ 1.619, 21/13 ≈ 1.615, close to φ = 1.618.

## Traditional Type Scale (Bringhurst)

From [[robert-bringhurst]]'s historical compilation:

| Name | Points |
|------|--------|
| Great Primer | 18 |
| English | 14 |
| Pica | 12 |
| Small Pica | 11 |
| Long Primer | 10 |
| Bourgeois | 9 |
| Brevier | 8 |
| Minion | 7 |
| Nonpareil | 6 |

## Application in PDF Generation

From [[pdf-design-spec]] (六師排版紀律):
- Page: A4, bleed 3mm, margin 20mm symmetric
- Type scale: **34/21/13/8pt** (digital golden ratio)
- Leading: **1.3x** (13pt → 16.9pt ≈ 17pt)
- Baseline grid: **13pt unit** (Müller-Brockmann from Bringhurst)

## Rules

1. **Consistency**: Use one scale exclusively — don't mix systems
2. **Hierarchy through scale**: Larger = more important
3. **Ligatures at 10pt+**: Enable fi/fl in serif faces
4. **One parameter at a time**: Change size OR weight OR spacing — not all at once

## Related Concepts

- [[typographic-scale]] — Bringhurst's traditional scale (more detailed)
- [[hierarchical-redundancy]] — triple-signal encoding for each level
- [[typographic-rhythm-proportion]] — leading relationship
- [[pdf-design-spec]] — operationalization in ReportLab
