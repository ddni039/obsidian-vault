---
title: Surgical Changes
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [guideline, llm, coding-practice]
sources: [raw/articles/karpathy-llm-wiki-2026.md]
---

# Surgical Changes

**核心原則：只碰需要碰的，清理自己造成的爛攤子。**

## 具體要求

### 編輯既有程式碼時
- 不「改善」相鄰的程式碼、註解、格式
- 不重構沒有壞的東西
- 配合現有風格，即使你會用不同方式
- 發現無關的死程式碼：提出來，不刪除

### 你的變更造成孤兒時
- 移除因你的變更而閒置的 import/變數/函式
- 不移除既有的死程式碼（除非被要求）

## 測試標準

**每個變更的行都應該可以直接追溯到使用者的請求。**

## 與文謀的對齊

[[文謀]] 的「精準擊發」：只改必須改的，不改善沒壞的。兩者精神一致——避免「好意改進」變成「意外破壞」。

## 相關原則

- [[Simplicity First]] — 最小化思維
- [[Think Before Coding]] — 動手前先想清楚
- [[Goal-Driven Execution]] — 目標驅動驗證
