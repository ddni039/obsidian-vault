---
UID: 20260610-hermes-rules
STATUS: Active
TYPE: Logic
---

# Hermes RULES

## 1. Summary
> 安全紅線：credential SSOT、密鑰不入 config、違反即失敗。

## 2. Assumptions & Invariants
* [ ] Hook 系統（`h-api-*`）已啟動
* [ ] 涉及 credential 的任務前會讀取 RULES.md
* [ ] auth.json 是唯一允許的 credential 儲存位置

## 3. Implementation

### Hard Rules（永不違反）

```
hermes config set <key> <value>   → 禁止寫入 API key
寫入 ~/.hermes/config.yaml         → 禁止
寫入任何 .md 檔案                  → 禁止
寫入任何 log 檔案                  → 禁止
寫入 playbook/*.md                → 禁止
```

### 違反回應

```
[E-BLOCKED] <操作> 被拒絕
原因：<違反原因>
修正：<如何糾正>
```

### Hook Chain

```
h-api-task-detector  → 偵測是否 API/credential 任務？
        ↓
h-api-file-guard     → 目標是否 credential 檔？
        ↓
h-api-guard          → 執行備份 + 寫入 + 同步
```

### API 呼叫前檢查清單

- [ ] Base URL 正確（無尾部斜線）
- [ ] Bearer token 格式
- [ ] Key 在 auth.json 中
- [ ] `hermes doctor` 通過

## 4. Verification

| 檢查 | 指令 |
|------|------|
| config 無 key | `rg "API_KEY" ~/.hermes/config.yaml`（期望 0）|
| .md 無 key | `rg "sk-" ~/.hermes/*.md`（期望 0）|
| Hook 存在 | `ls ~/.hermes/hooks/h-api-*.sh` |
| auth.json 存在 | `test -f ~/.hermes/auth.json` |

## 5. Changelog

* `2026-06-10`: 初始版本 — Hard rules、違反回應、Hook chain、驗證指令