---
title: 御史審計聖經 — OWASP Top 10 2025 + Secure-by-Design + Threat Modeling
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [audit, security, owasp, threat-modeling, secure-by-design, code-review, top-10, llm-security, supply-chain, yu-shi]
urls:
  - https://owasp.org/www-project-secure-by-design-framework/
  - https://owasp.org/www-community/Threat_Modeling
  - https://cycode.com/blog/the-2025-owasp-top-10-addressing-software-supply-chain-and-llm-risks-with-cycode/
license: Open source（OWASP CC BY-SA 4.0）+ CC sources
audience: Yu-shi (Auditor) profile — security review, threat modeling, quality assurance
---

# 御史審計聖經 — Source Material

> 整合 3 個**完全 open-source + 高權威**的審計/安全文獻：
> - **OWASP Top 10 2025**（最新）
> - **OWASP Secure-by-Design Framework**（v0.5.0, 2025-08）
> - **OWASP Threat Modeling**（官方 community page）
> 
> **無版權疑慮**（CC BY-SA + OWASP open-source）。
> 與既有 `references/agents-architecture-patterns.md` 中的「Yu-shi」角色對應。

## 與 Hermes 角色對應

```
Yu-shi（御史）= 審計者（Auditor）

5 大職責：
  1. Code Review（E 階段）
  2. Threat Modeling
  3. Quality Assurance（QA）
  4. Compliance Audit
  5. Postmortem (When E-code triggers)
```

## 書 1：OWASP Top 10 2025（最新版）

### 發布狀態

| 項目 | 內容 |
|------|------|
| **發布** | 2025 RC（Release Candidate）|
| **最新分析文** | 2026-03（Cycode 完整解讀）|
| **License** | CC BY-SA 4.0 |

### 2025 vs 之前版本的主要變化

| 趨勢 | 影響 |
|------|------|
| **從「單點漏洞」→「生態系統風險」** | 從 patch 漏洞到設計階段防禦 |
| **軟體供應鏈成核心** | A03 升級為核心關注 |
| **AI/LLM 威脅納入** | OWASP Top 10 for LLM Applications 一起使用 |
| **Insecure Design 新類別** | 早期設計階段就要處理 |

### 10 大類別（基於 Cycode 2025 解讀）

| ID | 類別 | 重點 | Hermes 對應 |
|----|------|------|-----------|
| **A01** | Broken Access Control | 權限檢查失敗 | TRAP-SOP-024（Skill <250 行含權限聲明）|
| **A02** | Cryptographic Failures | 加密失敗 | MCP auth/Secret SSOT |
| **A03** | **Software Supply Chain** | 依賴／組件風險 | 更新 dependency 風險評估 |
| **A04** | Insecure Design | 設計階段安全失敗 | **Secure-by-Design Framework** |
| **A05** | Security Misconfiguration | 配置錯誤 | MCP config 陷阱（TRAP-SOP-025~028）|
| **A06** | Vulnerable Components | 易受攻擊組件 | Skill version control |
| **A07** | Auth Failures | 認證失敗 | API Gateway auth |
| **A08** | Software & Data Integrity | 軟體與資料完整性 | checksum / signature |
| **A09** | Logging Failures | 記錄失敗 | audit log + E-code |
| **A10** | SSRF | Server-Side Request Forgery | 外部請求驗證 |

### 5 個 LLM 威脅（OWASP Top 10 for LLM Applications）

| ID | 類別 |
|----|------|
| LLM01 | Prompt Injection |
| LLM02 | Insecure Output Handling |
| LLM03 | Training Data Poisoning |
| LLM04 | Model DoS |
| LLM05 | Supply Chain（model）|

### 3 大高調供應鏈事件（教訓）

1. **Shai-Hulud Worm**（npm, 2025-09）：自複製蠕蟲，感染 500+ packages
2. **tj-actions Compromise**（GitHub Actions, 2025-03）：洩漏 23,000 repos secrets
3. **XZ Utils Backdoor**（2024-03）：多年布局的信任背叛案例

## 書 2：OWASP Secure-by-Design Framework（v0.5.0, 2025-08）

### 簡介

> **Secure-by-Design (SbD)** = 在 SDLC 的**設計階段**就把安全內建進去，而不是後來才補。

### 三大核心階段（SDLC 整合）

```
┌─ Planning ───────────────────┐
│  Security Requirements       │  ← OWASP ASVS 對應
│  Elicit + Map                │
└──────────────────────────────┘
               ↓
┌─ Design ────────────────────┐
│  SbD framework apply         │  ← ★ 重點
│  Principles + Patterns       │
│  Threat Modeling checkpoint  │
└──────────────────────────────┘
               ↓
┌─ Development ───────────────┐
│  Code follow ASVS           │
└──────────────────────────────┘
               ↓
┌─ Test ──────────────────────┐
│  Security verification       │
└──────────────────────────────┘
```

### SbD 與其他 OWASP 專案關係

| 階段 | OWASP 工具 |
|------|-----------|
| Planning | ASVS requirements mapping |
| **Design** | **SbD Framework** ★ |
| Development | ASVS |
| Test | Security verification |
| All phases | Threat Modeling（持續）|

### SbD 核心原則

1. **Least Privilege**：最小權限
2. **Defense in Depth**：縱深防禦
3. **Secure Defaults**：安全預設
4. **Fail Secure**：失敗時安全
5. **Complete Mediation**：完整中介
6. **Open Design**：開放設計
7. **Least Common Mechanism**：最少共用機制
8. **Psychological Acceptability**：心理可接受

### 5 大 SbD 重點領域

| 領域 | 內容 |
|------|------|
| Microservices 隔離 | service 邊界 + 信任模型 |
| Resilience Patterns | circuit breaker, bulkhead |
| Service-to-Service | mTLS, identity |
| Data Protection | encryption at rest/in transit |
| Observability | logging, metrics, tracing |

### 完整 SbD 檢核清單（節錄）

```yaml
sb_d_review_checklist:
  authentication:
    - [ ] MFA for sensitive ops
    - [ ] OAuth2/OIDC at edge
    - [ ] JWT validation at all services
  authorization:
    - [ ] Least privilege zones
    - [ ] Role-based access control
  data_protection:
    - [ ] Encryption at rest
    - [ ] mTLS in transit
    - [ ] No secrets in code
  resilience:
    - [ ] Circuit breakers
    - [ ] Graceful degradation
    - [ ] Health checks (3 levels)
```

## 書 3：OWASP Threat Modeling（官方 community page）

### 簡介

**Threat modeling** = 系統化識別威脅與緩解措施的過程。

> "A structured representation of all the information that affects the security of an application."

### 4 大問題框架

```
1. What are we working on?（在處理什麼）
2. What can go wrong?（會出什麼錯）
3. What are we going to do about it?（要怎麼處理）
4. Did we do a good job?（做得好不好）
```

### 主要方法

| 方法 | 適用 |
|------|------|
| **STRIDE** | Spoofing / Tampering / Repudiation / Information Disclosure / DoS / Elevation |
| **DREAD** | 風險評分（已較少使用）|
| **Attack Trees** | 攻擊樹分析 |
| **PASTA** | Process for Attack Simulation |

### 整合進 SDLC

| 階段 | 動作 |
|------|------|
| **Concept / Planning** | 高階威脅模型先建立 |
| **Refinement** | 隨細節逐步更新 |
| **新 feature release** | 重新評估 |
| **Security incident** | 反向 trace |
| **Architecture change** | 重新 threat model |

### 更新觸發條件

- 新功能釋出
- 安全事件發生
- 架構變更
- 基礎設施變更

## 對 Hermes「御史」（Yu-shi）的核心啟示

### Yu-shi role 是什麼？

> Yu-shi（御史）= Hermes 的審計代理，負責驗證工匠產出符合品質與安全標準。

### 適用 OWASP Top 10 哪些？

| OWASP Top 10 | Hermes 對應 |
|--------------|-----------|
| A01 Broken Access | Hermes Skill 權限與可訪問性 |
| A02 Cryptographic | MCP auth + Credential SSOT（已有）|
| A03 Supply Chain | Skill dependency 風險（待建立）|
| A04 Insecure Design | **SbD Framework 對應** |
| A05 Misconfig | **mcp-config-traps SOP（已有）**|
| A06 Vulnerable | Skill version control |
| A07 Auth Failures | API Gateway（待建立）|
| A08 Integrity | Skill checksum（待建立）|
| A09 Logging | **E-code + TRAP-SOP（已有）** |
| A10 SSRF | 外部請求驗證 |

### 適用 SbD Framework 哪些？

| SbD 原則 | Hermes 對應 |
|----------|-----------|
| Least Privilege | Skill 最小權限 |
| Defense in Depth | E 階段 + Decision Log + Physical Verification |
| Secure Defaults | Skill frontmatter 必填欄位 |
| Fail Secure | E-code 系統 |
| Complete Mediation | Plan 強制範本 |
| Open Design | 開源 Skill manifest |
| Least Common Mechanism | DI / decoupling |
| Psychological Acceptability | Plan 範本 v1.1.1 易用 |

### 適用 Threat Modeling 哪些？

| 步驟 | Hermes 對應 |
|------|-----------|
| 1. What are we working on | Plan YAML |
| 2. What can go wrong | Pre-mortem |
| 3. Mitigation | TRAP-SOP（54 個）|
| 4. Quality check | E-code audit + verify-before-redo |

## 4 大審計框架整合

```
PLAN (Yu-shi 審計對象)
   ↓
OWASP SbD（設計階段）
- 套用 Secure-by-Design 原則
- 參考 SbD Patterns Library
   ↓
OWASP Threat Modeling（風險識別）
- 4 問題框架
- STRIDE analysis
   ↓
OWASP Top 10 2025（合規檢核）
- A01-A10 對應 Hermes Skill
- LLM01-LLM05 對應 AI Agent
   ↓
Hermes TRAP-SOP 自動審計
- 54 個 TRAP（已建立）
- E-code 系統
   ↓
Audit Report
```

## 引用

```bibtex
@project{owasp2025secure_by_design,
  title={OWASP Secure by Design Framework},
  version={0.5.0},
  year={2025},
  month={Aug},
  publisher={OWASP Foundation},
  license={CC BY-SA 4.0}
}

@project{owasp2025top10,
  title={OWASP Top 10 2025},
  year={2025},
  publisher={OWASP Foundation},
  license={CC BY-SA 4.0}
}

@project{owasp_threat_modeling,
  title={OWASP Threat Modeling},
  author={Victoria Drake},
  publisher={OWASP Foundation},
  license={CC BY-SA 4.0}
}
```

## 資源

- [OWASP Secure-by-Design Framework](https://owasp.org/www-project-secure-by-design-framework/)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [OWASP Top 10 2025 第三方解讀](https://cycode.com/blog/the-2025-owasp-top-10-addressing-software-supply-chain-and-llm-risks-with-cycode/)
- [OWASP Top 10 LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## 對 Hermes TRAP-SOP 的擴展建議

| 新 TRAP | 主題 |
|---------|------|
| TRAP-SOP-077 | 審計未跑 OWASP SbD Checklist |
| TRAP-SOP-078 | Threat Modeling 跳過某一步 |
| TRAP-SOP-079 | 沒做 A01-A10 對應檢核 |
| TRAP-SOP-080 | 沒做 LLM Top 10 對應（AI 時代必備）|
