---
title: The Agent Control Plane — Activant Research (2026)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [report, agent-control-plane, governance, orchestration, enterprise-ai, activant]
url: https://www.activantcapital.com/research/the-agent-control-plane/
author: Activant Capital Research
date: 2026
venue: VC research report
---

# The Agent Control Plane — Source Material

## 問題陳述

> 企業 AI 採用進入「第二階段」：從 **adopt**（採用）轉向 **govern**（治理）

**現實數據**：
- 95% 企業 AI 試點**無可衡量 P&L 影響**（MIT 2025 AI Report）
- 88% 企業 agent 專案**未達生產**
- 80% 公司**已發生**未授權 AI agent 動作
- 平均企業使用 **300+ SaaS 應用**（Okta 2023）
- 40% 公司有官方 AI 訂閱，但 **90% 員工**私下用 AI 工具（「shadow AI」）

## 解方：Agent Studio + AI Marketplace

**類比 Apple iOS 生態系**：
- **Agent Studio**：建構工具（iOS = Xcode）
- **AI Marketplace**：預建應用市集（iOS = App Store）
- **控制平面**：統一治理層（iOS = App Review + iCloud）

## 4 大核心能力

### 1. Governance & Identity
- **Per-agent identity**：agent 不用人類憑證，用 least-privilege service accounts
- **Policy-as-code at runtime**：地理、PII、模型選擇自動執行
- **Built-in redaction**：redaction 是 runtime 能力，不是 policy 文件

### 2. Context & Tooling
- **Scoped, mortal memory**：agent 只記得應該記得的
- **Tools are contracts**：每個 tool 簽名、限速、approval-gated

### 3. Studio & Orchestration
- **Visual flows**：在 canvas 上組裝 multi-step workflows
- **Production-ready by default**：versioned + reproducible + CI/CD friendly

### 4. Evals & Economics
- **Evaluate before ship**：first-class eval loops + sandboxes
- **Telemetry for finance**：每個 call 可追溯、可 replay、可計價

## 「Agent Builder Platform」 = 終局

> 統一 AI workforce marketplace：整合 build、buy、deploy、govern

**for whom**：
- 忙碌專業人士 → 買 pre-built agent
- 非技術 power-user → 用 no-code 自建
- 技術/IT 團隊 → full-stack custom

## 與 Hermes 的對應

| Activant 概念 | Hermes 實作 | 差距 |
|--------------|-------------|------|
| Per-agent identity | subagent via `delegate_task` | ⚠️ 無獨立 service account |
| Policy-as-code | `RULES.md` + E-code | ✅ 已實作 |
| Built-in redaction | `_sanitize_error` + `_CREDENTIAL_PATTERN` | ✅ |
| Scoped mortal memory | `fact_store`（holographic）| ✅ |
| Tools as contracts | MCP servers | ✅ |
| Visual flows | Dashboard WebUI | ⚠️ 無 visual workflow canvas |
| Eval loops | E 階段御史 | ✅ |
| Telemetry for finance | `~/.hermes/logs/` | ⚠️ 未整合到計價 |
| Agent Builder Platform | Skill + Plugin 系統 | ⚠️ 無統一 marketplace |

## 引用

> The Agent Control Plane emerges as the missing layer – a combination of inventory, policy engine, orchestration and observability that sits above models and agents, enforcing policies at the moment of action, recording what happened and enabling reversibility. — Mahmoud Abulfadda (LinkedIn)