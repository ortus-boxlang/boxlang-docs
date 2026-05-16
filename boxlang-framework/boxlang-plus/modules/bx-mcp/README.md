---
description: >-
  Model Context Protocol server module for BoxLang runtime diagnostics,
  introspection, and operational automation.
icon: bot
---

# MCP +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://boxlang.io/plans). It requires the `bx-plus` and `bx-ai` modules.
{% endhint %}

The `bx-mcp` module exposes a production-ready MCP server for BoxLang so MCP-capable clients (AI agents, IDE assistants, automation tools) can inspect and operate a live runtime safely.

When enabled, the module auto-registers a `boxlang` MCP server and exposes an HTTP endpoint at `/~bxmcp/boxlang.bxm`.

## 🚀 Installation

### Via CommandBox

```bash
box install bx-plus,bx-ai,bx-mcp
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-ai bx-mcp
```

## ⚙️ Configuration

Configure `bx-mcp` in your `boxlang.json` under `modules.bxmcp.settings`:

```json
{
  "modules": {
    "bxmcp": {
      "enabled": true,
      "settings": {
        "enabled": true,
        "authToken": "FILL_THIS_OUT_ALWAYS",
        "allowedIPs": ["127.0.0.1"],
        "corsAllowedOrigins": [],
        "enableStats": true,
        "maxRequestBodySize": 0,
        "includedTools": ["*"],
        "excludedTools": []
      }
    }
  }
}
```

### Settings Reference

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Master switch for MCP server registration. |
| `authToken` | string | `""` | Bearer token required by clients. |
| `allowedIPs` | array | `["127.0.0.1"]` | IP allowlist with IP/CIDR support. |
| `corsAllowedOrigins` | array | `[]` | CORS allowlist with wildcard support. |
| `enableStats` | boolean | `true` | Enables server and tool usage statistics. |
| `maxRequestBodySize` | numeric | `0` | Request body limit in bytes, `0` means unlimited. |
| `includedTools` | array | `["*"]` | Tool whitelist. |
| `excludedTools` | array | `[]` | Tool blacklist applied after whitelist. |

{% hint style="warning" %}
For any non-local deployment, set `authToken` and tighten `allowedIPs` and `excludedTools`.
{% endhint %}

## 🧰 MCP Tools (118 Total)

The server exposes tools across 12 runtime domains. Each tool is an `@mcpTool` annotated method discovered automatically via classpath scanning.

### Runtime & Configuration — `BoxLangTools`

| Tool | Description |
| --- | --- |
| `get_runtime_info` | BoxLang version, JVM environment, OS details, start time, uptime |
| `get_runtime_config` | Full runtime configuration: datasources, caches, executors, logging, security, schedulers |
| `get_config_value` | Get a specific config value by dotted path (e.g. `caches.default.provider`) |
| `get_bif_summary` | BIF counts by category and sorted name list |
| `get_bif_info` | Detailed metadata for a specific BIF: signature, parameters, documentation |
| `search_bifs` | Search BIFs by keyword |
| `get_component_summary` | All registered components with total count |
| `get_component_info` | Metadata for a specific component: methods, properties, inheritance |
| `search_components` | Search components by keyword |
| `get_global_services` | All registered global runtime services |
| `toggle_debug_mode` | Toggle BoxLang debug mode on/off |
| `get_class_resolver_info` | Class resolver prefixes, cache size, dynamic class loader count |
| `clear_system_cache` | Clear compiled class caches (template, function, component, etc.) |
| `clear_page_pool` | Clear the Boxpiler page pool of compiled class instances |

### JVM Diagnostics — `JVMTools`

| Tool | Description |
| --- | --- |
| `get_memory_info` | Heap and non-heap memory: used, committed, max, free, percent used |
| `get_memory_pool_details` | Memory pool breakdown: Eden, Survivor, Old Gen, Metaspace, Code Cache |
| `get_thread_info` | Thread counts: total, daemon, peak, started, by state |
| `get_thread_dump` | Full JVM thread dump with stack traces |
| `get_cpu_info` | Available processors, system load average, process CPU time |
| `get_gc_info` | GC algorithm statistics: collection count, cumulative collection time |
| `trigger_gc` | Manually trigger a garbage collection; returns before/after memory stats |
| `get_class_loading_info` | Currently loaded, total loaded, and total unloaded class counts |
| `get_jvm_runtime_info` | JVM name, vendor, version, uptime |
| `get_system_properties` | All JVM system properties |
| `get_environment_variables` | JVM environment variables (sensitive values masked) |
| `get_operating_system_info` | OS name, version, architecture, available processors |

### Cache Management — `CacheTools`

| Tool | Description |
| --- | --- |
| `get_caches` | All registered cache providers with stats, configuration, status |
| `get_cache_names` | Cache provider names only |
| `get_cache_stats` | Detailed cache stats: hits, misses, evictions, performance ratio |
| `get_cache_keys` | All keys stored in a specific cache |
| `get_cache_size` | Number of elements in a specific cache |
| `get_cache_key_metadata` | Metadata for a specific cached object |
| `cache_key_exists` | Check if a key exists in a cache |
| `get_store_metadata_report` | Full store metadata report for a cache |
| `clear_all` | Clear all elements from a specific cache |
| `clear_item` | Remove a specific item from a cache |
| `reap_cache` | Reap (clean up expired entries) from a cache |
| `clear_cache_stats` | Reset hit/miss/eviction counters for a cache |
| `clear_all_caches` | Clear all elements from every registered cache |
| `reap_all_caches` | Reap expired entries from every registered cache |
| `get_cache_health_summary` | Health overview: total size, hit rates, status across all caches |

### Datasource Management — `DatasourceTools`

| Tool | Description |
| --- | --- |
| `get_datasources` | All registered datasources with configurations and pool metrics |
| `get_datasource_names` | Datasource names only |
| `get_datasource` | Single datasource details with pool metrics |
| `has_datasource` | Check if a datasource is registered |
| `get_pool_metrics` | Connection pool metrics: active, idle, total connections, wait times |
| `get_datasource_config` | Datasource configuration (passwords masked) |
| `test_datasource` | Test a datasource connection; returns success/failure with timing |
| `get_datasource_health` | Health summary of all datasources and their pools |

### Async Executors — `AsyncTools`

| Tool | Description |
| --- | --- |
| `get_executors` | All registered async executors with status, pool info, task stats |
| `get_executor_names` | Executor names only |
| `get_executor_info` | Detailed executor info: type, status, configuration |
| `get_executor_stats` | Pool utilization, queue status, task counts, health metrics |
| `get_executor_health` | Health report with issues, recommendations, alerts |
| `get_executor_health_summary` | Health summary across all executors |

### Schedulers — `SchedulerTools`

| Tool | Description |
| --- | --- |
| `get_schedulers` | All registered schedulers with configurations and tasks |
| `get_scheduler_names` | Scheduler names only |
| `get_scheduler` | Single scheduler details including tasks and records |
| `has_scheduler` | Check if a scheduler is registered |
| `get_task_stats` | Execution statistics for a specific task |
| `get_task_info` | Task details: configuration and metadata |
| `get_all_tasks` | All tasks across all schedulers |
| `run_task` | Force-run a scheduled task immediately |
| `pause_task` | Pause a scheduled task |
| `resume_task` | Resume a paused scheduled task |
| `pause_persisted_task` | Pause a disk-persisted task (updates `tasks.json`) |
| `resume_persisted_task` | Resume a disk-persisted task |
| `pause_all_persisted_tasks` | Pause all disk-persisted tasks (filterable by scheduler/group) |
| `resume_all_persisted_tasks` | Resume all disk-persisted tasks |
| `get_scheduler_health` | Health summary of all schedulers and tasks |
| `get_all_task_stats` | Task stats summary across all schedulers |
| `get_persisted_tasks` | All scheduled tasks persisted on disk (`tasks.json`) |

### Modules — `ModuleTools`

| Tool | Description |
| --- | --- |
| `get_modules` | All registered modules with configuration and status |
| `get_module_names` | Module names only |
| `get_module_info` | Full configuration and status for a specific module |
| `get_module_settings` | Settings for a specific module |
| `get_module_paths` | Registered module search paths |
| `reload_module` | Reload a specific module (unload, re-register, re-activate) |
| `reload_all_modules` | Reload all registered modules |
| `has_module` | Check if a module is registered |
| `get_module_stats` | Module statistics: total count, activated, enabled, etc. |

### Interceptors — `InterceptorTools`

| Tool | Description |
| --- | --- |
| `get_interception_points` | All registered interception point names (sorted) |
| `has_interception_point` | Check if a specific interception point is registered |
| `get_interceptor_states` | All interceptor states with listener counts |
| `get_interceptor_state` | Listener count for a specific event |
| `get_interceptor_summary` | Registry totals, active states, events with most listeners |

### Applications — `ApplicationTools`

| Tool | Description |
| --- | --- |
| `get_application_names` | Active application names |
| `get_applications` | All active applications: start times, session counts, expiry status |
| `get_application` | Full runtime details for a specific application |
| `has_application` | Check if an application is active |
| `get_application_summary` | Summary: totals, session load, expired apps in registry |
| `stop_application` | Shut down a running application by name |

### Logging — `LoggingTools`

| Tool | Description |
| --- | --- |
| `get_logging_info` | Log directory, logger count, appender count |
| `get_logging_config` | Log levels, appenders, retention policies |
| `get_loggers` | All registered loggers with names and appenders |
| `get_logger` | Details for a specific logger |
| `get_root_logger` | Root logger details and attached appenders |
| `get_appenders` | All registered appenders: file paths, types, configuration |
| `read_log_entries` | Last N log entries from a log file |
| `get_last_error` | Most recent ERROR or FATAL entry from a logger |
| `search_log_entries` | Search log entries by keyword or pattern |
| `log_message` | Write a test log message (verify logging works) |

### HTTP & SOAP Clients — `HttpTools`

| Tool | Description |
| --- | --- |
| `get_http_client_count` | Number of active HTTP clients |
| `get_http_client_names` | HTTP client keys |
| `get_http_clients` | Per-client stats: connection counts, request counts, error rates |
| `get_soap_clients` | Per-WSDL SOAP client usage details |
| `get_http_executor` | HTTP executor thread pool status and configuration |
| `get_http_service_summary` | Consolidated HTTP service summary |

### File Watchers — `WatcherTools`

| Tool | Description |
| --- | --- |
| `get_watchers` | All registered filesystem watchers with configuration and state |
| `get_watcher_names` | Watcher names only |
| `get_watcher` | Single watcher details |
| `has_watcher` | Check if a watcher is registered |
| `get_watcher_stats` | Watcher execution statistics |
| `start_watcher` | Start a stopped watcher |
| `stop_watcher` | Stop a running watcher |
| `restart_watcher` | Restart a watcher |
| `remove_watcher` | Remove a watcher from the registry and stop it |
| `get_watcher_health` | Health summary of all watchers |

## 🧠 MCP Prompts (17 Total)

The server registers pre-built MCP prompts that guide AI clients through common diagnostic and administrative workflows. Each prompt instructs the AI agent which tools to call and in what order, and provides system-level context for interpreting results.

### Operations & Monitoring

| Prompt | Description | Arguments |
| --- | --- | --- |
| `runtime_health_check` | Comprehensive health check: memory, caches, datasources, executors, modules | — |
| `full_system_audit` | End-to-end audit of every subsystem (JVM, threads, caches, datasources, modules, schedulers, executors, logging, watchers) | — |
| `performance_troubleshooting` | Interactive diagnostic guide for a given symptom (slow responses, high memory, CPU spikes, thread pool exhaustion) | `symptom` *(required)* |
| `diagnose_memory_pressure` | JVM memory diagnosis: heap, non-heap, pools, GC activity; identifies leaks and misconfiguration | `threshold` *(optional, default: 80)* |
| `executor_saturation_check` | Async executor pool saturation, queue buildup, and rejected tasks | — |

### Data Layer

| Prompt | Description | Arguments |
| --- | --- | --- |
| `analyze_cache_performance` | Cache hit rates, eviction patterns, sizing; optionally focus on a named cache | `cacheName` *(optional)* |
| `datasource_health_report` | Datasource connectivity, connection pool utilization, configuration audit | — |

### Diagnostics

| Prompt | Description | Arguments |
| --- | --- | --- |
| `thread_dump_analysis` | JVM thread dump: identifies deadlocks, blocked threads, pool saturation, long-running operations | — |
| `investigate_errors` | Recent log error investigation: patterns, root causes, fixes | `loggerName`, `keyword` *(optional)* |
| `logging_infrastructure_review` | Logging infrastructure audit: log levels, appenders, recent error patterns | — |
| `class_loader_diagnostics` | Class loader health: resolver cache, loader count, deployment mode, runtime home | — |

### Auditing

| Prompt | Description | Arguments |
| --- | --- | --- |
| `module_audit` | All registered modules: status, version, BIFs, components, interceptors, configuration | — |
| `interceptor_registry_audit` | Interceptor/event system: registered points, listener counts, coverage gaps | — |
| `scheduler_status_report` | Scheduler task execution history, upcoming runs, failures | `schedulerName` *(optional)* |
| `application_lifecycle_status` | All active applications: uptime, session counts, expired apps, load indicators | — |
| `http_connectivity_audit` | Outbound HTTP and SOAP client activity: connections, pool usage, errors | — |

### Developer

| Prompt | Description | Arguments |
| --- | --- | --- |
| `bif_component_discovery` | Explore available BIFs and components; search by keyword | `keyword` *(optional)* |

## 🔌 Client Connection Example

Point your MCP client at the BoxLang endpoint:

```json
{
  "mcpServers": {
    "boxlang": {
      "url": "http://localhost:8080/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer your-auth-token"
      }
    }
  }
}
```

You can also configure it in your VSCode workspace by creating a `.vscode/mcp.json` file with the following content:

```json
{
  "mcpServers": {
    "boxlang-mcp": {
      "url": "http://localhost:8080/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer your-auth-token"
      }
    }
  }
}
```

Replace `your-auth-token` with the value of `authToken` from your module settings. If `authToken` is empty, omit the `headers` block.

Selectively expose only the tools you need:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "includedTools": [
          "get_runtime_info",
          "get_memory_info",
          "get_schedulers"
        ]
      }
    }
  }
}
```

Or exclude sensitive admin tools:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "includedTools": ["*"],
        "excludedTools": [
          "clear_all_caches",
          "reload_all_modules",
          "stop_application"
        ]
      }
    }
  }
}
```

## 🧩 Extending With Custom Tools

You are not limited to the built-in introspection tools. Any module or application can register its own tools, resources, and prompts into the BoxLang MCP server at runtime using the `bx-ai` BIF `mcpServer( "boxlang" )`.

### Register a Custom Tool

```js
// Get the BoxLang MCP server instance
var server = mcpServer( "boxlang" )

// Register a simple tool with a handler
server.registerTool(
    aiTool(
        "check_deployment_status",
        "Check the current deployment status of the application",
        ( environment ) => {
            var status = deploymentService.getStatus( environment )
            return {
                environment: arguments.environment,
                version: status.version,
                deployedAt: status.deployedAt.toString(),
                healthy: status.healthy
            }
        }
    )
    .addParameter(
        aiToolParam( "environment", "string", "The deployment environment to check (e.g., staging, production)" )
        .required()
    )
)
```

### Register a Custom Prompt

```js
mcpServer( "boxlang" ).registerPrompt(
    "deployment_health_check",
    "Check the health of the current deployment by analyzing application status and recent logs",
    ( args ) => [
        {
            role: "system",
            content: "You are a deployment operations expert. Verify the current deployment by checking the application status and analyzing recent logs."
        },
        {
            role: "user",
            content: "Check the deployment health. Use `check_deployment_status` for the '#args.environment ?: 'production'#' environment and `get_last_error` from the logging tools."
        }
    ],
    [
        { name: "environment", description: "The deployment environment to check", required: false }
    ]
)
```

### Multiple Ways to Register Tools

- **Direct handler**: Pass a BoxLang closure or lambda as the tool handler (shown above)
- **Classpath scanning**: Call `server.scan( "myapp.tools" )` to auto-discover methods annotated with `@mcpTool`
- **AITool instances**: Create `aiTool()` objects and register them individually or as an array via `server.registerTools( [...] )`

You can also access any existing tool by name:

```js
var tool = mcpServer( "boxlang" ).getTool( "get_runtime_info" )
writeOutput( tool.getDescription() )
```

## 🔗 Related Docs

- [BoxLang AI](../../../modularity/ai.md)
- [Module Installation](../../../../getting-started/installation/modules.md)
- [Module Configuration](../../../../getting-started/configuration/modules.md)
