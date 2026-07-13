---
title: "DMLS 11章 vs Hermes 架構對應分析"
created: 2026-07-11
updated: 2026-07-11
type: comparison
tags: [mlops, ml-systems, hermes, comparison, architecture, design]
sources: [entities/designing-ml-systems-book.md, entities/hermes-agent-version-history.md, concepts/mlops-systems-design.md, concepts/hermes-learning-loop.md, concepts/hermes-skills-system.md, concepts/hermes-messaging-gateway.md, concepts/hermes-hindsight.md, concepts/mcp-model-context-protocol.md]
confidence: high
---

# DMLS 11章 vs Hermes 架構對應分析

## 研究問題
[[designing-ml-systems-book]]（Chip Huyen, 2022）提出的 ML 系統設計框架，如何對應到 [[hermes-agent]] 的實際架構？哪些 DMLS 挑戰 Hermes 已解決？哪些仍有缺口？

## 十一章對應矩陣

| DMLS 章節 | DMLS 核心問題 | Hermes 對應 | 缺口分析 |
|-----------|-------------|-------------|---------|
| **Ch1 概述** | 研究 ML vs 生產 ML 差異 | Hermes 主要對標生產用例 | ✅ 符合 |
| **Ch2 系統設計** | 可靠性/擴展性/可維護性/適應性 | 分散式訊息 gateway、skills 系統、版本歷史 | ✅ 覆蓋 |
| **Ch3 數據工程** | 格式、數據模型、儲存引擎、批/流 | Memory 系統（跨 session FTS5） | ⚠️ 缺口：無原生 feature store、批流處理 |
| **Ch4 訓練數據** | 採樣、標註、類不平衡、增強 | 無直接對應 | ❌ 缺口：Hermes 不做模型訓練 |
| **Ch5 特徵工程** | Raw data → Features | Memory 萃取、Skills 封裝 | ⚠️ 部分對應：implicit，未結構化 |
| **Ch6 模型開發** | 實驗追蹤、AutoML、評估 | 無直接對應 | ❌ Hermes 是應用層，不做模型開發 |
| **Ch7 部署** | Shadow/Canary/Blue-Green | MCP tool gateway、provider 切換 | ⚠️ 有限對應：無 traffic splitting |
| **Ch8 分佈偏移** | Covariate/Label shift、監控 | [[hermes-hindsight]] 長期觀測記憶 | ⚠️ 缺口：無 distribution shift 檢測 |
| **Ch9 持續學習** | A/B 測試、Bandit、影子部署 | [[hermes-learning-loop]] 閉環學習 | ⚠️ 對應部分：學習迴圈，但非統計驅動 |
| **Ch10 基礎設施** | Model store、Feature store、部署工具 | MCP Protocol、Provider abstraction | ✅ 覆蓋：MCP 作為 tool store |
| **Ch11 人性面** | 用戶體驗、團隊結構、負責任 AI | Honcho user modeling | ⚠️ 有限對應 |

## 深度分析

### 1. 閉環學習：DMLS Ch9 的實現差異

**DMLS 的定義：** 持續學習 = 統計驅動的模型更新循環（A/B → 反饋 → 重訓練 → 部署）

**Hermes 的實現：** 經驗驅動的 Skills 創建循環（交互 → Memory → Skill → 優化）

```
DMLS:
  用戶行為數據 → 統計分析 → 模型更新 → A/B 測試 → 生產模型
       ↑________________________________________|

Hermes:
  交互經驗 → [[hermes-hindsight]] Memory → [[hermes-skills-system]] Skill
       ↑_____________________________________________|
```

**關鍵差異：** DMLS 專注於模型權重的更新；Hermes 專注於程序性知識（skills）的沉澱。兩者是互補的層次。

### 2. 四個系統需求：DMLS Ch2 vs Hermes 實現

|| DMLS 定義 | Hermes 實現 | 評估 |
|---------|---------|-----------|------|
| **Reliability** | 故障時繼續正確運作 | MCP tool fallback、多 provider 切換 | ✅ 良好 |
| **Scalability** | 需求成長可處理 | 水平擴展訊息 gateway | ⚠️ 單一瓶頸：gateway |
| **Maintainability** | 其他團隊可貢獻維護 | Skills 系統可被導出/分享 | ✅ 良好 |
| **Adaptability** | 隨需求/數據演化 | Learning loop + 技能自改進 | ✅ 優秀 |

### 3. 分佈偏移：DMLS Ch8 vs Hermes 現況

DMLS Ch8 定義了三種偏移：
- **Covariate shift:** P(X) 變化（輸入分佈漂移）
- **Label shift:** P(Y) 變化（標記分佈漂移）
- **Concept drift:** P(Y|X) 變化（標記函數本身漂移）

**Hermes 的問題：**
- `[[hermes-hindsight]]` 長期記憶可記錄歷史，但**沒有主動檢測分佈偏移**的機制
- [[hermes-learning-loop]] 可從錯誤中學習，但**被動觸發**，非主動監控
- 缺口：需要 PSI（Population Stability Index）或類似指標驅動的 alert

### 4. 工具生態：DMLS Ch10 vs MCP

DMLS Ch10 的 model store / feature store 模式：
```
Model Store: 版本化的模型 artifact + 元數據
Feature Store: 集中管理的可複用 features
```

MCP（[[mcp-model-context-protocol]]）是 Hermes 的工具 store：
```
Tool Store: 版本化的 tool schema + capability metadata
```

**對應：** MCP 解決了「工具的可發現性和版本化」問題，但不等同於 feature store（沒有 feature computation layer）。

### 5. 部署模式：DMLS Ch7 vs Hermes 現況

| DMLS 模式 | Hermes 對應 | 狀態 |
|----------|-----------|------|
| Shadow mode | 多 provider 平行查詢 | ⚠️ 有限實現 |
| Canary | 新 tool MCP 測試 | ⚠️ 社群反饋 |
| Blue-green | Provider 開關 | ✅ 已實現 |
| A/B testing | 無對應 | ❌ 缺口 |

## 主要發現

### 已解決
1. **LLMOps 核心問題：** Hermes 的 [[hermes-messaging-gateway]] 解決了多平台訊息收發的可靠性挑戰
2. **工具版本化：** MCP 作為標準化的 tool store，避免了 DMLS 担心的「工具飄移」
3. **Skills 即 Feature Store：** Hermes 的 skills 系統某種程度上扮演了「操作步驟的 feature store」角色

### 缺口
1. **模型訓練/更新：** Hermes 完全不碰模型訓練，適合應用層但無法解決 DMLS Ch4/Ch6 問題
2. **主動監控：** 無 distribution shift 主動檢測；依賴被動觸發的 learning loop
3. **統計驅動的 A/B 測試：** 無流量分割能力；依賴用戶反饋
4. **Feature store：** 無結構化的 feature computation layer

## 結論

**Hermes 是 DMLS 框架在 AI Agent 應用層的實現，而非完整的 ML 系統。**

- DMLS 覆蓋：數據工程 → 模型訓練 → 部署 → 監控 全鏈路
- Hermes 覆蓋：應用部署 → 工具組織 → 學習優化

對於構建 Hermes 生態系的開發者，DMLS 的價值在於：
1. **Ch2 系統需求框架** — 指導 Hermes 的可靠性/擴展性決策
2. **Ch8 分佈偏移** — 提醒需要主動監控（目前缺口）
3. **Ch11 人性面** — Honcho user modeling 已經體現

## See Also
- [[designing-ml-systems-book]] — 來源框架
- [[hermes-learning-loop]] — Hermes 的持續學習實現
- [[ai-engineering-framework]] — Chip 的 AIE 框架，填補 DMLS 和 LLM 時代的 gap
- [[llmops]] — 覆蓋 Hermes 未實現的模型訓練/評估部分
