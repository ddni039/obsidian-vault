---
title: PEV Loop (Plan-Execute-Verify)
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, architecture, plan-execute-verify, phase-gate, reasoning-sandwich]
sources:
  - raw/articles/agent-harness-engineering-2026-07-13.md
related:
  - "[[agent-harness]]"
  - "[[phase-locking]]"
  - "[[hermes-tri-role]]"
confidence: high
---

# PEV Loop (Plan-Execute-Verify)

## 定義

**PEV Loop** = Plan → Execute → Verify 的三階段循環，是 **Reasoning Sandwich** 的核心架構。

> To break the **Compounding Error Cascade**, high-performing harnesses utilize the **Plan-Execute-Verify (PEV)** architecture. This creates a **Reasoning Sandwich** where high-reasoning models are used for planning and **Self-Verification Gates**, while cheaper models handle intermediate work.
> — Adnan Masood (2026)

## 數學必要性

```
Step accuracy 0.85 × 10 steps = (0.85)^10 ≈ 20%
```

**即使每步 85% 正確**，累積 10 步後整體成功率僅 20%。**這就是為什麼必須在每步做 verification。**

## 三大設計原則

### 1. 用最強模型做 Plan + Verify

- **規劃階段**：用最強推理模型（高 reasoning）
- **執行階段**：用便宜模型（low cost）
- **驗證階段**：用最強模型（嚴格 gate）

### 2. Self-Verification Gates

每個 phase 結束必須有驗證 gate：
- 失敗 → rollback + replan
- 通過 → 進入下一 phase

### 3. Compounding Error Prevention

- 不要相信中間步驟的「看起來 OK」
- 每步獨立驗證
- 累積錯誤會級聯放大

## Hermes 的 PEV 實作對應

| PEV 階段 | Hermes 角色 | 機制 |
|---------|-------------|------|
| **Plan** | C (Master) + B (Planner) | `routing-check` + Plan 文件 |
| **Execute** | H (Executor) | 唯一寫入端 `CODEC_EXEC` |
| **Verify** | H′ (Reviewer) + E (Auditor) | E-code 斷路器 + Review |

## 對應決策矩陣

| 情境 | 對應的 Hermes Phase |
|------|---------------------|
| Plan 不完整/矛盾 | E 階段介入，拒絕執行（`E-PLAN-CONTRADICTION`）|
| Execute 階段失敗 | `set -e` 捕獲 + Master 介入 |
| Verify 階段未通過 | E-code 阻斷（如 `E-SUBAGENT-CONTEXT-BLOATED`）|

## 與 Phase-Gating 的關係

**Phase Lock** = PEV Verify 階段的實體化實作：
- `PHASE_LOCK_PDF` 檔案 = Gate 的互斥鎖
- `craftsman_result.json` = Plan → Execute 產出
- `auditor_result.json` = Verify 階段的通關認證

## 對 Hermes 的啟示

| 啟示 | 建議 |
|------|------|
| Plan 階段必須用最強模型 | Hermes B 角色已對應 |
| 每個 Phase 結束必須驗證 | `auditor_core.py` 已實作 |
| 中間步驟用便宜模型 | H 子代理已採用（Haiku） |
| 累積錯誤必須早期偵測 | E-code 斷路器已實作 |

## 來源

- Adnan Masood, PhD：https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d
- 「Reasoning Sandwich」概念首次提出：Adnan Masood 2026-04-23