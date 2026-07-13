---
title: Chaos Engineering — Pawlikowski (Manning) + Rosenthal/Jones (O'Reilly)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [chaos-engineering, control-plane, reliability, netflix, kubernetes, resilience, principles-of-chaos, pawlikowski, casey-rosenthal, nora-jones]
urls:
  - https://www.manning.com/books/chaos-engineering
  - https://books.google.com/books/about/Chaos_Engineering.html?id=jVjbDwAAQBAJ
---

# Chaos Engineering — Source Material

> ⚠️ 注：本文檔整合兩本 Chaos Engineering 權威書籍的合規資源。

## 書 1：Chaos Engineering — Mikolaj Pawlikowski（Manning, 2021）

### 基本資訊

| 項目 | 內容 |
|------|------|
| **書名** | Chaos Engineering: Site reliability through controlled disruption |
| **作者** | Mikolaj Pawlikowski |
| **出版** | Manning Publications, 2021-02 |
| **頁數** | 424 |
| **ISBN** | 9781617297755 |
| **語言** | English（簡體中譯版另有）|

### 作者背景

**Mikolaj Pawlikowski** = Chaos Engineering 領域的權威
- 創建 PowerfulSeal（Kubernetes chaos engineering tool）
- 創建 Goldpinger（networking visibility tool）
- 多場 podcast / conference speaker

### What's Inside

- Inject failure into processes, applications, and virtual machines
- Test software running on Kubernetes
- Work with both open source and legacy software
- Simulate database connection latency
- Test and improve your team's failure response

### 為什麼這本書有價值

| 價值 | 說明 |
|------|------|
| **三大主軸** | process / application / VM |
| **實作導向** | 包含可下載的 Linux VM image |
| **Kubernetes 重點** | PowerfulSeal = K8s chaos engineering |
| **完整方法論** | 從 design experiments 到 run chaos drills |

## 書 2：Chaos Engineering — Casey Rosenthal + Nora Jones（O'Reilly, 2020）

### 基本資訊

| 項目 | 內容 |
|------|------|
| **書名** | Chaos Engineering: System Resiliency in Practice |
| **作者** | Casey Rosenthal, Nora Jones（contributing authors）|
| **出版** | O'Reilly Media, 2020-04-06 |
| **頁數** | 308 |
| **ISBN** | 9781492043812 |

### 作者背景

**Casey Rosenthal**：
- Netflix Chaos Engineering 創辦人之一
- 後端工程主管

**Nora Jones**：
- Jeli CEO co-founder
- Netflix / Slack / Jet.com Reliability 經驗
- AWS re:Invent 2017 主題演講者（40,000 人）
- 創立 www.learningfromincidents.io
- Resilience Engineering 與 Chaos Engineering 推動者

### 17 章 + 6 contributors 結構

| 領域 | 內容 |
|------|------|
| **理論基礎** | complex systems + chaos methodology |
| **實作** | game days + automated experiments |
| **業界案例** | Google, Microsoft, Slack, LinkedIn |
| **人類因素** | how people interact with software |

### 為什麼這本書有價值

| 價值 | 說明 |
|------|------|
| **Netflix 原創** | 混沌工程的發源地 |
| **17 contributions** | 跨產業的真實經驗 |
| **Human factors** | 不是只有工具，還談人和組織 |
| **O'Reilly 品質** | 業界最高品質的技術書籍 |

## Chaos Engineering 核心原理

### 1. 定義

Chaos Engineering = 在分散式系統上 **故意注入故障** 來驗證韌性的工程學科

> 汽車工程師通過故意撞車來測試安全性。Chaos Engineering 把同樣的原則應用於軟體系統。

### 2. 實驗流程

```
Hypothesis（假設）→ Define steady state → Design experiment
       ↓
Run experiment in production → Measure → Learn → Iterate
       ↓
Fix or improve resilience
```

### 3. 適用範圍

從**簡單 WordPress 站**到 **Kubernetes 巨型分散式系統** 都可以做。

### 4. 工具生態

| 工具 | 用途 | 開發者 |
|------|------|--------|
| **Chaos Monkey** | 隨機殺掉 instance | Netflix |
| **PowerfulSeal** | K8s chaos engineering | Pawlikowski |
| **Chaos Toolkit** | 開源 chaos 框架 | Community |
| **Gremlin** | SaaS chaos platform | Gremlin Inc. |
| **LitmusChaos** | K8s-native chaos engineering | MayaData |
| **Chaos Blade** | 阿里雲開源 | Alibaba |

## 與 Control Plane 的關係

| Chaos Engineering | Control Plane |
|------------------|---------------|
| **注入故障** | 監控控制平面反應 |
| **測試 alerts** | 測試 reconciliation loop |
| **驗證 self-healing** | 測試 declarative state |
| **持續混沌** | 測試 HA failover |

**核心洞察**：Chaos Engineering 是 Control Plane 設計 **唯一**可靠的驗證方法。

## 對 Hermes 主控台（Master Console / Control Plane）的啟示

### 1. Continuous Chaos 原則

```yaml
# 不是偶爾 game day，是持續混沌
chaos_schedule:
  frequency: weekly
  experiments:
    - mcp_failure
    - config_reload_failure
    - skill_router_failure
    - cron_job_failure
```

### 2. Game Day 制度

```yaml
# Game Day：定期的混亂演練
game_day:
  frequency: monthly
  participants: [main_agent, subagent_observer, on_call]
  scenarios:
    - "mcp minimax 突然斷線"
    - "config hot reload 失敗"
    - "subagent 全部 timeout"
  runbook: chaos-engineering-runbook.md
```

### 3. Steadiness 觀察

```python
# Chaos 之前需要定義 steady state
steady_state = {
    "mcp_connected": True,
    "subagent_p99": "< 1 min",
    "skill_avg_response": "< 100ms"
}

# Chaos 中：比對 steady state 變化
delta = current_state - steady_state
```

### 4. Blast Radius 控制

```yaml
# 限制爆炸半徑
blast_radius:
  start_with: 1%
  validate: "steady state 維持"
  expand_to: 5%
  validate: "steady state 維持"
  expand_to: 25%
  # ...
```

## Netflix Chaos Monkey 核心機制

### Chaos Monkey 早期設計原則

| 原則 | 說明 |
|------|------|
| **沒什麼是安全的** | 任何 instance 都可以死 |
| **紅隊攻擊自己的系統** | 持續找漏洞 |
| **失敗是常態** | 必須設計 resilience |
| **測試是發現缺陷的唯一方法** | 不能只靠 review |

### Simian Army（Netflix's Chaos Tools）

| Tool | 用途 |
|------|------|
| **Chaos Monkey** | 隨機殺 instance |
| **Latency Monkey** | 模擬延遲 |
| **Conformity Monkey** | 找不符合 best practice 的 instance |
| **Doctor Monkey** | 抓出 unhealthy instance |
| **Janitor Monkey** | 清理 unused resources |
| **Security Monkey** | 找 security violations |
| **10-18 Monkey** | 找 multi-region 配置問題 |

## Hermes 主控台 Chaos 對應清單

| Hermes 元件 | Chaos 實驗 |
|-----------|----------|
| MCP minimax | 突然斷線 → 是否 graceful degradation |
| Config hot reload | 觸發 reload → 是否驗證成功 |
| Skill router | trigger 路由失敗 → 是否 fallback |
| Subagent | timeout → 是否 circuit breaker 啟動 |
| Cron job | 連續觸發 → 是否 dedupe |
| Disk full | logs 寫入失敗 → 是否 rotate |
| Memory pressure | agent OOM → 是否 swap |
| Gateway restart | kill gateway → 是否 connect back |

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
  title={Chaos Engineering: Site reliability through controlled disruption},
  author={Pawlikowski, Mikolaj},
  year={2021},
  publisher={Manning Publications},
  isbn={9781617297755}
}
```

## 資源

- [Chaos Engineering — Manning](https://www.manning.com/books/chaos-engineering)
- [Chaos Engineering: System Resiliency in Practice](https://books.google.com/books/about/Chaos_Engineering.html?id=jVjbDwAAQBAJ)
- [PowerfulSeal](https://github.com/bloomberg/powerfulseal)
- [Chaos Monkey](https://github.com/Netflix/chaosmonkey)
- [Learn from Incidents](https://www.learningfromincidents.io)
- [Gremlin](https://www.gremlin.com)
