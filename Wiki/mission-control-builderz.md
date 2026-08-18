---
UID: 20260610-mission-control-builderz
STATUS: Active
TYPE: Data
tags: [ai-agent, orchestration, openclaw, nextjs, sqlite, multi-agent, dashboard, builderz-labs]
---

# Builderz Labs Mission Control

## 1. Summary

**Mission Control** is an open-source AI agent orchestration dashboard by Builderz Labs. It provides a self-hosted fleet management platform for coordinating multi-agent workflows, task dispatch, and cost tracking — with zero external dependencies, powered by SQLite.

> Not affiliated with Nintendo Switch's MissionControl (ndeadly).

| Attribute | Value |
|-----------|-------|
| Stars | 5.3k |
| Forks | 907 |
| Language | TypeScript |
| Framework | Next.js 16, React 19 |
| Database | SQLite (better-sqlite3) |
| License | MIT |
| Latest Version | 2.0.1 (2026-03-18) |
| Last Commit | 2026-05-31 |

---

## 2. Core Functionality

Mission Control serves as a unified control plane for managing AI agent fleets across multiple gateways. Key capabilities include:

- **32-Panel Dashboard**: Tasks, Agents, Skills, Logs, Tokens, Memory, Security, Cron, Alerts, Webhooks, Pipelines — all in a single-page SPA
- **Zero External Dependencies**: Single `pnpm start` execution; no Redis or Postgres required
- **Real-time Updates**: WebSocket + SSE + intelligent polling (pauses when tab is inactive)
- **RBAC System**: Viewer / Operator / Admin roles with Google Sign-In support
- **Skills Hub**: Browse, install, and security-scan skills from ClawdHub / skills.sh
- **Multi-Gateway Support**: Connect multiple agent gateways simultaneously — OpenClaw, CrewAI, LangGraph, AutoGen, Claude SDK
- **Quality Gates**: Aegis review system requiring sign-off before task completion
- **Claude Code Bridge**: Read-only integration surfacing Claude Code team tasks, sessions, and configuration

### Agent Connection Methods

```
MCP Server (recommended) → mc:mcp script
TUI → mc:tui script
CLI → mc-cli.cjs
REST API → /api/agents/register
```

### Task Lifecycle

```
inbox → assigned → in_progress → review → done
                          ↓              ↓
                    rejected (retry)   done
                          ↓
                    failed (timeout/retry exhausted)
```

---

## 3. Architecture

### Frontend Stack
- Next.js 16 (App Router)
- React 19
- TypeScript 5.7
- Tailwind CSS 3.4
- Zustand (state management)
- Recharts / Reagraph (visualization)
- xterm.js (terminal)
- @radix-ui (UI components)

### Backend Stack
- Node.js >= 22
- better-sqlite3 (database)
- pino (logging)
- ws (WebSocket)
- zod (validation)
- node-pty (pseudo-terminal)

### DevOps
- pnpm
- Vitest (unit tests)
- Playwright (E2E)
- Docker / docker-compose

### Key Directory Structure
```
src/app/          Next.js pages + API routes
src/components/   UI panels
src/lib/          Core logic, database
.data/            SQLite DB + runtime state (gitignored)
scripts/          Install, deploy, diagnostic scripts
docs/             Documentation
```

### API Scale
OpenAPI 3.1 specification with 101 REST endpoints, documented at `/api-docs` (Scalar UI).

---

## 4. Integration Points

| Feature | Hermes Agent | Mission Control |
|---------|-------------|-----------------|
| Agent fleet management | ✅ | ✅ |
| Task dispatch | ✅ | ✅ |
| Personality definition | ✅ (SOUL.md) | ✅ (SOUL.md) |
| Skills Hub | ✅ (skills/) | ✅ (Skills Hub) |
| SQLite storage | ❌ (in-memory) | ✅ |
| Multi-agent workflows | ✅ | ✅ |
| Cron scheduling | ✅ (cronjob) | ✅ |
| Cost tracking | ❌ | ✅ |

---

## 5. Operational Considerations

### Security Mechanisms
- CSPRNG password generation
- CSP nonce-based policy (no `unsafe-inline`)
- Rate limiting: Login 5/min, Mutations 60/min, Reads 120/min
- Trust scoring / Secret detection
- SSRF + path traversal rules
- Hardened Docker Compose (read-only filesystem, capability dropping, HSTS)

### Installation

```bash
git clone https://github.com/builderz-labs/mission-control.git
cd mission-control
bash install.sh --local     # Local mode
# or
docker compose up           # Docker mode
```

Environment variables `AUTH_SECRET`, `API_KEY`, `AUTH_USER`, `AUTH_PASS` are auto-generated.

### Similarity to Hermes Agent
Mission Control shares architectural DNA with Hermes Agent — both orchestrate multi-agent fleets, support skill-based extensibility, and provide cron-based scheduling. Key differentiators: Hermes Agent uses in-memory storage (vs SQLite), lacks built-in cost tracking, and is designed for CLI-first interaction.

---

**Last updated: 2026-06-10**
