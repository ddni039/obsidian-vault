---
title: Agent Skills with Anthropic — Andrew Ng × Anthropic (2026)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [course, agent-skills, claude-code, anthropic, andrew-ng, progressive-disclosure]
url: https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/
course_notes: https://agentskillsdev.com/en/
instructor: Elie Schoppik (Anthropic)
date: 2026
venue: DeepLearning.AI short course
levels: L0-L8 (9 lessons)
---

# Agent Skills with Anthropic — Source Material

## 課程概覽

**Andrew Ng × Anthropic** 官方合作課程，由 Elie Schoppik（Anthropic）教授：
- **9 堂課**（L0-L8）
- **核心主題**：如何為 Claude 建立 reusable Skills
- **整合主題**：Skills + MCP + Subagents
- **應用範圍**：Claude.ai / Claude Code / Claude API / Agent SDK

## 課程結構

| Level | 主題 |
|-------|------|
| **L0** | Course intro · Skills, progressive disclosure |
| **L1** | Why Skills — part 1 · SKILL.md format |
| **L2** | Why Skills — part 2 · Progressive disclosure in depth |
| **L3** | Skills vs Tools, MCP, Subagents |
| **L4** | Built-in Skills explored |
| **L5** | Creating custom Skills |
| **L6** | Skills with Claude API |
| **L7** | Skills with Claude Code |
| **L8** | Skills with Agent SDK |

## 核心概念：Progressive Disclosure

Skills 系統使用**漸進式揭露**機制：
1. LLM 只看到 Skills 的 metadata（name + description）
2. 真正呼叫時才載入完整 SKILL.md
3. 進一步需要時才載入 references/

**這個模式與 Hermes 的 Skill 系統完全一致**（hooks/skill_view 只載入 metadata，deep dive 才讀 references）。

## Claude Code 架構（基於 source code 分析）

- **512K+ lines TypeScript** in **1,884 files**
- 8 大核心子系統：
  1. Entry Layer
  2. Query Engine
  3. Tool System
  4. Command System
  5. Permission System
  6. Multi-Agent Coordination
  7-8. (其他子系統)

## 與 Hermes Skill 系統的精準對應

| Anthropic Skills | Hermes Skills | 評估 |
|----------------|---------------|------|
| SKILL.md | `~/.hermes/skills/<name>/SKILL.md` | ✅ 完全對應 |
| description (frontmatter) | description (YAML) | ✅ |
| Progressive disclosure | hooks 系統按需載入 | ✅ 概念一致 |
| Skills vs Tools | MCP tools | ✅ |
| Skills vs MCP | MCP servers | ✅ |
| Skills vs Subagents | `delegate_task` | ✅ |
| Built-in Skills | 內建 skills/ | ✅ |

## Anthropic Skills 的 frontmatter 標準

```yaml
---
name: [required]
description: [required]  # 必須含 when to use
---
```

## Hermes 的 SKILL.md 標準（更嚴格）

```yaml
---
uid: 20260101-skill-name-v1.0.0
name: skill-name
status: active
version: 1.0.0
tags: [tag1, tag2]
description: "完整描述"
---
```

**差異**：
- Hermes 多了 `uid`（用於 SSoT 唯一識別）
- Hermes 有 `status`（active / deprecated）
- Hermes 有 `version`（semver）
- Hermes frontmatter 規格更嚴格（4 必填欄位）

## 對 Hermes 的啟示

| 行動 | 理由 |
|------|------|
| 研究 Anthropic 的「progressive disclosure」演算法 | 優化 skill 載入效能 |
| 借用「Skills vs Tools vs Subagents」決策表 | 完善 Hermes 的 skill 選擇 SOP |
| 參考 Claude Code 8 子系統架構 | 設計 Hermes 架構時的參考 |