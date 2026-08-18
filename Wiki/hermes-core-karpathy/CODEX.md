---
UID: 20260610-hermes-codex
STATUS: Active
TYPE: Logic
---

# Hermes CODEX

## 1. Summary
> API 操作標準：auth.json 為 SSOT，.env 為遮蔽層，密鑰不碰 config 檔。

## 2. Assumptions & Invariants
* [ ] `~/.hermes/auth.json` 存在且為有效 JSON
* [ ] API key 只透過 credential guard 寫入
* [ ] Base URL 無尾部斜線
* [ ] Authorization：`Bearer <key>`

## 3. Implementation

### Provider Endpoint

| Provider | Base URL | Env Key |
|----------|----------|---------|
| MiniMax Intl | `https://api.minimax.io/anthropic` | `MINIMAX_API_KEY` |
| MiniMax CN | `https://api.minimax.cn/anthropic` | `MINIMAX_CN_API_KEY` |
| Custom | `https://<user-defined>/anthropic` | `CUSTOM_API_KEY` |

### SSOT 寫入流程

```
Task 需要 key → Hook: h-api-task-detector 觸發
  → Guard: 目標是否 credential 檔？
  → 是：備份 auth.json → 寫入 → 同步 .env
  → 否：直接寫入
```

### 重試策略

| 錯誤 | 動作 | 最大次數 |
|------|------|----------|
| 429 Rate Limit | 指數退避（1s→2s→4s）| 3 |
| 5xx Server Error | 重試 | 3 |
| 4xx Client Error | 直接失敗 | 0 |
| 網路逾時 | 重試 | 3 |

## 4. Verification

| 檢查 | 指令 |
|------|------|
| auth.json 有效 | `python3 -c "import json; json.load(open('~/.hermes/auth.json'))"` |
| Key 存在 | `grep MINIMAX_API_KEY ~/.hermes/auth.json` |
| config 無 key | `grep API_KEY ~/.hermes/config.yaml`（期望空）|
| 連線測試 | `hermes doctor` |

## 5. Changelog

* `2026-06-10`: 初始版本 — Provider 矩陣、重試策略、驗證指令