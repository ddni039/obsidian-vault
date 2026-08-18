# Graphify 專案深度分析

> 研究日期：2026-07-15 | 最新版本：v0.9.16（2026-07-14） | Stars：87,353 | YC S26

---

## 一、專案定位

**Graphify** 是將任意程式碼庫轉為可查詢知識圖譜的 AI 編碼助手技能。透過 `/graphify` 指令，AI 助手可理解整個專案（代碼、文檔、PDF、圖片、影片），而非傳統關鍵詞搜索。2026 年入選 Y Combinator S26。

---

## 二、核心數據

| 指標 | 數值 |
|------|------|
| **Stars** | 87,353 |
| **Forks** | 8,567 |
| **提交數** | 1,122 |
| **貢獻者** | 174 |
| **開發語言** | Python 100% |
| **授權** | MIT（免費商業使用） |
| **最新版本** | v0.9.16（2026-07-14） |
| **活躍問題** | 513 open |
| **trendshift 排名** | 全球前 1 活躍Repos |
| **贊助者** | safishamsi（Y Combinator S26） |

---

## 三、核心功能矩陣

| 功能 | 說明 | 技術 |
|------|------|------|
| **Code Maps（代碼地圖）** | 自動解析程式碼結構關係 | Tree-sitter AST（36 種語言，本地執行） |
| **God Nodes** | 找出最密集連接的概念 | NetworkX 中心性分析 |
| **Communities** | 自動分群子系統 | Leiden 演算法 |
| **Cross-file Links** | 跨檔案呼叫/導入/繼承關係 | Tree-sitter 多檔案追蹤 |
| **Query / Path / Explain** | 自然語言問答、追蹤連接路径、解釋概念 | LLM + Graph 遍歷 |
| **Doc Refs** | ADR/RFC 文件註解轉為一級節點 | 正規表達式 + LLM |
| **Beyond Code** | PDF、圖片、影片、語音轉為圖譜節點 | 多模態 LLM 理解 |
| **Rationale Tags** | `# NOTE:` / `# WHY:` 註解轉為結構化節點 | 正規表達式 |

---

## 四、輸出檔案

```
graphify-out/
├── graph.html       可互動的力導向圖（瀏覽器打開）
├── GRAPH_REPORT.md  圖譜報告：核心概念、意外連接、建議問題
└── graph.json       完整圖譜數據，可反覆查詢無需重新讀取檔案
```

---

## 五、與其他方案的Benchmark對比

| Benchmark | Graphify | 對手 |
|-----------|---------|------|
| **LOCOMO recall@10** | **0.497** | mem0: 0.048, supermemory: 0.149 |
| **LOCOMO QA accuracy** | 45.3% | supermemory: 49.7%, mem0: 27.3% |
| **LongMemEval-S QA** | **76%** | 與 dense RAG 持平 |
| **Graph Build LLM credits** | **0** | 其他系統每 token 付費 |
| **ERPNext code intelligence** | ✅ | 實測有效 |

> 所有系統使用相同模型和預算，評分法官經盲測驗證（90.6% 一致性，Cohen's kappa 0.81）

---

## 六、架構設計

### 6.1 技術棧
```
解析層：Tree-sitter AST（代碼） + LLM semantic pass（文檔/多媒體）
圖譜層：NetworkX（純Python，無Neo4j依賴）
壓縮層：BFS 子圖查詢（~2k tokens vs 670k naive）
社群檢測：Leiden 演算法
CLI框架：Python 3.10+，uv 包管理
傳輸：Stdio（預設）+ HTTP Streamable（團隊共享，可選）
容器化：Dockerfile
```

### 6.2 核心模組
```
graphify/
├── extract.py           代碼解析引擎（tree-sitter，36語言）
├── llm/                 LLM語意理解（文檔/多媒體）
├── graph/               NetworkX圖譜建構
├── serve/               MCP Server（HTTP transport）
├── query/               查詢引擎（query/path/explain）
├── extractors/          語言解析器（blade/elixir/razor/zig/...）
└── skills/              AI助手整合（Claude/Cursor/Codex/OpenCode）
```

### 6.3 邊緣標籤語意
- `EXTRACTED`：源代碼中明確聲明的關係（直接解析）
- `INFERRED`：透過圖論解析推斷的關係（跨參照推斷）

---

## 七、支援平台

| 平台 | 支援狀態 |
|------|---------|
| **Claude Code** | ✅ 專用 skill-*.md，PreToolUse hook |
| **Cursor** | ✅ 專用 skill-*.md |
| **OpenAI Codex** | ✅ 專用 skill-*.md |
| **Gemini CLI** | ✅ 專用 skill-*.md |
| **GitHub Copilot** | ✅（通用 shell 模式） |
| **其他** | 任何可執行 shell 的 AI 助手 |

---

## 八、安裝方式

```bash
# 方式1：uv（推薦）
uv tool install graphifyy

# 方式2：pipx
pipx install graphifyy

# 方式3：Docker（團隊部署）
docker build -t graphify .
docker run -v $(pwd):/repo graphify graphify /repo

# 安裝後向AI助手註冊技能
graphify install
```

```bash
# 基本使用
/graphify .              # 在AI助手中建立圖譜
graphify query "..."      # 自然語言查詢
graphify path A B          # 追蹤A到B的最短路徑
graphify explain "..."    # 解釋單一概念

# MCP Server（團隊共享）
python -m graphify.serve graph.json --transport http --port 8080 --api-key YOUR_KEY
```

---

## 九、與 Hermes Agent 的整合評估

### 9.1 與 gbrain 的功能對照

| 功能 | Graphify | gbrain（Hermes） |
|------|---------|-----------------|
| **圖譜類型** | 程式碼結構知識圖譜 | Wiki/網絡語意圖 |
| **解析方式** | Tree-sitter AST（本地） | Embedding + LLM 語意 |
| **邊緣語意** | EXTRACTED / INFERRED | 語意相關性 |
| **查詢方式** | Query / Path / Explain | 自然語言問答 |
| **多模態** | ✅（圖片/影片/音頻） | ✅（網頁/文件） |
| **隱私** | 代碼本地解析 | Wiki 本地存儲 |
| **依賴** | 純 Python，無 Neo4j | PGLite + OpenRouter |

### 9.2 整合可能性

**Graphify × gbrain**：
- Graphify 擅長結構化程式碼圖譜（tree-sitter）
- gbrain 擅長語意維基（Embedding + LLM）
- 兩者可互补：Graphify 處理程式碼專案，gbrain 處理文檔研究

**Graphify × Hermes Agent 技能**：
- Graphify 本身是 AI 助手 skill（與 Hermes Skills 同類）
- 可探索將 Graphify 整合為 Hermes 的程式碼理解工具
- `graphify path A B` 可作為 Herms Agent 推理的結構化依據

### 9.3 推薦評估方向
1. **程式碼理解增強**：將 Graphify 用於 Hermes 理解大型程式碼庫
2. **雙圖譜系統**：Graphify 處理代碼圖譜，gbrain 處理文檔圖譜
3. **思維追蹤**：`graphify path` 用於理解複雜系統依賴關係

---

## 十、關鍵文獻

- [Graphify GitHub](https://github.com/Graphify-Labs/graphify) — 87.2k ⭐，v0.9.16
- [Graphify Official](https://graphify.net/) — 官方網站+圖譜展示
- [Graphify Benchmarks](https://github.com/Graphify-Labs/graphify/blob/v8/BENCHMARKS.md)
- [Graphify Architecture](https://github.com/Graphify-Labs/graphify/blob/v8/ARCHITECTURE.md)
- [Augment Code Docs](https://docs.augmentcode.com/) — 收錄 Graphify v0.9.9 教程
- [YouTube: Graphify Solves Claude's Biggest Limitation](https://www.youtube.com/watch?v=HQEm4rBKdec)
- [Medium: Graphify — One Command Turns Any Folder Into a Knowledge Graph](https://medium.com/how-to-profit-ai/graphify-one-command-turns-any-folder-into-a-knowledge-graph-7b0602b09bee)
- [Blog: Build a Knowledge Graph From Your Entire Codebase](https://blog.gopenai.com/graphify-build-a-knowledge-graph-from-your-entire-codebase-without-sending-your-code-to-anyone-1b6924474b50)

---

## 十一、相關開源替代品對照

| 專案 | ⭐ | 定位 |
|------|-----|------|
| **Graphify** | 87.2k | 程式碼+文檔→知識圖譜，MIT |
| **notebooklm-py** | 17.8k | NotebookLM Python SDK |
| **mem0** | - | 長期記憶層（作為Graphify對手） |
| **supermemory** | - | 記憶管理（Graphify對手） |
| **Sourcegraph** | - | 程式碼搜索引擎（vs Graphify視覺化圖譜） |
| **Code2Vec** | - | 程式碼結構向量（vs Graphify Graph-RAG） |

---

## 十二、標籤

#research #graphify #knowledge-graph #code-understanding #tree-sitter #rag #neo4j-alternative #claude-code #openclaw #yc-s26 #hermes-integration
