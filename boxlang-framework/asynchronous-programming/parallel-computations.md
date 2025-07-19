---
description: Powerful Parallel Computing with BoxLang's Async Framework
icon: list-timeline
---

# 🔄 Parallel Computations

BoxLang's async framework provides powerful tools for parallel computing, allowing you to execute multiple operations concurrently and efficiently process large datasets. Whether you're processing arrays, transforming data structures, or running independent computations, BoxLang's parallel computing BIFs give you the tools to maximize performance while maintaining code simplicity.

```text
Sequential:  Task1 → Task2 → Task3 → Task4  (16 seconds)
             🟦    🟦    🟦    🟦

Parallel:    Task1 ↘
             Task2  → Results              (4 seconds)
             Task3 ↗
             Task4 ↙
             🟦🟦🟦🟦
```

## 🎯 Core Parallel Computing BIFs

BoxLang provides several Built-In Functions (BIFs) for parallel computing:

| BIF | Purpose | Input | Output |
|-----|---------|-------|--------|
| `asyncAll()` | Execute futures in parallel | Array of futures/functions | BoxFuture<Array> |
| `asyncAny()` | Race multiple futures | Array of futures/functions | BoxFuture<Object> |
| `asyncRun()` | Execute single function async | Function | BoxFuture<Object> |
| `asyncAllApply()` | Apply function to collection in parallel | Array/Struct + mapper | Array/Struct |
| `futureNew()` | Create new BoxFuture | Value/Function | BoxFuture<Object> |

## 🚀 Basic Parallel Execution

### `asyncAll()` - Execute All in Parallel

The `asyncAll()` BIF executes multiple operations concurrently and returns results in order:

```javascript
// Execute multiple functions in parallel
futures = [
    () => fetchUserData( 1 ),
    () => fetchUserData( 2 ),
    () => fetchUserData( 3 )
];

// All functions execute concurrently
result = asyncAll( futures ).get();
// result = [ userData1, userData2, userData3 ]
```

**Advanced Example with Mixed Types:**

```javascript
// Mix of functions, futures, and values
operations = [
    // Function to execute
    () => performExpensiveCalculation(),

    // Pre-created future
    futureNew( () => fetchDataFromAPI() ),

    // Another function
    () => processLocalData()
];

allResults = asyncAll( operations )
    .then( results => {
        // Process all results together
        return combineResults( results );
    } )
    .get();
```

### `asyncAny()` - Race to the Finish

The `asyncAny()` BIF returns the result of the first operation to complete:

```javascript
// Race multiple data sources
dataSources = [
    () => fetchFromPrimaryDB(),
    () => fetchFromSecondaryDB(),
    () => fetchFromCache()
];

// Get result from whichever completes first
fastestResult = asyncAny( dataSources ).get();
```

**Timeout and Fallback Pattern:**

```javascript
// Race with timeout
operations = [
    () => fetchFromSlowAPI(),
    () => sleep( 5000 ).then( () => "TIMEOUT" )
];

result = asyncAny( operations )
    .then( value => {
        if( value == "TIMEOUT" ) {
            return getDefaultValue();
        }
        return value;
    } )
    .get();
```

## 🔄 Data Processing with `asyncAllApply()`

The `asyncAllApply()` BIF is perfect for applying transformations to collections in parallel:

### Array Processing

```javascript
// Process array of user IDs in parallel
userIds = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];

// Transform each user ID to user profile
userProfiles = asyncAllApply(
    userIds,
    ( userId ) => {
        // Each item processed in parallel
        return fetchUserProfile( userId );
    }
);

// userProfiles = [ profile1, profile2, ..., profile10 ]
```

### Struct Processing

```javascript
// Process struct entries in parallel
configuration = {
    "database": "production-db",
    "cache": "redis-cluster",
    "queue": "rabbitmq-primary"
};

// Validate each configuration in parallel
validationResults = asyncAllApply(
    configuration,
    ( item ) => {
        // item = { key: "database", value: "production-db" }
        return validateConfiguration( item.key, item.value );
    }
);

// Result: { database: true, cache: true, queue: false }
```

### With Error Handling

```javascript
// Process with error recovery
processedData = asyncAllApply(
    dataItems,

    // Mapper function
    ( item ) => processDataItem( item ),

    // Error handler
    ( error ) => {
        logger.error( "Processing failed: " & error.getMessage() );
        return { error: true, message: error.getMessage() };
    }
);
```

### With Custom Executor and Timeout

```javascript
// Use custom executor with timeout
results = asyncAllApply(
    largeDataset,
    ( item ) => expensiveComputation( item ),
    null, // no error handler
    "cpu-intensive", // custom executor
    30, // 30 second timeout
    "SECONDS"
);
```

## ⚡ Single Async Operations

### `asyncRun()` - Basic Async Execution

```javascript
// Execute function asynchronously
future = asyncRun( () => {
    return performLongRunningTask();
} );

// Continue with other work...
doOtherStuff();

// Get result when ready
result = future.get();
```

**With Custom Executor:**

```javascript
// Use specific executor for I/O intensive task
ioFuture = asyncRun(
    () => downloadLargeFile( url ),
    "io-threads"
);

// Use CPU executor for computation
cpuFuture = asyncRun(
    () => calculatePrimeNumbers( 1000000 ),
    "cpu-threads"
);
```

### `futureNew()` - Creating Futures

```javascript
// Create completed future
completedFuture = futureNew( "Hello World" );

// Create future from function
asyncFuture = futureNew( () => fetchRemoteData() );

// Create empty future (complete later)
emptyFuture = futureNew();
// ... later ...
emptyFuture.complete( "Result" );
```

## 🎛️ Advanced Patterns

### Pipeline Processing

```javascript
// Create processing pipeline
pipeline = futureNew( () => loadRawData() )
    .then( data => cleanData( data ) )
    .then( cleanData => transformData( cleanData ) )
    .then( transformedData => saveData( transformedData ) );

result = pipeline.get();
```

### Fan-Out/Fan-In Pattern

```javascript
// Fan out: split work across multiple operations
userIds = [ 1, 2, 3, 4, 5 ];

userFutures = userIds.map( id =>
    asyncRun( () => fetchUser( id ) )
);

// Fan in: combine all results
allUsers = asyncAll( userFutures )
    .then( users => {
        // Combine and process all users
        return aggregateUserData( users );
    } );

aggregatedData = allUsers.get();
```

### Retry with Exponential Backoff

```javascript
function retryOperation( operation, maxRetries = 3 ) {
    return asyncRun( () => {
        var attempt = 0;
        while( attempt < maxRetries ) {
            try {
                return operation();
            } catch( e ) {
                attempt++;
                if( attempt >= maxRetries ) throw e;

                // Exponential backoff
                sleep( 1000 * (2 ^ attempt) );
            }
        }
    } );
}

// Use retry wrapper
result = retryOperation( () => unreliableAPICall() ).get();
```

## 🛠️ Executor Management

### Using Custom Executors

```javascript
// Create custom executor for specific workload
executorNew(
    name: "data-processing",
    type: "fixed",
    maxThreads: 8
);

// Use custom executor
results = asyncAllApply(
    bigDataSet,
    ( item ) => processItem( item ),
    null, // no error handler
    "data-processing" // custom executor
);
```

### 🚨 Thread Cancellation Control

For scenarios where you need to cancel all running threads, use a custom executor that you can shutdown:

```javascript
// Create dedicated executor for cancellable work
executorNew(
    name: "cancellable-work",
    type: "cached",
    maxThreads: 10
);

try {
    // Start long-running parallel work
    future = asyncAllApply(
        massiveDataset,
        ( item ) => processVerySlowItem( item ),
        null,
        "cancellable-work", // our dedicated executor
        0, // no timeout
        "SECONDS"
    );

    // ... some condition occurs that requires cancellation ...
    if( shouldCancel() ) {
        // Shutdown the executor - this will attempt to cancel all running tasks
        executorShutdown( "cancellable-work", force: true );
        throw new Exception( "Processing was cancelled" );
    }

    result = future.get();

} finally {
    // Always clean up
    executorShutdown( "cancellable-work" );
}
```

**⚠️ Important Notes on Cancellation:**
- Thread cancellation is **cooperative** - tasks must check for interruption
- Use `Thread.interrupted()` or `Thread.currentThread().isInterrupted()` in your code
- Not all operations can be cancelled (e.g., blocking I/O)
- Cancellation may not be immediate

```javascript
// Cancellation-aware task
function cancellableTask( data ) {
    for( var i = 1; i <= data.size(); i++ ) {
        // Check for cancellation periodically
        if( Thread.currentThread().isInterrupted() ) {
            throw new InterruptedException( "Task was cancelled" );
        }

        // Do work
        processDataItem( data[i] );
    }
    return "Complete";
}
```

## 📊 Performance Monitoring

### Timing Parallel Operations

```javascript
startTime = getTickCount();

result = asyncAllApply(
    dataSet,
    ( item ) => processItem( item )
);

endTime = getTickCount();
systemOutput( "Parallel processing took: #(endTime - startTime)# ms" );
```

### Memory and Resource Monitoring

```javascript
// Monitor resource usage
memoryBefore = getMemoryUsage();

futures = [
    asyncRun( () => memoryIntensiveTask1() ),
    asyncRun( () => memoryIntensiveTask2() ),
    asyncRun( () => memoryIntensiveTask3() )
];

results = asyncAll( futures ).get();

memoryAfter = getMemoryUsage();
systemOutput( "Memory used: #(memoryAfter - memoryBefore)# bytes" );
```

## 🎯 Best Practices

### ✅ Do's

1. **Choose the Right Tool:**
   ```javascript
   // Use asyncAll() for independent parallel operations
   userProfiles = asyncAll( userIds.map( id => () => fetchUser( id ) ) );

   // Use asyncAllApply() for transforming collections
   processedData = asyncAllApply( rawData, item => transform( item ) );

   // Use asyncAny() for racing/fallback scenarios
   fastResult = asyncAny( [ primarySource, fallbackSource ] );
   ```

2. **Handle Errors Gracefully:**
   ```javascript
   results = asyncAllApply(
       data,
       item => processItem( item ),
       error => {
           // Log and return safe default
           logger.error( error );
           return getDefaultValue();
       }
   );
   ```

3. **Use Appropriate Executors:**
   ```javascript
   // I/O intensive - use more threads
   ioResults = asyncRun( () => fetchData(), "io-executor" );

   // CPU intensive - limit to CPU cores
   cpuResults = asyncRun( () => calculate(), "cpu-executor" );
   ```

### ❌ Don'ts

1. **Don't Block in Parallel Code:**
   ```javascript
   // BAD: Blocking defeats the purpose
   asyncAllApply( data, item => {
       return syncBlockingCall( item ); // This blocks!
   } );

   // GOOD: Keep operations async
   asyncAllApply( data, item => {
       return asyncNonBlockingCall( item );
   } );
   ```

2. **Don't Create Too Many Threads:**
   ```javascript
   // BAD: One thread per item
   bigData = range( 1, 10000 );
   asyncAllApply( bigData, item => process( item ) ); // 10,000 threads!

   // GOOD: Batch processing
   batches = chunk( bigData, 100 );
   asyncAllApply( batches, batch => processBatch( batch ) );
   ```

3. **Don't Forget Resource Cleanup:**
   ```javascript
   // BAD: Executor leaks resources
   executorNew( "temp-executor" );
   asyncRun( () => work(), "temp-executor" );
   // Never cleaned up!

   // GOOD: Always clean up
   try {
       executorNew( "temp-executor" );
       result = asyncRun( () => work(), "temp-executor" ).get();
   } finally {
       executorShutdown( "temp-executor" );
   }
   ```

## 🔗 Related Documentation

- **[Async Pipelines](async-pipelines.md)** - For chaining asynchronous operations
- **[Executors](executors.md)** - For managing thread pools and execution
- **[Scheduled Tasks](scheduled-tasks.md)** - For time-based parallel execution

## 📈 Performance Comparison

```text
Sequential Processing (1000 items):
Item1 → Item2 → Item3 → ... → Item1000
⏱️ Time: ~1000 seconds (1 second per item)

Parallel Processing (1000 items, 10 threads):
Batch1 (100 items) ↘
Batch2 (100 items) → Combined Results
Batch3 (100 items) ↗
...
Batch10 (100 items) ↙
⏱️ Time: ~100 seconds (10x speedup!)
```

---

With BoxLang's parallel computing capabilities, you can dramatically improve application performance by leveraging multiple CPU cores and concurrent execution. Choose the right BIF for your use case, handle errors properly, and always consider resource management for optimal results.