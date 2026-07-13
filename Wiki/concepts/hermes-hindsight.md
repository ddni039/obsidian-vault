---
title: Hindsight Memory Provider
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [agent, tool, memory, hermes]
sources: [raw/articles/hermes-hindsight-readme-2026.md]
confidence: high
---

# Hindsight Memory Provider

## Overview

Long-term memory plugin for Hermes Agent with knowledge graph, entity resolution, and multi-strategy retrieval.

**Repository:** NousResearch/hermes-agent
**Path:** `plugins/memory/hindsight/`
**Client Version:** `>= 0.6.1`

## Deployment Modes

| Mode | Requirements | Daemon |
|------|-------------|--------|
| Cloud | API key from vectorize.io | No |
| Local Embedded | LLM API key (any OpenAI-compatible) | Yes, auto-start/stop |
| Local External | Running Hindsight instance (HTTP) | No |

Local Embedded mode spins up a PostgreSQL-backed daemon that auto-starts on first use and stops after **5 minutes of inactivity**.

## Knowledge Architecture

Three fact types (configurable via `recall_types`):

| Type | Description | Density |
|------|-------------|---------|
| `observation` | **Default.** Consolidated, deduplicated beliefs grounded in evidence. Refined as new facts arrive. | High |
| `world` | Individual raw facts | Low |
| `experience` | Individual experience records | Low |

`observation` 是預設值，因為 per token 密度最高，避免餵給 model 多個已被單一 observation 總結的 raw facts。

## Tools

| Tool | Function |
|------|----------|
| `hindsight_retain` | Store info with auto entity extraction |
| `hindsight_recall` | Semantic + entity graph multi-strategy search |
| `hindsight_reflect` | Cross-memory LLM synthesis |

## Key Config

- `bank_id_template`: `{profile}`, `{workspace}`, `{platform}`, `{user}`, `{session}` 動態命名內存庫
- `recall_budget`: `low` / `mid` / `high` — recall 徹底度
- `auto_recall`: 每次 turn 前自動 inject memories
- `memory_mode`: `hybrid` (auto + tools) / `context` (auto only) / `tools` (tools only)

## Comparison: Hindsight vs Hermes Skills System

|| Dimension | Hermes Skills | Hindsight |
|-----------|--------------|-----------|
| Type | Procedural memory (how-to) | Observational memory (facts/beliefs) |
| Update | Manual, agent-authored | Automatic, evidence-grounded |
| Recall | Skill activation on trigger | Auto-inject before each turn |
| Storage | Markdown files in `~/.hermes/skills/` | Vector database (PostgreSQL + embeddings) |

## Gap Analysis: Distribution Shift Monitoring

**缺口（2026-07-11 研究發現）：**

Hindsight 是被動式長期記憶，**不提供主動的 distribution shift 檢測**。

| 維度 | DMLS Ch8 定義 | Hindsight 現況 |
|------|-------------|--------------|
| Covariate shift | P(X) 變化檢測 | ❌ 無主動 alert |
| Label shift | P(Y) 變化檢測 | ❌ 無主動 alert |
| Concept drift | P(Y\|X) 變化檢測 | ⚠️ 僅被動紀錄，無趨勢分析 |

**需要的組件（缺口）：**
- PSI（Population Stability Index）驅動的 alert
- 歷史記憶的趨勢視覺化
- 與 [[hermes-learning-loop]] 整合：當 drift 超過閾值時自動觸發 skill 重新學習

## Relationship

- [[hermes-agent]]
- [[hermes-learning-loop]]
- [[mcp-model-context-protocol]]
