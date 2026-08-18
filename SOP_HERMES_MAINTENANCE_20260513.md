# SOP_HERMES_MAINTENANCE_20260513.md — Hermes 維護記錄

## 日期：2026-05-13

---

## 錯誤發現

### 錯誤 1：stream_retry_pool_cleanup 導致 credential 丟失

**錯誤徵兆：**

```
WARNING run_agent: Failed to rebuild shared OpenAI client (stream_retry_pool_cleanup)
error=Missing credentials. Please pass an `api_key`...
```

**根本原因：**

- `_replace_primary_openai_client` 被 `stream_retry_pool_cleanup` 呼叫時
- `_client_kwargs` 在 credential rotation 或 fallback 過程中被清空
- 導致新客戶端創建時 api_key 為空
- 錯誤被 `except Exception: pass` 吞掉，客戶端重建失敗但流程繼續

**修復：** 重啟 Hermes 後清除問題，重新正常運行

**驗證：** 重啟後 12:40+ 無新的 stream_retry_pool_cleanup 錯誤

---

### 錯誤 2：MCP minimax-search 啟動失敗

**錯誤徵兆：**

```
MCP server 'minimax-search' failed initial connection:
missing executable '/Users/blackleo039icloud.com/.hermes/hermes-agent/venv/bin/python'
```

**根本原因：**

- 備份還原時 config.yaml 中路徑錯誤
- `/Users/blackleo039icloud.com/` 應為 `/Users/blackleo039/`
- 另一台機器的備份配置未修正路徑

**修復：**

```bash
sed -i '' 's|/Users/blackleo039icloud.com/.hermes/hermes-agent/venv/bin/python|/Users/blackleo039/.hermes/hermes-agent/venv/bin/python|g' ~/.hermes/config.yaml
sed -i '' 's|/Users/blackleo039icloud.com/.hermes/mcp-servers|/Users/blackleo039/.hermes/mcp-servers|g' ~/.hermes/config.yaml
```

**驗證：** 重啟後 `minimax-search` MCP 正常，6 tools registered

---

### 錯誤 3：state.db 損壞

**錯誤徵兆：**

```
database disk image is malformed (11)
```

**修復：**

```bash
rm ~/.hermes/state.db
# Hermes 會自動重建
```

---

### 錯誤 4：GitHub token 過期

**錯誤徵兆：**

```
Authentication Failed: Bad credentials (GitHub MCP)
```

**檢測：**

```bash
curl -s -H "Authorization: token ghp_xxx" https://api.github.com/user
# 返回 "Bad credentials" = token 無效
```

**修復：**

1. 刪除舊 token（GitHub Settings > Personal Access Tokens）
2. 更新 config.yaml 中的 GITHUB_PERSONAL_ACCESS_TOKEN
3. 修復 obsidian git remote

**驗證：** 新 token `[GITHUB_PAT]` 有效

---

## Git 整合工作

### 整合 workspace → hermes

**背景：**

- `ddni039/workspace` 有大量 skills 和 core docs
- `ddni039/hermes` 只有翻譯 skill
- 需合併並統一管理

**執行：**

```bash
# 1. Clone both repos
git clone https://...@github.com/ddni039/hermes.git hermes_dst
git clone https://...@github.com/ddni039/workspace.git workspace_src

# 2. Copy selected content
cp -r workspace_src/.learnings hermes_dst/
cp workspace_src/AGENTS.md BOOTSTRAP.md HEARTBEAT.md ... hermes_dst/
cp -r workspace_src/skills/* hermes_dst/.hermes/skills/

# 3. Commit and push
cd hermes_dst
git add -A
git commit -m "feat: merge workspace content into hermes"
git push origin main

# 4. Sync to local ~/.hermes/skills/
```

**結果：**

- 111 files changed, 11444 insertions
- 26+ skills
- Core docs: AGENTS, BOOTSTRAP, HEARTBEAT, IDENTITY, MEMORY, OPERATING-GUIDELINES, SOUL, TOOLS, USER

---

## Token 清理

### 廢棄 token：[GITHUB_PAT]

**狀態：** ❌ 已刪除（在 GitHub Web UI）

**清理範圍：**
| 位置 | 狀態 |
|------|------|
| `~/.hermes/obsidian/.git/config` | ✅ 已更新為新 token |
| `~/.claude/bash-log.txt` | ✅ 替換為 REDACTED |
| `~/.hermes/.hermes_history` | ✅ 替換為 REDACTED |
| `~/.hermes/sessions/*.json` | ✅ 替換為 REDACTED |
| `~/.claude/file-history/` | ✅ 替換為 REDACTED |
| `~/.hermes/skills/github/github-auth/SKILL.md` | ✅ 替換為 REDACTED |

**驗證：**

```bash
grep -r "[GITHUB_PAT]" ~ | grep -v "REDACTED"
# 應返回空
```

---

## 系統狀態（維護後）

| 項目               | 狀態                                               |
| ------------------ | -------------------------------------------------- |
| Hermes 主進程      | ✅ 運行中                                          |
| MCP minimax-search | ✅ 6 tools                                         |
| MCP github         | ✅ 26 tools                                        |
| MCP minimax (JS)   | ✅ 10 tools                                        |
| API                | ✅ MiniMax-M2.7, 99-100% cache                     |
| state.db           | ✅ 已重建                                          |
| GitHub token       | ✅ 統一 `[GITHUB_PAT]` |

---

## 預防措施

1. **路徑一致性：** 備份還原後檢查所有路徑
2. **Token 驗證：** 使用前先用 API 驗證有效性
3. **MCP Config：** 重啟後檢查 MCP 连接狀態
4. **定期清理：** 定期檢查廢棄 token 並清理

---

_v1.0 — 2026-05-13_
