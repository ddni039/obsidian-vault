---
title: "Typographic Ligatures"
created: "2026-07-11"
updated: "2026-07-11"
type: concept
tags: [typography, design, technique]
sources: [raw/papers/bringhurst-elements-of-typographic-style-2ed.md]
confidence: high
---

# Typographic Ligatures

Character-level refinements for improved readability. From [[robert-bringhurst]], [[bringhurst-elements-of-typographic-style]].

## The Five Basic Latin Ligatures

| Ligature | Description |
|----------|-------------|
| **ff** | Two f's joined |
| **fi** | f + i — most critical; the dot on i collides with f without ligature |
| **fl** | f + l — second most critical |
| **ffi** | f + f + i |
| **ffl** | f + f + l |

> "fi and fl are most crucial" — Bringhurst

## Why Ligatures Matter

- **Functional, not decorative**: Prevents collision between f's ascender and adjacent letters (especially i's dot, l's ascender)
- **Optical spacing**: ligatures replace what would otherwise be awkward spacing
- **Traditional**: Inherited from Renaissance printing, not invented by digital type designers

## Typographic Rules

1. Enable fi and fl at **10pt+ with serif faces**
2. **Never disable ffi and ffl** at display sizes — they almost never cause problems
3. **Sloped roman** (fake italic) has different collision behavior than **true italic** — test ligatures with actual italic faces
4. In PDF generation: use OpenType fonts with `liga` feature enabled

## Italic vs. Sloped Roman

> "Flow, not slope, differentiates italic from roman. True italic has cursive structure with transitive serifs. Sloped romans are calligraphic stunts."
> — Bringhurst

This distinction matters for PDF generation: sloped roman (mechanically tilted) needs different ligature handling than true italic (calligraphically designed).

## Related Concepts

- [[typographic-scale]] — type size and scale
- [[typographic-rhythm-proportion]] — leading and spacing
- [[typographic-harmony-counterpoint]] — type contrast and hierarchy
- [[pdf-design-spec]] — ligature settings in ReportLab PDF generation
