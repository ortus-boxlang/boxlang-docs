# Scheduler Service Events

These events are announced by the **SchedulerService** to allow interceptors to monitor and react to scheduler lifecycle and management operations. They are announced on the **global interceptor pool**.

| Event Name                   | Cancellable | Description                                        |
| ---------------------------- | :---------: | -------------------------------------------------- |
| `onSchedulerServiceStartup`  |     No      | When the scheduler service starts up.              |
| `onSchedulerServiceShutdown` |     No      | When the scheduler service shuts down.             |
| `onAllSchedulersStarted`     |     No      | After all registered schedulers have been started. |
| `onSchedulerStartup`         |     No      | When an individual scheduler starts up.            |
| `onSchedulerShutdown`        |     No      | When an individual scheduler shuts down.           |
| `onSchedulerRestart`         |     No      | When an individual scheduler is restarted.         |
| `onSchedulerRegistration`    |     No      | When a scheduler is registered.                    |
| `onSchedulerRemoval`         |     No      | When a scheduler is removed.                       |

* [`onSchedulerServiceStartup`](#onschedulerservicestartup)
* [`onSchedulerServiceShutdown`](#onschedulerserviceshutdown)
* [`onAllSchedulersStarted`](#onallschedulersstarted)
* [`onSchedulerStartup`](#onschedulerstartup)
* [`onSchedulerShutdown`](#onschedulershutdown)
* [`onSchedulerRestart`](#onschedulerrestart)
* [`onSchedulerRegistration`](#onschedulerregistration)
* [`onSchedulerRemoval`](#onschedulerremoval)

## onSchedulerServiceStartup

Fired when the SchedulerService starts up during runtime initialization — after all registered schedulers have been started.

### Data Structure

| Data Key           | Type               | Description                    |
| ------------------ | ------------------ | ------------------------------ |
| `schedulerService` | `SchedulerService` | The SchedulerService instance. |

### Example

```groovy
class myListener{
	function onSchedulerServiceStartup( struct data ){
		var schedulerService = data.schedulerService;
	}
}
```

## onSchedulerServiceShutdown

Fired when the SchedulerService begins shutting down. Fires before individual schedulers are shut down.

### Data Structure

| Data Key           | Type               | Description                    |
| ------------------ | ------------------ | ------------------------------ |
| `schedulerService` | `SchedulerService` | The SchedulerService instance. |

### Example

```groovy
class myListener{
	function onSchedulerServiceShutdown( struct data ){
		var schedulerService = data.schedulerService;
	}
}
```

## onAllSchedulersStarted

Fired after all registered schedulers have been started during service startup.

### Data Structure

| Data Key     | Type                   | Description                                     |
| ------------ | ---------------------- | ----------------------------------------------- |
| `schedulers` | `Map<Key, IScheduler>` | Map of all registered schedulers keyed by name. |

### Example

```groovy
class myListener{
	function onAllSchedulersStarted( struct data ){
		var schedulers = data.schedulers;
	}
}
```

## onSchedulerStartup

Fired after an individual scheduler has started. Fires once per scheduler during service startup and also when a scheduler is started via `registerAndStartScheduler`.

### Data Structure

| Data Key    | Type         | Description                    |
| ----------- | ------------ | ------------------------------ |
| `scheduler` | `IScheduler` | The scheduler that started up. |

### Example

```groovy
class myListener{
	function onSchedulerStartup( struct data ){
		var scheduler = data.scheduler;
	}
}
```

## onSchedulerShutdown

Fired before an individual scheduler is shut down. Fires both during service shutdown and when a scheduler is explicitly removed.

### Data Structure

| Data Key    | Type         | Description                                            |
| ----------- | ------------ | ------------------------------------------------------ |
| `scheduler` | `IScheduler` | The scheduler being shut down.                         |
| `force`     | `boolean`    | Whether the shutdown is forced (no graceful waiting).  |
| `timeout`   | `long`       | Milliseconds to wait for graceful shutdown.            |

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

Fired before an individual scheduler is restarted. The actual restart happens after this event fires.

### Data Structure

| Data Key    | Type         | Description                                            |
| ----------- | ------------ | ------------------------------------------------------ |
| `scheduler` | `IScheduler` | The scheduler being restarted.                         |
| `force`     | `boolean`    | Whether the restart forces an immediate shutdown.      |
| `timeout`   | `long`       | Milliseconds to wait for the scheduler to stop.        |

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

Fired when a scheduler is registered with the SchedulerService. If `force=true`, an existing scheduler with the same name was removed first before this event fires.

### Data Structure

| Data Key    | Type         | Description                                                       |
| ----------- | ------------ | ----------------------------------------------------------------- |
| `scheduler` | `IScheduler` | The scheduler that was registered.                                |
| `force`     | `Boolean`    | Whether the registration forced replacement of an existing entry. |

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

Fired when a scheduler is removed from the SchedulerService. Fires before the scheduler is shut down.

### Data Structure

| Data Key    | Type         | Description                                       |
| ----------- | ------------ | ------------------------------------------------- |
| `scheduler` | `IScheduler` | The scheduler being removed.                      |
| `force`     | `boolean`    | Whether the removal forces an immediate shutdown. |
| `timeout`   | `long`       | Milliseconds to wait for graceful shutdown.       |

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
