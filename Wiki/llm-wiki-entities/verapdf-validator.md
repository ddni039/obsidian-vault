---
uid: 20260713-verapdf-validator
name: veraPDF Validator
aka: [veraPDF, PDF/A validator, PDF/UA validator, open source PDF validator]
type: entity
tags: [PDF, validation, PDF/A, PDF/UA, open source, CLI, industry standard, ISO 19005, ISO 14289]
related_entities:
  - entities/matterhorn-protocol.md
related_concepts:
  - concepts/pdf-a-standard.md
  - concepts/pdf-ua-standard.md
  - concepts/pdf-quality-gate-framework.md
source: |
  veraPDF 官網：https://verapdf.org/
  veraPDF GitHub：https://github.com/verapdf/verapdf
  PDF Association veraPDF 資源頁：https://pdfa.org/resource/verapdf/
---

# veraPDF Validator

## 概述

**veraPDF** 是行業支持的開源 PDF/A + PDF/UA 驗證工具，由 PDF 軟體開發者社群聯合開發，PDF Association 背書。

定位：數位長期保存（digital preservation）場景的首選工具，滿足以下需求：
- 所有 PDF/A 和 PDF/UA parts 和 conformance levels
- 開源免費，適合機構批量部署
- CLI + GUI，適合自動化腳本集成

## 支援標準

| 標準系列 | 版本 |
|---------|------|
| PDF/A（ISO 19005）| 1a, 1b / 2a, 2b, 2u / 3a, 3b, 3u / 4, 4e, 4f |
| PDF/UA（ISO 14289）| UA-1（ISO 14289-1:2014）/ UA-2（ISO 14289-2:2024）|

## 安裝

```bash
# macOS
brew install verapdf/verapdf/verapdf

# Linux（AppImage）
wget https://github.com/verapdf/verapdf/releases/latest/download/veraPDF Linux AppImage.gz
gunzip veraPDF*.AppImage.gz
chmod +x veraPDF*.AppImage
./veraPDF*.AppImage --version

# Docker（無需安裝）
docker run --rm verapdf/verapdf:latest --format text document.pdf
```

## CLI 基本用法

```bash
# 基本驗證（輸出至終端）
verapdf document.pdf

# XML 格式輸出（適合腳本解析）
verapdf --format xml --profile PDF/A-2b document.pdf

# 指定驗證剖象
verapdf --format text --profile PDF/A-3b document.pdf
verapdf --format text --profile PDF/UA-1 document.pdf

# 目錄批量驗證
verapdf --batch --recursive /path/to/pdf/folder/

# 顯示詳細失敗信息
verapdf --format text --detail document.pdf
```

## 輸出格式

**text 格式**（人類可讀）：
```
veraPDF Validation Report
Profile: PDF/A-2b
Statement: document.pdf passed validation (compliant)
Details: 0 errors, 0 warnings, passed validation
```

**XML 格式**（機器可讀）：
```xml
<validationResult>
  <profile>PDF/A-2b</profile>
  <statement>document.pdf passed validation (compliant)</statement>
  <passed>true</passed>
  <totalErrors>0</totalErrors>
</validationResult>
```

## 與 Hermes pdf-edit 的集成

在 `pdf-design-spec` SSOT 框架下，veraPDF 構成 PDF Quality Gate L4（合規層）的主力工具：

```python
import subprocess
import xml.etree.ElementTree as ET

def verify_pdfa3b(path: str) -> dict:
    """用 veraPDF 驗證 PDF/A-3b 合規性"""
    result = subprocess.run(
        ['verapdf', '--format', 'xml', '--profile', 'PDF/A-3b', path],
        capture_output=True, text=True
    )
    # 解析 XML 輸出
    # return {"passed": bool, "errors": int, "warnings": int}
```

## 測試套件

veraPDF 自身通過 **Isartor Test Suite** 驗證——PDF Association 提供的標準化測試套件，用於確保 veraPDF 對 PDF/A-1 的實現正確性。

## 局限性

- 需安裝（CLI/GUI 非 Web 可達）
- Java 依賴（背底 JVM）
- 對某些自訂 PDF 功能（如部分 DRM）可能報告 false positive
- PDF/UA 的 47 個需人工判斷的檢查點：veraPDF 會報告"Warn"，需 PAC + 人工覆核

