---
source_url: https://github.com/mathruffian-dot/codex-lazy-packs/blob/master/02.5-%E9%80%A3%E6%8E%A5GitHub%E8%88%87Obsidian.md
ingested: 2026-07-11
sha256: <computed-on-ingest>
---

# Codex 懶人包 #02.5：連接 GitHub 與 Obsidian 第二大腦

版本：v0.4（Codex Desktop 版）
更新日期：2026-04-28

本篇聚焦 Codex 需要的兩件事：
1. 用 GitHub CLI 讓 Codex 可以 commit / push 到 GitHub
2. 找到使用者的 Obsidian vault，安裝 MCPVault，讓 Codex 可以讀寫第二大腦

## 整體流程

```
階段一：GitHub CLI
  1. 檢查 Git / gh
  2. 網頁端登入 gh
  3. 設定 Git 使用者
  4. 建立測試 repo，驗證 commit / push

階段二：Obsidian MCP
  1. 找到 Obsidian vault
  2. 檢查 Node.js / npm
  3. 安裝 mcpvault
  4. 寫入 ~/.codex/config.toml
  5. 重啟 Codex
  6. 測試讀寫筆記
```

## 踩坑筆記（摘要）

| 狀況 | 解法 |
|------|------|
| `git` 找不到 | 安裝 Git 後重啟 Codex |
| `gh auth login --web` 逾時 | Codex 無法代替輸入帳密，需開互動視窗執行 |
| `gh auth status` Access denied | Codex 沙盒讀不到 GitHub CLI 設定，允許後重跑 |
| npm.ps1 被擋 | 改用 `npm.cmd` |
| `npm install -g` EPERM | 沙盒沒有寫入全域目錄權限，須提權重跑 |
| TOML 路徑失敗 | Windows 反斜線用 `\\\\` 跳脫 |
| 找不到 vault | 搜尋 `.obsidian` 資料夾，請使用者確認 |

## 底線原則

- 不在未確認前刪除測試 repo 或測試資料夾
- 不把 GitHub token 寫進 AGENTS.md
