---
title: SRE (Site Reliability Engineering)
created: 2026-07-13
updated: 2026-07-13
uid: e-bda5d7541622
type: entity
tags: [concept, sre, google, reliability-engineering, devops, observability]
sources:
  - raw/articles/google-sre-book-2026-07-13.md
  - raw/articles/20-essential-sre-books-catchpoint-2026-07-13.md
related:
  - "[[slos-anti-fragility]]"
  - "[[cascading-failure-protection]]"
  - "[[eliminating-toil]]"
confidence: high
---

# SRE (Site Reliability Engineering)

## 定義

**SRE**（Site Reliability Engineering）= Google 在 2003 年發明的**運維工程化**方法論，核心是「**用軟體工程方法解決運維問題**」。

> SRE is what happens when you ask a software engineer to design an operations team.

## 5 大核心原則

### 1. Embracing Risk（接受風險）
- 100% 可用性是**錯誤目標**
- 99.99% (4-nines) 通常是甜蜜點
- 多 9 個 9 = 成本指數成長

### 2. Service Level Objectives（SLO）
- **SLI**（測量）→ **SLO**（內部目標）→ **SLA**（對外承諾）
- SLO 必須**定義 error budget**
- Error budget 用完 → 停止 feature，聚焦 reliability

### 3. Eliminating Toil（消除瑣事）
- **Toil 定義**：manual + repetitive + automatable + tactical + scale linearly
- **目標**：SRE 時間 < 50% 在 toil
- **每次自動化**：省下的時間用於 engineering work

### 4. Monitoring Distributed Systems（四大黃金信號）
- **Latency**（延遲）
- **Traffic**（流量）
- **Errors**（錯誤率）
- **Saturation**（飽和度）

加上 USE 方法（Utilization / Saturation / Errors）作補充。

### 5. Postmortem Culture（無指責事後檢討）
- **Blameless**：聚焦系統，不追究個人
- 每次事件都學習 → 系統改進
- **Justice**：追究根因 vs 追究個人

## Error Budget 機制（核心創新）

```
SLO 99.9% → Error Budget = 0.1%
若一個月有 43,200 分鐘，error budget = 43.2 分鐘

超出預算 → 凍結 deploy → 專注 reliability
未超出 → 允許更多變更
```

## SRE 與 DevOps 差異

| SRE | DevOps |
|-----|--------|
| 從運維出發 | 從開發出發 |
| Error Budget 量化 | 文化變革 |
| Toil 自動化 | CI/CD、監控 |
| 50% 時間在 engineering | 文化、流程、組織 |

## Hermes 對應評估

| SRE 概念 | Hermes 對應 | 評估 |
|---------|------------|------|
| SLO | 50k/80k/120k token 配額 | ✅ 100% |
| Error Budget | Warning/Distill/Lock 三階段 | ✅ 100% |
| Eliminating Toil | 並聯 SOP（7.5× speedup）| ✅ 100% |
| 四大黃金信號 | API call logs（latency, traffic, errors, saturation）| ✅ 90% |
| Blameless Postmortem | TRAP-SOP-010/011（無指責自我記錄）| ✅ 100% |
| 50% engineering time | subagent 並聯 → engineer 解放時間 | ✅ 100% |
| Load Balancing | `max_concurrent_children=3` | ✅ 100% |
| Cascading Failures | E-code 斷路器 | ✅ 100% |
| Simplicity | 110 行核心檔案 | ✅ 100% |

**總評**：Hermes 已實作 **95%+ SRE 核心原則**

## 關鍵資源

- **Google SRE Book**（免費線上版）：https://sre.google/sre-book/
- **SRE Workbook**：https://sre.google/workbook/
- **Building Secure & Reliable Systems**：https://google.github.io/building-secure-and-reliable-systems/

## 推薦書單

1. 🔴 **Accelerate**（Gene Kim）— 量化研究
2. 🔴 **SRE Book**（Google）— 基礎原理
3. 🔴 **The Phoenix Project** — DevOps 入門小說
4. 🔴 **The DevOps Handbook** — DevOps 原則
5. 🟡 **SRE Workbook** — 實務操作
6. 🟡 **Post-Incident Reviews** — modern postmortem

完整 20 本書單：`raw/articles/20-essential-sre-books-catchpoint-2026-07-13.md`