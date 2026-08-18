# SOP_CREDENTIAL_GUARD.md — Credential 防呆 SOP v1.4

## 三層職責

| 層        | 職責                | 禁止         |
| --------- | ------------------- | ------------ |
| **B**rain | 分析、判定 key 類型 | 直接碰檔案   |
| **H**and  | upsert、寫入、重啟  | 自行判斷對錯 |
| **E**ye   | 活性測試、SSoT 對齊 | 跳過驗證     |

---

## 防禦深度 (Defense Depth)

> **注意：** L1/L2/L3 是深度防禦機制，與 BHEC 系統層級無關。

| 層  | 機制                                              | 指令                                            |
| --- | ------------------------------------------------- | ----------------------------------------------- |
| L1  | validate 寫入前校驗 (Read-only) (Read-only check) | `guard_credential.py validate <provider> <key>` |
| L2  | h-fix C-012 STEP 0 (Write-lock)                   | `h-fix C-012` → guard_credential.py audit       |
| L3  | cron 每日 04:00 (Audit-trigger)                   | cron "Credential Guard Audit"                   |

---

## Prefix Map

| Provider   | Prefix       |
| ---------- | ------------ |
| minimax    | sk-cp- / eyJ |
| nvidia     | nvapi-       |
| openrouter | sk-or-v1-    |
| github     | ghp\_        |
| jina       | jina\_       |
| airtable   | pat          |
| telegram   | 81           |
| discord    | 1a3          |

---

## Prefix Map

| Provider   | Prefix       |
| ---------- | ------------ |
| minimax    | sk-cp- / eyJ |
| nvidia     | nvapi-       |
| openrouter | sk-or-v1-    |
| github     | ghp\_        |
| jina       | jina\_       |
| airtable   | pat          |
| telegram   | 81           |
| discord    | 1a3          |

---

## Active Tokens (2026-05-13)

| Provider         | Token                                      | Status     | Used For               |
| ---------------- | ------------------------------------------ | ---------- | ---------------------- |
| minimax          | `sk-cp-...`                                | ✅ valid   | AI Agent               |
| github           | `[GITHUB_PAT]` | ✅ valid   | wiki, obsidian, hermes |
| github (retired) | `[RETIRED]`     | ❌ deleted | —                      |

---

## 維護清單

| 項目                  | 狀態          |
| --------------------- | ------------- |
| 修復 minimax key      | ✅            |
| 更新 token_types.json | ✅            |
| guard_credential.py   | ✅            |
| L2 h-fix 整合         | ✅            |
| L3 cron 自動審計      | ✅            |
| 更新 openrouter key   | ⬜            |
| 統一 github token     | ✅ 2026-05-13 |
| 清理廢棄 token 殘留   | ✅ 2026-05-13 |

---

_v1.4 — 2026-05-13_
