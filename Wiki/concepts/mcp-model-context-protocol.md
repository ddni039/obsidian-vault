---
title: MCP (Model Context Protocol)
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [tool, standard]
sources: [raw/articles/hermes-agent-docs-2026.md]
confidence: high
---

# MCP (Model Context Protocol)

## Definition
**Model Context Protocol** 是由 Anthropic 於 2024 年 11 月發布的**開放標準**，旨在標準化 AI 模型與外部數據源、工具之間的安全雙向連接。

## Overview
MCP 提供了一種標準化方式，讓應用程式：
- 與語言模型共享上下文資訊
- 向 AI 暴露工具和能力
- 實現安全的 AI-工具整合

## Key Characteristics
- **開放標準** — 任何人都可以實現和使用
- **雙向連接** — 不僅是 tool calling，還包括 context 共享
- **安全優先** — 設計時考慮了安全性
- **跨平台** — 不綁定特定 AI provider

## Relationship to Hermes Agent
Hermes Agent 原生支援 MCP Integration，可連接 MCP servers 並過濾其 tools。這使得 Hermes 能夠：
- 擴展工具集到任何 MCP-compatible server
- 作為統一介面整合多個 MCP 資料來源

## Relationship to Claude Code
Claude Code 也支援 MCP，被視為其主要擴展機制之一。

## Ecosystem
- Anthropic 官方支援
- 越來越多 tools 和 platforms採用
- 與 OpenAI tool use、GPTs 等形成競爭格局

## Open Questions
- MCP 與 OpenAI 的 tool use 標準誰會勝出？
- 企業採用程度與標準化進程

## Related Concepts
- [[ai-agent]] — AI Agent 定義與核心元件
- [[hermes-agent]] — 原生支援 MCP 的自主 agent
- [[claude-code]] — 同樣支援 MCP 的 coding agent
