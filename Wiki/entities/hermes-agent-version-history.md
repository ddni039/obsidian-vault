---
uid: e-bd729a5b7011
title: "Hermes Agent 版本歷史"
created: "2026-07-04"
source: "nousresearch/hermes-agent GitHub repository analysis"
tags: [entity, hermes, versioning, release-history]
related_tags: [hermes-agent, hermes-learning-loop, hermes-skills-system, hermes-messaging-gateway]
---

# Hermes Agent 版本歷史

## 總覽

Hermes Agent 採用**雙軌版本命名**：
- **內部版本**：`vYYYY.M.D` 格式（時間戳導向，如 `v2026.3.12`）
- **對外版本**：`v0.N.0` 格式（公版號，如 `v0.4.0`）

版本從 `v0.2.0`（2026-03-12）到 `v0.18.0`（2026-07-01），4個月內共發布 19 個版本。

---

## 版本釋出時間線

| 內部版本 | 對外版本 | 日期 | 主要變更量 |
|---------|---------|------|-----------|
| v2026.3.12 | v0.2.0 | 2026-03-12 | 初始版本基礎設施 |
| v2026.3.17 | v0.3.0 | 2026-03-17 | +OAuth/PKCE +平臺接入 |
| v2026.3.23 | v0.4.0 | 2026-03-23 | +SSRF防護 +配置替換 |
| v2026.3.28 | v0.5.0 | 2026-03-28 | +工具使用強制執行 |
| v2026.3.30 | v0.6.0 | 2026-03-30 | +多工作區Slack +Matrix語音 |
| v2026.4.3  | v0.7.0 | 2026-04-03 | +MCP穩定性 +更新加固 |
| v2026.4.8  | v0.8.0 | 2026-04-08 | +預算系統 +Feishu卡片 |
| v2026.4.13 | v0.9.0 | 2026-04-13 | +儀表板OAuth +Kimi provider |
| v2026.4.16 | v0.10.0 | 2026-04-16 | +Tool Gateway發布 |
| v2026.4.23 | v0.11.0 | 2026-04-23 | +Cron enabled_toolsets |
| v2026.4.30 | v0.12.0 | 2026-04-30 | +Curator技能統計 |
| v2026.5.7  | v0.13.0 | 2026-05-07 | +Google Chat平臺 |
| v2026.5.16 | v0.14.0 | 2026-05-16 | +X Search +osint-investigation |
| v2026.5.28 | v0.15.0 | 2026-05-28 | +桌面i18n(ZH) +XAI代理 |
| v2026.5.29 | v0.15.1 | 2026-05-28 | patch |
| v2026.5.29.2 | v0.15.2 | 2026-05-29 | patch (ethernet) |
| v2026.6.5  | v0.16.0 | 2026-06-05 | +桌面多語系 +max_tokens傳播鏈 |
| v2026.6.19 | v0.17.0 | 2026-06-19 | +MCP elicitation +Raft平臺 |
| v2026.7.1  | v0.18.0 | 2026-07-01 | +Vertex provider +安全加固 |

---

## 各版本詳細變更

### v0.2.0 / v2026.3.12（2026-03-12）
**類型**：初始版本基礎設施

**主要 commit**：
- `323ca708` feat: add versioning infrastructure and release script
- `8d182ec7` chore: bump version to v0.2.0 + add curated first-release changelog
- `92e9809c` fix: fetch live model lists from provider APIs instead of static lists

**說明**：建立版本管理基礎設施，包含版本化腳本與首版變更日誌框架。

---

### v0.3.0 / v2026.3.17（2026-03-17）
**類型**：認證與平臺接入

**主要 commit**：
- `4768ea62` fix: skip stale cron jobs on gateway restart instead of firing immediately
- `63e88326` feat: Hermes-native PKCE OAuth flow for Claude Pro/Max subscriptions
- `b7980625` fix: improve OAuth login UX for headless/SSH users
- `46176c80` refactor: centralize slash command registry (#1603)
- `3576f44a` feat: add Vercel AI Gateway provider (#1628)
- `474301ad` fix: improve execute_code error logging and harden cleanup (#1623)

**說明**：增加 OAuth PKCE 認證流程、 slash command 集中註冊、 Vercel AI Gateway provider 支援，以及 cron job 重啟邏輯修正。

---

### v0.4.0 / v2026.3.23（2026-03-23）
**類型**：安全與配置增強

**主要 commit**：
- `4ff73fb3` feat(config): support `${ENV_VAR}` substitution in config.yaml (#2684)
- `f9c2565a` fix(security): prevent shell injection in `_expand_path` via ~user paths
- `0791efe2` fix(vision): make SSRF redirect guard async for httpx.AsyncClient
- `934fbe3c` fix(security): add SSRF protection to vision_tools and web_tools
- `6302e56e` fix: strip ANSI at the source — clean terminal output before it reaches display
- `868b3c07` fix: platform default toolsets silently override tool deselection in skills

**說明**：大幅強化安全防護（SSRF + shell injection），同時引入 `${ENV_VAR}` 配置替換語法。

---

### v0.5.0 / v2026.3.28（2026-03-28）
**類型**：工具使用強制執行

**主要 commit**：
- `901494d7` feat: make tool-use enforcement configurable via `agent.tool_use_enforcement`
- `831e8ba0` feat: tool-use enforcement + strip budget warnings from history
- `455bf2e8` feat: activate plugin lifecycle hooks (pre/post_llm_call, session start/end)
- `735ca9df` refactor: replace swe-rex with native Modal SDK for Modal backend
- `df6ce848` fix(provider): remove MiniMax `/v1`→`/anthropic` auto-correction
- `80a899a8` fix: enable fine-grained tool streaming for Claude/OpenRouter + retry on truncation
- `b6b87ded` fix: discover plugins before reading plugin toolsets in tools_config

**說明**：核心功能改進，包括工具使用強制執行配置、外掛生命週期鉤子、Modal SDK 整合，以及 MiniMax provider 修正。

---

### v0.6.0 / v2026.3.30（2026-03-30）
**類型**：多平臺訊息與自動化

**主要 commit**：
- `efae525d` feat(plugins): add `inject_message` interface for remote message injection
- `5148682b` feat: mount skills directory into all remote backends with live sync
- `791f4e94` feat(slack): multi-workspace support via OAuth token file (#3903)
- `947faed3` feat(approvals): make dangerous command approval timeout configurable
- `649d1494` feat(telegram): add webhook mode as alternative to polling (#3880)
- `839f798b` feat(telegram): add group mention gating and regex triggers (#3870)
- `ce2841f3` feat(gateway): add WeCom (Enterprise WeChat) platform support (#3847)
- `5148682b` feat(matrix): support native voice messages via MSC3245 (#3877)
- `56024587` security: harden dangerous command detection and add file tool path allowlist

**說明**：大量新平臺支援（WeCom、Slack多工作區、Telegram webhook、Matrix語音），以及危險命令審批超時可配置化。

---

### v0.7.0 / v2026.4.3（2026-04-03）
**類型**：MCP 穩定性與更新系統

**主要 commit**：
- `cc54818d` fix(mcp): stability fix pack — reload timeout, shutdown cleanup, event handling
- `f374ae4c` fix: prevent compression death spiral from API disconnects
- `8fd9fafc` fix: handle Anthropic Sonnet long-context tier 429 by reducing to 200k
- `6b0022bb` Add fork detection and upstream sync to `hermes update`
- `0109547f` fix(update): handle conflicted git index during `hermes update` (#4735)
- `988ecc74` fix(update): avoid launchd restart race on macOS
- `a9330795` fix(cli): surface recent sessions inside `/history` and `/resume`

**說明**：MCP 穩定性修復、更新系統加固（fork偵測、git index衝突處理）、以及 Anthropic 長上下文 tier 429 處理。

---

### v0.8.0 / v2026.4.8（2026-04-08）
**類型**：預算控制與 Feishu 整合

**主要 commit**：
- `c8a5e36b` feat(prompting): self-optimized GPT/Codex tool-use guidance via auto-generated prompts
- `77c5bc9d` feat(budget): make tool result persistence thresholds configurable
- `65e24c94` wip: tool result fixes — persistence
- `598c25d4` feat(cron): track delivery failures in job status (#6042)
- `5c03f2e7` fix: provider/model resolution — salvage 4 PRs + MiniMax aux URL fix
- `598c25d4` feat(feishu): add interactive card approval buttons (#6043)
- `7fe6782a` feat: use `mimo-v2-pro` for non-vision auxiliary tasks on Nous free tier
- `2ad76948` fix(mcp): preserve structured_content in tool call results

**說明**：增加工具結果持久化閾值配置、Cron 交付失敗追蹤、Feishu 卡片審批按鈕，以及自優化 GPT/Codex 提示詞引導。

---

### v0.9.0 / v2026.4.13（2026-04-13）
**類型**：儀表板與 provider 擴展

**主要 commit**：
- `2b3aa362` feat(providers): add `kimi-coding-cn` provider for mainland China users
- `247929b0` feat: dashboard OAuth provider management
- `ba50fa30` fix(run_agent): refresh activity during streaming responses
- `c449cd1a` fix(config): restore custom providers after v11→v12 migration
- `0dd26c94` fix(tests): fix 78 CI test failures and remove dead test (#9036)
- `2a9e50c1` fix(copilot): resolve GHE token poisoning when GITHUB_TOKEN is set
- `381810ad` feat: fix SQLite safety in `hermes backup` + add `--quick` snapshots

**說明**：新增 Kimi provider（大陸用戶）、儀表板 OAuth provider 管理介面、備份快照功能，以及大量 CI 測試修復。

---

### v0.10.0 / v2026.4.16（2026-04-16）
**類型**：Tool Gateway 開放

**主要 commit**：
- `f188ac74` feat: ungate Tool Gateway — subscription-based access with per-tool billing
- `10edd288` docs: add Nous Tool Gateway documentation
- `0517ac3e` fix(agent): complete Claude Opus 4.7 API migration
- `37913d91` fix(agent): downgrade xhigh→max on Anthropic pre-4.7 adaptive models
- `c1809e85` fix(gateway): handle stale lock files in `acquire_scoped_lock`
- `fe12042e` fix: remove context pressure warnings entirely (#11039)

**說明**：Tool Gateway 正式開放（訂閱制按工具計費），完整支援 Claude Opus 4.7 API遷移，並移除 context pressure 警告。

---

### v0.11.0 / v2026.4.23（2026-04-23）
**類型**：Cron 精細化控制

**主要 commit**：
- `8b79acb8` feat(cron): expose `enabled_toolsets` in cronjob tool and `create_job()`
- `0086fd89` feat(cron): support `enabled_toolsets` per job to reduce token overhead
- `a5e4a86e` feat(xai): add xAI image generation provider (grok-imagine-image)
- `d42b6a2ed` docs(agents): refresh AGENTS.md — fix stale facts, expand plugins/skills
- `c7d02393` Update CONTRIBUTING.md
- `67c8f837` fix(mcp): per-process PID isolation prevents cross-session crash

**說明**：Cron job 支援 per-job `enabled_toolsets` 配置以節省 token、新增 xAI 圖像生成 provider（MCP per-process PID 隔離修復）。

---

### v0.12.0 / v2026.4.30（2026-04-30）
**類型**：Curator 與技能管理

**主要 commit**：
- `d60a9917` feat(curator): show most-used and least-used skills in `hermes curator`
- `8b290a59` feat(curator): split archived into consolidated vs pruned with mode selection
- `564a649e` fix(curator): scan nested archive subdirs in `restore_skill`
- `4e296dcd` fix(auxiliary): pass raw base_url to `_maybe_wrap_anthropic` for correct header signing
- `b50bc13e` fix(config): preserve YAML lists in `hermes config set` (#17876)
- `e0fa2cf9` fix: prevent bare 'custom' slug in `model.provider` (#17478)

**說明**：Curator 技能統計功能（使用頻率排行）、封存技能分類管理，以及配置集合操作修復。

---

### v0.13.0 / v2026.5.7（2026-05-07）
**類型**：新平臺整合

**主要 commit**：
- `44cd79e7` feat(plugins/google_chat): Google Chat platform adapter as a bundle plugin
- `af9336d5` feat(gateway): generic plugin hooks for env enablement + cron delivery
- `de584cd1` feat(qqbot): add inline-keyboard approvals and update prompts
- `ac51c4c1` feat(kanban): per-task `max_retries` override
- `04918345e` fix(cron): initialize MCP servers before constructing the cron AIAgent
- `c8e3e391` fix(mcp): surface image tool results as MEDIA tags instead of dropping

**說明**：新增 Google Chat 平臺適配器、通用外掛鉤子機制、QQ Bot 內聯鍵盤審批，以及 Kanban per-task `max_retries` 覆寫。

---

### v0.14.0 / v2026.5.16（2026-05-16）
**類型**：安全加固與工具擴展

**主要 commit**：
- `74d0b392` feat(x_search): gated X (Twitter) search tool with OAuth-or-API-key auth
- `5f91b1a4` feat(skills): add `osint-investigation` optional skill
- `395e9dd9` feat: add `supports_parallel_tool_calls` for MCP servers (#26825)
- `6ba35ec3` security(deps): bump aiohttp, anthropic, cryptography to CVE-fixed versions
- `627f8a5f` security: sanitize tool error strings before injecting into model context
- `016c772e` feat(plugins): tool override flag for replacing built-in tools
- `c9b32a65` feat(skill): `darwinian-evolver` optional skill

**說明**：新增 X (Twitter) 搜尋工具、OSINT 調查技能、平行工具呼叫支援，同時大量安全相關依賴更新。

---

### v0.15.0 / v2026.5.28（2026-05-28）
**類型**：i18n 與代理增強

**主要 commit**：
- `1d9c3eba` feat(desktop): persist i18n language in config
- `4a1907bd` feat(desktop): add i18n with Simplified Chinese (zh-Hans) support
- `345821b4` fix(security): separate OAuth PKCE state from code_verifier
- `72f94f4a` test(security): regression guard for OAuth PKCE state/verifier separation
- `1a747957` feat: add claude-opus-4.8 and claude-opus-4.8-fast
- `e0572a6d` feat(agent): buffer retry/fallback status, surface only on terminal response
- `eafe11d4` perf(skills-page): lazy-fetch the catalog instead of bundling 34MB metadata

**說明**：桌面應用完整 i18n 支援（簡體中文）、安全 OAuth PKCE 狀態分離、Claude Opus 4.8 模型支援，以及技能頁面效能優化。

---

### v0.15.1 / v2026.5.29
**類型**：Patch
**說明**：微調版本，無重大變更。

---

### v0.15.2 / v2026.5.29.2
**類型**：Patch（ethernet）
**說明**：由 ethernet 維護者發布的微調版本。

---

### v0.16.0 / v2026.6.5（2026-06-05）
**類型**：多語系與傳播鏈修復

**主要 commit**：
- `1d9c3eba` feat(desktop): add i18n with Simplified Chinese (zh-Hans) support
- `02d6bf1c` fix(desktop+gateway): full multi-profile support over one global-remote connection
- `1c909e75` fix(cli,gateway): complete max_tokens propagation — CLI path + env bridge
- `14275d7b` fix(gateway): honor per-provider `max_output_tokens` in max_tokens chain
- `1a3e6085` feat(desktop): per-profile remote gateway hosts (#39778)
- `72eb42d9` feat(update): stash/restore by default + settable discard for non-interactive updates
- `06268f11` feat(gateway): explain `/voice` usage when toggled bare

**說明**：完整 i18n（簡中）、`max_tokens` 傳播鏈全面修復、桌面多 profile 遠端閘道支援，以及更新時 stash/restore 機制。

---

### v0.17.0 / v2026.6.19（2026-06-19）
**類型**：MCP 深度整合

**主要 commit**：
- `239740a1` feat(tools): MCP elicitation handler with gateway-aware approval routing
- `37134838` fix(mcp): refresh agent tool snapshot between turns (cache-safe latency hiding)
- `93d6e730` fix(mcp): expose late-connecting MCP tools to the agent (TUI/CLI/gateway)
- `16642e27` refactor(cron): copy os.environ before sanitizing for subprocess
- `da725321` fix(cron): sanitize env for job script subprocesses
- `26e76a75` feat(telegram): opt-in Online/Offline bot status indicator
- `9026a8c7` feat(gateway): add Raft bundled platform plugin with activity hooks
- `ac00e736` feat(dashboard): add a reasoning-effort picker to the chat sidebar

**說明**：MCP elicitation 處理器（帶閘道感知審批路由）、MCP 工具延遲連接暴露、Raft 平臺插件，以及 reasoning-effort 選擇器。

---

### v0.18.0 / v2026.7.1（2026-07-01）
**類型**：安全加固 + Vertex + Windows

**主要 commit**：
- `c73e7438` feat(vertex): add Google Vertex AI provider for Gemini (OAuth2)
- `5248877c` security(gateway): prove chat/thread origin for persisted `/resume`; fail closed on no-provenance
- `bb6e216a` security(gateway): scope Matrix `/resume` by thread, not just room
- `c4f278c0` security(gateway): scope `/resume` and `/sessions` to the caller's origin
- `5d613a56` fix(terminal): route init_session bootstrap cd through Windows path expansion
- `9ed7252a` fix(terminal): prefer Git for Windows bash over Linux bash on Windows
- `ba0bc01d` feat(delegate): remove model-facing toolsets arg — subagents always inherit parent toolsets
- `eae3700b` fix(moa): raise aux timeouts to 900s and give Codex aux path a retry on timeout
- `b795a45b` fix(compaction): detect and strip merge-into-tail summaries past threshold

**說明**：大量安全相關改進（`/resume` 源證明、Matrix 範圍限制）、新增 Vertex AI provider、Windows 原生支援改進、Delegate subagent toolsets 簡化，以及 MoA 超時延長至 900s。

---

## 版本差異分析

### 成長規模

| 版本區間 | 檔案變更數 | 總變更行數 |
|---------|----------|-----------|
| v0.4.0 → v0.18.0 | ~5957 個 | +1,817,479 / -118,260 行 |

### 主要功能軸線

1. **平臺擴展**：Telegram → Slack → Discord → WhatsApp → WeCom → Matrix → Google Chat → QQBot → Raft → Vertex
2. **安全加固**：OAuth PKCE → SSRF防護 → Shell injection → `/resume` 源驗證 → Matrix scope
3. **MCP 深化**：從無到完整 MCP elicitation、工具快照刷新、PID 隔離
4. **i18n**：v0.15.0 開始桌面完整多語系支援（簡體中文優先）
5. **Provider 擴展**：Nous → OpenRouter → OpenAI → Vercel → Kimi → xAI → Vertex

### 非正式版本標籤（Backup Tags）

```
backup/opentui-prestrip-20260616-1950
backup/precopystrip-20260616-2058
clean-before-remerge
desktop-pr20059-installers
merge-commit-backup
premerge-oh-god
```
這些為開發過程中的臨時備份點，非正式 release。

---

## 更新頻率統計

- **平均發布間隔**：約 5.3 天
- **最快區間**：v2026.5.28 → v2026.5.29（1天，patch）
- **最慢區間**：v2026.5.16 → v2026.5.28（12天）
- **熱點開發領域**：安全修復 > MCP > 桌面客戶端 > 平臺整合

---

## Source

- GitHub: https://github.com/nousresearch/hermes-agent
- 分析日期：2026-07-04
- 資料來源：bare git repository clone（tags / commit history / diff stats）
