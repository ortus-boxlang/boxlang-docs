---
description: HTTP-driven scheduled tasks via the bx:schedule component
icon: calendar-clock
---

# Schedule Component

The `bx:schedule` component lets you create, manage, and persist HTTP-driven scheduled tasks directly from BoxLang templates and scripts. Each task fires an HTTP GET request to a URL of your choice on a defined schedule, making it the simplest way to trigger periodic work without writing a full Scheduler class.

{% hint style="info" %}
If you need to run arbitrary BoxLang code (not just HTTP calls) on a schedule, use the [Scheduler DSL](./scheduled-tasks.md) instead. Both approaches share the same `SchedulerService` under the hood.
{% endhint %}

## Choosing an Approach

| | bx:schedule | Scheduler DSL |
|---|---|---|
| **Runs** | HTTP GET requests | Any BoxLang code |
| **Defined in** | Templates / scripts | Scheduler class files |
| **Persisted automatically** | Yes (`tasks.json`) | No (must reload on startup via config) |
| **Cron support** | Yes | Yes (`.cron()`) |
| **Best for** | Simple webhooks, endpoint pings, web callbacks | In-process computation, complex task logic |

---

## Creating a Task

Every `create` call requires a `task` name, a `url`, and either an `interval` or a `cronTime`.

### Interval-based scheduling

```javascript
// Run every 5 minutes (300 seconds)
bx:schedule action="create"
    task="pingHealthCheck"
    url="https://myapp.com/health"
    interval="300";
```

Named intervals are also accepted:

```javascript
bx:schedule action="create"
    task="dailyReport"
    url="https://myapp.com/tasks/report"
    interval="daily";
```

Valid named intervals: `once`, `daily`, `weekly`, `monthly`.

### Cron-based scheduling

```javascript
// Every day at 2 AM (5-field Unix cron)
bx:schedule action="create"
    task="nightlyCleanup"
    url="https://myapp.com/tasks/cleanup"
    cronTime="0 2 * * *";

// Every weekday at 8:30 AM (6-field Quartz cron)
bx:schedule action="create"
    task="morningDigest"
    url="https://myapp.com/tasks/digest"
    cronTime="0 30 8 * * MON-FRI";
```

### Cron expression formats

BoxLang supports two cron formats:

**5-field Unix** — `minute hour day-of-month month day-of-week`

```
# Every hour
0 * * * *

# At midnight every Sunday
0 0 * * 0

# At 9 AM on the 1st of every month
0 9 1 * *
```

**6-field Quartz** — `second minute hour day-of-month month day-of-week`

```
# Every 30 seconds
*/30 * * * * ?

# At noon every weekday
0 0 12 * * MON-FRI

# At midnight on the last day of each month
0 0 0 L * ?
```

Special characters: `*` (all), `?` (any), `-` (range), `,` (list), `/` (step), `L` (last).

---

## Updating and Deleting Tasks

Use `update` (or its alias `modify`) when you want create-or-replace semantics. Use `create` when you want a hard error if the task already exists.

```javascript
// Replace task definition silently
bx:schedule action="update"
    task="nightlyCleanup"
    url="https://myapp.com/tasks/cleanup-v2"
    cronTime="0 3 * * *";

// Remove a task
bx:schedule action="delete" task="nightlyCleanup";
```

---

## Pausing and Resuming Tasks

```javascript
// Pause a single task
bx:schedule action="pause" task="dailyReport";

// Resume it
bx:schedule action="resume" task="dailyReport";

// Pause every task in the scheduler
bx:schedule action="pauseall";

// Resume everything
bx:schedule action="resumeall";
```

You can scope `pauseall` / `resumeall` to a task group:

```javascript
bx:schedule action="create"
    task="reportA"
    url="https://myapp.com/report/a"
    interval="daily"
    group="reports";

bx:schedule action="create"
    task="reportB"
    url="https://myapp.com/report/b"
    interval="daily"
    group="reports";

// Only pause the "reports" group
bx:schedule action="pauseall" group="reports";
```

---

## Listing Tasks

```javascript
bx:schedule action="list" result="tasks";

for ( var name in tasks ) {
    var t = tasks[ name ];
    writeOutput( "#name# — paused: #t.isPaused()#<br>" );
}
```

---

## Running a Task Immediately

```javascript
bx:schedule action="run" task="nightlyCleanup";
```

This fires the task's HTTP request right now, independent of its normal schedule.

---

## Authentication and Proxies

```javascript
bx:schedule action="create"
    task="secureEndpoint"
    url="https://internal.corp.com/tasks/run"
    interval="3600"
    username="taskuser"
    password="s3cret"
    proxyServer="proxy.corp.com"
    proxyPort="8080";
```

Credentials are stored encrypted in `tasks.json` using the runtime's `.seed` file.

---

## Publishing Output to Disk

Set `publish="true"` to capture the HTTP response body and write it to a file after each run.

```javascript
bx:schedule action="create"
    task="dailyReport"
    url="https://myapp.com/tasks/report"
    interval="daily"
    publish="true"
    path="/var/log/tasks"
    file="daily-report.html";
```

---

## Date and Time Constraints

Restrict when a task is active using `startDate`, `startTime`, `endDate`, and `endTime`. You can also exclude specific dates:

```javascript
bx:schedule action="create"
    task="holiday"
    url="https://myapp.com/tasks/check"
    interval="daily"
    startDate="2026-01-01"
    endDate="2026-12-31"
    exclude="2026-07-04,2026-12-25";
```

Date ranges are also valid in `exclude`: `"2026-12-24 to 2026-12-26"`.

---

## Limiting Executions

Use `repeat` to cap the total number of runs:

```javascript
// Run exactly 5 times, then stop
bx:schedule action="create"
    task="onboarding"
    url="https://myapp.com/onboarding/step"
    interval="86400"
    repeat="5";
```

---

## Exception Handling

Configure what happens when all retries are exhausted with `onException`:

| Value | Behaviour |
|-------|-----------|
| `refire` (default) | Re-attempt on the next scheduled interval |
| `pause` | Automatically pause the task |
| `invokeHandler` | Call the BoxLang file at `eventHandler` |

```javascript
bx:schedule action="create"
    task="criticalTask"
    url="https://myapp.com/tasks/critical"
    interval="3600"
    retryCount="5"
    onException="invokeHandler"
    eventHandler="/handlers/TaskErrorHandler.bx";
```

---

## Persistence

Tasks are automatically saved to `${boxLangHome}/config/tasks.json` after every create, update, or delete operation. When the BoxLang runtime starts, it reads this file and re-registers all tasks in the scheduler.

You can customise the storage location in `boxlang.json`:

```json
"scheduler": {
    "tasksFile": "/shared/config/tasks.json"
}
```

This is useful in clustered environments where multiple instances share a mounted volume.

---

## Tag Syntax Reference

```cfm
<bx:schedule action="create"
    task="myTask"
    url="https://myapp.com/run"
    cronTime="0 2 * * *"
    retryCount="3"
    onException="pause" />

<bx:schedule action="list" result="tasks" />
<bx:schedule action="pause" task="myTask" />
<bx:schedule action="resume" task="myTask" />
<bx:schedule action="delete" task="myTask" />
```

---

## 📋 Tasks File Reference (`tasks.json`)

Every `create`, `update`, and `delete` operation writes the full task registry to disk at `${boxLangHome}/config/tasks.json` (configurable via `scheduler.tasksFile`). The file is a JSON array — one object per task — and is re-read on every runtime startup to restore all persisted tasks.

Below is a fully annotated example of a single task entry, followed by a field-by-field reference.

### Annotated Example

```json
[
  {
    "task"          : "nightlyCleanup",
    "scheduler"     : "default",
    "group"         : "maintenance",
    "url"           : "https://myapp.com/tasks/cleanup",
    "interval"      : null,
    "cronTime"      : "0 2 * * *",
    "startDate"     : "2026-01-01",
    "startTime"     : "00:00",
    "endDate"       : "2026-12-31",
    "endTime"       : "23:59",
    "repeat"        : 0,
    "exclude"       : "2026-07-04,2026-12-25",
    "port"          : 443,
    "username"      : "ENC:a3g...==",
    "password"      : "ENC:b7k...==",
    "proxyServer"   : "proxy.corp.com",
    "proxyPort"     : 8080,
    "proxyUser"     : null,
    "proxyPassword" : null,
    "publish"       : true,
    "path"          : "/var/log/tasks",
    "file"          : "cleanup-output.html",
    "overwrite"     : true,
    "resolveURL"    : false,
    "retryCount"    : 3,
    "onException"   : "invokeHandler",
    "oncomplete"    : null,
    "eventhandler"  : "/handlers/TaskErrorHandler.bx",
    "cluster"       : false,
    "isDaily"       : false,
    "paused"        : false
  }
]
```

{% hint style="warning" %}
**Never edit `username`, `password`, `proxyUser`, or `proxyPassword` values by hand.** These are encrypted with AES using the runtime's `.seed` file. Always use `bx:schedule action="update"` to change credentials.
{% endhint %}

### Field Reference

#### 🗂️ Identity

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `task` | `string` | _(required)_ | Unique task name within the scheduler. Used as the primary identifier for all actions. |
| `scheduler` | `string` | `"default"` | Name of the `BaseScheduler` instance that owns this task. Automatically created if it does not exist. |
| `group` | `string` | `null` | Logical grouping label. Lets you `pauseall`/`resumeall` a subset of tasks at once. |
| `paused` | `boolean` | `false` | Runtime paused state. Set to `true` by `action="pause"` and back to `false` by `action="resume"`. Restored on startup. |

#### ⏰ Scheduling

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `interval` | `string` | `null` | Repeat interval in **seconds**, or a named value: `once`, `daily`, `weekly`, `monthly`. Mutually exclusive with `cronTime`. |
| `cronTime` | `string` | `null` | Cron expression. Accepts 5-field Unix (`minute hour dom month dow`) or 6-field Quartz (`second minute hour dom month dow`). Mutually exclusive with `interval`. |
| `startDate` | `string` | `null` | ISO-8601 date (`YYYY-MM-DD`). Task will not fire before this date. |
| `startTime` | `string` | `null` | Time-of-day (`HH:mm`) paired with `startDate` to form the activation instant. |
| `endDate` | `string` | `null` | ISO-8601 date after which no more firings occur. |
| `endTime` | `string` | `null` | Time-of-day paired with `endDate` to form the deactivation instant. |
| `repeat` | `integer` | `0` | Maximum number of executions. `0` (or `null`) means unlimited. |
| `exclude` | `string` | `null` | Comma-separated dates or ranges to skip. Example: `"2026-07-04,2026-12-24 to 2026-12-26"`. |
| `isDaily` | `boolean` | `false` | Derived convenience flag; `true` when the task fires once per day regardless of cron/interval. Managed by the runtime. |

#### 🌐 HTTP Request

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `url` | `string` | _(required)_ | Full URL that the scheduler fires via HTTP GET on each execution. |
| `port` | `integer` | `null` | Override the URL's default port (e.g., `8080` for HTTP, `443` for HTTPS). |
| `resolveURL` | `boolean` | `false` | When `true`, relative URLs in the HTTP response are rewritten to absolute URLs before any output is captured. |

#### 🔐 Credentials

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `username` | `string` | `null` | HTTP Basic Auth username. Stored as `ENC:<base64>` — AES-encrypted with the runtime seed. |
| `password` | `string` | `null` | HTTP Basic Auth password. Same encryption scheme as `username`. |
| `proxyServer` | `string` | `null` | Proxy server hostname or IP. |
| `proxyPort` | `integer` | `null` | Proxy server port. |
| `proxyUser` | `string` | `null` | Proxy authentication username. Encrypted at rest. |
| `proxyPassword` | `string` | `null` | Proxy authentication password. Encrypted at rest. |

#### 📄 Output Publishing

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `publish` | `boolean` | `false` | When `true`, the HTTP response body is written to disk after each run. |
| `path` | `string` | `null` | Directory path to write the published file to. Required when `publish` is `true`. |
| `file` | `string` | `null` | Filename for the published output. Required when `publish` is `true`. |
| `overwrite` | `boolean` | `true` | Whether to overwrite an existing file at `path/file` on each run. Set to `false` to append/skip. |

#### 🔁 Error Handling & Callbacks

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `retryCount` | `integer` | `0` | Number of times to retry a failed HTTP request before triggering `onException` behaviour. |
| `onException` | `string` | `"refire"` | What to do when all retries are exhausted. Values: `refire` (try again next interval), `pause` (auto-pause the task), `invokeHandler` (call `eventhandler`). |
| `eventhandler` | `string` | `null` | Absolute path to a BoxLang file (`.bx`) invoked when `onException` is `invokeHandler`. Receives the task context as an argument. |
| `oncomplete` | `string` | `null` | Absolute path to a BoxLang file invoked after **every successful** execution, regardless of retry behaviour. |

#### 🌍 Cluster

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `cluster` | `boolean` | `false` | When `true`, the `SchedulerService` uses the configured `cacheName` to ensure the task fires on only one node at a time in a cluster. |

### Minimal Task Entry

The smallest valid `tasks.json` entry that will be re-loaded on startup:

```json
[
  {
    "task"     : "pingHealth",
    "scheduler": "default",
    "url"      : "https://myapp.com/health",
    "interval" : "300",
    "paused"   : false
  }
]
```

All other fields default to `null` / `false` / `0` and are safe to omit.

---

## Related

* [bx:schedule Component Reference](../../boxlang-language/reference/components/async/Schedule.md)
* [Scheduled Tasks — Fluent DSL](./scheduled-tasks.md)
* [Scheduler Configuration](../../getting-started/configuration/scheduler.md)
