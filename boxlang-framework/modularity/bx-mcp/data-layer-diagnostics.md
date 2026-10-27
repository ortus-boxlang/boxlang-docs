---
description: Diagnose cache performance, datasource health, slow SQL queries, and slow outbound HTTP/SOAP calls.
icon: database
---

# 🗄️ Data Layer Diagnostics

This guide covers how to diagnose data layer issues using the `bx-mcp` tools — cache performance, datasource connectivity, slow SQL queries, and slow outbound HTTP/SOAP calls.

---

## 🗃️ Cache Analysis

### View All Caches

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_all","arguments":{}},"id":"1"}'
```

Returns configuration, statistics, and status for every registered cache provider.

### Cache Health Assessment

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_health","arguments":{}},"id":"1"}'
```

The health report flags issues like:

| Issue | Severity | Trigger |
| --- | --- | --- |
| `CACHE_DISABLED` | warning | Cache not enabled |
| `CACHE_LOW_HIT_RATE` | warning | Hit rate < 30% |
| `CACHE_HIGH_EVICTIONS` | warning | Evictions >= cache size (thrashing) |

### Detailed Cache Statistics

```bash
# Get hit/miss/eviction counts and performance ratio
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_stats","arguments":{}},"id":"1"}'

# List all keys in a specific cache
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_keys","arguments":{"cacheName":"default"}},"id":"2"}'

# Get metadata for a specific cached object
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_key_metadata","arguments":{"cacheName":"default","key":"myKey"}},"id":"3"}'
```

### Cache Maintenance Operations

```bash
# Reap expired entries from all caches
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_reap_all","arguments":{}},"id":"1"}'

# Clear stats (reset hit/miss counters) for analysis
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_clear_stats","arguments":{}},"id":"2"}'
```

---

## 🔌 Datasource Connectivity

### View All Datasources

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_get_all","arguments":{}},"id":"1"}'
```

### Datasource Health Assessment

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_get_health","arguments":{}},"id":"1"}'
```

The health report flags issues like:

| Issue | Severity | Trigger |
| --- | --- | --- |
| `DS_POOL_NOT_STARTED` | warning | Pooling not started |
| `DS_POOL_HIGH_UTILIZATION` | warning | > 80% utilization |
| `DS_POOL_SATURATED` | critical | >= 95% utilization |
| `DS_POOL_THREADS_AWAITING` | warning | Waiting threads > 0 |

### Test a Specific Connection

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_test","arguments":{"dsn":"myDB"}},"id":"1"}'
```

Returns success/failure with timing information to quickly identify connectivity issues.

### Pool Metrics and Latency

```bash
# Basic pool metrics (active, idle, total, wait times)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_get_pool_metrics","arguments":{"dsn":"myDB"}},"id":"1"}'

# Pool latency histograms (requires enablePoolLatencyTracking: true)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_get_pool_latency","arguments":{"dsn":"myDB"}},"id":"2"}'
```

The pool latency tool returns p50/p95/p99/max for acquire, usage, and creation times, plus timeout counts. Enable it in your configuration:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "enablePoolLatencyTracking": true
      }
    }
  }
}
```

> Requires BoxLang 1.14+ with `ON_DATASOURCE_INITIALIZED` event support.

---

## 🐢 Slow SQL Diagnosis

The `bx-mcp` module captures slow SQL queries automatically when `slowSQL.enabled` is `true` (default).

### Configuration

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "slowSQL": {
          "enabled": true,
          "slowQueryThresholdMs": 1000,
          "slowQueryBufferSize": 200,
          "slowQueryCapture": true
        }
      }
    }
  }
}
```

### View Captured Slow Queries

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"sql_get_slow_queries","arguments":{"limit":20}},"id":"1"}'
```

### Aggregate Query Statistics

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"sql_get_query_stats","arguments":{}},"id":"1"}'
```

This groups captured queries by their original SQL and datasource, showing counts, average latency, and max latency.

### Runtime Configuration

```bash
# View current slow SQL config
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"sql_get_config","arguments":{}},"id":"1"}'

# Update threshold at runtime
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"sql_set_config","arguments":{"slowQueryThresholdMs":500}},"id":"2"}'

# Clear captured samples and stats
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"sql_clear","arguments":{}},"id":"3"}'
```

---

## 🌐 Slow HTTP/SOAP Diagnosis

The module captures slow outbound HTTP and SOAP calls automatically when `slowHttp.enabled` is `true` (default). Since SOAP calls transit through the same `BoxHttpClient` pipeline, they are captured automatically.

### Configuration

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "slowHttp": {
          "enabled": true,
          "slowHttpThresholdMs": 1000,
          "slowHttpBufferSize": 200,
          "slowHttpCaptureBody": false
        }
      }
    }
  }
}
```

### View Captured Slow Calls

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"slow_http_get_calls","arguments":{"limit":20}},"id":"1"}'
```

### Aggregate Call Statistics

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"slow_http_get_stats","arguments":{}},"id":"1"}'
```

Groups slow calls by destination host with count, average latency, and max latency.

### Runtime Configuration

```bash
# View current slow HTTP config
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"slow_http_get_config","arguments":{}},"id":"1"}'

# Clear captured samples and stats
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"slow_http_clear","arguments":{}},"id":"2"}'
```

---

## 📋 Troubleshooting Example: Slow Application Response

Here's a systematic approach to diagnose a slow-responding application:

**1. Check system health:**

```bash
# Get the big picture
curl -s ... -d '{"method":"tools/call","params":{"name":"performance_get_snapshot","arguments":{}}}'

# Check for heap pressure
curl -s ... -d '{"method":"tools/call","params":{"name":"jvm_get_memory_info","arguments":{}}}'
```

**2. Look for slow queries:**

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"sql_get_slow_queries","arguments":{"limit":20}}}'
```

**3. Check for slow HTTP calls to downstream services:**

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"slow_http_get_calls","arguments":{"limit":20}}}'
```

**4. Inspect connection pools:**

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"datasource_get_pool_metrics","arguments":{"dsn":"myDB"}}}'
```

**5. Check for thread contention:**

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"jvm_get_thread_info","arguments":{}}}'
curl -s ... -d '{"method":"tools/call","params":{"name":"jvm_get_hot_threads","arguments":{}}}'
```

---

## 📚 Next Steps

- [Operations & Monitoring](operations-and-monitoring.md) — Health checks and performance monitoring
- [Incident Response](incident-response.md) — Triage and error response workflows
- [MCP Tools Reference](reference/tools/README.md) — Complete tool catalog
