---
title: Red-Green-Refactor (TDD Cycle)
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, tdd, red-green-refactor, kent-beck, test-driven, craftsmanship, hong-jiang, sdlc-cycle]
sources:
  - raw/articles/craftsman-tools-2026-07-13.md
  - https://martinfowler.com/bliki/TestDrivenDevelopment.html
related:
  - "[[software-testing-fundamentals]]"
confidence: high
---

# Red-Green-Refactor (TDD Cycle)

## 定義

**Red-Green-Refactor（紅綠重構）** = Kent Beck 在 *Test-Driven Development* (2003) 中提出的 3 步 TDD 循環。

> "三大步驟的簡單反覆：寫一個會失敗的測試，讓它通過，重構。"
> — Kent Beck

## 三大步驟

```
RED（紅）       GREEN（綠）       REFACTOR（重構）
  ↓                ↓                ↓
寫一個測試       寫 production code  改善結構
預期失敗        直到測試 pass       (保持測試全綠)
                                      不改變行為
```

## 為何這個循環有效？

| 步驟 | 解決 |
|------|------|
| **Red（測試先寫）** | 強制設計接口（而非先寫實作後補測試）|
| **Green（最小實作）** | 避免過度設計，只為通過測試 |
| **Refactor（重構）** | 在測試保證下，安全改進結構 |

## 4 個常見失敗

### 1. Skip refactor（最常見）
**Kent Beck**：「最常見的失敗是略過第三步。」
→ 結果：分散但不乾淨的代碼

### 2. 寫 Big Tests
寫太粗粒度 test → 失敗難定位
→ 寫 smaller tests

### 3. 寫 Slow Tests
測試太慢 → 開發者會 skip
→ 重構 test 結構

### 4. 測試 Implementation
測試「內部實現」而非「行為」
→ 一改實作就 fail，但行為沒變

## 對 Hermes 工匠（Hong-jiang）的應用

```
Hermes 工匠 TDD 對應：
  RED    →  E 階段審計（測試 TRAP 是否觸發）
  GREEN  →  套用 TRAP fix 自動驗證
  REFACTOR → Skill 改進（SOP 演進）
```

| TDD 步驟 | Hermes 對應 |
|---------|------------|
| Red test | E-code 觸發 |
| Green fix | TRAP-SOP repair |
| Refactor | SOP version 升級（v1.0 → v3.7）|

## Red-Green-Refactor 的現代變體

| 方法 | 差異 |
|------|------|
| **Refactor 優先** | 先寫 refactor plan，再 Red |
| **Outside-In TDD** | 從 API 開始 |
| **Property-based TDD** | 用 invariant 而非 example |
| **Mutation TDD** | 用 mutation test 驗證 test 品質 |

## 引用

- Kent Beck: TDD By Example (2003)
- Martin Fowler: TestDrivenDevelopment bliki (2023)

## 相關 SOP

- `references/craftsman-tools-sop.md`（工匠 SOP）
- TRAP-SOP-024：Skill <250 行
- TRAP-SOP-023：Skill consistency

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（Kent Beck TDD cycle + Hermes 工匠對應）|