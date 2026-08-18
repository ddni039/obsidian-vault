# Security Sentinel — OpenClaw 敏感資訊守護

## 觸發關鍵字

「安全檢測」、「敏感資訊檢查」、「檢查 Token 是否外洩」、「API Key 是否安全」

---

## 使用方式

```bash
# 僅報告（不修改）
python3 ~/.openclaw/workspace/skills/security-sentinel/security_sentinel.py

# 自動修復
python3 ~/.openclaw/workspace/skills/security-sentinel/security_sentinel.py --fix
```

---

## 掃描範圍

| 檔案 | 檢測目標 |
|------|----------|
| `~/.openclaw/openclaw.json` | 明文 API Key / Token |
| `~/.openclaw/workspace/MEMORY.md` | 密碼、完整 API Key |
| `~/.openclaw/workspace/USER.md` | 密碼、完整 API Key |
| `~/.openclaw/workspace/SOUL.md` | 密碼、敏感內容 |
| `~/.openclaw/exec-approvals.json` | socket token 外洩 |
| 檔案權限 | 全部應為 `600`，否則警告 |

---

## 檢測的危險 Pattern

| Pattern | 意義 |
|--------|------|
| `sk-xxxx`（20+字） | OpenAI / MiniMax API Key |
| `jina_xxxx`（20+字） | Jina API Key |
| `ghp_xxxx`（20+字） | GitHub PAT |
| `password": "xxxx"`（8+字） | 明文密碼 |
| `BOT_TOKEN` | Bot Token |

---

## 修復邏輯

- 🔴 **明文 API Key** → 改為 `${ENV_VAR}` 格式，寫入 `.env`
- 🔴 **權限 644/777** → `chmod 600`
- 🔴 **Token 外洩** → 重新產生 `exec-approvals.json`
- ⚠️ 所有修改前先備份到 `~/.openclaw/trash/`

---

## 輸出格式

```
🔍 Security Sentinel 報告
掃描時間：2026-04-01 16:54
🔴 發現 X 項｜🟡 中風險 X 項｜🟢 安全 X 項

[🔴] openclaw.json
  問題：疑似 MiniMax API Key（明文）
  位置：第 12 行，內容：sk-cp-e7……xmwQ
  修復：已改為 ${MINIMAX_API_KEY} 格式
```
