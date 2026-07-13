---
title: Eliminating Toil
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, sre, automation, toil-reduction, devops]
sources:
  - raw/articles/google-sre-book-2026-07-13.md
related:
  - "[[sre-site-reliability-engineering]]"
  - "[[slos-error-budget]]"
confidence: high
---

# Eliminating Toil

## 定義

**Toil** = Operations work that is:
- **Manual**：需要人執行
- **Repetitive**：可預測重複
- **Automatable**：可被機器取代
- **Tactical**：救火性質，非戰略
- **Devoid of enduring value**：做完就消失
- **Scales linearly with service growth**：服務成長 toil 等比增加

## Toil vs Engineering

| 維度 | Toil | Engineering |
|------|------|-------------|
| 重複性 | 高度 | 低度 |
| 自動化 | 無 | 通常有 |
| 長期價值 | 0 | 高 |
| 服務影響 | 線性 | 指數 |
| 心智挑戰 | 低 | 高 |

## Google SRE 目標

> **SRE 應花 ≤ 50% 時間在 toil**

若超過 50% → 應該自動化或重新分配工作。

## 6 大 Toil 自動化策略

### 1. Script Everything（腳本化一切）
- 每個手動任務寫一次腳本
- 第二次重複時必須自動化

### 2. Cron + Job Scheduler
- 定時任務自動化
- 監控 cron job 失敗

### 3. Self-Service Tools
- 開發者自助工具（deploy / rollback / scaling）
- 減少 ticket-based 工作流

### 4. Runbook Automation
- 將 runbook（操作手冊）轉為自動化
- 例：開新 GCP project → Terraform

### 5. Alert Auto-Remediation
- 自動修復常見 alert
- 例：磁碟滿 → 自動清 log + 通知

### 6. AI-Assisted Operations
- 用 LLM 做 log 分析、incident triage
- **例**：Hermes 用 Claude Code 做 subagent 任務

## Hermes 對應（Toil 消除範例）

| Toil 任務 | 自動化方式 | Speedup |
|----------|-----------|---------|
| 拆 71 顆過胖 Skill | 並聯 `delegate_task` | 7.5× |
| 健康檢查（6 Phase）| `system-health-check.md` 6-Phase Protocol | 一次性執行 |
| Frontmatter 補齊 | `skill-consistency-audit.sh` 自動掃描 | ~50× |
| MCP 連線測試 | 並聯 subagent + `mcp-config-traps.md` | ~10× |
| 4 條 SOP 路由決策樹 | `references/` 章節索引表 | -100% toil |

## Toil 計算法

```
Toil % = Toil 時間 / 總工作時間 × 100%

若 Toil % > 50%：
  1. 識別最大 toil 來源
  2. 估算自動化成本
  3. 自動化最高 ROI 的 toil
  4. 重新測量
```

## 對 Hermes 的啟示

### 立即可行

| Toil | 自動化方案 |
|------|-----------|
| 每次重複的 skill 結構檢查 | `skill-consistency-audit.sh` 自動掃描 |
| 每次重複的 system health 檢查 | `system_health_check.sh` 6-Phase Protocol |
| 每次 MCP 連線失敗除錯 | `mcp-config-traps.md` 5 條錯誤路徑表 |
| 每次重複的 SKILL.md 拆分 | 並聯 `delegate_task` |

### 設計原則

1. **第二次手動時必須自動化**：第一次容忍，第二次不
2. **Toil 預算 50%**：超過即自動化
3. **量化 toil 時間**：記錄每次任務耗時，找出最高 ROI 自動化目標
4. **避免過度自動化**：複雜度 < 價值才自動化

## 來源

- Google SRE Book Ch. 5: Eliminating Toil
- [SRE Workbook Ch. 5](https://sre.google/workbook/table-of-contents/)
- The Phoenix Project（Gene Kim）— Toil in IT Operations