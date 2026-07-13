---
title: SLO + Error Budget
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, sre, slo, error-budget, reliability, observability]
sources:
  - raw/articles/google-sre-book-2026-07-13.md
related:
  - "[[sre-site-reliability-engineering]]"
  - "[[eliminating-toil]]"
confidence: high
---

# SLO + Error Budget

## 三層指標體系

| 指標 | 定義 | 誰設定 | 衡量對象 |
|------|------|--------|---------|
| **SLI** | Service Level Indicator（量化測量）| 工程團隊 | 客觀測量 |
| **SLO** | Service Level Objective（內部目標）| 工程團隊 | 內部承諾 |
| **SLA** | Service Level Agreement（對外契約）| 業務 + 法務 | 對客戶承諾 |

**關鍵洞察**：**SLO 必須比 SLA 更嚴格**，因為 SLA 是底線（違反需賠償），SLO 是目標（達成才能保持可靠性）。

## Error Budget 機制

```
可用率 99.9% → Error Budget = 0.1%
一個月（43,200 分鐘）→ Budget = 43.2 分鐘

超出 → 凍結 deploy，focus reliability
未超出 → 允許更多 feature 變更
```

### 預算分配建議

| SLO | 月允許 downtime | 用途 |
|-----|----------------|------|
| 99.0% | 7.2 小時 | 內部工具 |
| 99.9% | 43 分鐘 | 一般 API |
| 99.95% | 22 分鐘 | 高頻服務 |
| 99.99% | 4.3 分鐘 | 關鍵基礎設施 |
| 99.999% | 26 秒 | 電信級 |

## SLO 設計 4 大原則

### 1. 從用戶角度定義
- 不要用「CPU < 80%」（內部指標）
- 要用「API 回應 < 200ms（p99）」（用戶體驗）

### 2. 少即是多
- 1-3 個關鍵 SLI > 20 個無用指標
- Google SRE Book 建議：每服務 **3-5 個** SLI

### 3. SLI 公式
```
SLI = (成功請求數) / (總請求數)

例：
HTTP API 成功率 = 2xx 數 / 總數
延遲 SLI = <SLO 閾值 的請求 / 總請求
```

### 4. Error Budget 必須消耗
> SLO 訂了不用 = 白訂

- **剩餘很多** → 可加速 feature release
- **快用完** → 減緩 deploy，優先 reliability

## Hermes 對應

| Hermes 機制 | SLO 對應 |
|------------|---------|
| 50k token → **Warning** | 內部 SLO 提醒 |
| 80k token → **Distill** | 達到 SLO 閾值，需行動 |
| 120k token → **Lock** | 超出 error budget，凍結 |
| `E-SUBAGENT-CONTEXT-BLOATED` | SLO 違規的 E-code 通知 |

### SLO 設計（建議）

| SLI | SLO | 對應 Hermes |
|-----|-----|-------------|
| 對話完成率 | > 95% | `fact_store` 持久化率 |
| API 回應時間 | < 30s（p95）| agent.conversation_loop 延遲 |
| Error rate | < 5% | errors.log MCP errors |
| Token 使用率 | < 80k（distill 閾值）| context_window 監控 |

## 與 Alerting 整合

> White-box monitoring（白盒）+ Black-box monitoring（黑盒）+ Page-on-burn-rate

**Burn rate**：error budget 消耗速度
- 慢燒（slow burn）：2% 在 30 天內用完
- 快燒（fast burn）：50% 在 1 小時內用完

**告警策略**：
- 慢燒 → email（給 SRE 團隊）
- 快燒 → page（即時通知 on-call）

## 對 Hermes 的啟示

### 立即可行

| 啟示 | 建議 |
|------|------|
| 量化 SLO | 為各 skill 定義 SLI（觸發成功率、平均耗時）|
| 自動 alert | Dashboard 顯示 token 用量趨勢 |
| Error budget 整合 | 連續 3 次 > 80k 觸發「slow burn」警告 |

### 設計原則

1. **少即是多**：3-5 個關鍵 SLI > 20 個無用指標
2. **從用戶出發**：不要追蹤內部 CPU，追蹤 API p99 延遲
3. **Error budget 必須消耗**：否則 SLO = 紙上談兵
4. **白盒 + 黑盒**：內部 metrics + 模擬用戶請求

## 來源

- Google SRE Book Ch. 4: Service Level Objectives
- Accelerate（Gene Kim et al.）— 量化研究
- [SRE Workbook Ch. 3](https://sre.google/workbook/table-of-contents/)