---
title: DORA State of DevOps Report 2024
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [dora, google-cloud, devops, research, metrics, 2024, ai]
url: https://dora.dev/research/2024/dora-report/
date: 2026-04-13（最近更新）
publisher: Google Cloud / DORA Team
researchers:
  - Dr. Nicole Forsgren (DORA)
  - 聯合多家 industry sponsors（Catchpoint, Datadog, Deloitte 等）
---

# DORA 2024 報告 — Source Material

## 關於 DORA

**DORA**（DevOps Research and Assessment）= Google Cloud 旗下研究團隊，每年發布 State of DevOps Report，是業界最權威的 DevOps 量化研究。

## 4 大關鍵指標（DORA Four Key Metrics）

| 指標 | 定義 | 計算 | Elite performers |
|------|------|------|-----------------|
| **Deployment Frequency** | 部署頻率 | 單位時間的部署次數 | On-demand（多次/天）|
| **Lead Time for Changes** | 變更前置時間 | 從 commit 到 production 運行 | < 1 小時 |
| **Change Failure Rate** | 變更失敗率 | 失敗部署 / 總部署 | 0-15% |
| **Failed Deployment Recovery Time** | 失敗恢復時間 | 從失敗到恢復 | < 1 小時 |

**重要性**：這 4 個指標已成為業界軟體交付效能的「業界標準」（從 2013 年起）。

## 2024 報告核心發現

### 1. AI 雙刃劍
- ✅ **正面**：AI 顯著提升個人生產力、flow、工作滿意度
- ❌ **負面**：AI 對**軟體交付穩定性和吞吐量**有負面影響
- **教訓**：Small batch sizes、robust testing 等**基礎**仍關鍵

### 2. User-centricity 終極驅動
- 重視 end-user experience 的組織 → 更高品質產品
- 開發者以 user-centric 思維工作 → 更有生產力、更滿意、burnout 較低

### 3. 穩定優先級
- 組織優先級**不穩定**→ 生產力下降、burnout 大增
- 此負面影響**難以緩解**（即使有強領導 + 高品質文檔）
- **教訓**：寧可減少功能也要保護優先級穩定

### 4. Platform Engineering 取捨
- 內部 developer platform → 提升個人生產力、團隊效能
- 但可能**降低 change stability 和 throughput**
- 需要專注於 developer independence

### 5. Transformational Leadership
- 激勵、智識刺激、支持團隊的領導者 → 顯著提升：
  - 員工生產力
  - 組織效能
  - 工作滿意度
- 同時**降低 burnout**

### 6. Infrastructure Flexibility
- 靈活雲基礎設施 → 直接提升組織效能
- 僅僅 migrate 雲而不採用其彈性 → 可能**比傳統機房更糟**

## 對 Hermes 的對應

| DORA 指標 | Hermes 對應 | 評估 |
|----------|------------|------|
| **Deployment Frequency** | 24 輪並聯拆分 Skill = 100+ ops/天 | ✅ Elite |
| **Lead Time for Changes** | 並聯 = ~10x faster（vs 序列 3 小時 → 24 分鐘）| ✅ Elite |
| **Change Failure Rate** | 21 個 TRAP-SOP + E-code 系統把關 | ✅ Low |
| **Recovery Time** | `touch config.yaml` + gateway 重啟 = ~30 秒 | ✅ Elite |

## DORA 4 能力 vs Hermes

DORA 將高效能組織的特質分為**連續能力**（Continous Capabilities）：

1. **Continuous Integration** ✅ — Hermes 用 Claude Code 做 subagent CI
2. **Continuous Delivery** ✅ — 並聯 SOP 即「continuous delivery」實踐
3. **Continuous Testing** ⚠️ — `physical-verification.md` 提供手動驗證
4. **Continuous Monitoring** ✅ — `~/.hermes/logs/` 全日誌
5. **Database Change Management** ❌ — Hermes 無 DB 變更 SOP（gavin-only skill）
6. **Continuous Security** ⚠️ — MCP 修補（realpath shim）但缺專門 SOP
7. **Test Data Management** ❌ — 無
8. **Trunk-based Development** ✅ — Hermes git workflow
9. **Working in Small Batches** ✅ — 24 輪每輪 3 顆 Skill = 小批量
10. **Loosely Coupled Architecture** ✅ — 三層職責邊界
11. **Empowering Teams to Choose Tools** ✅ — 工具中立的 subagent 設計

**對應評估**：11 個 DORA 能力中 Hermes 已對應 7 個（64%），部分對應 2 個，缺失 2 個。

## 與 METR 2025 RCT 的對比

DORA 2024 報告（自我報告 + survey）vs METR 2025 RCT（客觀測量）：

| 面向 | DORA 2024 | METR 2025 RCT |
|------|---------|------------|
| 方法 | Survey + 統計分析 | RCT（控制變數）|
| AI 對生產力 | 提升 | 慢 19%（資深開發者）|
| 指標類型 | Self-report | 客觀時間測量 |
| 樣本 | 業界調查 | 16 位資深開發者 |
| 結論傾向 | 樂觀 | 謹慎 |

**結合使用**：DORA 給**方向**（哪些能力有用），METR 給**量化**（AI 真的快了嗎）。

## 對 Hermes 的核心啟示

### 立即可行

| 啟示 | 行動 |
|------|------|
| **AI 降低 stability** | 為 MCP minimax 連線加 retry + circuit breaker |
| **User-centric** | Dashboard 加「用戶體驗」指標（API 成功率）|
| **Stable priorities** | 保持 SOP 系統結構穩定，避免大幅重構 |
| **Transformational leadership** | E 階段審計 = Hermes 的「領導力」 |

### 待優化

| 項目 | 建議 |
|------|------|
| Test Data Management | 為 gbrain 測試加 fixture SOP |
| Database Change Management | 為 ChromaDB 結構變更加 SOP |
| Continuous Security | 加 TRAP-SOP-042（Secret leak in config）|

## 引用

```bibtex
@techreport{dora2024,
  title={Accelerate State of DevOps Report 2024},
  author={{DORA Team} and {Google Cloud}},
  year={2024},
  url={https://dora.dev/research/2024/dora-report/}
}
```