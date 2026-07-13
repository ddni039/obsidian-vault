---
title: Chaos Engineering
created: 2026-07-13
updated: 2026-07-13
uid: e-565ce8cf8d1e
type: entity
tags: [chaos-engineering, control-plane, reliability, netflix, resilience, principles-of-chaos, casey-rosenthal, nora-jones, mikolaj-pawlikowski]
sources:
  - raw/articles/chaos-engineering-books-2026-07-13.md
related:
  - "[[kubernetes-control-plane]]"
  - "[[control-plane-pattern]]"
confidence: high
---

# Chaos Engineering

## 簡介

**Chaos Engineering** = 在分散式系統上 **故意注入故障** 來驗證韌性的工程學科。

> 汽車工程師通過故意撞車來測試安全性。Chaos Engineering 把同樣的原則應用於軟體系統。

## 兩本權威書籍

### 書 1：Chaos Engineering: System Resiliency in Practice

| 項目 | 內容 |
|------|------|
| **作者** | Casey Rosenthal, Nora Jones（contributing authors）|
| **出版** | O'Reilly Media, 2020-04 |
| **頁數** | 308 |
| **ISBN** | 9781492043812 |

**作者背景**：
- Casey Rosenthal：Netflix Chaos Engineering 創辦人
- Nora Jones：Jeli CEO co-founder；Netflix/Slack/Jet.com reliability

### 書 2：Chaos Engineering: Site Reliability Through Controlled Disruption

| 項目 | 內容 |
|------|------|
| **作者** | Mikolaj Pawlikowski |
| **出版** | Manning Publications, 2021-02 |
| **頁數** | 424 |
| **ISBN** | 9781617297755 |

**作者背景**：
- 創建 PowerfulSeal（K8s chaos tool）
- 創建 Goldpinger（network visibility tool）

## 實驗流程

```
Hypothesis → Define steady state → Design experiment
       ↓
Run experiment in production → Measure → Learn → Iterate
       ↓
Fix or improve resilience
```

## Netflix 的 Simian Army

| Tool | 用途 |
|------|------|
| **Chaos Monkey** | 隨機殺 instance |
| **Latency Monkey** | 模擬延遲 |
| **Conformity Monkey** | 找不符合 best practice 的 instance |
| **Doctor Monkey** | 抓出 unhealthy instance |
| **Janitor Monkey** | 清理 unused resources |
| **Security Monkey** | 找 security violations |
| **10-18 Monkey** | 找 multi-region 配置問題 |

## 4 大實驗原則

### 1. Steady State 必須量化

```python
steady_state = {
    "p99_latency": "< 100ms",
    "error_rate": "< 0.1%",
    "mcp_connected": True,
    "skill_avg_response": "< 100ms"
}

delta = current_state - steady_state
```

### 2. Blast Radius 控制

```
1% → validate → 5% → validate → 25% → 100%
```

絕不直接 100% blast。從最小爆炸半徑開始，逐步擴大。

### 3. Continuous Chaos > Game Day

不是偶爾做一次 game day，是**持續自動做**。

### 4. Fail-Fast & Learn Fast

混沌不是破壞，是**發現缺陷 → 學習 → 改進**。

## 工具生態

| 工具 | 用途 | 開發者 |
|------|------|--------|
| **Chaos Monkey** | 隨機殺 instance | Netflix |
| **PowerfulSeal** | K8s chaos engineering | Pawlikowski / Bloomberg |
| **Chaos Toolkit** | 開源框架 | Community |
| **Gremlin** | SaaS platform | Gremlin Inc. |
| **LitmusChaos** | K8s-native | MayaData |
| **Chaos Blade** | Alibaba 開源 | Alibaba |

## 對 Hermes 主控台的啟示

| Hermes 元件 | Chaos 實驗 |
|-----------|----------|
| **MCP minimax** | 突然斷線 → graceful degradation |
| **Config hot reload** | 觸發 reload → 是否驗證成功 |
| **Skill router** | trigger 失敗 → fallback |
| **Subagent** | timeout → circuit breaker |
| **Cron job** | 連續觸發 → dedupe |
| **Disk full** | logs 寫入失敗 → rotate |
| **Gateway restart** | kill → reconnect |

## 3 大應用場景

### 1. Game Day
**頻率**：每月
**參與**：main_agent + observer + on-call
**場景**：mcp 斷線 / config 失敗 / subagent timeout

### 2. Continuous Chaos
**頻率**：每週
**自動**：cron 觸發
**範圍**：1% blast radius

### 3. Pre-Production Chaos
**頻率**：每次發布前
**範圍**：完整 service
**驗證**：reconciliation 正常

## 為什麼 Chaos Engineering 對 Hermes 重要？

| 原因 | 說明 |
|------|------|
| **驗證控制平面** | Chaos 是 control plane 唯一可靠驗證方法 |
| **發現未知 bug** | 計劃測不到的，混沌能測到 |
| **建立信心** | 對 production system 的信心 |
| **持續改進** | 反覆 iteration，推動 reliability |

## 引用

```bibtex
@book{rosenthal2020chaos,
  title={Chaos Engineering: System Resiliency in Practice},
  author={Rosenthal, Casey and Jones, Nora},
  year={2020},
  publisher={O'Reilly Media},
  isbn={9781492043812}
}

@book{pawlikowski2021chaos,
  title={Chaos Engineering: Site Reliability Through Controlled Disruption},
  author={Pawlikowski, Mikolaj},
  year={2021},
  publisher={Manning Publications},
  isbn={9781617297755}
}
```

## 資源

- [Chaos Engineering — Manning](https://www.manning.com/books/chaos-engineering)
- [Chaos Engineering: System Resiliency in Practice — O'Reilly](https://books.google.com/books/about/Chaos_Engineering.html?id=jVjbDwAAQBAJ)
- [PowerfulSeal](https://github.com/bloomberg/powerfulseal)
- [Chaos Monkey](https://github.com/Netflix/chaosmonkey)
- [Learn from Incidents](https://www.learningfromincidents.io)