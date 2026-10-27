---
icon: database
description: Cache, datasource, and SQL diagnostic tools for monitoring and managing the BoxLang data layer.
---

# 🗄️ Data Layer Tools

This page covers tools for cache management (`CacheTools`), datasource management (`DatasourceTools`), and SQL diagnostics (`SQLTools`).

---

## Cache Management — `CacheTools`

| Tool | Description |
| --- | --- |
| `cache_get_all` | All registered cache providers with stats, configuration, status |
| `cache_get_names` | Cache provider names only |
| `cache_get_stats` | Detailed cache stats: hits, misses, evictions, performance ratio |
| `cache_get_keys` | All keys stored in a specific cache |
| `cache_get_size` | Number of elements in a specific cache |
| `cache_get_key_metadata` | Metadata for a specific cached object |
| `cache_has_key` | Check if a key exists in a cache |
| `cache_get_store_metadata` | Full store metadata report for a cache |
| `cache_clear` | Clear all elements from a specific cache |
| `cache_clear_item` | Remove a specific item from a cache |
| `cache_reap` | Reap (clean up expired entries) from a cache |
| `cache_clear_stats` | Reset hit/miss/eviction counters for a cache |
| `cache_clear_all` | Clear all elements from every registered cache |
| `cache_reap_all` | Reap expired entries from every registered cache |
| `cache_get_health` | Structured health assessment: status, score, issues with codes per cache |

---

## Datasource Management — `DatasourceTools`

| Tool | Description |
| --- | --- |
| `datasource_get_all` | All registered datasources with configurations and pool metrics |
| `datasource_get_names` | Datasource names only |
| `datasource_get` | Single datasource details with pool metrics |
| `datasource_has` | Check if a datasource is registered |
| `datasource_get_pool_metrics` | Connection pool metrics: active, idle, total connections, wait times |
| `datasource_get_config` | Datasource configuration (passwords masked) |
| `datasource_test` | Test a datasource connection; returns success/failure with timing |
| `datasource_get_health` | Structured health assessment: status, score, per-datasource pool utilization issues |
| `datasource_get_pool_latency` | Connection pool latency histograms: acquire/usage/creation p50/p95/p99/max/count + timeout count. Requires `enablePoolLatencyTracking: true` |

---

## SQL Diagnostics — `SQLTools`

| Tool | Description |
| --- | --- |
| `sql_get_slow_queries` | Recent captured slow query samples with optional limit and since filter |
| `sql_get_query_stats` | Aggregate slow query statistics by original SQL and datasource |
| `sql_clear` | Clear all captured slow-query samples and statistics |
| `sql_get_config` | Current slow SQL collector configuration |
| `sql_set_config` | Update slow SQL collector configuration at runtime |
