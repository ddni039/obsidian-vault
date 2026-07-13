---
title: 6 Orchestration Patterns（Dibia 2025 + EITT 2026）
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, orchestration-pattern, multi-agent, dibia-2025, eitt-2026, sequential, conditional, parallel, supervisor, handoff, conversation-driven, agent-architecture]
sources:
  - raw/articles/hermes-intelligence-reading-map-2026-07-13.md
related:
  - "[[wen-mou-plan-template-v1.1]]"
  - "[[chain-of-thought-reasoning]]"
confidence: high
---

# 6 Orchestration Patterns（Dibia 2025 + EITT 2026）

## 定義

**6 Orchestration Patterns** = 多智能體編排的 6 種標準模式，由 Victor Dibia 在《Designing Multi-Agent Systems》（2025）正式提出。每個 Plan 在 Hermes 必須明確標註屬於哪一個 pattern（TRAP-SOP-068 防 Pattern Mismatch）。

## 來源

- **Victor Dibia**（MSR / PicoAgents 作者）：Designing Multi-Agent Systems, 2025, Chapter 1
- **EITT Academy**：AI Agents 2026 Guide Agent Anatomy
- **Wikipedia**：Multi-agent system

## 6 大 Pattern 一覽

### Pattern 1：Sequential（順序型）

```
[Plan] → [Step A] → [Step B] → [Step C] → [Done]
```

- 嚴格依序
- 簡單可預測
- 適用：簡單任務、有明確前後依賴

### Pattern 2：Conditional（條件分支型）

```
[Plan] → {if X → Path A} → [Done]
       └ {else → Path B} → [Done]
```

- 條件決定路徑
- 靜態 routing
- 適用：if/else 邏輯

### Pattern 3：Parallel（並行型）

```
        ┌── [Sub-task 1] ──┐
[Plan] ─┤── [Sub-task 2] ──├─→ [Merge] → [Done]
        └── [Sub-task N] ──┘
```

- 多任務並行
- 結果合併
- 適用：3+ 獨立任務

### Pattern 4：Supervisor（監督型）

```
              ┌→ [Worker A] ─┐
[Plan] → [Supervisor] ─→ [Worker B] ─→ [Aggregate] → [Done]
              └→ [Worker C] ─┘
```

- Supervisor 動態派工
- 集中式決策
- 適用：多個 subagent

### Pattern 5：Handoff（交接型）

```
[Agent A] → [Agent B] → [Agent C] → ...
```

- Agent-to-agent 任務交接
- 模組化 domain expertise
- 適用：跨域任務

### Pattern 6：Conversation-driven（對話驅動型）

```
[User Input] → [State] → [Action] → [New State] → [Response]
```

- 對話歷史是狀態
- 上下文驅動
- 適用：多輪對話

## Pattern 決策表

| 場景 | Pattern |
|------|---------|
| 簡單依序 | Sequential |
| if/else | Conditional |
| 3+ 並聯 | Parallel |
| 動態派工 | Supervisor |
| 跨域交接 | Handoff |
| 多輪對話 | Conversation-driven |

## 5 大 Mismatch 情境

| 標的 | 實際 | 修正 |
|------|------|------|
| Parallel | Sequential | 改 sequential |
| Conditional | Parallel + Aggregate | 改 parallel |
| Supervisor | 無指定 workers | 列出 worker agents |
| Handoff | 無交接條件 | 明確觸發 |
| Conversation | 單輪 Q&A | 改 sequential |

## Hermes 對應

| Pattern | Hermes 現狀 |
|---------|------------|
| Sequential | ✅ 單一 Skill 呼叫 |
| Conditional | ✅ trigger 路由 |
| Parallel | ✅ `max_concurrent_children=3` |
| Supervisor | ✅ 主控 + subagent |
| Handoff | ⚠️ 缺口（需補）|
| Conversation-driven | ✅ WebUI 多輪對話 |

## 引用

- Victor Dibia (2025). Designing Multi-Agent Systems. Chapter 1
- EITT Academy (2026). AI Agents 2026 Guide

## 相關 SOP

- `references/orchestration-patterns.md` — 完整 SOP
- `references/wen-mou-plan-template.md` v1.1 — pattern 必填
- TRAP-SOP-068 — Pattern Mismatch