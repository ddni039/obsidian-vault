---
title: PicoAgents
created: 2026-07-13
updated: 2026-07-13
uid: e-075a1dd7f6bc
type: entity
tags: [framework, library, multi-agent, python, open-source]
sources:
  - raw/articles/designing-multiagent-systems-book-2026-07-13.md
related:
  - "[[designing-multi-agent-systems-book]]"
  - "[[victor-dibia]]"
confidence: high
---

# PicoAgents

## 簡介

**PicoAgents** 是 Victor Dibia 在《Designing Multi-Agent Systems》書中**從零實作**的 lightweight multi-agent framework。它是書中所有概念的可執行程式碼展示。

**特色**：
- ✅ MIT License（書中用 Apache-2.0 repo 展示）
- ✅ 50+ runnable examples
- ✅ 完整 Web UI（`picoagents ui`）
- ✅ Streaming responses + real-time debug events
- ✅ OpenTelemetry 整合（Gen-AI semantic conventions）
- ✅ Workflow checkpoint system（file/memory storage backends）

## 安裝與啟動

```bash
# 從 GitHub clone
git clone https://github.com/victordibia/designing-multiagent-systems.git
cd designing-multiagent-systems/picoagents

# 安裝含 dev dependencies
pip install -e ".[dev]"

# 啟動 Web UI（含 auto-discovery）
picoagents ui
```

## 核心模組

### src/picoagents/
- **agents/** — Agent 類別（含 `Agent` 基礎類別、`as_tool()` pattern）
- **orchestration/** — Multi-agent 編排（sequencer / group chat / handoffs）
- **workflows/** — 工作流引擎（含 checkpointing）
- **memory/** — Memory tools
- **store/** — SQLModel persistence（SQLite/PostgreSQL）
- **llm/** — LLM clients（OpenAI、Anthropic、Azure、Gemini）
- **eval/** — Evaluation runner + LLM-as-judge
- **web/** — Web UI 後端

### tools/
- `claude_code_target.py` — ClaudeCode 整合（捕獲完整 tool trace）
- `llm_completion_check_hook.py` — End hook 用 LLM judge 驗證完成

## 與 Hermes 的對照

| PicoAgents | Hermes |
|-----------|--------|
| `Agent` 類別 | subagent via `delegate_task` |
| `Orchestrator` (group chat) | C 角色（Master）+ routing-check |
| `ToolMessage.metadata` | `fact_store` + `MEMORY.md` |
| Workflow checkpoint | `PHASE_LOCK_PDF.lock` + `craftsman_result.json` |
| `eval/judge.py` | E 階段御史（`auditor_core.py`） |
| Web UI（React） | Dashboard (:9119) + WebUI (:8648) |

## 為何對 Hermes 有價值

1. **範例程式碼庫**：50+ 真實 multi-agent 案例可參考
2. **評估方法論**：LLM-as-judge 模式可直接借鏡
3. **持久化設計**：SQLModel schema 提供 ORM 範本
4. **Web UI 模式**：React debug panel 值得 Dashboard 借鏡

## 來源

- GitHub：https://github.com/victordibia/designing-multiagent-systems/tree/main/picoagents
- 版本：v0.4.0（2026-02-11）
- Stars：703 ⭐ / Forks：181