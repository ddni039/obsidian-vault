---
UID: 20260610-builderz-mission-control
STATUS: Active
TYPE: Tool
tags: [ai-agent, orchestration, openclaw, nextjs, sqlite, multi-agent, dashboard]
---

# Builderz Labs Mission Control — 深度分析

## 1. Summary

**Open-source AI agent orchestration dashboard.** 自部署的代理車隊管理平台，支援任務派遣、成本追蹤、多代理工作流協調，零外部依賴，SQLite 驅動。

> 與 Nintendo Switch 的 MissionControl（ndeadly）是完全不同的專案。

---

## 2. 核心定位

| 維度 | 描述 |
|------|------|
| Stars | 5.3k |
| Forks | 907 |
| 語言 | TypeScript |
| 框架 | Next.js 16, React 19 |
| 資料庫 | SQLite (better-sqlite3) |
| 授權 | MIT |
| 最新版本 | 2.0.1（2026-03-18）|
| 最近提交 | 2026-05-31 |

---

## 3. 功能架構

### 3.1 32 面板系統

Tasks、Agents、Skills、Logs、Tokens、Memory、Security、Cron、Alerts、Webhooks、Pipelines 等，單頁 SPA。

### 3.2 核心特色

- **Zero 外部依賴**：SQLite，單行 `pnpm start` 執行，無 Redis/Postgres
- **即時更新**：WebSocket + SSE + 智慧輪詢（離開時暫停）
- **RBAC**：Viewer / Operator / Admin 三級角色，支援 Google Sign-In
- **Skills Hub**：從 ClawdHub / skills.sh 瀏覽、安裝、安全掃描技能
- **多 Gateway**：同時連接多個代理閘道，支援 OpenClaw / CrewAI / LangGraph / AutoGen / Claude SDK
- **Quality Gates**：Aegis 審查系統，任務完成前必須通過簽核
- **Claude Code Bridge**：唯讀整合 surfacing Claude Code 團隊任務、工作階段、配置

### 3.3 代理接入方式

```
MCP Server（推薦）→ mc:mcp script
TUI → mc:tui script
CLI → mc-cli.cjs
REST API → /api/agents/register
```

### 3.4 任務生命週期

```
inbox → assigned → in_progress → review → done
                          ↓              ↓
                    rejected (重試)   done
                          ↓
                    failed (超時/重試耗盡)
```

---

## 4. 技術棧

### 前端
- Next.js 16 (App Router)
- React 19
- TypeScript 5.7
- Tailwind CSS 3.4
- Zustand (狀態管理)
- Recharts / Reagraph (視覺化)
- xterm.js (終端)
- @radix-ui (UI 元件)

### 後端
- Node.js >= 22
- better-sqlite3 (DB)
- pino (日誌)
- ws (WebSocket)
- zod (驗證)
- node-pty (pseudo-terminal)

### DevOps
- pnpm
- Vitest (單元測試)
- Playwright (E2E)
- Docker / docker-compose

---

## 5. API 規模

OpenAPI 3.1 規範，101 個 REST 端點，文件位於 `/api-docs`（Scalar UI）。

---

## 6. 安全機制

- CSPRNG 密碼產生
- CSP nonce-based（移除 `unsafe-inline`）
- 速率限制（Login 5/min、Mutations 60/min、Reads 120/min）
- 信任評分 / Secret 檢測
- SSRF + 路徑穿越 規則
- Hardened Docker Compose（唯讀 filesystem、capability dropping、HSTS）

---

## 7. 安裝方式

```bash
git clone https://github.com/builderz-labs/mission-control.git
cd mission-control
bash install.sh --local     # 本機模式
# 或
docker compose up            # Docker 模式
```

環境變數：`AUTH_SECRET`、`API_KEY`、`AUTH_USER`、`AUTH_PASS` 自動生成。

---

## 8. 關鍵目錄結構

```
src/app/          Next.js pages + API routes
src/components/   UI panels
src/lib/          核心邏輯、資料庫
.data/            SQLite DB + 運行時狀態（gitignored）
scripts/          安裝、部署、診斷腳本
docs/             文件
```

---

## 9. 與 Hermes Agent 的相似性

| 功能 | Hermes Agent | Mission Control |
|------|-------------|-----------------|
| 代理車隊管理 | ✅ | ✅ |
| 任務派遣 | ✅ | ✅ |
| SOUL 個性定義 | ✅ (SOUL.md) | ✅ (SOUL.md) |
| 技能 Hub | ✅ (skills/) | ✅ (Skills Hub) |
| SQLite 儲存 | ❌ (記憶體) | ✅ |
| 多代理工作流 | ✅ | ✅ |
| Cron 調度 | ✅ (cronjob) | ✅ |
| 成本追蹤 | ❌ | ✅ |

---

## 10. Changelog

* `2026-06-10`: 建立 — 基於 GitHub repo 深度分析 + 文件爬取