---
title: Working Effectively with Legacy Code
created: 2026-07-09
updated: 2026-07-09
uid: e-42bc07baccb6
type: entity
subtype: book
author: Michael Feathers
year: 2004
publisher: Prentice Hall
pages: ~450
isbn: "0131177052"
tags: [legacy-code, refactoring, testing, software-maintenance, technical-debt]
confidence: high
status: wiki-entity-only
---

# Working Effectively with Legacy Code — Michael Feathers

## About Michael Feathers
Michael Feathers 是 Object Mentor（前身為 Crystalix）顧問公司創始人。职业生涯专注遗留系统重构与测试文化。

## Core Contribution: The Legacy Code Definition

> **Legacy code is code without tests.**

定義的關鍵不是時間，而是可測試性。沒有測試覆蓋的代碼就是 legacy code。

## Core Techniques (Book Summary)

### 1. Sensing and Separation（感知與分離）
在不改變代碼的情況下，觀察系統行為。
- 插入日誌/打印語句
- 透過 debugger 逐步執行
- 利用 profiler 了解調用模式

### 2. Characterization Tests（特徵測試）
「我不知道這段代碼應該做什麼，但我知道它現在在做什麼。」

步驟：
1. 寫一個會失敗的測試
2. 運行它，看它怎麼失敗
3. 將測試的斷言設為「當前行為」（即使錯了）
4. 這樣文檔化了現有行為 → 防止重構時意外破壞

### 3. The Seams Model（接縫模型）
Seam = 能夠在不改變其他地方的情況下改變行為的點。

類型：
- **Link Seam**（連結接縫）：透過不同對象替換
- **Preprocessing Seam**（預處理接縫）：條件編譯
- **Object Seam**（對象接縫）：依賴注入/子類覆寫

### 4. Dependency-Breaking Techniques（依賴斷裂技法）

| 技法 | 描述 |
|------|------|
| **Sprout Method** | 在原方法外新增新行為，舊行為不動 |
| **Wrap Method** | 用新方法包裝舊方法，在調用前後加入邏輯 |
| **Extract Method** | 從大方法中提取小方法以便隔離測試 |
| **Pull Up Dependency** | 將依賴作為參數傳入，而非直接創建 |
| **Subclass and Override** | 透過子類覆寫 mock 行為 |
| **Adapt Parameter** | 為外部依賴寫 wrapper/interface |

### 5. Influence vs. Effect
- **Effect** = 觀察得到的行為變化
- **Influence** = 為達到 Effect 而對代碼做的修改

 Legacy code 問題：很難只引入 Influence 而不產生不可預期的 Effect。

## Hermes 應用

- Hermes 有 ~17k tests 覆蓋核心模組，但 `hermes_cli/` 和 `gateway/` 部分模組測試覆蓋有限
- Characterization tests 概念可直接應用：capture 現有行為再重構
- 接縫模型幫助識別可以在不破壞的情況下修改的點
- `systematic-debugging` skill 的 4-phase 流程與 Feathers 方法互補
- `sop-design-maintenance-errors` skill 記錄維護教訓

## See Also
- [[software-testing-maintenance]] — software testing and maintenance concepts
- [[debugging]] — debugging techniques
- [[software-testing-fundamentals]] — testing fundamentals
