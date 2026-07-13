---
source_url: https://hermes-agent.nousresearch.com/docs/
ingested: 2026-07-01
---

# Hermes Agent Documentation

## Overview

**Hermes Agent** is a self-improving autonomous AI agent built by [Nous Research](https://nousresearch.com/). It's the only agent with a **built-in learning loop** — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of users across sessions.

Unlike coding copilots or chatbot wrappers, Hermes:
- Lives wherever you deploy it ($5 VPS, GPU cluster, or serverless)
- Communicates across platforms (Telegram, Discord, etc.)
- Doesn't require local infrastructure — interact while it runs on cloud VMs

## Installation

### Desktop Install (Windows/macOS)
Download the Hermes Desktop installer and run it.

### Command-Line Only
**Linux / macOS / WSL2 / Android (Termux):**
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Windows (native):**
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

### Quick Setup
After installation, run:
```bash
hermes setup --portal
```
This one OAuth covers a model plus all four Tool Gateway tools (web search, image generation, TTS, browser).

## Key Features

### Learning & Memory
- **Closed learning loop** — Agent-curated memory with periodic nudges, autonomous skill creation, skill self-improvement during use
- **FTS5 cross-session recall** with LLM summarization
- **Honcho dialectic user modeling** — builds user profiles across sessions
- **Memory System** — Persistent memory that grows across sessions
- **Skills System** — Procedural memory the agent creates and reuses

### Deployment & Platforms
| Category | Options |
|----------|---------|
| **Terminal Backends** | Local, Docker, SSH, Daytona, Singularity, Modal |
| **Serverless Ready** | Daytona and Modal hibernate when idle (near-zero cost) |
| **Messaging Platforms** | CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Weixin, QQ Bot, Yuanbao, BlueBubbles, Home Assistant, Microsoft Teams, Google Chat — **20+ platforms** |

### Model & Integration Support
- **Nous Portal** (recommended), OpenRouter, OpenAI, or any endpoint
- **MCP Integration** — Connect to MCP servers, filter their tools
- Full web control: Search, extract, browse, vision, image generation, TTS
- One subscription via Nous Portal bundles all web tools

### Advanced Capabilities
- **Scheduled automations** — Built-in cron with delivery to any platform
- **Parallelization** — Spawn isolated subagents for parallel workstreams
- **Programmatic Tool Calling** via `execute_code` — collapses multi-step pipelines into single inference calls
- **Open standard skills** — Compatible with agentskills.io, portable and shareable via Skills Hub
- **Research-ready** — Batch processing, trajectory export, RL training with Atropos
- **Voice Mode** — Real-time voice in CLI, Telegram, Discord, and Discord VC
- **Personality System** — Define Hermes' default voice with global `SOUL.md`
- **Context Files** — Project context that shapes every conversation

### Security
- Command approval, authorization, container isolation

## Quick Reference Links

| Topic | Link |
|-------|------|
| 🚀 Installation | 60-second install on Linux, macOS, WSL2, Windows, Android |
| 📖 Quickstart Tutorial | First conversation and key features |
| 🗺️ Learning Path | Docs organized by experience level |
| ⚙️ Configuration | Config file, providers, models, options |
| 💬 Messaging Gateway | Telegram, Discord, Slack, WhatsApp, Teams setup |
| 🔧 Tools & Toolsets | 60+ built-in tools |
| 🧠 Memory System | Persistent cross-session memory |
| 📚 Skills System | Agent-created procedural memory |
| 🔌 MCP Integration | Connect MCP servers safely |
| 🎙️ Voice Mode | Real-time voice interaction |
| 🎭 Personality & SOUL.md | Define agent personality |
