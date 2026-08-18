# MEMORY.md - 長期記憶

> 重要的事情才記，瑣事不記。每天寫日記，但只記重點。

---

## 👤 用戶資料

| 項目 | 內容 |
|------|------|
| **名稱** | 痞子林 |
| **Telegram** | @bbni039 |
| **Email** | ddni039@gmail.com（主要）、bbni039@gmail.com（已標注安全） |
| **時區** | Asia/Taipei (GMT+8) |
| **偏好語言** | 中文 |

---

## ✨ 我的身份

| 項目 | 內容 |
|------|------|
| **名稱** | 輕舞飛揚 |
| **角色** | AI 精靈 🧚 |
| **風格** | 專業技術顧問，可愛但帶毒舌 |
| **Emoji** | ✨ |

---

## 🔐 安全設定

### 已標注安全信箱
- `bbni039@gmail.com` — 可自動寄信

### 紅線（絕對不能做）
- 密碼、API Key 嚴禁外傳
- 未經確認不得刪除檔案（優先用 `trash`）
- 未經確認不得開啟攝像頭/麥克風
- 絕對禁止刷卡付款或關閉防毒軟體
- 系統設定修改前必須詢問

---

## 🛠️ OpenClaw Gmail 監控與權限修復 SOP（2026-04-09 完整版）

### 核心問題
| 問題 | 說明 |
|------|------|
| **權限孤島** | Daemon allowlist 與終端機完全隔離 |
| **路徑隔離** | Gateway Daemon 不一定抓得到用戶的 `$PATH` |

### 關鍵修正
- gmail_cli.py Shebang：`#!/opt/homebrew/bin/python3`
- 真正設定檔：`~/.claude/settings.json`（不是 exec-approvals.json！）
- 路徑必須絕對路徑：`/opt/homebrew/bin/gog`

### SOP（指令被擋時）
1. `which [指令]` → 確定位址
2. `openclaw config set exec.approvals.allowlist '["..."]'`
3. `openclaw gateway restart`
4. 在**痞子林終端機**驗證

### ✅ 目前狀態
| 組件 | 路徑 |
|------|------|
| Python（Homebrew） | `/opt/homebrew/Cellar/python@3.14/.../python3.14` |
| gog CLI | `/opt/homebrew/bin/gog` |
| gmail_cli.py | `/Users/leo039/gmail_cli.py` |

---

## 🛠️ 已設定系統

### gog（Google Workspace CLI）
- 已授權：`ddni039@gmail.com`（2026-04-08 更新 OAuth 授權）
- 服務：Gmail, Calendar, Drive, Contacts, Sheets, Docs
- 狀態：✅ 正常運作
- Gmail 讀取測試：✅ 成功（`gog gmail search 'newer_than:1d'`）

### OpenClaw
- 版本：2026.3.31 (213a704)
- 設定檔：`/Users/leo039/.openclaw/openclaw.json`
- exec-approvals：`/Users/leo039/.openclaw/exec-approvals.json`

### lossless-claw-enhanced（LCM 插件）
- 版本：0.5.2，GitHub：https://github.com/win4r/lossless-claw-enhanced
- 功能：DAG 壓縮架構，SQLite 持久化，`lcm_grep`/`lcm_describe`/`lcm_expand` 召回工具
- 目前配置：`contextThreshold=0.65`，`leafChunkTokens=8000`，`freshTailCount=32`
- 驗證狀態：✅ 正常（55 條訊息已儲存，1 次摘要壓縮）
- 資料庫：`~/.openclaw/lcm.db`（192KB）

### 🧠 LCM Memory 系統設計思路（2026-04-10）

#### 架構
```
原始對話（葉節點）→ 葉摘要 → 高層摘要 → ...
```
- **DAG 結構**：支援分叉與合併，SQLite 持久化
- **增量壓縮**：只處理未压缩的尾部，freshTailCount=32 保護最新上下文

#### 與現有 Memory 整合原則
- `MEMORY.md` = 結論記憶（LCM 召回後寫入）
- `SOUL.md` / `USER.md` = 人格/用戶偏好（靜態，不依賴 LCM）

---

## ⚠️ 重要技術限制（2026-04-09 更新）

### exec allowlist 行為
- Pattern 比對**只看 argv[0]**（命令第一個單詞），不含參數或路徑
- 例：`echo test` → argv[0]="echo"；`node -e` → argv[0]="node"（會被 content filter 擋）

### 關鍵限制
- OpenClaw 2026.3.31 **不支援** `exec` key，必須用 `exec-approvals.json`
- 真正設定檔：`~/.claude/settings.json`（不是 exec-approvals.json！）
- 路徑必須寫**絕對路徑**，不能只寫 `gog`

### 🐍 Python 環境
- Homebrew Python：python@3.14，`#!/opt/homebrew/bin/python3`

### 🛠️ 維護腳本（2026-04-09 重構鎖定）
| 腳本 | 說明 |
|------|------|
| `oc_sentinel_unified.sh` | ✅ 主要維護腳本（7.9KB，5 階段 SOP） |
| `oc_sentinel_unified.py` | ✅ Python 版（8.6KB） |
| `~/oc-sentinel.sh` | 符號連結 → `oc_sentinel_unified.sh` |

**5 階段 SOP**：Pre-flight → Backup → Execute → Validate → Reset（kill -9 + restart）

❌ 已廢除：`oc_unify_fix.sh`、`oc_ops_vault.sh`、`openclaw_sentinel_plus.sh`、`fix_oc.sh`

### 🔐 Gmail Cron 授權失敗（2026-04-09 新登錄）

| 徵候 | 成因 | 解決方案 |
|------|------|----------|
| `No auth for gmail bbni039@gmail.com` | Cron 背景 session 無 OAuth Token（終端機成功≠背景成功） | `gog auth add bbni039@gmail.com --services gmail` |

⚠️ **日後注意**：gog OAuth Token 存於本地，Cron Job 屬於另一個 session，可能讀不到同一組 Token。痞子林終端機成功不代表背景也成功（再次驗證「路徑/環境隔離」問題）。

### 🛠️ 權限維護核心觀念（摘要）

| 問題 | 核心洞察 |
|------|----------|
| **權限孤島** | Daemon 的 allowlist 與終端機完全隔離，終端機能跑 ≠ Daemon 也能跑 |
| **路徑隔離** | Gateway Daemon 不一定抓得到用戶的 `$PATH`，導致找不到 gog 等二進位 |
| **真正設定檔** | `~/.claude/settings.json`（不是 `exec-approvals.json`）|
| **路徑必須絕對** | 必須寫 `/opt/homebrew/bin/gog`，不能用相對路徑 |

**修復 SOP**：`which [指令]` → `openclaw config set exec.approvals.allowlist` → `openclaw gateway restart`

### 🧠 WebSocket 1006/1008 錯誤（速查）

| 錯誤碼 | 成因 | 解決方案 |
|--------|------|----------|
| **1006** | Zombie Process / Localhost 隔離 | `kill -9 <PID>` + `openclaw gateway restart` |
| **1008** | Token/Pairing 驗證失敗 | 在 Control UI 填 Token 或 `openclaw gateway restart` |

### pairing required 行為（2026-04-09 確認）

在 Control UI 執行 `./oc-maintenance.sh` 時收到 `gateway closed (1008): pairing required` = **正常行為**，不代表腳本有問題。解鎖方式：終端機執行 `openclaw gateway restart`。

---

### 🛠️ Cron Job 網路重試機制（2026-04-10 新增）

#### 核心檔案
| 檔案 | 說明 |
|------|------|
| `scripts/network_retry.sh` | ⭐ 框架核心 |
| `backup.sh` | 每日備份 |
| `scripts/check-update.sh` | OpenClaw 版本更新 |
| `scripts/check_unified_security.sh` | ⭐ 統一安全檢查 |
| `scripts/check-oil-price.sh` | 油價查詢 |

#### 關鍵參數
| 參數 | 預設值 | 說明 |
|------|--------|------|
| `MAX_RETRIES` | 3 | 失敗多少次才放棄 |
| `RETRY_DELAY_MINUTES` | 5 | 每次失敗後延後幾分鐘 |
| `FAILURE_THRESHOLD` | 5 | 觸發 timeout 調整的失敗次數 |
| `TIMEOUT_MULTIPLIER` | 1.5 | 調整倍率（5次失敗後 timeout × 1.5）|

#### Exit Code
| Code | 意義 |
|------|------|
| `0` | 成功 |
| `1` | 達到失敗閾值（3次），發送通知 |
| `99` | 需延後重試 |

#### 三階段管線
Pre-flight Check（網路偵測）→ Execute → Threshold Check

完整設計：`~/.openclaw/workspace/docs/cron-sop-design.md`

---

### 🛡️ 統一安全檢查 SOP（2026-04-10 新增）

#### 使用方式
| 模式 | 指令 |
|------|------|
| **完整** | `./check_unified_security.sh full` |
| **網路** | `./check_unified_security.sh network` |
| **權限** | `./check_unified_security.sh permission` |

#### 腳本狀態
| 項目 | 內容 |
|------|------|
| **路徑** | `~/.openclaw/scripts/check_unified_security.sh` |
| **大小** | 12,828 bytes |
| **狀態** | ✅ 已驗證 |

四階段：Phase 0（Pre-flight 網路偵測）→ Phase 1（網路安全）→ Phase 2（權限安全）→ Phase 3（總結）

Exit Code：0 成功 / 1 ISSUES / 99 延後重試

---

## 📦 已安裝技能

| 技能 | 用途 |
|------|------|
| `text-to-speech` / `tts` | Marswave TTS |
| `obsidian-markdown` | Obsidian 筆記整合 |
| `reminder` | 自動化提醒 |
| `playwright-mcp` | 瀏覽器自動化 |
| `chrome-devtools-mcp` | Chrome DevTools MCP |

安裝腳本：`~/.openclaw/workspace/clawhub-install.sh`

---

## 📁 專案狀態

### Star Office UI
- 狀態：✅ 已部署（2026-04-07）
- 位置：`~/.openclaw/workspace/Star-Office-UI`
- 後端：Flask + Python venv，運行於 `http://localhost:19000`
- 前端：已由後端服務（`/` 路由）
- 依賴：Flask 3.0.2、Pillow 10.4.0（venv 位於 `backend/venv/`）
- 注意：v3.14 venv 路徑需與 `run.sh` 中的 `$ROOT_DIR/.venv` 配合，否則手動指定 Python 路徑

### gmail_cli.py（SOP 優化版）
- 新版：`/Users/leo039/.openclaw/workspace/gmail_cli_sop.py`（五階段 SOP）
- 舊版：`/Users/leo039/gmail_cli.py`（備用）
- Python Shebang：`#!/opt/homebrew/bin/python3`（需寫死 3.14 路徑）
- gog 路徑：需使用 `/opt/homebrew/bin/gog`
- 主要信箱：`ddni039@gmail.com`（gog 已授權）
- 狀態檔：`~/.openclaw/backlog/gmail_monitor_state.json`
- 通知邏輯：**兩小時無新郵件才發心跳通知**

### 兩小時無新郵件通知邏輯（2026-04-10 新增）
| 情境 | 行為 |
|------|------|
| 有新郵件 | ✅ 立即通知 |
| 無新郵件 + 距上次 > 2h | ✅ 心跳通知 |
| 無新郵件 + 距上次 < 2h | 🚫 安靜跳過 |
| 首次執行 | ✅ 通知一次 |

### cron_backlog_sentinel.sh（v2.0）
- 路徑：`~/.openclaw/workspace/cron_backlog_sentinel.sh`
- 功能：Cron 任務狀態偵查（**已暫停 Cron**，手動執行）
- 簡化：狀態由 `openclaw cron list` 的 `lastRunStatus` 直接映射

---

## ⏰ 排程任務（Cron）

| 任務 | 時間 | 狀態 | 備註 |
|------|------|------|------|
| AI 關注提醒 | 19:00 | ✅ 正常 | |
| 每日備份 | 00:00, 12:00 | ✅ 已優化 | 網路重試 SOP |
| OpenClaw 版本更新 | 12:00 | ✅ 已優化 | 網路重試 SOP |
| **統一安全檢查** | 不固定 | ✅ 已合併 | 統一 SOP（網路+權限一次完成）|
| 週日油價通知 | 週日 13:00 | ✅ 已新建 | 網路重試 SOP |
| **方案C 狀態偵查** | — | ❌ 已暫停 | 2026-04-10 移除（手動執行）|
| OpenClaw 每週維護 | 每週日 03:00 | ✅ 已設定 | 執行 `~/oc-sentinel.sh` |
| 統一安全檢查 | 每週日 03:00 | ✅ 已設定 | 執行 `check_unified_security.sh full` |

---

## 🗂️ 中央任務排程器

- 核心：`~/.openclaw/workspace/task_scheduler.sh`
- 新增：`~/.openclaw/workspace/add_task.sh`
- 優先級：backup(1) > gmail(2) > oil-price(3) > network-check(4)

使用：`task_scheduler.sh now` / `status`

---

## 🔧 待處理事項

- [ ] **LCM 上下文監控** — 晚點繼續（驗證壓縮行為、確保 MEMORY.md 同步）
- [x] 每週維護 Cron 已設定（2026-04-10）
- [x] 統一安全檢查 Cron 已設定（2026-04-10）
- [x] 中央任務排程器（2026-04-10）
- [x] exec allowlist 修復 SOP 已確認（2026-04-09）
- [x] oc-sentinel.sh 已確認存在（2026-04-09）
- [x] fix_oc.sh 已重寫（PICO 殘留已清除，87行，2026-04-09 21:15）
- [x] Gmail CLI / gmail_cli.py 環境已對齊（2026-04-09）
- [x] Cron Job 網路重試機制（2026-04-10）

---

## 📋 任務分工 SOP（大型任務處理框架）

> 詳細說明在 `AGENTS.md`「任務分工 SOP」章節。

### 🔀 三種分工模式（快速參照）

| 模式 | 用途 | 核心機制 |
|------|------|----------|
| **垂直拆分** | 有明確階層結構的大型任務 | Architect → Executor → Reviewer |
| **水平拆分** | 需隔離上下文避免遺忘限制條件 | 資訊緩存 + 上下文重置 |
| **標準化格式** | 分派工作時確保 AI 理解率 80%+ | 角色 / 區間 / DoD / 異常處理 |

### 📌 上下文護照（每次子任務開始前回答）
- 角色：[Executor / Architect / Reviewer]
- 區間：[具體操作範圍]
- 上次狀態 / 本次目標

### 🚨 異常處理
遇到 `ENOENT` 或權限衝突 → **立即停止**，回報 `<錯誤類型> | <路徑> | <建議>`

---

## 📋 OpenClaw Cron 最佳實踐（2026-04-10 新增）

### ⏱️ Gateway Timeout 設定
- 原則：Timeout = 最長任務執行時間 × 1.5
- 目前設定值：**300 秒（5 分鐘）**
- 查詢：`openclaw config get agents.defaults.timeoutSeconds`

⚠️ **風險**：任務超時會被截斷，建議任務不超過 15 分鐘

### 🔔 條件通知策略
| 通知類型 | 適用場景 |
|---------|---------|
| **異常才通知** | 網路安全檢查、系統監控 |
| **定期摘要** | Gmail 檢查 — 兩小時無新郵件心跳 |
| **立即通知** | 重要提醒（19:00 AI 關注提醒）|

### 📊 Cron 成本意識
| 頻率 | 月估算 | 建議 |
|------|--------|------|
| 每分鐘 | ~43,200 次 | ⚠️ 極高，避免 |
| 每小時 | ~720 次 | ⚠️ 高成本 |
| 每天一次 | ~30 次 | ✅ 多數場景適用 |
| 每週一次 | ~4 次 | ✅ 低成本日常維護 |

---

_Last updated: 2026-04-10 20:29_

## 📝 歷史日記

- `memory/2026-04-06.md`
- `memory/2026-04-08.md`
- `memory/2026-04-09.md` ← 最新

---

## 安全基線（2026-03-30）

痞子林已確認以下安全設定為默認基準：

- **SSH**：金鑰認證，禁用密碼，防火牆開啟（22, 443 端口）
- **API Key**：全存環境變數或 .env，.env 加入 .gitignore，每 3 個月輪換
- **OAuth Token**：檔案權限 600，定期備份 ~/clawd/
- **行為**：外發消息必須確認，破壞性操作必須確認，用 trash 代替 rm

---

_Last updated: 2026-04-10 01:14_
