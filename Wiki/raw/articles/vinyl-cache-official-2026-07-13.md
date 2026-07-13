---
title: Vinyl Cache（formerly Varnish Cache）Official Documentation
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [vinyl-cache, varnish, http-accelerator, reverse-proxy, caching, vcl, open-source, bsd]
urls:
  - https://vinyl-cache.org/intro/
  - https://varnish-cache.org/docs/
  - https://varnish-cache.org/docs/users-guide/
  - https://varnish-cache.org/docs/reference/
license: two-clause BSD license
version: 9.0.0（Stable, 2026-03-16）
developers:
  - Poul-Henning Kamp（Lead architect, FreeBSD developer）
  - Redpill-Linpro（Original infrastructure）
  - Varnish Software（Commercial support）
---

# Vinyl Cache Official Documentation — Source Material

> ⚠️ 注意：專案於 2025-2026 年間從 **Varnish Cache** 改名為 **Vinyl Cache**（名稱衝突）。版本 9.0.0（2026-03-16）是當前 stable release。

## 攝入來源（完全合規）

| 來源 | URL |
|------|-----|
| 官方 Intro | https://vinyl-cache.org/intro/ |
| Users Guide | https://varnish-cache.org/docs/users-guide/ |
| Reference Manual | https://varnish-cache.org/docs/reference/ |
| VMODs Directory | https://vinyl-cache.org/vmods |
| Wikipedia | https://en.wikipedia.org/wiki/Vinyl_Cache |

**不使用**：ebooks.karbust.me（未授權盜版 PDF）

## 專案起源

| 項目 | 內容 |
|------|------|
| **發起** | 2005 年，挪威報紙 Verdens Gang（VG）線上版 |
| **Lead architect** | Poul-Henning Kamp（丹麥 FreeBSD 知名開發者）|
| **Original infra** | Linux consulting company Linpro（挪威）|
| **Spin-off** | Varnish Software（商業支援）|
| **v1.0 release** | September 2006 |
| **改名時機** | v8.0（2025-09）到 v9.0（2026-03）之間 |

## 核心定位

**Vinyl Cache** = HTTP accelerator = caching HTTP reverse proxy

> 安裝在任何 HTTP 伺服器前面，配置它快取內容。速度非常快，通常提升 300-1000 倍。

| 與其他軟體對比 | 說明 |
|---------------|------|
| vs Squid | Squid 最初是 client-side cache；Vinyl Cache 從一開始就是 HTTP accelerator |
| vs Apache/nginx | Apache/nginx 主要是 origin server；Vinyl Cache 專注 HTTP 加速 |
| vs 其他 proxy | 其他 proxy 支援 FTP/SMTP；Vinyl Cache 專注 HTTP |

## 架構特色

### 1. Virtual Memory 設計
- 資料存在 virtual memory
- 由 OS 決定什麼存 memory、什麼 swap 到磁碟
- **關鍵**：避免 OS 快取資料時 application 又要把資料寫到磁碟

### 2. 高度 Threaded
- 每個 client connection 由獨立 worker thread 處理
- 當 worker thread 數量達到上限，connections 進入 overflow queue
- Queue 滿時 → 拒絕新連線

### 3. VCL（Varnish Configuration Language）
- Domain-specific language（DSL）
- 寫 policies 決定如何處理 incoming requests
- **VCL → C code → compiled shared object → loaded into accelerator**
- 可在 runtime 重新編譯、載入、啟用，**不需要重啟**

### 4. Shared Memory Logging
- 減少 fast path 的 system calls
- Log 資料存在 shared memory
- 監控、過濾、格式化、寫入磁碟由獨立 application 處理

## Users Guide 結構（完整章節）

### Users Guide 章節

| 章節 | 內容 |
|------|------|
| **The Big Varnish Picture** | 整體架構 |
| **Starting and running Varnish** | 配置、storage、security、CLI |
| **VCL - Varnish Configuration Language** | vcl-subroutines、backend、health checks、grace mode、ESI |
| **Reporting and statistics** | 交易級監控、聚合統計 |
| **Varnish and Website Performance** | 提升 hitrate、HTTP headers、cache misses、purging |
| **Troubleshooting Varnish** | 常見問題、Guru meditation、crash handling |

### VCL 章節（核心）

| 子章節 | 內容 |
|--------|------|
| VCL Syntax | 語法 |
| Built-in VCL | 內建 VCL |
| Request and response VCL objects | req/bereq/obj/beresp/resp |
| Backend servers | 單一 backend、多 backend、virtual hosts |
| Directors | 負載平衡、health checks |
| Health checks | Probe 設計 |
| Grace mode and keep | 處理 backend 慢或掛掉的策略 |
| Separate VCL files | vmod、include |
| Using inline C | 用 C 擴展 Varnish |
| Device detection | 行動裝置偵測 |
| Edge Side Includes (ESI) | partial caching（fragment-level cache）|

### 監控/統計章節

| 章節 | 工具 |
|------|------|
| **Logging** | varnishlog、VSL |
| **Statistics** | varnishstat（快照）、VSC counters |
| **Real-time** | VarnishHist、VarnishTop |

## Reference Manual 結構

### VCL 語言

| 參考 | 內容 |
|------|------|
| VCL | Configuration Language 完整語法 |
| VCL Variables | req/bereq/obj/beresp/resp/變數 |
| VCL Steps | vcl_hash/vcl_miss/vcl_hit/vcl_deliver 等 |
| VCL backend configuration | backend/virtual director/probe |
| Varnish Processing States | 完整狀態機 |

### Bundled VMODs（內建模組）

| VMOD | 用途 |
|------|------|
| **blob** | BLOBs encoding/decoding |
| **cookie** | Cookie 處理 |
| **directors** | 負載平衡 director |
| **h2** | HTTP/2 傳輸控制 |
| **proxy** | PROXYv2 TLV attributes |
| **purge** | Cache purging |
| **std** | 標準工具（log/rollack/random 等）|
| **unix** | Unix domain sockets |

### CLI 工具

| 工具 | 用途 |
|------|------|
| **varnishadm** | CLI 控制 program |
| **varnish-cli** | 完整 CLI commands |
| **varnishd** | actual worker daemon |
| **varnishtest** | 測試 framework |
| **varnishstat** | 統計監控 |
| **varnishlog** | raw log |
| **varnishncsa** | NCSA format log |
| **varnishhist** | response time histogram |
| **varnishtop** | real-time activity |

## Performance 指標

| 指標類別 | 內容 |
|---------|------|
| **Client metrics** | connections、requests |
| **Cache performance** | hits、misses、evictions |
| **Thread metrics** | creation、failures、queues |
| **Backend metrics** | success、failure、health |

**典型速度**：20 Gbps on off-the-shelf hardware（Vinyl Cache 官網）

## VMOD 生態（30+ modules）

完整列表在 https://vinyl-cache.org/vmods

| VMOD | 用途 | License |
|------|------|--------|
| **awsrest** | AWS Signature V4 | FreeBSD |
| **blobdigest** | SHA256/HMAC for BLOBs | FreeBSD |
| **cluster** | Cache clustering | FreeBSD |
| **crypto** | RSA/DSA signatures | FreeBSD |
| **softpurge** | Soft purge（cache invalidation）| FreeBSD |
| **statsd** | StatsD integration | FreeBSD |
| **vslp** | Shard director（since v5.0）| FreeBSD |

## Hermes 對應評估

| Vinyl Cache 概念 | Hermes 對應 | 評估 |
|-----------------|------------|------|
| **VCL DSL** | SOUL/AGENTS/RULES/CODEX 核心檔（宣告式配置）| ✅ 可借鏡 |
| **Health checks** | MCP 連線監控（minimax）| ✅ 直接對應 |
| **Grace mode** | E-code 斷路器（fail-open/fail-close）| ✅ 可借鏡 |
| **Shared memory logging** | `~/.hermes/logs/` 全日誌 | ✅ 可借鏡 |
| **Cache invalidation（purge）** | `touch config.yaml` 觸發重載 | ✅ 直接對應 |
| **Backend health probes** | MCP minimax heartbeat | ✅ 直接對應 |
| **Thread pools** | `max_concurrent_children=3` | ✅ 可借鏡 |
| **ESI（Edge Side Includes）**| Hermès 模組化 Skill 設計 | ⚠️ 概念相似 |
| **Varnishstat** | token usage monitoring | ✅ 可借鏡 |
| **Hot reload VCL** | `touch config.yaml` + reload | ✅ 直接對應 |

**總評**：Vinyl Cache 的 **HTTP caching + health monitoring** 模式與 Hermes 的 **MCP 管理 + config reload** 有高度相似性。

## 對 Hermes 的設計啟示

### 1. VCL 的「宣告式 DSL」設計
Vinyl Cache 用 VCL 宣告 policies，編譯成 C → shared object → hot reload。
→ **Hermes 可以借鏡**：核心檔（SOUL/AGENTS）用宣告式語法，runtime 解析，hot reload。

### 2. Health Check 模式
```
backend probe = {
    .url = "/health";
    .timeout = 2s;
    .interval = 5s;
    .window = 5;
    .threshold = 3;
}
```
→ **Hermes 可以借鏡**：MCP heartbeat probe，window=5/threshold=3 確保可靠性。

### 3. Grace Mode
Backend 掛了 → 繼續 serving stale content while fetching fresh。
→ **Hermes 可以借鏡**：MCP 連線斷了 → 用 cache 繼續 service，async 恢復。

### 4. Shared Memory Logging
減少 fast path system calls → **Hermes 可以借鏡**：寫 logs 到 shared memory buffer，async 刷到磁碟。

## 版本歷史

| 版本 | 日期 | 重要變更 |
|------|------|---------|
| v1.0 | Sep 2006 | 初始 release |
| v2.0 | 2008 | major rewrite |
| v3.0 | 2011 | DNS resolver、Saint Mode |
| v4.0 | 2014 | vcl_backend, vmod |
| v5.0 | 2016 | HTTP/2 support、shard director |
| v6.0 | Mar 2018 | VMOD vtc、Persistency |
| v7.0 | Sep 2021 | HTTP/3 support、Arm64 |
| v8.0 | Sep 2025 | **改名 Vinyl Cache** |
| v9.0 | Mar 2026 | Current stable |

## 引用

```bibtex
@software{varnishcache2024,
  title={Vinyl Cache (formerly Varnish Cache)},
  author={Poul-Henning Kamp and Redpill-Linpro and Varnish Software},
  year={2026},
  version={9.0.0},
  license={BSD 2-Clause},
  url={https://vinyl-cache.org}
}
```