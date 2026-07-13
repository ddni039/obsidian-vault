---
title: METR (AI Measurement)
created: 2026-07-13
updated: 2026-07-13
uid: e-54aa68016942
type: entity
tags: [organization, research, ai-evaluation, productivity-measurement, rct, metr]
sources:
  - raw/articles/metr-2025-rct-developer-productivity-2026-07-13.md
  - raw/articles/metr-2026-uplift-survey-2026-07-13.md
related:
  - "[[ai-coding-productivity-paradox]]"
  - "[[perception-vs-reality-gap]]"
confidence: high
---

# METR (Model Evaluation and Threat Research)

## 簡介

**METR**（前身 MATS）是**專門評估前沿 AI 自主執行複雜任務能力**的非營利研究組織。

> METR researches, develops and runs cutting-edge tests of AI capabilities, including broad autonomous capabilities and the ability of AI systems to conduct AI R&D.

## 核心研究領域

- **AI 能力評估**（SWE-Bench、RE-Bench、HLE）
- **Time Horizon 分析**（AI 完成任務的時間長度）
- **生產力影響**（RCT 實驗）
- **AI 安全監控**（Monitorability Evaluations）

## 2025-2026 生產力研究時間軸

| 日期 | 報告 | 結論 |
|------|------|------|
| 2025-07-10 | [Early-2025 RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | **AI 慢 19%** |
| 2026-02-24 | [Uplift Update](https://metr.org/blog/2026-02-24-uplift-update/) | 重新設計；估計**快 4-18%** |
| 2026-05-11 | [AI Usage Survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) | 349 人自我報告 **1.4-2× value** |

## 數據集

- [Early-2025-AI-on-Exp-OSS-Devs](https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs)
- [Late-2025-AI-on-OSS-Devs](https://github.com/METR/Measuring-Late-2025-AI-on-OSS-Devs)

## 與 Hermes 的關聯

METR 研究對 Hermes 設計的啟示：

1. **RCT 比 Survey 更可信**：Hermes 不應僅依賴用戶回饋，需內建物理驗證機制
2. **Perception gap**：用戶可能「覺得快」但實際「慢」→ Hermes 應有客觀 metric
3. **Selection effects**：開發者會避開 AI 不擅長的任務 → Hermes subagent 委派需強制覆蓋所有類型
4. **Task substitution**：開發者會用 AI 做「本來不會做的任務」→ Hermes 應記錄任務類型演變

## 來源

- [METR 官網](https://metr.org/)
- [METR Research](https://metr.org/research)
- [METR Blog](https://metr.org/blog)