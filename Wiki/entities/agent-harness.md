---
title: Agent Harness
created: 2026-07-13
updated: 2026-07-13
uid: e-313803951f9b
type: entity
tags: [concept, runtime, infrastructure, agent-harness, control-plane]
sources:
  - raw/articles/agent-harness-engineering-2026-07-13.md
related:
  - "[[agent-control-plane]]"
  - "[[agent-skills-with-anthropic-course]]"
  - "[[pev-loop]]"
confidence: high
---

# Agent Harness

## 定義

**Agent Harness** = 包圍 LLM 的 scaffolding，把它變成可工作的 agent。

**核心等式**：`{Agent} = {Model} + {Harness}`

> The model functions as a stateless token predictor providing raw cognitive reasoning, while the harness comprises the Runtime Software Infrastructure that coordinates tool dispatch, context management, and safety enforcement.
> — Adnan Masood (2026)

## 6 大核心職責

| 職責 | 描述 | 失敗症狀 |
|------|------|---------|
| **The Loop** | 反覆呼叫 model、解析 output、執行 tool、feeding back | 無限循環、無收斂 |
| **Tool/Function Calling** | 暴露能力（search、code、MCP）並 routing | Tool 路由錯誤 |
| **Context Management** | system prompts、history、RAG、compaction | Context Drift |
| **State and Memory** | scratchpads、task lists、short/long-term | State Degradation |
| **Control Flow** | retries、timeouts、budget、stop | 失控、無界消耗 |
| **Safety & Observability** | guardrails、approval、logging、tracing | 風險、不可審計 |

## 統計事實

- **88%** 企業 AI agent 專案未達生產
- **65%** 失敗來自 Harness Defects（Context Drift / Schema Misalignment / State Degradation）
- **80%** 公司已發生未授權 AI 動作
- **95%** AI 試點無 P&L 影響

## 與 Hermes 的對應（已實作）

| Harness 職責 | Hermes 對應 |
|-------------|------------|
| Loop | `conversation_loop.py` |
| Tool Calling | MCP + `delegate_task` |
| Context Management | `distill` + token budget |
| State/Memory | `fact_store` + `MEMORY.md` |
| Control Flow | `RULES.md` E-code + child_timeout_seconds |
| Safety/Observability | E 階段御史 + logs |

## 對 Hermes 的設計啟示（推薦）

1. **Prefix Stability**：移除 prompt 動態元素（如秒級時間戳）→ KV-cache 命中
2. **MCP Standardization**：繼續推進 MCP 採用（已有 6+ servers）
3. **PEV Loop**：Plan → Execute → Verify（已有 Phase Lock 機制）
4. **Virtualized Filesystem**：用 `~/.hermes/` 結構作為 externalized memory（已實作）

## 來源

- Adnan Masood, PhD：https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d
- 日期：2026-04-23
- 長度：24 min read