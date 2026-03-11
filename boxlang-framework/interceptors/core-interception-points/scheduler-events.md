# Scheduler Events

These events fire throughout the lifecycle of schedulers and scheduled task execution. They are announced on the **global interceptor pool**.

> **Execution order per task run (success):** `schedulerBeforeAnyTask` → task executes → `schedulerOnAnyTaskSuccess` → `schedulerAfterAnyTask`
>
> **Execution order per task run (failure):** `schedulerBeforeAnyTask` → task throws → `schedulerOnAnyTaskError` → `schedulerAfterAnyTask`

| Event Name                  | Cancellable | Description                                                               |
| --------------------------- | :---------: | ------------------------------------------------------------------------- |
| `onSchedulerServiceStartup` |     No      | Fired after the `SchedulerService` starts and all schedulers are running. |
| `onSchedulerServiceShutdown`|     No      | Fired before the `SchedulerService` shuts down with the runtime.          |
| `onAllSchedulersStarted`    |     No      | Fired after all registered schedulers have been started.                  |
| `onSchedulerStartup`        |     No      | Fired after an individual scheduler has been started.                     |
| `onSchedulerShutdown`       |     No      | Fired before an individual scheduler is shut down.                        |
| `onSchedulerRestart`        |     No      | Fired before an individual scheduler is restarted.                        |
| `onSchedulerRegistration`   |     No      | Fired after a scheduler is registered with the `SchedulerService`.        |
| `onSchedulerRemoval`        |     No      | Fired before a scheduler is removed and shut down.                        |
| `schedulerBeforeAnyTask`    |     No      | Fired before a scheduled task executes.                                   |
| `schedulerAfterAnyTask`     |     No      | Fired after a scheduled task finishes — always fires, success or failure. |
| `schedulerOnAnyTaskSuccess` |     No      | Fired after a task completes successfully.                                |
| `schedulerOnAnyTaskError`   |     No      | Fired when a task throws an exception during execution.                   |

* [`onSchedulerServiceStartup`](scheduler-events.md#onschedulerservicestartup)
* [`onSchedulerServiceShutdown`](scheduler-events.md#onschedulerserviceshutdown)
* [`onAllSchedulersStarted`](scheduler-events.md#onallschedulersstarted)
* [`onSchedulerStartup`](scheduler-events.md#onschedulerstartup)
* [`onSchedulerShutdown`](scheduler-events.md#onschedulershutdown)
* [`onSchedulerRestart`](scheduler-events.md#onschedulerrestart)
* [`onSchedulerRegistration`](scheduler-events.md#onschedulerregistration)
* [`onSchedulerRemoval`](scheduler-events.md#onschedulerremoval)
* [`schedulerBeforeAnyTask`](scheduler-events.md#schedulerbeforeanytask)
* [`schedulerAfterAnyTask`](scheduler-events.md#schedulerafteranytask)
* [`schedulerOnAnyTaskSuccess`](scheduler-events.md#scheduleronanyTasksuccess)
* [`schedulerOnAnyTaskError`](scheduler-events.md#scheduleronanytaskerror)

## onSchedulerServiceStartup

Fired after the `SchedulerService` has started up and all configured schedulers are running.

### Data Structure

| Data Key           | Type               | Description                     |
| ------------------ | ------------------ | ------------------------------- |
| `schedulerService` | `SchedulerService` | The scheduler service instance. |

### Example

```groovy
class myListener{
	function onSchedulerServiceStartup( struct data ){
		var schedulerService = data.schedulerService;
	}
}
```

## onSchedulerServiceShutdown

Fired before the `SchedulerService` begins shutting down all schedulers. Individual `onSchedulerShutdown` events follow for each registered scheduler.

### Data Structure

| Data Key           | Type               | Description                     |
| ------------------ | ------------------ | ------------------------------- |
| `schedulerService` | `SchedulerService` | The scheduler service instance. |

### Example

```groovy
class myListener{
	function onSchedulerServiceShutdown( struct data ){
		var schedulerService = data.schedulerService;
	}
}
```

## onAllSchedulersStarted

Fired after all registered schedulers have been started in parallel. At this point every scheduler in the service is running.

### Data Structure

| Data Key     | Type                   | Description                                            |
| ------------ | ---------------------- | ------------------------------------------------------ |
| `schedulers` | `Map<Key, IScheduler>` | The full map of all registered and started schedulers. |

### Example

```groovy
class myListener{
	function onAllSchedulersStarted( struct data ){
		var schedulers = data.schedulers;
	}
}
```

## onSchedulerStartup

Fired after an individual scheduler has been started. The scheduler's tasks are now scheduled and running.

### Data Structure

| Data Key    | Type         | Description                          |
| ----------- | ------------ | ------------------------------------ |
| `scheduler` | `IScheduler` | The scheduler instance that started. |

### Example

```groovy
class myListener{
	function onSchedulerStartup( struct data ){
		var scheduler = data.scheduler;
	}
}
```

## onSchedulerShutdown

Fired before an individual scheduler is shut down. Fires both during explicit removal and during service-level shutdown.

### Data Structure

| Data Key    | Type         | Description                                                |
| ----------- | ------------ | ---------------------------------------------------------- |
| `scheduler` | `IScheduler` | The scheduler being shut down.                             |
| `force`     | `boolean`    | Whether this is a forced (immediate) shutdown.             |
| `timeout`   | `long`       | Milliseconds to wait for graceful shutdown before forcing. |

### Example

```groovy
class myListener{
	function onSchedulerShutdown( struct data ){
		var scheduler = data.scheduler;
		var force     = data.force;
		var timeout   = data.timeout;
	}
}
```

## onSchedulerRestart

Fired before an individual scheduler is restarted. The scheduler is shut down and started again after this event.

### Data Structure

| Data Key    | Type         | Description                                                |
| ----------- | ------------ | ---------------------------------------------------------- |
| `scheduler` | `IScheduler` | The scheduler being restarted.                             |
| `force`     | `boolean`    | Whether the shutdown phase of the restart is forced.       |
| `timeout`   | `long`       | Milliseconds to wait for graceful shutdown before forcing. |

### Example

```groovy
class myListener{
	function onSchedulerRestart( struct data ){
		var scheduler = data.scheduler;
		var force     = data.force;
		var timeout   = data.timeout;
	}
}
```

## onSchedulerRegistration

Fired after a scheduler is registered with the `SchedulerService`. If `force=true`, any previously registered scheduler with the same name was already removed before this fires.

### Data Structure

| Data Key    | Type         | Description                                                    |
| ----------- | ------------ | -------------------------------------------------------------- |
| `scheduler` | `IScheduler` | The scheduler that was registered.                             |
| `force`     | `boolean`    | Whether an existing scheduler with the same name was replaced. |

### Example

```groovy
class myListener{
	function onSchedulerRegistration( struct data ){
		var scheduler = data.scheduler;
		var force     = data.force;
	}
}
```

## onSchedulerRemoval

Fired before a scheduler is removed from the service and shut down.

### Data Structure

| Data Key    | Type         | Description                                |
| ----------- | ------------ | ------------------------------------------ |
| `scheduler` | `IScheduler` | The scheduler being removed.               |
| `force`     | `boolean`    | Whether the shutdown is forced.            |
| `timeout`   | `long`       | Milliseconds to wait for graceful shutdown.|

### Example

```groovy
class myListener{
	function onSchedulerRemoval( struct data ){
		var scheduler = data.scheduler;
		var force     = data.force;
		var timeout   = data.timeout;
	}
}
```

## schedulerBeforeAnyTask

Fired before a scheduled task executes. This is the first event in the task execution lifecycle.

### Data Structure

| Data Key | Type            | Description                |
| -------- | --------------- | -------------------------- |
| `task`   | `ScheduledTask` | The task about to execute. |

### Example

```groovy
class myListener{
	function schedulerBeforeAnyTask( struct data ){
		var task = data.task;
		// Log, validate preconditions, acquire resources, etc.
	}
}
```

## schedulerAfterAnyTask

Fired after a scheduled task finishes — **always fires**, whether the task succeeded or threw an exception. On the error path, `result` wraps the caught exception.

### Data Structure

| Data Key | Type            | Description                                                                                      |
| -------- | --------------- | ------------------------------------------------------------------------------------------------ |
| `task`   | `ScheduledTask` | The task that ran.                                                                               |
| `result` | `Optional<?>`   | The task's last result on success, or `Optional.of(exception)` if the task threw an exception.  |

### Example

```groovy
class myListener{
	function schedulerAfterAnyTask( struct data ){
		var task   = data.task;
		var result = data.result;
		// Release resources, update metrics, etc.
	}
}
```

## schedulerOnAnyTaskSuccess

Fired after a task completes successfully without throwing an exception. Always fires before `schedulerAfterAnyTask` on the success path.

### Data Structure

| Data Key | Type            | Description                                            |
| -------- | --------------- | ------------------------------------------------------ |
| `task`   | `ScheduledTask` | The task that completed successfully.                  |
| `result` | `Optional<?>`   | The task's return value (may be empty if void return). |

### Example

```groovy
class myListener{
	function schedulerOnAnyTaskSuccess( struct data ){
		var task   = data.task;
		var result = data.result;
		// Record metrics, trigger success-dependent actions, etc.
	}
}
```

## schedulerOnAnyTaskError

Fired when a task throws an exception. Fires before `schedulerAfterAnyTask` on the error path. The exception is caught by the task executor — it does not propagate and will not stop other tasks from running.

### Data Structure

| Data Key    | Type            | Description                            |
| ----------- | --------------- | -------------------------------------- |
| `task`      | `ScheduledTask` | The task that failed.                  |
| `exception` | `Exception`     | The exception thrown during execution. |

### Example

```groovy
class myListener{
	function schedulerOnAnyTaskError( struct data ){
		var task      = data.task;
		var exception = data.exception;
		// Alert, log, record failure metrics, etc.
	}
}
```
