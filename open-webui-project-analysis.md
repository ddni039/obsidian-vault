# Open WebUI 項目深度分析

> 研究日期：2026-07-15 | 最新版本：v0.10.2（2026-07-01） | Stars：145,496 | 語言：Python 36.5% / Svelte 32.4% / JavaScript 23.4%

---

## 專案概覽

**Open WebUI** 是自託管 AI 介面的領先開源專案，支援 Ollama、OpenAI API、Anthropic 等所有主流 LLM 提供者。

**定位：** 取代團隊日常使用的碎片化 AI 工具（ChatGPT 寫作、獨立影像生成 App、另一個文件搜尋工具、試算表提示庫），將對話、知識、工具和模型統一在一個平台。

**官方標籤：** `ai`, `llm-ui`, `llm-webui`, `llms`, `mcp`, `ollama`, `ollama-webui`, `open-webui`, `openai`, `openapi`, `rag`, `self-hosted`, `ui`, `webui`

**最新版本亮點（v0.10.2，2026-07-01）：**
- 💭 **Streamed reasoning display**：模型輸出的思考過程即時串流顯示
- 🗂️ **Folder uploads to knowledge bases**：上傳資料夾時保留子資料夾結構
- 🧠 **Memory system context toggle**：管理員可控制記憶系統上下文開關

---

## 核心架構

### 技術棧

| 層 | 技術 | 佔比 |
|----|------|------|
| 後端 | Python（FastAPI 風格） | 36.5% |
| 前端框架 | Svelte | 32.4% |
| 前端邏輯 | JavaScript | 23.4% |
| 類型安全 | TypeScript | 5.0% |
| 樣式 | CSS | 2.3% |

### 目錄結構

```
open-webui/
├── backend/
│   └── open_webui/
│       ├── main.py              # FastAPI 入口
│       ├── config.py            # 配置管理
│       ├── constants.py         # 常數定義
│       ├── functions.py         # 函式擴展
│       ├── tasks.py             # 背景任務
│       ├── internal/            # 內部模組
│       ├── models/              # 資料模型（Pydantic）
│       ├── routers/            # API 路由
│       ├── socket/              # WebSocket
│       ├── retrieval/           # RAG 檢索核心
│       │   ├── loaders/        # 文件載入器（Tika, Docling, PaddleOCR...）
│       │   ├── models/         # 檢索模型
│       │   ├── vector/         # 向量資料庫適配（ChromaDB, PGVector...）
│       │   ├── web/            # 網頁檢索
│       │   └── utils.py
│       ├── tools/              # 工具擴展
│       └── utils/              # 通用工具
├── src/                        # Svelte 前端
│   └── lib/components/
│       ├── chat/               # 對話元件
│       ├── workspace/           # 工作區（模型、知識庫、代理）
│       ├── admin/              # 管理後台
│       ├── channel/            # 頻道功能
│       └── ...
└── docs/                       # 官方文檔
```

### RAG 檢索架構（`retrieval/`）

**支援 9 種向量資料庫：**
- 官方維護：ChromaDB、PGVector
- 社群支援：Qdrant、Milvus、Elasticsearch 等

**8 種文件提取引擎：** Tika、Docling、Azure、Mistral OCR、Datalab Marker、MinerU、PaddleOCR、custom loaders

**混合檢索：** BM25 + 向量搜尋 + cross-encoder reranking

**Agentic retrieval：** 模型可自主搜尋、閱讀、跨文件綜合

---

## 與 Hermes Agent 的定位比較

| 維度 | Open WebUI | Hermes Agent |
|------|-----------|-------------|
| **核心定位** | AI 統一介面平台 | 自增長 AI Agent |
| **主要用戶** | 團隊、多使用者 | 個人、開發者 |
| **部署模式** | Docker/自託管/企業 | CLI + 訊息平台 |
| **記憶系統** | Per-user Memory + 跨對話 | Brain/Wiki + Session |
| **擴展方式** | Tools/Pipelines/MCP/OpenAPI | Skills + 腳本 |
| **知識庫** | 原生 RAG（多向量DB） | 外掛 gbrain wiki |
| **代理能力** | 工具調用 + 自動化 | 多 Agent 協作 |
| **即時推理顯示** | ✅ v0.10.2 新增 | 依賴模型能力 |

**互補關係：** Open WebUI 是「所有人的 AI 介面」，Hermes Agent 是「你的個人 AI 代理」。Open WebUI 的 Computer 生態（見下）是兩者最接近的領域。

---

## Open WebUI Computer 生態

> 與 Hermes Agent 直接競爭的功能集合

**Open WebUI Computer** 是一個在真實機器上運行的 Agent harness：
- 安裝一個 App，連接 AI（API key、本地模型或 Claude Code/Codex 等編碼代理）
- 直接在真實檔案上工作，批准的檔案就是磁碟上的檔案
- 瀏覽器內完整終端、檔案總管、Git；從桌面或手機操作
- 從 Telegram 或 WhatsApp 發消息
- 排程代理定期匯報

**Computer vs Open WebUI 平台策略：**
- **Open WebUI** 是穩定平台：企業就緒、多使用者，團隊部署依賴它
- **Computer** 移動更快：新功能先在 Computer 構建和發布，成熟後遷入 Open WebUI

---

## 主要功能地圖

### 💬 對話與溝通
- 多模型並排聊天對比
- 檔案/圖片上傳分析
- 網頁搜尋 + 即時引用來源
- 瀏覽器內 Python 程式執行
- 訊息佇列（打字時自動發送）
- 多模型記憶（跨對話記住用戶偏好）
- 資料夾/標籤/釘選組織
- 語音輸入/輸出/免持通話
- 圖片生成（DALL-E、Gemini、ComfyUI）
- 自動化排程提示
- 任務管理（模型維護結構化任務清單）

### 📚 知識與 RAG
- 向量檢索 + 混合搜尋
- 完整內容注入模式（繞過 chunking）
- 知識庫子資料夾結構保持（v0.10.2）
- 多源文件攝入（40+ 來源 via oikb）
- Agentic 自主檢索

### 🤖 模型與代理
- Model Presets（系統提示 + 工具 + 知識 + 參數封裝）
- 動態變數 `{{ USER_NAME }}`, `{{ CURRENT_DATE }}`
- Per-model 工具綁定
- Per-user/group 存取控制
- 全域預設參數

### 📝 Notes
- Markdown/Rich Text 編輯器
- AI 即時原地改寫
- 任意對話上下文注入（無需 chunking）

### 💬 Channels
- 人類和 AI 模型參與同一對話
- `@model` 標記召喚任意 AI
- 執行緒回覆 + 表情反應
- AI 跨頻道綜合能力

### ⚡ Open Terminal
- 瀏覽器內程式執行（隔離可選 Docker 或 bare metal）
- 側邊欄檔案瀏覽器
- 網站即時預覽

### 🔌 擴展性
| 類型 | 用途 |
|------|------|
| **Tool** | 聊天內呼叫 Python 程式（API key 可保密在 server-side） |
| **Pipe Function** | 在模型選擇器新增新模型/提供者 |
| **Filter Function** | inlet/outlet/stream鉤子修改訊息（PII 脫敏、翻譯、注入） |
| **Action Function** | 訊息上的按鈕觸發自訂程式碼 |
| **MCP Server** | 原生 Streamable HTTP，Model Context Protocol 支援 |
| **OpenAPI Server** | 自動發現 OpenAPI 端點為可呼叫工具 |
| **Skills** | Markdown 指令集，教模型如何處理任務 |
| **Prompts** | 斜線命令範本，帶類型輸入變數和版本控制 |

### 🔐 認證與存取
- RBAC（角色、用戶組、資源權限）
- SSO/OIDC/LDAP 聯邦認證
- SCIM 2.0 自動用戶/群組供應
- API Keys（腳本/機器人程式存取）

### 🔧 管理
- Analytics（使用量、Token 消耗、成本追蹤）
- Model Arena、A/B 測試、ELO 排行榜
- 自訂系統公告橫幅
- Webhooks（註冊、對話完成、外部整合通知）

### 🏗️ 部署
- Docker Compose（含 GPU 支援）
- Kubernetes + Helm
- `pip install open-webui`
- uv 安裝：`uvx open-webui@latest serve`
- Desktop App（原生無 Docker）
- S3/GCS/Azure Blob 雲端儲存（無狀態實例）
- OpenTelemetry 追蹤/指標/日誌
- Redis 跨 worker/node 水準擴展

---

## 生態系統專案

| 專案 | 用途 |
|------|------|
| **open-terminal** | 為 Open WebUI 提供沙盒終端、檔案瀏覽、程式執行 |
| **oikb** | 知識庫同步：監視本地資料夾、GitHub repos、S3、Confluence、40+ 來源 |
| **mcpo** | MCP-to-OpenAPI 代理：任何 MCP 工具伺服器用於 Open WebUI |
| **desktop** | 桌面原生 App（無 Docker） |

---

## 安裝方式

```bash
# Docker（一行命令）
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main

# pip
pip install open-webui && open-webui serve

# uv（推薦）
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
```

---

## 與 Hermes Agent 的潛在整合點

1. **Open WebUI 作為 Hermes 的 UI 層**：透過 MCP 將 Hermes Agent 接入 Open WebUI 作為一個模型/工具
2. **Open WebUI 的 RAG 能力**：Hermes 的 gbrain wiki 可借助 Open WebUI 的混合檢索引擎增強
3. **Computer 模式**：Open WebUI Computer 與 Hermes Agent 的 Computer Use 高度重疊，可研究互相借鑒
4. **oikb 知識同步**：Open WebUI 的知識庫同步工具可補充 Hermes 的 wiki 攝入流程

---

## 參考資料

- [GitHub](https://github.com/open-webui/open-webui)
- [官方文檔](https://docs.openwebui.com/)
- [Features](https://docs.openwebui.com/features/)
- [v0.10.2 Release Notes](https://github.com/open-webui/open-webui/releases/tag/v0.10.2)
- [Open WebUI Computer](https://docs.openwebui.com/ecosystem/computer)
- [Extensibility Guide](https://docs.openwebui.com/features/extensibility/)
- [User Stories](https://openwebui.com/)
