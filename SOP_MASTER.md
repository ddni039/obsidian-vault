# SOP_MASTER — Hermes 作業索引 v18.0

## 三層職責邊界

```
B — Brain  分析/規劃/分流（禁：直接碰檔案）
H — Hand   執行/腳本/終端（禁：自行判斷對錯）
E — Eye    核查/審計（禁：跳過驗證）
C — Config 密鑰/環境（禁：邏輯覆蓋物理）
```

---

## 快速入口

| 指令                    | 層      | 說明                   |
| ----------------------- | ------- | ---------------------- | --- | --------------------- |
| `h-status`              | E       | 健康分儀表板           |
| `h-clean [--dry-run]`   | H       | session+log 脫水       |
| `h-fix <代碼>`          | H       | 互動式維修             |
| `h-sop <代碼>`          | B       | ERRORS.md 止損動作     |
| `h-audit-pro`           | B/H/E   | 三層職責審計           |
| `h-env-audit [--clean]` | C/E     | .env vs auth.json SSoT |
| `h-compare`             | E       | MATRIX.md 標配比對     |
| `h-trace`               | B/E     | 時序追蹤（Mermaid）    |
| `h-pdf-export`          | H       | SOP_MASTER.md → PDF    |
| `h-watch --install`     | E       | 每小時背景偵測         |
| `h-err-monitor --all`   | B/H/E/C | 錯誤感測全項目健檢     |
| `h-mmax probe`          | E       | MiniMax MCP 探針       |
| `h-mem-gate [check      | pointer | status]`               | C   | Memory L1/L2 寫入閘門 |

---

## Memory 寫入約束

```
L1 單次寫入 ≤ 500 chars（memory tool）
L2 詳細內容進 memory.md
超限 → h-mem-gate pointer 生成指標
```

---

## 脫水門檻

| 類型         | 條件   | 動作           |
| ------------ | ------ | -------------- |
| session      | >100KB | H 刪除         |
| request_dump | >1天   | H 刪除         |
| \*.log       | 任意   | H tail-20 脫水 |

---

## SOP-as-Code 條文

### h-audit

```
B: 單檔>200行 → REJECT
H: find -name "*.sh" | xargs wc -l
E: 比對 MATRIX.md 標配
```

### h-fix

```
B: 密鑰洩漏 → LOCK
H: ERRORS.md → 執行修復
E: h-status 驗證
C: 雙寫 auth.json + .env
```

### h-clean

```
B: session>100KB → STRICT
H: find -size +100k -delete
E: 脫水後 h-status 確認
```

### h-env-audit

```
B: 讀取 .env + auth.json
H: 比對 key 前綴
E: 不一致 → exit 1
```

### h-trace

```
B: 解析 JSON log
H: grep task_id
E: Mermaid sequenceDiagram
```

### h-mmax

```
B: Offline → STRICT
H: h-mmax probe
E: 8 Tools Online → NOTIFY
```

### h-push

```
B: 聚合 h-status
H: curl POST webhook
E: HTTP 200 驗證
C: 讀取 HYPEROS_WEBHOOK
```

### h-compare

```
B: MATRIX.md SSoT 基線
H: 遍歷 h-* 指令
E: 差異矩陣輸出
```

---

## 流程速查

```
故障 → health_probe.sh → h-sop <代碼> → h-fix <代碼>
預警 → h-watch --install
核查 → h-env-audit --clean
```

---

## 維護 SOP 索引

| 代碼           | 文件                               | 說明                |
| -------------- | ---------------------------------- | ------------------- |
| MAINT-20260513 | SOP_HERMES_MAINTENANCE_20260513.md | 2026-05-13 維護記錄 |

---

_v18.2 — 2026-05-13（新增 MAINT-20260513 維護 SOP）_

---

## Memory Write-Gate SOP

### 觸發條件

任一：寫入 > 300 chars / 含配置或代碼

### 流程

```
1. h-mem-gate check <content>
2. PASS → 寫入 L1
   REJECT → h-mem-gate pointer <section>
3. 內容寫入 memory.md（L2）
4. 指針寫入 L1
5. h-mem-gate status 確認
```

### 禁止

- L1 寫入完整腳本/配置/列表
- L1 寫入 > 500 chars

### 驗證

```bash
h-mem-gate status
h-status | grep Memory
```
