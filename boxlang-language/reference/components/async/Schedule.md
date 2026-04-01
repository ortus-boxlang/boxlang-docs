
# Component: `Schedule`

Manages scheduled tasks that execute HTTP requests on a defined interval or cron expression. Tasks are created, modified, and deleted at runtime and automatically persist to disk so they survive restarts.

## Component Signature

```
<bx:Schedule action=[string]
task=[string]
scheduler=[string]
group=[string]
url=[string]
interval=[string]
isDaily=[boolean]
cronTime=[string]
startDate=[string]
startTime=[string]
endDate=[string]
endTime=[string]
repeat=[integer]
exclude=[string]
port=[integer]
username=[string]
password=[string]
proxyServer=[string]
proxyPort=[integer]
proxyUser=[string]
proxyPassword=[string]
publish=[boolean]
path=[string]
file=[string]
overwrite=[boolean]
resolveUrl=[boolean]
retryCount=[integer]
onException=[string]
onComplete=[string]
eventHandler=[string]
cluster=[boolean]
result=[string] />
```

### Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `action` | `string` | `true` | The operation to perform. One of: `create`, `update`, `modify`, `delete`, `run`, `pause`, `resume`, `list`, `pauseall`, `resumeall`. |  |
| `task` | `string` | `false` | The unique name of the task. Required for all actions except `list`, `pauseall`, and `resumeall`. |  |
| `scheduler` | `string` | `false` | The name of the scheduler to target. Defaults to the BoxLang built-in default scheduler. | `_boxlang_default_` |
| `group` | `string` | `false` | A group label for organizing tasks. Used with `pauseall`/`resumeall` to target a subset of tasks. | `""` |
| `url` | `string` | `false` | The URL to GET on each scheduled execution. Required for `create`, `update`, and `modify`. |  |
| `interval` | `string` | `false` | How often to run the task. Accepted values: `once`, `daily`, `weekly`, `monthly`, or a number of seconds (minimum 60). |  |
| `isDaily` | `boolean` | `false` | Shorthand for `interval="daily"`. | `false` |
| `cronTime` | `string` | `false` | A cron expression defining the schedule. Supports 5-field Unix format (`minute hour day month weekday`) and 6-field Quartz format (`second minute hour day month weekday`). |  |
| `startDate` | `string` | `false` | Date on which the task becomes active. |  |
| `startTime` | `string` | `false` | Time on `startDate` at which the task becomes active. |  |
| `endDate` | `string` | `false` | Date on which the task is automatically deactivated. |  |
| `endTime` | `string` | `false` | Time on `endDate` at which the task is deactivated. |  |
| `repeat` | `integer` | `false` | Maximum number of times the task runs before it is automatically stopped. |  |
| `exclude` | `string` | `false` | Comma-separated list of dates or date ranges (`d1 to d2`) on which the task should not run. |  |
| `port` | `integer` | `false` | The HTTP port to use when calling the task URL. | `80` |
| `username` | `string` | `false` | HTTP Basic authentication username. Stored encrypted on disk. |  |
| `password` | `string` | `false` | HTTP Basic authentication password. Stored encrypted on disk. |  |
| `proxyServer` | `string` | `false` | Proxy server hostname for the HTTP request. |  |
| `proxyPort` | `integer` | `false` | Proxy server port. |  |
| `proxyUser` | `string` | `false` | Proxy authentication username. |  |
| `proxyPassword` | `string` | `false` | Proxy authentication password. |  |
| `publish` | `boolean` | `false` | When `true`, the HTTP response body is written to the file specified by `path` and `file`. | `false` |
| `path` | `string` | `false` | Directory path where the published output file is written. Required when `publish="true"`. |  |
| `file` | `string` | `false` | Filename for the published output. Required when `publish="true"`. |  |
| `overwrite` | `boolean` | `false` | Whether to overwrite an existing published output file on each run. | `true` |
| `resolveUrl` | `boolean` | `false` | When `true`, resolves relative URLs found in the HTTP response. | `false` |
| `retryCount` | `integer` | `false` | Number of times to retry the HTTP request on failure before applying the `onException` policy. | `3` |
| `onException` | `string` | `false` | How to handle an unrecoverable task failure after all retries. One of: `refire` (retry next interval), `pause` (pause the task), `invokeHandler` (call the `eventHandler` path). | `refire` |
| `onComplete` | `string` | `false` | Path to a BoxLang file invoked when the task completes successfully. |  |
| `eventHandler` | `string` | `false` | Path to a BoxLang file invoked when `onException="invokeHandler"`. |  |
| `cluster` | `boolean` | `false` | Marks the task as cluster-aware for metadata purposes. | `false` |
| `result` | `string` | `false` | Variable name into which the task list struct is stored. Used with `action="list"`. |  |

## Actions

### `create`

Creates a new task. Throws a `BoxRuntimeException` if a task with the same name already exists in the scheduler — use `update` if you want create-or-replace semantics. Requires `task`, `url`, and either `interval` or `cronTime`.

### `update` / `modify`

Creates a task if it does not exist, or replaces it entirely if it does. These two action values are equivalent. Requires `task`, `url`, and either `interval` or `cronTime`.

### `delete`

Permanently removes a named task from the scheduler and from the persistence file.

### `run`

Immediately executes a named task regardless of its schedule. The task must already exist.

### `pause`

Suspends execution of a named task. The task remains registered and can be resumed later.

### `resume`

Re-enables a previously paused task, restoring normal scheduled execution.

### `list`

Retrieves all registered tasks as a struct keyed by task name and stores it in the variable named by the `result` attribute.

### `pauseall`

Pauses every task in the targeted scheduler. If `group` is specified, only tasks in that group are paused.

### `resumeall`

Resumes every paused task in the targeted scheduler. If `group` is specified, only tasks in that group are resumed.

## Scheduling Options

A task must specify exactly one of the following scheduling approaches:

| Approach | Attribute | Example |
|----------|-----------|---------|
| Fixed interval | `interval` | `interval="3600"` (every hour) |
| Named interval | `interval` | `interval="daily"`, `interval="weekly"`, `interval="monthly"`, `interval="once"` |
| Daily shorthand | `isDaily` | `isDaily="true"` |
| Cron expression | `cronTime` | `cronTime="0 2 * * *"` (2 AM daily) |

## Persistence

All tasks managed through `bx:schedule` are automatically persisted to `${boxLangHome}/config/tasks.json` and reloaded when the BoxLang runtime starts. The persistence file path can be customised via the `tasksFile` property in `boxlang.json`. Credentials are stored encrypted using the runtime's `.seed` file.

## Examples

### Script Syntax

```javascript
// Create a task that runs every hour
bx:schedule action="create"
    task="hourlyReport"
    url="https://myapp.com/tasks/report"
    interval="3600";

// Create a task using a cron expression (runs at 2 AM every day)
bx:schedule action="create"
    task="nightlyCleanup"
    url="https://myapp.com/tasks/cleanup"
    cronTime="0 2 * * *";

// List all tasks
bx:schedule action="list" result="allTasks";
writeDump( allTasks );

// Pause a task
bx:schedule action="pause" task="hourlyReport";

// Resume a task
bx:schedule action="resume" task="hourlyReport";

// Delete a task
bx:schedule action="delete" task="hourlyReport";
```

### Tag Syntax

```cfm
<!--- Create a task that runs every hour --->
<bx:schedule action="create"
    task="hourlyReport"
    url="https://myapp.com/tasks/report"
    interval="3600" />

<!--- Create a task using a cron expression (runs at 2 AM every day) --->
<bx:schedule action="create"
    task="nightlyCleanup"
    url="https://myapp.com/tasks/cleanup"
    cronTime="0 2 * * *" />

<!--- List all tasks --->
<bx:schedule action="list" result="allTasks" />
<bx:dump var="#allTasks#" />

<!--- Pause and resume a task --->
<bx:schedule action="pause" task="hourlyReport" />
<bx:schedule action="resume" task="hourlyReport" />

<!--- Delete a task --->
<bx:schedule action="delete" task="hourlyReport" />
```

## Related

* [Scheduled Tasks Guide](../../../boxlang-framework/asynchronous-programming/scheduling-component.md)
* [Schedule Component Guide](../../../boxlang-framework/asynchronous-programming/scheduling-component.md)
* [Thread](./Thread.md)
