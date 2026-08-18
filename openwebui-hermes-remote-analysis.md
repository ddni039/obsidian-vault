---
title: "OpenWebUI 深度分析 — 與 Hermes Remote SOP 整合評估"
created: 2026-07-11
tags: [research, openwebui, hermes, remote-access, web-ui]
---

# OpenWebUI 深度分析 — 與 Hermes Remote SOP 整合評估

## 執行摘要

**結論：OpenWebUI 非常適合整合到現有 Hermes Remote SOP。** 它解決了 Studio 的 Electron Origin WS Bug 和上下文記憶體滿兩大痛點，且完全相容 Hermes Gateway 的 OpenAI 兼容 API。

---

## 1. OpenWebUI 核心特性

### 協議導向架構
OpenWebUI 採用**協議優先設計**，以 OpenAI Chat Completions Protocol 為核心：
- 任何實現該協議的 provider 都能直接接入
- 不需要 provider-specific 適配層
- 對 Hermes Gateway 這類 OpenAI-compatible API 天然友好

### 必備 API Endpoint 支援狀態（Hermes Gateway）

| Endpoint | Hermes Gateway | OpenWebUI 需求 | 狀態 |
|----------|--------------|----------------|------|
| GET /v1/models | yes | 建議（用於模型發現） | 完全相容 |
| POST /v1/chat/completions | yes | **必須** | 完全相容 |
| POST /v1/embeddings | yes | RAG 需要 | 完全相容 |
| POST /v1/audio/speech | unknown | TTS | 需驗證 |
| POST /v1/audio/transcriptions | unknown | STT/Whisper | 需驗證 |
| POST /v1/images/generations | no | 圖片生成 | 不支持 |

### 上下文記憶體管理（對比 Studio）

| 功能 | Studio | OpenWebUI |
|------|--------|-----------|
| 自動上下文壓縮 | no | yes RAG 內建 |
| Session 持久化 | SQLite（獨立） | SQLite + 外置 |
| 對話歷史管理 | 容易滿 | 更適合長對話 |
| 文件上傳 + 知識庫 | 有限 | 完整 RAG |

---

## 2. 與 Hermes Remote SOP 的整合分析

### 現有 SOP 架構

Remote Client -> Tailscale (HTTPS) -> Studio (port 8648) -> Hermes Gateway (8642)

**痛點**：
1. Studio Electron 有 Origin Guard Bug（無法直連 Tailscale IP 的 Gateway）
2. Studio 上下文容易滿，需重開話題
3. Studio 適合短查詢，不適合複雜任務

### OpenWebUI 整合後架構

Remote Client -> Tailscale (HTTPS) -> OpenWebUI (port 3000) -> Hermes Gateway (8642)

**優勢**：
1. **無 Electron Origin Bug** — OpenWebUI 是標準瀏覽器，Origin 正常
2. **上下文管理更好** — RAG 支援，長對話更穩定
3. **統一的認證** — OpenWebUI 自己管理用戶，Gateway API Key 只做 backend 認證
4. **模型橋接** — 如果日後想連接其他 LLM provider（Ollama、vLLM），同一介面切換

### Tailscale 暴露命令（更新）

```bash
# 啟動 OpenWebUI
open-webui serve --port 3000

# Tailscale 暴露
/Applications/Tailscale.app/Contents/MacOS/Tailscale serve --bg https+insecure://localhost:3000
```

### 訪問 URL

- OpenWebUI: http://100.125.199.62:3000 (direct, browser auth)
- Studio: http://100.125.199.62:8648 (direct)

---

## 3. OpenWebUI 作為統一介面的戰略價值

### 多後端整合能力
OpenWebUI 可以同時連接：
- Hermes Gateway（當前主要 backend）
- Ollama（本地模型）
- OpenAI（雲端備用）
- Anthropic、Google Gemini 等

這意味著用戶可以在單一介面切換不同 LLM，而不需要改變使用習慣。

---

## 4. 風險與限制

### 尚未驗證的功能
1. **Tool/Function Calling** — Hermes Gateway 支援 tools，但 OpenWebUI 的 tool calling 需確認兼容
2. **Streaming** — 理論上支援，需要實際測試
3. **TTS/STT** — OpenWebUI 有這些功能，但 Hermes Gateway 可能不支持對應 endpoint

### 額外維護成本
- 需要安裝和維護 OpenWebUI 服務
- 需要管理 OpenWebUI 的用戶帳戶
- 與現有 Studio 造成功能重疊

---

## 5. 推薦行動

### 立即可做
1. 在 Host Mac 安裝 OpenWebUI：pip install open-webui
2. 設定連接 Hermes Gateway：
   - URL: http://100.125.199.62:8642/v1
   - API Key: nXkp0Zrfs9bFdLGMAPHVVlHeBDojMjIGr1QpjO8h2_U
   - Model ID: hermes-agent（手動添加）
3. 用 Tailscale 暴露並測試

### 更新 Remote SOP
建議在現有 hermes-webui-remote/SKILL.md 中新增 OpenWebUI 作為**第二 Web UI 選項**：
- 何種情境用 Studio（快速管理任務）
- 何種情境用 OpenWebUI（長對話、RAG、多後端）

---

## 6. 參考資料

- OpenWebUI 文档: https://docs.openwebui.com/
- OpenWebUI GitHub: https://github.com/open-webui/open-webui
- Hermes Studio Remote SOP: hermes-studio/references/remote-sop.md
- Electron Origin Bug: hermes-webui-remote/references/electron-origin-ws-bug.md
