\# 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

\> \*\*A complete AI agency at your fingertips\*\* - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

\[!\[GitHub stars\](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)\](https://github.com/msitarzewski/agency-agents)
\[!\[License: MIT\](https://img.shields.io/badge/License-MIT-yellow.svg)\](https://opensource.org/licenses/MIT)
\[!\[PRs Welcome\](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)\](https://makeapullrequest.com)
\[!\[Sponsor\](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github)\](https://github.com/sponsors/msitarzewski)

\-\-\-

\## 🚀 What Is This?

Born from a Reddit thread and months of iteration, \*\*The Agency\*\* is a growing collection of meticulously crafted AI agent personalities. Each agent is:

\- \*\*🎯 Specialized\*\*: Deep expertise in their domain (not generic prompt templates)
\- \*\*🧠 Personality-Driven\*\*: Unique voice, communication style, and approach
\- \*\*📋 Deliverable-Focused\*\*: Real code, processes, and measurable outcomes
\- \*\*✅ Production-Ready\*\*: Battle-tested workflows and success metrics

\*\*Think of it as\*\*: Assembling your dream team, except they're AI specialists who never sleep, never complain, and always deliver.

\-\-\-

\## ⚡ Quick Start

\### Option 1: Use with Claude Code (Recommended)

\`\`\`bash
\# Install all agents to your Claude Code directory
./scripts/install.sh --tool claude-code

\# Or manually copy a category if you only want one division
cp engineering/\*.md ~/.claude/agents/

\# Then activate any agent in your Claude Code sessions:
\# "Hey Claude, activate Frontend Developer mode and help me build a React component"
\`\`\`

\### Option 2: Use as Reference

Each agent file contains:
\- Identity & personality traits
\- Core mission & workflows
\- Technical deliverables with code examples
\- Success metrics & communication style

Browse the agents below and copy/adapt the ones you need!

\### Option 3: Use with Other Tools (GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Kimi Code, Codex)

\`\`\`bash
\# Step 1 -- generate integration files for all supported tools
./scripts/convert.sh

\# Step 2 -- install interactively (auto-detects what you have installed)
./scripts/install.sh

\# Or target a specific tool directly
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool opencode
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool cursor
./scripts/install.sh --tool aider
./scripts/install.sh --tool windsurf
./scripts/install.sh --tool kimi
./scripts/install.sh --tool codex
\`\`\`

\*\*Install only the teams you need\*\* (not everyone wants all 16 divisions):

\`\`\`bash
./scripts/install.sh # interactive wizard: pick tools + teams
./scripts/install.sh --tool claude-code --division engineering,security
./scripts/install.sh --tool cursor --agent frontend-developer,ui-designer
./scripts/install.sh --list teams # see every team + agent count
./scripts/install.sh --tool opencode --division engineering --dry-run
\`\`\`

\> \*\*OpenCode note:\*\* OpenCode's runtime currently registers only ~119 agents and silently drops the rest (\[upstream bug\](https://github.com/anomalyco/opencode/issues/27988)). Installing a subset with \`--division\` keeps you under that limit. The installer warns you when a selection would exceed it.

See the \[Multi-Tool Integrations\](#-multi-tool-integrations) section below for full details.

\-\-\-

\## 🎨 The Agency Roster

\### 💻 Engineering Division

Building the future, one commit at a time.

\| Agent \| Specialty \| When to Use \|
\|-------\|-----------\|-------------\|
\| 🎨 \[Frontend Developer\](engineering/engineering-frontend-developer.md) \| React/Vue/Angular, UI implementation, performance \| Modern web apps, pixel-perfect UIs, Core Web Vitals optimization \|
\| 🏗️ \[Backend Architect\](engineering/engineering-backend-architect.md) \| API design, database architecture, scalability \| Server-side systems, microservices, cloud infrastructure \|
\| 📱 \[Mobile App Builder\](engineering/engineering-mobile-app-builder.md) \| iOS/Android, React Native, Flutter \| Native and cross-platform mobile applications \|
\| 🤖 \[AI Engineer\](engineering/engineering-ai-engineer.md) \| ML models, deployment, AI integration \| Machine learning features, data pipelines, AI-powered apps \|
\| 🚀 \[DevOps Automator\](engineering/engineering-devops-automator.md) \| CI/CD, infrastructure automation, cloud ops \| Pipeline development, deployment automation, monitoring \|
\| ⚡ \[Rapid Prototyper\](engineering/engineering-rapid-prototyper.md) \| Fast POC development, MVPs \| Quick proof-of-concepts, hackathon projects, fast iteration \|
\| 💎 \[Senior Dev

[Content truncated — showing first 5,000 of 72,341 chars. LLM summarization timed out. To fix: increase auxiliary.web_extract.timeout in config.yaml, or use a faster auxiliary model. Use browser_navigate for the full page.]