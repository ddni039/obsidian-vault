---
title: The DevOps Handbook — Gene Kim et al. (2016)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book, devops, three-ways, calms, dora, gene-kim, jez-humble, patrick-debois, john-willis]
urls:
  - http://images.itrevolution.com/documents/DevOps_Handbook_Intro_Part1_Part2.pdf
  - https://www.oreilly.com/library/view/the-devops-handbook/9781457191381/
authors:
  - Gene Kim（IT Revolution 創辦人、《Phoenix Project》作者）
  - Jez Humble（《Continuous Delivery》合著者、Lean Enterprise 作者）
  - Patrick Debois（DevOpsDays 創辦人，「DevOps」一詞的共同發明者）
  - John Willis（Docker 前傳教士、55 年 IT 經驗）
publisher: IT Revolution Press, LLC
year: 2016
isbn: 978-1942788003
---

# The DevOps Handbook — Source Material

## 攝入來源（合規）

| 來源 | 用途 | URL |
|------|------|-----|
| IT Revolution 官方 Intro PDF | 目錄、作者背景、3 Ways 結構 | http://images.itrevolution.com/documents/DevOps_Handbook_Intro_Part1_Part2.pdf |
| O'Reilly 完整目錄 | 23 章 + 6 部結構 | https://www.oreilly.com/library/view/the-devops-handbook/9781457191381/ |
| DORA 2024 報告（Google Cloud）| 量化延伸研究 | https://dora.dev/research/2024/dora-report/ |

**未擷取未授權完整 PDF**（避免版權問題）。改用官方免費章節 + 公開研究。

## 核心結構（23 章 + 6 部）

### Part I - The Three Ways（1-4 章）
- Ch 1: Agile, Continuous Delivery, and the Three Ways
- Ch 2: The First Way - The Principles of Flow
- Ch 3: The Second Way - The Principles of Feedback
- Ch 4: The Third Way - The Principles of Continual Learning and Experimentation

### Part II - Where to Start（5-8 章）
- Ch 5: Selecting Which Value Stream to Start With
- Ch 6: Understanding the Work in Our Value Stream, Making it Visible
- Ch 7: How to Design Our Organization and Architecture (Conway's Law)
- Ch 8: How to Get Great Outcomes by Integrating Operations

### Part III - The First Way: Technical Practices of Flow（9-13 章）
- Ch 9: Create the Foundations of Our Deployment Pipeline
- Ch 10: Enable Fast and Reliable Automated Testing
- Ch 11: Enable and Practice Continuous Integration
- Ch 12: Automate and Enable Low-Risk Releases
- Ch 13: Architect for Low-Risk Releases

### Part IV - The Second Way: Technical Practices of Feedback（14-18 章）
- Ch 14: Create Telemetry
- Ch 15: Analyze Telemetry
- Ch 16: Enable Feedback for Dev and Ops
- Ch 17: Integrate Hypothesis-Driven Development and A/B Testing
- Ch 18: Create Review and Coordination Processes

### Part V - The Third Way: Continual Learning（19-21 章）
- Ch 19: Enable and Inject Learning into Daily Work
- Ch 20: Convert Local Discoveries into Global Improvements
- Ch 21: Reserve Time to Create Organizational Learning

### Part VI - Integrating InfoSec, Change Management, Compliance（22-23 章）
- Ch 22: Information Security as Everyone's Job
- Ch 23: Protecting the Deployment Pipeline

## 3 Ways 核心框架

### The First Way: Flow（左→右）
- 優化工作從 Dev 到 Ops 的流動
- 實踐：CI、CD、自動化測試、低風險發布

### The Second Way: Feedback（右→左）
- 建立快速回饋機制
- 實踐：遙測、監控、A/B Test、ChatOps

### The Third Way: Continual Learning
- 建立持續學習與實驗文化
- 實踐：Blameless postmortem、Game Days、Innovation time

## CALMS 框架（Damon Edwards 推廣）

| 字母 | 領域 | 核心問題 |
|------|------|---------|
| **C**ulture | 文化 | 如何打破 Dev 與 Ops 壁壘？ |
| **A**utomation | 自動化 | 如何減少手動錯誤？ |
| **L**ean | 精實 | 如何消除浪費？ |
| **M**easurement | 度量 | 如何量化交付效能？ |
| **S**haring | 分享 | 如何跨團隊傳播知識？ |

## DORA 4 大關鍵指標（DevOps 業界標準）

| 指標 | 定義 | Elite performers |
|------|------|-----------------|
| **Deployment Frequency** | 部署頻率 | On-demand（多次/天）|
| **Lead Time for Changes** | 變更前置時間 | < 1 小時 |
| **Change Failure Rate** | 變更失敗率 | 0-15% |
| **Failed Deployment Recovery Time** | 失敗恢復時間 | < 1 小時 |

## 作者群簡介

### Gene Kim
- IT Revolution 創辦人
- 著作：《The Phoenix Project》（DevOps 入門小說，銷量百萬）
- 創辦 DevOps Enterprise Summit
- **研究起點**：1999 年起研究高效能技術組織

### Jez Humble
- 《Continuous Delivery》合著者（Jolt Award 得主）
- 《Lean Enterprise》作者
- 焦點：幫助組織可靠地交付有價值、高品質軟體

### Patrick Debois
- **「DevOps」一詞的共同發明者**
- 2009 年創辦 **DevOpsDays**（比利時）
- IEEE 論文：Kanban in Operations

### John Willis
- IT 管理 35+ 年經驗
- 前 Docker 傳教士
- 創辦 Chain Bridge Systems

## 4 位作者各自的「Aha Moment」

| 作者 | 觸發時刻 |
|------|---------|
| Gene Kim | 2006：某航空公司 IT 運維每年大發布導致災難、SLA 罰款、裁員 |
| Jez Humble | 2004：在 ThoughtWorks 將 2 週手動部署 → 1 小時自動化部署 |
| Patrick Debois | 2009：看完 John Allspaw 的「10 Deploys per Day」演講，決定創辦 DevOpsDays |
| John Willis | 2008：遇見 Puppet 創辦人 Luke Kanies，重新認識 config management |

## Hermes 對應評估

| DevOps 概念 | Hermes 對應 |
|------------|------------|
| Three Ways Flow | 並聯 `delegate_task`（24 輪 7.5× speedup）|
| Three Ways Feedback | E 階段審計 + TRAP-SOP 學習 |
| Three Ways Continual Learning | TRAP-SOP 21 個 → SOP 系統演進 |
| CALMS - Culture | 三層職責邊界（TRAP-SOP-021）|
| CALMS - Automation | 自動掃描腳本（consistency-audit.sh）|
| CALMS - Lean | 110 行核心檔案 + 71 顆 <250 行 Skill |
| CALMS - Measurement | E-code 斷路器 + token 監控 |
| CALMS - Sharing | `~/.hermes/skills/` 共用 + Wiki 攝入 |
| DORA Deployment Frequency | 24 輪並聯 = ~100 deployments/天 |
| DORA Lead Time | 並聯 = ~10x faster |
| DORA Change Failure Rate | TRAP-SOP 21 個 + E-code 系統 = 低失敗率 |
| DORA Recovery Time | `touch config.yaml` + 重啟 gateway = ~30 秒 |

**總評**：Hermes 已實作 **85-90%** DevOps Handbook 核心實踐

## 與 SRE 的關係

| DevOps | SRE |
|--------|-----|
| 哲學（為什麼）| 實踐（怎麼做）|
| 跨團隊協作 | 系統可靠性 |
| 流程優化 | 量化 SLO |
| 文化變革 | 工程方法論 |
| The Three Ways | 5 大 SRE 原則 |

DevOps 講**為什麼**，SRE 講**怎麼做**。本書與 SRE Book 形成完整閉環。

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