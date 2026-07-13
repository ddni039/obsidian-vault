---
uid: 20260713-pdf-quality-gate-framework
name: PDF Quality Gate 四層審查框架
aka: [PDF Quality Gate, 四層審查, L1 L2 L3 L4, PDF/A, PDF/UA, preflight, Matterhorn]
type: concept
tags: [PDF, quality gate, preflight, PDF/A, PDF/UA, Matterhorn, veraPDF, conformance, audit, 御史]
related_entities:
  - entities/verapdf-validator.md
  - entities/matterhorn-protocol.md
related_concepts:
  - concepts/pdf-a-standard.md
  - concepts/pdf-ua-standard.md
  - concepts/pdf-tagged-structure.md
trigger: |
  PDF 審查, Quality Gate, 四層審查, preflight, 合規檢測, PDF/A, PDF/UA,
  Matterhorn, veraPDF, 御史, 交付前檢查, T1-T14, 國際標準, ISO 19005,
  ISO 14289, 長期保存, 可及性, 無障礙, 結構驗證, 語義審查
source: |
  整合自 pdf-edit SKILL.md T1-T14、物理驗證、TRAP-TRAP 及本輪 research
---

# PDF Quality Gate 四層審查框架

## 動機

現有 `pdf-edit` skill 的 T1-T14 物理驗證解決了「燒出來的 PDF 物理上是否正確」的問題，但沒有解決「PDF 是否符合國際標準」的問題。Quality Gate 框架將兩者整合，構成完整的交付前審查體系。

## 四層架構

```
┌─────────────────────────────────────────────┐
│  L4 合規層  ← 新增：PDF/A + PDF/UA 標準合規  │
├─────────────────────────────────────────────┤
│  L3 語義層  ← 像素差異、視覺回放、內容完整性  │
├─────────────────────────────────────────────┤
│  L2 結構層  ← 版本 Diff、頁面結構、Metadata  │
├─────────────────────────────────────────────┤
│  L1 物理層  ← T1-T14，坐標、字體、色彩、佈局  │
└─────────────────────────────────────────────┘
```

### L1：物理層（T1-T14）

基於 `pdf-edit` 操作層現有 T1-T14 清單，用 pymupdf + PIL 物理測量：
- T1：文件可開啟、完整
- T2：頁數正確
- T3：字體嵌入（CJK 子集化）
- T4：色彩空間正確
- T5：坐標系合規（G-CVR-*）
- T6：GrayLine 存在且位置正確
- T7：Pro-Tip 無碰撞
- T8：KPI 柵格撐滿版
- T9：分欄無重疊
- T10：頁眉/頁腳距離合規
- T11：章節進度正確
- T12：表格 GRID 完整
- T13：圖表嵌入無失真
- T14：Metadata 完整

### L2：結構層

使用 PyMuPDF + pikepdf 提取結構，difflib 文字比對：
- 版本-diff（L2）：PyMuPDF 提取文字 → unified_diff
- 結構性操作：頁面合併/拆分/旋轉/裁切
- Metadata 安全寫入：`reader.metadata` → merge → `writer.add_metadata(merged)`

### L3：語義層

像素級比對，模擬視覺回放：
- 版本-diff（L3）：`pdf2image` → PIL `ImageChops.difference()`
- 可及性抽樣：5 頁隨機抽樣 → 螢幕閱讀器模擬
- 文字萃取完整性：pymupdf `get_text()` 覆蓋率

### L4：合規層（新增）

國際標準認證：

| 子層 | 標準 | 工具 | 通過條件 |
|------|------|------|---------|
| L4-A | PDF/A-3b | veraPDF CLI | `passed=true`, `totalErrors=0` |
| L4-B | PDF/UA-1 | veraPDF + PAC | `passed=true`, Matterhorn FAIL ≤ 0 |
| L4-C | Tagged PDF 結構抽檢 | pikepdf 讀 StructTreeRoot | 抽查 3 頁，標籤完整 |
| L4-D | Matterhorn 檢查點覆蓋 | PAC 工具 | 31 檢查點 Warn ≤ 3 |

## 與 Martin Gluhak Quality Gate 的映射

Martin Gluhak 2022 論文的 Quality Gate 概念映射：

| Martin QG 節點 | Hermes L 層 |
|---------------|------------|
| T1: Invoice Data Completeness | L2 結構層（Metadata）|
| T2: Visual Reproduction | L3 語義層（像素比對）|
| T3: Accessibility | L4 合規層（PDF/UA）|
| T4: Long-term Preservation | L4-A（PDF/A）|
| T5: Legal Acceptance | L4-B（PDF/UA + 法律合規）|

## L4 合規層詳細協議

### L4-A：PDF/A-3b 驗證腳本

```python
import subprocess, xml.etree.ElementTree as ET, sys

def verify_pdfa3b(pdf_path: str) -> dict:
    result = subprocess.run(
        ['verapdf', '--format', 'xml', '--profile', 'PDF/A-3b', pdf_path],
        capture_output=True, text=True, timeout=60
    )
    root = ET.fromstring(result.stdout)
    ns = {'v': 'http://www.verapdf.org/2018/validator'}
    statement = root.find('.//v:statement', ns)
    errors = root.find('.//v:totalErrors', ns)
    return {
        'passed': statement.text == 'passed validation',
        'errors': int(errors.text) if errors is not None else -1,
        'raw': result.stdout
    }
```

### L4-B：PDF/UA-1 Matterhorn 覆核

```python
def verify_pdfua1(pdf_path: str) -> dict:
    result = subprocess.run(
        ['verapdf', '--format', 'xml', '--profile', 'PDF/UA-1', pdf_path],
        capture_output=True, text=True, timeout=60
    )
    # 解析 veraPDF PDF/UA 結果
    # 注意：veraPDF 覆蓋所有 89 個可自動化的失敗條件
    # 剩餘 47 個需 PAC + 人工
    return parse_verapdf_xml(result.stdout)
```

### L4-C：Tagged PDF 結構抽檢

```python
import pikepdf

def spot_check_tagged_structure(pdf_path: str, sample_pages: list) -> dict:
    """抽查指定頁的結構樹"""
    with pikepdf.open(pdf_path) as pdf:
        findings = []
        for pnum in sample_pages:
            page = pdf.pages[pnum]
            struct = page.get('/StructTreeRoot')
            findings.append({
                'page': pnum,
                'has_struct_tree': struct is not None,
                'struct_type': str(struct.get('/Type')) if struct else None
            })
        return findings
```

## 失敗時的中斷原則

| 層 | 失敗行為 | 御史中斷點 |
|----|---------|---------|
| L1 | 任意 T FAIL | ✅ 立即停止，不燒錄 |
| L2 | Diff > 20% 頁數偏離 | ✅ 立即停止 |
| L3 | PSNR < 30dB 或 mismatch > 1% | ✅ 御史中斷 |
| L4-A | veraPDF errors > 0 | ⚠️ 合規警告，不中斷但紀錄 |
| L4-B | Matterhorn FAIL > 0 | ⚠️ 告知用戶，不中斷 |

> **注意**：L4-A/B 是「告知用戶」而非「中斷」，因為 Hermes 生成的 PDF 主要用戶是 Telegram 分享，PDF/A/UA 合規並非默認需求。Art Director 或 regulatory 場景有需要時才執行。

## 與 TRAP-TRAP 的接口

| TRAP ID | 觸發的 Gate |
|---------|-----------|
| TRAP-OPT-4 | L4-A（`garbage=4` 破壞 PDF/A）|
| TRAP-CJK-005 | L4-A（CJK 字體子集化）|
| TRAP-TAG-1~4 | L4-B（PDF/UA 結構失敗）|
| TRAP-SIG-1~3 | L4-A + L4-B（簽章與 PDF/A 衝突）|

