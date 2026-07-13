---
title: Chain-of-Thought (CoT) Reasoning
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, llm-reasoning, chain-of-thought, prompting, wegoogle, wei-2022, hermes-intelligence]
sources:
  - raw/articles/hermes-intelligence-reading-map-2026-07-13.md
  - https://arxiv.org/abs/2201.11903
confidence: high
author: Jason Wei et al. (Google Research, 2022)
---

# Chain-of-Thought (CoT) Reasoning

## 定義

**Chain-of-Thought (CoT) Reasoning** = 一種 prompting 技術，透過讓 LLM 顯示推理中間步驟來提升 reasoning tasks 的表現。

> 不是直接給答案，而是讓 LLM「逐步思考」→ 突破 reasoning 能力的瓶頸。

## 論文資訊

| 項目 | 內容 |
|------|------|
| **標題** | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models |
| **作者** | Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Chi, Quoc Le, Denny Zhou（Google Research）|
| **發表** | NeurIPS 2022 |
| **arXiv** | 2201.11903 |
| **引用數** | **32,540 次**（Google Scholar）|
| **核心影響** | 開啟 LLM reasoning 研究熱潮 |

## 範例對比

```
Q: Roger 有 5 顆網球。他又買了 2 罐網球，每罐 3 顆。他現在有幾顆？

【No-CoT】（無推理）：
A: 11  （直接猜，可能錯）

【CoT】（有推理）：
A: Roger 一開始 5 顆。
   2 罐 × 3 顆 = 6 顆。
   5 + 6 = 11。
   所以 Roger 有 11 顆。
```

## 3 大核心原則

### 1. Decomposition（任務分解）
- 拆解複雜問題成多步子問題
- 每一步明確且可驗證

### 2. Intermediate Steps（中間步驟可見）
- 不要跳到結論
- 每步驟都有明確理由

### 3. Self-consistency（自洽性）
- 多個 CoT → 多個結果 → 投票取最一致

## 量化效果（PaLM 540B）

| 任務 | No-CoT | CoT | 提升 |
|------|--------|-----|------|
| GSM8K（算術推理）| 18% | **57%** | +39pp |
| Commonsense | 56% | **70%** | +14pp |
| Symbolic reasoning | 23% | **52%** | +29pp |

## CoT 演進樹

```
CoT (Wei et al. 2022)
  ├── Zero-shot CoT：「Let's think step by step」
  ├── Self-Consistency (Wang et al. 2022)
  │   └── 多樣本 + 多數決
  ├── Tree-of-Thoughts (Yao et al. 2023)
  │   └── 多分支 + 剪枝 + BFS/DFS
  ├── ReAct (Yao et al. 2022)
  │   └── Reasoning + Acting 交錯
  ├── Self-Refine (Madaan et al. 2023)
  │   └── 生成 → 自我批評 → 修正
  └── Reflexion (Shinn et al. 2023)
      └── 反思 + 長期記憶
```

## 對 Hermes 智能的核心應用

### 文謀 Plan 階段應用

```python
# 文謀 Plan 時啟用 CoT
plan = wmou_plan(
    goal="...",
    reasoning_chain=[
        "Step 1: 確認目標",
        "Step 2: 識別限制",
        "Step 3: 列出 3+ 方案",
        "Step 4: 評估 trade-off",
        "Step 5: 選擇 + 驗證"
    ]
)
```

### E-code + TRAP 學習

每次失敗產生 CoT：
```
E-code: E005 Plan failed
CoT trace:
  Step 1: 檢測到 ANCHORING bias
  Step 2: 應該用 3+ 方案
  Step 3: 評估外部基準率
Lesson: TRAP-SOP-050
```

### Subagent 規劃

```python
# Subagent 自動 CoT
def subagent_think(task):
    # Zero-shot CoT
    thought = llm("Let me think step by step about: " + task)
    action = llm("Given thought above, what's the best action?")
    return action
```

### RAG 增強

把 CoT reasoning 加入 RAG context：
```yaml
rag:
  retrieved_docs: [...]
  cot_steps:
    - "What does the user really want?"
    - "Which docs are most relevant?"
    - "How to combine them?"
  final_answer: ...
```

## 何時使用 CoT

| 任務 | 是否用 CoT |
|------|----------|
| 簡單事實查詢 | ❌ 不必 |
| 多步算術推理 | ✅ 必須 |
| 邏輯推論 | ✅ 必須 |
| 程式碼生成 | ✅ 強烈推薦 |
| 架構決策 | ✅ 必須 |
| 創意寫作 | ⚠️ 視情況 |
| 對話閒聊 | ❌ 不必 |

## 對 Hermes 系統設計的啟示

### 1. 顯式推理

Plan 階段應該顯示推理步驟（不是直接 action）：
```yaml
plan:
  user_goal: "提升 Hermes 智能"
  reasoning_steps:
    - "用戶希望升級 LLM 推理能力"
    - "這涉及 LLM reasoning 模型 + agent 架構"
    - "5 層架構需要全盤審查"
  actions:
    - "implement CoT"
    - "review 5 layer architecture"
```

### 2. Self-Consistency 投票

當前步驟選擇時，可以產生多個方案 → 投票：
```python
plans = [plan_strategy_1, plan_strategy_2, plan_strategy_3]
best = vote(plans)  # 多數決 / best-of-N
```

### 3. Self-Refine 機制

E-code 檢測失敗 → 自動 refine plan → 再執行：
```
Plan A → execute → fail with E-code
  ↓
Refine: identify failure mode, adjust
Plan A' → execute → success ✅
```

## 為什麼 CoT 對 Hermes 重要？

| 原因 | 說明 |
|------|------|
| **智能瓶頸突破** | Hermes 的智能層面受限於 LLM 推理能力 |
| **可解釋性** | 推理步驟可見，便於審計 |
| **錯誤定位** | 失敗時可以定位到哪一步 |
| **自我學習** | 正確的 CoT 可存入 fact_store |
| **業界標準** | 32,540 citations 是 LLM 推理必讀 |

## 引用

```bibtex
@article{wei2022chain,
  title={Chain-of-Thought Prompting Elicits Reasoning in Large Language Models},
  author={Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Chi, Brian and Le, Quoc and Zhou, Denny},
  journal={Advances in Neural Information Processing Systems (NeurIPS 2022)},
  year={2022},
  eprint={2201.11903},
  archivePrefix={arXiv}
}
```

## 資源

- [arXiv Paper](https://arxiv.org/abs/2201.11903)
- [Google Research Blog](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/)
- [Deep (Learning) Focus 分析](https://cameronrwolfe.substack.com/p/chain-of-thought-prompting-for-llms)