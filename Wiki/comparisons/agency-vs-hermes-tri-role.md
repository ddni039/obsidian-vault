---
title: Agency vs Hermes Tri-Role
created: 2026-06-11
updated: 2026-06-11
type: comparison
tags: [comparison, multi-agent, agency, hermes, tri-role]
sources: [raw/articles/agency-agents-readme-2026.md]
---

# Agency vs Hermes Tri-Role

## 設計哲學對比

| 維度 | Agency Agents | Hermes Tri-Role |
|------|-------------|-----------------|
| 哲學 | 水平specialization（專家池） | 垂直治理（決策鏈） |
| Agent 粒度 | 232 種獨立專業 | 3 種治理視角 |
| 上下文 | 各自獨立 | 共享 MEMORY/USER |
| 觸發 | 人工選agent | 事件自動驅動 |
| 個性表達 | vibe + emoji + color | Hook Chain + 三角色腳本 |
| 目標 | 交付特定領域成果 | 維持系統長期健康 |

## Agency 的 232 agent 如何分類

```
水平Specialization（按Division）
├── Engineering (30): Frontend, Backend, AI, DevOps...
├── Design (9): UI, UX, Brand, Visual Storyteller...
├── Marketing (36): Growth, Content, SEO, China platforms...
├── Specialized (62): HR, Legal, Healthcare, Finance...
└── ...

垂直治理（Hermes Tri-Role）
├── 文謀：規劃、診斷、策略
├── 工匠：執行、迭代、交付
└── 御史：驗收、監控、品質
```

## 互補點

Agency agents 可作為 Hermes 的**執行工具庫**：
- 當 Hermes 需要專業領域知識時，調用對應 Agency agent
- Hermes 的三角色保持系統治理，Agency agents 負責專門任務
- 兩者組合：治理層（Hermes）+ 執行層（Agency）

## 結論

- **Agency**：橫向擴展專業能力，適合多元任務
- **Hermes**：縱向維持系統健康，適合長期陪伴
- **最佳組合**：Hermes 擔任教練，Agency agents 擔任專家
