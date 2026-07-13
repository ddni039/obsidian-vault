---
title: xUnit Test Patterns — Gerard Meszaros 測試壞味道與重構
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [xunit-test-patterns, test-smells, test-doubles, characterization-tests, refactoring]
source: "[[xunit-test-patterns]] | Gerard Meszaros
---

# xUnit Test Patterns — Gerard Meszaros 測試壞味道與重構

## 核心定位

xUnit Test Patterns 是關於**如何寫好測試**的百科全書。區別於：
- **Feathers**（《Working Effectively...》）：如何處理沒有測試的代碼
- **Butcher**（《Debug It!》）：如何系統化偵錯
- **Meszaros**：如何**不把測試寫爛**（以及如何修好它們）

## 測試壞味道（Test Smells）

### 1. Code Smells（代碼層次）

| 壞味道 | 症狀 | 修法 |
|--------|------|------|
| **Duplicated Test Code** | 多個測試重複相同的 arrange/act/assert | Extract Method → shared helper |
| **Complex Teardown** | teardown 超過 10 行 | SUT 工廠方法 + automatic teardown |
| **Test Logic in Production Code** | 測試邏輯滲透進產品代碼 | 重構分界，測試邏輯留在測試層 |
| **Hard-coded Test Data** | 魔法數字散落各測試 | Test Data Builder pattern |
| **冗長的測試名稱** | `test_should_return_user_list_when_user_is_logged_in_and_database_is_connected` | 描述行為，不描述實現 |

### 2. Behavior Smells（行為層次）

| 壞味道 | 說明 | 代價 |
|--------|------|------|
| **Erratic Test** | 時好時壞，不穩定 | 失去對測試結果的信任 |
| **Slow Test** | 測試超過 1 分鐘 | 延遲 feedback cycle |
| **Fragile Test** | 業務邏輯沒變，但測試因無關原因失敗 | Change-detector tests |
| **Verbose Test** | 測試本身難以理解 | 維護成本高 |

### 3. Fragile Test 的子類（按失敗原因細分）

| 子類 | 觸發原因 |
|------|----------|
| **Brittle Test** | 介面/實作改了，但行為沒變 |
| **嘎嘎測試（嘎嘎,象聲詞）** | 隨機數/時間/順序依賴 |
| **別名測試** | 測試之間共享狀態，順序影響結果 |

## Test Double 模式

Test Double = 在測試中取代真實相依物的替身。

| 角色 | 目的 | 何時用 |
|------|------|--------|
| **Dummy** | 填補參數槽，不使用 | 不想實際呼叫的參數 |
| **Fake** | 輕量假實作（in-memory DB）| 取代真實 DB/外部服務 |
| **Stub** | 提供固定回應 | 控制 SUT 的輸入 |
| **Spy** | 記錄誰呼叫了什麼 | 驗證互動次數/順序 |
| **Mock** | 期望＋驗證一體 | 驗證物件間契約 |

**重要區分**：
```
Stub：你告訴它「返回 X」
Mock：你驗證「Y 被 Z 方式呼叫了 N 次」
Fake：自己實作了一個簡化版（不驗證，只提供數據）
```

## Characterisation Test（特徵化測試）vs. Stub vs. Mock

```
Characterisation Test：
  目標 = 記錄代碼的實際行為（你不知道它是對是錯）
  階段 = 還沒有測試覆蓋的 legacy code
  語氣 = 「我不知道它做什麼，所以我先 capture」

Stub / Mock：
  目標 = 隔離 SUT，驗證預期行為
  階段 = 代碼已有測試覆蓋
  語氣 = 「我知道它應該做 X，我驗證它做了 X」
```

## 測試層次結構（Meszaros 的 4 層）

```
第4層：End-to-End Tests（E2E）
  目的：業務價值驗證
  速度：最慢（分鐘級）
  數量：少量

第3層：Integration Tests（整合測試）
  目的：跨組件介面
  速度：中（秒級）
  數量：中量

第2層：Unit Tests（單元測試）
  目的：最小可測試單元
  速度：快（毫秒級）
  數量：大量

第1層：Component Tests（元件測試）
  目的：隔離的類/模組
  速度：快
  數量：取決於架構
```

## 重構方向

### 走向「表達意圖的測試」

**Before（壞味道）**：
```python
def test_23():
    u = User()
    u.id = 1
    u.name = "a"
    db.save(u)
    r = u.find(1)
    assert r == u
```

**After（意圖表達）**：
```python
def test_user_persisted_and_retrievable():
    # Arrange: a user with known identity
    user = a_user().with_name("Alice")
    # Act: when we save and retrieve the user
    retrieved = user.save().find(user.id)
    # Assert: we get back the same user
    assert retrieved == user
```

### Test Data Builder Pattern

```python
# 壞：魔法數字
user = User(name="Bob", age=30, active=True, roles=["admin"])

# 好：Test Data Builder
user = UserBuilder().name("Bob").age(30).as_admin().build()

# 更好的 DSL
user = a_user().with_name("Bob").as_admin().build()
```

## 壞味道 → 重構映射（快速參考）

| 壞味道 | 立即修法 |
|--------|----------|
| Duplicated Test Code | `extract_method()` → 共享 helper |
| Complex Teardown | 用工廠方法管理 fixture lifecycle |
| Brittle Test（介面敏感）| 測試行為而非實作 |
| Erratic Test | 隔離測試，消除共享狀態 |
| Slow Test | 移到單元測試套件，定時跑 |
| Fragile Test | 移除絕對時間/隨機種子依賴 |
| Hard-coded Test Data | Test Data Builder |

## 與其他書籍的整合

| xUnit Pattern | 對應概念 |
|--------------|---------|
| Erratic Test | Feathers 的 Legacy Code 接縫 |
| Stub/Mock | Butcher 的假設-演繹法中的「隔離假設」|
| Fragile Test | AGENTS.md：「不要寫 change-detector tests」|
| Characterization Test | Feathers：先 capture 現有行為 |
| Test Pyramid（第2/3/4層）| Pezzè/Young 的測試金字塔 |

## Hermes 應用

| Meszaros 觀念 | Hermes 對應 |
|--------------|-----------|
| Erratic Test | subprocess-per-test-file 隔離 — 防止狀態共享 |
| Fragile Test | `tri-role-pipeline` 御史核查 — 防止無關改動觸發失敗 |
| Don't write change-detector tests | AGENTS.md 明確禁止 |
| Test Double | Plugin ABC mock points |
| Characterization Test | `sop-design-maintenance-errors` 每次記錄實際失敗模式 |

## 關聯

- [[xunit-test-patterns]] — Meszaros 原書 entity
- [[working-effectively-with-legacy-code]] — Feathers 接縫模型
- [[debugging]] — Butcher 系統化偵錯
- [[software-testing-maintenance]] — 測試維護概念
