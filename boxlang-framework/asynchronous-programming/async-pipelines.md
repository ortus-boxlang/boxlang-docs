---
description: Powerful Asynchronous Programming with BoxFuture Pipelines
icon: diagram-sankey
---

# 🚀 Async Pipelines and BoxFutures

## What Are Async Pipelines?

Async pipelines in BoxLang are powerful chains of asynchronous operations that allow you to compose complex workflows from simple, reusable components. Built on top of **BoxFuture** (which extends Java's `CompletableFuture`), they provide a fluent, functional programming approach to handling asynchronous operations.

```text
Input → Transform → Process → Combine → Result
  📥      ⚡️        🔄        🔗       ✅
```

Think of pipelines as assembly lines for data processing - each stage performs a specific operation and passes the result to the next stage, all running asynchronously for maximum performance.

### 💡 Why Use Async Pipelines?

* **🔄 Non-blocking:** Operations don't freeze your application
* **⚡ Performance:** Parallel execution and optimized resource usage
* **🧩 Composability:** Chain operations in a readable, maintainable way
* **🎯 Error Handling:** Centralized exception management and recovery
* **🔀 Flexibility:** Mix synchronous and asynchronous operations seamlessly
* **📊 Monitoring:** Built-in logging and performance tracking

## 🎯 Entry Points: Creating BoxFutures

BoxLang provides two main entry points for creating async pipelines:

### 🆕 `futureNew()` BIF

The primary way to create BoxFuture instances with maximum flexibility:

```js
// Create an empty future (to be completed later)
future = futureNew()

// Create a completed future with a value
future = futureNew( "Hello World" )

// Create a future from a function (executed asynchronously)
future = futureNew( () => {
    // Your async code here
    return performExpensiveOperation()
} )

// Create with a specific executor
future = futureNew(
    () => performCPUIntensiveTask(),
    "cpu-tasks"
)
```

### ⚡ `asyncRun()` BIF

Simplified function for running code asynchronously:

```js
// Run code asynchronously with default executor
future = asyncRun( () => {
    return fetchDataFromAPI()
} )

// Run with specific executor
future = asyncRun(
    () => processLargeFile(),
    "cpu-tasks"
)
```

## 🎨 BoxFuture Pipeline Methods

BoxFuture extends CompletableFuture with BoxLang-specific enhancements and fluent methods:

### 🔄 Transformation Methods

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `then( function )` | Transform result synchronously | `BoxFuture` | `future.then( x => x * 2 )` |
| `thenAsync( function )` | Transform result asynchronously | `BoxFuture` | `future.thenAsync( x => processAsync(x) )` |
| `then( function, executor )` | Transform with specific executor | `BoxFuture` | `future.then( x => x + 1, "cpu-tasks" )` |
| `thenAsync( function, executor )` | Transform async with executor | `BoxFuture` | `future.thenAsync( transform, "io-tasks" )` |

### 🚨 Error Handling Methods

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `onError( function )` | Handle exceptions | `BoxFuture` | `future.onError( ex => handleError(ex) )` |
| `exceptionally( function )` | Handle exceptions (Java style) | `BoxFuture` | `future.exceptionally( ex => defaultValue )` |

### ⏰ Timeout Methods

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `orTimeout( timeout )` | Timeout in milliseconds | `BoxFuture` | `future.orTimeout( 5000 )` |
| `orTimeout( timeout, unit )` | Timeout with time unit | `BoxFuture` | `future.orTimeout( 5, "seconds" )` |
| `completeOnTimeout( value, timeout )` | Complete with value on timeout (ms) | `BoxFuture` | `future.completeOnTimeout( "default", 3000 )` |
| `completeOnTimeout( value, timeout, unit )` | Complete with value on timeout | `BoxFuture` | `future.completeOnTimeout( null, 1, "minute" )` |

### 📥 Result Retrieval Methods

| Method | Purpose | Returns | Usage |
|--------|---------|---------|-------|
| `get()` | Get result (blocking) | `Object` | `result = future.get()` |
| `get( timeout )` | Get result with timeout (ms) | `Object` | `result = future.get( 5000 )` |
| `get( timeout, unit )` | Get result with timeout | `Object` | `result = future.get( 30, "seconds" )` |
| `getOrDefault( defaultValue )` | Get result or default | `Object` | `result = future.getOrDefault( "fallback" )` |
| `join()` | Get result (blocking, unchecked) | `Object` | `result = future.join()` |
| `joinOrDefault( defaultValue )` | Join with default value | `Object` | `result = future.joinOrDefault( 0 )` |
| `getAsAttempt()` | Get result as Attempt object | `Attempt` | `attempt = future.getAsAttempt()` |
| `getAsAttempt( timeout )` | Get as Attempt with timeout (ms) | `Attempt` | `attempt = future.getAsAttempt( 5000 )` |
| `getAsAttempt( timeout, unit )` | Get as Attempt with timeout | `Attempt` | `attempt = future.getAsAttempt( 1, "minute" )` |

## 🌊 Pipeline Examples

### Basic Pipeline

```js
// Simple transformation pipeline
result = futureNew( () => fetchUser(123) )
    .then( user => user.name )
    .then( name => name.toUpperCase() )
    .onError( ex => "Unknown User" )
    .get()

println( "User: #result#" )
```

### Complex Data Processing Pipeline

```js
// Multi-stage data processing
pipeline = futureNew( () => {
    // Fetch data from multiple sources
    return [
        fetchFromDatabase(),
        fetchFromAPI(),
        fetchFromCache()
    ]
} )
.then( dataSources => {
    // Combine and normalize data
    return dataSources.reduce( (acc, source) => {
        return acc.append( source.data )
    }, [] )
} )
.thenAsync( data => {
    // Process asynchronously with CPU executor
    return processLargeDataset( data )
}, "cpu-tasks" )
.then( processedData => {
    // Format for output
    return {
        "results": processedData,
        "count": processedData.len(),
        "timestamp": now()
    }
} )
.onError( ex => {
    // Handle any errors in the pipeline
    writeLog( text: "Pipeline error: #ex.message#", log: "async" )
    return { "error": true, "message": ex.message }
} )

// Execute the pipeline
result = pipeline.get( 30, "seconds" )
```

### Parallel Processing with `all()`

```js
// Process multiple items in parallel
userIds = [ 1, 2, 3, 4, 5 ]

// Create futures for each user
userFutures = userIds.map( id => {
    return futureNew( () => fetchUserProfile( id ) )
} )

// Wait for all to complete
results = BoxFuture.all( userFutures )
    .then( profiles => {
        // Process all profiles together
        return profiles.filter( profile => profile.isActive )
    } )
    .get()

println( "Active users: #results.len()#" )
```

### Error Recovery Pipeline

```js
// Pipeline with fallback strategies
robustPipeline = futureNew( () => {
    // Try primary service
    return primaryService.getData()
} )
.onError( ex => {
    // Try secondary service
    writeLog( text: "Primary failed, trying secondary", log: "async" )
    return secondaryService.getData()
} )
.onError( ex => {
    // Try cache as last resort
    writeLog( text: "Secondary failed, using cache", log: "async" )
    return cache.get( "fallback-data" )
} )
.then( data => {
    // Process successfully retrieved data
    return processData( data )
} )
.orTimeout( 10, "seconds" )
.onError( ex => {
    // Ultimate fallback
    return { "error": true, "message": "All services unavailable" }
} )

result = robustPipeline.get()
```

## 🔗 Combining Futures

### Sequential Chaining

```js
// Each step depends on the previous
chain = futureNew( () => authenticateUser() )
    .then( token => fetchUserProfile( token ) )
    .then( profile => loadUserPreferences( profile.id ) )
    .then( preferences => customizeExperience( preferences ) )
    .get()
```

### Parallel Execution

```js
// Run multiple operations in parallel
parallel = BoxFuture.all(
    futureNew( () => loadUserData() ),
    futureNew( () => loadSystemConfig() ),
    futureNew( () => loadPermissions() )
)
.then( results => {
    userData = results[1]
    config = results[2]
    permissions = results[3]

    return initializeApplication( userData, config, permissions )
} )
.get()
```

## 🎯 Advanced Patterns

### 🔄 Retry Pattern

```js
function retryAsync( operation, maxRetries = 3 ) {
    return futureNew( () => {
        var attempt = 0
        while ( attempt < maxRetries ) {
            try {
                return operation()
            } catch ( e ) {
                attempt++
                if ( attempt >= maxRetries ) throw e
                sleep( 1000 * attempt ) // Exponential backoff
            }
        }
    } )
}

// Usage
result = retryAsync( () => unreliableService.call() )
    .orTimeout( 30, "seconds" )
    .onError( ex => "Service unavailable" )
    .get()
```

### 🔀 Fan-out/Fan-in Pattern

```js
// Fan-out: Split work across multiple processors
fanOut = futureNew( () => loadLargeDataset() )
    .then( data => {
        // Split data into chunks
        chunks = data.chunk( 100 )

        // Process each chunk in parallel
        return BoxFuture.all(
            chunks.map( chunk => {
                return futureNew( () => processChunk( chunk ), "cpu-tasks" )
            } )
        )
    } )

// Fan-in: Combine results
result = fanOut.then( processedChunks => {
    // Combine all processed chunks
    return processedChunks.reduce( (acc, chunk) => {
        return acc.append( chunk )
    }, [] )
} ).get()
```

### 🚪 Circuit Breaker Pattern

```js
component CircuitBreaker {
    property failures = 0
    property threshold = 5
    property isOpen = false
    property lastFailTime = 0
    property resetTimeout = 30000 // 30 seconds

    function call( operation ) {
        // Check if circuit should be closed
        if ( isOpen && (getTickCount() - lastFailTime) > resetTimeout ) {
            isOpen = false
            failures = 0
        }

        if ( isOpen ) {
            return futureNew( () => {
                throw( "Circuit breaker is open" )
            } )
        }

        return futureNew( operation )
            .onError( ex => {
                failures++
                lastFailTime = getTickCount()

                if ( failures >= threshold ) {
                    isOpen = true
                    writeLog( text: "Circuit breaker opened", log: "async" )
                }

                throw ex
            } )
    }
}

// Usage
breaker = new CircuitBreaker()
result = breaker.call( () => externalService.getData() )
    .onError( ex => "Service temporarily unavailable" )
    .get()
```

## 🔧 Executor Integration

### Using Specific Executors

```js
// CPU-intensive operations
cpuFuture = futureNew( () => {
    return performComplexCalculation()
}, "cpu-tasks" )

// I/O operations
ioFuture = futureNew( () => {
    return fetchFromDatabase()
}, "io-tasks" )

// Scheduled operations
scheduledFuture = futureNew( () => {
    return generateReport()
}, "scheduled-tasks" )
```

### Dynamic Executor Selection

```js
function smartExecutorChoice( operationType ) {
    switch ( operationType ) {
        case "cpu":
            return "cpu-tasks"
        case "io":
            return "io-tasks"
        case "scheduled":
            return "scheduled-tasks"
        default:
            return "io-tasks" // Default
    }
}

// Usage
future = futureNew(
    () => performOperation(),
    smartExecutorChoice( "cpu" )
)
```

## 📊 Monitoring and Debugging

### Performance Tracking

```js
startTime = getTickCount()

result = futureNew( () => {
    return expensiveOperation()
} )
.then( result => {
    duration = getTickCount() - startTime
    writeLog(
        text: "Operation completed in #duration#ms",
        log: "async"
    )
    return result
} )
.onError( ex => {
    duration = getTickCount() - startTime
    writeLog(
        text: "Operation failed after #duration#ms: #ex.message#",
        type: "Error",
        log: "async"
    )
    return null
} )
.get()
```

### Debug Pipeline

```js
debugPipeline = futureNew( () => {
    writeLog( text: "Starting data fetch", log: "async" )
    return fetchData()
} )
.then( data => {
    writeLog( text: "Data fetched, processing #data.len()# items", log: "async" )
    return processData( data )
} )
.then( processed => {
    writeLog( text: "Processing complete, #processed.len()# results", log: "async" )
    return formatResults( processed )
} )
.onError( ex => {
    writeLog(
        text: "Pipeline error at step: #ex.message#",
        type: "Error",
        log: "async"
    )
    return { "error": true }
} )
```

## 🌟 Static Factory Methods

BoxFuture provides convenient static methods for common scenarios:

### Creating Futures

```js
// Completed future with value
completed = BoxFuture.completedFuture( "Hello World" )

// Failed future with exception
failed = BoxFuture.failedFuture( "Something went wrong" )

// Future from value
valueFuture = BoxFuture.ofValue( 42 )

// Future from CompletableFuture
javaFuture = CompletableFuture.completedFuture( "test" )
boxFuture = BoxFuture.ofCompletableFuture( javaFuture )
```

### Delayed Execution

```js
// Execute after delay
delayed = BoxFuture.run(
    () => performDelayedTask(),
    BoxFuture.delayedExecutor( 5, "seconds" )
)

// Execute with custom executor after delay
customDelayed = BoxFuture.run(
    () => performTask(),
    BoxFuture.delayedExecutor( 10, "seconds", executorGet( "cpu-tasks" ) )
)
```

## 🚨 Error Handling Best Practices

### 1. Always Handle Errors

```js
// Good - Error handling included
future = futureNew( () => riskyOperation() )
    .onError( ex => {
        writeLog( text: "Operation failed: #ex.message#", log: "async" )
        return defaultValue
    } )

// Bad - No error handling
future = futureNew( () => riskyOperation() )
```

### 2. Use Timeouts

```js
// Good - Prevents hanging indefinitely
result = futureNew( () => externalCall() )
    .orTimeout( 30, "seconds" )
    .onError( ex => "Timeout occurred" )
    .get()

// Bad - Could hang forever
result = futureNew( () => externalCall() ).get()
```

### 3. Graceful Degradation

```js
// Good - Multiple fallback strategies
result = futureNew( () => primaryService() )
    .onError( ex => secondaryService() )
    .onError( ex => cacheService() )
    .onError( ex => "Service unavailable" )
    .get()
```

## 🎯 Performance Tips

### 1. Choose the Right Executor

```js
// CPU-intensive: Use cpu-tasks
cpuFuture = futureNew( () => calculatePi(1000000), "cpu-tasks" )

// I/O-intensive: Use io-tasks (default)
ioFuture = futureNew( () => fetchFromAPI() )

// Scheduled: Use scheduled-tasks
scheduledFuture = futureNew( () => cleanupTask(), "scheduled-tasks" )
```

### 2. Avoid Blocking Operations

```js
// Good - Non-blocking chaining
result = futureNew( () => fetchData() )
    .then( data => processData( data ) )
    .then( processed => saveData( processed ) )
    // Don't call .get() until you need the result

// Bad - Blocking at each step
data = futureNew( () => fetchData() ).get()
processed = futureNew( () => processData( data ) ).get()
result = futureNew( () => saveData( processed ) ).get()
```

### 3. Use Parallel Processing

```js
// Good - Parallel execution
results = BoxFuture.all(
    futureNew( () => task1() ),
    futureNew( () => task2() ),
    futureNew( () => task3() )
).get()

// Bad - Sequential execution
result1 = futureNew( () => task1() ).get()
result2 = futureNew( () => task2() ).get()
result3 = futureNew( () => task3() ).get()
```

## 🔍 Common Patterns and Use Cases

### API Orchestration

```js
// Orchestrate multiple API calls
apiResults = BoxFuture.all(
    futureNew( () => userService.getUser( userId ) ),
    futureNew( () => orderService.getOrders( userId ) ),
    futureNew( () => preferencesService.getPreferences( userId ) )
)
.then( results => {
    return {
        "user": results[1],
        "orders": results[2],
        "preferences": results[3]
    }
} )
.orTimeout( 10, "seconds" )
.get()
```

### Data Pipeline Processing

```js
// ETL pipeline
pipeline = futureNew( () => {
    // Extract
    return extractDataFromSources()
} )
.then( rawData => {
    // Transform
    return transformData( rawData )
}, "cpu-tasks" )
.then( transformedData => {
    // Load
    return loadDataToDestination( transformedData )
}, "io-tasks" )
.onError( ex => {
    // Handle pipeline failure
    writeLog( text: "ETL pipeline failed: #ex.message#", log: "async" )
    return { "success": false, "error": ex.message }
} )
```

### Real-time Processing

```js
// Process streaming data
function processStream( dataStream ) {
    return dataStream.map( item => {
        return futureNew( () => processItem( item ) )
            .orTimeout( 5, "seconds" )
            .onError( ex => null ) // Skip failed items
    } )
}

// Batch process results
results = BoxFuture.all( processStream( streamData ) )
    .then( results => results.filter( r => r != null ) )
    .get()
```

## 🔚 Conclusion

BoxFuture async pipelines provide a powerful, flexible way to handle asynchronous operations in BoxLang. By combining the fluent API with proper error handling, timeouts, and executor selection, you can build robust, high-performance applications that scale effectively.

Key takeaways:

* Use `futureNew()` and `asyncRun()` as your primary entry points
* Chain operations with `then()` and `thenAsync()` for readable pipelines
* Always include error handling with `onError()` and `exceptionally()`
* Use timeouts to prevent hanging operations
* Choose appropriate executors for different types of work
* Leverage parallel processing with `BoxFuture.all()` for performance

Start simple with basic transformations, then gradually incorporate more advanced patterns as your needs grow. The async pipeline approach will help you build more responsive, efficient applications that can handle complex asynchronous workflows with ease.
