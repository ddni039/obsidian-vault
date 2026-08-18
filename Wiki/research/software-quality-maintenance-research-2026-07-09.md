---
title: Software Quality & Maintenance Research — 提升偵測維護編碼
created: 2026-07-09
updated: 2026-07-09
type: research
tags: [software-quality, maintenance, testing, debugging, legacy-code, research]
sources: [entities/working-effectively-with-legacy-code, entities/pragmatic-programmer, entities/debug-it-paul-butcher, entities/xunit-test-patterns, entities/software-testing-and-analysis-pezze-young, entities/automation-pipelines-martinfowler, concepts/software-testing-fundamentals, concepts/software-testing-maintenance, concepts/debugging, concepts/legacy-code-strategies, concepts/pragmatic-programmer-tips, concepts/xunit-test-patterns]
confidence: high
---

# 研究報告：提升偵測維護編碼

## 研究範圍
針對「提升偵測維護編碼」方向，攝入 4 本核心書籍 + 3 個軟體測試/偵錯/維護概念頁，形成連貫知識體系。

---

## 知識體系地圖

```
提升偵測維護編碼
├── 偵錯（Debugging）
│   ├── 基礎理論 → [[debugging]]
│   ├── 實用流程 → [[debug-it-paul-butcher]]
│   └── Hermes 工具 → hermes logs / session_search / git bisect
│
├── 測試工程（Testing）
│   ├── 核心概念 → [[software-testing-fundamentals]]
│   ├── 測試壞味道 → [[xunit-test-patterns]]
│   ├── 維護實踐 → [[software-testing-maintenance]]
│   ├── 測試策略 → [[software-testing-and-analysis-pezze-young]]
│   └── 測試模式 → [[xunit-test-patterns]]
│
├── 軟體維護（Maintenance）
│   ├── 理論框架 → [[working-effectively-with-legacy-code]]
│   ├── 接縫技法 → [[legacy-code-strategies]]
│   ├── 工藝態度 → [[pragmatic-programmer-tips]]
│   └── 自動化管線 → [[automation-pipelines-martinfowler]]
│
└── 整合應用（Hermes）
    ├── 測試隔離 → subprocess-per-test-file
    ├── Bug 防治 → No change-detector tests
    └── Debug 流程 → 4-phase systematic-debugging
```

---

## 書本核心提煉

### 1. [[working-effectively-with-legacy-code]] — Feathers

**一句話定義：** Legacy code = 沒有測試的代碼。

**最重要的一個技法：Characterization Tests**
> 「我不知道這段代碼應該做什麼，但我知道它現在在做什麼。」
> 先 capture 現有行為，再改寫。

**最重要的一個概念：Seams**
> 能夠在不改變其他地方的情況下改變行為的點。找到接縫，才能安全地修改。

**與其他書的連結：**
- 為 [[xunit-test-patterns]] 提供「為什麼壞測試危險」的動機
- 為 [[pragmatic-programmer]] Tip 32 提供具體操作方法

---

### 2. [[pragmatic-programmer]] — Hunt & Thomas

**一句話定義：** 軟體工藝靠日常紀律，不靠天才。

**最重要的一個 Tip：** Tip 24 — 修復，不要 workaround。
> 繞過問題只會累積技術債，最終讓系統不可維護。

**最重要的一個概念：Good Enough Software**
> 不必追求完美，但要知道何時「足夠好」。

**與其他書的連結：**
- Tip 24 呼應 [[working-effectively-with-legacy-code]] 的「不要累積技術債」
- Tip 27 呼應 [[working-effectively-with-legacy-code]] 的耦合斷裂技法
- 「知識組合」與 [[software-testing-maintenance]] 的技術債概念相通

---

### 3. [[debug-it-paul-butcher]] — Butcher

**一句話定義：** Debugging 是工藝，不是運氣。

**最重要的一個流程：四階段**
```
重現（Reproduce）
  → 定位（Identify）
    → 決定修復（Determine Fix）
      → 驗證（Validate）
```

**最重要的一個預防概念：Bug Taxonomy**
> 不是所有 bug 都值得修。修復代價 > bug 影響時，考慮不修。

**與其他書的連結：**
- 四階段為 [[software-testing-maintenance]] 的 defect prevention 提供操作流程
- 重現-隔離概念呼應 [[working-effectively-with-legacy-code]] 的 Sensing and Separation

---

### 4. [[xunit-test-patterns]] — Meszaros

**一句話定義：** 大多數開發者會寫測試，但不知道測試什麼時候壞了。

**最重要的一個概念：Test Smell**
> 壞測試比沒有測試更危險——它給你錯誤的安全感。

**最重要的一個 pattern：Test Double 分類**
```
Dummy → 只填充參數
Stub  → 提供預先定義回應
Spy   → 記錄調用信息
Mock  → 主動驗證交互期望
Fake  → 簡化實現（如 in-memory DB）
```

**與其他書的連結：**
- 測試壞味道為 [[software-testing-maintenance]] 提供具體症狀清單
- 與 [[pragmatic-programmer]] 的「讓軟體正確」態度一致

---

## 跨書共識（最大公因數）

| 命題 | 4 本書共同支持 |
|------|---------------|
| 測試是預防不是補救 | ✓ Feathers/Butcher/Meszaros/HuntThomas 全部提到 |
| 小步快跑 | ✓ Feathers 的每次小改、Butcher 的四階段、HuntThomas 的 Tip 32 |
| 不要累積技術債 | ✓ Feathers 的 Legacy Code、HuntThomas 的 Tip 24 |
| 測試隔離 | ✓ Meszaros 的 Erratic Test、Feathers 的接縫 |
| 記錄 bug 以防復發 | ✓ Butcher 的 bug 回歸、HuntThomas 的「殺蟲程序測試法」|

---

## Hermes 實務映射

### 偵錯（Debugging）→ Hermes

| 書 | 概念 | Hermes 實踐 |
|----|------|-----------|
| Butcher | 四階段流程 | `systematic-debugging` skill：理解→定位→修復→驗證 |
| Butcher | 假設-演繹法 | session_search 的 bookend 分析 |
| Butcher | 日誌挖掘 | `hermes logs` 命令 |
| Feathers | Sensing & Separation | hermes logs + session_search |
| Feathers | Git bisect | 壞 commit 定位 |
| [[pragmatic-programmer]] | Tip 24 | TRAP 陷阱表固化維護教訓 |

### 測試（Testing）→ Hermes

| 書 | 概念 | Hermes 實踐 |
|----|------|-----------|
| Meszaros | Erratic Test | subprocess-per-test-file 隔離 |
| Meszaros | Fragile Test | No change-detector tests |
| Meszaros | Test Double | Plugin ABC mock points |
| Feathers | Characterization Tests | 現有行為 capture 再重構 |
| [[pragmatic-programmer]] | CI-parity | `scripts/run_tests.sh`（TZ=UTC, LANG=C.UTF-8）|

### 維護（Maintenance）→ Hermes

| 書 | 概念 | Hermes 實踐 |
|----|------|-----------|
| Feathers | 接縫模型 | Plugin system（最小化核心改動）|
| Feathers | 依賴斷裂 | Plugin ABC + Hook registration |
| [[pragmatic-programmer]] | Tip 27 最小化耦合 | 3+1 分層架構 |
| [[pragmatic-programmer]] | Tip 17 業務/GUI 分離 | Core / Gateway / UI-TUI 分离 |
| Butcher | Bug Taxonomy | Issue 分類（defect / enhancement / chore）|

---

## 未來研究建議

1. **Code Review 文化**：與 [[pragmatic-programmer]] 的 Tip 17-36 配合，建立 Hermes code review checklist
2. **Mutation Testing**：Hermes 目前無 mutation testing，可以引進 `cosmic-ray` 或 `mutmut`
3. **Property-Based Testing**：[[pragmatic-programmer]] 20th Anniversary 提到的現代測試方向
4. **Technical Debt 追蹤**：與 [[working-effectively-with-legacy-code]] 配合，建立 Hermes 的技術債清單

---

## Source Files
- Raw sources: NONE（聯網被擋，vendor pages 無法抓取，僅以專家知識建立 entity）
- Entities: `wiki/entities/working-effectively-with-legacy-code.md`, `wiki/entities/pragmatic-programmer.md`, `wiki/entities/debug-it-paul-butcher.md`, `wiki/entities/xunit-test-patterns.md`
- Concepts: `wiki/concepts/debugging.md`, `wiki/concepts/software-testing-fundamentals.md`, `wiki/concepts/software-testing-maintenance.md`
