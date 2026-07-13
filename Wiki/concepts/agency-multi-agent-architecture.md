---
title: Agency Multi-Agent Architecture
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [multi-agent, architecture, agency, coordination]
sources: [raw/articles/agency-agents-readme-2026.md]
---

# Agency Multi-Agent Architecture

## 與 Hermes 三角色的本質差異

| 維度 | Agency Agents | Hermes Tri-Role |
|------|-------------|-----------------|
| Agent 定義 | 每個 agent 是獨立專家（62種專業） | 每個 agent 是治理視角（3種角色） |
| 協作模式 | 水平分工（ specialization） | 垂直分工（決策鏈） |
| 個性設計 | 外部表現（vibe, emoji, color） | 內部機制（Hook Chain） |
| 觸發方式 | 人工選擇 agent | 事件驅動 |
| 上下文 | 各自獨立，無共享記憶 | 共享 MEMORY.md / USER.md |
| 目標 | 交付特定領域成果 | 維持系統長期健康 |

## Agency 的分層設計

```
Division (16)
  └── Agent (232 total, e.g. Engineering/Frontend Developer)
        ├── Frontmatter (name, emoji, vibe, color)
        ├── Identity & Memory
        ├── Core Mission
        ├── Critical Rules
        ├── Technical Deliverables
        └── Workflow Process
```

每個 agent 的 frontmatter 包含：
- `emoji`：視覺識別
- `vibe`：一句話人格描述
- `color`：主題色（用於 UI）

## 關鍵創新：Multi-Tool Integration

Agency 支援 11 種工具的轉換：
- Claude Code, Cursor, OpenCode, Copilot, Windsurf, Aider, Gemini CLI, Antigravity, OpenClaw, Kimi, Codex

透過 `convert.sh` 自動轉換成各工具的 agent 格式。

## 與 Hermes 的互補

Hermes 的 [[文謀]] / [[工匠]] / [[御史]] 適合作為**系統層**治理，
Agency 的 specialized agents 適合作為**執行層**工具。
