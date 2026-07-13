---
title: M1-Parallel — Microsoft Research Parallel Multi-Agent Framework
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [paper, arxiv, multi-agent, parallel-execution, m1-parallel, microsoft-research]
url: https://arxiv.org/abs/2507.08944
authors:
  - Enhao Zhang (Microsoft Research)
  - Erkang (Eric) Zhu
  - Gagan Bansal
  - Adam Fourney
  - Hussein Mozannar
  - Jack Gerrits
date: 2025-07-11
venue: arXiv preprint (ICML track)
license: arXiv.org perpetual non-exclusive license
---

# M1-Parallel — Source Material

## 摘要

M1-Parallel 是一個**並行執行多個 multi-agent teams**的框架，目標是降低延遲並提升任務完成率。

> Large language model (LLM)-based multi-agent systems have demonstrated remarkable promise for tackling complex tasks by breaking them down into subtasks that are iteratively planned, executed, observed, and refined. Despite their effectiveness, these systems often incur high latency because real-world problems frequently demand multiple iterative cycles of reasoning steps.

## 核心創新

### Event-driven Communication + Asynchronous Messaging

- 多 agent teams **concurrently** 跑多個獨立 solution paths
- 第一個 team 完成時 early terminate（saves time）
- 多 team 都完成後 aggregate results（boosts accuracy）

### 兩種策略

| 策略 | 速度 | 準確率 | 適用情境 |
|------|------|--------|---------|
| **Early Termination** | ⚡ **2.2× speedup** | = 單 agent | 時間敏感的批次任務 |
| **Aggregation** | 🐢 慢（所有 teams 都跑完） | 📈 **更高完成率** | 準確率優先的關鍵任務 |

## 關鍵實驗結果

來自 GAIA benchmark：
- **單 agent**：完成時間 3 分鐘（6 steps）或 13 分鐘（20 steps，失敗）
- **M1-Parallel (3 plans in parallel)**：取決於最快的 plan
- **Diversity experiments**：未觀察到比 repeated sampling 顯著優勢

## 與 Hermes `delegate_task` 的對應

| M1-Parallel | Hermes |
|-------------|--------|
| Multiple parallel plans | `delegate_task` with `background: true` |
| Event-driven messaging | 背景進程 → `notify_on_complete: true` |
| Early termination | 第一個完成即觸發 follow-up |
| Aggregation | 等所有 subagent 結果後整合 |
| 2.2× speedup | 實戰 P1/P2 階段已驗證（並聯 SOP） |

## 對 Hermes 的設計啟示

1. **Parallel Teams = 並聯 SOP**：當任務可拆分為 N 個獨立子任務時，使用 `max_concurrent_children=3` 並聯執行
2. **Early Termination**：對「先求有」的情境（如 quick code review）適用
3. **Aggregation**：對「求好」的情境（如文檔品質審計）適用
4. **Diversity vs Repeated Sampling**：現有 SOP 已採 Repeated Sampling 策略（每顆 skill 獨立派發），M1-Parallel 證明這在 LLM agent context 中已足夠

## 引用

```bibtex
@inproceedings{zhang2025m1parallel,
  title={Optimizing Sequential Multi-Step Tasks with Parallel LLM Agents},
  author={Zhang, Enhao and Zhu, Erkang and Bansal, Gagan and Fourney, Adam and Mozannar, Hussein and Gerrits, Jack},
  booktitle={arXiv preprint arXiv:2507.08944},
  year={2025}
}
```