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

## Related

* [bx:schedule Component Reference](../../boxlang-language/reference/components/async/Schedule.md)
* [Scheduled Tasks — Fluent DSL](./scheduled-tasks.md)
* [Scheduler Configuration](../../getting-started/configuration/scheduler.md)
