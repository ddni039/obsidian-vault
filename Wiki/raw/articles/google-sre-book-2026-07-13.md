---
title: Google SRE Book — Site Reliability Engineering
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book, sre, google, reliability, observability, on-call, postmortem, distributed-systems]
urls:
  - https://sre.google/books/
  - https://sre.google/sre-book/table-of-contents/
editors:
  - Betsy Beyer
  - Chris Jones
  - Jennifer Petoff
  - Niall Richard Murphy
year: 2016 (orig) / 2018 (Workbook) / 2020 (BSRS)
license: CC BY-NC-ND 3.0（線上版免費）
---

# Google SRE Book — Source Material

## 三本官方 SRE 書籍

| 書名 | 主題 | 線上版 |
|------|------|--------|
| **Site Reliability Engineering** | 基礎原理與實踐 | [sre.google/sre-book](https://sre.google/sre-book/table-of-contents/) |
| **The Site Reliability Workbook** | 實務操作指南 | [sre.google/workbook](https://sre.google/workbook/table-of-contents/) |
| **Building Secure & Reliable Systems** | 安全 + 可靠性整合 | [google.github.io/...](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html) |

## SRE Book 完整章節（34 章 + 6 附錄）

### Part I - Introduction
- Chapter 1: Introduction
- Chapter 2: The Production Environment at Google

### Part II - Principles
- Chapter 3: **Embracing Risk** ⭐
- Chapter 4: **Service Level Objectives** ⭐
- Chapter 5: **Eliminating Toil** ⭐
- Chapter 6: Monitoring Distributed Systems
- Chapter 7: The Evolution of Automation at Google
- Chapter 8: Release Engineering
- Chapter 9: **Simplicity** ⭐

### Part III - Practices
- Chapter 10: **Practical Alerting** ⭐（白盒 vs 黑盒 vs 頁面）
- Chapter 11: Being On-Call
- Chapter 12: Effective Troubleshooting
- Chapter 13: Emergency Response
- Chapter 14: Managing Incidents
- Chapter 15: **Postmortem Culture: Learning from Failure** ⭐
- Chapter 16: Tracking Outages
- Chapter 17: Testing for Reliability
- Chapter 18: Software Engineering in SRE
- Chapter 19-20: Load Balancing
- Chapter 21: Handling Overload
- Chapter 22: Addressing Cascading Failures
- Chapter 23: Managing Critical State: Distributed Consensus
- Chapter 24: Distributed Periodic Scheduling
- Chapter 25: Data Processing Pipelines
- Chapter 26: Data Integrity
- Chapter 27: Reliable Product Launches at Scale

### Part IV - Management
- Chapter 28: Accelerating SREs to On-Call
- Chapter 29: Dealing with Interrupts
- Chapter 30: Embedding an SRE to Recover from Operational Overload
- Chapter 31: Communication and Collaboration in SRE
- Chapter 32: The Evolving SRE Engagement Model

### Part V - Conclusions
- Chapter 33: Lessons Learned from Other Industries
- Chapter 34: Conclusion

## 5 大 SRE 核心原則（精華）

### 1. Embracing Risk（接受風險）
> 100% 可用性是錯誤目標。高可用系統必須**接受並管理風險**。

### 2. Service Level Objectives（SLO）
> **SLO > SLA**：內部目標比對外承諾更重要。

| 概念 | 說明 |
|------|------|
| SLI | Service Level Indicator（測量）|
| SLO | Service Level Objective（內部目標）|
| SLA | Service Level Agreement（對外承諾）|

### 3. Eliminating Toil（消除瑣事）
> Toil = manual, repetitive, automatable, tactical, devoid of enduring value, scale linearly with service growth.

**目標**：SRE 時間 50% 在 engineering work，<50% 在 toil。

### 4. Monitoring Distributed Systems（四大黃金信號）
> - Latency
> - Traffic
> - Errors
> - Saturation

### 5. Postmortem Culture（事後檢討文化）
> **Blameless postmortem**：聚焦系統問題，不追究個人責任。

## 引用

```bibtex
@book{beyer2016sre,
  title={Site Reliability Engineering: How Google Runs Production Systems},
  editor={Beyer, Betsy and Jones, Chris and Petoff, Jennifer and Murphy, Niall Richard},
  year={2016},
  publisher={O'Reilly Media},
  url={https://sre.google/sre-book/table-of-contents/}
}
```