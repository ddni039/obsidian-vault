---
title: Codex Obsidian Integration
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [workflow, tool, platform]
sources: [raw/articles/codex-obsidian-integration-2026.md]
confidence: high
---

# Codex Obsidian Integration

## Overview

透過 MCPVault 讓 Codex 可以讀寫 Obsidian vault。Codex 不只能生成代碼，還能將工作進度與踩坑筆記寫回第二大腦。

## 核心流程

### 階段一：GitHub CLI
1. 檢查 `git --version` / `gh --version`
2. `gh auth login --web --git-protocol https` 網頁端登入
3. 設定 Git 使用者 `user.name` / `user.email`
4. 建立測試 repo，驗證 commit / push

### 階段二：Obsidian MCP
1. 找到 Obsidian vault（路徑含 `.obsidian` 資料夾）
2. 檢查 Node.js / npm
3. `npm install -g @bitbonsai/mcpvault`
4. 寫入 `~/.codex/config.toml`
5. 重啟 Codex Desktop app
6. 測試讀寫筆記

## 關鍵陷阱

| 狀況 | 解法 |
|------|------|
| `gh auth login` 逾時 | Codex 無法代替用戶在瀏覽器輸入密碼，需開互動 PowerShell 視窗執行 |
| npm全域安裝 EPERM | Codex 沙盒無寫入全域名限，改用提權模式 |
| Windows TOML路徑 | 反斜線用 `\\\\` 跳脫 |
| vault 找不到 | 搜尋含 `.obsidian` 的資料夾，請用戶確認主 vault |

## 底線原則

- 不在未確認前刪除測試 repo 或資料夾
- 不把 GitHub token 寫進 AGENTS.md

## 關聯

- [[codex]] — OpenAI 官方 CLI 程式碼 agent
- [[mcp-model-context-protocol]] — MCP 標準讓 Codex 能接各種工具
- [[claude-code]] — Anthropic 官方 CLI agent，有類似 MCP 整合模式
