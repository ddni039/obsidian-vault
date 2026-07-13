---
title: Parallel Multi-Agent Execution
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [multi-agent, parallel-execution, orchestration, performance, m1-parallel]
sources:
  - raw/articles/m1-parallel-arxiv-2026-07-13.md
  - raw/articles/designing-multiagent-systems-book-2026-07-13.md
related:
  - "[[m1-parallel-framework]]"
  - "[[agency-multi-agent-architecture]]"
  - "[[hermes-subagent-delegation]]"
  - "[[picoagents]]"
confidence: high
---

# Parallel Multi-Agent Execution

## 概念定義

**Parallel Multi-Agent Execution** 是指**同時運行多個 multi-agent teams**（或單一 multi-agent 系統的多個獨立 plan）以降低延遲或提升準確率的執行模式。

由 **M1-Parallel** 論文（Microsoft Research, 2025-07）首次系統化提出。

## 兩種核心策略

### 1. Early Termination（速度優先）

```
Task → 啟動 N 個 parallel plans → 第一個完成 → 終止其餘
```

**優勢**：
- **2.2× speedup**（來自 M1-Parallel 實驗）
- 適合時間敏感的批次任務
- 與人類「先求有、再求好」的工作模式一致

**劣勢**：
- 犧牲了「多樣性帶來的準確度提升」機會
- 對於失敗 plan 不會 retry

### 2. Aggregation（準確率優先）

```
Task → 啟動 N 個 parallel plans → 等所有完成 → aggregate results
```

**優勢**：
- 提升任務完成率（特別是高難度任務）
- 不同 plan 可能互補錯誤

**劣勢**：
- 延遲 = max(plan latencies)
- 計算成本 ×N

## 關鍵發現（來自 M1-Parallel）

> Our experiments on complex tasks show that M1-Parallel with early termination achieves up to **2.2× speedup** while preserving accuracy.

> However, our experiments indicate that **diverse planning provides no clear advantage compared to repeated sampling**, likely due to the generation of suboptimal plans containing unnecessary steps intended solely to diversify the plans.

## 適用 vs 不適用情境

### ✅ 適合平行執行

| 任務類型 | 範例 |
|---------|------|
| 多個獨立檔案重構 | 71 顆 SKILL.md 拆分 |
| 多顆 skill frontmatter 補齊 | 25 顆缺 uid/status |
| 多個 PDF 視覺驗證 | 12 顆 PDF skill 三層邊界檢查 |
| 多模型評測 | 5 個核心檔案 SSoT 掃描 |
| 多來源研究彙整 | LLM wiki 多書籍攝入 |

### ❌ 不適合平行執行

| 任務類型 | 為何不行 |
|---------|---------|
| 有狀態依賴的工作流 | 步驟 N+1 依賴步驟 N 結果 |
| 共享檔案的批次修改 | 容易造成衝突（TRAP-SOP-010 已知） |
| 需精確控制執行順序的審計 | 違反審計完整性 |
| Token 預算極小（<80k）| 並聯會快速耗光預算 |

## Hermes 的並聯執行 SOP

### 設定

```yaml
# ~/.hermes/config.yaml
delegation:
  max_concurrent_children: 3   # 硬性限制
  max_spawn_depth: 1            # 子代理不嵌套
```

### 使用模式

```python
# 並聯派發（H 子代理）
delegate_task(
    goal="[任務描述]",
    toolsets=["file", "terminal"],
    background=True,             # 不阻塞
    notify_on_complete=True      # 完成時通知
)
```

### 真實案例：P2 階段 71 顆 Skill 拆分

```
批次 1（5 顆 >1000 行）→ 3 顆/輪 並聯，共 2 輪
批次 2（23 顆 500-1000 行）→ 3 顆/輪 並聯，共 8 輪
批次 3（38 顆 300-500 行）→ 3 顆/輪 並聯，共 13 輪
────────────────────────────────────────────────
總計 24 輪並聯完成 71 顆 skill 拆分
```

## 已知陷阱

- **TRAP-SOP-010**：`write_file` 截斷 + Master/H 並行衝突
- **Master 介入處理後**：必須清理痕跡或只補差異，避免 H 重做雙版本
- **Token 預算**：3 顆並聯 × 30k = 90k，已接近 Warning 閾值

## 推薦閱讀

- M1-Parallel 論文：https://arxiv.org/abs/2507.08944
- 《Designing Multi-Agent Systems》Chapter 6: Multi-agent Coordination
- Hermes [[sop-design-maintenance-errors]] §TRAP-SOP-010