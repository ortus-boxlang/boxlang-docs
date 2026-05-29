---
icon: magnifying-glass
description: Pre-built prompts for thread dump analysis, error investigation, logging audits, class loader diagnostics, CPU profiling, and subsystem auditing.
---

# 🔍 Diagnostics & Auditing Prompts

## Diagnostics

| Prompt | Description | Arguments |
| --- | --- | --- |
| `thread_dump_analysis` | JVM thread dump: identifies deadlocks, blocked threads, pool saturation, long-running operations | — |
| `investigate_errors` | Recent log error investigation: patterns, root causes, fixes | `loggerName`, `keyword` *(optional)* |
| `logging_infrastructure_review` | Logging infrastructure audit: log levels, appenders, recent error patterns | — |
| `class_loader_diagnostics` | Class loader health: resolver cache, loader count, deployment mode, runtime home | — |
| `jvm_resource_audit` | OS-level JVM resource audit: file descriptors, disk space on all volumes, CPU load, key system properties — capacity planning and resource leak detection | — |
| `cpu_profiling` | Live CPU profiling via hot-thread and allocation-heavy-thread sampling over a configurable window; correlates with GC activity and thread dumps | `durationMs` *(optional, default: 3000)*, `topN` *(optional, default: 10)* |

## Auditing

| Prompt | Description | Arguments |
| --- | --- | --- |
| `module_audit` | All registered modules: status, version, BIFs, components, interceptors, configuration | — |
| `interceptor_registry_audit` | Interceptor/event system: registered points, listener counts, coverage gaps | — |
| `scheduler_status_report` | Scheduler task execution history, upcoming runs, failures | `schedulerName` *(optional)* |
| `application_lifecycle_status` | All active applications: uptime, session counts, expired apps, load indicators | — |
| `http_connectivity_audit` | Outbound HTTP and SOAP client activity: connections, pool usage, errors | — |
| `file_watcher_health` | File watcher health check: running vs. stopped state, events processed, error counts; flags stalled or failing watchers | — |
