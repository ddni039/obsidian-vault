# PDF/A ISO 19005 標準護城河研究 | 2026-07-13

## 研究背景

現有 `pdf-edit` skill 已有 T1-T14 物理驗證清單、`pdf-design-spec` 有 TRAP-CJK/TRAP-COORD/TRAP-DRAW 等陷阱表，但**缺乏國際標準合規審查**——無法回答「這個 PDF 是否符合 PDF/A-3b？」、「它是否通過 veraPDF 驗證？」。本頁建立 PDF/A 全家族的 SSOT 知識體系。

---

## PDF/A 家族（ISO 19005）

| 版本 | 基於 | 發布 | 關鍵特性 |
|------|------|------|---------|
| PDF/A-1 | PDF 1.4 | 2005 | 最早版本；禁止透明度；禁止外部引用 |
| PDF/A-2 | PDF 1.7 | 2011 | 加入 JPEG2000、透明度、PDF/A-2u（Unicode）|
| PDF/A-3 | PDF 1.7 | 2012 | 解除文件附件禁令（可嵌入 CSV/XML/其他 PDF）|
| PDF/A-4 | PDF 2.0 | 2019 | 支持增強 PAdES 簽章、3D 內容、更強邏輯結構 |

### 合規層級（每版本均有）

| 層級 | 後綴 | 含義 |
|------|------|------|
| **b**（Basic）| `PDF/A-2b` | 保障視覺外觀長期一致；字體必須嵌入 |
| **a**（Accessible）| `PDF/A-1a` | 在 b 基礎上 + 標籤結構、語義標記（PDF/UA 前身）|
| **u**（Unicode）| `PDF/A-2u` | 在 b 基礎上 + Unicode 文字映射，支援可靠全文萃取 |

> **實務默認**：`PDF/A-2b` 是大多數用途的推薦預設（支持 JPEG2000 壓縮、透明圖層、嵌套 PDF）；若需可靠文字萃取，用 `PDF/A-2u`；新項目考慮 `PDF/A-4`。

---

## PDF/A 核心約束（與普通 PDF 的差異）

| 約束 | PDF/A 要求 | 普通 PDF |
|------|-----------|---------|
| 字體嵌入 | **強制** | 建議 |
| 外部引用 | **禁止** | 允許 |
| JavaScript | **禁止** | 允許 |
| 音視頻 | **禁止** | 允許 |
| 加密 | **禁止** | 允許 |
| XMP metadata | **強制** | 可選 |
| 設備無關色彩 | **強制** | 可選 |
| 長期可讀性 | **ISO 保障** | 不保證 |

---

## PDF/A-3 附加約束（最常用）

在 PDF/A-2 基礎上：
- 允許嵌入**非 PDF 附件**（CSV、XML、ODT 等）
- 附件必須符合相應標準（如 ZUGFeRD 電子發票）
- 附件仍須是自包含的（不得引用外部 URL）

---

## 主流驗證工具

| 工具 | 類型 | 覆蓋 | 備註 |
|------|------|------|------|
| **veraPDF** | 開源 CLI/GUI | PDF/A 全家族 + PDF/UA | 行業標準，PDF Association 背書 |
| **Adobe Acrobat Preflight** | 商業 | PDF/A + 自訂剖象 | 強大但昂貴 |
| **PAC (PDF Accessibility Checker) | 免費工具 | PDF/UA 專注 | 德國出版業標配 |
| **PDFix SDK | 商業 API | PDF/A + PDF/UA + WCAG | 支援批量自動修復 |
| **CommonLook Validator | 商業 | PDF/UA | 美國政府合規 |

### veraPDF（首選開源方案）

```bash
# 安裝（macOS）
brew install verapdf/verapdf/verapdf

# CLI 基本用法
verapdf --format text document.pdf
verapdf --format xml --profile PDF/A-2b document.pdf

# Docker
docker run --rm verapdf/verapdf:latest --format text document.pdf
```

XMP metadata 強制：veraPDF 嚴格檢查 XMP 是否存在且格式正確。

---

## Matterhorn Protocol（PDF/UA 合規測試模型）

ISO 14289 的**可測試實現**：31 個檢查點、136 個失敗條件（89 個可自動化、47 個需人工）。

### 核心檢查類別

| 類別 | 數量 | 說明 |
|------|------|------|
| Document requirements | ~5 | 標籤存在、語言、標題、加密 |
| Structure tags | ~15 | H1-H6 順序正確、P/L/TABLE 標記 |
| Non-text content | ~10 | Alt text 存在且有意義 |
| Tables | ~8 | 標題行、數據行區分、header cells |
| Forms | ~8 | 標籤、tab 順序、角色 |
| Navigation | ~10 | 書籤、標籤順序 |

### PAC 工具（Matterhorn 視覺化）

PAC（PDF Accessibility Checker）免費桌面工具，直接展示 Matterhorn 各檢查點 Pass/Warn/Fail 狀態。

---

## Preflight 技術原理

Preflight = PDF 交付前的**自動化合規體檢**：

```
Input PDF → Parse Structure → Match against Profile → Output: Pass / Warn / Fail + Details
```

**典型 Preflight 剖象**：
- PDF/A-3b 剖象：檢查字體嵌入、色彩空間、加密、元數據
- PDF/UA 剖象：檢查標籤樹、閱讀順序、Alt text、表格結構

**重要區分**：
- **PDF 語法驗證**（PDF 規範符合性）≠ **PDF/A 語義驗證**（ISO 19005 約束符合性）
- Preflight 做語義檢查；`pikepdf.check()` 做語法檢查

---

## Hermes PDF Quality Gate L4：PDF/A + PDF/UA 審查（新增）

在現有 `pdf-edit` T1-T14 基礎上，新增 **L4 合規層**：

| 新層級 | 檢查目標 | 工具 |
|--------|---------|------|
| **L4-A** | PDF/A-3b 結構合規 | veraPDF CLI（無需 GUI）|
| **L4-B** | PDF/UA-1 語義合規 | veraPDF + PAC |
| **L4-C** | 標籤結構抽檢 | pikepdf 讀取 StructTreeRoot |
| **L4-D** | Matterhorn 檢查點覆蓋 | 31 檢查點 × 5 頁抽樣 |

---

## 閱讀清單與參考資源

| 資源 | URL |
|------|-----|
| veraPDF 官網 | https://verapdf.org |
| PDF Association PDF/A 資源 | https://pdfa.org/resource/iso-19005-1-pdf-a-1/ |
| ISO 19005-1（PDF/A-1）| 可從 PDF Association 免費獲取 |
| PDF/A in a Nutshell 2.0 | PDF Association 免費下載 |
| Isartor Test Suite | PDF/A 開源測試套件 |
| PAC (PDF Accessibility Checker) | https://pac.pdf-accessibility.org |
| Callas Preflight 白皮書（2025）| https://callassoftware.com |
| Nutrient PDF/A 完全指南 | https://www.nutrient.io/blog/what-is-pdf-a/ |
| Nutrient PDF/UA 完全指南 | https://www.nutrient.io/blog/what-is-pdf-ua/ |

---

## 與現有 TRAP 表的接口

現有 TRAP-TRAP 陷阱已覆蓋：

| TRAP ID | 內容 | 對應 PDF/A 約束 |
|---------|------|----------------|
| TRAP-CJK-005 | PDF/A + CJK 全字體嵌入 → 檔案過大 | 字體子集化策略 |
| TRAP-OPT-4 | 壓縮破壞 PDF/A 相容性 | `garbage=4` 不應用於 PDF/A |
| TRAP-TAG-1~4 | Tagged PDF / PDF/UA 陷阱 | 直接對應 PDF/UA 需求 |
| TRAP-SIG-1~3 | 數位簽章與 PDF/A 衝突 | PDF/A-3 不允許 LTV 附件 |

