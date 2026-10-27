---
icon: chart-line
description: Performance snapshot and system health aggregation tools for holistic runtime monitoring.
---

# 📊 Performance & Health Tools

This page covers the performance snapshot tool (`PerformanceTools`) and the system health aggregator (`SystemTools`).

---

## Performance Snapshot — `PerformanceTools`

| Tool | Description |
| --- | --- |
| `performance_get_snapshot` | Single round-trip snapshot of memory, GC, CPU, threads, top memory pools, top executors, slow queries, slow requests, slow HTTP/SOAP calls, buffer pools, optional web server metrics, and a structured health report |

The `performance_get_snapshot` tool provides a holistic view of runtime health in a single call. It combines data from:

- **JVM Memory** — Heap and non-heap usage with pool breakdown
- **Garbage Collection** — Collection counts and cumulative time per algorithm
- **CPU** — Available processors, system load average, process CPU time
- **Threads** — Total, daemon, peak, and per-state counts
- **Top Memory Pools** — Highest-usage memory pools by percentage
- **Top Executors** — Most saturated async executor pools
- **Slow Queries** — Recent slow SQL samples
- **Slow Requests** — Recent slow inbound request samples
- **Slow HTTP** — Recent slow outbound HTTP/SOAP call samples
- **Buffer Pools** — Direct and mapped buffer usage
- **Web Server** — Undertow worker pool and listener metrics (when available)
- **Health Report** — Structured health assessment with score and issues

---

## System Health Aggregator — `SystemTools`

| Tool | Description |
| --- | --- |
| `system_get_health` | Unified health across all subsystems: datasources, caches, watchers, schedulers, executors, web server |

The `system_get_health` tool calls every subsystem health endpoint in a single round-trip and returns a consolidated report:

```json
{
  "status": "warning",
  "score": 65,
  "issues": [
    { "code": "executors:EXECUTOR_DEGRADED", "severity": "warning", ... }
  ],
  "subsystems": {
    "datasources": { "status": "healthy", "score": 100, "issues": [], ... },
    "caches": { "status": "warning", "score": 85, "issues": [...], ... },
    "watchers": { "status": "healthy", "score": 100, "issues": [], ... },
    "schedulers": { "status": "healthy", "score": 100, "issues": [], ... },
    "executors": { "status": "warning", "score": 65, "issues": [...], ... },
    "webServer": { "status": "healthy", "score": 100, "available": true, ... }
  },
  "scoreBreakdown": {
    "base": 100,
    "subsystems": [
      { "subsystem": "datasources", "score": 100, "status": "healthy" },
      ...
    ]
  }
}
```

The overall score is the **minimum subsystem score** (weakest-link model). Issue codes are prefixed with the subsystem name (e.g., `executors:EXECUTOR_DEGRADED`).

---

## Health Report Schema

All `*_get_health` tools return a consistent structured report. See the [Health Reports reference](../health-reports.md) for the complete schema, scoring model, and issue code catalog.
