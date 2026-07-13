---
title: Perception vs Reality Gap（AI Coding）
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, perception-bias, metr, ai-coding, metacognition, counterfactual]
sources:
  - raw/articles/metr-2025-rct-developer-productivity-2026-07-13.md
related:
  - "[[ai-coding-productivity-paradox]]"
confidence: high
---

# Perception vs Reality Gap（AI Coding）

## 定義

**Perception vs Reality Gap** = AI 用戶對自己生產力的**自我評估**與**實際表現**之間的巨大落差。

## METR 2025 RCT 的震撼數據

| 指標 | 數值 |
|------|------|
| 預期速度提升 | **+24%** |
| 實際速度變化 | **-19%** |
| **Gap** | **43 個百分點** |
| 實驗後仍相信的速度變化 | **+20%** |

**核心結論**：即使在實驗中**親身體驗了** AI 讓他們變慢，開發者**仍相信** AI 讓他們變快了 +20%。

## 為什麼 perception 與 reality 嚴重脫節？

### 認知偏誤（Cognitive Biases）

| 偏誤 | 機制 |
|------|------|
| **Confirmation bias** | 已有「AI 加速我」信念 → 找支持證據 |
| **Effort heuristic** | AI 看起來很努力 → 認為有產出 |
| **Counterfactual 難度** | 人類很難估計「如果沒 AI 我會多快」 |
| **Loss aversion** | 「失去 AI」的恐懼 > 「得到 AI」的滿足 |
| **Novelty effect** | 新工具總是感覺更快（短期） |

### 統計現實

> 人們對 AI 速度影響的高估**達 40 個百分點**（METR 2026 Survey）

## METR 2026 Survey 額外發現

### METR 員工特別保守

> METR staff give the lowest change in value answers of any subgroup we study.

**原因**：METR 員工知道 perception vs reality 落差。

### Survey vs RCT

| 證據類型 | 結論 |
|---------|------|
| Survey（自我報告）| 1.4-2× value |
| RCT（客觀測量）| -19% ~ +18%（隨時間變化）|

**結論**：Survey **可能**高估真實效果 40+ 個百分點。

## 對 Hermes 的啟示

### 立即可行

| 啟示 | 對策 |
|------|------|
| 用戶回饋「AI 加速了」不可信 | 物理驗證（物理測量 vs self-report） |
| LLM 自我評估「我做得好」不可信 | E 階段審計（程式碼審查、行為驗證）|
| Perception 有慣性 | 持續追蹤客觀 metric |

### 設計原則

1. **不相信 self-report**：永遠用 objective metrics 驗證
2. **多源三角驗證**：Survey + Benchmark + RCT 結合
3. **保留懷疑**：當一個工具聲稱「X% 加速」時，找 RCT 證據

## 相關概念

- [[ai-coding-productivity-paradox]] — 整體 Paradox
- METR 2025 RCT — 核心數據來源
- METR 2026 Survey — 自我報告基線

## 推薦閱讀

- [METR 2025-07-10 RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [METR 2026-05-11 Survey](https://metr.org/blog/2026-05-11-ai-usage-survey/)

## 來源

- METR 2025 RCT 全文
- METR 2026 Survey 全文