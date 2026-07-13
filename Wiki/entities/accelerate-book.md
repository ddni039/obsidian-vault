---
title: Accelerate — The Science of Lean Software and DevOps
created: 2026-07-13
updated: 2026-07-13
uid: e-6aa035852eae
type: entity
tags: [book, accelerate, dora, devops, four-key-metrics, nicole-forsgren, jez-humble, gene-kim, continuous-delivery, shingo-award]
sources:
  - raw/articles/accelerate-book-2026-07-13.md
related:
  - "[[the-devops-handbook-book]]"
  - "[[dora-four-key-metrics]]"
  - "[[three-ways-devops]]"
confidence: high
---

# Accelerate — The Science of Lean Software and DevOps

## 簡介

**Accelerate** 是 DevOps 領域的量化研究原典，確定了 24 個關鍵能力（key capabilities）和 4 個關鍵指標，證明軟體交付效能與組織績效正相關。

> 核心發現：**效能（Throughput）和穩定性（Stability）同步移動**——沒有取捨。

**基本資訊**：

| 項目 | 內容 |
|------|------|
| **作者** | Nicole Forsgren, Jez Humble, Gene Kim |
| **出版** | IT Revolution Press, 2018-03-27 |
| **頁數** | 288 |
| **獎項** | Shingo Publication Award |
| **ISBN** | 9781942788331 |

## 研究規模

| 項目 | 數據 |
|------|------|
| **研究年份** | 2014-2017（4 年）|
| **調查問卷** | 23,000+ 份 |
| **組織數量** | 2,000+ 個 |

**適用範圍**：任何規模（<5人到>10k人）、綠地與棕地、任何產業

## 四個關鍵指標（Four Key Metrics）

| 指標 | 定義 | Elite 標準 | Hermes 評估 |
|------|------|-----------|------------|
| **Lead Time** | 從程式碼提交到生產環境運行的時間 | < 1 小時 | ✅ Elite |
| **Deployment Frequency** | 部署頻率 | On-demand | ✅ Elite |
| **Mean Time To Restore (MTTR)** | 生產故障後恢復時間 | < 1 小時 | ✅ Elite |
| **Change Fail Rate** | 導致服務中斷或故障的變更比例 | 0-15% | ✅ Elite |

## 24 個關鍵能力（5 大類）

### 1. Continuous Delivery（持續交付）
1. Test Automation
2. Deployment Automation
3. Trunk-Based Development
4. Shift Left on Security
5. Continuous Integration
6. Continuous Delivery
7. Version Control
8. Test Data Management

### 2. Architecture（架構）
9. Loosely Coupled Architecture
10. Empowered Teams

### 3. Product and Process（產品與流程）
11. Small Batches
12. Make Flow of Work Visible
13. Customer Feedback
14. Team Experimentation

### 4. Lean Management and Monitoring（精益管理與監控）
15. Limit Work in Progress
16. Production Monitoring
17. Visualizing Work
18. Lightweight Change Approval
19. Proactive Notifications

### 5. Cultural（文化）
20. Foster generative culture
21. Encourage learning
22. Collaboration amongst teams
23. Job Satisfaction
24. Support Transformational leadership

## Westrum 組織文化模型

| Pathological（病態）| Bureaucratic（官僚）| Generative（生成）|
|-----------------|-----------------|----------------|
| 權力導向 | 規則導向 | **績效導向** ✅ |
| 低合作 | 適度合作 | 高度合作 |
| messenger 被「射殺」| messenger 被忽視 | messenger 被培訓 |
| 失敗→責備 | 失敗→正義 | **失敗→探究** ✅ |
| 創新被扼殺 | 創新→問題 | 創新→實施 |

## Maturity Model vs Capability Model

| Maturity Model | Capability Model |
|---------------|------------------|
| 有固定目標 | **永遠可以改進** ✅ |
| 靜態級別 | **動態級別** ✅ |
| 虛榮指標 | **結果導向指標** ✅ |
| 關注過程合規 | **關注正確的能力** ✅ |

## 對 Hermes 的直接對應

| Accelerate 能力 | Hermes 對應 | 評估 |
|----------------|------------|------|
| Deployment Automation | Skill 維護 SOP | ✅ |
| Version Control | `~/.hermes/skills/` + git | ✅ |
| Test Automation | E 階段御史審計 | ✅ |
| Loosely Coupled | 核心檔模組化（SOUL/AGENTS/RULES/CODEX）| ✅ |
| Continuous Delivery | Skill 持續維護 SOP | ✅ |
| Trunk-Based Development | 核心檔即時更新 | ✅ |
| Production Monitoring | `errors.log` + token usage | ✅ |
| Limit WIP | `max_concurrent_children=3` | ✅ |
| Generative Culture | TRAP-SOP-010/011（No blame）| ✅ |
| Lean Management | Phase Gate 審計 | ✅ |
| Empowered Teams | subagent 自主决策 | ✅ |
| Customer Feedback | 用戶溝通偏好 | ✅ |

## 核心洞察

1. **Quality == Speed**：效能和穩定性同步移動，沒有取捨
2. **文化預測績效**：Westrum generative culture 預測更好的軟體交付
3. **先改變行為**：文化變革先從改變人的行為開始，而非先改變想法
4. **MTTR > MTBF**：恢復時間比無故障時間更重要（失敗是不可避免的）
5. **Tooling affects culture**：採用 DevOps 工具會改變文化

## 與 DevOps Handbook 的關係

- **Accelerate**（2018）= DORA 研究原典，量化證明 DevOps 有效
- **The DevOps Handbook**（2016）= DevOps 實踐指南，基於同樣研究
- **DevOps Handbook 3 Ways** = Accelerate 24 capabilities 的實作框架

Accelerate 是 DevOps Handbook 的**理論基礎**，DevOps Handbook 是 Accelerate 的**實作指南**。

## 引用

```bibtex
@book{forsgren2018accelerate,
  title={Accelerate: The Science of Lean Software and DevOps},
  author={Forsgren, Nicole and Humble, Jez and Kim, Gene},
  year={2018},
  publisher={IT Revolution Press},
  isbn={9781942788331},
  note={Shingo Publication Award Winner}
}
```

## 資源

- [IT Revolution — Accelerate](https://itrevolution.com/product/accelerate/)
- [Free Excerpt PDF](https://itrevolution.com/wp-content/uploads/2022/06/ACC_excerpt.pdf)
- [DORA Research](https://dora.dev/resources/)