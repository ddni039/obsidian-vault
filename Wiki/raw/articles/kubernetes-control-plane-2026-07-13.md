---
title: Kubernetes Control Plane Architecture (2026)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [kubernetes, control-plane, container-orchestration, architecture, reconciliation-loop, declarative, crd, operators]
url: https://www.cloudoptimo.com/blog/inside-kubernetes-the-2026-architecture-breakdown/
source_date: 2026
---

# Kubernetes Control Plane Architecture — Source Material

> ⚠️ 注：本文檔整合 CloudOptimo 2026-04 完整 Kubernetes 架構分析（合規 blog post）。
> **不使用**：ebooks.karbust.me（盜版）

## 為什麼選這份資源

| 優勢 | 說明 |
|------|------|
| **2026 視角** | 包含 v1.36 最新特性 |
| **完整架構** | Control plane + worker nodes + CRD + Operator |
| **CNCF 數據** | 82% 容器用戶在 production |
| **AI workload** | 66% 生成式 AI 用 K8s 管理 |

## Kubernetes 起源

| 項目 | 內容 |
|------|------|
| **引入者** | Google, 2014 |
| **基礎** | Google 內部 Borg cluster manager |
| **捐贈** | CNCF（Cloud Native Computing Foundation）, 2015 |
| **採用率** | 82% 容器用戶（2025）|
| **AI 採用** | 66% 生成式 AI 用 K8s |

## 兩大層

### Control Plane（編排層）
維持 cluster 全域視圖，做出排程決策，持續 drive 系統到 desired state。

### Worker Nodes（執行層）
執行 control plane 的決策，運行 application workloads。

```
┌─────────────────────┐
│   Control Plane     │
│  ┌────────────────┐ │
│  │ kube-apiserver │ │ ← 所有操作的入口
│  ├────────────────┤ │
│  │ etcd           │ │ ← distributed KV store
│  ├────────────────┤ │
│  │ kube-scheduler │ │ ← Pod scheduling
│  ├────────────────┤ │
│  │ controller-    │ │
│  │ manager        │ │ ← reconciliation loops
│  ├────────────────┤ │
│  │ cloud-         │ │
│  │ controller-    │ │ ← cloud provider integration
│  │ manager        │ │
│  └────────────────┘ │
└─────────────────────┘
           ↓
┌─────────────────────┐
│   Worker Nodes      │
│  ┌────────────────┐ │
│  │ kubelet        │ │ ← node agent
│  ├────────────────┤ │
│  │ kube-proxy     │ │ ← service routing
│  ├────────────────┤ │
│  │ Container      │ │
│  │ Runtime        │ │ ← execute containers
│  └────────────────┘ │
└─────────────────────┘
```

## 核心 Control Plane 元件

| 元件 | 角色 |
|------|------|
| **kube-apiserver** | 所有 cluster 操作的入口。處理認證、RBAC、schema validation、admission control。透過 HTTPS 通訊，通常水平擴展在 LB 後面。 |
| **etcd** | 分散式 KV store，持久化所有 cluster 資料（specifications、state、secrets、policies）。使用 Raft consensus algorithm。**etcd 資料備份失敗 = 整個 cluster state 丟失**。|
| **kube-scheduler** | 將 unscheduled Pods 分配到 worker nodes（兩階段：filtering 過濾不適合 + scoring 排名）|
| **kube-controller-manager** | 運行多個 reconciliation loops，持續比對 desired/actual state 並自動修復 |
| **cloud-controller-manager** | 與雲端 API 整合（AWS/Azure/GCP）|

## Controller 職責分工

| Controller | 職責 |
|-----------|------|
| **Node Controller** | 通過 missed heartbeats 偵測 node 失敗，重新排程 Pods |
| **ReplicaSet Controller** | 維持 desired number of Pod replicas |
| **Endpoints Controller** | 更新 Service-to-Pod mappings |
| **Service Account Controller** | 在新 namespace 創建 service accounts |

## 關鍵設計：Declarative Reconciliation

```
Engineer defines desired state (YAML manifest)
                ↓
       Control Plane continuously reconciles
                ↓
       Actual state → matches → desired state
```

**這是 declarative + reconciliation 模型**，不是 imperative 命令式。

## API Extensibility：CRDs + Operators

### CRD（Custom Resource Definitions）

| 名詞 | 說明 |
|------|------|
| **CRD** | schema / definition |
| **CR** | instance of that schema |
| **Custom Resource** | kubectl get 可看到 |

**比喻**：類似 OOP 的 class 與 object。

### Operator Pattern

```
CRD（schema）
   +
Custom Controller（reconciliation loop）
   =
Operator
```

**常見實例**：
| Operator | 用途 |
|---------|------|
| cert-manager | Certificate + ClusterIssuer |
| Prometheus Operator | ServiceMonitor + PrometheusRule |
| Istio | VirtualService + DestinationRule |

**Operator Framework**：Kubebuilder / Operator SDK / Operator Lifecycle Manager (OLM)

## Admission Control（v1.36 新設計）

### 兩階段 Pipeline

1. **Mutating controllers** 修改 incoming requests
2. **Validating controllers** 強制規則，accept/reject

### 新設計：In-process Policy

| API | 狀態 | 用途 |
|-----|------|------|
| **ValidatingAdmissionPolicy** | GA（v1.30 起）| 內部 validation，無需 external webhook |
| **MutatingAdmissionPolicy** | GA（v1.36 起）| API server 內部直接 mutation |

**好處**：低延遲、無 TLS overhead、高可靠。

## Worker Node 機制

### 三大元件

| 元件 | 角色 |
|------|------|
| **kubelet** | 主要 node agent；監聽 API server assigned Pods；透過 CRI 執行容器；回報 node/Pod 健康 |
| **kube-proxy** | 實作 Kubernetes Service abstraction；維護 network routing rules（iptables 或 IPVS）|
| **Container Runtime** | 執行容器；kubelet 透過 CRI 互動 |

### CRI-Compliant Runtimes

| Runtime | 特性 |
|---------|------|
| **containerd** | 業界標準；AWS EKS/GKE/AKS 使用 |
| **CRI-O** | K8s 專用；Red Hat OpenShift 使用 |

## 對 Hermes 主控台（Master Console）的核心啟示

### 1. Declarative State + Reconciliation Loop

```yaml
# Hermes 的 declarative design
control_plane:
  desired_state:
    mcp_status: "connected"
    skill_count: 71
    active_profile: "default"
  
  reconciliation_loop:
    - name: "mcp_health_check"
      interval: 30s
      action: "reconnect if disconnected"
    - name: "skill_integrity"
      interval: 60s
      action: "rollback if corrupted"
```

**關鍵洞察**：Hermes 應該把「期望狀態」描述清楚，控制平面自動 reconcile。

### 2. 水平擴展 + HA

K8s control plane 是分散式、可水平擴展的：
- kube-apiserver 多實例 + LB
- etcd 用 Raft 3-node 或 5-node
- controller-manager HA failover

**對 Hermes 啟示**：MCP / Skill router / subagent dispatcher 也應該支援水平擴展。

### 3. Operator Pattern

Hermes 的 Skill + subagent 類似 Operator Pattern：
- **Skill definition** ≈ CRD
- **subagent execution** ≈ Custom Controller
- **reconciliation** ≈ Skill 自動載入/卸載

### 4. Admission Control 設計

Hermes 應該有類似 admission webhook 的機制：
- **mutating**：自動 context distillation
- **validating**：E-code 審計（不允許 E005/E009）

### 5. CRD 設計：Skill 系統

| K8s | Hermes |
|-----|--------|
| CRD | Skill yaml schema |
| CR | Skill instance |
| Operator | subagent 執行 skill |
| kubectl | Hermes trigger dispatch |

## 控制器設計經典模式

| K8s Controller Pattern | Hermes 對應 |
|----------------------|------------|
| Watch resources | trigger 監聽 |
| Reconciliation loop | subagent 並聯 |
| Status subresource | E-code 認證 |
| Finalizer | SOP 完整退出 |

## 為什麼 K8s Control Plane 是 Hermes 的最佳參考

### 三大核心相似

1. **Declarative + Reconciliation**：K8s 把 imperative → declarative，Hermes 也應該（high-level Plan + auto execution）。
2. **Self-healing**：K8s 自動 reconcile 失敗 Pod，Hermes 也應該 auto-rollback skill 失敗。
3. **API 為中心**：K8s 用 API 統一所有操作，Hermes 也應該用 trigger API 統一所有 Skill 調用。

## 核心洞察

```
Control Plane = API + Reconciliation Loop + State Store

K8s:
- API = kube-apiserver
- Loop = controllers
- Store = etcd

Hermes:
- API = trigger dispatch
- Loop = subagent 並聯
- Store = ~/.hermes state
```

## 引用

```bibtex
@online{cloudoptimo2026k8s,
  title={Inside Kubernetes: The 2026 Architecture Breakdown},
  author={CloudOptimo},
  year={2026},
  url={https://www.cloudoptimo.com/blog/inside-kubernetes-the-2026-architecture-breakdown/}
}
```

## 資源

- [CloudOptimo - Inside Kubernetes: 2026 Architecture](https://www.cloudoptimo.com/blog/inside-kubernetes-the-2026-architecture-breakdown/)
- [Kubernetes Official](https://kubernetes.io)
- [CNCF Annual Survey 2025](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/)
- [Operator SDK](https://sdk.operatorframework.io)
