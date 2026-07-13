---
uid: 20260713-pdf-a-standard
name: PDF/A ISO 19005 標準
aka: [PDF/A, PDF/A-1, PDF/A-2, PDF/A-3, PDF/A-4, archival PDF, ISO 19005]
type: concept
tags: [PDF, ISO 19005, PDF/A, archival, long-term preservation, veraPDF, conformance]
related_entities:
  - entities/verapdf-validator.md
related_concepts:
  - concepts/pdf-ua-standard.md
  - concepts/pdf-quality-gate-framework.md
  - concepts/pdf-preflight-technology.md
trigger: |
  PDF/A, PDF/A-1b, PDF/A-2b, PDF/A-3b, PDF/A-4, ISO 19005, 長期保存, 字體嵌入,
  veraPDF, 合規驗證, Preflight, 歸檔標準, XMP metadata, JPEG2000, PDF/A-3
source: |
  Nutrient PDF/A 完全指南：https://www.nutrient.io/blog/what-is-pdf-a/
  PDF Association ISO 19005 資源：https://pdfa.org/resource/iso-19005-1-pdf-a-1/
  veraPDF 官網：https://verapdf.org/
---

# PDF/A ISO 19005 標準

## 定義

PDF/A（Portable Document Format / Archive）是一個 ISO 標準系列（ISO 19005），定義了 PDF 的長期保存子集，確保文檔在未來任何技術環境下都能保持原始視覺外觀。

核心原則：**自包含**（無外部引用）、**字體嵌入**、**無加密**、**設備無關色彩**。

## 版本家族

| 版本 | 基於 | 發布 | 核心創新 |
|------|------|------|---------|
| PDF/A-1 | PDF 1.4 | 2005 | 首批標準；禁止透明度 |
| PDF/A-2 | PDF 1.7 | 2011 | JPEG2000、透明度、嵌套 PDF |
| PDF/A-3 | PDF 1.7 | 2012 | 解除附件禁令（CSV/XML/其他 PDF）|
| PDF/A-4 | PDF 2.0 | 2019 | PDF 2.0 功能；PAdES 簽章；3D 內容 |

### 合規層級

| 後綴 | 全稱 | 保障 |
|------|------|------|
| `b` | Basic | 視覺外觀一致；字體嵌入 |
| `a` | Accessible | b + 語義標記結構（PDF/UA 前身）|
| `u` | Unicode | b + Unicode 文字映射（可靠全文萃取）|

**實務預設**：PDF/A-2b（通用）；PDF/A-2u（需文字萃取）；PDF/A-3b（需附件）；PDF/A-4（新項目）。

## PDF/A vs 普通 PDF

| 約束 | PDF/A | 普通 PDF |
|------|-------|---------|
| 字體嵌入 | ✅ 強制 | 建議 |
| 外部內容引用 | ❌ 禁止 | 允許 |
| JavaScript | ❌ 禁止 | 允許 |
| 音視頻 | ❌ 禁止 | 允許 |
| 加密 | ❌ 禁止 | 允許 |
| XMP metadata | ✅ 強制 | 可選 |
| 設備無關色彩 | ✅ 強制 | 可選 |

## 驗證工具生態

| 工具 | 類型 | 費用 |
|------|------|------|
| **veraPDF** | CLI/GUI | 免費開源 |
| Adobe Acrobat Preflight | 內嵌 | 商業 |
| PAC | 桌面工具 | 免費 |
| PDFix SDK | API | 商業 |
| CommonLook | 桌面工具 | 商業 |

**首選**：veraPDF（行業標準，行會背書，覆蓋所有 PDF/A + PDF/UA）

## Hermes 對接

`pdf-design-spec` TRAP 表中已定義：

| TRAP | 對應 PDF/A 約束 |
|------|----------------|
| TRAP-OPT-4 | `garbage=4` 破壞 PDF/A 相容性 |
| TRAP-CJK-005 | PDF/A + CJK 全字體嵌入 → 檔案過大（需子集化）|
| TRAP-SIG-3 | PDF/A-3 不允許 LTV 簽章附件 |

