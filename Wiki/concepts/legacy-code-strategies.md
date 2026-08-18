---
title: Legacy Code Strategies — Michael Feathers 方法論
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [legacy-code, dependency-breaking, characterization-tests, refactoring, seams]
source: "[[working-effectively-with-legacy-code]] | Michael Feathers
---

# Legacy Code Strategies — Michael Feathers 方法論

## 核心定義

**Legacy Code** = 沒有測試覆蓋的代碼。

「Legacy code」不是「舊代碼」或「爛代碼」——而是「無法安全改動的代碼」。任何沒有自動化測試的代碼，在改動時都是在黑暗中摸索。

## 兩大核心問題

### 1. Sensing（感知）

在代碼外部觀察其內部行為。

問題：當你呼叫一個函式，你如何知道它實際做了什麼？
- 沒有測試，你只能靠猜測和運氣
- 對外行為不明確（side effects、副作用）

### 2. Separation（分離）

隔離依賴，獨立測試目標函式。

問題：要測 A 函式，但 A 依賴 B/C/D，全部耦合在一起，無法單獨測試。
- 資料庫依賴
- 網路服務依賴
- 時間/隨機數依賴

## 接縫模型（Seams）

**接縫** = 一個可以放進測試替代品的地方。

代碼中存在「接縫點」，可以在那裡注入測試替代（Test Double），讓你隔離目標函式。

```
原始呼叫：
  A() → B() → C() → D()

接縫點（在 B 之前）：
  A() → [接縫] → B() → C() → D()

測試時注入 Mock B：
  A() → [接縫] → MockB()  ← B 被替換，C/D 不需理會
```

### 接縫類型

| 接縫類型 | 說明 | 範例 |
|---------|------|------|
| **Object Seams** | 替換物件實例 | 依賴注入 |
| **Preprocessor Seams** | C/C++ 巨集替換 | `#define` |
| **Link Seams** | 替換已編譯目標檔 | 測試用 stub |
| **Function Pointers** | 函式指標注入 | 回調鉤子 |

## Characterisation Tests（特徵化測試）

### 定義

Capture 代碼的**實際行為**（不是你期望的行為），建立「現有事實快照」。

目標：記錄系統**實際做什麼**，而不是**應該做什麼**。

### 為什麼要先建 Characterisation Tests

1. 你不知道代碼的實際行為
2. 改動前需要知道「現狀」
3. Characterisation Tests = 代碼的「黑盒子日誌」
4. 改壞了測試會馬上告訴你

### Feathers 協議

```
1. Write a test that reveals the current behavior
2. Run it — it will FAIL (because you don't know the behavior yet)
3. Examine the output to understand what the code ACTUALLY does
4. Update the test to assert the ACTUAL behavior
5. Now you have a characterization test
6. When you refactor, the characterization test guards against regression
```

### Characterisation Test 範例

```python
# 不知道 foo() 實際行為，先建 test
def test_foo_returns_current_behavior():
    result = foo(input="test")
    # 此時不知道 result 是什麼
    # 執行，看實際輸出，然後 assert 那個實際值
    assert result == "actual_output_value"  # 這就是 characterization
```

## 依賴斷裂技術（Dependency-Breaking Techniques）

Feathers 書中列出 9 種打破依賴的技術：

### 1. Sprout Method（萌芽法）
症狀：要測的方法是現有函式中間一段邏輯。
解法：把那段邏輯提煉成新函式，對新函式獨立測試。

### 2. Wrap Method（包裝法）
症狀：無法在要測的函式中注入依賴。
解法：在呼叫點之前包裝一層，把依賴物件傳入。

### 3. Subclass and Override（子類覆寫）
```
class SUT:
    def helper(self): ...  # 要 mock 的依賴

class TestableSUT(SUT):
    def helper(self): return MockHelper()  # 覆寫
```

### 4. Extract and Override（提煉並覆寫）
把全域依賴的存取封裝成一個 protected/virtual 方法，然後子類覆寫。

### 5. Parameterise Constructor（參數化建構子）
將依賴物件傳入建構子，預設用真實依賴，測試時傳 mock。

### 6. Introduce Static setter（引入靜態 setter）
適用於無處不在的 Singleton：
```python
class ServiceLocator:
    _instance = None
    @staticmethod
    def set(instance): ServiceLocator._instance = instance
    @staticmethod
    def get(): return ServiceLocator._instance
```

### 7. Extract Interface（提取介面）
將依賴的具體類別抽象成介面，測試時注入 mock。

### 8. Fake It（假實作）
先寫一個滿足介面的假實作，讓系統能跑，之後再替換成真實實作。

### 9. Record/Playback
適用於外部服務依賴：測試時錄製實際回應，之後回放而不需要真實服務。

## 緊急修復 Legacy Code 的步驟

```
1. 確認要改動的位置
2. 用「特徵化測試」capture 現有行為
3. 找到最近的接縫點
4. 用依賴斷裂技術隔離目標代碼
5. 寫新的單元測試覆蓋預期行為
6. 小步改動 + 每次確認測試通過
7. 重構提升設計（以測試為保護網）
```

## Hermes 應用

| Feathers 技術 | Hermes 對應 |
|--------------|-----------|
| Characterisation Tests | `session_search` 捕捉現有對話行為 |
| 接縫模型 | Plugin ABC 系統（最小化核心改動）|
| 依賴斷裂 | Plugin Hook Registration 機制 |
| 快速確認 | `hermes logs` 即時觀察行為 |
| Sprout Method | 新功能 → 新 plugin / skill 而非改核心 |

## 關聯

- [[working-effectively-with-legacy-code]] — Feathers 原書 entity
- [[software-testing-maintenance]] — 軟體維護概念
- [[debugging]] — 偵錯技術
- [[xunit-test-patterns]] — Meszaros 測試壞味道
