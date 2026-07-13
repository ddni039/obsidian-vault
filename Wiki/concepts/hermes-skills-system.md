---
title: Hermes Skills System
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [agent, workflow]
sources: [raw/articles/hermes-agent-docs-2026.md]
confidence: high
---

# Hermes Skills System

## Definition
Hermes Agent 的**程序性記憶系統**，將從經驗中學習到的操作模式封裝為可複用的 Skills。

## Overview
不同於 static prompt templates，Hermes Skills 是動態創建和改進的：
- Agent 從成功案例中**自動提取** skill
- Skills 在使用中**持續優化**
- Skills 可被**跨 session 複用**

## Key Characteristics
- **Autonomous creation** — 不需要手動定義，Hermes 自動生成
- **Self-improvement** — 每次使用都是優化機會
- **Open standard** — 與 agentskills.io 相容
- **Skills Hub** — 可分享和發現 community skills
- **Portable** — 可導入導出，跨部署迁移

## Relationship to Memory System
Skills System 建立在 Memory System 之上：
- Memory 提供**原材料**（ raw experiences）
- Skills System 將記憶**結構化**（ organized procedures）
- Together they enable **closed-loop learning**

## Related Concepts
- [[hermes-learning-loop]] — Skills 是學習迴圈的產出
- [[hermes-agent]] — Skills System 的宿主
- [[mcp-model-context-protocol]] — 外部工具擴展的互補機制
