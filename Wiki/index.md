# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: 2026-07-13 | Total pages: 72 + 1 archive log

## Entities
<!-- Alphabetical within section -->
|- [[chip-huyen]] — ML/AI author; *Designing ML Systems* (2022), *AI Engineering* (2025, O'Reilly); coined LLMOps; MIT licensed repo (16k stars)
|- [[designing-ml-systems-book]] — Chip Huyen (O'Reilly 2022); holistic ML systems design; reliability/scalability/maintainability/adaptability requirements
|- [[designing-multi-agent-systems-book]] — Victor Dibia (2025)：*Designing Multi-Agent Systems*，15章395頁，picoagents framework，5種語言翻譯
|- [[victor-dibia]] — Microsoft Research，AutoGen/AutoGen Studio 作者；2025 Amazon AI Agents #1 New Release
|- [[picoagents]] — 從零實作的 lightweight multi-agent framework（Apache-2.0，703⭐）
|- [[m1-parallel-framework]] — Microsoft Research arXiv 2507.08944；並行多 plan 執行，2.2× speedup
|- [[agent-harness]] — 包圍 LLM 的 scaffolding（Adnan Masood 2026）；6 大職責；`{Agent} = {Model} + {Harness}`
|- [[agent-control-plane]] — 治理 + 編排 + 觀測統一層（Activant 2026）；88% agent 專案未達生產的根因
|- [[metr]] — Model Evaluation and Threat Research；2025-2026 AI 生產力 RCT 與 Survey 研究
|- [[accelerate-book]] — **Accelerate 原典**（Nicole Forsgren, Jez Humble, Gene Kim, 2018）；Shingo Award；24 個關鍵能力 + 4 個關鍵指標 + Westrum 文化模型；DevOps Handbook 的理論基礎；Hermes 4/4 達 Elite
|- [[strategic-thinking-reading-list]] — **文謀閱讀地圖**（McKinsey 2026 96 本 + OfferZen 20 本 + DEV.to 7 本 整合）；5 大文謀能力維度；3 本聖經（DDIA / Thinking Fast / Hard Parts）
|- [[chaos-engineering]] — **Chaos Engineering 雙書攝入**（Casey Rosenthal + Nora Jones O'Reilly 2020；Mikolaj Pawlikowski Manning 2021）；Netflix 起源；Simian Army；Game Day + Continuous Chaos；Hermes 主控台必備驗證工具
|- [[hermes-intelligence-5-layer-architecture]] — **Hermes 智能 5 層架構評估**（基於 EITT 2026 Agent Anatomy）；Layer 1 LLM / 2 Reasoning / 3 Tools / 4 Memory / 5 Observability；現狀 71% → 目標 93% 改進路徑
|- [[the-devops-handbook-book]] — Gene Kim 等 4 位 DevOps 創辦人合著（2016）；23 章 + 6 部；3 Ways + CALMS 框架聖經
|- [[vinyl-cache]] — **Vinyl Cache**（formerly Varnish Cache）；HTTP accelerator / caching reverse proxy；BSD license；VCL DSL + Health Probe + Grace Mode；Hermes MCP health monitoring 直接對應
- [[robert-bringhurst]] — Canadian typographer; author of *The Elements of Typographic Style* (1992, 1996)
- [[josef-albers]] — German-American artist; *Interaction of Color* (1963); Bauhaus/Yale; color relativity pioneer
- [[josef-muller-brockmann]] — Swiss designer; *Grid Systems in Graphic Design* (1968); Swiss Style pioneer
- [[ellen-lupton]] — American designer/curator; *Thinking with Type* (2004/2010/2024); AIGA Medal 2007
- [[edward-tufte]] — Statistician/visualization pioneer; *Visual Display* (1983), *Envisioning Information* (1990)
- [[josef-and-annin-albers-foundation]] — Non-profit preserving Josef & Anni Albers' artistic legacy (est. 1971)
- [[hermes-agent-version-history]] — Hermes Agent v0.2.0→v0.18.0 結構化版本歷史（2026-03 至 2026-07）

### Writing & Rhetoric

- [[wenxin-diaolong]] — 劉勰《文心雕龍》（南北朝）；「體大思精」；50篇：文體論＋創作論＋批評論；核心：情采/風骨/神思/通變/隱秀
- [[jingzhun-xiezuo]] — 洪震宇《精準寫作：寫作力就是思考力》（2020）；讀者視角、服務業心態、主題發想法、數字開頭

### PDF Quality & Audit

- [[matterhorn-protocol]] — PDF/UA ISO 14289 合規測試模型：31 檢查點 × 136 失敗條件（89 可自動 / 47 需人工）；PAC 工具核心
- [[verapdf-validator]] — veraPDF：行業標準開源 PDF/A + PDF/UA 驗證器（CLI/GUI）；覆蓋所有 ISO 19005 + ISO 14289 版本

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
- [[parallel-multi-agent-execution]] — M1-Parallel 框架：early termination (2.2× speedup) vs aggregation；Hermes `delegate_task` 對應
- [[pev-loop]] — Plan-Execute-Verify 三階段循環；Reasoning Sandwich；Hermes C/B/H/E 五角色對應
- [[progressive-disclosure-skills]] — Anthropic Skills 三階段揭露（metadata → SKILL.md → references/）；Hermes skill 系統對應
- [[ai-coding-productivity-paradox]] — AI 工具「覺得快但實測可能慢」的 Paradox；METR 2025 RCT vs Benchmark 矛盾
- [[perception-vs-reality-gap]] — Perception vs Reality 落差（METR RCT：高估 40 個百分點）；自我報告不可信
- [[slos-error-budget]] — SLI/SLO/SLA 三層 + Error Budget 機制；Hermes 50k/80k/120k 已對應
- [[eliminating-toil]] — Toil 自動化 6 策略；Hermes 並聯 SOP 7.5× speedup 案例
|- [[sre-site-reliability-engineering]] — Google SRE（2003）；5 大核心原則（Embracing Risk / SLO / Toil / Monitoring / Postmortem）；Hermes 已對應 95%+；Catchpoint 20 書單收錄
|- [[three-ways-devops]] — DevOps 三大原則：Flow / Feedback / Continual Learning；Hermes 三軸對應
|- [[calms-framework]] — CALMS 5 支柱（Culture/Automation/Lean/Measurement/Sharing）；Hermes 已實作 90%
- [[dora-four-key-metrics]] — DORA 4 大關鍵指標（DF/LT/CFR/MTTR）；Hermes 4/4 達 Elite
|- [[vcl-varnish-configuration-language]] — VCL DSL：VCL → C → .so → hot reload；Hook lifecycle（vcl_recv→vcl_hash→vcl_miss→...）；VMOD plugin 生態
|- [[system-1-system-2-thinking]] — Kahneman 兩個思維系統：System 1（快/直覺/95%）vs System 2（慢/邏輯/5%）；8 大認知偏誤；文謀應用決策品質
|- [[control-plane-pattern-declarative-reconciliation]] — Control Plane Pattern：Declarative 期望狀態 + Reconciliation Loop + State Store；Hermes 主控台 1.0→2.0 演進核心
|- [[chain-of-thought-reasoning]] — Chain-of-Thought（Wei 2022，32540 citations）；Zero-shot CoT → Tree-of-Thoughts → ReAct → Self-Refine 演進樹；Hermes 文謀 CoT 應用
|- [[cognitive-bias-quick-reference]] — **Cognitive Bias Quick Reference**（Dobelli 99 偏誤 + Kahneman + Duke 三部曲）；5 大必查偏誤 SOP（Confirmation/Hindsight/Survivorship/Self-Serving/Anchoring）；評估前必跑
|- [[orchestration-patterns-2026-07-13]] — **6 Orchestration Patterns**（Dibia 2025 + EITT 2026）：Sequential / Conditional / Parallel / Supervisor / Handoff / Conversation-driven；決策表；5 大 Mismatch 情境
|- [[mlops-systems-design]] — DMLS Ch2: reliability/scalability/maintainability/adaptability; iterative ML development
|- [[data-distribution-shifts]] — DMLS Ch8: covariate/label shift, concept drift; detection and remediation
|- [[training-data-lifecycle]] — DMLS Ch4: sampling, labeling (human/weak supervision), class imbalance, augmentation
- [[openai-prompt-engineering]] — OpenAI官方prompt工程：Message Roles/Instructions/Fewshot/RAG/Prompt Caching
- [[reasoning-models]] — Reasoning vs GPT模型：內部CoT/代價/場景選擇；Anthropic Adaptive Thinking
- [[prompt-engineering]] — Lilian Weng 2023：Zero/Few-shot/CoT/Self-consistency/自動Prompt設計/Toolformer

### Writing & Rhetoric

- [[classical-chinese-rhetoric]] — 古典修辭學地圖：文心雕龍50篇核心脈絡（神思/風骨/情采/通變/鎔裁/隱秀）；「為情造文」vs「為文造情」；六觀審批法
- [[jingzhun-xiezuo-techniques]] — 精準寫作技法手冊：讀者視角、服務業心態、主題發想（水平/脈絡）、數字開頭、砍掉重點；AI寫作工作流對接
- [[strunk-white-elements-of-style]] — Strunk & White《Elements of Style》：17條英語寫作金律、主動語態，省詞、肯定形式；應用於AI英文輸出
- [[ai-writing-style-transfer]] — AI風格寫作：Style Injection、Persona引導、Voice Preservation、詞彙密度控制（<66%）；避免AI文字識別

### Visual Design & Typography
>- 2026-07-13 新增 Wilke *Fundamentals of Data Visualization*（免費全書在線：clauswilke.com/dataviz/）

- [[wilke-color-scales]] — **Wilke 色彩四用途**：Qualitative（類別）/ Sequential（順序）/ Diverging（發散）/ Accent（強調）；Okabe-Ito + Viridis 色盲安全色盤
- [[wilke-figure-design]] — **Wilke 圖表設計**：標題 assertion 原則、表格無垂直線、data-context 平衡、small multiples Y軸一致

### PDF Quality & Audit

- [[pdf-a-standard]] — PDF/A（ISO 19005）長期保存標準家族：PDF/A-1/2/3/4，b/a/u 層級；veraPDF 行業驗證；核心約束：字體嵌入/無外部引用/無加密/XMP強制
- [[pdf-ua-standard]] — PDF/UA（ISO 14289）無障礙標準：Tagged PDF 機制、H1-H6 層次、Alt text、閱讀順序；PDF/UA-1（2014）vs PDF/UA-2（2024）
- [[pdf-tagged-structure]] — Tagged PDF 結構樹（StructTreeRoot）：H/P/L/Table/Figure 標準標籤；閱讀順序與視覺順序分離；Artifacts 裝飾性元素
- [[pdf-quality-gate-framework]] — PDF Quality Gate 四層審查框架：L1 物理（T1-T14）/L2 結構（版本-diff）/L3 語義（像素比對）/L4 合規（veraPDF + Matterhorn）

## LLM Engineering (2026-07-11)
- [[llmops]] — LLM Operations: production challenges (cost/latency/eval/versioning) systematized by Chip Huyen
- [[prompt-engineering-production]] — Systematic prompt techniques: fewshot/CoT/self-consistency/versioning
- [[embedding-vector-database]] — LLM embeddings + vector DBs; 2023 "year of vector DBs"; Chroma ecosystem
- [[llm-agents-tool-use]] — LLM agents via tools (SQL/search/browser/bash) + control flows (sequential/parallel/if/for)
- [[talk-to-your-data]] — #1 enterprise use case: NL→DB query→NL; RAG pipeline; defensibility concerns
- [[finetuning-vs-prompting]] — Tradeoffs: prompting (flexible, high inference cost) vs finetuning (cheap, slow to change)
- [[ai-engineering-framework]] — Chip Huyen's AIE framework: 3-part structure (Eval → Adaptation → Infrastructure), 10 key questions
- [[ai-evaluation]] — AI evaluation methodology: perplexity, AI-as-a-Judge, comparative evaluation, eval pipeline design
- [[rag-and-agents]] — RAG (retrieve→generate) and Agents (planner+tools+memory); RAG is a special case of agents
- [[inference-optimization]] — Inference optimization: TTFT/TPOT, quantization, KV cache, batching, parallelism
- [[anthropic-prompt-engineering]] — Anthropic官方prompt工程：XML結構/Examples/Role/Thinking/Agentic Systems
- [[openai-prompt-engineering]] — OpenAI官方prompt工程：Message Roles/Instructions/Fewshot/RAG/Prompt Caching
- [[reasoning-models]] — Reasoning vs GPT模型：內部CoT/代價/場景選擇；Anthropic Adaptive Thinking
- [[anthropic-adaptive-thinking]] — Anthropic Adaptive Thinking：動態思考深度控制（effort參數），取代budget_tokens
- [[prompt-engineering]] — Lilian Weng 2023：Zero/Few-shot/CoT/Self-consistency/自動Prompt設計/Toolformer
- [[llm-agent]] — Lilian Weng 2023：LLM Agent三元件（Planning/Memory/Tool Use）+ ReAct/Reflexion/MRKL

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
|- [[dmls-vs-aie-vs-llmops]] — DMLS/AIE/LLMOps 三部曲知識邊界：互補無衝突，AIE 吸收 LLMOps
|- [[dmls-vs-hermes-architecture]] — DMLS 11章框架 vs Hermes 實際架構：Skills=Feature Store缺口、LLM時代新解法
- [[prompt-engineering-cross-provider]] — Chip Huyen vs Anthropic vs OpenAI prompt工程方法論全面對比（2023→2026演進）
- [[karpathy-vs-hermes-tri-role]] — Karpathy guidelines 與 Hermes 三角色對齊分析
- [[agency-vs-hermes-tri-role]] — Agency 水平specialization vs Hermes 垂直治理

## Raw
- [[raw/articles/designing-multiagent-systems-book-2026-07-13.md]] — Victor Dibia 2025《Designing Multi-Agent Systems》書籍網站內容
- [[raw/articles/m1-parallel-arxiv-2026-07-13.md]] — Microsoft Research arXiv 2507.08944 論文內容
- [[raw/articles/agent-harness-engineering-2026-07-13.md]] — Adnan Masood《Agent Harness Engineering》核心 7 大 takeaways
- [[raw/articles/agent-control-plane-activant-2026-07-13.md]] — Activant 2026 控制平面研究（95% 試點失敗、88% 未達生產）
- [[raw/articles/agent-skills-anthropic-course-2026-07-13.md]] — Andrew Ng × Anthropic Agent Skills L0-L8 課程筆記
- [[raw/articles/metr-2025-rct-developer-productivity-2026-07-13.md]] — METR 2025 RCT：AI 讓資深開發者慢 19% 的震撼研究
- [[raw/articles/metr-2026-uplift-survey-2026-07-13.md]] — METR 2026 追蹤（Uplift Update + AI Usage Survey）
- [[raw/articles/ai-era-software-engineering-books-2026-07-13.md]] — AI 時代 SE 必讀書單（Clean Code / DDIA / Pragmatic Programmer）
- [[raw/articles/google-sre-book-2026-07-13.md]] — Google SRE Book 完整 34 章目錄 + 5 大核心原則
- [[raw/articles/20-essential-sre-books-catchpoint-2026-07-13.md]] — Catchpoint 整理 20 本 SRE 必讀書單（Accelerate / Phoenix Project / DevOps Handbook）
- [[raw/articles/accelerate-book-2026-07-13.md]] — Accelerate 原典（IT Revolution 官方 + 第三方摘要）；24 個關鍵能力 + 4 個關鍵指標 + Westrum 文化模型
- [[raw/articles/strategic-thinking-reading-list-2026-07-13.md]] — 文謀閱讀地圖（McKinsey 2026 96 本 + OfferZen 20 本 + DEV.to 7 本 整合）；5 大能力維度；閱讀順序建議
- [[raw/articles/chaos-engineering-books-2026-07-13.md]] — Chaos Engineering 雙書完整攝入（Rosenthal+Jones O'Reilly 2020；Pawlikowski Manning 2021）；Simian Army；4 大實驗原則；Hermes Chaos 對應清單
- [[raw/articles/hermes-intelligence-reading-map-2026-07-13.md]] — Hermes 智能閱讀地圖（EITT 2026 + Victor Dibia + Future AGI 整合）；5 層架構；Chain-of-Thought；10 大行動項
- [[raw/articles/thinking-in-bets-and-art-of-thinking-clearly-2026-07-13.md]] — 評估偏誤雙書（Annie Duke Thinking in Bets + Rolf Dobelli Art of Thinking Clearly 99 偏誤）；決策品質三部曲
- [[raw/articles/kubernetes-control-plane-2026-07-13.md]] — Kubernetes 2026 完整架構（CloudOptimo 合規 blog）；Control Plane + Worker Nodes + CRD + Operator + Admission Control
- [[raw/articles/the-devops-handbook-2026-07-13.md]] — The DevOps Handbook 23 章完整目錄 + 3 Ways + CALMS（基於 IT Revolution 官方 Intro PDF）
- [[raw/articles/dora-2024-state-of-devops-2026-07-13.md]] — DORA 2024 報告核心發現 + 4 大關鍵指標 + AI 雙刃劍
- [[raw/articles/vinyl-cache-official-2026-07-13.md]] — Vinyl Cache 官方文件（BSD license）；Users Guide + Reference Manual + VMODs；v9.0.0
- [[raw/articles/designing-ml-systems-summary-2026-07-11.md]]
|- [[raw/articles/designing-ml-systems-mlops-tools-2026-07-11.md]] — DMLS MLOps tool catalog; Pandas/Kafka/SHAP/MLflow/Feast ecosystem
|- [[raw/articles/designing-ml-systems-resources-2026-07-11.md]] — DMLS further reading; 40+ papers/case studies
|- [[raw/articles/designing-ml-systems-basic-ml-review-2026-07-11.md]] — DMLS ML fundamentals; objective functions, gradient descent, optimizers
|- [[raw/papers/bringhurst-elements-of-typographic-style-2ed.md]] — Robert Bringhurst, *The Elements of Typographic Style* (2nd ed. 1996), Hartley & Marks
- [[raw/papers/josef-albers-wikipedia-2026.md]] — Josef Albers Wikipedia summary; *Interaction of Color* (1963)
- [[raw/papers/josef-muller-brockmann-wikipedia-2026.md]] — Josef Müller-Brockmann Wikipedia; *Grid Systems* (1968/1981)
- [[raw/papers/ellen-lupton-wikipedia-2026.md]] — Ellen Lupton Wikipedia; *Thinking with Type* (3rd ed. 2024)
- [[raw/papers/edward-tufte-wikipedia-2026.md]] — Edward Tufte Wikipedia; *Visual Display* (1983), *Envisioning Information* (1990)
- [[raw/articles/chip-huyen-llm-engineering-2023.md]] — Chip Huyen, *Building LLM Applications for Production* (2023); 131KB; LLMOps systematized
- [[raw/articles/anthropic-prompting-best-practices-2026.md]] — Anthropic官方：Prompting Best Practices for Claude；XML tags/Examples/Role/Thinking/Agentic Systems
- [[raw/articles/openai-prompt-engineering-2026.md]] — OpenAI官方：Prompt Engineering Guide；Message Roles/Fewshot/RAG/Prompt Caching
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
---

|- [[red-green-refactor]] — Red-Green-Refactor（Kent Beck 2003 TDD 3 步循環）；Hermes 工匠 4 大對應；常見失敗（skip refactor）+ Red 寫測試先 / Green 通過 / Refactor 改進
|- [[owasp-threat-modeling-framework]] — **OWASP Threat Modeling 四問框架**（What / What can go wrong / Mitigation / Quality Review）；STRIDE 分類整合；Hermes Yu-shi 4 階段審計入口

|- [[hnsw-algorithm]] — **HNSW（Hierarchical Navigable Small World）**；3 大參數（M/ef/ef_construction）；Filterable HNSW 創新（Qdrant）；4 大 Vector DB 對照表
|- [[rag-pipeline]] — **RAG (Retrieval-Augmented Generation) Pipeline**（Lewis 2020 起源 → 2026 Multimodal RAG 演進）；4-Stage Pipeline（Retrieval → Augmentation → Generation → Post-Processing）；4 大框架（LangChain / LlamaIndex / Haystack / RAGFlow）；7 大評估指標
|- [[lambdamart-ltr]] — **LambdaMART Learning to Rank**（Burges 2010 MSR-TR-2010-82）；演進樹 RankNet → LambdaRank → LambdaMART；4 大公式；4 大超參數；6 大訓練特徵
|- [[pdf-platypus-architecture]] — **PLATYPUS Page Layout Architecture**（ReportLab v5.0.0）；Flowable 系統（25+ 可組合區塊）；Generator-Renderer 分離模式；TableStyle 5 大常見錯誤；Document Template + Frame 架構
|- [[skill-ecosystem-architecture]] — **55 Hermes Skills 8-Tier 分層全景圖**（2026 研究）；Layer 1~8 分層架構；技術棧地圖（Playwright/Whisper/GitHub API）；2026 三大趨勢（Multi-Agent / LLM Inference / Skill Automation）
|- [[pdf-rendering-architecture]] — **PDF 渲染 4-Way 架構**（PyMuPDF vs PDF.js vs PDFium vs Native）；PyMuPDF 渲染 API（Matrix/DPI 控制）；PDF.js v4 CSP 問題；PDFium WASM 渲染；服務端渲染（Python/Rust/Node）；5 大性能優化策略

## 🚀 2026-07-13 重大研究攝入整合表

今日累計研究攝入 17 個權威資源 + 35 個 SOP references + 54 個 TRAP-SOP。
完整對照表見 `/Users/bbni039/workspace/hermes-sessions-master-changelog-20260713.md`

### 1. 架構運行（5 個新 raw + 4 concept + 4 entity）
- [[raw/articles/the-devops-handbook-2026-07-13]] | [[the-devops-handbook-book]]
- [[raw/articles/accelerate-book-2026-07-13]] | [[accelerate-book]]
- [[raw/articles/dora-2024-state-of-devops-2026-07-13]] | [[dora-four-key-metrics]]
- [[raw/articles/google-sre-book-2026-07-13]] | [[sre-site-reliability-engineering]]
- [[raw/articles/20-essential-sre-books-catchpoint-2026-07-13]]

### 2. 主控台（4 個新 raw + 1 entity + 1 concept）
- [[raw/articles/chaos-engineering-books-2026-07-13]] | [[chaos-engineering]]
- [[raw/articles/kubernetes-control-plane-2026-07-13]] | [[control-plane-pattern-declarative-reconciliation]]
- Vinyl Cache：[[raw/articles/vinyl-cache-official-2026-07-13]]

### 3. 文謀能力（2 個新 raw + 2 concept）
- [[raw/articles/strategic-thinking-reading-list-2026-07-13]]
- [[raw/articles/thinking-in-bets-and-art-of-thinking-clearly-2026-07-13]]
- [[system-1-system-2-thinking]] | [[cognitive-bias-quick-reference]]

### 4. Hermes 智能（3 個新 raw + 1 entity + 2 concept）
- [[raw/articles/hermes-intelligence-reading-map-2026-07-13]] | [[hermes-intelligence-5-layer-architecture]]
- [[chain-of-thought-reasoning]] | [[orchestration-patterns-2026-07-13]]

### 5. SOP 系統建立（v3.0 → v3.7 — 7 個版本演化）
- Plan 範本 v1.1.1（4 patterns 完整範例）
- 6 Orchestration Patterns 規格化
- Decision Log 機制（Annie Duke 4 象限）
- Verify-Before-Redo Protocol（TRAP-SOP-069）
- 版權合規 SOP（拒絕盜版）+ 書籍攝入工作流 SOP

### 6. SOP 主檔案
- `~/.hermes/skills/hermes/sop-design-maintenance-errors/SKILL.md`（**v3.7.0**）
- `~/.hermes/skills/hermes/sop-design-maintenance-errors/references/`（**35 個 references**）

### 7. 工具
- `~/.hermes/scripts/decision_log.py` — Annie Duke 啟發 CLI
- `~/.hermes/decisions/*.yaml` — 2 個示範決策

---

**今日總結**：54 個 TRAP-SOP + 35 個 references + 17 個權威資源攝入 + Decision Log + Plan v1.1.1
