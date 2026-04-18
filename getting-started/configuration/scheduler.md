---
description: Configure BoxLang's built-in task scheduler
icon: stopwatch
---

# Scheduler

BoxLang includes a powerful built-in task scheduler that allows you to schedule and manage tasks at the runtime level. The scheduler is managed by the `SchedulerService` and can be configured globally or programmatically.

## Configuration Structure

The scheduler configuration is located in the `scheduler` section of your `boxlang.json` file:

```json
{
  "scheduler": {
    "executor": "scheduled-tasks",
    "cacheName": "default",
    "schedulers": [],
    "tasksFile": "${boxlang-home}/config/tasks.json"
  }
}
```

## Configuration Properties

### executor

**Type:** `string` **Default:** `"scheduled-tasks"` **Description:** The name of the executor to use for running scheduled tasks. This must reference a valid executor defined in the `executors` section.

```json
"executor": "scheduled-tasks"
```

### cacheName

**Type:** `string` **Default:** `"default"` **Description:** The cache to leverage for server fixation or distribution. This is useful when running BoxLang in clustered environments to coordinate scheduled tasks across multiple instances.

```json
"cacheName": "default"
```

### schedulers

**Type:** `array` **Default:** `[]` **Description:** An array of absolute paths to BoxLang scheduler files (`.bx`) that should be registered upon runtime startup. You can use variable substitutions like `${user-dir}` or `${boxlang-home}`.

```json
"schedulers": [
  "${user-dir}/schedulers/MainScheduler.bx",
  "/path/to/custom/MyScheduler.bx"
]
```

### tasksFile

**Type:** `string` **Default:** `${boxlang-home}/config/tasks.json`

Path to the JSON file where the `bx:schedule` component persists task definitions. Tasks are written to this file on every create, update, or delete operation and reloaded from it on runtime startup.

```json
"tasksFile": "${boxlang-home}/config/tasks.json"
```

Override this path when you want multiple BoxLang instances to share a common task store (for example, via a shared mounted volume in a cluster).

## Programmatic Scheduling

You can create and manage scheduled tasks at runtime using:

* **[bx:schedule component](../../boxlang-framework/asynchronous-programming/scheduling-component.md)** — tag/script API for HTTP-driven tasks; changes persist automatically to `tasksFile`
* **[Scheduler DSL](../../boxlang-framework/asynchronous-programming/scheduled-tasks.md)** — fluent class-based API for running arbitrary BoxLang code on a schedule

The configuration above provides the foundation and default settings for the scheduler service.

## Related Configuration

* [Executors](executors.md) - Configure the thread pools used by the scheduler
* [Caches](caches.md) - Configure caches used for task coordination
* [Logging](logging.md) - Configure logging for scheduler operations
