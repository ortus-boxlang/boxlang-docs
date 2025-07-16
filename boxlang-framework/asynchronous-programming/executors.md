---
description: Powerful Concurrency Made Simple
icon: chart-network
---

# Executors

## 🚀 What Are Executors?

Executors in Java (and BoxLang) are high-level abstractions for managing and controlling thread execution. They provide a powerful way to handle concurrent tasks without the complexity of manually managing threads. Think of executors as specialized worker pools that can handle different types of workloads efficiently.

```bash
Tasks Queue  →  Executor Pool  →  Results
📋 📋 📋      🔄 🔄 🔄 🔄       ✅ ✅ ✅
```

Here is a great video you can check out about Executors: https://www.youtube.com/watch?v=6Oo-9Can3H8&t=2s

### **💡 Why Use Executors?**

* **Thread Management:** Automatic creation, pooling, and lifecycle management
* **Resource Control:** Limit concurrent threads to prevent system overload
* **Task Queuing:** Handle more tasks than available threads
* **Graceful Shutdown:** Clean termination of running tasks
* **Statistical Monitoring:** Real-time insights into executor performance
* **Error Handling:** Centralized exception management and logging

## 🎯 Executor Types & Use Cases

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

## 🎁 Pre-defined Runtime Executors

BoxLang ships with three carefully curated executors ready for immediate use.  They are defined in the BoxLang's Home `config` folder `boxlang.json.`  Check out the [configuration](../../getting-started/configuration/executors.md) section for more information.

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

BoxLang provides dedicated logging for all asynchronous operations through the `async.log` file located in the `logs` folder of your BoxLang home directory.  Please leverage logging as much as possible, as in async logging is critical for debugging and monitoring executor behavior.

### 🎯 Automatic Logging

All executor operations are automatically logged:

* Executor creation and configuration
* Task submissions and completions
* Shutdown events and timing
* Error conditions and exceptions
* Performance warnings

### 📊 Manual Logging

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

| Method                                           | Purpose                                         | Returns        |
| ------------------------------------------------ | ----------------------------------------------- | -------------- |
| `newExecutor( name, type, threads )`             | Create new executors with custom configurations | ExecutorRecord |
| `getExecutor( name )`                                         | Retrieve executor instances by name             | ExecutorRecord |
| `hasExecutor( name )`                                         | Check if an executor exists                               | Boolean        |
| `deleteExecutor( name )`                                       | Remove and shutdown executors                   | AsyncService   |
| `shutdownExecutor( name, force, timeout, unit )` | Gracefully shutdown specific executors          | AsyncService   |
| `shutdownAllExecutors( force, timeout, unit )`   | Shutdown all registered executors               | AsyncService   |
| `getExecutorStatusMap()`                                  | Get detailed statistics for all executors       | IStruct        |
| `getExecutorStatusMap( name )`                    | Get statistics for specific executor            | IStruct        |
| `getExecutorNames()`                                       | List all registered executor names              | List           |

### 🎯 Convenience Builder Methods

```boxlang
asyncService = getBoxRuntime().getAsyncService()

// Quick executor creation - all return ExecutorRecord
 cacheExecutor = asyncService.newCachedExecutor( "my-cache" )
 workerPool = asyncService.newFixedExecutor( "workers", 10 )
 ioPool = asyncService.newVirtualExecutor( "io-pool" )
 scheduler = asyncService.newScheduledExecutor( "scheduler", 5 )
 parallelPool = asyncService.newWorkStealingExecutor( "parallel-work", 8 )
 forkJoinPool = asyncService.newForkJoinExecutor( "fork-join", 4 )
 singleThread = asyncService.newSingleExecutor( "sequential" )
```

All methods return an `ExecutorRecord` instance, which provides enhanced functionality beyond standard Java ExecutorService.  Our BoxLang ExecutorRecord is a wrapper around the Java ExecutorService, providing additional features like statistics, logging, and task management.

## 🏗️ ExecutorRecord: Enhanced Executor Management

**Important:** BoxLang doesn't return raw Java executors. Instead, you get `ExecutorRecord` instances - enhanced wrappers that provide additional functionality beyond standard Java ExecutorService.

### 🔍 What is ExecutorRecord?

`ExecutorRecord` is BoxLang's enhanced executor wrapper that provides:

* **📊 Real-time Statistics:** Active threads, completed tasks, pool size metrics
* **🔧 Enhanced Control:** Graceful and forceful shutdown capabilities
* **📝 Integrated Logging:** Automatic logging to `async.log`
* **⚡ Convenience Methods:** Simplified task submission and result handling
* **🎯 Task Factory:** Built-in ScheduledTask creation for complex workflows
* **🔄 State Management:** Comprehensive executor state monitoring

### Getters

The `ExecutorRecord` provides several getters to access executor properties:

* `exectuor()` - Returns the underlying Java ExecutorService instance
* `name()` - Returns the executor's name
* `type()` - Returns the executor type (e.g., "fixed", "virtual")
* `maxThreads()` - Returns the maximum number of threads (if applicable)

The rest of the methods are similar to the Java ExecutorService, but with added BoxLang features.

### 📊 ExecutorRecord Statistics

Every ExecutorRecord provides detailed runtime statistics:

```boxlang
executor = executorGet( "cpu-tasks" )
stats = executor.getStats()

// Available statistics (varies by executor type)
println( "Active Threads: #stats.activeCount#" )
println( "Completed Tasks: #stats.completedTaskCount#" )
println( "Pool Size: #stats.poolSize#" )
println( "Maximum Pool Size: #stats.maximumPoolSize#" )
println( "Is Shutdown: #stats.isShutdown#" )
println( "Is Terminated: #stats.isTerminated#" )

// Fork/Join specific stats
if ( stats.keyExists( "stealCount" ) ) {
    println( "Work Steal Count: #stats.stealCount#" )
    println( "Queued Tasks: #stats.queuedTaskCount#" )
}
```

### 🎯 Task Creation Factory

`ExecutorRecord` includes a built-in task factory as well for complex scheduling.  These methods will give you back a BoxLang `ScheduledTask` instance, which you can configure and start manually or attach it to a BoxLang `Scheduler`.

```boxlang
var executor = executorGet( "scheduled-tasks" );

// Create a named task (not yet executing)
var cleanupTask = executor.newTask( "daily-cleanup" );

// Create an auto-named task
var monitoringTask = executor.newTask();

// Configure and start the task
cleanupTask
    .call( () => {
        cleanupTempFiles();
        return "Cleanup completed";
    } )
    .every( 1, "days" )
    .start();
```

### 🛡️ Enhanced Shutdown Management

```boxlang
var executor = executorGet( "my-custom-executor" );

// Graceful shutdown with timeout
executor.shutdownAndAwaitTermination( 30, "seconds" );

// Quick non-blocking shutdown
executor.shutdownQuiet();

// Check shutdown status
var stats = executor.getStats();
if ( stats.isShutdown ) {
    writeOutput( "Executor is shutdown" );
}
```

> **⚠️ CRITICAL WARNING:** Once an executor is shutdown, it **CANNOT** be restarted! The executor becomes permanently dead. Always plan your shutdown strategy carefully and prefer graceful shutdown with `shutdownAndAwaitTermination()` when possible.

## 🌟 Global BIFs (Built-in Functions)

BoxLang provides convenient global functions for executor management and usage:

| Function                                       | Purpose                                             | Returns        | Example                                 |
| ---------------------------------------------- | --------------------------------------------------- | -------------- | --------------------------------------- |
| `executorGet( [name] )`                        | Get ExecutorRecord by name (defaults to "io-tasks") | ExecutorRecord | `executorGet( "cpu-tasks" )`            |
| `executorHas( name )`                          | Check if executor exists                            | Boolean        | `executorHas( "my-pool" )`              |
| `executorList()`                                      | List all executor names                             | Array          | `executorList()`                        |
| `executorNew( name, type, [threads] )`         | Create new executor                                 | ExecutorRecord | `executorNew( "pool", "fixed", 8 )`     |
| `executorShutdown( name, [force], [timeout] )` | Shutdown executor gracefully or forcefully          | Boolean        | `executorShutdown( "pool", false, 30 )` |
| `executorStatus( [name] )`                     | Get executor statistics and status                  | Struct         | `executorStatus( "cpu-tasks" )`         |

Remember that if the BIF returns an executor, it will be an `ExecutorRecord` instance, not a raw Java ExecutorService.  This allows you to leverage all the enhanced features and methods provided by BoxLang.

### 🎯 BIF Usage Examples

```boxlang
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

### 🔧 Scheduler vs Direct Executor Scheduling

```boxlang
// ❌ Direct executor scheduling (basic)
var executor = executorGet( "scheduled-tasks" );
executor.schedule( task, 5, "seconds" );

// ✅ BoxLang Scheduler (recommended)
var scheduler = new Scheduler( "MyScheduler" );
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

### 🚀 Basic ExecutorRecord Usage

```boxlang
// Get the default I/O executor (returns ExecutorRecord)
var ioExecutor = executorGet();

// Create a custom executor for CPU tasks (returns ExecutorRecord)
var cpuExecutor = executorNew( "heavy-cpu", "fixed", 4 );

// Check executor status using ExecutorRecord methods
if ( executorHas( "heavy-cpu" ) ) {
    var stats = cpuExecutor.getStats();
    writeOutput( "Active threads: #stats.activeCount#" );
    writeOutput( "Pool size: #stats.poolSize#" );
    writeOutput( "Completed tasks: #stats.completedTaskCount#" );
}

// List all available executors
var allExecutors = executorList();
writeDump( allExecutors );

// Always shutdown custom executors when done
cpuExecutor.shutdownAndAwaitTermination( 30, "seconds" );
```

### ⚡ Asynchronous Task Execution with Error Handling

```boxlang
// Submit async tasks to different executors
var ioExecutor = executorGet( "io-tasks" );
var cpuExecutor = executorGet( "cpu-tasks" );

try {
    // I/O bound task (database query)
    var dbFuture = ioExecutor.submit( () => {
        log( text: "Starting database query", type: "Information", log: "async" );
        var result = queryExecute( "SELECT * FROM users WHERE active = ?", [ true ] );
        log( text: "Database query completed: #result.recordCount# records", type: "Information", log: "async" );
        return result;
    } );

    // CPU bound task (heavy computation)
    var mathFuture = cpuExecutor.submit( () => {
        log( text: "Starting prime calculation", type: "Information", log: "async" );
        var primes = calculatePrimes( 1000000 );
        log( text: "Prime calculation completed: #arrayLen( primes )# primes found", type: "Information", log: "async" );
        return primes;
    } );

    // Wait for results with timeout
    var users = dbFuture.get( 5000 ); // 5 second timeout
    var primes = mathFuture.get();

    writeOutput( "Found #users.recordCount# users and #arrayLen( primes )# primes" );

} catch ( any e ) {
    log( text: "Task execution failed: #e.message#", type: "Error", log: "async" );
    rethrow;
}

// Monitor executor performance
var ioStats = ioExecutor.getStats();
var cpuStats = cpuExecutor.getStats();

writeOutput( "I/O Executor - Active: #ioStats.activeCount#, Completed: #ioStats.completedTaskCount#" );
writeOutput( "CPU Executor - Active: #cpuStats.activeCount#, Pool Size: #cpuStats.poolSize#" );
```

### ⏰ Advanced Scheduled Task Management

```boxlang
// Get the scheduled executor
var scheduler = executorGet( "scheduled-tasks" );

// Create a named task for better tracking
var cleanupTask = scheduler.newTask( "temp-file-cleanup" );

// Configure the task but don't start it yet
cleanupTask.call( () => {
    log( text: "Starting temp file cleanup", type: "Information", log: "async" );

    var filesDeleted = cleanupTempFiles();

    log( text: "Cleanup completed: #filesDeleted# files deleted", type: "Information", log: "async" );
    return filesDeleted;
} );

// Start the task to run every hour
cleanupTask.every( 1, "hours" ).start();

// Schedule a one-time delayed task
var healthCheckTask = scheduler.newTask( "health-check" );
healthCheckTask.call( () => {
    var status = performHealthCheck();
    log( text: "Health check completed: #status#", type: "Information", log: "async" );
    return status;
} );

// Run once after 30 seconds
healthCheckTask.in( 30, "seconds" ).start();

// Monitor scheduled tasks
var stats = scheduler.getStats();
writeOutput( "Scheduled tasks - Active: #stats.activeCount#, Queue size: #stats.taskCount#" );
```

### 🔄 Parallel Processing with Work Stealing

```boxlang
// Create a work-stealing executor for parallel processing
var parallelExecutor = executorNew( "parallel-processor", "work_stealing", 8 );

try {
    var largeDataset = generateLargeDataset( 10000 ); // 10,000 items
    var chunkSize = 100;
    var futures = [];

    log( text: "Starting parallel processing of #arrayLen( largeDataset )# items", type: "Information", log: "async" );

    // Split work across multiple threads
    for ( var i = 1; i <= arrayLen( largeDataset ); i += chunkSize ) {
        var chunk = arraySlice( largeDataset, i, min( i + chunkSize - 1, arrayLen( largeDataset ) ) );

        futures.append( parallelExecutor.submit( () => {
            var processedChunk = processDataChunk( chunk );
            log( text: "Processed chunk of #arrayLen( chunk )# items", type: "Debug", log: "async" );
            return processedChunk;
        } ) );
    }

    // Collect all results
    var results = [];
    for ( var future in futures ) {
        try {
            results.append( future.get( 60000 ) ); // 60 second timeout per chunk
        } catch ( any e ) {
            log( text: "Chunk processing failed: #e.message#", type: "Error", log: "async" );
        }
    }

    log( text: "Parallel processing completed: #arrayLen( results )# chunks processed", type: "Information", log: "async" );

    // Monitor work stealing performance
    var stats = parallelExecutor.getStats();
    if ( stats.keyExists( "stealCount" ) ) {
        writeOutput( "Work stealing efficiency: #stats.stealCount# steals performed" );
    }

} catch ( any e ) {
    log( text: "Parallel processing failed: #e.message#", type: "Error", log: "async" );
    rethrow;
} finally {
    // CRITICAL: Always shutdown custom executors
    // Remember: Once shutdown, the executor cannot be restarted!
    parallelExecutor.shutdownAndAwaitTermination( 30, "seconds" );
    log( text: "Parallel processor shutdown completed", type: "Information", log: "async" );
}
```

### 🔄 Batch Processing with Virtual Threads

```boxlang
// Use virtual threads for I/O-intensive batch processing
var batchProcessor = executorNew( "batch-io-processor", "virtual" );

try {
    var apiEndpoints = [
        "https://api1.example.com/data",
        "https://api2.example.com/data",
        "https://api3.example.com/data"
        // ... hundreds more endpoints
    ];

    log( text: "Starting batch I/O processing with virtual threads", type: "Information", log: "async" );

    var futures = [];

    // Submit hundreds/thousands of I/O tasks - virtual threads handle it easily
    for ( var endpoint in apiEndpoints ) {
        futures.append( batchProcessor.submit( () => {
            try {
                var result = httpGet( endpoint );
                log( text: "API call completed: #endpoint#", type: "Debug", log: "async" );
                return result;
            } catch ( any e ) {
                log( text: "API call failed for #endpoint#: #e.message#", type: "Warning", log: "async" );
                return { error: e.message, endpoint: endpoint };
            }
        } ) );
    }

    // Process results as they complete
    var successCount = 0;
    var errorCount = 0;

    for ( var future in futures ) {
        var result = future.get( 30000 ); // 30 second timeout per API call
        if ( result.keyExists( "error" ) ) {
            errorCount++;
        } else {
            successCount++;
        }
    }

    log( text: "Batch processing completed - Success: #successCount#, Errors: #errorCount#", type: "Information", log: "async" );

} finally {
    // Virtual thread executors shutdown quickly
    batchProcessor.shutdownAndAwaitTermination( 10, "seconds" );
}
```

## ⚡ Performance Considerations & Best Practices

> **🚨 Critical Guidelines:**
>
> * **Virtual Threads:** Perfect for I/O, avoid for CPU-intensive tasks
> * **Fixed Pools:** Size according to available CPU cores for CPU tasks
> * **Cached Pools:** Monitor thread creation, can grow unbounded
> * **Always Shutdown:** Clean up custom executors to prevent resource leaks
> * **Monitor Stats:** Use `getStats()` to track executor performance
> * **Log Everything:** Use async logging for troubleshooting and monitoring

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

```boxlang
// Regular performance monitoring
function monitorExecutorPerformance() {
    var allStats = executorStatus(); // Gets all executor stats

    for ( var executorName in allStats ) {
        var stats = allStats[ executorName ];

        // Check for performance issues
        if ( stats.activeCount > stats.maximumPoolSize * 0.8 ) {
            log(
                text: "High thread utilization in #executorName#: #stats.activeCount#/#stats.maximumPoolSize#",
                type: "Warning",
                log: "async"
            );
        }

        // Monitor task completion rate
        if ( stats.keyExists( "completedTaskCount" ) && stats.completedTaskCount > 0 ) {
            var efficiency = stats.completedTaskCount / stats.taskCount;
            if ( efficiency < 0.7 ) {
                log(
                    text: "Low task completion efficiency in #executorName#: #efficiency * 100#%",
                    type: "Warning",
                    log: "async"
                );
            }
        }
    }
}

// Schedule monitoring to run every 5 minutes
var monitoringTask = executorGet( "scheduled-tasks" ).newTask( "performance-monitor" );
monitoringTask
    .call( monitorExecutorPerformance )
    .every( 5, "minutes" )
    .start();
```

### 🛡️ Error Handling & Recovery

```boxlang
// Robust error handling pattern
function executeWithRetry( task, maxRetries = 3, executorName = "io-tasks" ) {
    var executor = executorGet( executorName );
    var attempt = 0;

    while ( attempt < maxRetries ) {
        try {
            attempt++;

            var future = executor.submit( task );
            var result = future.get( 30000 ); // 30 second timeout

            log( text: "Task completed successfully on attempt #attempt#", type: "Information", log: "async" );
            return result;

        } catch ( any e ) {
            log( text: "Task failed on attempt #attempt#: #e.message#", type: "Warning", log: "async" );

            if ( attempt >= maxRetries ) {
                log( text: "Task failed after #maxRetries# attempts", type: "Error", log: "async" );
                rethrow;
            }

            // Exponential backoff
            sleep( attempt * 1000 );
        }
    }
}

// Usage
var result = executeWithRetry( () => {
    return riskyDatabaseOperation();
} );
```

### 🎯 Resource Management Best Practices

```boxlang
// Application shutdown hook - cleanup all custom executors
function applicationShutdown() {
    log( text: "Starting application shutdown", type: "Information", log: "async" );

    var customExecutors = [ "batch-processor", "parallel-work", "custom-scheduler" ];

    for ( var executorName in customExecutors ) {
        if ( executorHas( executorName ) ) {
            log( text: "Shutting down executor: #executorName#", type: "Information", log: "async" );

            try {
                // Attempt graceful shutdown first
                var success = executorShutdown( executorName, false, 30 );

                if ( !success ) {
                    log( text: "Graceful shutdown failed for #executorName#, forcing shutdown", type: "Warning", log: "async" );
                    executorShutdown( executorName, true, 5 );
                }

            } catch ( any e ) {
                log( text: "Failed to shutdown executor #executorName#: #e.message#", type: "Error", log: "async" );
            }
        }
    }

    log( text: "Application shutdown completed", type: "Information", log: "async" );
}
```

> **🔥 Production Best Practices:**
>
> * **Use Built-in Executors:** Start with `io-tasks` and `cpu-tasks` for most scenarios
> * **Create Custom Sparingly:** Only create custom executors for specific performance requirements
> * **Monitor Continuously:** Implement regular stats monitoring and alerting
> * **Plan Shutdown Strategy:** Always implement graceful shutdown with fallback to forceful
> * **Log Comprehensively:** Use async logging for all important operations
> * **Test Under Load:** Validate executor behavior under realistic workloads
> * **Size Appropriately:** Match thread counts to actual hardware capabilities

## 🎉 Quick Start Template

```boxlang
// 1. Simple async task with error handling
try {
    var future = executorGet().submit( () => {
        log( text: "Starting expensive operation", type: "Information", log: "async" );
        return expensiveOperation();
    } );

    // 2. Do other work while task runs
    doOtherWork();

    // 3. Get result when ready with timeout
    var result = future.get( 10000 ); // 10 second timeout

    // 4. Handle the result
    if ( !isNull( result ) ) {
        processResult( result );
        log( text: "Operation completed successfully", type: "Information", log: "async" );
    }

} catch ( any e ) {
    log( text: "Async operation failed: #e.message#", type: "Error", log: "async" );
    // Handle error appropriately
}
```

This template covers 80% of use cases - simple, effective, and leverages BoxLang's optimized defaults with proper error handling and logging!

## 🔧 Advanced ExecutorRecord Methods

### 📊 Statistical Analysis

```boxlang
var executor = executorGet( "cpu-tasks" );
var stats = executor.getStats();

// Analyze executor health
var threadUtilization = stats.activeCount / stats.maximumPoolSize;
var taskThroughput = stats.completedTaskCount / stats.taskCount;

if ( threadUtilization > 0.9 ) {
    log( text: "Executor near capacity: #threadUtilization * 100#% utilization", type: "Warning", log: "async" );
}

// Create performance report
var report = {
    "executorName": stats.name,
    "type": stats.type,
    "threadUtilization": threadUtilization,
    "taskThroughput": taskThroughput,
    "isHealthy": threadUtilization < 0.8 && !stats.isTerminating
};
```

### 🎯 Convenient Submission Methods

```boxlang
var executor = executorGet( "io-tasks" );

// Submit and get result immediately (blocks until complete)
var result = executor.submitAndGet( () => {
    return databaseQuery();
} );

// Submit with automatic error handling
try {
    var data = executor.submitAndGet( () => {
        if ( Math.random() > 0.5 ) {
            throw new Exception( "Simulated failure" );
        }
        return "Success!";
    } );
} catch ( any e ) {
    log( text: "Submitted task failed: #e.message#", type: "Error", log: "async" );
}
```

***

🚀 **BoxLang Executors** - Making Java's powerful concurrency accessible, monitorable, and easy to use