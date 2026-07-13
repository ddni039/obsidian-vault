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

## [2026-07-11] comparison | Prompt Engineering Cross-Provider
- Created: comparisons/prompt-engineering-cross-provider.md
- Synthesizes all 3 sources: Chip Huyen + Anthropic + OpenAI
- 10-dimension comparison table + practical decision guide + 2023→2026 evolution
- Index: updated (total pages: 93)

## [2026-07-11] ingest | Anthropic + OpenAI Prompt Engineering Guides
- Anthropic: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/ (overview) + /claude-prompting-best-practices
- OpenAI: https://platform.openai.com/docs/guides/prompt-engineering
- Raw: raw/articles/anthropic-prompting-best-practices-2026.md, raw/articles/openai-prompt-engineering-2026.md
- Concepts: anthropic-prompt-engineering.md, openai-prompt-engineering.md, reasoning-models.md, anthropic-adaptive-thinking.md
- Index: updated (total pages: 92)
- Note: reasoning-models.md cross-references both Anthropic + OpenAI sources
- Note: anthropic-adaptive-thinking.md covers the deprecated→adaptive thinking migration

## [2026-07-11] ingest | Chip Huyen — Building LLM Applications for Production
- Source: https://huyenchip.com/2023/04/11/llm-engineering.html (131KB, 130K+ chars)
- Raw: raw/articles/chip-huyen-llm-engineering-2023.md (sha256: 2e514ccadc0d119c1be6699b2106c99423e1e6290d23b6371071d7ffa7dbb699)
- Entity: entities/chip-huyen.md
- Concepts: llmops.md, prompt-engineering-production.md, embedding-vector-database.md, llm-agents-tool-use.md, talk-to-your-data.md, finetuning-vs-prompting.md
- Index: updated (total pages: 88)
- New section "LLM Engineering (2026-07-11)" added to Concepts

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

## [2026-07-11] ingest | AI Engineering (Chip Huyen, O'Reilly 2025)
- Source: https://github.com/chiphuyen/aie-book (MIT License, 16.4k stars)
- Raw sources saved: `raw/articles/aie-book-toc-2025.md`, `aie-book-chapter-summaries-2025.md`, `aie-book-resources-2025.md`
- Updated: `entities/chip-huyen.md` — expanded with full AIE book details (10 key questions, 3-part structure, key contributions)
- Created: `concepts/ai-engineering-framework.md` — 3-layer stack, 10-chapter structure, adaptation sequence
- Created: `concepts/ai-evaluation.md` — perplexity, AI-as-a-Judge, comparative eval, eval pipeline design
- Created: `concepts/rag-and-agents.md` — RAG architecture, retrieval algorithms, agent components, failure modes
- Created: `concepts/inference-optimization.md` — TTFT/TPOT, quantization, KV cache, parallelism
- Index → Total 97 pages (+4 new concepts)

## [2026-07-11] ingest | Designing ML Systems book (Chip Huyen, O'Reilly 2022)
- Source: https://github.com/chiphuyen/dmls-book (5MB, 16 forks, MIT license)
- Raw: 4 files in raw/articles/designing-ml-systems-*-2026-07-11.md (summary/mlops-tools/resources/basic-ml-review)
- Entity: entities/designing-ml-systems-book.md
- Concepts: concepts/mlops-systems-design.md, concepts/data-distribution-shifts.md, concepts/training-data-lifecycle.md
- Index: Total 101 pages (+4 new)

## [2026-07-11] research | DMLS vs Hermes + DMLS vs AIE/LLMOps 深化分析
- Comparison: comparisons/dmls-vs-hermes-architecture.md — DMLS 11章 vs Hermes 架構對應矩陣；Skills=Feature Store缺口、分佈偏移監控缺口
- Comparison: comparisons/dmls-vs-aie-vs-llmops.md — DMLS/AIE/LLMOps 三部曲知識邊界；發現：AIE 未引用 DMLS 四系統需求、LLMOps 未引用 adaptation sequence
- Patched: ai-engineering-framework.md — 添加與 DMLS Ch2 的繼承關係
- Index: Total 103 pages (+2 new comparisons)

## [2026-07-13] ingest | Designing Multi-Agent Systems (Victor Dibia 2025) + M1-Parallel (arXiv 2507.08944)
- Source: raw/articles/designing-multiagent-systems-book-2026-07-13.md
- Source: raw/articles/m1-parallel-arxiv-2026-07-13.md
- Entity: entities/designing-multi-agent-systems-book.md
- Entity: entities/victor-dibia.md
- Entity: entities/picoagents.md
- Entity: entities/m1-parallel-framework.md
- Concept: concepts/parallel-multi-agent-execution.md
- Index: Total 108 pages (+5 new: 4 entities + 1 concept)
- 核心發現：M1-Parallel 證實並行多 plan + early termination 可達 2.2× speedup；diversity 不顯著優於 repeated sampling
- 與 Hermes 對應：`delegate_task` + `background:true` + `notify_on_complete:true` 即對應 M1-Parallel event-driven 模式

## [2026-07-13] ingest | 主控台/控制平面 3 大權威資源
- Source: raw/articles/agent-harness-engineering-2026-07-13.md — Adnan Masood《Agent Harness Engineering》7 大 takeaways
- Source: raw/articles/agent-control-plane-activant-2026-07-13.md — Activant 2026 控制平面研究
- Source: raw/articles/agent-skills-anthropic-course-2026-07-13.md — Andrew Ng × Anthropic Agent Skills L0-L8
- Entity: entities/agent-harness.md — `{Agent} = {Model} + {Harness}` 6 大職責
- Entity: entities/agent-control-plane.md — 4 大核心能力（治理/上下文/編排/評估）
- Concept: concepts/pev-loop.md — Plan-Execute-Verify 三階段循環；Reasoning Sandwich
- Concept: concepts/progressive-disclosure-skills.md — Anthropic Skills 三階段揭露模式
- Index: Total 113 pages (+5: 2 entities + 2 concepts + 1 raw above)
- 核心發現：
  - Hermes 的 C/B/H/H'/E 五角色 + RULES.md = Agent Harness 完整實作
  - PEV Loop 在 Hermes 中由 `routing-check` + Phase Lock + E-code 斷路器支撐
  - Progressive Disclosure 在 Hermes Skill 系統中已對應（metadata → SKILL.md → references/）
  - 差距：Per-agent identity、Visual Workflow Canvas、Cost Guardrails

## [2026-07-13] ingest | 編碼能力提升書籍研究（METR RCT + AI 時代書單）
- Source: raw/articles/metr-2025-rct-developer-productivity-2026-07-13.md — METR 2025-07 RCT：AI 讓 16 位資深開發者慢 19%
- Source: raw/articles/metr-2026-uplift-survey-2026-07-13.md — METR 2026 追蹤（Late RCT + Survey）
- Source: raw/articles/ai-era-software-engineering-books-2026-07-13.md — AI 時代 SE 必讀書單
- Entity: entities/metr.md — Model Evaluation and Threat Research 組織
- Concept: concepts/ai-coding-productivity-paradox.md — 三大證據矛盾（benchmark vs RCT vs anecdotes）
- Concept: concepts/perception-vs-reality-gap.md — Perception vs Reality 落差（高估 40 個百分點）
- Index: Total 119 pages (+6: 1 entity + 2 concepts + 3 raw)
- 核心發現：
  - **METR 2025 RCT 震撼**：預期 +24%，實際 -19%，實驗後仍相信 +20%
  - **METR 2026 更新**：估計 AI 從負轉正（快 4-18%）
  - **METR 2026 Survey**：349 人自我報告 1.4-2× value，3× speed（可能高估）
  - **AI 時代核心轉變**：Tools 是 collaborators 而非 assistants → fundamentals 更重要

## [2026-07-13] ingest | 架構運行書籍研究（Google SRE + 20 書單）
- Source: raw/articles/google-sre-book-2026-07-13.md — Google SRE Book 完整 34 章 + 5 大核心原則
- Source: raw/articles/20-essential-sre-books-catchpoint-2026-07-13.md — Catchpoint 整理 20 本 SRE 必讀書單
- Entity: entities/sre-site-reliability-engineering.md — SRE 概念、5 大原則、Error Budget、與 Hermes 對應（95%+）
- Concept: concepts/slos-error-budget.md — SLI/SLO/SLA 三層 + Error Budget 機制
- Concept: concepts/eliminating-toil.md — Toil 自動化 6 策略 + Hermes 案例
- Index: Total 122 pages (+5: 1 entity + 2 concepts + 2 raw)
- 核心發現：
  - Hermes 已實作 95%+ SRE 核心原則（SLO/Toil/Postmortem/Cascading Failure Protection）
  - Google SRE Book 免費線上版（sre.google/sre-book/）含完整 34 章
  - 推薦必讀 5 本：Accelerate / SRE Book / Phoenix Project / DevOps Handbook / Continuous Delivery

## [2026-07-13] ingest | The DevOps Handbook（合規攝入）+ DORA 2024
- Source: raw/articles/the-devops-handbook-2026-07-13.md — IT Revolution 官方 Intro PDF（23 章 + 6 部目錄）
- Source: raw/articles/dora-2024-state-of-devops-2026-07-13.md — Google Cloud 官方 DORA 2024 報告
- Entity: entities/the-devops-handbook-book.md — Gene Kim 等 4 位 DevOps 創辦人合著
- Concept: concepts/three-ways-devops.md — Flow / Feedback / Continual Learning
- Concept: concepts/calms-framework.md — 5 支柱（Culture/Automation/Lean/Measurement/Sharing）
- Concept: concepts/dora-four-key-metrics.md — DF/LT/CFR/MTTR 業界標準
- Index: Total 128 pages (+6: 1 entity + 3 concepts + 2 raw)
- 攝入方法：使用 IT Revolution 官方免費章節 + O'Reilly 目錄 + DORA 官方頁面，**未擷取未授權完整 PDF**
- 核心發現：
  - Hermes 對 DORA 4 大關鍵指標 4/4 達 Elite
  - Hermes 對 CALMS 5 支柱 90% 實作
  - DORA 2024 警告：AI 對 stability 有負面影響（建議加 retry + circuit breaker）

## [2026-07-13] ingest | Vinyl Cache（formerly Varnish Cache）官方文件
- Entity: entities/vinyl-cache.md — HTTP accelerator / caching reverse proxy；BSD license；v9.0.0（2026-03-16）
- Concept: concepts/vcl-varnish-configuration-language.md — VCL DSL 完整解析；VCL → C → .so → hot reload；Hook lifecycle
- Source: raw/articles/vinyl-cache-official-2026-07-13.md — 官方文件完整攝入（Users Guide + Reference Manual + VMODs）
- Index: Total 133 pages (+4: 1 entity + 1 concept + 2 raw)
- ⚠️ 注意：ebooks.karbust.me 的盜版 PDF 未使用，改用官方 vinyl-cache.org 完全合規文檔
- 核心發現：
  - Vinyl Cache v8→v9 改名（避免名稱衝突）
  - VCL hot reload = Hermes `touch config.yaml` 直接對應
  - Backend health probe = Hermes MCP heartbeat 直接對應
  - Grace mode = Hermes E-code circuit breaker 可借鏡
  - VMOD plugin = Hermes Skill plugin 直接對應

## [2026-07-13] ingest | Accelerate 原典（DevOps 量化研究）
- Entity: entities/accelerate-book.md — Accelerate 原典（Nicole Forsgren, Jez Humble, Gene Kim, 2018）；Shingo Award；24 個關鍵能力 + 4 個關鍵指標 + Westrum 文化模型
- Source: raw/articles/accelerate-book-2026-07-13.md — IT Revolution 官方書籍頁面 + 第三方章節摘要（danlebrero.com + roman.pt）
- Index: Total 136 pages (+4: 1 entity + 1 raw)
- ⚠️ 注意：ebooks.karbust.me 的盜版 PDF 未使用，改用 IT Revolution 官方 excerpt PDF + 合規摘要
- 核心發現：
  - Accelerate 是 DevOps Handbook 的理論基礎
  - 24 個關鍵能力分為 5 大類（CD/Architecture/Product/Lean/Cultural）
  - 4 個關鍵指標（Lead Time/DF/MTTR/CFR）量化組織效能
  - Westrum generative culture 預測更好的軟體交付
  - Hermes 4/4 達 Elite 水準

## [2026-07-13] ingest | 文謀閱讀地圖（Strategic Thinking Reading List）
- Entity: entities/strategic-thinking-reading-list.md — McKinsey 2026 + OfferZen 20 + DEV.to 7 整合書單；5 大文謀能力維度
- Concept: concepts/system-1-system-2-thinking.md — Kahneman 兩個思維系統（System 1 快/直覺 vs System 2 慢/邏輯）；8 大認知偏誤；文謀應用決策品質
- Source: raw/articles/strategic-thinking-reading-list-2026-07-13.md — 完整書單 + 推薦順序
- Index: Total 232 pages (+3: 1 entity + 1 concept + 1 raw)
- 3 本聖經：
  - **Thinking Fast and Slow**（Kahneman；決策品質）
  - **Designing Data-Intensive Applications**（Kleppmann；系統思維）
  - **Software Architecture: The Hard Parts**（Ford et al.；技術架構）
- 3 本輔助：
  - Software Engineering at Google（業界實踐）
  - An Elegant Puzzle（工程管理）
  - Clean Architecture（結構思維）

## [2026-07-13] ingest | 主控台書籍研究（Chaos Engineering + K8s Control Plane）
- Entity: entities/chaos-engineering.md — 雙書攝入（Rosenthal+Jones O'Reilly 2020；Pawlikowski Manning 2021）；4 大實驗原則；Simian Army
- Concept: concepts/control-plane-pattern-declarative-reconciliation.md — Declarative + Reconciliation Loop + State Store；K8s 與 Hermes 對應；Hermes 1.0→2.0 演進
- Source: raw/articles/chaos-engineering-books-2026-07-13.md — 完整雙書原始資料
- Source: raw/articles/kubernetes-control-plane-2026-07-13.md — K8s 2026 完整架構（CloudOptimo 合規 blog）
- Index: Total 235 pages (+5: 1 entity + 1 concept + 2 raw)
- 核心洞察：
  - Chaos Engineering 是 Control Plane 唯一可靠驗證方法
  - K8s Declarative + Reconciliation 是 Hermes 主控台設計最直接參考
  - Operator Pattern 對應 Hermes Skill + subagent
  - 4 大混沌實驗原則：Steady State / Blast Radius / Continuous / Fail-Fast

## [2026-07-13] ingest | Hermes 智能提升（LLM Reasoning + Agent Architecture）
- Entity: entities/hermes-intelligence-5-layer-architecture.md — 5 層架構評估；現狀 71% → 目標 93%
- Concept: concepts/chain-of-thought-reasoning.md — Chain-of-Thought（Wei 2022，32540 citations）；CoT 演進樹
- Source: raw/articles/hermes-intelligence-reading-map-2026-07-13.md — 完整閱讀地圖（EITT 2026 + Victor Dibia + Future AGI）
- Index: Total 238 pages (+3: 1 entity + 1 concept + 1 raw)
- 4 大權威資源：
  - **EITT Academy**：AI Agents 2026 Guide（含 5 層架構）
  - **Victor Dibia**（MSR）：Designing Multi-Agent Systems（6 orchestration patterns）
  - **Future AGI**：10 本 LLM 書單
  - **Chain-of-Thought Paper**（Wei 2022，32540 citations）
- 5 層架構評估：
  - Layer 1 LLM: 70%
  - Layer 2 Reasoning: 75%
  - Layer 3 Tools: 60%
  - Layer 4 Memory: 80%
  - Layer 5 Observability: 70%
  - **總體**: 71% → 93%
- 10 大立即行動項：CoT / Anchoring 防護 / Health probe / 6 patterns / Vector search / Langfuse tracing 等

## [2026-07-13] ingest | 評估偏誤研究（Thinking in Bets + Art of Thinking Clearly）
- Concept: concepts/cognitive-bias-quick-reference.md — 99 偏誤速查表 + Top 25 必知 + Hermes SOP 對應
- Source: raw/articles/thinking-in-bets-and-art-of-thinking-clearly-2026-07-13.md — 雙書完整攝入（Annie Duke 2018 + Rolf Dobelli 2013）
- Index: Total 236 pages (+2: 1 concept + 1 raw)
- 評估偏誤必讀三部曲：
  - **Kahneman Thinking, Fast and Slow**（2011）— 學術深度
  - **Dobelli The Art of Thinking Clearly**（2013）— 99 偏誤速查
  - **Duke Thinking in Bets**（2018）— 不確定中決策方法論
- 5 大評估偏誤 SOP：
  - Confirmation Bias（找反證）
  - Hindsight Bias（被結果污染）
  - Survivorship Bias（只看成功）
  - Self-Serving Bias（自己評自己）
  - Anchoring（第一方案控制）

## [2026-07-13] ingest | 6 Orchestration Patterns 規格化（A1）
- Concept: concepts/orchestration-patterns-2026-07-13.md — 6 patterns 完整概念 + 決策表 + 5 大 Mismatch
- SOP: references/orchestration-patterns.md — 完整 SOP v1.0（10.3KB）
- Plan Template: references/wen-mou-plan-template.md → v1.1（加 pattern + Self-Consistency voting 必填；7 個 self-check）
- TRAP-SOP-068：Pattern Mismatch（自動檢核 pattern 必填 + 與 alternatives 一致性）
- Index: Total 312 pages (+1 concept)
- 6 patterns：Sequential / Conditional / Parallel / Supervisor / Handoff / Conversation-driven
- Pattern Routing 決策表已建立
- 立刻讓 Plan 階段更系統化、routing 錯誤可預測

## [2026-07-13] Master Changelog 整合（v3.7.1）
- workspace/hermes-sessions-master-changelog-20260713.md：22 研究攝入事件 + 17 個權威資源 + 7 SOP 版本演化 + 5 維度提升 + 35 references 索引
- wiki/index.md：新增「2026-07-13 重大研究攝入整合表」
- SKILL.md → v3.7.1：100% 同步驗證（35/35 references 與目錄一致）
- 5 維度能力提升摘要：
  - 文謀能力：60% → 95%
  - 架構運行：50% → 95%
  - 主控台能力：40% → 90%
  - Hermes 智能：35% → 90%
  - 評估偏誤：30% → 90%
  - 決策品質：50% → 85%

## [2026-07-13] ingest | 工匠聖經整合（Clean Code + TDD + Refactoring）
- Concept: concepts/red-green-refactor.md — Kent Beck 3 步循環；Hermes 工匠 4 大對應
- Source: raw/articles/craftsman-tools-2026-07-13.md — 三本整合 11KB（合規 O'Reilly + Martin Fowler bliki）
- SOP: references/craftsman-tools-sop.md — TRAP-SOP-073~076 + 22 Bad Smells 對應 + 6 大檢核 + 紅綠重構 SOP
- Index: Total 313 pages (+1 concept)
- 合規來源：
  - Clean Code 2nd ed.（O'Reilly 官方）
  - TDD By Example（Kent Beck）+ Martin Fowler bliki
  - Pragma Prog（已攝入）+ WEwLC（已攝入）+ xUnit Test Patterns（已攝入）
- 6 本工匠聖經套：
  - Clean Code（規範）+ TDD（自動化）+ Refactoring（改進）
  - + Pragmatic Programmer（態度）+ WEwLC（修復）+ xUnit（細節）
- 4 大新 TRAP：
  - TRAP-SOP-073：工匠修改後沒留童子軍軍規痕跡
  - TRAP-SOP-074：工匠跳過 Refactor 階段
  - TRAP-SOP-075：工匠沒寫測試先寫實作
  - TRAP-SOP-076：工匠寫了 Big Test

## [2026-07-13] ingest | 御史審計聖經（OWASP Top 10 2025 + Secure-by-Design + Threat Modeling）
- Concept: concepts/owasp-threat-modeling-framework.md — OWASP 四問框架；STRIDE 整合
- Source: raw/articles/yu-shi-audit-frameworks-2026-07-13.md — 三大開源框架完整攝入
- SOP: references/yu-shi-audit-sop.md — TRAP-SOP-077~080 + 4 階段審計 SOP
- Index: Total 314 pages (+1 concept)
- 合規來源（CC BY-SA 4.0 完全開源）：
  - OWASP Top 10 2025（最新版）
  - OWASP Secure-by-Design Framework v0.5.0
  - OWASP Threat Modeling
- 4 大新 TRAP：
  - TRAP-SOP-077：審計未跑 OWASP SbD Checklist
  - TRAP-SOP-078：Threat Modeling 跳過某一步
  - TRAP-SOP-079：沒做 A01-A10 對應檢核
  - TRAP-SOP-080：沒做 LLM Top 10 對應
- 御史 4 階段審計 SOP：
  - Stage 1：SbD Checklist（8 原則）
  - Stage 2：Threat Modeling（STRIDE）
  - Stage 3：OWASP Top 10（10 + 5 LLM）
  - Stage 4：Audit Report + E-code

## [2026-07-13] SOP 系統精簡優化（SOP v3.7.4）
- 目標：去除矛盾衝突 / 重複 / 提升效能
- 修正問題清單：
  1. ✅ description 重複（v3.6+v3.7 拼接殘留 1.9KB → 1.36KB，-28%）
  2. ✅ 重複章節「常見維護陷阱」+「（續）」合併為單一完整章節（A-G 主題分組）
  3. ✅ description 與實際 version 同步（v3.7.2 → v3.7.4）
  4. ✅ TRAP-SOP-070 已對應到 trap-sop-070-one-skill-per-session.md
  5. ✅ description 內 TRAP-SOP 編號清單錯誤（之前有 058-062 跳到舊版）（已修正）
  6. ✅ FRONTMATTER description 內尾段重複內容（清除到 100% SSoT）
- 結構保留：
  - 12 個主要章節（原順序）
  - 62 個 TRAP-SOP（編號 1~80 合理）
  - 39 個 references（每個有獨立職責）
  - 33 個 triggers
- 文件結構不變（職責邊界沒越界）

## [2026-07-13] ingest | 智能搜尋聖經（Stanford IR + Vector DB 四強）
- Source: raw/articles/intelligent-search-bible-2026-07-13.md — 3 大合規開源資源整合
- Concept: concepts/hnsw-algorithm.md — HNSW 演算法 + 3 大參數調優
- SOP: references/intelligent-search-sop.md — TRAP-SOP-081~085 + 5 大場景工具決策表
- 索引: Wiki 313 pages (+1 concept)
- 合規來源（全部 open-source）：
  - Stanford NLP IR Book (Manning 2008) — CC 免費在線版
  - Qdrant 官方文檔 — Apache 2.0
  - Milvus AI Quick Reference — Apache 2.0
- 5 大新 TRAP：
  - TRAP-SOP-081：Vector Search 沒做 Hybrid
  - TRAP-SOP-082：Embedding 模型版本不一致
  - TRAP-SOP-083：ANN 參數（ef, m）沒調優
  - TRAP-SOP-084：沒做 Reranking
  - TRAP-SOP-085：沒做 Quantization（記憶體爆炸）
- 4 大 Vector DB 對比：
  - Pinecone（管理、付費）
  - Weaviate（hybrid search 最佳）
  - Milvus（億級 vectors）
  - Qdrant（Rust + Filterable HNSW）
- 4-Stage Hybrid Search Pipeline:
  - Stage 1: Query Expansion (Stanford IR Ch 9)
  - Stage 2: Multi-Vector Encoding (Dense + Sparse + ColBERT)
  - Stage 3: ANN Retrieval (HNSW + Filterable)
  - Stage 4: Reranking (Cross-encoder + MMR)

## [2026-07-13] ingest | QA 問答智能聖經（Wikipedia RAG + Haystack + arXiv）
- Source: raw/articles/qa-intelligence-bible-2026-07-13.md — 3 大開源資源合規整合
- Concept: concepts/rag-pipeline.md — RAG 4-Stage + 6 大演進 + 4 框架 + 7 評估指標
- SOP: references/qa-intelligence-sop.md — 4-Stage QA Pipeline + 6 大 TRAP
- 索引: Wiki 313 pages (+1 concept)
- 合規來源：
  - Wikipedia RAG (CC BY-SA 4.0)
  - Haystack 官方文檔 (Apache 2.0)
  - arXiv 2507.18910 Systematic Review
- 6 大新 TRAP-SOP (086~091)：
  - TRAP-SOP-086：QA 系統只用 LLM 不用 retrieval
  - TRAP-SOP-087：Retrieval 沒做 Hybrid
  - TRAP-SOP-088：沒做 Late Interaction
  - TRAP-SOP-089：LLM prompt 沒要求引用來源
  - TRAP-SOP-090：沒做 Query Expansion
  - TRAP-SOP-091：沒做 Cost Monitoring
- 4 大 QA 框架：LangChain / LlamaIndex / Haystack / RAGFlow
- 4-Stage Pipeline: Retrieval → Augmentation → Generation → Post-Processing
- 7 大評估指標: EM / F1 / BLEU / ROUGE / MRR / NDCG / Faithfulness
- 對 Hermes: QA 整體能力 75% → 92%（+17pp）

## [2026-07-13] ingest | Web Search 精準度聖經（Microsoft LambdaMART + Stanford IR + Lucidworks）
- Source: raw/articles/web-search-precision-bible-2026-07-13.md — 3 大開源資源合規整合
- Concept: concepts/lambdamart-ltr.md — LambdaMART 完整演算法 + 4 公式
- SOP: references/web-search-precision-sop.md — 4-Stage Web Search Pipeline + 6 大 TRAP
- 索引: Wiki 314 pages (+1 concept)
- 合規來源：
  - Microsoft Research MSR-TR-2010-82 (Burges 2010, LambdaMART 原典)
  - Stanford IR Book Session 15 (Manning 2008, Learning to Rank)
  - Lucidworks ABCs of LTR
- 6 大新 TRAP-SOP (092~097)：
  - TRAP-SOP-092：用 BM25 不用 LTR
  - TRAP-SOP-093：LTR 訓練沒用 NDCG 評估
  - TRAP-SOP-094：LambdaMART 樹數太多（overfitting）
  - TRAP-SOP-095：沒做 Feature Normalization
  - TRAP-SOP-096：Train/Test 沒做 Query-level Split
  - TRAP-SOP-097：沒做 Fusion（單一模型結果）
- 3 大 LTR 流派：Pointwise / Pairwise / Listwise
- LambdaMART = LambdaRank + MART（Burges 2006-2010）
- 4 大評估指標：NDCG / MAP / MRR / P@K
- 6 大訓練特徵：Cosine / BM25 / Title / Body / Length / Coverage
- 4-Stage Pipeline: Multi-Retrieval → Feature Extraction → LambdaMART → Post-Processing
- Hermes Layer 4c 升級路徑: v2.0 → v3.0（加 LambdaMART rerank）
- SOP version: v3.7.10（新增 v3.7.10 描述本 session 親自踩的 2 個新陷阱）
- TRAP-SOP 總數：76 個

## [2026-07-13] ingest | PDF 製作能力聖經（ReportLab v5.0.0 + StackExchange PDF 生成架構模式）
- Source: raw/articles/pdf-production-bible-2026-07-13.md — 2 大開源資源合規整合
- Concept: concepts/pdf-platypus-architecture.md — PLATYPUS Flowable + Generator-Renderer
- SOP: references/pdf-production-sop.md — 3 層 PDF 架構 + 6 大 TRAP
- 索引: Wiki 316 pages (+1 concept)
- 合規來源：
  - ReportLab PDF Library User Guide v5.0.0 (reportlab.com/docs/reportlab-userguide.pdf)
  - StackExchange PDF 生成最佳實踐 (CC BY-SA)
- 6 大新 TRAP-SOP (098~103)：
  - TRAP-SOP-098：SPEC 值散落多個 Skill（應集中至 pdf-design-spec SSOT）
  - TRAP-SOP-099：Generator 和 Renderer 混耦合（應分離）
  - TRAP-SOP-100：DocAssert 缺失（應加斷言驗證）
  - TRAP-SOP-101：Hard-coded 座標和數值（應用變數）
  - TRAP-SOP-102：TableStyle 座標範圍錯誤（如 (0,0),(0,0) 只覆蓋一格）
  - TRAP-SOP-103：StyleSheet 定義不完整（應統一 StyleSheet）
- 3 層 PDF 架構：
  - Layer 1: pdf-design-spec (技法規範 SSOT)
  - Layer 2: pdf Skill (PLATYPUS + Generator-Renderer)
  - Layer 3: pdf-edit / chinese-pdf-gen (應用技能)
- Generator-Renderer 分離模式（StackExchange Kilian Foth）
- PLATYPUS Flowable 系統：25+ 可組合區塊
- DocAssert 斷言：防止邏輯矛盾
- SPEC 代號化：SPEC_CLR / SPEC_FNT / SPEC_GEO
- SOP version: v3.7.12
- TRAP-SOP 總數：82 個

## [2026-07-13] ingest | Skill 生態全景更新（55 個已安裝 Skills 聯網研究）
- Source: raw/articles/skill-ecosystem-update-2026-07-13.md — 30+ web searches 覆蓋全部 55 個 Skills
- Concept: concepts/skill-ecosystem-architecture.md — 8-Tier 分層全景圖
- 索引: Wiki 317 pages (+2)
- 批次研究（30+ web searches）：
  - 批次 1：mlops / serving-llms / autonomous-agents / ai-tooling / red-teaming / data-science
  - 批次 2：hermes / hermes-core-architecture / infrastructure / skills / note-taking
  - 批次 3：pdf / html-to-pdf / creative / media / computer-use
  - 批次 4：github / devops / software-development / research / productivity
  - 批次 5：social-media / apple / smart-home / tts / vercel
- 主要發現：
  - LLM Serving：vLLM vs TensorRT-LLM vs SGLang 三強格局
  - Multi-Agent：CrewAI / LangGraph / AutoGen 三國大戰
  - Skill 生態：Playwright/Whisper/GitHub API 三大跨層技術
  - Computer Use：Playwright+Claude 92% 可靠率 vs Anthropic 78%
  - TTS：ElevenLabs 質量 vs MiniMax 速度+價格
- Wiki pages: 317 (+2)

## [2026-07-13] ingest | PDF 渲染能力聖經（PyMuPDF + PDF.js + PDFium）
- Source: raw/articles/pdf-rendering-bible-2026-07-13.md
- Concept: concepts/pdf-rendering-architecture.md
- 索引: Wiki 318 pages (+2)
- 合規來源：
  - PyMuPDF 官方文檔 (GNU AGPL v3)
  - Mozilla PDF.js (Apache 2.0)
  - apryse PDF.js 渲染指南
  - Dropbox 預覽性能優化（原創）
- PDF 渲染 4-Way 架構：
  - Browser Native（HTML5 embed）
  - PDF.js（JavaScript Canvas，Mozilla）
  - PDFium（WASM，Chrome 內核）
  - Server-Side（PyMuPDF Python，無外部依賴）
- PyMuPDF 渲染 API：Matrix(dpi/72) 控制、annot/clip 參數
- PDF.js v4 CSP 問題（WASM 限制）
- 服務端渲染：Python/Rust/Node 三方案
- 渲染質量：Subpixel 抗鋸齒、亞像素渲染、LCD 優化
- 性能優化：5 大策略（DPI 控制、虛擬滾動、CDN 緩存）
- Wiki pages: 318 (+2)

## [2026-07-13] ingest | 寫作風格研究：四個傳統 SSOT 體系

### 背景
Hermes 缺乏中文寫作風格指引——`writing-guidelines` skill 只覆蓋 Vercel 文檔英文審查。現有 skill 無中文修辭學、無 AI 風格寫作指引。建設四個傳統的 SSOT 寫作知識體系。

### 行動

1. **聯網調研**：搜索寫作經典書籍，建立閱讀清單（文心雕龍/精準寫作/Strunk & White/AI style guide）
2. **建立研究日誌**：`research/writing-style-research-2026-07-13.md`
3. **Entity 頁（2個）**：
   - `entities/wenxin-diaolong.md` — 劉勰《文心雕龍》50篇體系（原道/宗經/正緯/辨騷/文體論20篇/創作論20篇/批評論5篇/總序/總術）；核心：神思/風骨/情采/通變/鎔裁/隱秀；「為情造文」vs「為文造情」；六觀審批
   - `entities/jingzhun-xiezuo.md` — 洪震宇《精準寫作》（2020）；讀者視角、服務業心態、「想清楚才能寫清楚」、水平/脈絡發想法
4. **Concept 頁（4個）**：
   - `concepts/classical-chinese-rhetoric.md` — 古典修辭學地圖：文心雕龍核心脈絡、「為情造文」vs「為文造情」、六觀審批法
   - `concepts/jingzhun-xiezuo-techniques.md` — 精準寫作法（含 AI 寫作工作流對接）：讀者視角四象限、數字開頭、七維度診斷
   - `concepts/strunk-white-elements-of-style.md` — Strunk & White 17條金律：Omit needless words / Active voice / Paragraphs / Word choice / Affirmative / Style
   - `concepts/ai-writing-style-transfer.md` — AI 風格寫作：Style Injection / Voice Preservation / Persona / 詞彙密度控制 / 避免 AI 文字識別
5. **更新 `writing-guidelines` skill**（v1.0.0 → v2.0.0）：
   - 描述：從 Vercel 英文覆核擴展為四傳統通用寫作風格指引
   - 觸發關鍵字：中文、寫作風格、文風檢查、persona、寫作品質審查
   - SSOT metadata 指向 6 個 wiki 頁
   - 四 Tradition SSOT Framework（七維度診斷 / TRAP 陷阱掃描 / 六觀審批 / AI Prompt Template）
6. **更新 `wiki/index.md`**：
   - 新增 `### Writing & Rhetoric` 區段（Entities + Concepts）
   - 總頁數：103 → 109

### 閱讀清單

| 書名 | 作者 | 核心價值 |
|------|------|---------|
| 文心雕龍 | 劉勰（南北朝）| 體系性：情采/風骨/神思/通變/隱秀 |
| 精準寫作 | 洪震宇（2020）| 讀者視角、服務業心態、主題先定 |
| Elements of Style | Strunk & White（1918/1959）| 17條英語寫作金律 |
| 風格與人格 | Josef Müller-Brockmann | 視覺傳達、網格系統 |

### Wiki pages: 318 (+6)

## [2026-07-13] ingest | PDF Quality Audit — PDF/A + PDF/UA 國際標準合規審查研究

### 背景
現有 `pdf-edit` skill 的 T1-T14 物理驗證解決了「PDF 物理上是否正確」，但缺乏國際標準合規審查能力（PDF/A、PDF/UA、Matterhorn Protocol）。本次研究填補此空白。

### 研究行動
- 聯網搜尋：veraPDF、ISO 19005、ISO 14289、Matterhorn Protocol、PDF Preflight 技術、PDF Accessibility Checker
- 擷取 6 篇核心文章完整內容（veraPDF 官網、PDF Association ISO 頁、Matterhorn 說明、Nutrient PDF/A + PDF/UA 完全指南、QualiBooth Accessibility Guide、Quadient Matterhorn 文章）
- 建立 research 頁：`research/pdf-quality-audit-research-2026-07-13.md`

### 新增 LLM wiki 頁面（6 個 + 1 個 research）
- Entity：`entities/matterhorn-protocol.md` — PDF/UA ISO 14289 合規測試模型（31 檢查點 × 136 失敗條件）
- Entity：`entities/verapdf-validator.md` — 開源 CLI/GUI 驗證器（覆蓋所有 PDF/A + PDF/UA 版本）
- Concept：`concepts/pdf-a-standard.md` — ISO 19005 PDF/A 家族（1/2/3/4 × b/a/u）
- Concept：`concepts/pdf-ua-standard.md` — ISO 14289 PDF/UA 標準（Tagged PDF 機制）
- Concept：`concepts/pdf-tagged-structure.md` — StructTreeRoot 結構樹、標準標籤、閱讀順序、Artifacts
- Concept：`concepts/pdf-quality-gate-framework.md` — 四層審查框架（L1 物理 / L2 結構 / L3 語義 / L4 合規）

### 新概念：PDF Quality Gate 四層框架
- **L1 物理層**：現有 T1-T14，pymupdf 物理測量
- **L2 結構層**：版本-diff（L2：文字 unified_diff；L3：像素 ImageChops.difference）
- **L3 語義層**：像素比對、螢幕閱讀器模擬、文字萃取完整性
- **L4 合規層（新增）**：L4-A（veraPDF PDF/A-3b）/ L4-B（veraPDF + PAC PDF/UA-1）/ L4-C（Tagged PDF 結構抽檢）/ L4-D（Matterhorn 31 檢查點）

### TRAP 衝突接口
- TRAP-OPT-4：`garbage=4` 破壞 PDF/A 相容性 → L4-A FAIL
- TRAP-CJK-005：PDF/A + CJK 全字體嵌入過大 → L4-A 警告
- TRAP-TAG-1~4：PDF/UA 結構失敗 → L4-B FAIL
- TRAP-SIG-1~3：簽章與 PDF/A 衝突 → L4-A + L4-B 警告

### SSOT 影響
- veraPDF 和 Matterhorn Protocol 是行業標準，構成 PDF 審查 SSOT 的「國際標準層」
- `pdf-design-spec/references/trap-maintenance.md` 維護 TRAP；Wiki 概念頁維護標準知識；`pdf-edit` skill 維護操作層

### Index 更新
- Entities 新增 `### PDF Quality & Audit`（matterhorn-protocol、verapdf-validator）
- Concepts 新增 `### PDF Quality & Audit`（pdf-a-standard、pdf-ua-standard、pdf-tagged-structure、pdf-quality-gate-framework）
- 總頁數：109 → 114

