---
title: "Continuous Integration & Automation Pipelines — Martin Fowler"
created: 2026-07-10
updated: 2026-07-10
type: entity
subtype: book
author: Martin Fowler
year: "2006 (CI article), 2018 (updated)"
publisher: martinfowler.com
pages: ~90000 chars (martinfowler.com article)
tags: [continuous-integration, automation-pipelines, testing, devops, quality]
source: "https://www.martinfowler.com/articles/continuousIntegration.html"
---

# Automation Pipelines — Martin Fowler (martinfowler.com)

## 核心定義

**持續整合（Continuous Integration, CI）**：
每次團隊成員將變更合併到主線時，由自動化建構（含測試）驗證，快速發現整合錯誤。

**自動化建構** = 軟體建構 + 自動化測試 + 異常通知
**Pipeline** = 從原始碼到可部署產品的自動化流程鏈

## CI 核心實踐（Martin Fowler 定義）

### 1. 所有人都將變更 commit 到主線（Mainline）
- 每天至少一次將個人分支合併回主線
- 減少分支分叉（branch divergence）
- 減少長期分支的整合痛苦

### 2. 自動化建構（Automate the Build）
- 建構是單一指令：`make`、`ant`、`maven`、`gradle`
- 建構包含：編譯 + 測試 + 部署前置
- 建構失敗時團隊停下來立即修復（破窗理論）

### 3. 自動化測試（Automate Tests）
- 單元測試：快速、隔離、確定性
- 整合測試：跨組件介面驗證
- 驗收測試：業務功能驗證

### 4. 每次 Commit 都觸發建構（Commit to Mainline Every Day）
- Commit 後立即執行 CI Server Pipeline
- 任何人收到失敗通知都有責任立即修復

### 5. 及時修復失敗的建構（Fix Broken Builds Immediately）
- 「破窗理論」：放任壞建構等於邀請更多缺陷
- 高風險：壞建構阻礙團隊所有人的工作

### 6. 保持建構快速（Keep the Build Fast）
- 完整 Pipeline < 10 分鐘目標
- 單元測試 < 1 分鐘（與 Meszaros 的「快遞測試」呼應）

### 7. 對生產環境克隆進行測試（Test in a Clone of Production）
- 環境一致性：開發/測試/預生生產盡可能相同
- 容器化（Docker）降低環境差異

## 建構 Pipeline 階段（典型設計）

```
Source → Build → Unit Tests → Integration Tests → System Tests → Deploy
```

| 階段 | 目標 | 典型時間 |
|------|------|----------|
| **Source** | Checkout + Dependency Install | 1-2 min |
| **Build** | Compile + Package | 1-5 min |
| **Unit Tests** | 快速單元測試 | 2-5 min |
| **Integration Tests** | API/DB/外部依賴 | 5-10 min |
| **System Tests** | 端到端場景 | 10-30 min |
| **Deploy** | Staging / Production | 5-15 min |

## Hermes Pipeline 類比

| CI 概念 | Hermes 對應 |
|---------|------------|
| Mainline branch | `main` branch — 所有變更最終彙入 |
| Commit hook | `pre-commit` / lint checks |
| CI Server | GitHub Actions / CircleCI |
| Unit Tests | `scripts/run_tests.sh`（subprocess-per-test-file）|
| Integration Tests | Gateway E2E tests |
| Build artifact | `.whl` / Docker image |
| Pipeline failure | `errors.log` + 通知 |

## 關聯

- [[xunit-test-patterns]] — Meszaros 單元測試模式
- [[software-testing-maintenance]] — 軟體維護與測試
- [[debugging]] — 偵錯技術
