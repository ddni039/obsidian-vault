---
name: claude-code-assistant
description: Claude Code 是 Anthropic 開發的 AI 程式碼助手，支援 Terminal、VS Code、Desktop、Web 等平台。本技能幫助 OpenClaw 使用者快速上手 Claude Code，包括安裝、基本操作、常用指令、與 OpenClaw 的整合應用。觸發場景：询问 Claude Code、想要學程式、開發環境設定、使用 spec-kit 開發專案。
---

# Claude Code 助手技能

## 什麼是 Claude Code？

Claude Code 是 Anthropic 開發的 AI 程式碼助手，可以：
- 讀取和編輯程式碼
- 執行終端機命令
- 自動化開發任務
- 與各種開發工具整合

**支援平台：** Terminal CLI、VS Code、JetBrains、Desktop App、Web

---

## 安裝 Claude Code

### macOS / Linux / WSL2
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows PowerShell
```powershell
irm https://claude.ai/install.ps1 | iex
```

### Homebrew
```bash
brew install --cask claude-code
```

### 驗證安裝
```bash
claude --version
```

---

## 與 OpenClaw 的整合方式

### 方式一：作為獨立工具
Claude Code 和 OpenClaw 是獨立的工具，可以：
- OpenClaw 負責日常任務、排程、訊息管理
- Claude Code 負責複雜的程式開發任務

### 方式二：透過 Agent SDK 調用
使用 Agent SDK 可以讓 Claude Code 被 OpenClaw 呼叫：
```python
from anthropic import Anthropic

client = Anthropic()
response = client.messages.create(
    model="claude-code",
    max_tokens=1024,
    messages=[{"role": "user", "content": "任務描述"}]
)
```

### 方式三：透過 sessions_spawn 啟動 Claude Code（推薦用於專案開發）

這是最推薦的方式，讓 Claude Code 以 subagent 形式執行完整專案：

```javascript
sessions_spawn({
    task: "任務描述，包含詳細需求和執行步驟",
    runtime: "subagent",
    mode: "run"
})
```

**實務經驗（2026-03-30 擬物風格 Todo List 專案）：**

1. **launch 前先準備好任務描述** — 包含需求、執行步驟、風格參考
2. **指定工作目錄** — Claude Code 預設在 workspace 根目錄，專案建議放子資料夾
3. **讓他直接執行，不要询问** — 在 task 最後加「請直接開始執行，不要询问，直接做」
4. **等待完成通知** — subagent 完成後會自動推送結果到 chat

```javascript
// 完整範例：啟動 Claude Code 開發擬物風格 Todo List
sessions_spawn({
    task: `使用 spec-kit 建立一個「擬物風格 Todo List」網頁應用。

## 需求
- 視覺風格：Skeuomorphic（擬物風）
- 功能：新增、完成刪除、編輯、分類/標籤
- 互動：拖曳排序、點擊打勾、雙擊編輯

## 執行步驟
1. 安裝 spec-kit（npm install -g spec-kit）
2. 初始化專案：specify init
3. 建立 Constitution.md、Spec.md、Plan.md、Tasks.md
4. 根據 spec 實作完整程式碼
5. 確保可以正常運行

請直接開始執行，不要询问，直接做。`,
    runtime: "subagent",
    mode: "run"
})
```

---

## 常用 Claude Code 指令

| 指令 | 用途 |
|------|------|
| `claude` | 啟動互動式對話 |
| `claude "任務描述"` | 直接執行單一任務 |
| `claude -p "提示"` | 管道模式，適合腳本整合 |
| `/help` | 顯示幫助資訊 |
| `/compact` | 壓縮上下文 |
| `/clear` | 清除對話歷史 |
| `/commit` | 建立 Git 提交 |
| `/pr` | 建立 Pull Request |
| `/review` | 程式碼審查 |
| `/schedule` | 排程任務 |

---

## spec-kit 開發流程（Claude Code 專用）

spec-kit 是一個結構化開發流程，建議與 Claude Code 搭配使用：

### 流程步驟

| 步驟 | 產出 | 說明 |
|------|------|------|
| 1 | Constitution.md | 設計原則與核心價值觀 |
| 2 | Spec.md | 功能規格（User Story + 需求文件）|
| 3 | Plan.md | 實作計劃（架構、技術選型）|
| 4 | Tasks.md | 任務清單（待辦事項）|
| 5 | 實作 | 根據 spec 完整實作 |

### 初始化專案
```bash
# 安裝 spec-kit
npm install -g spec-kit

# 初始化新專案
cd path/to/project
specify init
```

### Claude Code 如何使用 spec-kit

在 launch 的 task 描述中明確指定：
```
1. 安裝 spec-kit（npm install -g spec-kit）
2. 初始化專案：specify init
3. 建立 Constitution.md、Spec.md、Plan.md、Tasks.md
4. 讓 Claude Code 根據 spec 實作完整程式碼
5. 確保可以正常運行
```

### 專案結構範例
```
my-project/
├── Constitution.md   — 設計原則
├── Spec.md           — 功能規格
├── Plan.md           — 實作計劃
├── Tasks.md          — 任務清單
└── index.html        — 最終產出
```

---

## 常見使用情境

### 1. 自動化重複任務
```bash
claude "write tests for the auth module, run them, and fix any failures"
```

### 2. 修復 Bug
```bash
claude "fix the login bug: error 'undefined user' when session expires"
```

### 3. 建立提交和 PR
```bash
claude "commit my changes with a descriptive message"
claude "create a PR for the new feature"
```

### 4. 程式碼審查
```bash
claude "review these changed files for security issues"
```

### 5. 排程任務
```bash
# 在 Claude Code 內
/schedule "every day at 9am" "review open pull requests"
```

### 6. 使用 spec-kit 開發完整專案
```javascript
sessions_spawn({
    task: "使用 spec-kit 建立一個電商網站。包含：商品列表、購物車、結帳流程。請直接開始執行。",
    runtime: "subagent",
    mode: "run"
})
```

---

## Claude Code 與 OpenClaw 的分工建議

| 任務類型 | 推薦工具 |
|----------|----------|
| 日常訊息處理 | OpenClaw |
| 排程自動化 | OpenClaw Cron |
| 複雜程式開發 | Claude Code + spec-kit |
| 快速程式碼修正 | Claude Code |
| 程式碼審查 | Claude Code |
| 網頁/UI 自動化 | OpenClaw + Skills |
| 筆記整理 | OpenClaw + Obsidian |

---

## 進一步學習

- 官方文檔：https://docs.anthropic.com/claude-code/
- CLI 參考：https://docs.anthropic.com/en/docs/claude-code/cli-reference
- 快捷指南：https://docs.anthropic.com/en/docs/claude-code/quickstart

---

## 疑難排解

### Q: claude 指令找不到？
```bash
# 重新安裝或檢查路徑
curl -fsSL https://claude.ai/install.sh | bash
```

### Q: 需要登入？
```bash
claude login
```

### Q: 如何查看版本？
```bash
claude --version
```

### Q: sessions_spawn 無法啟動？
- 確認 runtime 參數為 "subagent"
- 確認 mode 為 "run"（不支援互動式 session）
- subagent 完成後會自動推送結果

### Q: Claude Code 完成後如何查看產出？
- subagent 會自動推送完成通知到 chat
- 專案檔案會建立在 workspace 子目錄
- 可用 exec 查看：`ls -la ~/path/to/project/`

---

## 更新紀錄

- **2026-03-30**：新增 sessions_spawn 啟動方式、spec-kit 開發流程、實務經驗（擬物風格 Todo List 專案）

---

_此技能由輕舞天堂整理自 Claude Code 官方文檔 + 實戰經驗_
