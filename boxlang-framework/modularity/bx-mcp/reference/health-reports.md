---
icon: clipboard-list
description: Structured health report schema, scoring model, and complete issue code catalog for all subsystems.
---

# 🏥 Health Reports Reference

All `*_get_health` tools (`cache_get_health`, `datasource_get_health`, `executor_get_health`, `scheduler_get_health`, `watcher_get_health`, `undertow_get_health`, `system_get_health`) return a consistent structured report that enables clients to rank, filter, and reason about runtime health programmatically.

---

## Standard Response Shape

```json
{
  "status": "healthy",
  "score": 85,
  "issues": [
    {
      "severity": "warning",
      "code": "DS_POOL_HIGH_UTILIZATION",
      "message": "Datasource 'mainDB' pool is under high load at 87% (28/32 active)",
      "suggestedAction": "Monitor pool utilization and consider increasing pool size",
      "entity": "mainDB",
      "entityMetrics": {
        "utilization": 87,
        "active": 28,
        "max": 32
      }
    }
  ],
  "scoreBreakdown": {
    "base": 100,
    "deductions": [
      {
        "code": "DS_POOL_HIGH_UTILIZATION",
        "severity": "warning",
        "penalty": 15
      }
    ]
  }
}
```

### Top-level Fields

| Field | Type | Description |
| --- | --- | --- |
| `status` | string | Overall health: `healthy`, `warning`, or `critical` |
| `score` | number | Numeric score 0–100 |
| `issues` | array | List of detected issues with severity, codes, and actions |
| `scoreBreakdown` | object | How the score was calculated |

### Issue Object

| Field | Type | Description |
| --- | --- | --- |
| `severity` | string | `info`, `warning`, or `critical` |
| `code` | string | Machine-readable issue code (see catalog below) |
| `message` | string | Human-readable description of the issue |
| `suggestedAction` | string | Recommended remediation |
| `entity` | string | The affected subsystem entity name |
| `entityMetrics` | object | Key metrics for the affected entity |

---

## Scoring Model

| Severity | Penalty | Score Range |
| --- | --- | --- |
| — | — | **80–100**: Healthy |
| `warning` | 25 per issue | **50–79**: Degraded |
| `critical` | 50 per issue | **0–49**: Critical |
| `info` | 5 per issue | No status change |

The **overall status** is determined by the lowest-severity bucket:
- If any issue is `critical` → status is `critical`
- If any issue is `warning` → status is `warning`
- Otherwise → status is `healthy`

---

## Issue Code Catalog

### Datasource Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `DS_POOL_NOT_STARTED` | warning | Pooling not started |
| `DS_POOL_HIGH_UTILIZATION` | warning | > 80% utilization |
| `DS_POOL_SATURATED` | critical | >= 95% utilization |
| `DS_POOL_THREADS_AWAITING` | warning | Waiting threads > 0 |

### Cache Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `CACHE_DISABLED` | warning | Cache not enabled |
| `CACHE_LOW_HIT_RATE` | warning | Hit rate < 30% |
| `CACHE_HIGH_EVICTIONS` | warning | Evictions >= cache size (thrashing) |

### Watcher Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `WATCHER_STOPPED` | warning | Watcher is stopped |
| `WATCHER_ERRORS` | warning | Consecutive errors > 0 |
| `WATCHER_HIGH_ERRORS` | critical | Consecutive errors >= 10 |

### Scheduler Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `SCHEDULER_NOT_STARTED` | warning | Scheduler not started |
| `SCHEDULER_ALL_TASKS_PAUSED` | warning | All tasks paused |

### Web Server Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `WEB_WORKER_SATURATED` | critical | Worker pool saturated |
| `WEB_WORKER_HIGH_LOAD` | warning | >= 80% utilization |
| `WEB_QUEUE_HIGH` | critical | Queue > 50% of max |
| `WEB_LISTENER_HIGH_ERROR_RATE` | warning | Error rate > 5% |
| `WEB_HIGH_CONNECTION_RATIO` | info | Connections >> workers |

### Executor Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `EXECUTOR_UNHEALTHY` | critical | Shutdown/terminated/critical state |
| `EXECUTOR_DEGRADED` | warning | Degraded/draining/idle state |
| `EXECUTOR_NEAR_SATURATION` | warning | High saturation score |

### Performance Issues

| Code | Severity | Trigger |
| --- | --- | --- |
| `JVM_HEAP_CRITICAL` | critical | Heap > 95% |
| `JVM_HEAP_PRESSURE` | warning | Heap > 85% |
| `JVM_BLOCKED_THREADS` | warning | Blocked threads > 0 |
| `PERF_SLOW_QUERIES` | info | Slow queries present |
| `PERF_SLOW_REQUESTS` | info | Slow requests present |
| `PERF_SLOW_HTTP` | info | Slow HTTP calls present |

---

## System Health Aggregator

The `system_get_health` tool calls every subsystem health endpoint and returns a consolidated report with:

- **Overall score** — The minimum subsystem score (weakest-link model)
- **Subsystem reports** — Each subsystem's health report
- **Merged issues** — Issues from all subsystems with prefixed codes (e.g., `executors:EXECUTOR_DEGRADED`)

```json
{
  "status": "warning",
  "score": 65,
  "issues": [
    { "code": "executors:EXECUTOR_DEGRADED", "severity": "warning", ... },
    { "code": "caches:CACHE_LOW_HIT_RATE", "severity": "warning", ... }
  ],
  "subsystems": {
    "datasources": { "status": "healthy", "score": 100, "issues": [] },
    "caches": { "status": "warning", "score": 85, "issues": [...] },
    "watchers": { "status": "healthy", "score": 100, "issues": [] },
    "schedulers": { "status": "healthy", "score": 100, "issues": [] },
    "executors": { "status": "warning", "score": 65, "issues": [...] },
    "webServer": { "status": "healthy", "score": 100, "available": true }
  }
}
```
