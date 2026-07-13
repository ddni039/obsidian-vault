---
title: Control Plane Pattern — Declarative + Reconciliation
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, control-plane, declarative, reconciliation-loop, kubernetes-pattern, desired-state, hermes-design]
sources:
  - raw/articles/kubernetes-control-plane-2026-07-13.md
related:
  - "[[kubernetes-control-plane]]"
  - "[[chaos-engineering]]"
confidence: high
---

# Control Plane Pattern — Declarative + Reconciliation

## 定義

**Control Plane Pattern** = 用 **Declarative state definition** + **Continuous reconciliation loop** 來管理複雜系統的設計模式。

> 不是告訴系統「做什麼」（imperative），而是告訴系統「要達到什麼狀態」（declarative），由 control loop 自動實現。

## 三大元件

```
┌─────────────────────┐
│   Declarative       │ ← 用戶定義 desired state（YAML / config）
│   State Spec        │
└─────────────────────┘
           ↓
┌─────────────────────┐
│   Control Loop      │ ← 持續比對 desired vs actual，自動修復
│   (Reconciliation)  │
└─────────────────────┘
           ↓
┌─────────────────────┐
│   State Store       │ ← 持久化 state（DB / KV store）
│   (etcd / files)    │
└─────────────────────┘
```

## K8s Control Plane 的 5 大元件對應

| K8s 元件 | 對應 | Hermes 對應 |
|---------|------|------------|
| **API Server** | API 入口 | trigger dispatch |
| **etcd** | State store | ~/.hermes state |
| **Scheduler** | 排程 | subagent 並聯 dispatcher |
| **Controller Manager** | Reconciliation | E 階段 + Audit |
| **Cloud Controller** | 外部整合 | MCP / external API |

## Declarative 設計的 5 個原則

### 1. 期望狀態描述

```yaml
# K8s 範例
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hermes-control-plane
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hermes
  template:
    metadata:
      labels:
        app: hermes
    spec:
      containers:
      - name: hermes
        image: hermes:latest
        ports:
        - containerPort: 8080
```

### 2. Reconciliation Loop

```
while running:
    actual_state = get_current_state()
    if actual_state != desired_state:
        reconcile(actual_state, desired_state)
    sleep(reconcile_interval)
```

### 3. Eventual Consistency

不要求立即一致，而是「最終一致」。

### 4. Idempotent Operations

無論執行幾次，結果相同。

### 5. Status Reporting

持續報告 current state（healthy / degraded / down）。

## Hermes 主控台如何套用

### 當前狀態（Imperative 為主）

```python
# 主控台目前：
if mcp_disconnected:
    reconnect()
if skill_failed:
    retry()
```

### 改為 Declarative + Reconciliation

```yaml
# 期望狀態
hermes_desired_state:
  mcp_minimax: "connected"
  skill_count: 71
  active_profile: "default"
  reconciliation:
    - resource: "mcp"
      health_check_interval: 30s
      reconcile_action: "reconnect"
    - resource: "skill"
      integrity_check_interval: 60s
      reconcile_action: "rollback or reload"
```

```python
# 主控台 reconciliation loop
while True:
    actual = observe_state()
    for resource in desired_state.reconciliation:
        if not actual[resource.name] == desired_state[resource.name]:
            reconcile(actual[resource.name], desired_state[resource.name])
    sleep(5)
```

## Control Plane 的 6 大優勢

| 優勢 | 說明 |
|------|------|
| **Self-healing** | 自動修復失敗 |
| **Declarative** | 用戶只描述期望，不需要命令 |
| **Idempotent** | 重複執行安全 |
| **Auditable** | state diff 容易追蹤 |
| **可測試** | Chaos Engineering 直接驗證 |
| **水平擴展** | stateless controller 容易加節點 |

## Control Plane 的 4 大挑戰

| 挑戰 | 解法 |
|------|------|
| **Eventual consistency** | 使用 status subresource |
| **State conflict** | optimistic locking + last-write-wins |
| **Distributed state** | Raft / Paxos consensus |
| **Rollback complexity** | snapshot previous state |

## Admission Control 模式

Hermes 也應該有 admission control：

| K8s | Hermes |
|-----|--------|
| **mutating webhook** | context distillation |
| **validating webhook** | E-code 審計（拒絕 E005/E009）|
| **policy** | TRAP-SOP 規則 |

## Operator Pattern

K8s 的 Operator = **CRD（schema）** + **Custom Controller（reconciliation）**

Hermes 對應：

```
K8s:                  Hermes:
CRD                   Skill YAML
CR (instance)         Skill instance
Operator              subagent
kubectl apply         trigger dispatch
kubectl get           status check
```

## Chaos Engineering + Control Plane

Chaos 是驗證 Control Plane 行為的**唯一**可靠方法：

| Chaos 實驗 | 驗證 Control Plane 反應 |
|----------|---------------------|
| Kill MCP | reconciliation 重連？|
| Config reload fail | rollback 工作？|
| Subagent OOM | circuit breaker？|
| State corruption | etcd backup restore？|

## 為什麼這對 Hermes 重要？

### Hermes 1.0 → 2.0 演進

**1.0**：imperative 命令式
```python
if condition:
    do()
```

**2.0**：declarative + reconciliation
```python
declare_desired_state()
while True:
    reconcile_to_desired_state()
```

**2.0 優勢**：
- 自動 self-healing
- 容易驗證（混沌測試）
- 容易擴展（新狀態描述）
- 容易維護（state diff 一目了然）

## 引用

```bibtex
@online{control-plane-pattern,
  title={Control Plane Pattern - Declarative + Reconciliation},
  source={Extracted from Kubernetes Control Plane Architecture (2026)},
  year={2026}
}
```

## 資源

- [Kubernetes Architecture 2026](https://www.cloudoptimo.com/blog/inside-kubernetes-the-2026-architecture-breakdown/)
- [Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [Controller Runtime](https://github.com/kubernetes-sigs/controller-runtime)
- [CNCF Operator White Paper](https://www.cncf.io)