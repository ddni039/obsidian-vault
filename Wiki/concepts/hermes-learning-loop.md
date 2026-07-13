---
title: Hermes Learning Loop
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [agent, workflow]
sources: [raw/articles/hermes-agent-docs-2026.md]
confidence: high
---

# Hermes Learning Loop

## Definition
Hermes Agent 的**閉環學習系統**，是其區別於其他 AI Agent 的核心特性。不同於一次性使用的 tool，Hermes 能從每次交互中學習並持續改進。

## Core Components

### 1. Memory System
- **Persistent cross-session memory** — 記憶跨 session 持久化
- **FTS5 cross-session recall** — 基於 FTS5 的精確全文檢索
- **LLM summarization** — 自動摘要長程記憶
- **Honcho user modeling** — dialectic 方式構建用戶 profile

### 2. Skills System
- **Autonomous skill creation** — 從經驗中自動創建 skills
- **Skill self-improvement during use** — 使用過程中持續優化
- **Procedural memory** — 將操作經驗轉化為可複用的技能
- **Open standard** — 與 agentskills.io 相容，Skills Hub 共享

### 3. Agent-Curated Memory
- **Periodic nudges** — 主動提醒自己保留重要資訊
- **Self-nudging** — Agent 主動 nudge 自己 persist 知識

## How It Works
1. 用戶與 Hermes 交互
2. 重要資訊被自動 capture 到 memory
3. 當類似的任務出現，Hermes 檢索相關記憶
4. 從記憶中提取 pattern，創建或更新 skill
5. 未來遇到類似任務時，直接應用 skill
6. 過程中持續優化 skill quality

## What Makes It Unique
| 特性 | Hermes | 傳統 Copilot |
|------|--------|-------------|
| 跨 session 記憶 | ✅ 原生 | ❌ 無 |
| 自動創建 skills | ✅ | ❌ |
| 使用中自我改進 | ✅ | ❌ |
| 用戶行為建模 | ✅ Honcho | ❌ |

## Related Concepts
- [[hermes-agent]] — 實現此學習迴圈的 AI Agent
- [[ai-agent]] — AI Agent 的一般定義
- [[mcp-model-context-protocol]] — Hermes 的工具擴展標準
