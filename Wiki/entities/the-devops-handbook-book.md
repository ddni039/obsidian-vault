---
title: The DevOps Handbook (Book)
created: 2026-07-13
updated: 2026-07-13
uid: e-db6165bb6fca
type: entity
tags: [book, devops, three-ways, calms, dora, gene-kim, jez-humble, patrick-debois, john-willis, it-revolution]
sources:
  - raw/articles/the-devops-handbook-2026-07-13.md
related:
  - "[[three-ways-devops]]"
  - "[[calms-framework]]"
  - "[[dora-four-key-metrics]]"
  - "[[the-phoenix-project]]"
confidence: high
---

# The DevOps Handbook (Book)

## 簡介

**The DevOps Handbook**（2016）= DevOps 界的**操作手冊聖經**，由 4 位 DevOps 創始人合著。

> 與《The Phoenix Project》小說體不同，本書是**操作指南**。

**規格**：
- 23 章 + 6 部
- 4 位作者（Gene Kim、Jez Humble、Patrick Debois、John Willis）
- IT Revolution Press 出版
- ISBN 978-1942788003
- O'Reilly 線上版免費閱讀

## 與《The Phoenix Project》關係

| Phoenix Project (2013) | DevOps Handbook (2016) |
|----------------------|------------------------|
| **小說體** | **操作手冊** |
| 引人入勝 | 實踐指南 |
| 講「為什麼」| 講「怎麼做」|
| 入門 | 進階 |
| 1 本 | 1 本 + 2 續作（Workbook、BSRS）|

**建議閱讀順序**：Phoenix Project → DevOps Handbook → SRE Book

## 4 位作者群

| 作者 | 角色 | 代表作 |
|------|------|--------|
| **Gene Kim** | IT Revolution 創辦人 | The Phoenix Project |
| **Jez Humble** | Continuous Delivery 合著者 | Lean Enterprise |
| **Patrick Debois** | DevOpsDays 創辦人（共同發明「DevOps」一詞）| Agile Infrastructure |
| **John Willis** | Docker 傳教士、55 年 IT 經驗 | The Visible Ops Handbook |

## 3 大部 + 23 章

### Part I - The Three Ways
- Ch 1: Agile, Continuous Delivery, and the Three Ways
- Ch 2: The First Way - Flow
- Ch 3: The Second Way - Feedback
- Ch 4: The Third Way - Continual Learning

### Part II - Where to Start
- Ch 5-8: 選擇 Value Stream、可視化、Conway's Law、整合 Ops

### Part III - The First Way: Flow Practices
- Ch 9-13: Deployment Pipeline、Automated Testing、CI、Low-Risk Releases

### Part IV - The Second Way: Feedback Practices
- Ch 14-18: Telemetry、Analyze、ChatOps、A/B Testing、Review Process

### Part V - The Third Way: Learning Practices
- Ch 19-21: Learning into Daily Work、Local → Global、Organizational Learning

### Part VI - InfoSec + Change Management
- Ch 22-23: Information Security for Everyone、Pipeline Protection

## 3 Ways 核心（Part I）

### The First Way: Flow
- CI/CD 流水線
- 自動化測試
- 小批量
- 低風險發布

### The Second Way: Feedback
- 遙測 + 監控
- ChatOps
- Feature flags
- A/B Testing
- **Blameless postmortem**

### The Third Way: Continual Learning
- 從失敗學習（No blame）
- 局部 → 全局 改進
- 預留創新時間
- 內部開源文化

## 與業界其他框架的關係

| 框架 | 關係 |
|------|------|
| **The Three Ways** | 本書的哲學核心 |
| **CALMS** | 附錄推薦的 5 支柱 |
| **DORA 4 metrics** | 量化延伸（Forsgren 合著 Accelerate）|
| **SRE Book** | 補完工程實踐 |
| **Lean / Toyota Production System** | 本書的源頭 |

## 與 Hermes 的對應

| 書中概念 | Hermes 對應 |
|---------|------------|
| The Three Ways - Flow | 並聯 SOP（24 輪 7.5× speedup）|
| The Three Ways - Feedback | E 階段審計 + 物理驗證 |
| The Three Ways - Learning | 21 個 TRAP-SOP 演進 |
| CALMS - Culture | SOUL/AGENTS 五角色 |
| CALMS - Automation | `delegate_task` 並聯 |
| CALMS - Lean | 110 行核心檔案 |
| CALMS - Measurement | E-code 系統 + token 監控 |
| CALMS - Sharing | Wiki 攝入 + Skill 共用 |
| DORA 4 metrics | Hermes 4/4 Elite |

**總評**：Hermes 已實作 **85-90%** 本書核心實踐

## 為何必讀

1. **業界聖經**：與 SRE Book、Accelerate 並列 DevOps 三本必讀
2. **操作指南**：不是哲學書，每章都有可實踐的 patterns
3. **4 位作者權威**：4 位 DevOps 創始人合著
4. **MIT/Stanford 等名校採用**：作為 DevOps 課程教材

## 相關書籍

- **The Phoenix Project**（2013）— 入門小說
- **The DevOps Handbook**（2016）— 操作手冊
- **The DevOps Handbook Workbook**（2017）— 實務
- **Building Secure & Reliable Systems**（2020）— 安全整合
- **Accelerate**（2018）— 量化研究（Forsgren, Humble, Kim）
- **Site Reliability Engineering**（2016）— SRE 補完

## 來源

- O'Reilly 線上版：https://www.oreilly.com/library/view/the-devops-handbook/9781457191381/
- IT Revolution Press：http://images.itrevolution.com/documents/DevOps_Handbook_Intro_Part1_Part2.pdf
- Amazon：https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002

## 引用

```bibtex
@book{kim2016devopshandbook,
  title={The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations},
  author={Kim, Gene and Humble, Jez and Debois, Patrick and Willis, John},
  year={2016},
  publisher={IT Revolution Press},
  isbn={978-1942788003}
}
```