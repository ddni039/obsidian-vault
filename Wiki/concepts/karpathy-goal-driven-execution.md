---
title: Goal-Driven Execution
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [guideline, llm, coding-practice]
sources: [raw/articles/karpathy-llm-wiki-2026.md]
---

# Goal-Driven Execution

**核心原則：定義成功標準，循環驗證直到確認。**

## 具體要求

將任務轉化為可驗證的目標：
- 「新增驗證」→ 「先寫無效輸入的測試，再讓它們通過」
- 「修復 bug」→ 「先寫能重現它的測試，再讓它通過」
- 「重構 X」→ 「確保重構前後測試都通過」

多步驟任務的標準格式：
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

## 強成功標準 vs 弱成功標準

| 類型 | 描述 | 效果 |
|------|------|------|
| 強 | 可獨立循環驗證 | 明確，減少來回 |
| 弱 | 「讓它能跑」 | 需要不斷確認 |

## 與御史的對齊

[[御史]] 的「嚴格驗證」：不接受「差不多」，需要可驗證的通過標準。兩者完全一致——Goal-Driven 是御史驗收原則的技術具象化。

## 相關原則

- [[Surgical Changes]] — 只碰必須碰的
- [[Think Before Coding]] — 事前預防
- [[Simplicity First]] — 最小化思維
