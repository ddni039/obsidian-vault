---
title: Designing Multi-Agent Systems (Book)
created: 2026-07-13
updated: 2026-07-13
uid: e-3762efc3264e
type: entity
tags: [book, multi-agent, lvm-agent, parallel-execution, orchestration, victor-dibia]
sources:
  - raw/articles/designing-multiagent-systems-book-2026-07-13.md
related:
  - "[[victor-dibia]]"
  - "[[picoagents]]"
  - "[[m1-parallel-framework]]"
  - "[[agency-multi-agent-architecture]]"
confidence: high
---

# Designing Multi-Agent Systems (Book)

## 核心內容

**2025 年最具代表性的 multi-agent 設計書籍**，由 AutoGen 作者 Victor Dibia 撰寫。

**結構**：
- 15 章 / 395 頁 / 46 張手繪圖 / 185+ 程式碼片段
- 支援 5 種語言翻譯（英、法、德、西、日、中）

## 四大核心章節

### Part 1: Foundations
- Multi-agent 系統的核心概念
- 何時使用、何時**不**使用 multi-agent
- 設計模式（sequential / concurrent / group chat / hierarchical）

### Part 2: Building（從零實作）
- **PicoAgents** framework：完整的 lightweight library
- 涵蓋：agents / tools / memory / workflows / orchestration
- 185+ 程式碼片段，讀者可逐步跟著建構

### Part 3: Evaluating & Optimizing
- **LLM-as-judge** 評估方法
- 平行執行優化（**M1-Parallel** 論文為基礎）
- Persistence layer + checkpoint system
- OpenTelemetry 整合（Gen-AI semantic conventions）

### Part 4: Real-World Applications
- 完整案例研究：
  - Data analysis pipelines
  - Software engineering tasks
  - Information processing workflows

## 與 Hermes 的對應關係

| 書中概念 | Hermes 實作 | 狀態 |
|---------|------------|------|
| Multi-agent orchestration | [[agency-multi-agent-architecture]] + Hermes 五角色 | ✅ 已採用 |
| Plan-level parallelism | `delegate_task` + `background: true` | ✅ 已用於 P1/P2 階段 |
| Tool approval workflow | Plan-Gate-Review（E 階段御史） | ✅ 已實作 |
| Persistence layer | `fact_store`（holographic memory） | ✅ 已實作 |
| Memory tools | `MEMORY.md` + `USER.md` | ✅ 已實作 |
| Web UI + debug events | Dashboard (:9119) + WebUI (:8648) | ✅ 已實作 |

## 推薦閱讀路徑

依 Hermes 維護者角色，建議優先讀：
1. **Chapter 4-5**：Your First Agent + Tools & Memory
2. **Chapter 6**：Multi-agent Coordination
3. **Chapter 8**：Evaluation Patterns
4. **Chapter 11**：Production Considerations

## 授權與來源

- 書籍內容：© 2026 Victor Dibia（保留所有權利）
- 程式碼：[Apache-2.0](https://github.com/victordibia/designing-multiagent-systems/blob/main/LICENSE)
- 配套 repo：https://github.com/victordibia/designing-multiagent-systems（703 ⭐）