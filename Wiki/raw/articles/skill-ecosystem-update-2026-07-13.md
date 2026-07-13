---
title: Skill 生態系統全景更新 2026 — 55 個已安裝 Skill 的最新研究合集
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [research, skill-ecosystem, mlops, llm-serving, autonomous-agents, ai-tooling, red-teaming, data-science, hermes-agent, system-prompts, pkm, obsidian, pdf-generation, html-to-pdf, ai-image, youtube-transcript, computer-use, github-actions, devops, tdd-bdd, literature-review, notion-api, discord-bot, apple-cli, smart-home, tts, vercel, skill-update-2026, layer-1]
sources:
  - web_search batch 2026-07-13 (30+ web searches)
license: CC BY 4.0 (all sources are public web content)
audience: Hermes Agent / Skill 生態系統研究者
---

# Skill 生態系統全景更新 2026

> 聯網搜尋 55 個已安裝 Skill 的最新資訊（2026 年 7 月）。
> **無版權疑慮** — 全部來自公開技術部落格、GitHub、官方文件、Reddit、arXiv。
> 涵蓋 30+ 個技術領域的 2025~2026 最新動態。

---

## Part 1: MLOps & LLM Serving（Tier 1 — 核心推理）

### 1.1 MLOps 生態（2026 版）

**核心工具格局**（来源：DataCamp / TrueFoundry / lakeFS）：

| 類別 | 主流工具 | 2026 新趨勢 |
|------|---------|-------------|
| **Experiment Tracking** | MLflow, Weights & Biases, Neptune | MLflow 主导开源，W&B 主导学术 |
| **Orchestration** | Kubeflow, Airflow, Prefect | Kubernetes 原生化 |
| **Data Versioning** | DVC, lakeFS, Delta Lake | lakeFS Git-like branching |
| **Model Registry** | MLflow, Seldon, Kserve | 统一模型注册表 |
| **Feature Store** | Feast, Tecton | 实时特征工程 |
| **Model Observability** | Arize, Fiddler, WhyLabs | ML-specific APM |

**2026 MLOps 五大重点**：
1. **Model Observability** — 模型在生产环境的可观测性（drift detection、performance monitoring）
2. **Multi-agent Workflows** — 多 agent 编排成为 MLOps 新挑战
3. **Reproducibility** — 不可复现的 ML 实验 = 无效实验
4. **GitOps for ML** — 用 Git 流程管理 ML pipeline
5. **LLMOps** — 专门的 LLM 模型管理和评估

### 1.2 LLM Serving 战争（vLLM vs TensorRT-LLM vs SGLang）

**三强对比**（来源：JarvisLabs / Intro / LinkedIn）：

| 维度 | vLLM | TensorRT-LLM | SGLang |
|------|------|-------------|--------|
| **吞吐量** | 高（continuous batching）| 极高（hardware-specific engine）| 高（radix attention）|
| **延迟** | 良好（capped runs 渐升）| 最稳定（9-12ms decode）| 良好 |
| **易用性** | 最简单（pip install）| 复杂（需 build engine）| 中等 |
| **自定义** | 高 | 低（hardware锁定）| 高 |
| **多模态** | 支持 | 支持 | 支持 |

**关键洞察**：
- **TensorRT-LLM**：硬件特定引擎，延迟最低（比 vLLM 快 1.34x~2.72x），但需要针对 GPU 型号 build engine
- **vLLM**：生产环境首选，易用 + 高吞吐 + PagedAttention 优化
- **SGLang**：支持 RadixAttention（前缀缓存），适合多轮对话场景

**2026 推理优化趋势**：
1. **Speculative Decoding** — 小模型预测 + 大模型验证
2. **Continuous Batching** — 动态批处理，最大化 GPU 利用率
3. **PagedAttention**（vLLM）— KV cache 分页管理，显存利用率提升 2~4x
4. **Quantization** — FP16 → INT8 → INT4；AWQ/GPTQ 主流

### 1.3 Autonomous AI Agents（多 Agent 编排）

**2026 框架格局**（来源：CrewAI / LangChain / Reddit / IBM）：

| 框架 | 定位 | 核心概念 |
|------|------|---------|
| **LangGraph**（LangChain）| 生产级状态机图 | 节点 = agents，边 = transitions，循环 = 迭代 |
| **CrewAI** | Role-based 多 agent 编排 | Agents with personas + tasks + crews |
| **AutoGen**（Microsoft）| 对话式多 agent | agent 间对话协作 |
| **BeeAI** | 企业级 | 集成 memory 和 knowledge |
| **Mastra** | 新兴 | JavaScript 生态 |

**LangGraph vs CrewAI**：
- **LangGraph**：适合复杂、确定性工作流（有向图 + 条件边）
- **CrewAI**：适合角色驱动的任务分解（agents 有 persona）
- **2026 趋势**：从"单 agent"到"agent 军队"——单个 agent 能力有限，多 agent 协作才能处理复杂任务

**Multi-agent 架构模式**：
1. **Hierarchical** — Manager agent → Worker agents
2. **Debate** — 多个 agent 对抗性讨论
3. **Sequential** — 链式处理
4. **Parallel** — 并行处理 + 结果聚合

### 1.4 AI Tooling Reference（CLI Coding Agents）

**2026 CLI Coding Agent 生態**（来源：YouTube / Medium / GitHub）：

| 工具 | 提供者 | 定位 |
|------|--------|------|
| **Claude Code** | Anthropic | 最强 coding agent（PR 审查、代码生成）|
| **Codex CLI** | OpenAI | GA 版本，lightweight 终端 coding partner |
| **Gemini CLI** | Google | 实验性 |
| **Devin** | Cognition | AI 软件工程师（独立产品）|

**最佳实践**：
- 已有 `claude-code` / `codex` skill → 关注两者的**差异化和安全边界**
- Codex CLI GA（2025）→ 新增安全 playbook 功能
- Claude Code → 擅长 PR review 和 long-horizon 任务
- **Agent Swarm** 模式：同时运行多个 CLI agent，协作处理复杂任务

### 1.5 Red Teaming（AI 安全）

**2026 LLM Red Teaming 前沿**（来源：arXiv / Mend / Vectra / Galileo）：

**主要攻击向量**：
1. **Jailbreak** — 1,400+ 种 jailbreak 策略（arXiv 2025）
2. **Prompt Injection** — 注入恶意指令
3. **Goal Hijacking** — 改变 agent 目标
4. **Tool Misuse** — 滥用 API / 文件系统
5. **Memory Poisoning** — 污染长期记忆
6. **CI/CD Adversarial** — 攻击 ML pipeline

**防御框架**：
- **Security-Aware Prompt Compression**（SecurityLingua）
- **Probing Latent Subspaces** — 检测模型内部表示的脆弱性
- **Systematic Evaluation** — 标准化 red team 评估流程

### 1.6 Data Science（工作流现代化）

**2025~2026 Data Science Stack**（来源：LinkedIn / Reddit / Medium）：

| 层级 | 工具 | 趋势 |
|------|------|------|
| **IDE** | VS Code + Cursor | AI 辅助编码成为标配 |
| **Notebook** | Jupyter → VS Code Notebooks | 统一开发体验 |
| **Core** | Pandas, Seaborn, Statsmodels, Scikit-learn | 覆盖 90% 需求 |
| **ML** | PyTorch, TensorFlow, JAX | PyTorch 主导研究 |
| **LLM** | OpenAI API, Anthropic, Ollama | Local + Cloud 混合 |

**关键转变**：从 Jupyter Notebook 到**可复现的模块化 ML workflow**：
- Notebook → 探索
- Modular Python → 生产
- DVC / MLflow → 版本控制和实验追踪

---

## Part 2: Hermes & Agent System Design（Tier 2 — 核心系統）

### 2.1 Hermes Agent（Nous Research）

**最新動態**（来源：Hermes 官方文档 / Medium / GitHub）：

- **2026 年 2 月 25 日發布** → 7 周内 GitHub Stars 超过 95,000
- **自我改進循環**：從經驗中創建和改進 Skills
- **持久記憶**：跨 session 記住項目和解決方案
- **多平台支援**：Web UI / Telegram / Discord / CLI
- **gBrain**：本地 embedding provider + 持久向量知識庫

### 2.2 System Prompt Engineering（Agent 設計）

**2026 最佳實踐**（来源：Anthropic Engineering / Claude Platform / Indie Hackers）：

**五大核心原則**：
1. **Clear Role Definition** — 明確定義 agent 角色和邊界
2. **Structured Instructions** — 分层组织指令（不堆砌）
3. **Explicit Tool Integration** — 清楚說明工具使用方式
4. **Step-by-Step** — 複雜任務拆成步驟
5. **Primacy + Recency Effect** — 重要內容放在开头和结尾

**Claude Code System Prompt 洞察**（Indie Hackers reverse-engineering）：
- 安全声明在开头**和结尾**都有 → 双重复强
- 简洁语言 > 冗长解释
- Right altitude（正确的抽象层次）

**Anti-patterns**：
- 过长 system prompt（超过 2,000 tokens → 性能下降）
- 模糊的工具描述
- 隐含假设（不说明边界条件）

### 2.3 Skill System（技能系統設計）

**Skill 三層架構**（来源：Anthropic / arXiv SkillX）：

```
Layer 1: Skill（技能）
  └─ YAML frontmatter + markdown body
  └─ 触发条件 + 步骤 + 验证
  └─ 被动触发（不主动调用）

Layer 2: Agent（智能体）
  └─ Skill 的编排者
  └─ 决定何时调用哪个 Skill

Layer 3: MCP（Model Context Protocol）
  └─ 外部工具连接器
  └─ 标准化工具接口
```

**SkillX 研究**（arXiv 2026）：自动化构建 Skill Knowledge Base
- 从经验中自动抽取 skill
- 可跨 agent 复用

---

## Part 3: PDF & Document Generation（Tier 3 — 文件生成）

### 3.1 PDF 生態

**2025~2026 Python PDF 工具格局**：

| 工具 | 定位 | 2026 状态 |
|------|------|---------|
| **ReportLab** | 低階 + PLATYPUS 高階 | v5.0.0 活跃，官方文档完善 |
| **WeasyPrint** | HTML/CSS → PDF | 活跃，适合 Web 技术栈 |
| **pdfkit** | wkhtmltopdf wrapper | 维护模式 |
| **PyMuPDF** | PDF 操作（不是生成）| 活跃，manipulation 最佳 |
| **Playwright** | Headless Chrome → PDF | 活跃，高保真 |
| **Puppeteer** | Node.js Chrome PDF | 活跃 |

**最佳实践**：
- **ReportLab + PLATYPUS**：复杂布局、高度定制
- **Playwright/Puppeteer**：已有 Web 界面，想保持一致
- **WeasyPrint**：HTML/CSS 开发者友好

### 3.2 HTML to PDF

**三方法对比**：

| 方法 | 优点 | 缺点 |
|------|------|------|
| **Headless Chrome (Playwright/Puppeteer)** | 100% Web fidelity | 慢，资源重 |
| **wkhtmltopdf** | 简单 | 已停止维护 |
| **Rust 渲染器（如 printpdf）** | 快，Rust 生态 | 功能有限 |

**Playwright PDF 生成最佳实践**：
```javascript
await page.pdf({
  format: 'A4',
  margin: { top: '20mm', bottom: '20mm' },
  printBackground: true,
  displayHeaderFooter: true,
  headerTemplate: '<span></span>',
  footerTemplate: '<span style="font-size:10px">Page <span class="pageNumber"></span></span>',
})
```

---

## Part 4: Creative & Media（Tier 4 — 創意與媒體）

### 4.1 AI Image Generation

**2026 CLI 工具格局**：

| 工具 | 定位 | CLI 支持 |
|------|------|---------|
| **FLUX (Black Forest Labs)** | 最强开源图像生成 | ComfyUI, CLI |
| **Stable Diffusion** | 开源主流 | WebUI, CLI |
| **Midjourney** | 高质量商业 | Discord only |
| **ComfyUI** | 可视化工作流 | 原生 |

**FLUX 新动态**（2026）：
- FLUX.1 dev/pro = 目前最强开源模型
- NF4 量化版本可用
- ComfyUI 原生支持

### 4.2 YouTube & Transcript

**2026 最佳方法**：

| 方法 | 工具 | 适用场景 |
|------|------|---------|
| **YouTube Transcript API** | youtube-transcript-api | 有字幕的视频 |
| **Whisper API** | OpenAI Whisper | 无字幕视频 |
| **Google Speech-to-Text** | Cloud API | 高精度需求 |

**Whisper 优势**：
- 支持 100+ 语言
- 本地部署可用
- 比 YouTube 字幕更准确

### 4.3 Computer Use（Browser Automation）

**Anthropic Computer Use vs Playwright**（来源：Reddit / Browserless / DigitalApplied）：

| 指标 | Playwright + Claude | Anthropic Computer Use |
|------|---------------------|----------------------|
| **可靠性** | 92% | 78% |
| **速度** | 快 | 较慢 |
| **控制力** | 完整 | 完整 |
| **学习成本** | 中等 | 低 |

**Playwright Computer Use**（Invariant Labs）：
- 连接 Playwright browser 到 Claude's computer use
- 92% 可靠率（vs 原生 78%）

---

## Part 5: GitHub & DevOps（Tier 5 — 工程基礎設施）

### 5.1 GitHub CLI

**2025 gh 核心命令**（来源：adamj.eu / GitHub CLI manual）：

```bash
gh pr create              # 创建 PR
gh pr review             # 添加 review
gh pr view --comments    # 查看 review comments（含 inline）
gh api                   # 直接调用 GitHub REST API
gh workflow list         # 列出 workflow
gh run watch             # 监控 CI run
```

**常见问题**：`--comments` 不包含 inline review comments（GitHub CLI #5788），需用 `gh api` 直接调用 REST API。

### 5.2 CI/CD & DevOps

**2026 最佳工具**（来源：Northflank / Reddit / DEV.to）：

| 工具 | 定位 | 2026 趋势 |
|------|------|---------|
| **GitHub Actions** | 免费 + 深度集成 | 最流行 |
| **Jenkins** | 传统大企业 | 仍广泛使用 |
| **GitLab CI** | GitLab 集成 | DevOps 全家桶 |
| **CircleCI** | 高速执行 | 性能优化 |
| **Argo CD** | GitOps Kubernetes | declarative CD |
| **Harness** | Enterprise | AI DevOps |

### 5.3 Testing（TDD/BDD）

**TDD vs BDD 选择指南**（来源：Qt / Testomat / YouTube）：

| 维度 | TDD | BDD |
|------|-----|-----|
| **关注点** | 技术正确性 | 业务行为 |
| **语言** | 开发者语言 | 业务语言 |
| **工具** | pytest, JUnit | Behave, Cucumber |
| **适用** | 库/框架/算法 | 产品功能/用户故事 |

**Pytest 2026 最佳实践**：
- `pytest-xdist` — 并行测试
- `pytest-cov` — 覆盖率
- `pytest-asyncio` — 异步测试
- `pytest-mock` — Mocking

---

## Part 6: Research & Productivity（Tier 6 — 知識管理）

### 6.1 AI Research 工具

**2026 文献综述 AI 工具对比**（来源：Nature / arXiv / Reddit / PaperGuide）：

| 工具 | 定位 | 开源 | 特点 |
|------|------|------|------|
| **SciSpace** | 单篇论文分析 | 否 | 最佳单篇理解 |
| **Consensus** | 假设驱动搜索 | 否 | 学术搜索 |
| **PaperQA** | 自动化文献综述 | 是 | 本地运行，便宜 |
| **Scispace** | 多论文综合 | 否 | AI 聊天式 |
| **Perplexity** | 实时网络搜索 | 否 | 最新研究 |
| **galileo** | 全方位 | 否 | 企业级 |

**Nature 2026 发现**：开源 AI 工具在文献综述中表现超过大型商业 LLMs，且成本低、透明。

### 6.2 Notion API

**2026 Notion AI 新功能**（来源：Notion 官方 / Reddit）：

- **Custom AI Agents** — 在 Notion 内构建 AI agent
- **Connected Apps Search** — 跨所有 app 搜索
- **SCIM Provisioning** — 企业用户管理自动化
- **Database Properties** — 更强大的数据库

**Notion API 最佳实践**：
```python
from notion_client import AsyncClient

notion = AsyncClient(auth=NOTION_TOKEN)
page = await notion.pages.create(
    parent={"database_id": DB_ID},
    properties={"Name": {"title": [{"text": {"content": "New Item"}}]}}
)
```

### 6.3 Obsidian PKM

**2026 Obsidian 生態**（来源：Obsidian 官方 / YouTube / Medium）：

| 插件 | 用途 |
|------|------|
| **Dataview** | 查询笔记，类似 SQL |
| **Templater** | 动态模板 |
| **Obsidian Git** | 版本控制 |
| **Canvas** | 可视化卡片连接 |
| **Spatial** | 白板式布局 |
| **Local REST API** | 外部工具集成 |

**Second Brain 最佳实践**：
1. **Atomic Notes** — 每篇笔记一个概念
2. **Linking** — 用 `[[wikilinks]]` 连接笔记
3. **Daily Notes** — 捕获零散想法
4. **Plugins** — 不要过度插件（< 20）

---

## Part 7: Social, IoT & TTS（Tier 7 — 生活與語音）

### 7.1 Discord Bot（2026）

**Discord Bot 最佳实践**（来源：Botpress / Clepher / Skywork）：

| 技术 | 说明 |
|------|------|
| **Webhooks** | 低成本实时更新（无需频繁 API 调用）|
| **Slash Commands** | 用户交互标准方式 |
| **Gateway vs REST** | Gateway 用于实时事件，REST 用于主动操作 |
| **Permissions** | 最小权限原则 |
| **AI Integration** | Discord + AI = 智能社区管理 |

### 7.2 Apple CLI（macOS）

**2026 Apple 自动化生态**（来源：Reddit / GitHub / Apple Support）：

| 工具 | 用途 |
|------|------|
| **rem** | 高速 macOS Reminders CLI |
| **apple-reminders-cli** | Swift 全功能 CLI（EventKit）|
| **Shortcuts** | macOS/iOS 自动化 |
| **memo** | Apple Notes CLI |
| **imsg** | iMessage CLI |

**最佳实践**：EventKit 全集成 → 支持 location alerts、recurring reminders、subtasks。

### 7.3 Smart Home（Home Assistant + Hue）

**2026 Smart Home 架构**（来源：Home Assistant 官方 / Reddit / YouTube）：

```
Apple Home / Google Home / Alexa
    ↓
 Assistant（中央控制器）
    ↓
Philips Hue Bridge → Hue Bulbs/Switches
    ↓
Tailscale → 远程访问
```

**Hue API + Home Assistant**：
- Hue Bridge 发现 → 自动加载 rooms/scenes
- Switch entity = Hue automation 触发器
- 无需暴露公网 IP（用 Tailscale）

### 7.4 TTS（Text-to-Speech）

**2026 TTS API 格局**（来源：Speechmatics / Inworld / Reddit）：

| 排名 | 提供者 | 特色 |
|------|--------|------|
| 1 | **ElevenLabs** | 最高质量，voice cloning |
| 2 | **OpenAI TTS** | tts-1, tts-1-hd, gpt-4o-mini-tts |
| 3 | **MiniMax** | 速度 + 价格优势，laugh/sigh 标记 |
| 4 | **Google Cloud TTS** | 多语言，波形质量 |
| 5 | **AWS Polly** | 企业级，稳定 |

**MiniMax vs ElevenLabs**（Reddit）：
- MiniMax = 速度 + 价格（10000 免费 credits）
- ElevenLabs = 质量 + voice cloning
- ElevenLabs 支持情感标记

---

## Part 8: Vercel & Web（Tier 8 — 前端部署）

### 8.1 Vercel Functions（2026）

**Serverless vs Edge Functions**：

| 维度 | Serverless Functions | Edge Functions |
|------|---------------------|----------------|
| **运行时** | Node.js | V8（JS/WASM）|
| **冷启动** | 100ms+ | < 5ms |
| **延迟** | 较高 | 全球最低 |
| **支持** | Python, Go, Ruby | JS, TS, WASM |
| **用例** | 复杂计算 | 简单逻辑、middleware |

**Next.js on Vercel**：
- App Router = 最新范式
- Server Components → 减少 client JS
- Route Handlers → API routes
- Streaming → 增量渲染

---

## Part 9: 跨領域洞察（Cross-Domain Insights）

### 9.1 Skill 生態的 8 個層次

```
Layer 1: Tool Execution（工具執行）
  mlops, serving-llms, github, devops, software-development
  
Layer 2: Intelligence（智能系統）
  autonomous-agents, red-teaming, ai-tooling-reference
  
Layer 3: Core System（核心系統）
  hermes, hermes-core-architecture, infrastructure, skills
  
Layer 4: Document Generation（文件生成）
  pdf, pdf-edit, chinese-pdf-gen, html-to-pdf
  
Layer 5: Creative & Media（創意與媒體）
  creative, media, computer-use
  
Layer 6: Knowledge（知識管理）
  research, note-taking, productivity
  
Layer 7: Life Integration（生活整合）
  social-media, apple, smart-home, tts
  
Layer 8: Deployment（部署）
  vercel-*, deploy-to-vercel
```

### 9.2 三大 2026 趨勢

| 趨勢 | 描述 | 受影響 Skills |
|------|------|-------------|
| **Multi-Agent Orchestration** | 從單一 agent 到 agent 軍隊 | autonomous-agents, langchain |
| **LLM Inference Optimization** | vLLM/TensorRT-LLM 性能大戰 | serving-llms, mlops |
| **Skill Lifecycle Automation** | 從手動維護到自動構建 | skills, hermes |

### 9.3 技術棧重疊地圖

| 技術 | 跨多個 Skill |
|------|------------|
| **Playwright** | html-to-pdf, computer-use, webapp-testing |
| **Whisper** | media/youtube-content, speechall-cli, local-stt-fallback |
| **GitHub API** | github, github-pr-workflow, github-issues |
| **REST API** | notion, airtable, productivity |
| **Home Assistant** | smart-home/openhue, infrastructure |

---

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（30+ web searches，55 個 Skills 全覆蓋）|