---
title: CALMS Framework
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, devops, calms-framework, damon-edwards, transformation]
sources:
  - raw/articles/the-devops-handbook-2026-07-13.md
related:
  - "[[three-ways-devops]]"
  - "[[dora-four-key-metrics]]"
confidence: high
---

# CALMS Framework

## 定義

**CALMS** = DevOps 轉型的 5 大支柱，由 **Damon Edwards** 推廣（DORA 共同創辦人之一），後被收錄進《The DevOps Handbook》附錄。

> **C**ulture、**A**utomation、**L**ean、**M**easurement、**S**haring

## 5 大支柱

| 字母 | 領域 | 核心問題 | 實踐 |
|------|------|---------|------|
| **C** | Culture | 如何打破 Dev 與 Ops 壁壘？ | 共用 KPI、No blame、Blameless postmortem |
| **A** | Automation | 如何減少手動錯誤？ | CI/CD、IaC、Self-service tools |
| **L** | Lean | 如何消除浪費？ | Value stream mapping、Small batch、消除等待 |
| **M** | Measurement | 如何量化交付效能？ | DORA 4 metrics、SLI/SLO |
| **S** | Sharing | 如何跨團隊傳播知識？ | Internal Open Source、Tech radar、ChatOps |

## 為何需要 CALMS？

DORA 4 metrics 是**結果指標**（What's measured），CALMS 是**驅動因素**（What drives improvement）。

```
CALMS（Cultural + Automation + Lean + Measurement + Sharing）
  ↓
驅動 DORA 4 metrics 改善
  ↓
  - Deployment Frequency ↑
  - Lead Time ↓
  - Change Failure Rate ↓
  - Recovery Time ↓
```

## 對 Hermes 的對應評估

| CALMS | Hermes 對應 | 評估 |
|-------|------------|------|
| **C**ulture | 三層職責邊界（TRAP-SOP-021）+ SOUL/AGENTS 治理 | ✅ 90% |
| **A**utomation | 並聯 SOP（24 輪 7.5× speedup）+ 自動掃描腳本 | ✅ 95% |
| **L**ean | 110 行核心檔案 + 71 顆 <250 行 Skill（消除冗餘）| ✅ 90% |
| **M**easurement | E-code 系統 + token 監控（50k/80k/120k）+ audit log | ✅ 85% |
| **S**haring | `~/.hermes/skills/` 共用 + Wiki 攝入 + Plugin 系統 | ✅ 90% |

**總評**：Hermes 已實作 **90%** CALMS 框架

## CALMS vs 三大路徑

| 框架 | 視角 | 用途 |
|------|------|------|
| **The Three Ways** | 哲學（為什麼）| 組織設計原則 |
| **CALMS** | 實踐（怎麼做）| DevOps 轉型檢核 |
| **DORA 4 Metrics** | 量化（測量什麼）| 效能評估 |

三者互補：The Three Ways → CALMS → DORA Metrics

## 對 Hermes 的啟示

### 立即可行

| 啟示 | 行動 |
|------|------|
| **Culture 強化** | 在 SOUL.md 加入 CALMS 對應條目 |
| **Automation 評估** | 為每個手動 SOP 計算「Toil 預算」（<50%）|
| **Measurement 擴展** | Dashboard 顯示 DORA 4 metrics 趨勢 |
| **Sharing 優化** | Wiki 攝入 SOP → 跨專案共用 |

### 設計原則

1. **從 Culture 開始**：DevOps 轉型 80% 是文化、20% 是技術
2. **Automation 必須優先於 Toil**：toil > 50% 立即自動化
3. **Measure 對齊 DORA**：4 個關鍵指標 + 1 個 Health
4. **Share 跨團隊**：internal open source + 公開 wiki

## 來源

- Damon Edwards（DevOps Enterprise Summit 創辦人）
- Jez Humble et al.，《The DevOps Handbook》附錄
- https://www.sonatype.com/blog/principle-based-devops-frameworks-calms

## 變體：CALDER / CARDS

業界也有其他變體：
- **CALDER** = CALMS + **R**isk
- **CARDS** = **C**ulture、**A**utomation、**R**isk、**D**ata、**S**ecurity

核心 5 大支柱不變，差異在附加維度。