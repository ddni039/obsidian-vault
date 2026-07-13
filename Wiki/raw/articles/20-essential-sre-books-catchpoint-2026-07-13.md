---
title: 20 Essential SRE Books（Catchpoint 整理）
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book-list, sre, reliability, devops, postmortem, monitoring, slm]
url: https://www.catchpoint.com/blog/sre-books
author: Peter Murray (Catchpoint)
date: 2020-02-26
---

# 20 Essential SRE Books — Source Material

## 完整 20 本書單

### 1. Accelerate: Building & Scaling High-Performing Technology Organizations
- **作者**：Nicole Forsgren, Jez Humble, Gene Kim
- **核心**：4 年研究，量化哪些實踐真正影響軟體交付效能
- **關鍵發現**：4 個關鍵指標（部署頻率、MTTR、変更前置時間、變更失敗率）

### 2. A Seat at the Table: IT Leadership in the Age of Agility
- **作者**：Mark Schwartz
- **核心**：IT 領導者應成為「價值創造引擎」

### 3. Continuous Delivery
- **作者**：Jez Humble, David Farley
- **核心**：自動化交付的策略與實踐

### 4. Data Visualization: A Handbook for Data Driven Design
- **作者**：Andy Kirk
- **核心**：資料視覺化（postmortem、SLM 談判用）

### 5. Foundations of Service Level Management
- **作者**：Rick Sturm, Wayne Morris, Mary Jander
- **核心**：SLM/SLA 經典（2000 年）

### 6. High Performance Web Sites
- **作者**：Steve Sounders
- **核心**：14 條性能優化規則

### 7. Inspired: How to Create Tech Products Customers Love
- **作者**：Marty Cagan
- **核心**：以客戶為中心的產品設計

### 8. Platform Revolution
- **作者**：Geoffrey Parker, Marshall Van Alstyne, Sangeet Choudray
- **核心**：PaaS 商業模式分析

### 9. Post-Incident Reviews: Learning from Failure
- **作者**：Jason Hand
- **核心**：現代化 postmortem 流程

### 10. Practical Reliability Engineering (5th Ed)
- **作者**：Patrick O'Conner, Andrew Kleyner
- **核心**：可靠性理論 + 實務

### 11. Principles of Network and System Administration
- **作者**：Mark Burgess
- **核心**：系統管理基礎原理

### 12. Seeking SRE: Conversations About Running Production Systems at Scale
- **作者**：David N. Blank-Edelman
- **核心**：40 位 SRE 訪談；聚焦「人」非「技術」

### 13. Site Reliability Engineering（見 google-sre-book-2026-07-13.md）

### 14. The Field Guide to Understanding 'Human Error'
- **作者**：Sidney Dekker
- **核心**：人為錯誤的新理解（Safety II 概念）

### 15. The Phoenix Project
- **作者**：Gene Kim, Kevin Behr, George Spafford
- **核心**：DevOps 小說體入門

### 16. The DevOps Handbook
- **作者**：Gene Kim, Patrick Debois, John Willis, Jez Humble
- **核心**：DevOps 原則與實踐

### 17. The Site Reliability Workbook（見 google-sre-book-2026-07-13.md）

### 18. The Visible Ops Handbook
- **作者**：Gene Kim et al.
- **核心**：可見性驅動的變更管理

### 19. Time Series Database Systems
- **核心**：時間序列資料庫（監控指標儲存）

### 20. Toil in IT Operations（白皮書）
- **核心**：定義 toil，量化影響

## 書單分類（按優先級）

### 🔴 必讀（5 本）
1. **Accelerate** — 量化研究 + 4 個關鍵指標
2. **SRE Book** — 基礎原理
3. **The Phoenix Project** — DevOps 入門小說
4. **The DevOps Handbook** — DevOps 原則
5. **Continuous Delivery** — 自動化交付

### 🟡 推薦（5 本）
6. **The Site Reliability Workbook** — SRE 實務
7. **Building Secure & Reliable Systems** — 安全整合
8. **Post-Incident Reviews** — modern postmortem
9. **Practical Reliability Engineering** — 可靠性理論
10. **Seeking SRE** — 人本 SRE

### 🟢 進階（10 本）
- 11. **High Performance Web Sites** — 性能優化
- 12. **Data Visualization** — 視覺化
- 13. **Inspired** — 產品管理
- 14. **A Seat at the Table** — IT 領導
- 15. **Platform Revolution** — 商業模式
- 16. **Foundations of SLM** — SLM 經典
- 17. **The Field Guide to Human Error** — 人因
- 18. **Principles of Network and System Admin** — 系統管理
- 19. **Time Series DB** — TSDB
- 20. **Toil in IT Operations** — Toil 定義

## 與 Hermes 的對應

| SRE 概念 | Hermes 對應 |
|---------|------------|
| SLO（服務等級目標）| `RULES.md` E-code + 50k/80k/120k token 配額 |
| Eliminating Toil | 並聯 SOP + 24 輪 7.5× speedup |
| Postmortem Culture | `physical-verification.md` Step 1-6 + `real-case-2026-07-11.md` |
| Monitoring 四大黃金信號 | `~/.hermes/logs/`（latency = API time, traffic = API count, errors = error.log, saturation = token usage）|
| Embracing Risk | 50k Warning / 80k Distill / 120k Lock（接受風險，明確閾值）|
| Simplicity | 110 行核心檔案 + 71 顆 <250 行 Skill |
| On-Call | `delegation: max_concurrent_children: 3` |
| Release Engineering | Skill 維護 SOP 的 v1.x→v2.x 演進 |
| Load Balancing | `delegate_task` 並聯 + early termination |
| Cascading Failures | E-code 斷路器（Circuit Breaker）|

## 來源

- [Catchpoint: 20 Essential Books for SRE](https://www.catchpoint.com/blog/sre-books)
- [Google SRE Books](https://sre.google/books/)
- [The Phoenix Project](https://itrevolution.com/product/the-phoenix-project/)
- [Accelerate](https://itrevolution.com/product/accelerate/)