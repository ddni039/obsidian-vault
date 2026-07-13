---
title: Progressive Disclosure (Agent Skills Pattern)
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, design-pattern, skill-system, claude-code, progressive-disclosure]
sources:
  - raw/articles/agent-skills-anthropic-course-2026-07-13.md
related:
  - "[[agent-skills-with-anthropic-course]]"
  - "[[hermes-skill-system]]"
  - "[[agent-harness]]"
confidence: high
---

# Progressive Disclosure (Agent Skills Pattern)

## 定義

**Progressive Disclosure** = 分階段揭露資訊，agent 只在需要時才載入完整內容。

這是 **Anthropic Skills 系統**的核心設計模式。

## 三階段揭露

```
┌─────────────────────────────────────────┐
│ Layer 1: Metadata（總是載入）           │
│   name, description, tags              │
│   → LLM 用於 routing 決策               │
└──────────────┬──────────────────────────┘
               │ agent 真正呼叫 skill
               ▼
┌─────────────────────────────────────────┐
│ Layer 2: SKILL.md 全文（按需載入）      │
│   YAML frontmatter + markdown body     │
│   → LLM 開始執行 skill 任務             │
└──────────────┬──────────────────────────┘
               │ 進一步深入需要
               ▼
┌─────────────────────────────────────────┐
│ Layer 3: references/ + assets/         │
│   scripts, templates, examples         │
│   → 完整 SOP / 範例 / 工具              │
└─────────────────────────────────────────┘
```

## 三個關鍵特性

### 1. Token Economy
- LLM prompt 只包含 skill **metadata**（~100 tokens）
- 完整 SKILL.md 只在需要時載入
- references/ 進一步按需揭露

### 2. Routing Accuracy
- description 是 routing 的核心
- 必須含「when to use」才能精準路由

### 3. Skill Independence
- Skill 之間不相依
- 每個 skill 可獨立更新

## 與 Hermes Skill 系統的對應

| Anthropic Skills | Hermes Skills | 評估 |
|----------------|---------------|------|
| Layer 1 metadata | frontmatter（name/description/tags）| ✅ |
| Layer 2 SKILL.md | SKILL.md 全文 | ✅ |
| Layer 3 references/ | references/ + scripts/ | ✅ |
| Progressive loading | hooks 系統按需載入 | ✅ 概念對應 |
| description routing | triggers keyword matching | ✅ |

## Hermes 的 progressive disclosure 優勢

### 已實作

- SKILL.md <250 行（薄主檔）
- references/ 章節化（按主題拆分）
- frontmatter 必填欄位（uid/status/version/tags/description）

### 待驗證

- **skill_view(name) 是否真的 lazy-load？**（LLM 層面的 progressive）
- **description 是否真的精準 routing？**（可從 LLM 觸發率分析）

## 對 Hermes 的建議

### 立即可行

1. **建立 skill metadata 索引檔**：把所有 skill 的 name+description 集中索引，加快 routing
2. **監控 skill 載入頻率**：識別哪些 skill 經常被載入到 Layer 3

### 設計層面

1. **保留 `references/` 結構**（已實作 ✅）
2. **禁止 SKILL.md > 250 行**（已實作 ✅）
3. **description 必含「when to use」**（已部分實作）

## 為何這個模式對 Hermes 至關重要

Hermes 已有 **185+ 顆 skill**（其中 29 顆是 hermes 自有），如果全部載入會：
- 浪費大量 tokens
- 容易導致 context rot
- routing 不精準

**Progressive disclosure 是 skill 系統規模化的必要設計**。

## 來源

- Andrew Ng × Anthropic 課程 L1-L2
- agentskillsdev.com 課程筆記
- Anthropic Skills 官方設計原則