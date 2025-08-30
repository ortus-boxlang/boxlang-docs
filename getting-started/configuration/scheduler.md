---
description: Configure BoxLang's built-in task scheduler
icon: clock-2
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
    "tasks": {}
  }
}
```

## Configuration Properties

### executor

**Type:** `string`
**Default:** `"scheduled-tasks"`
**Description:** The name of the executor to use for running scheduled tasks. This must reference a valid executor defined in the `executors` section.

```json
"executor": "scheduled-tasks"
```

### cacheName

**Type:** `string`
**Default:** `"default"`
**Description:** The cache to leverage for server fixation or distribution. This is useful when running BoxLang in clustered environments to coordinate scheduled tasks across multiple instances.

```json
"cacheName": "default"
```

### schedulers

**Type:** `array`
**Default:** `[]`
**Description:** An array of absolute paths to BoxLang scheduler files (`.bx`) that should be registered upon runtime startup. You can use variable substitutions like `${user-dir}` or `${boxlang-home}`.

```json
"schedulers": [
  "${user-dir}/schedulers/MainScheduler.bx",
  "/path/to/custom/MyScheduler.bx"
]
```

### tasks

Coming soon.

**Type:** `object`
**Default:** `{}`
**Description:** You can define tasks manually in the configuration instead of using scheduler files. Each task is defined as a key-value pair where the key is the unique task name.

## Programmatic Scheduling

You can also create and manage scheduled tasks programmatically using BoxLang's scheduling functions and components. The configuration above provides the foundation and default settings for the scheduler service.

## Related Configuration

- [Executors](executors.md) - Configure the thread pools used by the scheduler
- [Caches](caches.md) - Configure caches used for task coordination
- [Logging](logging.md) - Configure logging for scheduler operations
