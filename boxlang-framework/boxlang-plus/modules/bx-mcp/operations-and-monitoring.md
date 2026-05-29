---
description: Monitor your BoxLang runtime with health checks, performance snapshots, JVM diagnostics, and scheduler oversight.
icon: heartbeat
---

# ⚡ Operations & Monitoring

This guide covers the operational workflows for monitoring your BoxLang runtime using the `bx-mcp` tools.

---

## 🏥 Health Checks

### System-Wide Health

The `system_get_health` tool provides a single round-trip health assessment of all subsystems:

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"system_get_health","arguments":{}},"id":"1"}'
```

This returns a consolidated report with:

- **Overall status** — `healthy`, `warning`, or `critical`
- **Score** — 0-100 numeric score (weakest-link model)
- **Per-subsystem health** — datasources, caches, watchers, schedulers, executors, web server
- **All issues** — Merged across subsystems with severity and suggested actions

### Subsystem Health Checks

For drill-down analysis, each subsystem has its own health tool:

| Domain | Health Tool | What It Checks |
| --- | --- | --- |
| Caches | `cache_get_health` | Hit rates, eviction thrashing, enabled status |
| Datasources | `datasource_get_health` | Pool utilization, saturation, thread waiters |
| Executors | `executor_get_health` | Saturation, queue depth, shutdown status |
| Schedulers | `scheduler_get_health` | Task failures, paused tasks, scheduler state |
| Watchers | `watcher_get_health` | Error counts, stopped watchers |
| Web Server | `undertow_get_health` | Worker saturation, queue depth, error rates |

---

## 📊 Performance Snapshot

The `performance_get_snapshot` tool captures a holistic view of runtime performance in a single call:

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"performance_get_snapshot","arguments":{}},"id":"1"}'
```

The snapshot includes:

- **Memory** — Heap and non-heap usage, pool breakdown
- **Garbage Collection** — Collection counts and cumulative time
- **CPU** — Available processors, system load, process CPU time
- **Threads** — Thread counts by state
- **Top Executors** — Most utilized async executor pools
- **Slow Queries** — Recent slow SQL samples
- **Slow Requests** — Recent slow inbound requests
- **Slow HTTP** — Recent slow outbound HTTP/SOAP calls
- **Buffer Pools** — Direct and mapped buffer usage
- **Web Server** — Undertow worker pool and listener metrics (when available)
- **Health Report** — Built-in structured health assessment with recommendations

---

## 💻 JVM Monitoring

### Memory Analysis

```bash
# Quick memory overview
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_memory_info","arguments":{}},"id":"1"}'

# Detailed memory pool breakdown (Eden, Survivor, Old Gen, Metaspace, Code Cache)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_memory_pool_details","arguments":{}},"id":"2"}'
```

### Thread Analysis

```bash
# Thread counts by state
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_thread_info","arguments":{}},"id":"1"}'

# Full thread dump with stack traces
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_thread_dump","arguments":{}},"id":"2"}'

# Hot threads (top CPU consumers over a 3-second sampling window)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_hot_threads","arguments":{"durationMs":3000,"topN":5}},"id":"3"}'

# Top allocator threads (driving GC churn)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_top_allocators","arguments":{"durationMs":3000,"topN":10}},"id":"4"}'

# Deadlock detection
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_deadlocks","arguments":{}},"id":"5"}'
```

### Garbage Collection

```bash
# GC statistics
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_gc_info","arguments":{}},"id":"1"}'

# Trigger GC manually (emergency use only)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_trigger_gc","arguments":{}},"id":"2"}'
```

### Resource Usage

```bash
# File descriptors (Unix/macOS)
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_file_descriptors","arguments":{}},"id":"1"}'

# Disk usage across all volumes
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_disk_usage","arguments":{}},"id":"2"}'
```

---

## ⏰ Scheduler Monitoring

### View All Schedulers and Tasks

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"scheduler_get_all","arguments":{}},"id":"1"}'
```

### Check Scheduler Health

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"scheduler_get_health","arguments":{}},"id":"1"}'
```

### Get Task Execution Statistics

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"scheduler_get_all_task_stats","arguments":{}},"id":"1"}'
```

---

## 📈 Executor Monitoring

### View All Async Executors

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"executor_get_all","arguments":{}},"id":"1"}'
```

### Check Executor Health

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"executor_get_health","arguments":{}},"id":"1"}'
```

---

## 🌐 Web Server Monitoring

### Undertow Server Stats

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"undertow_get_stats","arguments":{}},"id":"1"}'
```

Returns worker pool metrics (core, max, busy, queue depth), IO pool, listener connection/request/error counts, and WebSocket connections.

---

## 📋 Daily Health Check Script

Here's a BoxLang script that performs a comprehensive daily health check:

```js
// Daily Health Check Script
// Run this on a schedule to monitor runtime health

// 1. System health overview
var health = mcpServer( "boxlang" ).callTool( "system_get_health", {} )
systemOutput( "Health Status: #health.status# (#health.score#/100)" )

// 2. Performance snapshot
var perf = mcpServer( "boxlang" ).callTool( "performance_get_snapshot", {} )
systemOutput( "Heap Used: #perf.heap.percentUsed#%" )
systemOutput( "Active Threads: #perf.threads.active#" )

// 3. Check for issues
if ( health.score < 80 ) {
  for ( var issue in health.issues ) {
    systemOutput( "[#issue.severity#] #issue.code#: #issue.message#" )
  }
}

// 4. Trigger GC if heap is critical
if ( perf.heap.percentUsed > 95 ) {
  systemOutput( "WARNING: Heap critical (>95%). Triggering GC..." )
  mcpServer( "boxlang" ).callTool( "jvm_trigger_gc", {} )
}
```

---

## 📚 Next Steps

- [Data Layer Diagnostics](data-layer-diagnostics.md) — Cache analysis, datasource health, and slow SQL diagnosis
- [Incident Response](incident-response.md) — Triage and error response workflows
- [MCP Prompts Reference](reference/prompts/README.md) — Pre-built diagnostic prompts
