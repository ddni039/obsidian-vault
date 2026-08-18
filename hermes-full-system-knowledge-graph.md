# Hermes 全系統知識圖譜

> 建立日期：2026-07-30 | 工具：Graphify v0.9.16 + Gemini | 來源：skills(329) + scripts + core-files
> 先前版本：2026-07-19（1,648 節點 / 2,666 邊緣）
> 圖譜數據：`~/hermes-full-graph/graph.json`

---

## 一、圖譜元數據

| 指標 | 2026-07-19 | 2026-07-30（本次） | 變化 |
|------|------------|-------------------|------|
| **總節點** | 1,648 | 598 | -1,050 |
| **總邊緣** | 2,666 | 995 | -1,671 |
| **社區數** | 126 | 52 | -74 |
| **Token 消耗 | ~$0.05 | $0.0138 | -82% |
| **提取率** | — | 99% EXTRACTED / 1% INFERRED | — |
| **平均節點度** | 1.62 | 1.66 | +0.04 |

> 節點銳減主因：圖譜定位改變——2026-07-19 統計口徑含 skills 目錄本身（329 SKILL.md），2026-07-30 僅統計 Hermes 根目錄覆寫範圍（不含 skills 目錄遞歸），且 AST-only extraction 去除了大量重複命名節點。

---

## 二、數據來源（2026-07-30）

| 子圖譜 | 節點 | 邊緣 | 說明 |
|--------|------|------|------|
| `scripts/`（AST） | ~400 | ~800 | PDF 產生器、Wenmou 流程、審計腳本 |
| `core-files/`（語意） | ~44 | ~47 | SOUL/AGENTS/RULES/CODEX 等核心 Markdown |
| `scripts-all/`（AST） | ~154 | ~148 | Middleware、Utils |
| **合併總計** | **598** | **995** | 去重後 |

---

## 三、52 社區摘要（Top 10）

| 社區 | 節點數 | 核心內容 |
|------|--------|---------|
| **Community 0** | 29 | Express.js 路由（app.js、errorHandler、item/user routes） |
| **Community 1** | 38 | Hermes 控制腳本（hermes_ctl、health check、cron watchdog） |
| **Community 2** | 24 | gbrain tutorial 產生器（build_story、FlowableDrawing、make_body） |
| **Community 3** | 24 | gbrain tutorial 產生器（重複檢測，待清理） |
| **Community 4** | 16 | Hermes Codex 架構腳本（ColorBlock、hr、make_code_block） |
| **Community 5** | — | Hermes Codex 架構腳本（續） |
| **Community 6** | — | PDF 設計規範腳本 |
| **Community 7** | — | Hacker 工具腳本 |
| **Community 8** | — | translate_and_speak |
| **Community 9** | — | core_health_check + cron-watchdog |

---

## 四、God Nodes（最密集連接節點）

| 排名 | 節點 | 邊緣數 | 類型 |
|------|------|--------|------|
| 1 | `build_story()` | 16 | PDF 章節建構函式 |
| 2 | `build_story()` | 16 | （重複） |
| 3 | `sp()` | 15 | 格式化工具函式 |
| 4 | `sp()` | 15 | （重複） |
| 5 | `build_story()` | 14 | （重複） |
| 6 | `build_story()` | 14 | （重複） |
| 7 | `sp()` | 12 | （重複） |
| 8 | `_build_chapter7()` | 12 | PDF 章節建構 |
| 9 | `_build_chapter7()` | 12 | （重複） |
| 10 | `sp()` | 12 | （重複） |

> 重複節點反映同一函式在不同腳本版本中的多重實例（gen_gbrain_tutorial.py 多版本共存）。

---

## 五、意外發現

### 5.1 CBHE Pipeline 為 Hyperedge
```
CBHE Standard Pipeline Flow — role_c, role_b, role_h, role_e [EXTRACTED 1.00]
Hermes Core SSoT Files — soul_md, agents_md, rules_md, codex_md, agents_index_md, user_md [EXTRACTED 1.00]
```
圖譜自動檢測出 CBHE 四角色構成的標準流程邊，這是 graphify 對 Markdown 語意的結構化理解。

### 5.2 Express Middleware 錯誤處理鏈
```
errorHandler() --calls--> error() [EXTRACTED]
scripts-all/src/middleware/errorHandler.js → scripts-all/src/utils/response.js
```
意外捕獲 Node.js 專案中的 Express 錯誤傳遞鏈。

### 5.3 Community 2/3 完全重疊
gen_gbrain_tutorial.py 出現在兩個不同社區，可能是多版本並存的幻象（v1.0.61 vs v2）。

### 5.4 Hermes Core SSoT Hyperedge
六個核心文件自動被識別為一組超邊，強度 1.00（最高信任度）。

---

## 六、節點/邊緣變化分析

### 為什麼從 1,648 降到 598？

1. **Skills 目錄排除**：2026-07-19 的口徑包含 `~/.hermes/skills/` 遞归（329 個 SKILL.md），2026-07-30 extraction 僅針對 `~/hermes-full-graph/` 根目錄覆寫（不含 skills 子目錄）
2. **去重化名**：多版本同名腳本（gen_gbrain_tutorial.py v1.0.61/v2/gen_hermes_tutorial_v2.py）被識別為同一節點的 Multiple instances，不再分別計數
3. **純 AST 模式**：未使用 `--mode deep` 推斷，大幅減少 INFERRED 邊緣

### 真實覆寫範圍對照

| 目錄 | 檔案數 | 圖譜覆蓋 |
|------|--------|---------|
| `~/.hermes/scripts/` | ~60 | ✅ 完整 AST |
| `~/.hermes/hermes-full-graph/core-files/` | 6 MD | ✅ 語意 |
| `~/.hermes/hermes-full-graph/scripts-all/` | ~30 | ✅ 完整 AST |
| `~/.hermes/skills/` | 329 SKILL.md | ❌ 未涵蓋 |

---

## 七、圖譜查詢示例

```bash
# 查詢 CBHE 流程節點
graphify query "role C B H E pipeline" --graph ~/hermes-full-graph/graph.json

# 查詢 PDF 產生器流程
graphify query "build_story make_body chapter" --graph ~/hermes-full-graph/graph.json

# 查詢錯誤處理鏈
graphify path errorHandler error --graph ~/hermes-full-graph/graph.json

# 查詢 hermes_ctl 的下游呼叫
graphify affected hermes-ctl --relation calls --depth 2 --graph ~/hermes-full-graph/graph.json
```

---

## 八、產出檔案

```
~/hermes-full-graph/
├── graph.json          完整圖譜數據（598 節點）
├── graph.html          力導向視覺化（需瀏覽器）
├── graph-tree.html     樹狀結構視覺化（54.3 KB）
└── graphify-out/
    ├── GRAPH_REPORT.md     圖譜分析報告
    ├── .graphify_analysis.json
    └── .graphify_labels.json

~/brain/pages/library/
└── hermes-full-system-knowledge-graph.md  本頁
```

---

## 九、待清理項目

- [ ] Community 2/3 完全重疊——多版本 gen_gbrain_tutorial.py 需要合併或版本標注
- [ ] 重複命名節點（build_story / sp / _build_chapter7）反映多版本共存問題
- [ ] Skills 目錄（329 SKILL.md）未涵蓋——建議建立獨立 skills-graph

---

## 十、相關研究

- [Hermes 核心文件知識圖譜](./hermes-core-files-knowledge-graph.md)
- [Graphify 專案分析](./graphify-project-analysis.md)
- [Open WebUI 專案分析](./open-webui-project-analysis.md)
- [NotebookLM 生態系分析](./notebooklm-project-analysis.md)

---

## 標籤

#hermes #knowledge-graph #graphify #full-system #cbhe #architecture #v2026-07-30
