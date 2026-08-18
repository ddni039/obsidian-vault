---
name: orchestrator
description: |
  OpenClaw 通用任務編排調度員。當有多步驟任務需要邏輯分工、按需調用技能、避免卡死時啟用。
  
  觸發時機：
  - 用戶說「自動執行」、「背景處理」、「任務編排」
  - Cron 觸發的背景任務（每 N 分鐘檢查任務隊列）
  - 複雜任務需要拆解並依序執行多個技能
  - 任務可能涉及多個領域（郵件、程式、資料、寫作）需要統一調度
  
  此技能包含：
  - Task Analyzer：理解任務本質與邊界
  - Task Decomposer：拆解為最小執行單元
  - Skill Router：根據子任務類型掛載對應技能
  - Isolation Engine：失敗自動繞路，連續 3 次失敗則降級處理
  - Delivery Agent：彙整結果並附檔案交付
---

# 技能調度員 (Orchestrator)

## 核心工作流程

```
任務輸入 → 任務分析 → 邏輯分解 → 技能路由 → 隔斷演算 → 交付
```

---

## 任務池（Task Queue）

路徑：`~/.openclaw/task_queue.txt`

格式：每行一筆任務，JSON 格式

```json
{"id":"001","type":"email","task":"檢查新郵件並回覆重要來信","priority":1,"status":"pending","retry":0}
{"id":"002","type":"code","task":"整理下載資料夾","priority":2,"status":"pending","retry":0}
```

---

## 技能池（Skill Registry）

| 任務類型 | 調用技能 | 說明 |
|----------|----------|------|
| `email` | gog | Gmail 讀取/發送/搜尋 |
| `code` | coding-agent | 程式開發、CodeAgent 委託 |
| `reminder` | reminder | 提醒事項創建 |
| `document` | obsidian-markdown | 筆記整理 |
| `web` | agent-browser / playwright | 網頁操作 |
| `search` | tavily-search / web-search | 資料搜尋 |
| `translate` | quick-translate | 翻譯 |
| `write` | writing-assistant | 寫作潤飾 |
| `media` | video-frames / summarize | 影片/音頻處理 |
| `general` | （直接處理） | 無需特殊技能 |

---

## 任務分析器（Task Analyzer）

### 分析流程

1. **讀取任務池**：`cat ~/.openclaw/task_queue.txt`
2. **識別任務類型**：依關鍵字判斷
   - `mail`、`email`、`gmail` → `email`
   - `code`、`程式`、`開發` → `code`
   - `提醒`、`鬧鐘`、`schedule` → `reminder`
   - `筆記`、`obsidian`、`整理` → `document`
   - `搜尋`、`查詢`、`找` → `search`
   - 其他 → `general`
3. **評估優先級**：1（最高）到 5（最低）
4. **設定失敗閾值**：預設 3 次

---

## 邏輯分解引擎（Task Decomposer）

### 複雜任務拆解原則

| 原則 | 說明 |
|------|------|
| **最小單元** | 每個子任務不可再拆 |
| **順序依賴** | 有依賴關係的任務排隊執行 |
| **可並行** | 無依賴的子任務可同時觸發 |
| **明確邊界** | 每個子任務有明確的輸入與輸出 |

### 拆解格式

```
任務：[原始任務描述]
├── 子任務 1：[描述] → [技能]
├── 子任務 2：[描述] → [技能]
└── 子任務 3：[描述] → [技能]
```

---

## 技能路由器（Skill Router）

### 路由邏輯

```python
def route(task_type):
    registry = {
        "email":   ["gog"],
        "code":    ["coding-agent", "code-explainer"],
        "reminder":["reminder", "remind-me"],
        "document":["obsidian-markdown"],
        "web":     ["agent-browser", "playwright"],
        "search":  ["tavily-search", "web-search"],
        "translate":["quick-translate"],
        "write":   ["writing-assistant"],
        "media":   ["video-frames", "summarize"],
        "general": []
    }
    return registry.get(task_type, [])
```

### 掛載順序

1. 先讀取對應 Skill 的 SKILL.md（如有）
2. 依序執行技能指令
3. 結果寫入任務日誌

---

## 隔斷式演算引擎（Isolation Engine）

### 失敗處理邏輯

```
子任務執行
    ↓
成功？ → 是 → 寫入日誌，繼續下一個
    ↓ 否
失敗計數 +1
    ↓
計數 < 3？ → 是 → 重試（等 30 秒）
    ↓ 否
標記為 FAILED，跳過，繼續下一個
    ↓
全部執行完 → 彙整結果 → 交付
```

### 繞路策略

| 失敗次數 | 策略 |
|----------|------|
| 1 次 | 等 30 秒重試 |
| 2 次 | 等 60 秒重試，更換技能 |
| 3 次 | 標記失敗，降級處理（跳過或簡化） |

### 降級處理

- `email` → 改用 `webmail` 或只標記不回覆
- `code` → 改用一般指令或擱置
- `search` → 改用 `web-search` 替代

---

## 交付代理（Delivery Agent）

### 輸出格式

```
📋 任務報告：{任務名稱}
━━━━━━━━━━━━━━━
✅ 完成：{子任務數}
⚠️ 失敗：{失敗數}（已跳過）
⏱️ 耗時：{總分鐘數}分鐘

詳細結果：
1. [子任務1] ✅ 完成
2. [子任務2] ⚠️ 失敗（已繞路）
3. [子任務3] ✅ 完成

📍 日誌：~/.openclaw/orchestrator/logs/{id}.log
```

### 交付方式

- **Telegram 回報**：使用 cron 的 announce delivery
- **檔案附件**：產出檔案附加到回報
- **日誌留存**：所有操作寫入 `~/.openclaw/orchestrator/logs/`

---

## 執行腳本（Task Queue Processor）

當 cron 觸發時，調用以下流程：

### 步驟 1：讀取任務池

```bash
# 讀取所有 pending 任務
grep '"status":"pending"' ~/.openclaw/task_queue.txt
```

### 步驟 2：依優先級排序

按 `priority` 欄位由小到大（1 最高優先）。

### 步驟 3：依序執行

對每個任務：
1. 解析任務類型與內容
2. 路由到對應技能
3. 執行並記錄結果
4. 更新任務狀態（done / failed）

### 步驟 4：清理與交付

- 刪除已完成任務（可保留歷史日誌）
- 發送完成報告

---

## 任務池管理命令

```bash
# 查看任務池
cat ~/.openclaw/task_queue.txt

# 手動加入任務（JSON 單行）
echo '{"id":"003","type":"search","task":"搜尋最新油價資訊","priority":1,"status":"pending","retry":0}' >> ~/.openclaw/task_queue.txt

# 查看執行日誌
ls ~/.openclaw/orchestrator/logs/

# 查看特定任務日誌
cat ~/.openclaw/orchestrator/logs/{id}.log
```

---

## 日誌格式

路徑：`~/.openclaw/orchestrator/logs/{task_id}_{timestamp}.log`

```
[2026-04-09 15:50:00] 任務開始：檢查新郵件
[2026-04-09 15:50:05] 掛載技能：gog (email)
[2026-04-09 15:50:10] 子任務執行：gog gmail search 'newer_than:30m'
[2026-04-09 15:50:15] 子任務完成：找到 3 封新郵件
[2026-04-09 15:50:16] 任務完成，耗時 16 秒
```

---

## 安全規則

- 刪除檔案前必須確認（用 `trash` 而非 `rm`）
- 發送外部訊息前必須確認收件人
- 發現錯誤立即記錄，不掩蓋
- 隔斷失敗不影響其他任務（隔離原則）

---

## 初始化設置

首次使用需建立目錄結構：

```bash
mkdir -p ~/.openclaw/orchestrator/logs
touch ~/.openclaw/task_queue.txt
chmod 600 ~/.openclaw/task_queue.txt
```

並設定 Cron Job（每 5 分鐘觸發）：

```bash
openclaw cron add \
  --name "Orchestrator 任務調度員" \
  --cron "*/5 * * * *" \
  --tz "Asia/Taipei" \
  --session isolated \
  --message "你是任務編排調度員。執行以下流程：\n1. 讀取任務池 ~/.openclaw/task_queue.txt\n2. 找出所有 status=pending 的任務\n3. 依 priority 順序執行每個任務\n4. 每個任務經歷：分析→分解→路由→執行→記錄\n5. 失敗超過 3 次的子任務自動繞路或降級\n6. 完成後更新任務狀態並回報結果" \
  --announce \
  --channel telegram \
  --to "7634988810"
```