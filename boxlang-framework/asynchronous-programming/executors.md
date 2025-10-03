---
description: Powerful Concurrency Made Simple
icon: chart-network
---

# 🚀 Executors

## What Are Executors?

Executors in Java (and BoxLang) are high-level abstractions for managing and controlling thread execution. They provide a powerful way to handle concurrent tasks without the complexity of manually managing threads. Think of executors as specialized worker pools that can handle different types of workloads efficiently.

```
Tasks Queue  →  Executor Pool  →  Results
📋 📋 📋           🔄 🔄 🔄          ✅ ✅ ✅
```

Here is a great video you can check out about Executors: [https://www.youtube.com/watch?v=6Oo-9Can3H8&t=2s](https://www.youtube.com/watch?v=6Oo-9Can3H8&t=2s)

### **💡 Why Use Executors?**

* **Thread Management:** Automatic creation, pooling, and lifecycle management
* **Resource Control:** Limit concurrent threads to prevent system overload
* **Task Queuing:** Handle more tasks than available threads
* **Graceful Shutdown:** Clean termination of running tasks
* **Statistical Monitoring:** Real-time insights into executor performance
* **Error Handling:** Centralized exception management and logging

## Executor Types & Use Cases

Here are all the executors types available in BoxLang, each tailored for specific workloads and performance characteristics:

### 🔄 CACHED

* **Best for:** Short-lived, asynchronous tasks with unpredictable load
* **Behavior:** Creates threads on demand, reuses idle threads for 60 seconds
* **Thread Pool:** Unbounded, grows and shrinks dynamically
* **Use Case:** Web requests, quick computations, burst I/O operations
* **Performance:** Excellent for variable workloads, can consume many resources

### 📊 FIXED

* **Best for:** Consistent workload with known thread requirements
* **Behavior:** Maintains a fixed number of threads throughout lifecycle
* **Thread Pool:** Fixed size, queues tasks when all threads busy
* **Use Case:** CPU-intensive tasks, batch processing, controlled concurrency
* **Performance:** Predictable resource usage, prevents thread explosion

### 🌿 VIRTUAL (Java 19+)

* **Best for:** I/O-bound tasks requiring massive concurrency
* **Behavior:** Lightweight virtual threads managed by the JVM
* **Thread Pool:** Virtually unlimited, extremely low memory footprint
* **Use Case:** Database calls, HTTP requests, file operations, microservices
* **Performance:** Scales to millions of threads, perfect for I/O blocking

### ⚡ WORK_STEALING

* **Best for:** Recursive, divide-and-conquer algorithms with uneven workload
* **Behavior:** Threads steal work from each other's deques for load balancing
* **Thread Pool:** Dynamic work distribution, optimal CPU utilization
* **Use Case:** Parallel streams, recursive computations, map-reduce operations
* **Performance:** Excellent for tasks with varying execution times

### 🍴 FORK_JOIN

* **Best for:** Parallel decomposition of large computational tasks
* **Behavior:** Optimized for fork-join pattern with work-stealing
* **Thread Pool:** Specialized for divide-and-conquer algorithms
* **Use Case:** Parallel algorithms, mathematical computations, data processing
* **Performance:** Superior for CPU-bound recursive tasks

### ⏰ SCHEDULED

* **Best for:** Time-based task execution and periodic operations
* **Behavior:** Supports delays, fixed-rate, and fixed-delay scheduling
* **Thread Pool:** Fixed size with timing capabilities
* **Use Case:** Cron jobs, periodic cleanup, delayed tasks, heartbeats
* **Performance:** Efficient for time-sensitive operations

### 1️⃣ SINGLE

* **Best for:** Sequential task execution ensuring order
* **Behavior:** One thread processes tasks in FIFO order
* **Thread Pool:** Single thread, guarantees execution order
* **Use Case:** Order-dependent operations, logging, state management
* **Performance:** No concurrency overhead, thread-safe by design

## 🔧 Pre-defined Runtime Executors

BoxLang ships with three carefully curated executors ready for immediate use.  They are defined in `boxlang.json` in the BoxLang's Home `config` folder. Check out the [configuration](../../getting-started/configuration/executors.md) section for more information.

```json
"executors": {
	// Use this for IO bound tasks, does not support scheduling
	// This is also the default when requestion an executor service via executorGet()
	"io-tasks": {
		"type": "virtual",
		"description": "Unlimited IO bound tasks using Java Virtual Threads"
	},
	// Use this for CPU bound tasks, supports scheduling
	"cpu-tasks": {
		"type": "scheduled",
		"threads": 20,
		"description": "CPU bound tasks using a fixed thread pool with scheduling capabilities"
	},
	// Used for all scheduled tasks in the runtime
	"scheduled-tasks": {
		"type": "scheduled",
		"threads": 20,
		"description": "Scheduled tasks using a fixed thread pool with scheduling capabilities"
	}
},
```

It's up to you to create additional executors as needed, but these three cover the most common use cases.

### 🌐 io-tasks

* **Type:** VIRTUAL
* **Configuration:** Unlimited virtual threads
* **Purpose:** Unlimited I/O bound tasks using Java Virtual Threads
* **Perfect for:** Database queries, API calls, file operations, network requests
* **Default:** Used when requesting executor via `executorGet()`
* **Memory:** Extremely low per-thread overhead (\~KB vs MB for platform threads)

### 🖥️ cpu-tasks

* **Type:** SCHEDULED (20 threads)
* **Configuration:** Fixed 20-thread pool with scheduling capabilities
* **Purpose:** CPU bound tasks with optional scheduling support
* **Perfect for:** Heavy computations, data processing, algorithms, image processing
* **Scheduling:** Supports delayed and periodic execution

### ⏱️ scheduled-tasks

* **Type:** SCHEDULED (20 threads)
* **Configuration:** Dedicated 20-thread pool for runtime scheduling
* **Purpose:** All scheduled tasks in the runtime
* **Perfect for:** Cron jobs, periodic maintenance, cleanup tasks, monitoring
* **Reserved:** Used internally by BoxLang runtime for system tasks

> **💡 Pro Tip:** These executors are automatically available at runtime startup. You can access them immediately without any setup!

## 📝 Async Logging

BoxLang provides dedicated logging for all asynchronous operations through the `async.log` file located in the `logs` folder of your BoxLang home directory.  Please leverage logging as much as possible, as in asynchronous environments logging is critical for debugging and monitoring executor behavior.

###  Automatic Logging

All executor operations are automatically logged:

* Executor creation and configuration
* Task submissions and completions
* Shutdown events and timing
* Error conditions and exceptions
* Performance warnings

###  Manual Logging

You can send custom messages to the async log:

```js
// Log different message types to async.log
writeLog( text: "Starting batch processing job",  log: "async" ) // info message
writeLog( text: "Performance degradation detected", type: "Warning", log: "async" )
writeLog( text: "Task execution failed", type: "Error", log: "async" )
writeLog( text: "Debugging executor behavior", type: "Debug", log: "async" )
writeLog( text: "Detailed execution trace", type: "Trace", log: "async" )
```

**Available Log Types:**

* `"Information"` - General operational messages - (Default)
* `"Warning"` - Performance issues or concerns
* `"Error"` - Execution failures and exceptions
* `"Debug"` - Development and troubleshooting info
* `"Trace"` - Detailed execution flow information

### 📂 Log File Location

```bash
{BoxLang-Home}/logs/async.log
```

Monitor this file for:

* Executor performance issues
* Task execution failures
* Resource exhaustion warnings
* Shutdown timing problems

## 🔧 AsyncService

The `AsyncService` is BoxLang's central service for managing executors and anything async related. It provides a unified API to create, retrieve, and control executors programmatically.  This API can be available to you or module authors via the `getBoxRuntime().getAsyncService()` method, but we would highly suggest also using the global built-in functions (BIFs) for convenience.

| Method                                           | Purpose                                         | Returns      |
| ------------------------------------------------ | ----------------------------------------------- | ------------ |
| `newExecutor( name, type, threads )`             | Create new executors with custom configurations | BoxExecutor  |
| `getExecutor( name )`                            | Retrieve executor instances by name             | BoxExecutor  |
| `hasExecutor( name )`                            | Check if an executor exists                     | Boolean      |
| `deleteExecutor( name )`                         | Remove and shutdown executors                   | AsyncService |
| `shutdownExecutor( name, force, timeout, unit )` | Gracefully shutdown specific executors          | AsyncService |
| `shutdownAllExecutors( force, timeout, unit )`   | Shutdown all registered executors               | AsyncService |
| `getExecutorStatusMap()`                         | Get detailed statistics for all executors       | IStruct      |
| `getExecutorStatusMap( name )`                   | Get statistics for specific executor            | IStruct      |
| `getExecutorNames()`                             | List all registered executor names              | List         |

###  Convenience Builder Methods

```js
asyncService = getBoxRuntime().getAsyncService()

// Quick executor creation - all return BoxExecutor
 cacheExecutor = asyncService.newCachedExecutor( "my-cache" )
 workerPool = asyncService.newFixedExecutor( "workers", 10 )
 ioPool = asyncService.newVirtualExecutor( "io-pool" )
 scheduler = asyncService.newScheduledExecutor( "scheduler", 5 )
 parallelPool = asyncService.newWorkStealingExecutor( "parallel-work", 8 )
 forkJoinPool = asyncService.newForkJoinExecutor( "fork-join", 4 )
 singleThread = asyncService.newSingleExecutor( "sequential" )
```

All methods return a `BoxExecutor` instance, which is a wrapper around the Java `ExecutorService` class providing additional features like statistics, health monitoring, activity tracking, logging, and task management.

## 🏗️ BoxExecutor: Enhanced Executor Management

**Important:** BoxLang doesn't return raw Java executors. Instead, you get `BoxExecutor` instances - enhanced wrappers that provide additional functionality beyond a standard Java `ExecutorService` instance.  These executor instances can be passed around wherever an executor is needed or if you need the raw Java `ExecutorService`, you can access it via the `executor()` method on the `BoxExecutor`.

###  What is BoxExecutor?

`BoxExecutor` (formerly `ExecutorRecord` in versions prior to 1.6.0) is BoxLang's enhanced executor wrapper that provides:

* **📊 Real-time Statistics:** Active threads, completed tasks, pool size metrics, task submission counts
* **🏥 Health Monitoring:** Comprehensive health status tracking with degraded/critical state detection
* **📈 Activity Tracking:** Last activity timestamps and task submission rate monitoring
* **🔧 Enhanced Control:** Graceful and forceful shutdown capabilities
* **📝 Integrated Logging:** Automatic logging to `async.log`
* **⚡ Convenience Methods:** Simplified task submission and result handling
* **🎯 Task Factory:** Built-in ScheduledTask creation for complex workflows
* **🔄 State Management:** Comprehensive executor state monitoring
* **⚠️ Health Reports:** Detailed health analysis with issues, recommendations, and insights

###  BoxExecutor Methods

Here are the key methods available on `ExecutorRecord` instances:

#### 🎯 Task Submission Methods

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `submit( callable )` | Submit a Callable task for asynchronous execution | `Future` | Submit and handle result later |
| `submit( runnable )` | Submit a Runnable task for asynchronous execution | `Future` | Fire-and-forget or wait for completion |
| `submitAndGet( callable )` | Submit and immediately wait for result | `Object` | Blocking call, returns result directly |
| `submitAndGet( runnable )` | Submit Runnable and wait for completion | `Object` | Blocking call for side-effect tasks |

```js
executor = executorGet( "cpu-tasks" );

// Submit and handle later
future = executor.submit( () => expensiveCalculation() );
// ... do other work ...
result = future.get(); // Get result when ready

// Submit and get immediately (blocks)
result = executor.submitAndGet( () => databaseQuery() );
```

#### 🔧 Lifecycle Management

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `shutdownQuiet()` | Non-blocking shutdown, no new tasks accepted | `void` | Quick shutdown without waiting |
| `shutdownAndAwaitTermination( timeout, unit )` | Graceful shutdown with timeout | `void` | Recommended for clean shutdown |

```js
// Quick shutdown - doesn't wait
executor.shutdownQuiet();

// Graceful shutdown with 30-second timeout
executor.shutdownAndAwaitTermination( 30, "seconds" );
```

> **⚠️ CRITICAL WARNING:** Once an executor is shutdown, it **CANNOT** be restarted! The executor becomes permanently dead. Always plan your shutdown strategy carefully and prefer graceful shutdown with `shutdownAndAwaitTermination()` when possible.

#### 🏭 Task Factory Methods

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `newTask( name )` | Create named ScheduledTask bound to this executor | `ScheduledTask` | For complex scheduling workflows |
| `newTask()` | Create auto-named ScheduledTask bound to this executor | `ScheduledTask` | Quick task creation |

```js
// Create named task for tracking
cleanupTask = executor.newTask( "cleanup-job" );
cleanupTask.call( () => performCleanup() )
    .every( 1, "hours" )
    .start();

// Auto-named task
quickTask = executor.newTask()
    .call( () => sendNotification() )
    .in( 5, "minutes" )
    .start();
```

#### 📊 Information & Monitoring

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `getStats()` | Get comprehensive executor statistics with health monitoring | `IStruct` | Performance monitoring, debugging, health checks |
| `isHealthy()` | Quick boolean health check | `Boolean` | Fast health verification |
| `name()` | Get executor name | `String` | Identification and logging |
| `type()` | Get executor type | `ExecutorType` | Type checking and decisions |
| `maxThreads()` | Get maximum thread count | `Integer` | Capacity planning |
| `executor()` | Get underlying Java ExecutorService | `ExecutorService` | Direct Java interop if needed |
| `isTerminated()` | Check if all tasks completed after shutdown | `Boolean` | Shutdown verification |
| `isTerminating()` | Check if executor is shutting down | `Boolean` | State checking |
| `isShutdown()` | Check if executor has been shut down | `Boolean` | State checking |

```js
// Quick health check
if ( executor.isHealthy() ) {
    println( "Executor is healthy and ready" )
}

// Detailed health monitoring
stats = executor.getStats()
println( "Name: #executor.name()#" )
println( "Type: #executor.type()#" )
println( "Max Threads: #executor.maxThreads()#" )
println( "Active: #stats.activeCount#/#stats.maximumPoolSize#" )
println( "Health Status: #stats.healthStatus#" )
println( "Pool Utilization: #stats.poolUtilization#%" )

// Check detailed health report
healthReport = stats.healthReport
println( "Health Summary: #healthReport.summary#" )
if ( arrayLen( healthReport.issues ) > 0 ) {
    println( "Issues detected: #arrayLen( healthReport.issues )#" )
}

// Get raw Java executor if needed
javaExecutor = executor.executor()
```

#### 🎯 Specialized Methods

| Method | Purpose | Returns | Availability |
|--------|---------|---------|--------------|
| `scheduledExecutor()` | Get as BoxScheduledExecutor | `BoxScheduledExecutor` | SCHEDULED type only |

```js
// For scheduled executors only
scheduledExec = executorGet( "scheduled-tasks" );
scheduler = scheduledExec.scheduledExecutor();
// Access to scheduling-specific methods
```

### 📊 BoxExecutor Statistics & Health Monitoring

Every BoxExecutor provides detailed runtime statistics including comprehensive health monitoring introduced in version 1.6.0:

```js
executor = executorGet( "cpu-tasks" )
stats = executor.getStats()

// ============================================
// BASIC INFORMATION
// ============================================
println( "Name: #stats.name#" )
println( "Type: #stats.type#" )
println( "Created: #stats.created#" )
println( "Uptime (days): #stats.uptimeDays#" )
println( "Uptime (seconds): #stats.uptimeSeconds#" )

// ============================================
// ACTIVITY TRACKING (New in 1.6.0)
// ============================================
println( "Last Activity: #stats.lastActivity#" )
println( "Last Activity (minutes ago): #stats.lastActivityMinutesAgo#" )
println( "Last Activity (seconds ago): #stats.lastActivitySecondsAgo#" )
println( "Task Submission Count: #stats.taskSubmissionCount#" )
println( "Average Tasks/Second: #stats.averageTasksPerSecond#" )
println( "Average Tasks/Minute: #stats.averageTasksPerMinute#" )

// ============================================
// EXECUTOR STATE
// ============================================
println( "Is Shutdown: #stats.isShutdown#" )
println( "Is Terminated: #stats.isTerminated#" )
println( "Is Terminating: #stats.isTerminating#" )

// ============================================
// POOL METRICS (ThreadPoolExecutor types)
// ============================================
println( "Core Pool Size: #stats.corePoolSize#" )
println( "Current Pool Size: #stats.poolSize#" )
println( "Maximum Pool Size: #stats.maximumPoolSize#" )
println( "Largest Pool Size: #stats.largestPoolSize#" )
println( "Pool Utilization: #stats.poolUtilization#%" )

// ============================================
// TASK METRICS
// ============================================
println( "Active Threads: #stats.activeCount#" )
println( "Completed Tasks: #stats.completedTaskCount#" )
println( "Total Tasks: #stats.taskCount#" )
println( "Task Completion Rate: #stats.taskCompletionRate#%" )
println( "Thread Utilization: #stats.threadsUtilization#%" )

// ============================================
// QUEUE METRICS (ThreadPoolExecutor types)
// ============================================
println( "Queue Type: #stats.queueType#" )
println( "Queue Size: #stats.queueSize#" )
println( "Queue Capacity: #stats.queueCapacity#" )
println( "Queue Remaining Capacity: #stats.queueRemainingCapacity#" )
println( "Queue Is Empty: #stats.queueIsEmpty#" )
println( "Queue Is Full: #stats.queueIsFull#" )
println( "Queue Utilization: #stats.queueUtilization#%" )

// ============================================
// HEALTH MONITORING (New in 1.6.0)
// ============================================
println( "\n=== HEALTH STATUS ===" )
println( "Health Status: #stats.healthStatus#" )
// Possible values: "healthy", "degraded", "critical", "idle", "shutdown", "terminated", "draining"

// Get detailed health report
healthReport = stats.healthReport

println( "\n=== HEALTH REPORT ===" )
println( "Status: #healthReport.status#" )
println( "Summary: #healthReport.summary#" )
println( "Last Checked: #healthReport.lastChecked#" )

// Display issues if any
if ( arrayLen( healthReport.issues ) > 0 ) {
    println( "\nIssues Detected:" )
    for ( issue in healthReport.issues ) {
        println( "  - #issue#" )
    }
}

// Display recommendations
if ( arrayLen( healthReport.recommendations ) > 0 ) {
    println( "\nRecommendations:" )
    for ( recommendation in healthReport.recommendations ) {
        println( "  - #recommendation#" )
    }
}

// Display critical alerts
if ( arrayLen( healthReport.alerts ) > 0 ) {
    println( "\nCRITICAL ALERTS:" )
    for ( alert in healthReport.alerts ) {
        println( "  ⚠️ #alert#" )
    }
}

// Display performance insights
if ( arrayLen( healthReport.insights ) > 0 ) {
    println( "\nPerformance Insights:" )
    for ( insight in healthReport.insights ) {
        println( "  💡 #insight#" )
    }
}

// ============================================
// FORK/JOIN SPECIFIC METRICS
// ============================================
if ( stats.keyExists( "stealCount" ) ) {
    println( "\n=== FORK/JOIN METRICS ===" )
    println( "Active Thread Count: #stats.activeThreadCount#" )
    println( "Parallelism: #stats.parallelism#" )
    println( "Pool Size: #stats.poolSize#" )
    println( "Queued Submission Count: #stats.queuedSubmissionCount#" )
    println( "Queued Task Count: #stats.queuedTaskCount#" )
    println( "Running Thread Count: #stats.runningThreadCount#" )
    println( "Steal Count: #stats.stealCount#" )
}
```

#### 🏥 Health Status Values

The `healthStatus` field can return the following values:

* **`"healthy"`** - Executor operating normally within all thresholds
* **`"degraded"`** - Performance issues detected, action recommended
* **`"critical"`** - Serious issues requiring immediate attention
* **`"idle"`** - No recent activity, may be underutilized
* **`"shutdown"`** - Executor has been shut down, no new tasks accepted
* **`"terminated"`** - All tasks completed, executor fully terminated
* **`"draining"`** - Shutting down and processing remaining tasks

#### 🎯 Health Monitoring Thresholds

BoxExecutor uses configurable thresholds to determine health status:

| Metric | Degraded Threshold | Critical Threshold |
|--------|-------------------|-------------------|
| **Pool Utilization** | 75% | 95% |
| **Thread Utilization** | 75% | 95% |
| **Queue Utilization** | 70% | 95% |
| **Task Completion Rate** | <50% | <25% |
| **Inactivity** | 30 minutes | N/A |

#### 📋 Health Report Structure

The health report provides detailed analysis:

```js
{
    "status": "healthy|degraded|critical|idle|shutdown|terminated|draining",
    "summary": "Brief description of health status",
    "lastChecked": "2025-10-03T14:30:00",
    "issues": [
        "High pool utilization: 87%",
        "Queue approaching capacity"
    ],
    "recommendations": [
        "Consider increasing pool size",
        "Monitor queue growth"
    ],
    "alerts": [
        "CRITICAL: Queue is full, tasks may be rejected"
    ],
    "insights": [
        "Processing 42.5 tasks per second",
        "Executor has been running for 5.2 days"
    ]
}
```

#### 🔍 Monitoring Examples

**Check overall health:**

```js
executor = executorGet( "cpu-tasks" )

// Quick boolean check
if ( !executor.isHealthy() ) {
    writeLog(
        text: "Executor #executor.name()# is unhealthy!",
        type: "Warning",
        log: "async"
    )

    stats = executor.getStats()
    writeLog(
        text: "Health Status: #stats.healthStatus#, Issues: #arrayLen( stats.healthReport.issues )#",
        type: "Warning",
        log: "async"
    )
}
```

**Monitor specific metrics:**

```js
stats = executor.getStats()

// Check for high utilization
if ( stats.poolUtilization > 80 ) {
    writeLog(
        text: "High pool utilization: #stats.poolUtilization#%",
        type: "Warning",
        log: "async"
    )
}

// Check for queue issues
if ( stats.queueUtilization > 70 ) {
    writeLog(
        text: "Queue filling up: #stats.queueSize# tasks queued",
        type: "Warning",
        log: "async"
    )
}

// Check task completion rate
if ( stats.taskCount > 10 && stats.taskCompletionRate < 50 ) {
    writeLog(
        text: "Low task completion rate: #stats.taskCompletionRate#%",
        type: "Warning",
        log: "async"
    )
}
```

**Automated health checks:**

```js
function performHealthCheck() {
    allExecutors = executorList()

    for ( executorName in allExecutors ) {
        executor = executorGet( executorName )
        stats = executor.getStats()

        writeLog(
            text: "Health Check - #executorName#: Status=#stats.healthStatus#, Active=#stats.activeCount#, Queue=#stats.queueSize#",
            type: "Information",
            log: "async"
        )

        // Alert on critical status
        if ( stats.healthStatus == "critical" ) {
            writeLog(
                text: "CRITICAL: Executor #executorName# is in critical state!",
                type: "Error",
                log: "async"
            )

            // Send alert to monitoring system
            sendAlert( executorName, stats )
        }
    }
}

// Schedule health checks every 5 minutes
healthCheckTask = executorGet( "scheduled-tasks" ).newTask( "health-monitor" )
healthCheckTask.call( performHealthCheck )
    .every( 5, "minutes" )
    .start()
```

## 🌟 Global BIFs (Built-in Functions)

BoxLang provides convenient global functions for executor management and usage:

| Function                                       | Purpose                                             | Returns     | Example                                 |
| ---------------------------------------------- | --------------------------------------------------- | ----------- | --------------------------------------- |
| `executorGet( [name] )`                        | Get BoxExecutor by name (defaults to "io-tasks")    | BoxExecutor | `executorGet( "cpu-tasks" )`            |
| `executorHas( name )`                          | Check if executor exists                            | Boolean     | `executorHas( "my-pool" )`              |
| `executorList()`                               | List all executor names                             | Array       | `executorList()`                        |
| `executorNew( name, type, [threads] )`         | Create new executor                                 | BoxExecutor | `executorNew( "pool", "fixed", 8 )`     |
| `executorShutdown( name, [force], [timeout] )` | Shutdown executor gracefully or forcefully          | Boolean     | `executorShutdown( "pool", false, 30 )` |
| `executorStatus( [name] )`                     | Get executor statistics and status                  | Struct      | `executorStatus( "cpu-tasks" )`         |

Remember that if the BIF returns an executor, it will be a `BoxExecutor` instance, not a raw Java ExecutorService.  This allows you to leverage all the enhanced features and methods provided by BoxLang, including health monitoring, activity tracking, and comprehensive statistics.

### BIF Usage Examples

```js
// Quick executor access
defaultIO = executorGet(); // Gets "io-tasks"
cpuPool = executorGet( "cpu-tasks" )

// Check availability
if ( executorHas( "custom-pool" ) ) {
    customPool = executorGet( "custom-pool" )
}

// Create custom executors
batchProcessor = executorNew( "batch-processor", "fixed", 4 )
scheduler = executorNew( "my-scheduler", "scheduled", 2 )

// Monitor all executors
allExecutors = executorList()
for ( name in allExecutors ) {
    status = executorStatus( name )
    println( "#name#: #status.activeCount# active threads" )
}
```

## ⏰ Scheduled Tasks: Use BoxLang Schedulers

> **🎯 Preferred Approach:** For scheduled tasks, use BoxLang's dedicated Scheduler framework instead of direct executor scheduling. Schedulers provide more features, better management, and integrated lifecycle handling.

### Scheduler vs Direct Executor Scheduling

```js
// ❌ Direct executor scheduling (basic)
executor = executorGet( "scheduled-tasks" );
executor.schedule( task, 5, "seconds" );

// ✅ BoxLang Scheduler (recommended)
scheduler = schedulerNew( "MyScheduler" );
scheduler.task( "cleanup" )
    .call( () => cleanupTempFiles() )
    .every( 1, "hours" )
    .start();
```

**Benefits of BoxLang Schedulers:**

* **Rich Configuration:** Timezone support, complex scheduling patterns
* **Lifecycle Management:** Automatic startup/shutdown handling
* **Error Handling:** Built-in retry logic and error recovery
* **Monitoring:** Enhanced logging and statistics
* **Persistence:** Optional task persistence across restarts

## 📚 Practical Examples

### 🚀 Basic Usage

```js
// Get the default I/O executor that leverages virtual threads
virtualExecutor = executorGet()

// Create a custom executor for CPU tasks (returns BoxExecutor)
cpuExecutor = executorNew( "heavy-cpu", "fixed", 4 )

// Check executor status using BoxExecutor methods
if ( executorHas( "heavy-cpu" ) ) {
    stats = cpuExecutor.getStats()
    println( "Active threads: #stats.activeCount#" )
    println( "Pool size: #stats.poolSize#" )
    println( "Completed tasks: #stats.completedTaskCount#" )

    // Check health (new in 1.6.0)
    if ( cpuExecutor.isHealthy() ) {
        println( "Executor is healthy" )
    } else {
        println( "Health Status: #stats.healthStatus#" )
        println( "Health Report: #stats.healthReport.summary#" )
    }
}

// List all available executors
allExecutors = executorList()
writeDump( allExecutors )

// Always shutdown custom executors when done
cpuExecutor.shutdownAndAwaitTermination( 30, "seconds" )

// Submit a simple task to the default executor
// This returns a Java Future object
future = virtualExecutor.submit( () => {
    writeLog( text: "Starting async task", type: "Information", log: "async" )
    sleep( 2000 ) // Simulate work
    writeLog( text: "Async task completed", type: "Information", log: "async" )
    return "Task Result"
} )

// Submit a simple task and wait for the result
result = virtualExecutor.submitAndGet( () => {
    writeLog( text: "Starting async task", type: "Information", log: "async" )
    sleep( 2000 ) // Simulate work
    writeLog( text: "Async task completed", type: "Information", log: "async" )
    return "Task Result"
} )
```

### ⚡ Asynchronous Task Execution with Error Handling

```js
// Submit async tasks to different executors
ioExecutor = executorGet( "io-tasks" )
cpuExecutor = executorGet( "cpu-tasks" )

try {
    // I/O bound task (database query)
    dbFuture = ioExecutor.submit( () => {
        writeLog( text: "Starting database query", type: "Information", log: "async" )
        result = queryExecute( "SELECT * FROM users WHERE active = ?", [ true ] )
        writeLog( text: "Database query completed: #result.recordCount# records", type: "Information", log: "async" )
        return result
    } )

    // CPU bound task (heavy computation)
    mathFuture = cpuExecutor.submit( () => {
        writeLog( text: "Starting prime calculation", type: "Information", log: "async" )
        primes = calculatePrimes( 1000000 )
        writeLog( text: "Prime calculation completed: #arrayLen( primes )# primes found", type: "Information", log: "async" )
        return primes
    } )

    // Wait for results with timeout
    users = dbFuture.get( 5000 ) // 5 second timeout
    primes = mathFuture.get()

    println( "Found #users.recordCount# users and #arrayLen( primes )# primes" )

} catch ( any e ) {
    writeLog( text: "Task execution failed: #e.message#", type: "Error", log: "async" )
    rethrow
}

// Monitor executor performance
ioStats = ioExecutor.getStats()
cpuStats = cpuExecutor.getStats()

println( "I/O Executor - Active: #ioStats.activeCount#, Completed: #ioStats.completedTaskCount#" )
println( "CPU Executor - Active: #cpuStats.activeCount#, Pool Size: #cpuStats.poolSize#" )
```

### ⏰ Advanced Scheduled Task Management

```js
// Get the scheduled executor
scheduler = executorGet( "scheduled-tasks" )

// Create a named task for better tracking
cleanupTask = scheduler.newTask( "temp-file-cleanup" )

// Configure the task but don't start it yet
cleanupTask.call( () => {
    writeLog( text: "Starting temp file cleanup", type: "Information", log: "async" )

    filesDeleted = cleanupTempFiles()

    writeLog( text: "Cleanup completed: #filesDeleted# files deleted", type: "Information", log: "async" )
    return filesDeleted
} )

// Start the task to run every hour
cleanupTask.every( 1, "hours" ).start()

// Schedule a one-time delayed task
healthCheckTask = scheduler.newTask( "health-check" )
healthCheckTask.call( () => {
    status = performHealthCheck()
    writeLog( text: "Health check completed: #status#", type: "Information", log: "async" )
    return status
} )

// Run once after 30 seconds
healthCheckTask.in( 30, "seconds" ).start()

// Monitor scheduled tasks
stats = scheduler.getStats()
println( "Scheduled tasks - Active: #stats.activeCount#, Queue size: #stats.taskCount#" )
```

### 🔄 Parallel Processing with Work Stealing

```js
// Create a work-stealing executor for parallel processing
parallelExecutor = executorNew( "parallel-processor", "work_stealing", 8 )

try {
    largeDataset = generateLargeDataset( 10000 ) // 10,000 items
    chunkSize = 100
    futures = []

    writeLog( text: "Starting parallel processing of #arrayLen( largeDataset )# items", type: "Information", log: "async" )

    // Split work across multiple threads
    for ( i = 1 i <= arrayLen( largeDataset ) i += chunkSize ) {
        chunk = arraySlice( largeDataset, i, min( i + chunkSize - 1, arrayLen( largeDataset ) ) )

        futures.append( parallelExecutor.submit( () => {
            processedChunk = processDataChunk( chunk )
            writeLog( text: "Processed chunk of #arrayLen( chunk )# items", type: "Debug", log: "async" )
            return processedChunk
        } ) )
    }

    // Collect all results
    results = []
    for ( future in futures ) {
        try {
            results.append( future.get( 60000 ) ) // 60 second timeout per chunk
        } catch ( any e ) {
            writeLog( text: "Chunk processing failed: #e.message#", type: "Error", log: "async" )
        }
    }

    writeLog( text: "Parallel processing completed: #arrayLen( results )# chunks processed", type: "Information", log: "async" )

    // Monitor work stealing performance
    stats = parallelExecutor.getStats()
    if ( stats.keyExists( "stealCount" ) ) {
        println( "Work stealing efficiency: #stats.stealCount# steals performed" )
    }

} catch ( any e ) {
    writeLog( text: "Parallel processing failed: #e.message#", type: "Error", log: "async" )
    rethrow
} finally {
    // CRITICAL: Always shutdown custom executors
    // Remember: Once shutdown, the executor cannot be restarted!
    parallelExecutor.shutdownAndAwaitTermination( 30, "seconds" )
    writeLog( text: "Parallel processor shutdown completed", type: "Information", log: "async" )
}
```

### 🔄 Batch Processing with Virtual Threads

```js
// Use virtual threads for I/O-intensive batch processing
batchProcessor = executorNew( "batch-io-processor", "virtual" )

try {
    apiEndpoints = [
        "https://api1.example.com/data",
        "https://api2.example.com/data",
        "https://api3.example.com/data"
        // ... hundreds more endpoints
    ]

    writeLog( text: "Starting batch I/O processing with virtual threads", log: "async" )

    futures = []

    // Submit hundreds/thousands of I/O tasks - virtual threads handle it easily
    for ( endpoint in apiEndpoints ) {
        futures.append( batchProcessor.submit( () => {
            try {
                result = httpGet( endpoint )
                writeLog( text: "API call completed: #endpoint#", type: "Debug", log: "async" )
                return result
            } catch ( any e ) {
                writeLog( text: "API call failed for #endpoint#: #e.message#", type: "Warning", log: "async" )
                return { error: e.message, endpoint: endpoint }
            }
        } ) )
    }

    // Process results as they complete
    successCount = 0
    errorCount = 0

    for ( future in futures ) {
        result = future.get( 30000 ) // 30 second timeout per API call
        if ( result.keyExists( "error" ) ) {
            errorCount++
        } else {
            successCount++
        }
    }

    writeLog( text: "Batch processing completed - Success: #successCount#, Errors: #errorCount#", type: "Information", log: "async" )

} finally {
    // Virtual thread executors shutdown quickly
    batchProcessor.shutdownAndAwaitTermination( 10, "seconds" )
}
```

## ⚡ Performance Considerations & Best Practices

### **🚨 Critical Guidelines:**

* **Virtual Threads:** Perfect for I/O, avoid for CPU-intensive tasks
* **Fixed Pools:** Size according to available CPU cores for CPU tasks
* **Cached Pools:** Monitor thread creation, can grow unbounded
* **Always Shutdown:** Clean up custom executors to prevent resource leaks
* **Monitor Stats:** Use `getStats()` to track executor performance
* **Log Everything:** Use async logging for troubleshooting and monitoring
* **Use BoxFutures** it is tempting to use the Java Future, but BoxFutures provide better integration with BoxLang's async model and error handling.
* **Use BoxLang Schedulers:** For scheduled tasks, prefer BoxLang's Scheduler framework for better management and features.

### 🎯 Executor Selection Matrix

| Task Characteristics          | Recommended Executor | Thread Count | Memory Usage           | Best Performance          |
| ----------------------------- | -------------------- | ------------ | ---------------------- | ------------------------- |
| **Database Queries**          | VIRTUAL (io-tasks)   | Unlimited    | Very Low (\~KB/thread) | Excellent for I/O         |
| **File Operations**           | VIRTUAL (io-tasks)   | Unlimited    | Very Low               | Scales to thousands       |
| **HTTP API Calls**            | VIRTUAL (io-tasks)   | Unlimited    | Very Low               | Perfect for microservices |
| **Mathematical Calculations** | FIXED (cpu-tasks)    | = CPU cores  | Medium                 | Optimal CPU usage         |
| **Image/Video Processing**    | FIXED                | = CPU cores  | High                   | Prevents oversubscription |
| **Data Transformations**      | WORK\_STEALING       | = CPU cores  | Medium                 | Load balancing            |
| **Parallel Algorithms**       | FORK\_JOIN           | = CPU cores  | Medium                 | Divide-and-conquer        |
| **Periodic Maintenance**      | SCHEDULED            | Small (2-5)  | Low                    | Time-based execution      |
| **Background Tasks**          | CACHED               | Dynamic      | Variable               | Burst workloads           |
| **Sequential Processing**     | SINGLE               | 1            | Low                    | Order guarantee           |

### 📊 Performance Monitoring

```js
// Regular performance monitoring with health checks
function monitorExecutorPerformance() {
    var allStats = executorStatus() // Gets all executor stats

    for ( var executorName in allStats ) {
        var executor = executorGet( executorName )
        var stats = executor.getStats()

        // Quick health check (new in 1.6.0)
        if ( !executor.isHealthy() ) {
            writeLog(
                text: "UNHEALTHY: #executorName# - Status: #stats.healthStatus#",
                type: "Warning",
                log: "async"
            )

            // Log health report issues
            var healthReport = stats.healthReport
            if ( arrayLen( healthReport.issues ) > 0 ) {
                writeLog(
                    text: "Issues for #executorName#: #arrayToList( healthReport.issues )#",
                    type: "Warning",
                    log: "async"
                )
            }
        }

        // Check for performance issues
        if ( stats.poolUtilization > 80 ) {
            writeLog(
                text: "High pool utilization in #executorName#: #stats.poolUtilization#%",
                type: "Warning",
                log: "async"
            )
        }

        // Check queue health
        if ( stats.queueUtilization > 70 ) {
            writeLog(
                text: "Queue filling in #executorName#: #stats.queueSize# tasks (#stats.queueUtilization#% full)",
                type: "Warning",
                log: "async"
            )
        }

        // Monitor task completion rate
        if ( stats.keyExists( "taskCompletionRate" ) && stats.taskCount > 10 ) {
            if ( stats.taskCompletionRate < 70 ) {
                writeLog(
                    text: "Low completion rate in #executorName#: #stats.taskCompletionRate#%",
                    type: "Warning",
                    log: "async"
                )
            }
        }

        // Monitor activity
        if ( stats.lastActivityMinutesAgo > 30 && stats.activeCount == 0 ) {
            writeLog(
                text: "Executor #executorName# has been idle for #stats.lastActivityMinutesAgo# minutes",
                type: "Information",
                log: "async"
            )
        }

        // Log healthy status periodically
        if ( executor.isHealthy() ) {
            writeLog(
                text: "Executor #executorName#: Healthy - Active: #stats.activeCount#, Completed: #stats.completedTaskCount#, Queue: #stats.queueSize#",
                type: "Debug",
                log: "async"
            )
        }
    }
}

// Schedule monitoring to run every 5 minutes
monitoringTask = executorGet( "scheduled-tasks" ).newTask( "performance-monitor" )
monitoringTask
    .call( monitorExecutorPerformance )
    .every( 5, "minutes" )
    .start()
```

### 🛡️ Error Handling & Recovery

```js
// Robust error handling pattern
function executeWithRetry( task, maxRetries = 3, executorName = "io-tasks" ) {
    executor = executorGet( executorName )
    attempt = 0

    while ( attempt < maxRetries ) {
        try {
            attempt++

            future = executor.submit( task )
            result = future.get( 30000 ) // 30 second timeout

            writeLog( text: "Task completed successfully on attempt #attempt#", type: "Information", log: "async" )
            return result

        } catch ( any e ) {
            writeLog( text: "Task failed on attempt #attempt#: #e.message#", type: "Warning", log: "async" );

            if ( attempt >= maxRetries ) {
                writeLog( text: "Task failed after #maxRetries# attempts", type: "Error", log: "async" );
                rethrow;
            }

            // Exponential backoff
            sleep( attempt * 1000 );
        }
    }
}

// Usage
result = executeWithRetry( () => {
    return riskyDatabaseOperation();
} );
```

## 🔥 Production Best Practices

* **Use Built-in Executors:** Start with `io-tasks` and `cpu-tasks` for most scenarios
* **Create Custom Sparingly:** Only create custom executors for specific performance requirements
* **Monitor Continuously:** Implement regular stats monitoring and alerting
* **Plan Shutdown Strategy:** Always implement graceful shutdown with fallback to forceful
* **Log Comprehensively:** Use async logging for all important operations
* **Test Under Load:** Validate executor behavior under realistic workloads
* **Size Appropriately:** Match thread counts to actual hardware capabilities

## 🎉 Quick Start Template

```js
// 1. Simple async task with error handling
try {
    future = executorGet().submit( () => {
        writeLog( text: "Starting expensive operation", type: "Information", log: "async" );
        return expensiveOperation();
    } );

    // 2. Do other work while task runs
    doOtherWork();

    // 3. Get result when ready with timeout
    result = future.get( 10000 ); // 10 second timeout

    // 4. Handle the result
    if ( !isNull( result ) ) {
        processResult( result );
        writeLog( text: "Operation completed successfully", type: "Information", log: "async" );
    }

} catch ( any e ) {
    writeLog( text: "Async operation failed: #e.message#", type: "Error", log: "async" );
    // Handle error appropriately
}
```

This template covers 80% of use cases - simple, effective, and leverages BoxLang's optimized defaults with proper error handling and logging!  Please note that if you need fluent pipelines or enhanced computation capabilities, consider using BoxLang's `BoxFutures` for better integration with the async model and leveraging the full power of CompletableFuture.
