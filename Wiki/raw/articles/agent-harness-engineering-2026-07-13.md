---
title: Agent Harness Engineering — Adnan Masood (2026)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [paper, agent-harness, control-plane, runtime, mcp, a2a, adnan-masood]
url: https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d
author: Adnan Masood, PhD (Stanford / Harvard / Microsoft Regional Director)
date: 2026-04-23
length: 24 min read
license: Medium article (text mining for research allowed)
---

# Agent Harness Engineering — Source Material

## 核心定義

> **Agent Harness** = 包圍 LLM 的 scaffolding，把它變成可工作的 agent
> 包含：loop、tool calls、context management、memory、guardrails、tracing

**核心等式**：`{Agent} = {Model} + {Harness}`

> The model functions as a stateless token predictor providing raw cognitive reasoning, while the harness comprises the Runtime Software Infrastructure that coordinates tool dispatch, context management, and safety enforcement.

## 7 大核心 Takeaways（必讀）

### Takeaway 1: Your Model Isn't the Problem — Your Harness Is

- 88% 企業 AI agent 專案**未達生產**
- 65% 失敗來自 **Harness Defects**：Context Drift / Schema Misalignment / State Degradation
- 純優化模型效益遞減

### Takeaway 2: Tenfold Economic Differential（成本 10 倍差距）

- KV-cache Locality + Semantic Routing → 成本從 $3.00/MTok 降至 $0.30/MTok
- **Prefix Stability**：保持 system instructions 和 history 穩定，防止 cache 失效
- **具體戰術**：移除 prompt 頂部的動態元素（如秒級時間戳）→ 確保 tokens 持續被 cache

### Takeaway 3: Death of the "Chaotic Swarm"

- 不受約束的多 agent mesh 已死
- 生產環境轉向 **Bounded, Deterministic Workflows**
- **Supervisor Pattern + Strict Phase-Gating**
- Human-on-the-loop（高風險補救需人為授權）

### Takeaway 4: "USB-C" Moment for AI

兩個關鍵協議標準化：
- **MCP (Model Context Protocol)**：Agent-to-Tool 垂直互動
- **A2A (Agent-to-Agent)**：水平委派

### Takeaway 5: Agent Legibility & Environment Engineering

- 失敗原因：繳 **Orientation Tax**（耗數千 tokens 探索陌生環境）
- 解決方案：**Structural Code Mapping**（tree-sitter / RepoMapper）
- **Maturity Level 3** = Observable Runtime（session checkpointing + 顯式 filesystem memory）

### Takeaway 6: "Reasoning Sandwich" + PEV Loops

- **PEV = Plan-Execute-Verify**
- 高推理模型用於 planning 和 self-verification gates
- 便宜模型做中間工作
- **數學必要性**：若無驗證，0.85^10 ≈ 20%（誤差級聯導致系統失敗）

### Takeaway 7: Avoiding "Context Rot" with Virtual Memory

- 大型 tool outputs 導致 Context Rot（注意力退化）
- **Virtualized Filesystem**：externalize memory 到 `AGENTS.md` 或 `todo.md`
- **Matryoshka principle**（俄羅斯娃娃）：context layering

## 與 Hermes 的對應

| Harness 概念 | Hermes 實作 | 評估 |
|-------------|------------|------|
| Loop | conversation_loop + agent.conversation_loop | ✅ |
| Tool calls | `delegate_task` + MCP | ✅ |
| Context management | `distill` / token budget | ✅ |
| State / memory | `fact_store` + `MEMORY.md` | ✅ |
| Safety / guardrails | `RULES.md` + E-code 斷路器 | ✅ |
| Tracing | `~/.hermes/logs/` | ✅ |
| Phase-Gating | `PHASE_LOCK_PDF.lock` + Phase Routing | ✅ |
| Supervisor Pattern | C 角色（Master）+ routing-check | ✅ |
| PEV Loop | Plan → H (Executor) → E (Auditor) → C | ✅ |
| Virtualized Filesystem | `~/.hermes/` 結構 | ✅ |
| MCP Standardization | MCP servers (6+ in config) | ✅ |
| A2A Protocol | subagent 委派 + notification | ⚠️ 部分 |

## 對 Hermes 的啟示（推薦行動）

| 優先級 | 行動 | 理由 |
|--------|------|------|
| 🟡 中 | 移除 prompt 中的秒級時間戳 | 提升 KV-cache hit rate |
| 🟡 中 | 為 subagent 加入 independent identity | 對應 Per-agent identity |
| 🟢 低 | 評估 PEV loop 對 E 階段審計的影響 | 已部分實作 |
| 🟢 低 | 研究 Structural Code Mapping 工具 | tree-sitter 整合 |