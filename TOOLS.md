# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Installed Skills（已安裝技能）

### TTS（文字轉語音）
- `text-to-speech` - Inference TTS
- `tts` - Marswave TTS (600 installs)
- 安裝方式：`npx skills add marswaveai/skills@tts -g -y`
- 使用：需要參考對應 SKILL.md

### Obsidian
- `obsidian-markdown` - Obsidian 筆記增強（11.4K installs）
- 安裝方式：`npx skills add kepano/obsidian-skills@obsidian-markdown -g -y`
- 適用於：筆記整理、Markdown 增強

### Automation（自動化）
- `reminder` - 提醒技能（188 installs）
- 安裝方式：`npx skills add lostabaddon/headlessknight@reminder -g -y`
- 搭配 Cron 使用效果更好

### Claude Code + OpenClaw
- `claude-code-clawdbot` - Claude Code 與 OpenClaw 整合（16 installs）
- 安裝方式：`npx skills add win4r/claude-code-clawdbot-skill@claude-code-clawdbot -g -y`
- 適用於：Code Agent 協作

### Claude Code 助手（自定義）
- `claude-code-assistant` - Claude Code 使用指南技能
- 路徑：`~/.agents/skills/claude-code-assistant/SKILL.md`
- 功能：Claude Code 安裝、操作、整合 OpenClaw 方式
- 適用於：想學習或使用 Claude Code 的使用者

### Spec Kit
- `uvx` - 安裝於 `~/.local/bin/uvx`
- `Claude Code` - 安裝於 `~/.local/bin/claude`（版本 2.1.87）
- 功能：規格驅動開發（Spec-Driven Development）
- 使用：`uvx --from git+https://github.com/github/spec-kit.git specify init <項目>`

### Backup
- `clawhub-install.sh` - 技能安裝腳本（自訂）
- 路徑：`~/.openclaw/workspace/clawhub-install.sh`
- 功能：防 Rate Limit、互動式輸入、自動重試

## 安裝技巧

### 安裝多個技能時
1. 使用 `clawhub-install.sh` 腳本避免 Rate Limit
2. 每個技能安裝後建議等待 45 秒
3. 被限流時自動等待 30/60/90/120/150 秒並重試

### Skill 安裝指令
```bash
# 搜尋技能
npx skills find <關鍵字>

# 安裝技能
npx skills add <owner/repo@skill> -g -y

# 列出已安裝
npx skills list

# 移除技能
npx skills remove <owner/repo@skill> -g -y
```

## Cron 排程經驗

### 常見錯誤修復
- **"Channel is required"**：需指定 `--channel telegram --to <chatId>`
- **"Delivering to Telegram requires target"**：需在 delivery 設定中加入 `to: "<chatId>"`

### 建議的 delivery 設定
```bash
openclaw cron add \
  --name "任務名稱" \
  --cron "0 12 * * *" \
  --tz "Asia/Taipei" \
  --session isolated \
  --message "任務內容" \
  --announce \
  --channel telegram \
  --to "7634988810"
```

## 用戶偏好

- 稱呼：痞子林
- 語言：中文
- 時區：Asia/Taipei (GMT+8)
- Telegram ID：7634988810

### 任務完成交付方式
- **預設**：直接以附件發送到 Telegram
- **例外**：只有純文字回覆才可以直接發送
- **適用**：HTML/程式碼檔案、文件、PPT 等
- **回覆格式**：盡量使用表格、列表、表情符號等豐富格式，類似截圖中的效果

---

Add whatever helps you do your job. This is your cheat sheet.
