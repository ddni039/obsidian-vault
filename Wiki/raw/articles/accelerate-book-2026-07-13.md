---
title: Accelerate — Nicole Forsgren, Jez Humble, Gene Kim (2018)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book, accelerate, dora, devops, four-key-metrics, nicole-forsgren, jez-humble, gene-kim, lean, continuous-delivery, shingo-award]
urls:
  - https://itrevolution.com/product/accelerate/
  - https://itrevolution.com/wp-content/uploads/2022/06/ACC_excerpt.pdf
license: Commercial book (official excerpt available free from IT Revolution)
publication: March 27, 2018
pages: 288
isbn: "9781942788331"
authors:
  - Nicole Forsgren (Partner, Microsoft Research; PhD)
  - Jez Humble (coauthor, The DevOps Handbook)
  - Gene Kim (WSJ bestselling author; Tripwire founder)
awards:
  - Shingo Publication Award
sources:
  - danlebrero.com blog summary
  - roman.pt five-minute summary
---

# Accelerate — Source Material

> **合規來源**：IT Revolution 官方書籍頁面（itrevolution.com）+ 作者公開摘要 + 第三方章節筆記
> **不使用**：ebooks.karbust.me（未授權盜版 PDF）

## 官方書籍資訊

| 項目 | 內容 |
|------|------|
| **書名** | Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations |
| **作者** | Nicole Forsgren, Jez Humble, Gene Kim |
| **出版** | IT Revolution Press, 2018-03-27 |
| **頁數** | 288 |
| **ISBN** | 9781942788331 |
| **獎項** | Shingo Institute Publication Award |

### 作者背景

**Nicole Forsgren**：
- Partner at Microsoft Research
- Shingo Publication Award-winning author
- Puppet 調查研究主要研究者（State of DevOps Reports 2014-2017）
- 曾創業並成功退出至 Google
- Professor, performance engineer, sysadmin

**Jez Humble**：
- Coauthor of Accelerate and The DevOps Handbook
- Continuous Delivery 專家

**Gene Kim**：
- WSJ bestselling author（The Phoenix Project, The Unicorn Project）
- Tripwire 創辦人兼 CTO（任職 13 年）
- DevOps Enterprise Summit 創辦人（2014 起）
- 超過 100 萬本書銷售量

## 研究規模

| 項目 | 數據 |
|------|------|
| **研究年份** | 2014-2017（4 年）|
| **調查問卷** | 23,000+ 份 |
| **組織數量** | 2,000+ 個 |
| **適用範圍** | 任何規模（<5人到>10k人）、綠地與棕地、任何產業 |

## 核心發現（Part I: What We Found）

### Chapter 1 - Accelerate

**Maturity Model vs Capability Model**：

| Maturity Model | Capability Model |
|---------------|------------------|
| 有固定目標，抵達後就「完成」| 永遠可以改進，沒有終點 |
| 鎖步式，所有組織/團隊被同等對待 | 多維度、動態、需考慮團隊與組織情境 |
| 虛榮指標 | 結果導向指標 |
| 靜態級別 | 動態級別 |
| 關注過程合規 | 關注正確的能力 |

### Chapter 2 - Measuring Performance

**Four Key Metrics（四個關鍵指標）**：

| 指標 | 定義 | Elite 標準 |
|------|------|-----------|
| **Lead Time** | 從程式碼提交到生產環境運行的時間 | < 1 小時 |
| **Deployment Frequency** | 部署頻率 | On-demand（每天多次）|
| **Mean Time To Restore (MTTR)** | 生產故障後恢復服務的時間 | < 1 小時 |
| **Change Fail Rate** | 導致服務中斷或故障的變更比例 | 0-15% |

**測量維度**：
- **Throughput（效能）**：Lead Time + Deployment Frequency
- **Stability（穩定性）**：MTTR + Change Fail Rate
- **兩者同步移動** → 沒有效能與穩定性的取捨

**為什麼 MTTR 比 MTBF 更好**：「失敗是不可避免的」（Failure is inevitable）

**舊指標的缺陷**：
- Lines of Code（個人/局部）
- Velocity（個人/局部）
- Utilization（個人/局部）
- 關注輸出而非結果

**核心洞察**：「軟體交付效能影響組織績效，包括非商業性的」

### Chapter 3 - Measuring and Changing Culture

**Westrum 組織文化三類型**：

| Pathological | Bureaucratic | Generative |
|-------------|-------------|------------|
| 權力導向 | 規則導向 | 績效導向 |
| 低合作 | 適度合作 | 高度合作 |
|  messenger 被「射殺」| messenger 被忽視 | messenger 被培訓 |
| 推卸責任 | 狹隘責任 | 風險共擔 |
| 跨部門被阻止 | 跨部門被容忍 | 跨部門被鼓勵 |
| 失敗→責備 | 失敗→正義 | 失敗→探究 |
| 創新被扼殺 | 創新→問題 | 創新→實施 |

**好資訊流的關鍵**：及時、以可用的方式回答需要回答的問題

**文化變革**：先改變人的行為，而非先改變人的想法（John Shook）

### Chapter 4 - Technical Practices

**Continuous Delivery 關鍵原則**：
- Build quality in（內建品質）
- Small batches（小批次）
- People solve problems, computers do repetitive tasks（人解決問題，電腦做重複性工作）
- Continuous improvement（持續改進）
- Everyone is responsible（每個人都負責）

**Continuous Delivery 基礎**：
- Comprehensive configuration management：一切都在版本控制中
- Continuous Integration
- Continuous testing

**技術實踐**：
- Version Control（包括系統和應用配置）
- Test Automation（可靠測試、開發者撰寫）
- Test Data Management
- Trunk-Based Development（不超過一天的分支）
- Shift Left on Security

### Chapter 5 - Architecture

**最重要的特性**：Loosely Coupled（鬆耦合）

**Loosely Coupled 的定義**：
- 大多數測試可以在非整合環境中完成
- 可以獨立於依賴的應用程式進行發布

**架構師應關注**：工程師和成果，而非工具或技術

**增加人數不會線性提升產出**：如果人們能夠自主工作，人數與產出有正相關

### Chapter 6 - Integrating InfoSec into Delivery Lifecycle

- Shift Left on Security
- Security 在每個階段都參與

### Chapter 7 - Management Practices

- Limit Work in Progress（WIP 限制）
- Visual management（視覺化管理）
- Lightweight change approval processes

### Chapter 8 - Product Development

- Small batches
- Make flow of work visible
- Customer feedback
- Team experimentation

### Chapter 9 - Making Work Sustainable

**核心洞察**：「如果它讓你痛苦，就更頻繁地做它」（if it hurts, do it more often）

**Microsoft 案例**：採用 DevOps 後，開發者滿意度從 38% 提升到 75%

### Chapter 10 - Employee Satisfaction, Identity and Engagement

- Job satisfaction drives performance
- Identity and engagement matter

### Chapter 11 - Leaders and Managers

**Transformational Leader 特徵**：
- Enable cross-functional collaboration
- Create a climate of learning
- Make effective use of tools

**組織變革失敗的常見原因**：
1. 把轉型當成有截止日期的項目
2. 自上而下實施，沒有受影響者的意見
3. 沒有為轉型設定可衡量的業務和組織成果目標

## 24 Key Capabilities（24 個關鍵能力）

分為 5 大類：

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
16. Production Monitoring（inform business decisions）
17. Visualizing Work
18. Lightweight Change Approval
19. Proactive Notifications

### 5. Cultural（文化）
20. Foster generative culture
21. Encourage learning
22. Collaboration amongst teams
23. Job Satisfaction
24. Support Transformational leadership

## 對 Hermes 的對應

| Accelerate 能力 | Hermes 對應 | 評估 |
|----------------|------------|------|
| **Deployment Automation** | Skill 維護 SOP 自動化 | ✅ 直接對應 |
| **Version Control** | `~/.hermes/skills/` + git | ✅ 直接對應 |
| **Test Automation** | E 階段御史審計（四大死穴核查）| ✅ 直接對應 |
| **Loosely Coupled** | 核心檔（SOUL/AGENTS/RULES/CODEX）模組化 | ✅ 直接對應 |
| **Continuous Delivery** | Skill 持續維護 SOP | ✅ 直接對應 |
| **Trunk-Based Development** | 核心檔及時更新（無長期分支）| ✅ 直接對應 |
| **Production Monitoring** | `errors.log` + token usage 監控 | ✅ 直接對應 |
| **Limit WIP** | `max_concurrent_children=3` | ✅ 直接對應 |
| **Generative Culture** | TRAP-SOP-010/011（No blame postmortem）| ✅ 直接對應 |
| **Lean Management** | Phase Gate 審計機制 | ✅ 直接對應 |
| **Empowered Teams** | subagent 自主决策 | ✅ 直接對應 |
| **Customer Feedback** | 用戶溝通偏好（確認於 2026-07-13）| ✅ 直接對應 |

## 量化對應（Elite vs Hermes）

| 指標 | Elite 標準 | Hermes 評估 |
|------|-----------|------------|
| **Lead Time** | < 1 小時 | ✅ ~10x faster |
| **Deployment Frequency** | On-demand | ✅ 每天多次 |
| **MTTR** | < 1 小時 | ✅ ~30 秒 |
| **Change Fail Rate** | 0-15% | ✅ 極低 |

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