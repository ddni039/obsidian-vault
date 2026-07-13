---
title: OWASP Threat Modeling 四問框架
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, threat-modeling, owasp, stride, four-question-framework, audit, yu-shi, security]
sources:
  - raw/articles/yu-shi-audit-frameworks-2026-07-13.md
  - https://owasp.org/www-community/Threat_Modeling
confidence: high
---

# OWASP Threat Modeling 四問框架

## 定義

**OWASP Threat Modeling 四問框架** = 系統化識別威脅的 4 個問題。

```
1. What are we working on?（在處理什麼）
   ↓
2. What can go wrong?（會出什麼錯）
   ↓
3. What are we going to do about it?（要怎麼處理）
   ↓
4. Did we do a good job?（做得好不好）
```

**核心**：threat modeling 是**持續**過程，不是單次活動。

## 4 個階段詳細說明

### 1. What are we working on?（範疇評估）

```yaml
threat_model_scope:
  範圍: Skill SOUN_X_V1.1.1
  觸及範圍:
    - YAML frontmatter 格式
    - Plan 強制欄位
  不在範圍:
    - 內容設計細節
    - skill 內部邏輯
  假設:
    - 用戶會用 Hermes WebUI 訪問
    - Subagent 從 main agent 接收觸發
  不假設:
    - 用戶會直接修改 Skill
```

### 2. What can go wrong?（威脅識別）

常用方法：
- **STRIDE**：6 類威脅
- **DREAD**：風險評分（舊）
- **Attack Trees**：攻擊樹
- **Brainstorm**：腦力激盪

#### STRIDE 框架

| 代號 | 威脅類型 | 對應 |
|------|----------|------|
| **S**poofing | 偽裝身份 | A07 Authentication |
| **T**ampering | 篡改資料 | A01 Access Control |
| **R**epudiation | 拒絕承認 | A09 Logging |
| **I**nformation Disclosure | 資訊外洩 | A02 Crypto + A01 |
| **D**enial of Service | 拒絕服務 | LLM04 |
| **E**levation of Privilege | 提權 | A01 Access Control |

### 3. What are we going to do about it?（緩解方案）

| 策略 | 觸發 | 應用 |
|------|------|------|
| **Mitigate** | 高風險 | 加 controls |
| **Transfer** | 不是核心 | 委外 |
| **Accept** | 低風險 + 低影響 | 記錄 |
| **Eliminate** | 多餘功能 | 移除 |

### 4. Did we do a good job?（品質保證）

```yaml
quality_review:
  - 威脅模型更新時機？
  - 相關 stakeholders 都 review？
  - controls 真的有效？
  - 攻擊面變化追蹤？
  - 整合進 CI/CD security tests？
```

## 與 Hermes 對應

| STRIDE | Hermes 對應 | TRAP-SOP |
|--------|-------------|---------|
| Spoofing | MCP auth + gateway | TRAP-SOP-025~028 |
| Tampering | SOP 變更需要嚴格驗證 | TRAP-SOP-024 |
| Repudiation | E-code + audit log | 已有 |
| Info Disclosure | Credential SSOT | 已有 |
| DoS | MCP health + circuit breaker | TRAP-SOP-060 |
| Elevation | Plan 強制範本 | 已建立 |

## 4 大整合工具

| 工具 | 整合時機 |
|------|---------|
| **STRIDE** | Plan 階段識別 |
| **DREAD** | Post-mortem 評分 |
| **Attack Trees** | 設計 review |
| **PASTA** | 重大變更前 |

## 何時做 Threat Model

| 觸發 | 動作 |
|------|------|
| 新 feature release | 更新模型 |
| Security incident | 反向 trace |
| Architectural change | 重新評估 |
| Infrastructure 變更 | 重新評估 |
| Plan 階段（每次） | STRIDE 簡化版 |

## 與 Pre-mortem 的整合

```
Pre-mortem（5 步）：
  1. 想失敗
  2. 5 個失敗模式
  3. 早期信號
  4. 預防設計
  5. retry

STRIDE 對 Pre-mortem 5 個失敗模式分類：
  S → Spoofing 失敗模式
  T → Tampering 失敗模式
  R → Repudiation 失敗模式
  I → Info Disclosure 失敗模式
  D → DoS 失敗模式
  E → Elevation 失敗模式
```

## 何時不適用

| 不適用情境 | 替代方案 |
|----------|---------|
| 簡單 Skill 維護 | 跳過威脅模型 |
| 緊急 bug fix | 暫時不通過 SbD |
| 學習用 skill | 跳過 compliance |

## 引用

- OWASP Threat Modeling: https://owasp.org/www-community/Threat_Modeling
- Threat Modeling Manifesto: https://www.threatmodelingmanifesto.org/

## 相關 SOP

- `references/yu-shi-audit-sop.md`（御史 SOP）
- TRAP-SOP-024~024（Skill 結構）

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（OWASP 4 問框架 + STRIDE 整合）|