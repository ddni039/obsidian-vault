---
title: AI Coding Productivity Paradox
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, ai-coding, productivity, perception-gap, benchmarks-vs-reality]
sources:
  - raw/articles/metr-2025-rct-developer-productivity-2026-07-13.md
  - raw/articles/metr-2026-uplift-survey-2026-07-13.md
related:
  - "[[perception-vs-reality-gap]]"
  - "[[task-substitution-effect]]"
confidence: high
---

# AI Coding Productivity Paradox

## 定義

**AI Coding Productivity Paradox** = AI coding 工具被廣泛採用且 benchmark 表現優異，但在真實開發任務中**可能讓資深開發者變慢**，且開發者**普遍相信**自己變快了。

## 數據對比（METR 2025-2026）

| 來源 | 觀察對象 | 結論 |
|------|---------|------|
| SWE-Bench Verified | 開源 PR + 自動測試 | 模型經常成功 |
| RE-Bench | AI 研究問題 | 模型經常成功 |
| Anecdotes | 多樣化開發者 | 多數覺得很有幫助 |
| **METR Early-2025 RCT** | 16 位資深開發者 + 246 真實 issue | **AI 慢 19%** |
| **METR Late-2025 RCT** | 57 位開發者 | 估計**AI 快 4-18%** |
| **METR 2026 Survey** | 349 位技術工作者 | 自我報告 **1.4-2× value** |

## 為什麼有 Paradox？

### 假說 1：Benchmarks/Ancedotes 高估

- Benchmarks 用自動測試，**忽略風格/文檔/維護性**
- Anecdotes 來自「已經擁抱 AI 的開發者」sample bias
- 開發者**無法準確估計自己沒做過的事**（counterfactual bias）

### 假說 2：任務類型替代

開發者用 AI 做「本來不會做的任務」（如 UI polish、文件、測試），這些任務「本來就不重要」→ AI 加速了「不重要的任務」。

### 假說 3：時間測量失準

開發者會在 AI agent 運行時**同時做其他事** → self-reported time 不準。

## 三大互補證據來源

| 來源 | 優勢 | 盲點 |
|------|------|------|
| **Benchmarks** | 標準化、可重現 | 外部效度爭議；忽略人類在乎的事 |
| **RCT** | 控制嚴謹、外部效度高 | 極昂貴；selection effects |
| **Observational** | 樣本大、便宜 | Selection effects；難推因果 |

## 對 Hermes 的啟示

### 立即可行

| 啟示 | 對策 |
|------|------|
| 開發者 perception 不可信 | 物理驗證清單（`physical-verification.md` Step 1-6）|
| Task selection bias | subagent 必須覆蓋所有任務類型，不能避開 |
| Counterfactual 難評估 | E 階段審計（`auditor_core.py`） |

### 設計原則

1. **多源證據三角驗證**：不僅依賴單一 metric
2. **客觀 metric 優先**：用 token 用量、錯誤率、完成時間等可測量指標
3. **避免 selection bias**：隨機抽樣任務，覆蓋所有難度

## 相關研究

- [METR 2025 RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [METR 2026 Uplift Update](https://metr.org/blog/2026-02-24-uplift-update/)
- [METR 2026 Survey](https://metr.org/blog/2026-05-11-ai-usage-survey/)

## 來源

- Tomisin Abiodun：「AI Agent 時代的 SE 必讀書單」（強調 fundamentals 反而更重要）
- METR 三篇研究（見 sources）