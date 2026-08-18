# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-07-11] ingest | Bringhurst — The Elements of Typographic Style (2nd ed. 1996)
- Source: https://readings.design/PDF/the_elements_of_typographic_style.pdf
- Raw: raw/papers/bringhurst-elements-of-typographic-style-2ed.md
- Entity: entities/robert-bringhurst.md
- Concepts: concepts/typographic-scale.md, concepts/typographic-rhythm-proportion.md, concepts/typographic-ligatures.md, concepts/typographic-page-design.md
- ChromaDB: 59 pages total (wiki_karpathy collection)
- Index: updated (total pages: 31)

## [2026-07-11] ingest | Six Masters of Typographic Design → LLM Wiki + ChromaDB
- Sources: Wikipedia summaries for Albers, Müller-Brockmann, Ellen Lupton, Edward Tufte
- Raw: josef-albers-wikipedia-2026.md, josef-muller-brockmann-wikipedia-2026.md, ellen-lupton-wikipedia-2026.md, edward-tufte-wikipedia-2026.md (note: physical PDFs were image scans with 0 extractable text)
- Entities: josef-albers.md, josef-muller-brockmann.md, ellen-lupton.md, edward-tufte.md, josef-and-annin-albers-foundation.md
- Concepts: color-relativity-principle.md, tufte-data-ink-principle.md, tufte-envisioning-information.md, grid-systems-graphic-design.md, hierarchical-redundancy.md, type-scale-golden-ratio.md
- ChromaDB: 70 pages total (wiki_karpathy collection)
- Index: updated (total pages: 43)

## [2026-07-11] ingest | Hindsight Memory Provider README
- Created: raw/articles/hermes-hindsight-readme-2026.md
- Created: concepts/hermes-hindsight.md
- Updated: index.md (Concepts + Raw sections)
- Tags: agent, tool, memory, hermes

## [2026-07-11] ingest | NousResearch/hermes-agent GitHub repo
- Created: raw/articles/nous-hermes-agent-repo-2026.md (v0.18.0, 208k stars)
- Created: entities/hermes-agent.md (全面重寫，取代舊版)
- Updated: index.md (Entities section, Raw section updated)
- Tags: platform, framework, agent, nous-research

## [2026-07-11] 整理 | Hermes Agent v0.18.0 更新內容 PDF 教程
- 整理 Hermes Agent v0.18.0 更新為小白教程，PDF 格式輸出
- 標的：無基礎用戶，由專家視角撰寫
- Created: raw/articles/codex-obsidian-integration-2026.md
- Created: concepts/codex-obsidian-integration.md
- Updated: index.md (Concepts + Raw sections)
- Tags: workflow, tool, platform
- Domain: AI Agent技術、生態系與應用
- Structure created with SCHEMA.md, index.md, log.md
- Directories: raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/, _archive/
- Pages created: entities/hermes-agent.md, entities/claude-code.md, entities/codex.md, concepts/ai-agent.md
- Index updated
## [2026-06-11] ingest | Karpathy LLM Wiki → wiki + ChromaDB
- Source: https://github.com/multica-ai/andrej-karpathy-skills
- Raw: raw/articles/karpathy-llm-wiki-2026.md
- Entities: andrej-karpathy, multica-ai
- Concepts: karpathy-think-before-coding, karpathy-simplicity-first, karpathy-surgical-changes, karpathy-goal-driven-execution
- Comparisons: karpathy-vs-hermes-tri-role
- ChromaDB: 11 pages ingested (collection: wiki_karpathy)

## [2026-06-11] ingest | Agency Agents → wiki + ChromaDB
- Source: https://github.com/msitarzewski/agency-agents
- Raw: raw/articles/agency-agents-readme-2026.md (71.8KB README, 232 agents/16 divisions)
- Entities: agency-agents, agency-engineering-division, agency-frontend-developer
- Concepts: agency-multi-agent-architecture
- Comparisons: agency-vs-hermes-tri-role
- ChromaDB: ingested into wiki_karpathy collection

## [2026-07-01] ingest | Hermes Agent Docs → wiki
- Source: https://hermes-agent.nousresearch.com/docs/
- Raw: raw/articles/hermes-agent-docs-2026.md
- Entities: hermes-agent (updated, expanded with architecture, memory, skills, messaging gateway)
- Concepts: mcp-model-context-protocol, hermes-learning-loop, hermes-skills-system, hermes-messaging-gateway
- Index: updated (total pages: 22)



## [2026-07-08] ingest | 9 sources → LLM Wiki + ChromaDB
- Sources: 5 new papers (Anthropic/Raft/3x arXiv) + 4 books (DDIA/SQL Perf/Art of SQL/Learning SQL)
- Raw: raw/papers/*-2026-07-08.md (9 files)
- Entities: 9 new (anthropic-ai-agents-framework, raft-consensus-algorithm, agentic-design-patterns-2025, agentic-ai-software-architecture-evolution, agentic-communities-paper, markus-winand-sql-performance-explained, martin-kleppmann-ddia, stephane-faroult-art-of-sql, alan-beaulieu-learning-sql)
- Concepts: 22 new (4 agents + 7 distributed systems + 11 database)
- Index: updated (total pages: {total_entities + total_concepts})


## 2026-07-08 — Visual Art Books INGEST
- **Sources:** 6 PDFs (7th grid-scan=failed)
- **Entities:** dashboard-design-few, interaction-of-color-albers, non-designers-design-book, shape-of-design, signs-symbols-frutiger, universal-methods-design
- **Concepts:** 12 visual art concepts established
- **Raw files:** ~/.wiki/raw/visual/
- **Status:** Wiki pages written, ChromaDB pending


## 2026-07-08b — Thinking with Type (Lupton) INGEST
- **Source:** mubranding.com (designer workbook, 224pp, 374K chars)
- **Entity:** thinking-with-type-lupton.md
- **Concepts:** 10 new Lupton-specific concepts
- **Chunks:** 521
- **Status:** Raw + Entity + Concepts + Wiki index done

## 2026-07-08 16:45 — DDIA (Kleppmann) 攝入完成

| 項目 | 值 |
|------|-----|
| Raw | `raw/papers/designing-data-intensive-applications-2026-07-08.md`（1.43M chars）|
| ChromaDB | `llm-wiki-papers-v1` +1791 chunks（總計 5912）|
| Query 驗證 | partitioning / stream processing / ACID BASE — 全部命中 |

## [2026-07-09] ingest | Software Testing, Debugging, Maintenance — Wikipedia Sources

- **Raw sources:**
  - `raw/articles/software-testing-wikipedia-2026-07-09.md` — Software testing Wikipedia (Wikipedia)
  - `raw/articles/debugging-wikipedia-2026-07-09.md` — Debugging Wikipedia (Wikipedia)
- **Wiki pages created:**
  - `concepts/software-testing-fundamentals.md` — Oracle problem, test pyramid, static/dynamic, exploratory testing
  - `concepts/debugging.md` — Wolf fence, delta debugging, git bisect, post-mortem, zero-defects anti-pattern
  - `concepts/software-testing-maintenance.md` — Legacy code strategies, characterisation tests, Hermes maintenance patterns
- **Index:** 3 concepts added → Total 70 pages
- **Source:** Jina AI Reader (r.jina.ai) Wikipedia extraction
- **Note:** Firecrawl API key revoked (HTTP 401); Jina fallback worked for Wikipedia. Key updated 2026-07-10.

## [2026-07-10] ingest | Software Testing & Analysis (Pezzè/Young) + Automation Pipelines (Fowler) + 3 concepts
- **Entities 新增（2個）：**
  - `entities/software-testing-and-analysis-pezze-young.md` — 靜態/動態分析、NIST Bug Cost、測試策略框架
  - `entities/automation-pipelines-martinfowler.md` — CI 定義、Martin Fowler 核心實踐、Pipeline 階段
- **Concepts 新增（3個）：**
  - `concepts/legacy-code-strategies.md` — Feathers Seams 模型、Characterisation Tests、九種依賴斷裂技術
  - `concepts/pragmatic-programmer-tips.md` — Hunt & Thomas 20 Tips 精煉、DRY/Eliminate Effects/Debugging Mindset
  - `concepts/xunit-test-patterns.md` — Meszaros 壞味道分類、Test Double、Test Data Builder
- **Index 更新：** 6 個新頁面加入 index.md
- **Research report 更新：** sources 欄位加入 6 個新頁面
- **Source:** Firecrawl API v1 scrape (key fc-c27...0f97) + martinfowler.com + ThoughtWorks blog
- **Note:** Firecrawl key fc-c27fbed112a14d8d9897221739620f97 confirmed valid 2026-07-10

## [2026-07-09] research | Software Quality & Maintenance — 提升偵測維護編碼

- **書單（4本）：** Feathers / PragProg / Butcher / Meszaros
- **聯網失敗：** vendor pages (InformIT/O'Reilly/PragProg/Goodreads) 全部被擋，無 raw source
- **因應做法：** 以專家知識建立 entity，標註 `status: wiki-entity-only`
- **成果：**
  - 4 entities (`wiki/entities/`)
  - 3 concepts (已有)
  - 1 research report (`wiki/research/`)
  - Index → Total 74 pages
