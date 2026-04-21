---
name: boxlang-core-dev-async-tasks
description: "Use this skill when working with BoxLang asynchronous programming: BoxFuture (CompletableFuture extension), AsyncService, executor types (VIRTUAL/FIXED/CACHED/SCHEDULED), BaseScheduler, ScheduledTask fluent API, scheduling with cron constraints, task lifecycle callbacks, and registerring schedulers via ModuleConfig.bx."
---

# BoxLang Async & Scheduled Tasks

## Overview

BoxLang provides first-class async support built on JRE 21 virtual threads and
`CompletableFuture`. Key classes:

| Class | Package | Purpose |
|---|---|---|
| `BoxFuture<T>` | `ortus.boxlang.runtime.async` | Extended `CompletableFuture` |
| `AsyncService` | `ortus.boxlang.runtime.services` | Executor and future factory |
| `BaseScheduler` | `ortus.boxlang.runtime.async.tasks` | Extend to create a scheduler |
| `ScheduledTask` | `ortus.boxlang.runtime.async.tasks` | Fluent scheduled task builder |
| `BoxExecutor` | `ortus.boxlang.runtime.async.executors` | Thead pool wrapper |

## AsyncService — Executor Factory

```java
import ortus.boxlang.runtime.services.AsyncService;
import ortus.boxlang.runtime.async.executors.BoxExecutor;
import ortus.boxlang.runtime.async.BoxFuture;

AsyncService asyncService = BoxRuntime.getInstance().getAsyncService();

// Create executors
BoxExecutor virtualExec   = asyncService.newExecutor( "myPool", ExecutorType.VIRTUAL );   // Virtual threads (default)
BoxExecutor fixedExec     = asyncService.newExecutor( "myFixed", ExecutorType.FIXED, 4 ); // Fixed 4-thread pool
BoxExecutor cachedExec    = asyncService.newExecutor( "myCached", ExecutorType.CACHED );  // Cached thread pool
BoxExecutor scheduledExec = asyncService.newScheduledExecutor( "myScheduled" );           // For scheduled tasks

// Get an existing executor
BoxExecutor exec = asyncService.getExecutor( "myPool" );

// Check existence
boolean exists = asyncService.hasExecutor( "myPool" );

// Shut it down
asyncService.shutdownExecutor( "myPool" );
```

### Executor Types

| Type | Backed By | Best For |
|---|---|---|
| `VIRTUAL` | `Executors.newVirtualThreadPerTaskExecutor()` | I/O-bound work (default) |
| `FIXED` | `Executors.newFixedThreadPool(n)` | CPU-bound work with known concurrency |
| `CACHED` | `Executors.newCachedThreadPool()` | Short-lived tasks with variable load |
| `SCHEDULED` | `ScheduledThreadPoolExecutor` | Scheduled and recurring tasks |

## BoxFuture — Async Work

`BoxFuture<T>` extends `CompletableFuture<T>` with fluent BoxLang helpers.

```java
import ortus.boxlang.runtime.async.BoxFuture;

// Create a future that runs work asynchronously
BoxFuture<String> future = asyncService.newFuture( () -> fetchFromRemote( url ) );

// Chain transformations
future
    .thenApply( result -> result.toUpperCase() )
    .thenAccept( result -> System.out.println( "Got: " + result ) )
    .exceptionally( err -> {
        logger.error( "Failed: {}", err.getMessage() );
        return null;
    });

// Block and get result (with timeout)
String result = future.get( 10, TimeUnit.SECONDS );

// All-of: wait for multiple futures
BoxFuture<Void> all = asyncService.allOf(
    asyncService.newFuture( () -> taskA() ),
    asyncService.newFuture( () -> taskB() )
);
all.join();

// Any-of: first to complete wins
BoxFuture<Object> any = asyncService.anyOf(
    asyncService.newFuture( () -> serviceA() ),
    asyncService.newFuture( () -> serviceB() )
);
Object first = any.join();
```

### BoxFuture in BoxLang Script

```boxlang
// Using runAsync BIF
var future = runAsync( () -> {
    return fetchData()
})

// Chain
var result = future
    .then( (v) -> v.toUpperCase() )
    .get()

// Parallel execution
var futures = [
    runAsync( () -> fetchUsers() ),
    runAsync( () -> fetchOrders() )
]

// Wait for all
var all = BoxFuture::allOf( futures )
all.join()
```

## BaseScheduler — Creating a Scheduler

Extend `BaseScheduler` to define a scheduler with one or more tasks.
Override `configure()` to register tasks.

### Java Scheduler

```java
import ortus.boxlang.runtime.async.tasks.BaseScheduler;
import ortus.boxlang.runtime.async.tasks.ScheduledTask;

public class MyModuleScheduler extends BaseScheduler {

    public MyModuleScheduler() {
        super( "my-module-scheduler" );
    }

    @Override
    public void configure() {
        // Register tasks using the fluent task() API
        task( "cleanupExpiredSessions" )
            .call( () -> sessionService.cleanExpired() )
            .every( 15, TimeUnit.MINUTES );

        task( "generateDailyReport" )
            .call( () -> reportService.generate() )
            .dailyAt( "02:00" );

        task( "healthCheck" )
            .call( () -> monitor.ping() )
            .every( 30, TimeUnit.SECONDS )
            .withNoOverlaps();
    }

    // Optional lifecycle callbacks
    @Override
    public void onStartup() {
        this.logger.info( "MyModuleScheduler started" );
    }

    @Override
    public void onShutdown() {
        this.logger.info( "MyModuleScheduler shutting down" );
    }

    @Override
    public void onError( ScheduledTask task, Exception e ) {
        this.logger.error( "Task [{}] failed: {}", task.getName(), e.getMessage(), e );
    }

    @Override
    public void onSuccess( ScheduledTask task, Object result ) {
        this.logger.debug( "Task [{}] succeeded", task.getName() );
    }
}
```

### BoxLang Scheduler

```boxlang
// schedulers/MyScheduler.bx
class extends="ortus.boxlang.runtime.async.tasks.BaseScheduler" {

    function configure() {
        // Tasks registered via the Java task() API called through DynamicObject
        task( "cleanup" )
            .call( () -> cleanupExpiredData() )
            .everyHour()

        task( "report" )
            .call( () -> generateReport() )
            .dailyAt( "06:00" )
    }

}
```

## ScheduledTask — Fluent API

`ScheduledTask` has a rich fluent API for defining frequency and constraints.

### Frequency Methods

```java
ScheduledTask t = task( "myTask" ).call( callable );

// Time-based intervals
t.every( 5, TimeUnit.MINUTES );
t.everyMinute();
t.everyHour();
t.everyDay();
t.everyWeek();
t.everyMonth();

// Delay before first run
t.startOn( LocalDateTime.now().plusHours( 1 ) );
t.withDelay( 30, TimeUnit.SECONDS );

// Daily at a specific time
t.dailyAt( "08:00" );      // HH:mm
t.weeklyOn( 2, "08:00" );  // Day of week (1=Mon), time

// Monthly
t.monthlyOn( 1, "00:00" ); // 1st of month at midnight
```

### Constraint Methods

```java
// Day constraints
t.onWeekends();         // Only Sat/Sun
t.onWeekdays();         // Only Mon-Fri
t.onMonday();
t.onTuesday();
// ... onWednesday(), onThursday(), onFriday(), onSaturday(), onSunday()

t.onFirstBusinessDayOfMonth();
t.onLastBusinessDayOfMonth();
t.dayOfMonth( 15 );     // Specific day

// Dynamic constraint — skip task if predicate returns false
t.when( (task) -> systemIsReady() );

// Prevent overlapping runs
t.withNoOverlaps();   // Don't fire if previous run still active

// Disable this task (useful for debugging)
t.disable();
// or use xtask() from the scheduler:
// xtask("myTask").call(callable).everyHour();
```

### Callbacks

```java
t.before( (task) -> logger.info("Starting {}", task.getName()) )
 .after( (task, result) -> logger.info("Done {}", task.getName()) )
 .onFailure( (task, err) -> alertTeam(err) )
 .onSuccess( (task, result) -> metrics.increment("task.success") );
```

## Registering a Scheduler in ModuleConfig.bx

```boxlang
// ModuleConfig.bx
class {

    function onLoad() {
        // Register and start a Java scheduler
        var scheduler = createObject( "java", "com.example.schedulers.MyModuleScheduler" ).init()
        boxRuntime.getSchedulerService().registerScheduler( scheduler )
        scheduler.startup()

        log.info( "MyModuleScheduler registered and started" )
    }

    function onUnload() {
        // Schedulers are auto-shutdown by SchedulerService on runtime shutdown.
        // Explicit shutdown only needed for early cleanup:
        boxRuntime.getSchedulerService().removeScheduler( "my-module-scheduler" )
        log.info( "MyModuleScheduler removed" )
    }

}
```

## SchedulerService API

```java
import ortus.boxlang.runtime.services.SchedulerService;

SchedulerService schedulerSvc = BoxRuntime.getInstance().getSchedulerService();

// Check if a scheduler is registered
boolean has = schedulerSvc.hasScheduler( "my-module-scheduler" );

// Get an existing scheduler
BaseScheduler sched = schedulerSvc.getScheduler( "my-module-scheduler" );

// Remove (also calls shutdown)
schedulerSvc.removeScheduler( "my-module-scheduler" );

// List all registered schedulers
Set<String> names = schedulerSvc.getSchedulerNames();
```

## Task Lifecycle Events (Interceptors)

These `BoxEvent` keys fire for every task in every scheduler:

| Event | When |
|---|---|
| `schedulerBeforeAnyTask` | Before a task runs |
| `schedulerAfterAnyTask` | After a task runs |
| `schedulerOnAnyTaskSuccess` | Task completed without error |
| `schedulerOnAnyTaskError` | Task threw an exception |
| `onSchedulerStartup` | Scheduler started |
| `onSchedulerShutdown` | Scheduler stopped |

## Testing Schedulers

```java
// Create and run in isolation
MyModuleScheduler scheduler = new MyModuleScheduler();
scheduler.configure();

// Get a registered task
ScheduledTask task = scheduler.getTask( "cleanupExpiredSessions" );
assertNotNull( task );

// Run a task manually (bypasses scheduling)
task.run();
```

```boxlang
// tests/specs/SchedulerTest.bx
class extends="testbox.system.BaseSpec" {

    function run() {
        describe( "MyScheduler tasks", () -> {
            it( "should have the cleanup task registered", () -> {
                var scheduler = new com.example.schedulers.MyModuleScheduler()
                scheduler.configure()
                expect( scheduler.hasTask("cleanupExpiredSessions") ).toBeTrue()
            })
        })
    }

}
```

## References

- [AsyncService.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/AsyncService.java)
- [BoxFuture.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/async/BoxFuture.java)
- [BaseScheduler.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/async/tasks/BaseScheduler.java)
- [ScheduledTask.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/async/tasks/ScheduledTask.java)
- [BoxLang Async Docs](https://boxlang.ortusbooks.com/boxlang-framework/async-programming)
