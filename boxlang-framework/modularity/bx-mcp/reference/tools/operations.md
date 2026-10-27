---
icon: gear
description: Async executor, scheduler, module, interceptor, application, logging, and file watcher management tools.
---

# ⚙️ Operations Tools

This page covers tools for async executors (`AsyncTools`), schedulers (`SchedulerTools`), modules (`ModuleTools`), interceptors (`InterceptorTools`), applications (`ApplicationTools`), logging (`LoggingTools`), and file watchers (`WatcherTools`).

---

## Async Executors — `AsyncTools`

| Tool | Description |
| --- | --- |
| `executor_get_all` | All registered async executors with status, pool info, task stats |
| `executor_get_names` | Executor names only |
| `executor_get_info` | Detailed executor info: type, status, configuration |
| `executor_get_stats` | Pool utilization, queue status, task counts, health metrics |
| `executor_get_health` | Structured health report: status, score, per-executor issues with codes |
| `executor_get_health_summary` | Structured health summary across all executors with status and score |

---

## Schedulers — `SchedulerTools`

| Tool | Description |
| --- | --- |
| `scheduler_get_all` | All registered schedulers with configurations and tasks |
| `scheduler_get_names` | Scheduler names only |
| `scheduler_get` | Single scheduler details including tasks and records |
| `scheduler_has` | Check if a scheduler is registered |
| `scheduler_get_task_stats` | Execution statistics for a specific task |
| `scheduler_get_task_info` | Task details: configuration and metadata |
| `scheduler_get_all_tasks` | All tasks across all schedulers |
| `scheduler_run_task` | Force-run a scheduled task immediately |
| `scheduler_pause_task` | Pause a scheduled task |
| `scheduler_resume_task` | Resume a paused scheduled task |
| `scheduler_pause_persisted_task` | Pause a disk-persisted task (updates `tasks.json`) |
| `scheduler_resume_persisted_task` | Resume a disk-persisted task |
| `scheduler_pause_all_persisted_tasks` | Pause all disk-persisted tasks (filterable by scheduler/group) |
| `scheduler_resume_all_persisted_tasks` | Resume all disk-persisted tasks |
| `scheduler_get_health` | Structured health assessment: status, score, per-scheduler issues |
| `scheduler_get_all_task_stats` | Task stats summary across all schedulers |
| `scheduler_get_persisted_tasks` | All scheduled tasks persisted on disk (`tasks.json`) |

---

## Modules — `ModuleTools`

| Tool | Description |
| --- | --- |
| `module_get_all` | All registered modules with configuration and status |
| `module_get_names` | Module names only |
| `module_get_info` | Full configuration and status for a specific module |
| `module_get_settings` | Settings for a specific module |
| `module_get_paths` | Registered module search paths |
| `module_reload` | Reload a specific module (unload, re-register, re-activate) |
| `module_reload_all` | Reload all registered modules |
| `module_has` | Check if a module is registered |
| `module_get_stats` | Module statistics: total count, activated, enabled, etc. |

---

## Interceptors — `InterceptorTools`

| Tool | Description |
| --- | --- |
| `interceptor_get_points` | All registered interception point names (sorted) |
| `interceptor_has_point` | Check if a specific interception point is registered |
| `interceptor_get_states` | All interceptor states with listener counts |
| `interceptor_get_state` | Listener count for a specific event |
| `interceptor_get_summary` | Registry totals, active states, events with most listeners |

---

## Applications — `ApplicationTools`

| Tool | Description |
| --- | --- |
| `app_get_names` | Active application names |
| `app_get_all` | All active applications: start times, session counts, class loader counts, expiry status |
| `app_get` | Full runtime details: session cache metadata, application scope keys, class loaders, uptime |
| `app_has` | Check if an application is active |
| `app_get_summary` | Summary: totals, session load, expired apps in registry |
| `app_stop` | Shut down a running application by name |
| `app_restart` | Restart a named application, picking up config/code changes |
| `app_sessions_clear` | Clear all sessions for an application (logs out all users) |

---

## Logging — `LoggingTools`

| Tool | Description |
| --- | --- |
| `logging_get_info` | Log directory, logger count, appender count |
| `logging_get_config` | Log levels, appenders, retention policies |
| `logging_get_loggers` | All registered loggers with names and appenders |
| `logging_get_logger` | Details for a specific logger |
| `logging_get_root_logger` | Root logger details and attached appenders |
| `logging_get_appenders` | All registered appenders: file paths, types, configuration |
| `logging_read_entries` | Last N log entries from a log file |
| `logging_get_last_error` | Most recent ERROR or FATAL entry from a logger |
| `logging_search_entries` | Search log entries by keyword or pattern |
| `logging_log_message` | Write a test log message (verify logging works) |

---

## File Watchers — `WatcherTools`

| Tool | Description |
| --- | --- |
| `watcher_get_all` | All registered filesystem watchers with configuration and state |
| `watcher_get_names` | Watcher names only |
| `watcher_get` | Single watcher details |
| `watcher_has` | Check if a watcher is registered |
| `watcher_get_stats` | Watcher execution statistics |
| `watcher_start` | Start a stopped watcher |
| `watcher_stop` | Stop a running watcher |
| `watcher_restart` | Restart a watcher |
| `watcher_remove` | Remove a watcher from the registry and stop it |
| `watcher_get_health` | Structured health assessment: status, score, per-watcher errors |
