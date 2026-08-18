---
title: Hermes Messaging Gateway
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [agent, platform]
sources: [raw/articles/hermes-agent-docs-2026.md]
confidence: high
---

# Hermes Messaging Gateway

## Definition
Hermes Agent 的**統一跨平台消息系統**，通過一個 Agent instance 即可同時連接 20+ 不同的通訊平台。

## Supported Platforms
- **即時通訊:** Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost
- **企業通訊:** Microsoft Teams, Google Chat, DingTalk, Feishu, WeCom, Weixin, QQ Bot
- **其他:** Email, SMS, Yuanbao, BlueBubbles, Home Assistant

## Architecture Advantage
傳統 Agent 通常綁定單一介面（CLI 或特定 messenger），Hermes 的 messaging gateway 實現了：
- **Single brain, multiple bodies** — 一個 Agent instance 服務所有平台
- **Unified personality** — 跨平台保持一致的 voice 和 SOUL.md
- **Platform-specific optimizations** — 各平台差異化呈現
- **Cron delivery** — 排程任務可投放到任意平台

## Use Cases
- 跨時區團隊的統一 AI 助手
- 將 Hermes 部署在雲端，通過 Telegram/Discord 隨時喚醒
- 實現"永不停機"的 AI 服務

## Related Concepts
- [[hermes-agent]] — Messaging Gateway 的宿主
- [[hermes-skills-system]] — 跨平台一致的能力沉澱
- [[ai-agent]] — 更廣泛的 AI Agent 定義
