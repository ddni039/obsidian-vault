---
title: "Typographic Page Design"
created: "2026-07-11"
updated: "2026-07-11"
type: concept
tags: [typography, design, technique]
sources: [raw/papers/bringhurst-elements-of-typographic-style-2ed.md]
confidence: high
---

# Typographic Page Design

Page proportion, margin, and textblock design principles from [[robert-bringhurst]], [[bringhurst-elements-of-typographic-style]].

## Proportions

Musical intervals translate directly to page proportions.

| System | Ratio |
|--------|-------|
| **Golden section (φ)** | 1.618 |
| **Medieval favorites** | 2:3, 3:4 |
| **Renaissance** | narrower (major/minor sixth) |
| **ISO paper** | 1:√2 (1:1.414) |
| **Common book** | 1:1.5 to 1:1.8 |

> The golden section (φ = 1.618) appears in nature and classical architecture — Bringhurst recommends it as the basis for page proportion systems.

## Textblock

- For **continuous reading**: set in columns taller than wide
- **Medieval books**: page and textblock used same proportions (monophonic page)
- **Renaissance**: polyphonic page — page and textblock with different proportions
- Columns should be **taller than wide** for continuous reading

## Margins

Margins must:
1. **Lock the textblock** to the page (structural)
2. **Frame it appropriately** (aesthetic)
3. **Leave room for thumbs** (practical)

**Folios** (page numbers) work best at upper/lower outside corners.

## Application to PDF Generation

For A4 PDF (210 × 297mm, ratio 1:√2 ≈ 1:1.414):
- Follow ISO proportion naturally
- Golden section → use φ = 1.618 for internal proportions (textblock to margin ratio)
- 20mm symmetric margins (≈ 0.75in) for print-ready output
- 3mm bleed for press

## Related Concepts

- [[typographic-scale]] — type size selection
- [[typographic-rhythm-proportion]] — leading and line length
- [[typographic-harmony-counterpoint]] — historical type periods
- [[pdf-design-spec]] — application to ReportLab PDF generation
