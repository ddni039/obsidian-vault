---
title: The Three Ways (DevOps)
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, devops, three-ways, gene-kim, principles]
sources:
  - raw/articles/the-devops-handbook-2026-07-13.md
related:
  - "[[calms-framework]]"
  - "[[dora-four-key-metrics]]"
confidence: high
---

# The Three Ways（DevOps 三大原則）

## 起源

**The Three Ways** 是 Gene Kim 在《The DevOps Handbook》《The Phoenix Project》中闡述的 DevOps 核心哲學框架，源自 Toyota Production System 和 Lean。

> DevOps 的三大原則：Flow、Feedback、Continual Learning。

## 第一路：Flow（左→右）

**核心**：優化工作從 **Dev → Ops → Customer** 的流動。

**目標**：
- 縮短 Lead Time
- 增加 Deployment Frequency
- 減少 Batch Size（小批量）

**實踐**：
- Continuous Integration / Delivery
- 自動化測試
- 低風險發布
- 部署流水線
- 架構決策支援頻繁發布

## 第二路：Feedback（右→左）

**核心**：建立**快速回饋機制**，讓問題早期發現、迅速修復。

**目標**：
- 縮短 MTTR（Mean Time to Recovery）
- 及早發現問題（測試 → staging → production）
- 開發者親身體驗生產環境

**實踐**：
- 遙測與監控
- ChatOps
- A/B Testing
- Feature Flags
- Blameless postmortem

## 第三路：Continual Learning

**核心**：建立**持續學習和實驗的文化**。

**目標**：
- 從失敗中學習（不責備）
- 將局部發現轉化為全局改進
- 預留創新時間

**實踐**：
- Blameless postmortem
- Game Days（chaos engineering）
- 20% 創新時間
- 知識分享會
- 內部開源文化

## 對 Hermes 的對應

| Three Ways | Hermes 對應 |
|------------|------------|
| **Flow** | `delegate_task` 並聯 + 24 輪拆分 Skill + `max_concurrent_children=3` |
| **Feedback** | E 階段審計（`auditor_core.py`）+ E-code 斷路器 + 物理驗證 |
| **Continual Learning** | 21 個 TRAP-SOP + SOP 系統演進（v1.5 → v2.4）+ Wiki 攝入 |

## 與 SRE 的對應

| Three Ways | SRE 對應 |
|------------|---------|
| Flow | SLO（服務等級目標）+ Deployment Pipeline |
| Feedback | Postmortem + Monitoring（四大黃金信號）|
| Continual Learning | Eliminating Toil + Error Budget |

DevOps 三大原則提供**哲學框架**，SRE 提供**量化實踐**。

## 實戰檢驗清單

### Flow
- [ ] CI/CD pipeline 完整
- [ ] 自動化測試覆蓋率 > 80%
- [ ] 平均 Lead Time < 1 天
- [ ] Deployment Frequency > 1/天

### Feedback
- [ ] 4 大黃金信號監控（Latency/Traffic/Errors/Saturation）
- [ ] Blameless postmortem 流程
- [ ] ChatOps（issue → Slack 整合）
- [ ] Feature flags 機制

### Continual Learning
- [ ] 例行 postmortem → action items
- [ ] Knowledge sharing sessions
- [ ] Game Days 定期演練
- [ ] 創新時間（員工可花 10-20% 時間探索）

## 來源

- The DevOps Handbook, Part I（Ch 1-4）
- The Phoenix Project（Gene Kim 2013）— 三大原則首次在小說中提出
- Toyota Production System 啟發

## 引用

```bibtex
@book{kim2016threeways,
  title={The Three Ways: The Principles Underpinning DevOps},
  author={Kim, Gene and Humble, Jez and Debois, Patrick and Willis, John},
  booktitle={The DevOps Handbook},
  year={2016}
}
```