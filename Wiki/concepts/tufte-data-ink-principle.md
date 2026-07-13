---
title: "Data-Ink Maximization"
created: "2026-07-11"
updated: "2026-07-11"
type: concept
tags: [design, data-visualization, typography, tufte]
sources: [raw/papers/edward-tufte-wikipedia-2026.md]
confidence: high
---

# Data-Ink Maximization

Core principle from [[edward-tufte]]'s *The Visual Display of Quantitative Information* (1983).

## Core Statement

> "Maximize the data-ink ratio. Above all else, show data."

The **data-ink ratio** = ink used for actual data ÷ total ink used. Maximize it.

> "Sometimes decoration can help editorialize about the substance of the graphic. But it is wrong to distort the data measures—the ink locating values of numbers—in order to make an editorial comment or fit a decorative scheme."

## Chartjunk

Useless, non-informative, or information-obscuring elements. Types:
- 3D effects that distort proportions
- Decorative borders and backgrounds
- Shading that competes with data
- Heavy grid lines that dominate data ink
- ZapfDingbats, stars, decorative bullets

## Lie Factor

Ratio of graphic effect size to data effect size. A well-designed graphic has Lie Factor close to 1.

Lie Factor = (size of effect in graphic) ÷ (size of effect in data)

Example: A bar showing a 2× increase that appears 5× as tall has Lie Factor = 2.5.

## Application to PDF Design

From [[pdf-design-spec]]廢除清單 v2.0:
- **ZapfDingbats stars** → chartjunk, not data
- **Thick grid lines** → competing with content
- **Decorative gray lines** → non-data ink
- **3D effects** → lie factor distortion

## Related Concepts

- [[tufte-chartjunk]] — eliminating non-informative decoration
- [[color-relativity-principle]] — Albers' parallel principle for color
- [[pdf-design-spec]] — TRAP-57 (最小有效差異 threshold) is the operationalization of this
- [[tufte-small-multiples]] — design technique for high data density
