---
title: System 1 / System 2 Thinking — Kahneman
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, kahneman, decision-making, cognitive-bias, two-systems, nobel-prize, wen-mou]
sources:
  - raw/articles/strategic-thinking-reading-list-2026-07-13.md
  - https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow
confidence: high
author: Daniel Kahneman（Nobel Prize in Economics 2002；Princeton）
---

# System 1 / System 2 Thinking

## 定義

**Kahneman 的兩個思維系統**——區分人類思考的兩種模式：

| 系統 | 速度 | 意識 | 用途 | 比例 |
|------|------|------|------|------|
| **System 1** | 快 | 自動、無意識 | 直覺、情緒、模式辨識 | **~95-96%** |
| **System 2** | 慢 | 深思、有意識 | 邏輯、推理、計算 | **~4-5%** |

## 核心發現

### System 1（直覺系統）

| 特徵 | 說明 |
|------|------|
| Speed | 非常快（毫秒級）|
| Effort | 零努力 |
| Consciousness | 無意識、自動 |
| Mode | 直覺、模式辨識 |
| Reliability | 容易出錯，但感覺自信 |
| Examples | 讀臉部表情、罵人、理解簡單句 |

### System 2（推理系統）

| 特徵 | 說明 |
|------|------|
| Speed | 慢（秒鐘到分鐘）|
| Effort | 需要集中注意力 |
| Consciousness | 有意識 |
| Mode | 邏輯、分析、計算 |
| Reliability | 較可靠但費力 |
| Examples | 數學計算、複雜推理、自我控制 |

## 認知偏誤（Cognitive Biases）

Kahneman 揭示的偏誤：

| 偏誤 | 說明 | 對「文謀」的影響 |
|------|------|----------------|
| **Anchoring** | 第一個數字影響後續判斷 | 初始報價影響 trade-off |
| **Availability heuristic** | 易想到的事被高估 | 近期事件過度影響決策 |
| **Framing effect** | 框架影響選擇 | 風險/收益的描述影響判斷 |
| **Sunk cost fallacy** | 沉沒成本謬誤 | 已投入的時間/金錢影響決策 |
| **Confirmation bias** | 確認偏差 | 只看支持自己觀點的證據 |
| **Loss aversion** | 損失規避 | 害怕損失大於追求收益 |
| **Endowment effect** | 禀賦效應 | 擁有什麼就高估什麼 |
| **WYSIATI** | What You See Is All There Is | 只看到已知的就以為全貌 |

## 與「文謀」的核心對應

| 文謀決策類型 | 應該用哪個系統 |
|-------------|---------------|
| **日常任務派發** | System 1（快速路由）|
| **架構選型** | System 2（深度 trade-off）|
| **Pattern 識別** | System 1（經驗）|
| **新技術評估** | System 2（slow 思考）|
| **緊急 Bug** | System 1（快速決策）|
| **重大技術決策** | System 2（slow 思考）|

**核心原則**：意識到何時要「slow down 用 System 2」——尤其在不熟悉的領域。

## 對 Hermes Wen-mou (Planner) 的應用

### Plan 階段的應用

```python
# System 2 觸發條件
should_use_slow_thinking = (
    impact == "high" OR
    uncertainty > threshold OR
    reversibility == "low"
)

if should_use_slow_thinking:
    activate_system_2()  # 觸發 Trade-off 分析
else:
    use_heuristics()  # 用 System 1
```

### 文謀關鍵決策原則

1. **Default to System 2 for architecture**（架構必須慢思考）
2. **Beware of WYSIATI**（不只是「目前看到的」）
3. **Avoid framing**（獨立評估風險和收益）
4. **Pre-mortem**（想像失敗 → 反推設計）
5. **Outside view**（基準率 vs 內部視角）

## 對 Hermes 系統設計的啟示

| Hermes 設計 | 對應 System |
|------------|------------|
| **Skill 路由（triggers）** | System 1（快速路由）|
| **Phase Lock 審計** | System 2（慢審核）|
| **SOP 規則** | System 1（慣例化）|
| **TRAP 規避** | System 2（學習來的）|
| **Daily cron 排程** | System 1（routine）|
| **異常 E-code** | System 2（switch 思考）|

## 為什麼這書對文謀重要？

| 價值 | 說明 |
|------|------|
| **自我覺察** | 認識到自己的偏誤 |
| **決策品質** | 知道何時要「慢下來」|
| **團隊管理** | 理解人心的非理性 |
| **量化基礎** | Kahneman 與 Tversky 的 prospect theory |
| **Nobel Prize** | 1979 + 2002 雙料得獎研究 |

## 引用

```bibtex
@book{kahneman2011thinking,
  title={Thinking, Fast and Slow},
  author={Kahneman, Daniel},
  year={2011},
  publisher={Farrar, Straus and Giroux},
  isbn={9780374275630},
  note={Nobel Memorial Prize in Economic Sciences (2002) - Behavioral Economics}
}
```

## 資源

- Wikipedia：[Thinking, Fast and Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)
- The Decision Lab：[System 1 and System 2 Thinking](https://thedecisionlab.com/reference-guide/philosophy/system-1-and-system-2-thinking)
- 書評：[Sue Behavioural Design](https://www.suebehaviouraldesign.com/en/blog/kahneman-thinking-fast-and-slow/)