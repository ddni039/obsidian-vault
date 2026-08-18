---
title: Agent Control Plane
created: 2026-07-13
updated: 2026-07-13
uid: e-76974fc2bd41
type: entity
tags: [concept, governance, orchestration, enterprise-ai, control-plane, market]
sources:
  - raw/articles/agent-control-plane-activant-2026-07-13.md
related:
  - "[[agent-harness]]"
  - "[[forrester-agent-control-plane]]"
confidence: high
---

# Agent Control Plane

## 定義

**AI Control Plane** = 治理 + 編排 + 觀測的統一層，位於 models 和 agents 之上。

> The AI control plane has emerged as that missing layer – a combination of inventory, policy engine, orchestration and observability that sits above models and agents, enforcing policies at the moment of action, recording what happened and enabling reversibility.
> — Mahmoud Abulfadda (LinkedIn)

## 市場背景（Activant 2026）

| 指標 | 數值 |
|------|------|
| 企業 AI 試點無 P&L 影響 | **95%** |
| Agent 專案未達生產 | **88%** |
| 公司經歷未授權 AI 動作 | **80%** |
| 平均企業 SaaS 數 | **300+** |
| 官方 AI 訂閱滲透率 | **40%** |
| 員工私下用 AI 工具比例 | **90%** |

**結論**：企業 AI 從「adopt」轉向「govern」階段。

## 4 大核心能力

### 1. Governance & Identity
- **Per-agent identity**：獨立 service accounts，least-privilege
- **Policy-as-code at runtime**：地理規則、PII 處理、模型選擇自動執行
- **Built-in redaction**：redaction 是 runtime 能力

### 2. Context & Tooling
- **Scoped, mortal memory**：agent 只記得該記的
- **Tools are contracts**：簽名、限速、approval-gated

### 3. Studio & Orchestration
- **Visual flows**：canvas 上組裝 multi-step workflows
- **Production-ready by default**：versioned + CI/CD

### 4. Evals & Economics
- **Evaluate before ship**：first-class eval loops
- **Telemetry for finance**：每個 call 可追溯、可 replay、可計價

## 類比 Apple iOS 生態系

| iOS | Agent Control Plane |
|-----|---------------------|
| Xcode | **Agent Studio**（建構工具）|
| App Store | **AI Marketplace**（預建應用）|
| App Review + iCloud | **Control Plane**（統一治理）|

## Hermes 對應評估

| Activant 概念 | Hermes 實作 | 狀態 |
|--------------|-------------|------|
| Per-agent identity | subagent + delegate_task | ⚠️ 需獨立 identity |
| Policy-as-code | RULES.md + E-code | ✅ |
| Built-in redaction | `_sanitize_error` | ✅ |
| Scoped mortal memory | `fact_store` | ✅ |
| Tools as contracts | MCP servers | ✅ |
| Visual flows | Dashboard WebUI | ⚠️ 無 canvas |
| Eval loops | E 階段御史 | ✅ |
| Telemetry for finance | logs | ⚠️ 未整合到計價 |
| Agent Studio | Skill 系統 | ✅ |
| AI Marketplace | 無 | ❌ |

## 對 Hermes 的啟示

### 短期可行（無需大改）

1. **為 subagent 加入 unique session id**（接近 per-agent identity）
2. **在 Dashboard 增加 Visual Workflow Canvas**（顯示 routing 流程）

### 長期願景

1. **整合 cost guardrails**（基於 token usage 自動 throttle）
2. **建立 Skills Marketplace**（社群可發布/共享 skills）

## 來源

- Activant Research：https://www.activantcapital.com/research/the-agent-control-plane/
- LinkedIn (Mahmoud Abulfadda)：https://www.linkedin.com/pulse/rise-ai-control-planes-governing-models-agents-scale-mahmoud-abufadda-d1f5f
- Forrester：「Agent Control Plane Market」evaluation
- Prefactor.tech：AI Agent Identity Audits Reporting Standards