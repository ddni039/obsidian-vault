#!/usr/bin/env python3
"""
Security Sentinel — OpenClaw 敏感資訊守護腳本
功能：掃描 + 自動修復敏感資訊外洩風險
使用：python3 security_sentinel.py [--fix]
"""

import os
import re
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# ── 設定 ──
HOME = Path.home()
OPENCLAW_ROOT = HOME / ".openclaw"
TRASH_DIR = OPENCLAW_ROOT / "trash"
WORKSPACE = OPENCLAW_ROOT / "workspace"

DANGEROUS_PATTERNS = [
    (re.compile(r"sk-[a-zA-Z0-9]{20,}"), "🔴", "疑似 OpenAI/MiniMax API Key（明文）"),
    (re.compile(r"jina_[a-zA-Z0-9]{20,}"), "🔴", "疑似 Jina API Key（明文）"),
    (re.compile(r"password[\"':\s]*[:=][ \"']+[^\s\"']{8,}"), "🔴", "疑似密碼欄位（明文）"),
    (re.compile(r"BOT_TOKEN['\":\s]*[:=][ \"']+[a-zA-Z0-9:_\-]{20,}"), "🔴", "疑似 Bot Token（明文）"),
    (re.compile(r"ghp_[a-zA-Z0-9]{20,}"), "🔴", "疑似 GitHub PAT（明文）"),
]

SENSITIVE_FILES = [
    OPENCLAW_ROOT / "openclaw.json",
    WORKSPACE / "MEMORY.md",
    WORKSPACE / "USER.md",
    WORKSPACE / "SOUL.md",
    OPENCLAW_ROOT / "exec-approvals.json",
]

RED = '\033[0;31m'
GRN = '\033[0;32m'
YLW = '\033[1;33m'
CYN = '\033[0;36m'
WH = '\033[0m'

found_issues = []
fixed_count = 0
skipped_count = 0

def log(level, msg):
    print(f"{level}{msg}{WH}")

def mask(s, show=6):
    if len(s) <= show + 4:
        return "****"
    return s[:show] + "****" + s[-4:]

def backup_to_trash(src_path):
    TRASH_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    dst = TRASH_DIR / f"{src_path.name}.bak.{ts}"
    shutil.copy2(src_path, dst)
    log(GRN, f"  ✅ 已備份 → {dst}")

def check_permissions(path):
    global found_issues, fixed_count, skipped_count
    if not path.exists():
        return
    mode = oct(path.stat().st_mode)[-3:]
    if mode != "600":
        log(YLW, f"[⚠️] {path.name} 權限為 {mode}（應為 600）")
        found_issues.append(f"權限 {mode} → 應為 600：{path}")
        if FIX_MODE:
            os.chmod(path, 0o600)
            log(GRN, f"  ✅ 已修復：chmod 600")
            fixed_count += 1
    else:
        log(GRN, f"  ✅ 權限正常：{path.name}")

def scan_file(path):
    global found_issues, fixed_count, skipped_count
    if not path.exists():
        return
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return

    modified = content
    needs_backup = False

    for pattern, level, desc in DANGEROUS_PATTERNS:
        for match in pattern.finditer(modified):
            raw = match.group(0)
            pos = match.span()
            log(level, f"[{level}] {path.name}：{desc}")
            log(level, f"      位置：第 ~{modified[:pos[0]].count(chr(10))+1} 行，內容：{mask(raw)}")
            found_issues.append(f"{path.name}：{desc}")
            if FIX_MODE:
                needs_backup = True

    if FIX_MODE and needs_backup:
        backup_to_trash(path)
        # 逐一替換所有匹配的敏感字串
        for pattern, level, desc in DANGEROUS_PATTERNS:
            modified, count = pattern.subn("[REDACTED]", modified)
            if count:
                log(GRN, f"  ✅ 已替換 {count} 處：{desc}")
                fixed_count += count
        path.write_text(modified, encoding="utf-8")
        log(GRN, f"  ✅ 已寫回：{path.name}")

    # 權限檢查
    check_permissions(path)

FIX_MODE = "--fix" in __import__("sys").argv

def main():
    global found_issues, fixed_count, skipped_count

    print(f"\n{'='*50}")
    print(f"{CYN}🔍 Security Sentinel — OpenClaw 敏感資訊守護{WH}")
    print(f"{'='*50}")
    print(f"模式：{'🔧 自動修復' if FIX_MODE else '🔍 僅報告'}")

    for path in SENSITIVE_FILES:
        print(f"\n{CYN}── 掃描：{path.relative_to(HOME)}{WH}")
        scan_file(path)

    print(f"\n{'='*50}")
    print(f"📊 結果：🔴 🔴 🔴")
    if FIX_MODE:
        print(f"  已修復：{fixed_count} 項")
    else:
        print(f"  發現問題：{len(found_issues)} 項（加 --fix 執行修復）")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
