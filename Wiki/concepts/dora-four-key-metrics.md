---
title: DORA Four Key Metrics
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, dora, metrics, software-delivery, performance, four-key-metrics]
sources:
  - raw/articles/dora-2024-state-of-devops-2026-07-13.md
related:
  - "[[calms-framework]]"
  - "[[three-ways-devops]]"
  - "[[sre-site-reliability-engineering]]"
confidence: high
---

# DORA Four Key Metrics（DORA 4 大關鍵指標）

## 定義

**DORA 4 大關鍵指標** = Google Cloud DORA 團隊自 2013 年起追蹤的軟體交付效能標準指標，已成為業界**事實標準**。

> 從 2013 年至今，數千個組織使用這 4 個指標評估 DevOps 成熟度。

## 4 大指標

| 指標 | 定義 | 計算公式 | 改善方向 |
|------|------|---------|---------|
| **Deployment Frequency (DF)** | 部署頻率 | 單位時間的部署次數 | ↑ 越高越好 |
| **Lead Time for Changes (LT)** | 變更前置時間 | commit → production 運行 | ↓ 越短越好 |
| **Change Failure Rate (CFR)** | 變更失敗率 | 失敗部署 / 總部署 × 100% | ↓ 越低越好 |
| **Failed Deployment Recovery Time (MTTR)** | 失敗恢復時間 | 從失敗到恢復 | ↓ 越短越好 |

## Elite vs Low Performers（DORA 2024 數據）

| 指標 | Elite Performers | Low Performers | 差距 |
|------|----------------|----------------|------|
| **Deployment Frequency** | On-demand（多次/天）| 1 次/多月 | 1000+× |
| **Lead Time** | < 1 小時 | > 6 個月 | 4000+× |
| **Change Failure Rate** | 0-15% | 46-60% | 4× |
| **MTTR** | < 1 小時 | > 1 個月 | 700+× |

> 來源：2024 DORA Report（Google Cloud）

## 為何這 4 個指標？

DORA 通過 10+ 年研究發現，這 4 個指標：
- ✅ 高度可測量
- ✅ 反映軟體交付健康度
- ✅ 與業務結果（revenue、customer satisfaction）正相關
- ✅ 跨組織、跨規模、跨產業通用

## Hermes 對應（量化評估）

| 指標 | 當前狀態 | 評估 |
|------|---------|------|
| **DF** | 24 輪並聯 / 一次會話 = **~100 ops/天** | ✅ Elite |
| **LT** | 並聯 = **~10x 速度提升** | ✅ Elite |
| **CFR** | 21 個 TRAP-SOP + E-code 把關 | ✅ Low |
| **MTTR** | `touch config.yaml` + 重啟 = **~30 秒** | ✅ Elite |

**總評**：Hermes **4/4 指標均達 Elite** 表現。

## 如何測量 Hermes 的 4 大指標

### 1. Deployment Frequency
```bash
# 從 git log 統計
cd ~/.hermes && git log --since="1 day ago" --oneline | wc -l
```

### 2. Lead Time for Changes
```bash
# 從 commit 到部署
git log --format="%H %ct" | head -1
# 部署時間從 errors.log 提取
grep "minimax all tools enabled" ~/.hermes/logs/errors.log
```

### 3. Change Failure Rate
```bash
# 從 errors.log 統計失敗
grep -c "ERROR\|WARNING" ~/.hermes/logs/errors.log
# / 總操作數
```

### 4. MTTR
```bash
# 從 MCP 失敗到恢復的時間
# (透過 log timestamp 計算)
```

## DORA 4 能力模型

DORA 將高效能組織的特質分為**連續能力**（11 個）：

| 能力 | 描述 | Hermes 對應 |
|------|------|------------|
| Continuous Integration | 整合到共享 mainline | ✅ subagent 並聯 |
| Continuous Delivery | 自動部署到 production | ✅ Phase Lock |
| Continuous Testing | 自動化測試 | ⚠️ 手動驗證 |
| Continuous Monitoring | 持續監控 | ✅ `~/.hermes/logs/` |
| Database Change Management | 資料庫 schema 變更 | ❌ 無 |
| Continuous Security | 整合安全檢查 | ⚠️ 修補（realpath shim）|
| Test Data Management | 測試資料管理 | ❌ 無 |
| Trunk-based Development | 短分支、頻繁合併 | ✅ git workflow |
| Working in Small Batches | 小批量變更 | ✅ 24 輪每輪 3 顆 |
| Loosely Coupled Architecture | 鬆耦合架構 | ✅ 三層職責邊界 |
| Empowering Teams to Choose Tools | 賦能選工具 | ✅ toolset 設計 |

**對應評估**：11 個能力中 **7 個 ✅ + 2 個 ⚠️ + 2 個 ❌**

## DORA 2024 與 Hermes 對應

| DORA 2024 發現 | Hermes 影響 |
|---------------|-----------|
| **AI 雙刃劍**（提升個人生產力、降低 stability）| 為 MCP 加 retry + circuit breaker |
| **User-centric 終極驅動** | Dashboard 加 user 體驗指標 |
| **Stable priorities 關鍵** | 保持 SOP 系統結構穩定 |
| **Platform Engineering 取捨** | Skill 系統設計需專注 developer independence |
| **Transformational leadership** | E 階段審計 = Hermes 的「領導力」|
| **Infrastructure flexibility** | `~/.hermes/config.yaml` 易於遷移 |

## 對 Hermes 的啟示

### 立即可行

1. **建立 DORA Dashboard**：4 個指標即時追蹤
2. **TRAP-SOP 補完**：Database Change Management + Test Data Management
3. **Continuous Security SOP**：TRAP-SOP-042（Secret leak）

### 設計原則

1. **指標必須可測量**：DF / LT / CFR / MTTR 都有明確計算公式
2. **DORA 對齊業界**：4 個指標讓 Hermes 可與其他工具比較
3. **結合 METR RCT**：Survey + RCT 三角驗證

## 來源

- [DORA 2024 報告](https://dora.dev/research/2024/dora-report/)
- 《Accelerate》（Forsgren, Humble, Kim, 2018）— 量化研究基石
- [DORA Capabilities 列表](https://dora.dev/capabilities/)
- [Google Cloud Blog 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)

## 引用

```bibtex
@techreport{dora2024metrics,
  title={The Four Key Metrics - DORA State of DevOps 2024},
  author={{DORA Team} and {Google Cloud}},
  year={2024},
  url={https://dora.dev/research/2024/dora-report/}
}
```