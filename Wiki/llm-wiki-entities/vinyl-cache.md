---
title: Vinyl Cache（formerly Varnish Cache）
created: 2026-07-13
updated: 2026-07-13
uid: e-4cba1476b41d
type: entity
tags: [vinyl-cache, varnish, http-accelerator, reverse-proxy, caching, vcl, open-source, bsd, Poul-Henning-Kamp]
sources:
  - raw/articles/vinyl-cache-official-2026-07-13.md
related:
  - "[[http-caching]]"
  - "[[reverse-proxy-pattern]]"
confidence: high
---

# Vinyl Cache（formerly Varnish Cache）

## 簡介

**Vinyl Cache** = HTTP accelerator（caching reverse proxy），最初名稱為 Varnish Cache，於 2025-2026 年間改名以避免名稱衝突。

> **Vinyl Cache** = Reverse caching proxy + HTTP accelerator for content-heavy dynamic web sites and APIs.

**規格**：
- **License**：Two-clause BSD（完全開源）
- **Written in**：C
- **Platforms**：BSD、Linux、Unix
- **Version**：9.0.0（2026-03-16 stable）
- **Website**：vinyl-cache.org

## 核心定位

| 定位 | 說明 |
|------|------|
| **Type** | HTTP accelerator / caching reverse proxy |
| **Focus** | 專注 HTTP，不同於支援 FTP/SMTP 的通用 proxy |
| **vs origin servers** | 不是 Apache/nginx 那樣的 origin server，而是加速器 |
| **vs client-side cache** | 不是 Squid 那樣的 client-side cache |

**速度**：typically speeds up delivery with a factor of **300-1000x**（官網）；seen delivering **20 Gbps on regular off-the-shelf hardware**。

## 與其他產品的對比

| 軟體 | 類型 | Vinyl Cache 差異 |
|------|------|----------------|
| **Squid** | Client-side cache | Varnish 從一開始就是 HTTP accelerator |
| **Apache** | Origin server | Vinyl Cache 放在前面做加速 |
| **nginx** | Origin server + reverse proxy | Vinyl Cache 專注 HTTP 加速 |
| **CDN** | Content delivery | Vinyl Cache 是 self-hosted 解決方案 |
| **Redis/Memcached** | In-memory cache | Vinyl Cache 是 HTTP-level cache，不是 key-value store |

## 架構特色

### 1. Virtual Memory Management
- 資料存在 virtual memory
- 由 OS 決定 memory vs disk
- **避免**：OS 快取資料時 application 又要寫入磁碟（double caching 問題）

### 2. Threaded Architecture
- 每個 client connection = 獨立 worker thread
- Worker thread limit → overflow queue → reject
- **避免**：block I/O 影響其他 connections

### 3. VCL（Varnish Configuration Language）
- DSL for HTTP request policies
- **編譯流程**：VCL → C code → compiled .so → loaded into accelerator
- **Hot reload**：不需要重啟就能載入新 VCL
- **內建**：vcl_hash/vcl_miss/vcl_hit/vcl_deliver 等 hooks

### 4. Shared Memory Logging
- 減少 fast path system calls
- Log → shared memory → 獨立 application 處理
- 不 blocking 主流程

## VCL 核心概念

### Request Lifecycle（VCL Steps）

```
vcl_recv       → 收到請求，決定如何處理（cache/pass/pipe）
vcl_hash       → 生成 cache key
vcl_miss       → cache miss，決定是否 fetch from backend
vcl_hit        → cache hit，可選擇 deliver 或 pass
vcl_hit_for_pass → 決定多久後重新 fetch
vcl_backend_fetch → 從 backend fetch
vcl_backend_response → backend 回應，可修改/判斷
vcl_deliver    → 回應 client 前最後 hook
vcl_synth      → synthetic 錯誤回應
vcl_init       → startup（載入 VMODs）
vcl_fini       → shutdown
```

### Backend Health Check

```
probe health_check {
    .url = "/health";
    .timeout = 2s;
    .interval = 5s;
    .window = 5;
    .threshold = 3;
}

backend origin {
    .host = "127.0.0.1";
    .port = "8080";
    .probe = health_check;
}
```

**健康判斷**：5 次檢查中至少 3 次成功 = healthy

### Grace Mode
Backend 掛了 → 繼續 serving **stale content**，同時 async fetch fresh content。

## 與 Hermes 的對應

| Vinyl Cache 概念 | Hermes 對應 | 評估 |
|-----------------|------------|------|
| **VCL DSL** | SOUL/AGENTS/RULES/CODEX 核心檔 | ✅ 概念相似 |
| **Backend health probe** | MCP minimax heartbeat | ✅ 直接對應 |
| **Grace mode** | E-code fail-open circuit breaker | ✅ 可借鏡 |
| **Hot reload VCL** | `touch config.yaml` → gateway reload | ✅ 直接對應 |
| **Thread pools** | `max_concurrent_children=3` | ✅ 概念相似 |
| **Shared memory log** | `~/.hermes/logs/` async log | ✅ 可借鏡 |
| **Cache invalidation (purge)** | `touch config.yaml` + MCP restart | ✅ 直接對應 |
| **Varnishstat** | token usage + errors.log | ✅ 概念相似 |
| **ESI** | Skill 模組化 include | ⚠️ 概念相似 |

## 對 Hermes 的設計啟示

### 1. Health Check Window/Threshold
Vinyl Cache 的 `window=5, threshold=3` 模式（5 次中至少 3 次成功）比簡單的 ping 更可靠。

**Hermes 應用**：MCP minimax heartbeat 改用 sliding window 判斷：
```python
# 而不是簡單的 connected/disconnected
window = 5
threshold = 3
success_count = count_recent_heartbeats(window=5)
is_healthy = success_count >= 3
```

### 2. Grace Mode（Stale-while-Revalidate）
Vinyl Cache 在 backend 恢復時 serving stale content → **Hermes 應用**：
- MCP 連線斷了 → 用上次成功結果（cache）繼續 service
- Async 嘗試 reconnect，不 blocking user

### 3. VCL DSL → Hermes Config DSL
Vinyl Cache 的 VCL 被編譯成 C → .so → hot reload。
**Hermes 應用**：核心檔翻譯成 internal representation → hot reload without restart。

## 作者：Poul-Henning Kamp

| 項目 | 內容 |
|------|------|
| **Role** | Lead architect and developer |
| **背景** | 丹麥獨立 consultant、知名 FreeBSD developer |
| **著作** | 多個 BSD 系統軟體 |
| **發起原因** | 2005 年挪威報紙 VG 需要加速 web |

> **名言**：「Varnish is really, really fast. It is usually bound by the speed of the network, effectively turning performance into a non-issue.」

## 商業支援

| 公司 | 服務 |
|------|------|
| **Varnish Software** | Commercial support、training、consulting |
| **UPLEX** | High-performance VMODs（cluster/crypto/blobdigest）|
| **Allenta Consulting** | DevOps consulting |

## 資源

- **官網**：https://vinyl-cache.org
- **官方文檔**：https://varnish-cache.org/docs/
- **Users Guide**：https://varnish-cache.org/docs/users-guide/
- **VMODs**：https://vinyl-cache.org/vmods
- **GitHub**（已移出）：https://code.vinyl-cache.org

## 引用

```bibtex
@software{vinylcache2026,
  title={Vinyl Cache (formerly Varnish Cache)},
  author={Poul-Henning Kamp and Redpill-Linpro and Varnish Software},
  year={2026},
  version={9.0.0},
  license={BSD 2-Clause},
  url={https://vinyl-cache.org}
}
```