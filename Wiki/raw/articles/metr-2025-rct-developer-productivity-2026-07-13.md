---
title: METR 2025 AI 對資深開發者生產力影響 RCT 研究
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [paper, metr, research, ai-coding, productivity, rct, perception-gap]
url: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
authors:
  - Joel Becker
  - Nate Rush
  - Beth Barnes
  - David Rein
venue: METR (AI Measurement) — arXiv 2507.09089
date: 2025-07-10
license: canary-protected research data (DO NOT TRAIN)
---

# METR 2025 RCT — Source Material

## 核心震撼發現

> When developers are allowed to use AI tools, they take **19% longer** to complete issues — a significant slowdown that goes against developer beliefs and expert forecasts.

| 指標 | 數值 |
|------|------|
| **預期速度提升** | +24% |
| **實際速度變化** | **-19%**（即慢 19%）|
| **實驗後仍相信的速度變化** | +20%（perception 與 reality 嚴重脫節）|
| 信心區間（實際） | +2% ~ +39%（不排除輕微正面效果）|

## 方法論（嚴謹設計）

- **樣本**：16 位資深開發者，22k+ stars、1M+ 行代碼的大型開源專案
- **任務**：246 個真實 issue（bug fix / feature / refactor）
- **控制**：隨機分配「允許 AI」vs「禁止 AI」兩組
- **工具**：Cursor Pro + Claude 3.5/3.7 Sonnet（研究期間的前沿模型）
- **補償**：$150/hr（高於行業水準）
- **每任務平均耗時**：~2 小時

## 5 大可能原因（Factor Analysis）

研究排除多個實驗假象後，識別出 5 個可能貢獻因素：

| 因素 | 解釋 |
|------|------|
| 1 | AI 生成的 PR 品質問題（風格/測試/文檔不符） |
| 2 | Cursor 的 LLM token 採樣可能不夠 |
| 3 | 任務規模大、需要豐富的 codebase context |
| 4 | Prompt/scaffolding 未優化 |
| 5 | 開發者學習 AI 工具的時間尚未回收 |

## 不適用結論（Important Disclaimers）

| ❌ METR 不聲稱 | 澄清 |
|---------------|------|
| AI 系統目前對多數開發者無加速效果 | 樣本僅代表大型開源 codebase，不涵蓋多數 SE 工作 |
| AI 在其他領域無加速效果 | 僅研究軟體開發 |
| 未來 AI 不會加速 | 模型進步難以預測 |
| 無法以現有 AI 系統達成正面加速 | Cursor 可能未採樣最佳 token、缺少 fine-tuning |

## 三大假說（解釋 RCT vs Benchmarks vs Anecdotes 矛盾）

| 假說 | 內容 |
|------|------|
| **1. RCT 低估能力** | 我們的設定低估，benchmarks 和 anecdotes 正確 |
| **2. Benchmarks/Ancedotes 高估** | RCT 正確，benchmarks 過度樂觀 |
| **3. 互補證據** | 三者都正確，只是測量不同任務分布 |

## 與其他證據的對比

| 來源 | 任務類型 | 觀察 |
|------|---------|------|
| **本 RCT** | 4 個大型開源 codebase 的真實 PR | **慢 19%** |
| SWE-Bench Verified | 開源 PR + 自動測試 | 模型經常成功 |
| RE-Bench | 手作 AI 研究問題 | 模型經常成功 |
| Anecdotes | 多樣化 | 多數人覺得很有幫助 |

## 引用

```bibtex
@misc{metr-2025-early-2025-ai-experienced-os-dev-study,
    title = {Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity},
    author = {Joel Becker and Nate Rush and Beth Barnes and David Rein},
    howpublished = {https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/},
    year = {2025},
    month = {07}
}
```

## 數據集

- 完整數據：https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs