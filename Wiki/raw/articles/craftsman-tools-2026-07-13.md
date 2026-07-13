---
title: 工匠聖經 — Clean Code + TDD + Refactoring 整合
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book-summary, software-craftsmanship, clean-code, tdd, refactoring, uncle-bob, kent-beck, martin-fowler, hong-jiang, builder]
urls:
  - https://www.oreilly.com/library/view/clean-code-a/9780135398586/
  - https://martinfowler.com/bliki/TestDrivenDevelopment.html
  - https://www.amazon.com/Test-Driven-Development-Addison-Wesley-Signature/dp/0321146530
license: Commercial book summaries + O'Reilly + Martin Fowler official bliki
audience: Hong-jiang (Builder) profile — software craftsmanship, code quality, testing, refactoring
---

# 工匠聖經 — Source Material

> 整合 3 本工匠類核心書籍：Clean Code 2nd ed.（2024）+ TDD By Example（Kent Beck，2003）+ Refactoring（Fowler, 1999/2018）
> 與既有 `entities/pragmatic-programmer.md`、`entities/working-effectively-with-legacy-code.md`、`entities/xunit-test-patterns.md` 共同形成「工匠聖經六本套」。

## 書 1：Clean Code: A Handbook of Agile Software Craftsmanship（2nd Edition）

### 基本資訊

| 項目 | 內容 |
|------|------|
| **書名** | Clean Code: A Handbook of Agile Software Craftsmanship (2nd Edition) |
| **作者** | Robert C. Martin（Uncle Bob）|
| **初版** | 2008（1st edition，2009-08-01）|
| **二版** | 2024-12-31（ISBN: 9780135398586）|
| **初版頁數** | 464 |
| **出版** | Pearson / Prentice Hall |

### 4 大部分（2nd Edition 結構）

```
Part 1: Basic Coding Practices（基礎編碼實踐）
Part 2: Design Principles and Heuristics（設計原則與啟發）
Part 3: High-Level Architecture（高階架構）
Part 4: The Ethics of Craftsmanship（工匠倫理）
```

### 涵蓋的 10 大主題（2nd Edition）

1. 設計與架構原則（與編碼實踐整合）
2. 跨語言覆蓋（Java, JS, Go, Python, Clojure, C#, C）
3. 案例研究與代碼轉換練習
4. 命名、函數、物件、類別的技巧
5. 程式碼格式化（最大化可讀性）
6. 錯誤處理與測試實踐
7. **AI 工具的生產力使用**（2nd Edition 新增）
8. 軟技能與程式設計倫理
9. **SOLID 原則**（2nd Edition 新增）
10. 依賴管理、OOAD trade-off

### 17 章節涵蓋（基於 1st Edition + 2nd Edition 補充）

| 部 | 章 | 主題 |
|----|----|------|
| **Part 1** | 1 | Clean Code（品質定義）|
| | 2 | Meaningful Names |
| | 3 | Functions |
| | 4 | Comments |
| | 5 | Formatting |
| | 6 | Objects and Data Structures |
| | 7 | Error Handling |
| **Part 2** | 8 | Boundaries |
| | 9 | Unit Tests |
| | 10 | Classes |
| | 11 | Systems |
| | 12 | Emergence |
| **Part 3** | 13 | Concurrency |
| **Part 4** | 14-17 | Successive Refinement、Comparison、JUnit、Evolution |

### Clean Code 3 大原則

1. **可讀性優先**：code is read more often than written
2. **童子軍軍規**：leave the campground cleaner than you found it
3. **先正確再快**（Pragmatic 呼應）：make it work → make it right → make it fast

## 書 2：Test-Driven Development By Example（Kent Beck, 2003）

### 基本資訊

| 項目 | 內容 |
|------|------|
| **書名** | Test-Driven Development: By Example |
| **作者** | Kent Beck |
| **出版** | Addison-Wesley, 2003 |
| **ISBN** | 0321146530 |
| **頁數** | 240 |

### TDD 3 大步驟（Red-Green-Refactor）

```
RED          GREEN            REFACTOR
↓            ↓                ↓
Write       Make            Improve
a test     the test pass    the structure
that       (write          of both new
fails     only enough      & old code
           production
           code)
```

**Kent Beck 原話**（Martin Fowler bliki 引用）：
> "The most common way that I hear to screw up TDD is neglecting the third step. Refactoring the code to keep it clean is a key part of the process, otherwise we just end up with a messy aggregation of code fragments."

### TDD 關鍵效益

| 效益 | 說明 |
|------|------|
| **1. SelfTestingCode** | 永遠有 test → confidence in refactoring |
| **2. 分離接口/實作** | write test first → 想清楚 interface 後再用 |

### 4 大 TDD 章節

| 章節 | 主題 |
|------|------|
| Part I: Money | 範例驅動：multi-currency 開發 |
| Part II: xUnit | how to write test framework |
| Part III: Patterns | TDD-derived patterns（紅/綠燈可觀察）|
| Part IV: xUnit | 完整測試 framework |

### TDD 與 Clean Code 整合

```
Clean Code 強調: 童子軍軍規
TDD          強調: Refactor 是 TDD 第三步

=> 兩者整合：TDD 持續 自動讓 code 變 clean
```

### TDD Pitfalls

| 坑 | 解法 |
|----|------|
| Skipping refactor | **這是最常見的失敗** |
| Big tests | 寫 smaller tests |
| Slow tests | 重構 test 結構 |
| Testing implementation | 測 behavior，不測 detail |

## 書 3：Refactoring（Fowler, 1999 / 2018）

### 基本資訊

| 項目 | 內容 |
|------|------|
| **書名** | Refactoring: Improving the Design of Existing Code |
| **作者** | Martin Fowler + Kent Beck 等 10 人 |
| **1st** | 1999 |
| **2nd** | 2018-11-30（JavaScript + ES6）|

### Refactoring 的定義（Fowler）

> A change to the structure of software that does not change its observable behavior. Improves design, reduces complexity, helps understand.

### 兩個關鍵（2nd ed.）

1. **Refactoring 改變結構不改變行為**
2. **測試先行確保安全**（← TDD 整合）

### 核心目錄（2nd ed.）

| 章節 | 主題 |
|------|------|
| 1 | Refactoring, a First Example |
| 2 | Principles in Refactoring |
| 3 | Bad Smells in Code（22 smells）|
| 4 | Building Tests |
| 5 | Toward a Catalog of Refactorings |
| 6-12 | Refactoring 60+ pattern 目錄 |

### 22 大 Bad Smell（精選）

| Smell | 觸發 |
|-------|------|
| Duplicate Code | 兩個地方同樣 code |
| Long Method | 超過 10 行 |
| Large Class | 超過 300 行 |
| Long Parameter List | >3 個參數 |
| Divergent Change | 一個 class 多個原因改 |
| Shotgun Surgery | 一個 change 要改多處 |
| Feature Envy | method 用其他 class 資料 |
| Data Clumps | 同一群欄位重複出現 |
| Primitive Obsession | 用 primitive 而非 small object |
| Switch Statements | over-use of switch |
| Parallel Inheritance | 加 subclass 要兩處都加 |
| Speculative Generality | 過度泛化 |
| Temporary Field | 欄位只在某 case 用 |
| Message Chains | a.b().c().d() |
| Middle Man | class 只轉發 method |
| Inappropriate Intimacy | 兩個 class 太熟 |
| Alternative Classes with Different Interfaces | 同功能不同接口 |
| Incomplete Library Class | library 不夠用 |
| Data Class | 只有 field 無 method |
| Refused Bequest | subclass 不用 parent method |
| Comments | comment 過多掩蓋壞 code |
| Duplicate Observed Data | UI layer 不獨立 |
| Long Function Calls | parameter 過長 |

### 60+ Refactoring 名單（精選）

- Extract Method
- Inline Method
- Move Method
- Extract Class
- Inline Class
- Rename Variable/Function/Class
- Introduce Parameter Object
- Replace Magic Number with Symbolic Constant
- Replace Conditional with Polymorphism
- Replace Magic Literal with Constant
- Decompose Conditional
- Pull Up Method / Push Down Method
- Pull Up Constructor Body
- Replace Inheritance with Delegation

## 3 本書整合框架

```
Clean Code（規範）
    + TDD（自動化品質保證）
    = Refactoring（結構改進）
```

3 本書是**連續光譜**：

```
| 規範 | 自動保證 | 重構 |
| Clean Code | TDD | Refactoring |
| 「寫得好」| 「測過了」| 「改進了」|
```

### 各自負責的工匠問題

| 書 | 回答的問題 |
|----|-----------|
| Clean Code | 「什麼是好的程式碼？」|
| TDD | 「如何保證它持續好？」|
| Refactoring | 「如何把它從好變成更好？」|

## 工匠 6 本套（與原 wiki 整合）

| # | 書 | 類別 |
|---|----|------|
| 1 | Clean Code（Uncle Bob）| 規範 |
| 2 | TDD By Example（Kent Beck）| 自動化 |
| 3 | Refactoring（Fowler）| 結構 |
| 4 | The Pragmatic Programmer（已有）| 態度 |
| 5 | Working Effectively with Legacy Code（已有）| 現實 |
| 6 | xUnit Test Patterns（已有）| 細節 |

**3 + 3 = 工匠聖經全集**

## 對 Hermes「工匠」（Hong-jiang）的核心啟示

### Hong-jiang role 是什麼？

> Hong-jiang（工匠）= 執行 Plan 的子代理，負責 subagent 委派的實際編碼工作。

### 適用 Clean Code 哪些原則？

| Clean Code 原則 | Hermes 工匠對應 |
|----------------|---------------|
| Meaningful Names | Skill/SOP 命名用 kebab-case + 描述清楚 |
| Functions 簡短 | Skill entrypoint 應該 <100 行 |
| Comments 解釋「為何」 | SKILL.md description 解釋用途 |
| Error Handling | E-code 系統已建立 |
| Unit Tests | E 階段審計自動驗證 |

### 適用 TDD 哪些原則？

| TDD 原則 | Hermes 對應 |
|---------|------------|
| Red-Green-Refactor | SOP 寫 → 驗證 → 改進 |
| Test first | E 階段審計在部署前 |
| SelfTestingCode | TRAP-SOP 自動捕捉失敗 |
| Refactor in cycle | TRAP-SOP-051/052（Confirmation/Pre-mortem）|

### 適用 Refactoring 哪些？

| Bad Smell | Hermes 警告 |
|-----------|------------|
| Long Method | TRAP-SOP-024（Skill 250 行限制）|
| Large Class | TRAP-SOP-024（SKILL.md limit 250 行）|
| Duplicate Code | TRAP-SOP-023（Skill consistency）|
| Long Parameter List | Plan 範本 v1.1.1（7 個必填欄位 標準化）|

## 工匠日常工作流程

```
            Plan（文謀）
              ↓
        artisan_handoff（handoff pattern）
              ↓
        ┌─ Hong-jiang 工匠 ─┐
        │  Step 1: Read Clean Code rules   │
        │  Step 2: TDD (Write test plan)   │
        │  Step 3: Refactor before output   │
        └────────────────────┘
              ↓
        Yu-shi（御史）auditing
              ↓
        Production
```

## 引用

```bibtex
@book{martin2024cleancode,
  title={Clean Code: A Handbook of Agile Software Craftsmanship (2nd Edition)},
  author={Martin, Robert C.},
  year={2024},
  publisher={Pearson},
  isbn={9780135398586}
}

@book{beck2003tdd,
  title={Test-Driven Development: By Example},
  author={Beck, Kent},
  year={2003},
  publisher={Addison-Wesley},
  isbn={0321146530}
}

@book{fowler2018refactoring,
  title={Refactoring: Improving the Design of Existing Code (2nd Edition)},
  author={Fowler, Martin and Beck, Kent and others},
  year={2018},
  publisher={Addison-Wesley}
}
```

## 資源

- [Clean Code 2nd ed.（O'Reilly）](https://www.oreilly.com/library/view/clean-code-a/9780135398586/)
- [Test Driven Development（Martin Fowler bliki）](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
- [Test-Driven Development（Amazon）](https://www.amazon.com/Test-Driven-Development-Addison-Wesley-Signature/dp/0321146530)
- [The Pragmatic Programmer Wiki](https://pragprog.com/)
- [Working Effectively with Legacy Code](https://www.amazon.com/Working-Effectively-Legacy-Code-Michael/dp/0131177052)