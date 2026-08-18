# Hermes Studio（hermes-web-ui）

> Web UI / Desktop App for Hermes Agent by [EKKOLearnAI](https://github.com/EKKOLearnAI/hermes-web-ui)
> ⭐ 7.7k stars · 946 forks · 735 commits · 活跃开发中（5小時前有commit）

## 產品定位

Hermes Studio 是 Hermes Agent 的圖形化管理介面，提供：
- 桌面應用（Windows/macOS/Linux）
- npm CLI：`npm install -g hermes-web-ui && hermes-web-ui start`
- Docker 映像

**與 CLI 的區別**：CLI 適合進階用戶，Studio 適合視覺化操作、平台頻道管理和分析。

---

## 核心功能

### 1. AI 聊天（核心）

| 功能 | 說明 |
|------|------|
| 串流回應 | Socket.IO `/chat-run`，即時 streaming |
| 多 Session 管理 | 創建/命名/刪除/切換 |
| 本地 Session DB | Web UI 自建 SQLite，Hermes state.db 僅供唯讀讀取 |
| 來源分組 | 按平台（Telegram/Discord/Slack 等）折疊顯示 |
| 即時狀態指示 | 活躍 session 置頂 + 旋轉圖示 |
| Markdown 渲染 | 語法高亮 + 程式碼一鍵複製 |
| Tool Call 展開 | 顯示參數與回傳結果 |
| 檔案上傳/下載 | Profile 範圍內上傳，下載代理涵蓋 local/Docker/SSH/Singularity |
| Session 搜尋 | Ctrl+K 搜尋本機資料庫（Hermes 歷史session不納入） |
| Model 選擇器 | Profile 感知，自動發現已授權模型 |
| Token 用量顯示 | 單一 session 級別 badge |

### 2. 平台頻道（8平台統一管理）

| 平台 | 功能亮點 |
|------|---------|
| Telegram | Bot token、提及控制、表情反應、自由回覆 |
| Discord | Bot token、提及、Auto-thread、表情反應、頻道黑白名單 |
| Slack | Bot token、提及控制、Bot 訊息處理 |
| WhatsApp | 啟用/停用、提及控制、提及模式 |
| Matrix | Access token、homeserver、Auto-thread、DM 提及執行緒 |
| Feishu (Lark) | App ID/Secret、提及控制 |
| WeChat | QR code 登入（瀏覽器掃描，自動儲存憑證） |
| WeCom | Bot ID/Secret |

**憑證儲存**：
- 敏感資訊寫入 `~/.hermes/.env`
- 平台行為設定寫入 `~/.hermes/config.yaml`

### 3. 使用分析（Usage Analytics）

- 總 Token 用量細分（input / output）
- Session 數量與日均統計
- 預估費用追蹤 & 快取命中率
- Model 用量分佈圖
- 30天每日趨勢（長條圖 + 數據表）

### 4. 排程任務（Scheduled Jobs）

- 創建/編輯/暫停/恢復/刪除 cron jobs
- 立即觸發執行
- Cron 表達式快速預設

### 5. Kanban 工作板

- Profile 感知的任務看板
- 任務創建、更新、狀態移動
- 與 Web UI 同一本地狀態和認證模型

### 6. Model 管理

- 從 credential pool（`~/.hermes/auth.json`）自動發現模型
- 向各 provider 端點（`/v1/models`）獲取可用模型
- 新增/更新/刪除 providers（預設 & 自訂 OpenAI 相容）
- OpenAI Codex & Nous Portal OAuth 登入
- Provider URL 自動偵測

### 7. 工作區工具

- 檔案瀏覽器
- Web 終端機
- 語音輸入/輸出
- Coding Agent 運行器（Claude Code / Codex）
- 裝置發現
- 效能視圖

---

## 技術架構

### 核心設計原則（Harness）

來自 `docs/harness/README.md`：

> Make repository context legible through short maps and deeper docs.
> Keep architecture constraints close to the code they protect.
> Give agents a deterministic validation path before opening or updating a PR.
> Prefer mechanical checks over reminder text when a rule can be verified.

### Canonical Event Stream 架構

所有 provider（Claude Code / Codex / Hermes Bridge）統一為 `CanonicalAgentEvent`：

```
Provider protocol
  → ProtocolAdapter
  → CanonicalAgentEvent stream
  → Subscribers
    → HTTP SSE serializer
    → Socket.IO emitter
    → DB persistence subscriber
    → Usage subscriber
    → Debug/log subscriber
```

### 關鍵元件

| 元件 | 職責 |
|------|------|
| `TargetRegistry` | 管理本地代理目標、生成路由 key/Token、隔離上游 API key |
| `EndpointResolver` | 建構上游端點 URL，支援 `/v1`、`/v1beta/openai`、`/api/paas/v4` 等多種根路徑 |
| `ProtocolAdapter` | 轉換各 provider 協定為 canonical events（目前：anthropic messages、chat completions、codex responses） |
| `AgentRunGateway` | facade，統一接收 `AgentRunRequest` → 選 target/adapter → call upstream → yield events |
| `StreamSerializers` | 序列化成客戶端特定格式（Responses SSE、Anthropic Messages SSE、Socket.IO） |
| `RunPersistenceSubscriber` | 消費 canonical events，寫入現有 session 表 |

### Canonical Event Contract

```
response.created
response.output_text.delta
response.output_text.done
response.output_item.added
response.function_call_arguments.delta
response.output_item.done
response.completed
response.failed
```

攜帶：`type`、`response_id`/`run_id`、`model`、`output_index`/`item_id`、`usage`（終端事件）、provider error details。

### 代理流向

**Claude Code**：
1. Route 驗證本地 target token
2. 將 Anthropic request body 傳給 `AgentRunGateway`
3. Gateway 標準化上游輸出為 canonical events
4. 可選：persistence subscriber 記錄到 DB

**Codex**：
1. Route 驗證本地 target token
2. 將 Responses request body 傳給 `AgentRunGateway`
3. 類似流程

---

## 與 Hermes CLI 的關係

| 維度 | Hermes CLI | Hermes Studio |
|------|-----------|---------------|
| 介面 | 終端機文字 | 圖形化 / 桌面應用 |
| Session 管理 | 純文字，state.db | 獨立 SQLite + 圖形化 |
| 平台頻道 | 手動設定 | 統一 Web UI 設定 |
| 使用分析 | 無內建 | 完整儀表板 |
| 遠端存取 | Telegram Bot（唯一方式） | 可本地暴露或搭配 tunnel |
| 資源耗用 | 極輕 | 中等（Electron 或 Node.js 服務） |

---

## 安裝方式

```bash
# npm 全域安裝
npm install -g hermes-web-ui && hermes-web-ui start

# 或下載桌面應用
# https://github.com/EKKOLearnAI/hermes-web-ui/releases/latest
```

---

## 標籤

#hermes-agent #web-ui #desktop-app #ai-tool #chat-interface #automation #usage-analytics