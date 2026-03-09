# Scheduler Service Events

These events occur around the management of multiple schedulers in the system.

| Event Name                   | Data | Description                            |
| ---------------------------- | :--: | -------------------------------------- |
| `onSchedulerServiceStartup`  | `schedulerService` | When the scheduler service starts up.  |
| `onSchedulerServiceShutdown` | `schedulerService` | When the scheduler service shuts down. |
| `onAllSchedulersStarted`     | `schedulerService` | After all schedulers have started.     |
| `onSchedulerRemoval`         | `name` | When a scheduler is removed.           |
| `onSchedulerRegistration`    | `name`, `scheduler` | When a scheduler is registered.        |
# Scheduler Service Events Documentation

This document outlines all the events that are announced by the **SchedulerService** in BoxLang. These events allow interceptors to monitor and react to scheduler lifecycle and management operations.

## Event Overview

The SchedulerService announces events at key points in the scheduler lifecycle:
- Service startup and shutdown
- Individual scheduler startup and shutdown
- Scheduler registration and removal
- All schedulers startup completion

---

## Events

### `onSchedulerServiceStartup`

**Event Key:** `ON_SCHEDULER_SERVICE_STARTUP`

**Triggered:** When the SchedulerService starts up during runtime initialization.

**Data Payload:**

```java
{
  "schedulerService": SchedulerService // The SchedulerService instance
}
```

**Interceptor Method:**
```boxlang
function onSchedulerServiceStartup( data ) {
  var schedulerService = data.schedulerService;
  // Handle startup logic
}
```

**Location in Code:** [SchedulerService.java:121-123](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/SchedulerService.java#L121-L123)

---

### `onSchedulerServiceShutdown`

**Event Key:** `ON_SCHEDULER_SERVICE_SHUTDOWN`

**Triggered:** When the SchedulerService shuts down during runtime shutdown.

**Data Payload:**

```java
{
  "schedulerService": SchedulerService // The SchedulerService instance
}
```

**Interceptor Method:**
```boxlang
function onSchedulerServiceShutdown( data ) {
  var schedulerService = data.schedulerService;
  // Handle shutdown logic
}
```

**Location in Code:** [SchedulerService.java:169-171](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/SchedulerService.java#L169-L171)

---

### `onAllSchedulersStarted`

**Event Key:** `ON_ALL_SCHEDULERS_STARTED`

**Triggered:** After all registered schedulers have been successfully started.

**Data Payload:**

```java
{
  "schedulers": Map<Key, IScheduler> // Map of all schedulers keyed by their names
}
```

**Interceptor Method:**
```boxlang
function onAllSchedulersStarted( data ) {
  var allSchedulers = data.schedulers;
  
  // Iterate through schedulers
  for ( var schedulerName in allSchedulers ) {
    var scheduler = allSchedulers[ schedulerName ];
    // Access scheduler methods like scheduler.getSchedulerName()
  }
}
```

**Data Structure Details:**
- `schedulers` is a `Map<Key, IScheduler>` where keys are scheduler names
- Each `IScheduler` instance provides methods to query scheduler state and configuration

**Location in Code:** [SchedulerService.java:199-201](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/SchedulerService.java#L199-L201)

---

### `onSchedulerRegistration`

**Event Key:** `ON_SCHEDULER_REGISTRATION`

**Triggered:** When a new scheduler is registered with the SchedulerService.

**Data Payload:**

```java
{
  "scheduler": IScheduler,  // The scheduler instance that was registered
  "force": Boolean          // Whether the registration was forced (overwrites existing)
}
```

**Interceptor Method:**
```boxlang
function onSchedulerRegistration( data ) {
  var scheduler = data.scheduler;
  var force = data.force;
  var schedulerName = scheduler.getSchedulerName();
  
  if ( force ) {
    // Handle forced registration (overwrote existing scheduler)
  }
}
```

**Data Structure Details:**
- `scheduler`: The `IScheduler` instance that provides access to scheduler properties and methods
  - `getSchedulerName()` - Returns the name of the scheduler
  - Other scheduler-specific methods for querying state and configuration
- `force`: Boolean indicating if this registration overwrote an existing scheduler with the same name

**Location in Code:** [SchedulerService.java:398-400](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/SchedulerService.java#L398-L400)

---

### `onSchedulerRemoval`

**Event Key:** `ON_SCHEDULER_REMOVAL`

**Triggered:** When a scheduler is removed from the SchedulerService.

**Data Payload:**

```java
{
  "scheduler": IScheduler,  // The scheduler instance that was removed
  "force": Boolean,         // Whether the removal was forced
  "timeout": Long           // Shutdown timeout in seconds (if applicable)
}
```

**Interceptor Method:**
```boxlang
function onSchedulerRemoval( data ) {
  var scheduler = data.scheduler;
  var force = data.force;
  var timeout = data.timeout;
  var schedulerName = scheduler.getSchedulerName();
  
  writeln( "Scheduler [#schedulerName#] is being removed" );
  
  if ( force ) {
    // Force removal with no waiting
  } else {
    // Graceful removal with shutdown timeout
  }
}
```

**Data Structure Details:**
- `scheduler`: The `IScheduler` instance being removed
  - `getSchedulerName()` - Returns the name of the scheduler
  - Other scheduler-specific methods
- `force`: Boolean indicating if the removal is forced (no graceful shutdown)
- `timeout`: Long representing the timeout duration in seconds for scheduler shutdown

**Location in Code:** [SchedulerService.java:439-444](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/SchedulerService.java#L439-L444)

---

## Additional Scheduler Events

While the SchedulerService manages these service-level events, individual schedulers also announce their own events. These include:

- `ON_SCHEDULER_STARTUP` - Individual scheduler startup
- `ON_SCHEDULER_SHUTDOWN` - Individual scheduler shutdown
- `ON_SCHEDULER_RESTART` - Individual scheduler restart
- `SCHEDULER_BEFORE_ANY_TASK` - Before any scheduled task executes
- `SCHEDULER_AFTER_ANY_TASK` - After any scheduled task executes
- `SCHEDULER_ON_ANY_TASK_SUCCESS` - When any scheduled task succeeds
- `SCHEDULER_ON_ANY_TASK_ERROR` - When any scheduled task errors

See [BoxEvent.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/events/BoxEvent.java) for complete event definitions.

---

## Example Interceptor Implementation

```boxlang
/**
 * A sample interceptor for Scheduler Service events
 */
class SchedulerInterceptor {

  function configure() {
    // Any configuration needed
  }

  function onSchedulerServiceStartup( data ) {
    var schedulerService = data.schedulerService;
    writeln( "Scheduler Service has started" );
  }

  function onAllSchedulersStarted( data ) {
    var schedulers = data.schedulers;
    writeln( "All #schedulers.size()# schedulers have been started" );
    
    for ( var name in schedulers ) {
      writeln( "  - #name#" );
    }
  }

  function onSchedulerRegistration( data ) {
    var scheduler = data.scheduler;
    var force = data.force;
    var schedulerName = scheduler.getSchedulerName();
    
    writeln( "Scheduler registered: #schedulerName#" & 
             (force ? " (force overwrite)" : "") );
  }

  function onSchedulerRemoval( data ) {
    var scheduler = data.scheduler;
    var force = data.force;
    var timeout = data.timeout;
    var schedulerName = scheduler.getSchedulerName();
    
    writeln( "Scheduler removed: #schedulerName#" &
             (force ? " (forced)" : " (graceful shutdown #timeout#s)") );
  }

  function onSchedulerServiceShutdown( data ) {
    var schedulerService = data.schedulerService;
    writeln( "Scheduler Service has shut down" );
  }

}
```

---

## Registering an Interceptor

To register an interceptor with the runtime to listen to scheduler service events:

```boxlang
// In your Application.bx or initialization code
var interceptor = new SchedulerInterceptor();
var interceptorService = getRuntimeAttribute( "boxRuntime" ).getInterceptorService();
interceptorService.register( interceptor );
```

Or via module configuration:

```boxlang
// In ModuleConfig.bx
function configure() {
  var interceptor = new path.to.SchedulerInterceptor();
  interceptorService.register( interceptor );
}
```

---

## Related Resources

- [SchedulerService Source](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/SchedulerService.java)
- [BoxEvent Enum](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/events/BoxEvent.java)
- [InterceptorService Source](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/InterceptorService.java)
- [Scheduler Implementation](https://github.com/ortus-boxlang/BoxLang/tree/development/src/main/java/ortus/boxlang/runtime/async/tasks)
