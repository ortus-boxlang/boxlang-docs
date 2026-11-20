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
    "clusterMode": "eager",
    "clusterTasks": true,
    "taskOverlapPolicy": "skip",
    "shutdownGraceSeconds": 15,
    "shutdownInterruptGraceSeconds": 5,
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

### clusterMode

**Type:** `string` **Default:** `"eager"` **Description:** How clustered task occurrences are shared out across nodes. `eager` makes each node wait a short random delay (up to 1 second) before claiming. `balanced` ranks nodes by their published load, and the busiest waits longest (up to 5 seconds). Requires the [`cluster`](cluster.md) block to be enabled. See [Clustered Scheduled Tasks](../../boxlang-framework/asynchronous-programming/clustered-scheduled-tasks.md).

```json
"clusterMode": "balanced"
```

### clusterTasks

**Type:** `boolean` **Default:** `true` **Description:** Whether tasks that state no `cluster` preference are clustered. A task that sets `cluster` explicitly always wins. It only applies on a node where [`cluster.enabled`](cluster.md#enabled) is `true`. Set it to `false` to keep every task local on a clustered node unless it opts in.

```json
"clusterTasks": false
```

### taskOverlapPolicy

**Type:** `string` **Default:** `"skip"` **Description:** What a clustered task does when its previous occurrence is still running. `skip` drops the next occurrence, matching single node behavior. `run` allows occurrences to overlap. Tasks can override it with their own `overlap` setting.

### shutdownGraceSeconds

**Type:** `integer` **Default:** `15` **Description:** How long a shutdown waits for in-flight runs to finish before interrupting them. `0` skips the graceful wait and interrupts immediately.

### shutdownInterruptGraceSeconds

**Type:** `integer` **Default:** `5` **Description:** How long to wait after interrupting before the executor is forced down. With both shutdown settings at `0`, shutdown stops runs immediately.

### cacheName (deprecated)

{% hint style="warning" %}
`cacheName` is deprecated as of 1.20.0. Cluster coordination now uses [`cluster.cacheName`](cluster.md#cachename). The old value is still honored as an upgrade bridge, except the legacy `"default"` value, which is ignored so that upgrading does not switch clustering on.
{% endhint %}

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
* **[Tasks File Reference](../../boxlang-framework/asynchronous-programming/scheduling-component.md#tasks-file-reference-tasksjson)** — full `tasks.json` field-by-field schema with examples
* **[Scheduler DSL](../../boxlang-framework/asynchronous-programming/scheduled-tasks.md)** — fluent class-based API for running arbitrary BoxLang code on a schedule

The configuration above provides the foundation and default settings for the scheduler service.

## Related Configuration

* [Executors](executors.md) - Configure the thread pools used by the scheduler
* [Cluster](cluster.md) - Configure cluster coordination for clustered tasks
* [Caches](caches.md) - Configure caches used for task coordination
* [Logging](logging.md) - Configure logging for scheduler operations
