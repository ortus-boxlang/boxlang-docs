# Scheduler Events

Scheduler events are fired throughout the lifecycle of schedulers and schedled task execution. these events allow you to hook into scheduler operations, monitor task execution, and respond to scheduler state changes.

## Scheduler Lifecycle Events

### `onSchedulerStartup`
**Event:** `onSchedulerStartup`

Fired when a scheduler starts up and begins accepting scheduled tasks for execution.

**Data Structure:**
```boxlang
{
    scheduler: IScheduler  // The scheduler instance that started
}
```

**Use Cases:**
- Initialize resources needed for task execution
- Log scheduler initialization
- Start monitoring or metrics collection

---

### `onSchedulerShutdown`
**Event:** `onSchedulerShutdown`

Fired when a scheduler is being shut down and will stop executing tasks.

**Data Structure:**
```boxlang
{
    scheduler: IScheduler,  // The scheduler instance being shut down
    force: boolean,         // Whether the shutdown is forced (immediate)
    timeout: number         // Timeout in milliseconds for graceful shutdown
}
```

**Use Cases:**
- Clean up resources associated with the scheduler
- Save final state or statistics
- Log scheduler shutdown

---

### `onSchedulerRestart`
**Event:** `onSchedulerRestart`

Fired when a scheduler is being restarted, stopping and then restarting its execution.

**Data Structure:**
```boxlang
{
    scheduler: IScheduler,  // The scheduler instance being restarted
    force: boolean,         // Whether the restart is forced (immediate)
    timeout: number         // Timeout in milliseconds for graceful shutdown before restart
}
```

**Use Cases:**
- Reinitialize resources
- Monitor scheduler restart operations
- Handle task queue cleanup during restart

---

## Scheduler Registration Events

### `onSchedulerRegistration`
**Event:** `onSchedulerRegistration`

Fired when a scheduler is registered with the SchedulerService, making it available in the system.

**Data Structure:**
```boxlang
{
    scheduler: IScheduler,  // The scheduler being registered
    force: boolean          // Whether registration forced replacement of existing scheduler
}
```

**Use Cases:**
- Track newly registered schedulers
- Perform validation on scheduler configuration
- Apply system-wide scheduler policies

---

### `onSchedulerRemoval`
**Event:** `onSchedulerRemoval`

Fired when a scheduler is removed from the system.

**Data Structure:**
```boxlang
{
    scheduler: IScheduler,  // The scheduler being removed
    force: boolean,         // Whether removal is forced
    timeout: number         // Timeout in milliseconds
}
```

**Use Cases:**
- Clean up scheduler-specific configurations
- Update monitoring/tracking systems
- Audit scheduler lifecycle

---

## Task Execution Events

### `schedulerBeforeAnyTask`
**Event:** `schedulerBeforeAnyTask`

Fired before a scheduled task begins execution. This is the first event in the task execution lifecycle.

**Data Structure:**
```boxlang
{
    task: ScheduledTask  // The task about to execute
}
```

**Task Object Properties:**
- `name` - Task name
- `group` - Task group
- `status` - Current execution status
- `stats` - Execution statistics including total runs, successes, failures, etc.

**Use Cases:**
- Validate task preconditions
- Set up task execution context
- Log task startup
- Acquire locks or resources needed for task execution
- Apply rate limiting or throttling

---

### `schedulerAfterAnyTask`
**Event:** `schedulerAfterAnyTask`

Fired after a scheduled task completes execution, whether successfully or with an error.

**Data Structure:**
```boxlang
{
    task: ScheduledTask,          // The completed task
    result: Optional<?> | Exception // Task result or exception if one occurred
}
```

**Use Cases:**
- Release resources acquired before task execution
- Log task completion
- Update monitoring metrics
- Clean up task-specific context
- Handle both successful and failed task outcomes

---

### `schedulerOnAnyTaskSuccess`
**Event:** `schedulerOnAnyTaskSuccess`

Fired after a scheduled task completes successfully without throwing an exception.

**Data Structure:**
```boxlang
{
    task: ScheduledTask,      // The successfully completed task
    result: Optional<?>       // The task's return value (may be empty if no return)
}
```

**Use Cases:**
- Record successful task metrics
- Update statistics or dashboards
- Trigger success-dependent actions
- Log successful task completion
- Send success notifications

---

### `schedulerOnAnyTaskError`
**Event:** `schedulerOnAnyTaskError`

Fired when a scheduled task throws an exception during execution.

**Data Structure:**
```boxlang
{
    task: ScheduledTask,      // The failed task
    exception: Exception      // The exception thrown during execution
}
```

**Use Cases:**
- Record failure metrics and statistics
- Log error details for debugging
- Send error alerts or notifications
- Implement retry logic
- Update error tracking systems
- Preserve error context for analysis

---

## Service-Level Events

### `onSchedulerServiceStartup`
**Event:** `onSchedulerServiceStartup`

Fired when the SchedulerService itself starts up during BoxLang runtime initialization.

**Use Cases:**
- Initialize scheduler monitoring
- Configure service-wide scheduler policies
- Load scheduler configurations

---

### `onSchedulerServiceShutdown`
**Event:** `onSchedulerServiceShutdown`

Fired when the SchedulerService shuts down with the BoxLang runtime.

**Use Cases:**
- Gracefully shutdown all schedulers
- Save scheduler state
- Clean up service-level resources

---

### `onAllSchedulersStarted`
**Event:** `onAllSchedulersStarted`

Fired after all configured schedulers have been successfully started.

**Use Cases:**
- Execute initialization logic that depends on all schedulers being ready
- Trigger dependent systems
- Log successful service startup

---

## Event Interception Pattern

Events follow a **global-to-local** pattern for before events and **local-to-global** for after events:

1. **Global Interceptors** (via `InterceptorService`)
2. **Local Interceptors** (via callbacks on task or scheduler)
3. **Local Lifecycle Handlers** (via task configuration)

This ensures proper ordering of side effects and allows both global monitoring and local control.

## Interceptor Implementation Example

```boxlang
component {
    function onSchedulerBeforeAnyTask(event) {
        var task = event.data.task;
        writeLog(
            text="Starting task: #task.getName()#",
            type="information"
        );
    }

    function onSchedulerOnAnyTaskSuccess(event) {
        var task = event.data.task;
        var result = event.data.result;
        writeLog(
            text="Task #task.getName()# completed successfully",
            type="information"
        );
    }

    function onSchedulerOnAnyTaskError(event) {
        var task = event.data.task;
        var exception = event.data.exception;
        writeLog(
            text="Task #task.getName()# failed: #exception.message#",
            type="error"
        );
    }
}
```

## Event Flow for Successful Task Execution

```
┌─────────────────────────────────────────┐
│ schedulerBeforeAnyTask                  │
│ Data: { task }                          │
└──────────────┬──────────────────────────┘
               ↓
        [Task Executes]
               ↓
┌──────────────┬──────────────────────────┐
│ schedulerAfterAnyTask                   │
│ Data: { task, result }                  │
└──────────────┬──────────────────────────┘
               ↓
┌──────────────┬──────────────────────────┐
│ schedulerOnAnyTaskSuccess               │
│ Data: { task, result }                  │
└─────────────────────────────────────────┘
```

## Event Flow for Failed Task Execution

```
┌─────────────────────────────────────────┐
│ schedulerBeforeAnyTask                  │
│ Data: { task }                          │
└──────────────┬──────────────────────────┘
               ↓
        [Task Executes & Throws]
               ↓
┌──────────────┬──────────────────────────┐
│ schedulerOnAnyTaskError                 │
│ Data: { task, exception }               │
└──────────────┬──────────────────────────┘
               ↓
┌──────────────┬──────────────────────────┐
│ schedulerAfterAnyTask                   │
│ Data: { task, result: Optional(exception) }
└─────────────────────────────────────────┘
```

## Important Considerations

- **Event Data Immutability:** Event data passed to interceptors should be treated as read-only. Modifications to the task or other event data may have unintended consequences.

- **Exception Handling:** Exceptions thrown in event interceptors are caught and logged by the task executor to prevent one interceptor's failure from affecting others.

- **Thread Safety:** Events are fired in the context of the task execution thread. If your interceptor accesses shared state, ensure proper synchronization.

- **Performance:** Keep event interceptors lightweight. Heavy operations in `schedulerBeforeAnyTask` or `schedulerAfterAnyTask` will impact task performance.

- **Scheduler Context:** The task context is available via `RequestBoxContext.getCurrent()` during task execution events.

