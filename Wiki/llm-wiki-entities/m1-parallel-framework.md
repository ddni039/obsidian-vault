---
title: M1-Parallel Framework
created: 2026-07-13
updated: 2026-07-13
uid: e-ced7de8f5f30
type: entity
tags: [framework, multi-agent, parallel-execution, microsoft-research, paper]
sources:
  - raw/articles/m1-parallel-arxiv-2026-07-13.md
related:
  - "[[parallel-multi-agent-execution]]"
  - "[[designing-multi-agent-systems-book]]"
confidence: high
---

# M1-Parallel Framework

## 簡介

**M1-Parallel** 是 Microsoft Research 在 2025 年 7 月提出的 multi-agent 並聯執行框架，來自 arXiv 論文 [2507.08944](https://arxiv.org/abs/2507.08944)。

## 核心貢獻

1. **首次系統化**「並行執行多個 multi-agent teams」概念
2. **2.2× speedup**（early termination 模式）
3. **證實 diversity vs repeated sampling**：diversity 不顯著優於 repeated sampling
4. **Event-driven 訊息模型**：支援大規模並行

## 兩種模式

### Early Termination
```
啟動 N 個 plans → 第一個完成 → 終止其餘
實驗結果：2.2× speedup，accuracy 不降
```

### Aggregation
```
啟動 N 個 plans → 等所有完成 → aggregate
實驗結果：completion rate 提升，latency ×N
```

## 關鍵實驗設定

- **Benchmark**：GAIA（general AI assistants benchmark）
- **典型任務**：「2000-2009 年間 Mercedes Sosa 出了幾張錄音室專輯？」
- **單 agent baseline**：3 分鐘（成功）或 13 分鐘（失敗）
- **Parallel (3 plans)**：取最快的 plan 結果

## 作者群

- **Enhao Zhang**（Microsoft Research）
- **Erkang (Eric) Zhu**
- **Gagan Bansal**
- **Adam Fourney**
- **Hussein Mozannar**
- **Jack Gerrits**

## 與 Hermes `delegate_task` 的對應

| M1-Parallel | Hermes |
|-------------|--------|
| Multiple parallel plans | `delegate_task` 並聯派發 |
| Event-driven comm | `notify_on_complete=True` |
| Early termination | 第一個完成觸發 follow-up |
| Aggregation | 等所有 subagent 結果後整合 |
| 2.2× speedup | 實戰已驗證（P1/P2 並聯 SOP） |

## 對 Hermes 設計的啟示

| 設計建議 | 理由 |
|---------|------|
| `max_concurrent_children=3` 已合理 | 3 個 plan 平行 = 3× latency reduction，token 仍可控 |
| 採用 early termination 模式 | 第一個完成即觸發下一步，省時間 |
| 失敗 subagent 不自動 retry | M1-Parallel 證明 diversity 幫助不大，retry 可能擴大錯誤 |
| 持久化每個 plan 結果 | 對 aggregation 模式必要 |

## 引用

```bibtex
@inproceedings{zhang2025m1parallel,
  title={Optimizing Sequential Multi-Step Tasks with Parallel LLM Agents},
  author={Zhang, Enhao and Zhu, Erkang and Bansal, Gagan and Fourney, Adam and Mozannar, Hussein and Gerrits, Jack},
  booktitle={arXiv preprint arXiv:2507.08944},
  year={2025}
}
```