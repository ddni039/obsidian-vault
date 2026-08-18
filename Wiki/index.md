# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: 2026-07-10 | Total pages: 80

## Entities
<!-- Alphabetical within section -->
- [[robert-bringhurst]] — Canadian typographer; author of *The Elements of Typographic Style* (1992, 1996)
- [[josef-albers]] — German-American artist; *Interaction of Color* (1963); Bauhaus/Yale; color relativity pioneer
- [[josef-muller-brockmann]] — Swiss designer; *Grid Systems in Graphic Design* (1968); Swiss Style pioneer
- [[ellen-lupton]] — American designer/curator; *Thinking with Type* (2004/2010/2024); AIGA Medal 2007
- [[edward-tufte]] — Statistician/visualization pioneer; *Visual Display* (1983), *Envisioning Information* (1990)
- [[josef-and-annin-albers-foundation]] — Non-profit preserving Josef & Anni Albers' artistic legacy (est. 1971)
- [[hermes-agent-version-history]] — Hermes Agent v0.2.0→v0.18.0 結構化版本歷史（2026-03 至 2026-07）

### Software Quality & Maintenance

- [[working-effectively-with-legacy-code]] — Feathers：Legacy Code = 無測試代碼；依賴斷裂、特徵測試、Seams 模型
- [[pragmatic-programmer]] — Hunt/Thomas：軟體工藝態度；Tip 24 修復不workaround、Tip 32 先正確再快
- [[debug-it-paul-butcher]] — Butcher：四階段偵錯流程（重現→定位→決定修復→驗證）；bug 根因分類
- [[xunit-test-patterns]] — Meszaros：測試壞味道分類；Test Double（Dummy/Stub/Spy/Mock/Fake）；四階段結構
- [[software-testing-and-analysis-pezze-young]] — Pezzè/Young：靜態/動態分析；NIST Bug Cost 研究；測試策略框架（2026-07-10 新增）
- [[automation-pipelines-martinfowler]] — Martin Fowler：持續整合定義；CI 核心實踐；建構 Pipeline 階段設計（2026-07-10 新增）

- [[anthropic-ai-agents-framework]] — Anthropic官方：AI Agent架構模式（Tool Use/Reflection/Planning/Multi-Agent）
- [[raft-consensus-algorithm]] — Raft共識演算法：Leader Election + Log Replication + Safety
- [[agentic-design-patterns-2025]] — Dao et al. 2025：18種Agentic Design Patterns系統理論框架
- [[agentic-ai-software-architecture-evolution]] — arXiv 2025：LLM Agents → Agentic AI → Agentic Communities三層演進
- [[agentic-communities-paper]] — arXiv 2025：Agentic Communities設計模式三層分類
- [[markus-winand-sql-performance-explained]] — Markus Winand：SQL效能調校（索引/執行計劃/JOIN/WHERE）
- [[martin-kleppmann-ddia]] — Martin Kleppmann：分散式系統聖經（複製/分區/共識/串流）
- [[stephane-faroult-art-of-sql]] — Faroult：SQL策略性寫作、反模式、查詢結構
- [[alan-beaulieu-learning-sql]] — Alan Beaulieu：SQL基礎（CRUD/交易/Schema設計）

- [[claude-code]] — Anthropic官方CLI程式碼agent，v2.1.169
- [[codex]] — OpenAI官方CLI程式碼agent
- [[andrej-karpathy]] — AI研究者，LLM coding guidelines作者
- [[multica-ai]] — GitHub組織，封裝Karpathy guidelines成CLAUDE.md
- [[agency-agents]] — 232 agents/16 divisions多專家agent系統，18.1k forks
- [[agency-engineering-division]] — 30個工程專業agent（前端/後端/AI/DevOps等）
- [[agency-frontend-developer]] — 前端開發專家，React/Vue/Angular，Core Web Vitals

## Concepts

## Agents
- [[agentic-reflection-pattern]] — Agent自我批判與改進輸出的迴圈
- [[agentic-tool-use-pattern]] — Agent呼叫外部工具/API擴展能力
- [[agentic-planning-pattern]] — Agent將複雜目標分解為有序子任務
- [[agentic-multiagent-pattern]] — 多Agent協調解決單一Agent無法處理的問題

## Distributed Systems
- [[raft-leader-election]] — Raft心跳式Leader選舉，Term編號保障安全
- [[raft-log-replication]] — Leader接受客戶端請求，複製到多數派後提交
- [[raft-safety]] — Raft狀態機安全：已提交日誌永不回滾
- [[data-replication]] — 單點/多點/無Leader複製策略與衝突解決
- [[data-partitioning]] — 分片策略：鍵範圍/雜湊/複合分区
- [[distributed-transactions]] — ACID vs BASE、2PC/Sagas分散式交易
- [[consistency-models]] — 線性一致性→最終一致性好窄
- [[stream-processing]] — 串流處理：Kafka/Flink、Watermark、視窗

## Database
- [[database-index]] — B-tree索引結構、列選擇性、索引類型
- [[sql-execution-plan]] — EXPLAIN輸出分析、掃描類型、WHERE→存取路徑
- [[sql-join-strategies]] — Nested Loop/Hash/Merge JOIN演算法與代價
- [[sql-covering-index]] — 涵蓋索引實現Index-Only Scan
- [[sql-strategic-writing]] — 聲明式SQL思維，避免程序化寫法
- [[sql-anti-patterns]] — Faroult黑暗法則：NULL恐懼/指標分散/更新失控
- [[sql-query-structure]] — CTE、子查詢與JOIN選擇、代價估算
- [[sql-fundamentals]] — SELECT執行順序、聚合、視窗函數
- [[sql-data-modification]] — INSERT/UPDATE/DELETE與交易隔離級別
- [[sql-schema-design]] — 正規化、PK/FK/視圖、觸發器

- [[ai-agent]] — AI Agent定義、核心元件、生態系趨勢
- [[typographic-scale]] — Traditional type size scale (Nonpareil→Great Primer, Bringhurst)
- [[typographic-rhythm-proportion]] — 10/12 leading, 66-char line, M/4 word space, φ=1.618
- [[typographic-ligatures]] — ff/fi/fl/ffi/ffl ligatures; true italic vs sloped roman
- [[typographic-page-design]] — Page proportions, margins, textblock (monophonic/polyphonic)
- [[color-relativity-principle]] — Albers: color perceived in context, never isolation; 1+1=3 emergent meaning
- [[tufte-data-ink-principle]] — Maximize data-ink ratio; eliminate chartjunk; Lie Factor ≈ 1.0
- [[tufte-envisioning-information]] — Layering, micro/macro, small multiples, eye-span constraint
- [[grid-systems-graphic-design]] — Müller-Brockmann: baseline grid 13pt, modular grids, grid as tool not constraint
- [[hierarchical-redundancy]] — Lupton: size+weight+spacing = three independent signals for same level
- [[type-scale-golden-ratio]] — φ=1.618 type scale: 34/21/13/8pt; traditional Bringhurst scale
- [[karpathy-think-before-coding]] — 不假設、不隱藏困惑、主動揭露取捨
- [[karpathy-simplicity-first]] — 最小化代碼，沒有投機性功能
- [[karpathy-surgical-changes]] — 只碰需要碰的，清理自己造成的爛攤子
- [[karpathy-goal-driven-execution]] — 定義成功標準，循環驗證直到確認
- [[agency-multi-agent-architecture]] — Agency 232-agent 分層架構分析
- [[mcp-model-context-protocol]] — Anthropic 開放標準，AI 與工具/數據的安全雙向連接
- [[hermes-learning-loop]] — Hermes 閉環學習系統，跨 session 自進化的核心
- [[hermes-skills-system]] — Hermes 程序性記憶，將經驗封裝為可複用 Skills
- [[hermes-messaging-gateway]] — Hermes 20+ 平台統一消息系統
- [[hermes-hindsight]] — Hermes 長期記憶插件，知識圖譜 + 觀測性記憶
- [[codex-obsidian-integration]] — Codex + Obsidian vault + MCPVault 讀寫第二大腦

## Comparisons
- [[karpathy-vs-hermes-tri-role]] — Karpathy guidelines 與 Hermes 三角色對齊分析
- [[agency-vs-hermes-tri-role]] — Agency 水平specialization vs Hermes 垂直治理

## Raw
- [[raw/papers/bringhurst-elements-of-typographic-style-2ed.md]] — Robert Bringhurst, *The Elements of Typographic Style* (2nd ed. 1996), Hartley & Marks
- [[raw/papers/josef-albers-wikipedia-2026.md]] — Josef Albers Wikipedia summary; *Interaction of Color* (1963)
- [[raw/papers/josef-muller-brockmann-wikipedia-2026.md]] — Josef Müller-Brockmann Wikipedia; *Grid Systems* (1968/1981)
- [[raw/papers/ellen-lupton-wikipedia-2026.md]] — Ellen Lupton Wikipedia; *Thinking with Type* (3rd ed. 2024)
- [[raw/papers/edward-tufte-wikipedia-2026.md]] — Edward Tufte Wikipedia; *Visual Display* (1983), *Envisioning Information* (1990)
- [[raw/articles/karpathy-llm-wiki-2026.md]] — Karpathy LLM Wiki 原始來源
- [[raw/articles/agency-agents-readme-2026.md]] — Agency Agents README 原始來源
- [[raw/articles/nous-hermes-agent-repo-2026.md]] — NousResearch/hermes-agent GitHub 原始來源（v0.18.0）
- [[raw/articles/hermes-hindsight-readme-2026.md]] — Hindsight Memory Provider README 原始來源
- [[raw/articles/codex-obsidian-integration-2026.md]] — Codex 懶人包：GitHub + Obsidian MCPVault 整合

## Queries

## Visual Art & Design (2026-07-08)

### Entities (Books)

| Entity | Author | Year | Tags |
|--------|--------|------|------|
| [[dashboard-design-few]] | Stephen Few | 2013 | data-visualization, dashboard |
| [[interaction-of-color-albers]] | Josef Albers | 2013 | color-theory, perception |
| [[non-designers-design-book]] | Robin Williams | 2014 | design-principles, CRAP |
| [[shape-of-design]] | Frank Chimero | 2012 | design-philosophy, craft |
| [[signs-symbols-frutiger]] | Adrian Frutiger | 1989 | semiotics, wayfinding |
| [[universal-methods-design]] | Hanington & Martin | 2012 |
| [[thinking-with-type-lupton]] | Ellen Lupton | 2022 | ux-research, methodology |

### Concepts

| Concept | Summary |
|---------|---------|
| [[visual-hierarchy]] | 視覺層級引導眼睛順序 |
| [[contrast-repetition-alignment-proximity]] | CRAP四大原則（Robin Williams）|
| [[color-relativity]] | Albers色彩相對性理論 |
| [[grid-systems]] | 網格系統（瑞士國際主義）|
| [[typographic-scale]] | 字體大小比例階梯 |
| [[data-ink-ratio]] | Tufte數據墨水比 |
| [[ Gestalt-principles]] | 完形原則：接近/相似/封閉/連續 |
| [[signage-wayfinding]] | Frutiger導引系統設計 |
| [[dashboard-cognitive-load]] | 儀表板認知負擔控制 |
| [[semiotics-visual-language]] | 符號學視覺語言 |
| [[design-research-methods]] | 100種研究驅動設計方法 |
| [[visual-narrative]] | Chimero設計敘事框架 |
| [[software-testing-fundamentals]] | 軟體測試核心概念：Oracle問題、測試金字塔、白盒/黑盒 |
| [[debugging]] | 軟體偵錯技術：wolf fence、delta debugging、git bisect |
| [[software-testing-maintenance]] | 軟體維護策略：legacy code依賴斷裂、特徵測試、影響評估 |
| [[legacy-code-strategies]] | Feathers 方法論：Seams 模型、Characterisation Tests、九種依賴斷裂技術（2026-07-10 新增）|
| [[pragmatic-programmer-tips]] | Hunt & Thomas 20 Tips 精煉：DRY、Eliminate Effects、Debugging Mindset（2026-07-10 新增）|
| [[xunit-test-patterns]] | Meszaros 測試壞味道與重構：Erratic/Fragile Test、Test Double、Test Data Builder（2026-07-10 新增）|

## Books