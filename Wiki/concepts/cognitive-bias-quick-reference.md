---
title: Cognitive Bias Quick Reference（99 偏誤速查表）
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, cognitive-bias, decision-making, evaluation-bias, dobeli, kahneman, quick-reference]
sources:
  - raw/articles/thinking-in-bets-and-art-of-thinking-clearly-2026-07-13.md
related:
  - "[[system-1-system-2-thinking]]"
  - "[[wen-mou-plan-template]]"
confidence: high
---

# Cognitive Bias Quick Reference（99 偏誤速查表）

## 定義

**Cognitive Bias Quick Reference** = 基於 Rolf Dobelli 的《The Art of Thinking Clearly》整理的 **99 個認知偏誤速查手冊**，用於任何評估、決策、自我審視場景。

> 來自 Dobelli 「3-5 頁/偏誤」格式 + Kahneman 學術解釋 + Duke 實戰驗證 = **工程師用評估偏誤工具**。

## 為什麼需要速查表？

| 場景 | 若沒有速查表 | 若有速查表 |
|------|-------------|------------|
| 評估 AI agent | 隨意判斷 | 檢核表逐項排除 |
| 寫評估報告 | 主觀偏見 | 結構化偏誤清單 |
| 復盤失敗 | 找單一原因 | 多重偏誤識別 |

## Top 25 必知偏誤（Dobelli 強調）

### 1. Survivorship Bias（倖存者偏差）

**一句話**：只看成功者，忽略失敗者。

**評估影響**：
- 評估 AI Agent 時只看到成功案例
- 選擇學習對象時只看到成功的例子
- **失敗案例往往更值得研究**

**Hermes 應用**：
- subagent 失敗 ≠ subagent 沒用
- Plan 失敗 ≠ Plan 思路錯

### 3. Confirmation Bias（確認偏誤）

**一句話**：找支持自己觀點的證據，忽略反證。

**評估影響**：
- 評估已支援的專案時只看正面
- 評估已批判的專案時只看負面
- **需要 Devil's Advocate**

**Hermes 應用**：TRAP-SOP-051 已有 devil_advocate 機制

### 4. Contrast Effect（對比效應）

**一句話**：相對比較影響判斷。

**評估影響**：
- 先看到好的再看到普通的 → 覺得普通是差的
- 評估量表的位置依賴之前看的對象
- **獨立評分 vs 比較評分結果不同**

### 5. Anchoring（錨定）

**一句話**：第一個數字/方案影響後續。

**評估影響**：見 TRAP-SOP-050

### 7. Sunk Cost Fallacy（沉沒成本謬誤）

**一句話**：已投入的時間/金錢不應該影響未來決策。

**評估影響**：
- 評估已進行半年的專案 → 給過高評分
- 評估已 spend 100 萬小時的 SOP → 不想改
- **前瞻 vs 回顧混淆**

**Hermes 應用**：
```python
def sunk_cost_check(plan):
    invested_hours = current_state.total_spent
    forward_value = projected_value(plan, next_3_months)
    if forward_value > 0:
        # 不論投入多少，仍值得做
        return "proceed"
    elif forward_value < 0:
        # 即使已投入 100 萬，仍止損
        return "stop"
```

### 8. Hindsight Bias（事後偏誤）

**一句話**：結果出來後認為「我早知道」。

**評估影響**：
- 評估**過去的決策**時，自動合理化
- 「那個決定顯然是 X」 — 但事前並不知道
- **必須分離「事前 vs 事後」**

### 12. Availability Heuristic（可得性偏誤）

**一句話**：易想到的事被高估。

**評估影響**：
- 最近發生的失敗被高估
- 媒體報導的案例被放大
- **基率**vs 易想起的案例

### 17. Loss Aversion（損失規避）

**一句話**：同樣大小的「損失」比「收益」感受更強。

**評估影響**：
- 強調 loss 比強調 gain 更有說服力（不可靠）
- 應該等量比較：「失敗機率 X%」vs「成功率 Y%」

### 22. Self-Serving Bias（自利偏誤）

**一句話**：成功歸功於自己，失敗怪運氣。

**評估影響**：
- 評估自己作品時不自覺地加分
- 評估對手作品時不自覺地減分
- **盲點**：自動化最強

### 28. Planning Fallacy（計劃謬誤）

**一句話**：低估時間/預算/複雜度。

**評估影響**：
- SOP 預估時間總是太樂觀
- 系統設計低估未來問題
- **對策**：用 2× to 3× buffer

### 31. Dunning-Kruger Effect（達克效應）

**一句話**：低能力者高估自己，高能力者低估自己。

**評估影響**：
- 評估 AI agent 時：簡單任務以為簡單
- 評估自己能力時：有 30% 不自知

### 50. Information Bias（資訊偏誤）

**一句話**：更多資訊不等於更好決策。

**評估影響**：
- 抓住每一條資料 ≠ 做出好決策
- **資訊光譜**：sometimes 少一點資訊更好

### 64. Authority Bias（權威偏誤）

**一句話**：因為說的人是權威就信。

**評估影響**：
- AI 領域大牛說的方法直接信
- 反而不質疑前提
- **對策**：評估論點本身，不評估說的人

### 78. Denial（否認）

**一句話**：拒絕接受壞消息。

**評估影響**：
- 自己專案的問題被低估
- 競爭對手的威脅被淡化
- **對策**：定期請外部 reviewer

### 92. Failure Bias（失敗恐懼）

**一句話**：對失敗的恐懼過度。

**評估影響**：
- 過度保守，錯失機會
- 「不能失敗」等同於「不能嘗試」
- **對策**：計算失敗的成本，是否真的不可承受？

### 93. Status Quo Bias（現狀偏誤）

**一句話**：不願改變，即使改變會更好。

**評估影響**：
- 評估新方案時偏向給低分
- 評估既有方案時偏向給高分
- **對策**：明確「是否為新方案」標記

## 99 個偏誤分類速查（Dobelli 結構）

```
1-25: 決策類（judgment）
26-50: 動機類（motivation）
51-75: 社會類（social）
76-99: 機率/統計類（probability）
```

## 對 Hermes 評估 SOP 的應用

### 5 大評估偏誤預防 SOP（落地版）

```python
# 任何評估前：5 大必檢
def evaluation_bias_check(evaluation_target):
    biases_checked = {
        "confirmation": "找反證 vs 找正證 — 結論是否都站?"
        "hindsight": "事前知道嗎？還是被結果污染？"
        "survivorship": "看到失敗案例嗎？vs 全部案例"
        "self_serving": "自己評嗎？還是 abstract reviewer?"
        "anchoring": "第一個印象是否控制後續？"
    }
    
    for bias_name, question in biases_checked.items():
        answer = reflect(question)
        if not answer:
            return "BLOCK: 評估前需先回答這個問題"
    
    return "PROCEED"
```

### 評估報告模板（含偏誤自檢）

```markdown
## 評估：XXX

### 結論
- 推薦選項：[A / B / C]
- 信心程度：高/中/低

### 偏誤自檢（5 必答）
- [ ] 我有找反證（Devil's Advocate）？
- [ ] 我分離了決策品質與結果？
- [ ] 我看了失敗案例？
- [ ] 我區分成功是我功勞還是運氣？
- [ ] 第一個數字沒控制後續判斷？

### 已知限制
- [任何已知的偏誤影響]
```

## 引用

- Dobelli, R. (2013). The Art of Thinking Clearly
- Duke, A. (2018). Thinking in Bets
- Kahneman, D. (2011). Thinking, Fast and Slow
- Hermes TRAP-SOP-049~052（文謀 SOP）
- Hermes TRAP-SOP-058（CoT）

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（基於 Dobelli 99 偏誤速查，整合 Kahneman 學術解釋 + Duke 實戰驗證）|