---
title: Pragmatic Programmer Tips — Hunt & Thomas 核心法則
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [pragmatic-programmer, software-craft, tips, craftsmanship, best-practices]
source: "[[pragmatic-programmer]] | Andy Hunt & Dave Thomas
---

# Pragmatic Programmer Tips — Hunt & Thomas 核心法則

## 定位

《The Pragmatic Programmer》20 個 Tips 的精煉解讀，源自軟體工藝（Software Craftsmanship）運動的基石文獻。Hunt & Thomas 的核心立場：**每個程式設計師都是工匠，每段代碼都是個人Craft的表達**。

## 20 Tips 分類地圖

### Category 1：前期投資（Early Investment）

| Tip | 標題 | 核心 |
|-----|------|------|
| Tip 1 | Care About Your Code | 投入感是品質前提 |
| Tip 2 | Think! About Your Work | 主動思考，而非被動回應 |
| Tip 3 | You Have to Finish It | 「 Almost Done」是謊言 |
| Tip 4 | Build Modular Software | 模組化減少改動成本 |
| Tip 5 | Work in Short Bottlenecks | 減少等待瓶頸 |
| Tip 6 | Don't Use Envy to Prioritise | 別用「技術酷度」排序需求 |

### Category 2：代碼撰寫（Code Craft）

| Tip | 標題 | 核心 |
|-----|------|------|
| Tip 7 | Make It Work, Then Make It Right | 先讓它跑，再追求優美 |
| Tip 8 | Don't Repeat Yourself (DRY) | 知識只在一處表達 |
| Tip 9 | Eliminate Effects Between Things | 減少副作用 / 隔離變化源 |
| Tip 10 | Use the Power of Command Shells | 善用命令列工具 |
| Tip 11 | Use a Single Editor Well | 精通一個編輯器 |
| Tip 12 | Always Use Source Code Control | 永遠用版本控制 |
| Tip 13 | Debugging Mindset | 偵錯心態：假設不是事實 |
| Tip 14 | Fix the Problem, Not the Blame | 修補問題，不是修補情緒 |
| Tip 99 | Don't Assume It — Prove It | 不要假設 — 證明它 |

### Category 3：知識組合（Knowledge Portfolio）

| Tip | 標題 | 核心 |
|-----|------|------|
| Tip 15 | Learn a New Language Every Year | 每年學一個新語言 |
| Tip 16 | Read Books About Other Projects | 閱讀他專案的書籍 |
| Tip 17 | Attend Conferences and Meetups | 參加技術社群 |
| Tip 18 | Follow Industry News | 追蹤技術趨勢 |

### Category 4：溝通與協作（Communication）

| Tip | 標題 | 核心 |
|-----|------|------|
| Tip 19 | Write Code Every Day | 每天寫代碼 |
| Tip 20 | Communicate and Collaborate | 溝通是技術能力的一部分 |

## 最重要的 5 個核心 Tip

### Tip 8: DRY — Don't Repeat Yourself

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

違反 DRY 的代價：
- 同一知識在 N 處重複 → N 處要同步改動
- 忘記改其中一處 → Bug
- **Software Bubble**（泡泡）：一個地方改了，其他地方忘記改

**Hermes 例子**：
- 同一個 Convention 同時寫在 AGENTS.md、CLAUDE.md、.cursorrules → DRY 破壞
- Skill 文件的 frontmatter schema 應該只有一個 source of truth

### Tip 99（原書 Tip 24）: Eliminate Effects Between Things

模組化的物理意義：
- 每個模組**封裝**自己的知識
- 模組之間只通過**穩定介面**互動
- 內部改動不應該讓其他模組知道

**好**：物件的內部狀態是 private，改了不影響外部
**壞**：全域變數、單例（Singleton）讓 N 個模組隱式耦合

### Tip 13（原書 Tip 8）: Debugging Mindset

>调试的心态：相信代码有问题，而不是你的脑有问题。

步驟：
```
1. 观察 → 什麼情況下 Bug 出現？
2. 形成假設 → 我認為代碼哪裡做錯了？
3. 演繹 → 如果假設成立，會有什麼其他症狀？
4. 驗證 → 檢驗其他症狀是否存在
5. 修復 → 只修假設成立的那個原因
```

### Tip 7（原書 Tip 21）: Make It Work, Then Make It Right

```
第一步（Make It Work）：
  讓功能正確，用任何手段達成目標
  這個階段不要優化

第二步（Make It Right）：
  重構代碼，提升設計品質
  保持測試覆蓋

第二步（Make It Fast）：
  效能優化
  基於 profiling 數據，而非直覺
```

### Tip 14（原書 Tip 40）: Fix the Problem, Not the Blame

> It doesn't matter whether the bug is your fault or someone else's. It is still your problem.

## 與其他書籍的整合

| PragProg Tip | 對應概念 |
|-------------|---------|
| DRY | Meszaros 的「壞味道」：旣碼重複（Duplicated Code）|
| Eliminate Effects | Feathers 的「接縫模型」|
| Don't Assume It — Prove It | Butcher 的「系統化偵錯」第一步 |
| Modular Software | NIST 研究：模組化降低 Bug 修復成本 |
| Make It Work, Then Make It Right | Feathers Characterisation Tests 先 capture 再重構 |

## Hermes 應用

| PragProg 觀念 | Hermes 對應 |
|--------------|-----------|
| DRY | SOUL/AGENTS/CODEX/RULES 分層邊界 — 知識只在一層表達 |
| Eliminate Effects | 三關串流機制（C→B→H→H′→E）防止職責混雜 |
| Don't Repeat Yourself | `sop-design-maintenance-errors` TRAP 防止重複犯錯 |
| Proof Before Assumption | 御史 Core（H′）的第一個死穴：邏輯完整性核查 |
| Daily Coding | `sop-design-maintenance-errors` 每次作業後記錄教訓 |

## 關聯

- [[pragmatic-programmer]] — Hunt & Thomas 原書 entity
- [[working-effectively-with-legacy-code]] — Feathers 接縫模型
- [[debugging]] — Butcher 系統化偵錯
- [[xunit-test-patterns]] — Meszaros 測試壞味道
