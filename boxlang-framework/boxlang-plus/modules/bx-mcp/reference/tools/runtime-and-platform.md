---
icon: cube
description: Runtime introspection and JVM diagnostics tools for querying BoxLang configuration, BIFs, components, and JVM health.
---

# 🖥️ Runtime & Platform Tools

This page covers tools for BoxLang runtime introspection (`BoxLangTools`) and JVM diagnostics (`JVMTools`).

---

## Runtime & Configuration — `BoxLangTools`

| Tool | Description |
| --- | --- |
| `runtime_get_info` | BoxLang version, JVM environment, OS details, start time, uptime, and license status |
| `runtime_get_license_status` | Current license status: trial mode, validity, expiration, product info (no sensitive tokens) |
| `runtime_get_config` | Full runtime configuration: datasources, caches, executors, logging, security, schedulers |
| `runtime_get_config_value` | Get a specific config value by dotted path (e.g. `caches.default.provider`) |
| `runtime_config_diff` | Diff live BoxRuntime configuration against `boxlang.json` on disk |
| `runtime_get_bif_summary` | BIF counts by category and sorted name list |
| `runtime_get_bif_info` | Detailed metadata for a specific BIF: signature, parameters, documentation |
| `runtime_search_bifs` | Search BIFs by keyword |
| `runtime_get_component_summary` | All registered components with total count |
| `runtime_get_component_info` | Metadata for a specific component: methods, properties, inheritance |
| `runtime_search_components` | Search components by keyword |
| `runtime_get_global_services` | All registered global runtime services |
| `runtime_toggle_debug_mode` | Toggle BoxLang debug mode on/off |
| `runtime_get_class_resolver_info` | Class resolver prefixes, cache size, dynamic class loader count |
| `runtime_clear_system_cache` | Clear compiled class caches (template, function, component, etc.) |
| `runtime_clear_page_pool` | Clear the Boxpiler page pool of compiled class instances |

---

## JVM Diagnostics — `JVMTools`

| Tool | Description |
| --- | --- |
| `jvm_get_memory_info` | Heap and non-heap memory: used, committed, max, free, percent used |
| `jvm_get_memory_pool_details` | Memory pool breakdown: Eden, Survivor, Old Gen, Metaspace, Code Cache |
| `jvm_get_thread_info` | Thread counts: total, daemon, peak, started, by state |
| `jvm_get_thread_dump` | Full JVM thread dump with stack traces |
| `jvm_get_hot_threads` | Top-N CPU-consuming threads over a sampling window using ThreadMXBean CPU-time deltas; includes stack traces |
| `jvm_get_top_allocators` | Top-N thread allocators over a sampling window using per-thread allocated-bytes deltas; includes stack traces and allocation rate |
| `jvm_get_deadlocks` | Detects deadlocked threads; returns participant stacks, waited lock owner, locked monitors, and synchronizers |
| `jvm_get_cpu_info` | Available processors, system load average, process CPU time |
| `jvm_get_gc_info` | GC algorithm statistics: collection count, cumulative collection time |
| `jvm_trigger_gc` | Manually trigger a garbage collection; returns before/after memory stats |
| `jvm_trigger_heap_dump` | Trigger an on-demand JVM heap dump (`.hprof`) to the configured `heapDumpDir` |
| `jvm_get_class_loading_info` | Currently loaded, total loaded, and total unloaded class counts |
| `jvm_get_runtime_info` | JVM name, vendor, version, uptime |
| `jvm_get_system_properties` | All JVM system properties |
| `jvm_get_environment_variables` | JVM environment variables (sensitive values masked) |
| `jvm_get_operating_system_info` | OS name, version, architecture, available processors |
| `jvm_get_file_descriptors` | Open and max file descriptor counts plus utilization percent (Unix/Linux/macOS only) |
| `jvm_get_disk_usage` | Disk usage for all mounted volumes and BoxLang-relevant paths (temp, logs, home, working directory) |

### Hot Threads Sampling

`jvm_get_hot_threads` identifies hot threads by taking CPU-time snapshots, waiting for a sampling window, and ranking threads by CPU delta:

- Default arguments: `durationMs=3000`, `topN=5`, `stackDepth=20`
- Single-window delta sampler (not an interval profiler)
- Best for quick triage of top CPU consumers

### Top Allocators Sampling

`jvm_get_top_allocators` identifies allocation-heavy threads by comparing per-thread allocated bytes over a sampling window:

- Default arguments: `durationMs=3000`, `topN=10`
- Best for finding requests driving young-generation GC churn

### Deadlock Detection

`jvm_get_deadlocks` returns an empty array when no deadlock exists. When a deadlock is found, each array entry includes:
- Thread ID, name, state, stack trace
- Lock being waited on and its owner
- Locked monitors and synchronizers
