---
title: AI Agent
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [agent, concept]
sources: []
confidence: high
---

# AI Agent

## Definition
AI Agent 是一種能自主規劃、執行多步驟任務的 AI系統，透過 tool use、MCP 或 plugin與外部世界互動。

## Core Components
- **Model:** LLM brain（GPT、Claude、MiniMax等）
- **Tools:** 可呼叫的 actions（搜尋、代碼執行、API呼叫）
- **Memory:** 跨session持久化記憶
- **Planning:** 任務分解與自我反思

## Key Frameworks
- [[hermes-agent]] — Nous Research, 多provider支援
- [[claude-code]] — Anthropic, 程式碼專用
- [[codex]] — OpenAI, 程式碼專用
- [[opencode]] — OpenCode, open model支援

## Related Concepts
- [[mcp]] — Model Context Protocol,工具標準化
- [[autonomous-coding]] — 自主編碼agent子領域

## Ecosystem Trends
- 各平台陸續推出 MCP Server（Google、TikTok、Meta）
- AI Agent 正在從簡單 chatbot 走向 complex task automation
- 2026年趨勢：agentic workflow、multi-agent協作
