---
title: xUnit Test Patterns — Gerard Meszaros
created: 2026-07-09
updated: 2026-07-09
uid: e-3de01b4dbb1a
type: entity
subtype: book
author: Gerard Meszaros
year: 2007
publisher: Addison-Wesley
pages: ~900
isbn: "978-0131495050"
tags: [testing, xunit, test-patterns, refactoring, test-quality]
confidence: high
status: wiki-entity-only
---

# xUnit Test Patterns — Gerard Meszaros

## About the Author
Gerard Meszaros 是敏捷教練，曾參與多個大型敏捷項目，擅長測試自動化與重構。

## Core Problem the Book Solves

> Most developers have learned to write tests, but don't know when their tests have gone bad.

書的目標不是教你如何寫測試，而是教你**如何知道測試壞了**、**為什麼壞了**、**怎麼修**。

## Key Concepts

### 1. Test Smells（測試壞味道）

壞測試症狀分類：

**代碼層面 (Code-level)**
| Smell | 症狀 | 修復 |
|-------|------|------|
| **Duplicated Test Code** | 多個測試重複相同設置邏輯 | Extract Method → `setUp()` |
| **Test Logic in Production Code** | 測試邏輯滲透進生產代碼 | 隔離測試與生產代碼職責 |
| **Hard-coded Expectations** | 期望值寫死在測試裡 | Data-driven testing |
| **Obscure Test** | 意圖不清的測試 | Name tests clearly |

**行為層面 (Behavior-level)**
| Smell | 問題 |
|-------|------|
| **Fragile Test** | 實現細節變了就失敗 |
| **Erratic Test** | 有時通過有時失敗（非確定性）|
| **Slow Test** | 測試套件過慢影響反饋速度 |
| **Conditional Test Logic** | `if`/`skip` 在測試裡 |
| **Silent Test** | 測試失敗不報告 |

### 2. The Four Stages of a Test

```
[FIXTURE SETUP] → [EXERCISE SUT] → [VERIFY RESULTS] → [FIXTURE TEARDOWN]
     (Given)          (When)           (Then)
```

每個階段職責要分明，不能混淆。

### 3. Test Strategy Patterns

- **Result Verification**：驗證行為結果（推薦）
- **State Verification**：驗證對象狀態
- **Behavior Verification**：驗證交互順序（mock/stub）
- **Delta Verification**：驗證變化量

### 4. Fixture Strategies

| Pattern | 適用場景 |
|---------|---------|
| **Inline Setup** | 簡單對象，無共享 |
| **Delegated Setup** | 通過 helper 方法設置 |
| **Implicit Setup** | 使用 `setUp()` 鉤子 |
| **Create Once, Use Many** | 昂貴 fixture，所有測試共享 |
| **Lazy Setup** | 按需創建 fixture |

### 5. Test Double Patterns（測試替身）

- **Dummy Object**：只填充參數，不使用
- **Test Stub**：提供預先定義的回應
- **Test Spy**：記錄調用信息用於驗證
- **Mock Object**：預設期望，主動驗證交互
- **Fake Object**：簡化實現（in-memory DB）

> 不要用 mock 驗證實現細節；用 mock 隔離外部依賴。

### 6. Lessons Learned

1. **測試是**規範，不是實驗
2. **測試壞了**比沒有測試更危險——它給你錯誤的安全感
3. **測試隔離**意味著：一個測試失敗不應該導致另一個測試失敗
4. **測試速度**是紀律：每個功能完成的快速反饋依賴它
5. **壞味道**是預警系統——早發現早處理

## 與 Hermes 相關

Hermes 的 `scripts/run_tests.sh` 解決了 Meszaros 的多個測試壞味道：

| Hermes 做法 | 對應 Pattern |
|------------|-------------|
| Subprocess-per-test-file 隔離 | 測試隔離（Erratic Test 防治）|
| Temp HERMES_HOME | Implicit Setup（隔離狀態）|
| CI-parity（TZ=UTC, LANG=C.UTF-8）| 消除非確定性（Flaky Test 防治）|
| `-n auto` xdist 並行 | Slow Test 優化 |
| No change-detector tests | Fragile Test 防治（不測實現細節）|

## See Also
- [[software-testing-fundamentals]] — testing fundamentals
- [[software-testing-maintenance]] — testing and maintenance
- [[debugging]] — debugging techniques
- [[working-effectively-with-legacy-code]] — fixing untested code
