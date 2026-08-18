# Hermes Agent 官方 GitHub 深度分析

**來源**：https://github.com/NousResearch/hermes-agent  
**分析日期**：2026-06-10  
**Stars**：189k | **Forks**：32.7k | **Commits**：11,265

---

## 基本概覽

Hermes Agent 是 Nous Research 開發的**自我改進 AI Agent**，具備內建學習循環。它是唯一具有內建學習循環的 Agent——從經驗中創建技能、在使用中改進、督促自己持久化知識、搜索過往對話，並在 sessions 之間建立不斷深化的用戶模型。

### 核心定位

> It's not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. It's an **autonomous agent** that gets more capable the longer it runs.

### 支援的模型提供商

| 提供商 | 備註 |
|--------|------|
| Nous Portal | 推薦，一站式 OAuth |
| OpenRouter | 200+ models |
| NovitaAI | AI-native cloud |
| NVIDIA NIM | Nemotron |
| Xiaomi MiMo | |
| z.ai / GLM | |
| Kimi / Moonshot | |
| **MiniMax** | ✅ |
| Hugging Face | |
| OpenAI | |
| 自定義端點 | |

---

## 核心架構設計原則

### 兩大核心屬性

1. **Per-conversation prompt caching is sacred**
   - 長对话重用缓存的前缀。任何改变过去上下文、交换工具集或在对话中途重建系统提示的操作都会使缓存失效并增加用户成本。
   - 唯一例外：context compression

2. **The core is a narrow waist; capability lives at the edges**
   - 每个模型工具都在每次 API 调用时发送，所以新核心工具的门槛很高。
   - 大部分新能力应作为 CLI 命令 + skill、服务级工具、或插件——而不是核心表面。

### Footprint Ladder（优先级顺序）

新能力接入顺序：
1. 扩展现有代码
2. CLI 命令 + skill
3. 服务级工具（`check_fn`）
4. 插件
5. MCP 服务器
6. 新核心工具（**最后手段**）

---

## 主要目錄結構

```
hermes-agent/
├── .github/           # CI/CD workflows
├── .plans/            # PR/功能计划文档
├── acp_adapter/       # Agent Communication Protocol 适配器
├── acp_registry/      # ACP 注册表
├── agent/             # 核心 Agent 逻辑
├── apps/              # 应用程序（Desktop, TUI等）
├── assets/            # 资源文件
├── cron/              # 定时任务系统
├── datagen-config-examples/  # 数据生成配置示例
├── docker/            # Docker 相关
├── docs/              # 文档
│   ├── kanban/        # Kanban 功能文档
│   ├── middleware/    # 中间件文档
│   └── observability/ # 可观测性文档
├── gateway/           # 消息网关（Telegram, Discord等）
├── hermes_cli/        # CLI 实现
└── locales/          # 国际化
```

---

## 核心功能模塊

### 1. Messaging Gateway（消息网关）

支援平台：Telegram, Discord, Slack, WhatsApp, Signal, SMS, Email, Home Assistant, Mattermost, Matrix, DingTalk, Feishu/Lark, WeCom, Weixin, BlueBubbles (iMessage), QQ, Yuanbao, Microsoft Teams, LINE, ntfy, Browser

每個平台適配器接收消息、通過每 chat session store 路由，並分發到 AIAgent 處理。网关还运行 cron 调度器，每 60 秒 tick 一次执行任何到期的 job。

### 2. Terminal Backend（终端后端）

| Backend | 描述 | 使用場景 |
|---------|------|---------|
| local | 本地运行（默认） | 开发、信任任务 |
| docker | 隔离容器 | 安全、可重现性 |
| ssh | 远程服务器 | 沙箱、隔离 Agent 与自身代码 |
| singularity | HPC 容器 | 集群计算、无 root |
| modal | 云端执行 | 无服务器、扩展 |
| daytona | 云端沙箱工作区 | 持久化远程开发环境 |

### 3. Memory System（記憶系統）

两个文件组成 Agent 的記憶：

| 文件 | 用途 | 字元限制 |
|------|------|---------|
| **MEMORY.md** | Agent 的个人笔记 | 2,200 chars (~800 tokens) |
| **USER.md** | 用户画像 | 1,375 chars (~500 tokens) |

**Frozen snapshot pattern**：系统提示注入在 session 开始时捕获一次且永不改变。Agent 在 session 中添加/删除记忆条目时，更改立即持久化到磁盘，但直到下一个 session 开始才会出现在系统提示中。

### 4. Skills System（技能系統）

Skills 是按需知识文档，遵循**渐进式披露**模式以最小化 token 使用：

```
Level 0: skills_list()           → [{name, description, category}, ...]
Level 1: skill_view(name)        → Full content + metadata
Level 2: skill_view(name, path)  → Specific reference file
```

所有 skills 位于 `~/.hermes/skills/`，相容 [agentskills.io](https://agentskills.io/specification) 开放标准。

### 5. MCP (Model Context Protocol)

Hermes 通过 MCP 连接到外部工具服务器：
- 本地 stdio 服务器和远程 HTTP MCP 服务器
- 自动工具发现和注册
- 每个服务器的过滤，暴露所需工具

### 6. SOUL.md（人格系統）

`SOUL.md` 是**主要身份**——它是系统提示中的第一个内容，定义 Agent 是谁。默认位于 `~/.hermes/SOUL.md`。

人格文件内容直接进入系统提示的 slot #1——代理身份位置。不添加包装语言。

### 7. Cron Job System（定時任務）

内置 cron 调度器，支持：
- 每日报告
- 夜间备份
- 每周审计
- 自然语言配置，无人值守运行

交付目标：任何平台（origin, all, 或特定 platform:chat_id:thread_id）

### 8. Delegation（委派系統）

- 生成隔离的 subagents 进行并行工作流
- 编写调用工具的 Python 脚本（通过 RPC）
- 将多步骤管道折叠为零上下文成本 turns

---

## 工具生態

### 內建工具分類

| 類別 | 工具示例 | 描述 |
|------|---------|------|
| Web | `web_search`, `web_extract` | 搜索网页、提取页面内容 |
| X Search | `x_search` | X (Twitter) 搜索（需要 xAI 凭证）|
| Terminal & Files | `terminal`, `process`, `read_file`, `patch` | 执行命令、文件操作 |
| Browser | `browser_navigate`, `browser_snapshot`, `browser_vision` | 交互式浏览器自动化 |
| Media | `vision_analyze`, `image_generate`, `text_to_speech` | 多模态分析与生成 |
| Agent orchestration | `todo`, `clarify`, `execute_code`, `delegate_task` | 计划、澄清、代码执行、subagent 委托 |
| Memory & recall | `memory`, `session_search` | 持久记忆与 session 搜索 |
| Automation & delivery | `cronjob`, `send_message` | 定时任务、出站消息投递 |
| Integrations | `ha_*`, MCP server tools | Home Assistant、MCP 等 |

### Nous Tool Gateway

付费 [Nous Portal](https://portal.nousresearch.com/) 订阅者可以使用：
- Web search
- Image generation
- TTS
- Cloud browser

无需单独的 API 密钥。

---

## 安裝方式

### Linux / macOS / WSL2 / Android (Termux)
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### Windows (Native)
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

### 安裝後快速配置
```bash
hermes setup --portal  # 最快路径：OAuth 覆盖 model + 4 个 Tool Gateway 工具
```

### Installer 處理內容
- uv（快速 Python 包管理器）
- Python 3.11（通过 uv，无需 sudo）
- Node.js v22（浏览器自动化和 WhatsApp bridge）
- ripgrep（快速文件搜索）
- ffmpeg（TTS 音频格式转换）

---

## 開發貢獻指南（AGENTS.md 要點）

### 歡迎的貢獻

- **修复真实 bug**：好的修复在当前 `main` 上复现症状，指向确切行，修复整个 bug 类
- **在边缘扩展覆盖**：新平台适配器、渠道、提供商、模型、桌面/TUI/仪表盘功能
- **重构 god-files**：将多行文件提取为聚焦模块
- **保持核心狭窄**：新模型工具是昂贵异常——优先扩展现有代码

### 不歡迎的貢獻

- 改变检测器测试（freeze 当前值而非行为契约）
- 未经验证的单元 mocks（需要 E2E 验证）
- 绕过现有基础设施的重复模块

### 設計原則

- **Behavior contracts over snapshots**：测试断言数据关系（不变量），而非冻结当前值
- **E2E validation**：对任何涉及解析链、配置传播、安全边界、远程后端或文件/网络 I/O 的内容，使用真实路径

---

## 版本與最近更新

### 最新動態（2026-06-10）
- `fix(docker): optimize image size — .dockerignore, drop dev deps, split layers` (a72bb03)
- `feat(kanban): gate notifier watcher on dispatch_in_gateway`
- `perf(ci): cache uv + use uv sync in tests workflow`
- `feat(observability): observer-grade telemetry hooks + NeMo-Relay plugin`
- `fix(middleware): preserve translated downstream failures`

### YOLO Mode（PR #724）
- `--yolo` flag：绕过所有批准提示
- `HERMES_YOLO_MODE` 环境变量
- 作者：dmahan93

---

## 與用戶環境的相關性

### 用戶當前配置
- **Provider**：MiniMax International (minimax.io)
- **Model**：MiniMax-M2.7
- **API endpoint**：https://api.minimax.io/v1
- **Auth**：auth.json（SSOT）
- **安裝路徑**：~/.hermes/hermes-agent/

### 對應功能映射

| 用戶需求 | Hermes 功能 | 當前狀態 |
|---------|------------|---------|
| 接入 MiniMax | 内置 provider | ✅ 已配置 |
| 每日工作日誌 | cron job + obsidian skill | ✅ 已設定 |
| ChromaDB 攝入 | cron job 內 Python chromadb | ✅ 已驗證 |
| GitHub 備份 | hermes-cli git 操作 | ✅ 已實現 |
| Session 搜索 | session_search tool | ✅ 內建 |
| 記憶持久化 | memory tool | ✅ 內建 |
| 技能系統 | skills system | ✅ 內建 |

---

## 標籤

#hermes-agent #nous-research #ai-agent #self-improving #open-source #github