---
title: Simplicity First
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [guideline, llm, coding-practice]
sources: [raw/articles/karpathy-llm-wiki-2026.md]
---

# Simplicity First

**核心原則：最小化代碼，沒有投機性功能。**

## 具體要求

- 不做超出需求的 feature
- 單次使用的程式碼不抽象化
- 不提供「未被要求」的彈性或配置
- 不處理不可能發生的錯誤情境
- 200 行能做完就不要寫 200 行

## 自問

「資深工程師會說這太複雜了嗎？」如果會，簡化。

## 與文謀的對齊

[[文謀]] 的「精簡結構」：最小化、多思考、杜絕過度設計。兩者高度一致——Simplicity First 是文謀原則的技術具象化。

## 與工匠的張力

[[工匠]] 有時為了「通用性」或「擴展性」傾向添加抽象。Simplicity First 直接挑戰這種傾向——單次使用不抽象，沒有需求不擴展。

## 相關原則

- [[Think Before Coding]] — 動手前先想清楚
- [[Surgical Changes]] — 只碰必須碰的
- [[Goal-Driven Execution]] — 目標驅動驗證
