---
title: METR 2026 AI 生產力追蹤（Late-2025 RCT + 2026 Survey）
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [paper, metr, research, ai-coding, productivity, late-2025, survey, 2026]
urls:
  - https://metr.org/blog/2026-02-24-uplift-update/
  - https://metr.org/blog/2026-05-11-ai-usage-survey/
authors:
  - Joel Becker
  - Nate Rush
  - Tom Cunningham
  - David Rein
  - Khalid Mahamud
venue: METR
date: 2026-02 + 2026-05
---

# METR 2026 追蹤研究 — Source Material

## 兩篇關鍵報告

| 報告 | 結論 |
|------|------|
| **2026-02-24 Uplift Update** | 重新設計實驗，發現 2025 下半年 AI 對開發者可能從「慢 19%」轉為「快 4-18%」 |
| **2026-05-11 AI Usage Survey** | 349 位技術工作者自我報告 **1.4-2× value uplift**、**3× speed** |

## Late-2025 RCT（2026-02 報告）

### 為何重新設計？

研究者發現原實驗有 5 大 selection effects 問題：

1. **招募困難**：開發者不願在「無 AI」條件下工作
2. **任務選擇偏差**：30-50% 開發者刻意避開 AI 拿手的任務
3. **降低補償**：$150/hr → $50/hr
4. **任務類型替代**：開發者選 AI-friendly 的任務
5. **時間測量失準**：開發者會在 AI agent 運行時做其他事

### 新實驗結果

| 群體 | 樣本 | 速度變化 | 信心區間 |
|------|------|---------|---------|
| 原始開發者（追蹤）| 10 | **快 18%** | -38% ~ +9% |
| 新開發者（2025 H2 加入）| 47 | **快 4%** | -15% ~ +9% |
| **平均（含全部）**| 57 | **快 ~11%** | -25% ~ +7% |

### 關鍵引言

> _"I'm torn. I'd like to help provide updated data on this question but also I really like using AI!"_
> — 早期 2025 開發者回應

> _"my head's going to explode if I try to do too much the old fashioned way because it's like trying to get across the city walking when all of a sudden I was more used to taking an Uber."_
> — Late-2025 新開發者

### 結論

> Late-2025 AI **likely accelerated** open-source developers, but **selection effects obscure the true speedup**.

## 2026 Survey（349 位技術工作者）

### 樣本結構

| 角色 | 人數 |
|------|------|
| 軟體工程師 | 87 |
| 研究人員 | 71 |
| 學術界/PhD 學生 | 129 |
| 創辦人/管理者 | 48 |
| 其他 | 14 |
| **總計** | **349** |

### 關鍵指標（中位數）

| 指標 | 數值 |
|------|------|
| **March 2026 value uplift** | **1.4-2×** |
| March 2026 speed uplift | **3×** |
| March 2025 value uplift（追溯）| 1.3× |
| March 2027 value uplift（預測）| 2.5× |

### METR 員工特別值得注意

> METR staff give the lowest change in value answers of any subgroup we study.

**原因**：METR 員工知道 perception vs reality 的落差（基於 2025 RCT 結論），所以自我報告更保守。

### 重要保留

> Importantly, survey results are not necessarily grounded in reality.

- 人對 counterfactual 問題的回答有偏差
- 我們 2025 研究發現，人們對 AI 速度影響的高估 **達 40 個百分點**

## METR 2025 → 2026 對比時間軸

```
2025 H1：RCT 實驗 → 發現 AI 慢 19%
2025 H2：Late RCT → 估計 AI 快 4-18%（但有 selection effects）
2026 Q1：Uplift Update → 認為 AI 從負轉正
2026 Q2：Survey → 自我報告 1.4-2× value，3× speed
```

## 數據集

- Late 2025 study 數據：https://github.com/METR/Measuring-Late-2025-AI-on-OSS-Devs
- Survey 連結：https://forms.gle/TNnafiPXetVHVYNQA

## 引用

```bibtex
@misc{metr-2026-uplift-update,
    title = {We are Changing our Developer Productivity Experiment Design},
    author = {Joel Becker and Nate Rush and Tom Cunningham and David Rein and Khalid Mahamud},
    howpublished = {https://metr.org/blog/2026-02-24-uplift-update/},
    year = {2026},
    month = {02}
}

@misc{metr-2026-ai-usage-survey,
    title = {Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity},
    author = {Joel Becker},
    howpublished = {https://metr.org/blog/2026-05-11-ai-usage-survey/},
    year = {2026},
    month = {05}
}
```