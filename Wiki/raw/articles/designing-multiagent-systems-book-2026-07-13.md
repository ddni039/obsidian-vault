---
title: Designing Multi-Agent Systems — Victor Dibia (2025)
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book, multi-agent, lvm-agent, parallel-execution, orchestration, victor-dibia]
url: https://multiagentbook.com/
github: https://github.com/victordibia/designing-multiagent-systems
license: Apache-2.0 (code) / All rights reserved (book content)
author: Victor Dibia, PhD (Microsoft Research, AutoGen author)
year: 2025
format: 15 chapters, 185+ code snippets, 46 diagrams, 395 pages
---

# Designing Multi-Agent Systems — Source Material

## 書籍基本資訊

- **作者**：Victor Dibia（Microsoft Research，AutoGen / AutoGen Studio / Agent Framework 作者）
- **副標**：Principles, Patterns and Implementation for AI Agents
- **規模**：15 章 / 185+ 程式碼片段 / 46 張手繪圖 / 395 頁
- **支援語言**：英、法、德、西、日、中（5 種翻譯版本同步）
- **配套 repo**：[victordibia/designing-multiagent-systems](https://github.com/victordibia/designing-multiagent-systems)（Apache-2.0，703 ⭐）
- **推薦語**：Andrew Ng（DeepLearning.AI）、Chi Wang（Google DeepMind）、Caitie McCaffrey（MCP Tech Lead, Microsoft）

## 四大結構部分

1. **Foundations** — 多 agent 系統基礎概念與設計模式
2. **Building** — 從零實作 `picoagents` framework（agents / tools / memory / workflows / orchestration）
3. **Evaluating & Optimizing** — 測試、衡量效能、規模化可靠系統
4. **Real-World Applications** — 完整案例：data analysis / software engineering / information processing

## 與 Hermes 直接相關的核心概念

### 1. PicoAgents：輕量 multi-agent framework

從零實作的 library（書中逐步建立）：
```python
from picoagents import Agent
from picoagents.llm import AzureOpenAIChatCompletionClient

def get_weather(location: str) -> str:
    weather_data = {"Seattle": "72°F, partly cloudy", "Paris": "65°F, sunny"}
    return weather_data.get(location, "70°F, clear")

agent = Agent(
    name="weather_assistant",
    description="A helpful weather assistant",
    instructions="You help users check the weather.",
    model_client=AzureOpenAIChatCompletionClient(...),
    tools=[get_weather],
)

async def main():
    async for event in agent.run_stream("What's the weather in Seattle?"):
        print(event)
```

### 2. Parallel Execution 的兩種策略（書中模式）

書中探討的並行模式：

- **Plan-level parallelism**：多個完整 plans 同時跑，第一個完成就終止（early termination）
- **Subtask-level parallelism**：在單一 plan 內平行處理 independent subtasks
- **Diversity encouragement**：透過不同 prompting 鼓勵多樣化解法

### 3. 評估與優化

- **LLM-as-judge**：用 LLM 評估其他 LLM 的輸出
- **Persistence layer**：SQLModel + SQLite/PostgreSQL 儲存 agent 執行記錄
- **OpenTelemetry integration**：Gen-AI semantic conventions
- **Tool approval workflow**：`@tool` decorator + `ApprovalMode`

### 4. 50+ Examples（按章節分類）

- `examples/agents/` — Basic agents, tools, memory, computer use（Ch 4-5）
- `examples/workflows/` — Workflow patterns（Ch 5）
- `examples/orchestration/` — Multi-agent coordination（Ch 6）
- `examples/evaluation/` — Evaluation patterns（Ch 8）

## 與現有 Wiki 概念的對應

| Victor Dibia 概念 | Hermes 對應 |
|------------------|-------------|
| Multi-agent orchestration | [[agency-multi-agent-architecture]]（Agency）、Hermes tri-role（[[文謀]]/[[工匠]]/[[御史]]） |
| Parallel plan execution | Hermes `delegate_task` + `background: true` 並聯 |
| Tool approval workflow | Hermes 的 Plan-Gate-Review 流程 |
| Persistence store | Hermes 的 `fact_store`（holographic memory）+ `MEMORY.md` |
| LLM-as-judge | Hermes 的 E 階段（御史） |

## 來源連結

- 書籍網站：https://multiagentbook.com/
- GitHub repo：https://github.com/victordibia/designing-multiagent-systems
- 免費 preview（45 頁）：https://multiagentbook.com/preview
- PicoAgents README：https://github.com/victordibia/designing-multiagent-systems/tree/main/picoagents
- 作者年終回顧：https://victordibia.com/blog/year-in-review-2025/

## Citation

```bibtex
@book{dibia2025multiagent,
  title={Designing Multi-Agent Systems: Principles, Patterns, and Implementation for AI Agents},
  author={Dibia, Victor},
  year={2025},
  url={https://buy.multiagentbook.com/},
  github={https://github.com/victordibia/designing-multiagent-systems}
}
```