# Hermes CBHE 核心文件知識圖譜

> 研究日期：2026-07-15 | 工具：Graphify v0.9.16 + DeepSeek-v4-flash | 消耗：$0.026

---

## 一、圖譜元數據

| 指標 | 數值 |
|------|------|
| **節點** | 44 |
| **邊緣** | 47 |
| **社區** | 6 |
| **提取率** | 100% EXTRACTED · 0% INFERRED |
| **語意模型** | DeepSeek-v4-flash |
| **Token 消耗** | 5,107 in / 15,106 out |

---

## 二、六大社區

| # | 名稱 | 節點數 | 核心內容 |
|---|------|--------|---------|
| 0 | Personal Knowledge Tools | 13 | brain、Obsidian、MiniMax API、字體 |
| 1 | Task Agent Phases | 11 | C、delegate_task、phase_ab_gate、5種Phase |
| 2 | Claude Agent Index | 8 | H'、H*、wenmou、yushi、hermes-ctl |
| 3 | Error Handling Rules | 7 | E 角色的6種電路阻斷碼 |
| 4 | Agent Role Trio | 4 | B/E/H 三角色 + SOUL |
| 5 | Master Console | 1 | master_console（橋接節點） |

---

## 三、God Nodes（最密集連接節點）

| 排名 | 節點 | 邊緣數 | 角色 |
|------|------|--------|------|
| 1 | `C (Master/Console)` | 4 | 流水線唯一入口 |
| 2 | `delegate_task` | 2 | 子代理生成 |
| 3 | `phase_ab_gate.py` | 2 | 階段閘門 |
| 4 | `routing-check` | 2 | 路由檢查 |
| 5 | `B (Planner/Wenmou)` | 1 | 規劃者 |
| 6 | `~/brain` | 1 | 知識庫 |

---

## 四、C (Master/Console) 角色職責

### 4.1 直接調用鏈

```
C (Master/Console)
  ├── calls ──→ delegate_task       [src=AGENTS.md]
  ├── calls ──→ phase_ab_gate.py  [src=AGENTS.md]
  └── calls ──→ routing-check       [src=AGENTS.md]
```

### 4.2 C 的檔案引用關係

```
C (Master/Console) --references──→ SOUL.md
SOUL.md --references──→ AGENTS_INDEX.md、AGENTS.md、RULES.md、CODEX.md、B、E、H
```

### 4.3 結論
C 是 CBHE 流水線的唯一入口，依賴三大核心工具：
- `delegate_task`：子代理生成
- `phase_ab_gate.py`：階段閘門驗證
- `routing-check`：路由檢查

---

## 五、Phase Gate 與路由工作流

### 5.1 完整 Phase 地圖（全部來自 AGENTS.md）

```
PHASE_SYSTEM    ← 系統頂層
PHASE_RESEARCH  ← 研究階段
PHASE_PDF       ← PDF 生成
PHASE_PDF_EDIT  ← PDF 編輯
PHASE_EVAL      ← 評估階段
```

### 5.2 Gate 邏輯循環

```
C (Master/Console)
  ├── calls → routing-check ──calls──→ C (Master/Console)（循環驗證）
  │
  └── calls → phase_ab_gate.py ──calls──→ C (Master/Console)（閘門確認）
```

### 5.3 delegate_task 回調 C

```
delegate_task ──calls──→ C (Master/Console)
```

**意外發現：** delegate_task 完成後，會回調 C 進行下一階段路由，構成 C↔delegate_task 雙向通訊。

---

## 六、E (Auditor/Yushi) 錯誤電路

### 6.1 六種電路阻斷碼（全部來自 RULES.md）

| 錯誤碼 | 意義 |
|--------|------|
| `E-SUBAGENT-CIRCUIT-OPEN` | 子代理電路 open |
| `E-SUBAGENT-CONTEXT-BLOATED` | 上下文膨脹 |
| `E-H-DOMAIN-BLOCKED` | H 角色域被阻斷 |
| `E-GATEWAY-DEP-UNHEALTHY` | 依賴服務不健康 |
| `E-SESSION-SIZE-UNCHECKED` | Session 未檢查大小 |
| `E-SESSION-UNDISTILLED` | Session 未蒸餾 |

### 6.2 錯誤處理Map

```
error_handler_map.yaml ──references──→ AGENTS.md
E-*-* 全部 ──references──→ RULES.md
```

### 6.3 E 的連接

```
E (Auditor/Yushi) --references──→ SOUL.md
E --[電路阻斷]──→ RULES.md
SOUL.md --references──→ AGENTS_INDEX.md、AGENTS.md、RULES.md、CODEX.md、B、C、H
```

---

## 七、delegate_task 子代理生成

### 7.1 完整調用圖

```
delegate_task
  ├── references → AGENTS.md
  ├── calls → C (Master/Console)
  │
  ├── [觸發5種Phase]
  │     PHASE_SYSTEM → PHASE_RESEARCH → PHASE_PDF → PHASE_PDF_EDIT → PHASE_EVAL
  │
  └── [6種錯誤處理]
        E-SUBAGENT-CIRCUIT-OPEN
        E-SUBAGENT-CONTEXT-BLOATED
        E-GATEWAY-DEP-UNHEALTHY
        E-SESSION-UNDISTILLED
        E-SESSION-SIZE-UNCHECKED
        E-H-DOMAIN-BLOCKED
```

### 7.2 關鍵發現
delegate_task 完成後， caller 會被 `E-*-*` 錯誤碼接管，構成 **C → delegate → E** 的完整錯誤處理環路。

---

## 八、H (Executor/Craftsman) 執行者

### 8.1 H 的連接（弱連接）

```
H (Executor/Craftsman)
  └── references → SOUL.md
       （其他 Phase 連接需透過 AGENTS.md）
```

### 8.2 H 涉及的 Phase

`PHASE_SYSTEM`、`PHASE_PDF`、`PHASE_PDF_EDIT`、`PHASE_RESEARCH`、`PHASE_EVAL`

### 8.3 發現
H 的節點在圖譜中屬於「高孤立」類型，驗證了 GRAPH_REPORT 中「34個孤立節點」的發現。H 的連接主要透過 AGENTS.md 間接建立。

---

## 九、意外連接（Surprising Connections）

| 連接 | 來源 | 意義 |
|------|------|------|
| `C --calls--> delegate_task` | SOUL.md → AGENTS.md | C 依賴 delegate_task 生成子代理 |
| `C --calls--> phase_ab_gate.py` | SOUL.md → AGENTS.md | C 依賴閘門驗證階段 |
| `C --calls--> routing-check` | SOUL.md → AGENTS.md | C 依賴路由檢查 |
| `delegate_task --calls--> C` | AGENTS.md | 子代理完成後回調 C |
| `routing-check --calls--> C` | AGENTS.md | 路由檢查完成後回調 C |

---

## 十、知識缺口

### 10.1 34 個孤立節點
這些節點有 ≤1 條連接，可能存在文檔缺口或未記錄的依賴：

- `B (Planner/Wenmou)` — 需加強與其他角色關聯
- `~/brain` — 需加強與核心系統的引用
- `~/.local/bin/claude` — 需加強與 Agent Index 的關聯
- `Discord Firecrawl bug` — 需記錄修復歷史
- `E-SUBAGENT-CIRCUIT-OPEN` 等 — 需加強與 delegate_task 的連接

### 10.2 建議
1. 為 B (Planner) 增加更多與 Phase 的連接記錄
2. 將 `~/brain` 的具體使用方式文件化
3. 為每個 E 錯誤碼增加與 delegate_task 的明確觸發條件

---

## 十一、整體架構圖

```
SOUL.md ──定義──→ C、B、H、E 四角色
    │
    ├── AGENTS.md ──定義──→ delegate_task、routing-check、phase_ab_gate
    │                   + 5 Phase：SYSTEM/RESEARCH/PDF/PDF_EDIT/EVAL
    │                   + error_handler_map.yaml
    │
    ├── RULES.md ──定義──→ 6種 E 錯誤電路阻斷碼
    │
    ├── CODEX.md ──定義──→ 工具、代號、外部適配器
    │
    └── AGENTS_INDEX.md ──定義──→ Agent 索引

C (Console)
  ├── calls ──→ delegate_task ──calls──→ [subagent]
  │                  │
  │                  │  觸發 Phase 鏈
  │                  │
  │                  └──calls──→ phase_ab_gate
  │                              │
  │                  若失敗觸發 E 錯誤碼 ──┴──→ RULES.md
  │
  ├── calls ──→ routing-check ──calls──→ C（循環驗證）
  └── references ──→ SOUL.md
```

---

## 十二、產出檔案

```
~/core-files-graph/graphify-out/
├── graph.html      力導向互動圖（瀏覽器打開）
├── graph.json      結構化圖譜數據
├── GRAPH_REPORT.md 圖譜分析報告
└── manifest.json   追蹤元數據
```

---

## 十三、相關研究

- [Graphify 專案分析](./graphify-project-analysis.md)
- [Open WebUI 專案分析](./open-webui-project-analysis.md)
- [NotebookLM 生態系分析](./notebooklm-project-analysis.md)
- [Telegram Bot 書籍研究](./telegram-bot-programming-books.md)

---

## 標籤

#hermes #cbhe #knowledge-graph #graphify #core-files #architecture
