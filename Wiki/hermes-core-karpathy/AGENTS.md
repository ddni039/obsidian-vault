---
UID: 20260610-hermes-agents
STATUS: Active
TYPE: Logic
---

# Hermes AGENTS

## 1. Summary
> 開發指南捷徑。完整內容：`~/.hermes/hermes-agent/AGENTS.md`。

## 2. Assumptions & Invariants
* [ ] Hermes 原始碼位於 `~/.hermes/hermes-agent/`
* [ ] `run_agent.py` 是 AIAgent 核心對話迴圈
* [ ] 工具透過 `tools/registry.py` 自動發現

## 3. Implementation

### 關鍵檔案

| 檔案 | 職責 |
|------|------|
| `run_agent.py` | AIAgent 核心（~12k LOC）|
| `model_tools.py` | 工具發現與調度 |
| `toolsets.py` | Toolset 定義 |
| `cli.py` | 互動式 CLI（~11k LOC）|
| `hermes_state.py` | SQLite session store（FTS5）|
| `hermes_cli/` | CLI 子命令、config、setup |

### 工具鏈

```
tools/registry.py    ← 啟動時自動 import
        ↑
tools/*.py           ← 每個工具呼叫 registry.register()
        ↑
model_tools.py       ← 觸發發現
        ↑
run_agent.py, cli.py ← 消費工具
```

### Slash Commands

Registry：`hermes_cli/commands.py`（CommandDef）
所有消費者（autocomplete、Telegram menu、Slack）皆從此衍生。

## 4. Verification

| 檢查 | 指令 |
|------|------|
| 原始碼存在 | `test -f ~/.hermes/hermes-agent/AGENTS.md` |
| 核心檔存在 | `ls ~/.hermes/hermes-agent/*.py` |
| 測試通過 | `cd ~/.hermes/hermes-agent && python -m pytest tests/ -q` |

## 5. Changelog

* `2026-06-10`: 初始版本 — 關鍵檔案地圖到此版本