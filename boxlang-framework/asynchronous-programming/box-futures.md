---
description: Asynchronous Programming Made Simple
icon: clock-rotate-left
---

# ⚡ BoxFutures

## 🙋 What Are BoxFutures?

`BoxFutures` are BoxLang's enhanced version of Java's `CompletableFuture`, designed to provide powerful asynchronous programming capabilities with dynamic constructs tailored for the BoxLang ecosystem. They represent a computation that will complete at some point in the future, allowing you to write non-blocking, concurrent code that's both elegant and efficient.

```text
Task Start  →  BoxFuture  →  Result Ready
    📋           ⚡           ✅
   (now)    (processing)     (later)
```

### **🎯 Why Use BoxFutures?**

* **Non-blocking Operations:** Execute tasks asynchronously without blocking the main thread
* **Fluent API:** Chain operations together with intuitive method names
* **Error Handling:** Built-in exception handling and recovery mechanisms
* **Composability:** Combine multiple futures for complex workflows
* **Dynamic Integration:** Seamlessly work with BoxLang's dynamic nature
* **Enhanced Timeouts:** Advanced timeout handling with custom behavior
* **Result Transformation:** Transform and map results through fluent pipelines

## 🚀 Creating BoxFutures

### Using the `futureNew()` BIF

The primary way to create BoxFutures is through the `futureNew()` Built-In Function (BIF):

```javascript
// Create an empty future (incomplete)
future = futureNew();

// Create a completed future with a value
future = futureNew( "Hello World" );

// Create a future from a function/closure
future = futureNew( () => {
    return "Computed result";
});

// Create a future with a specific executor
future = futureNew(
    () => heavyComputation(),
    "myCustomExecutor"
);
```

### Using Direct Java Import

For advanced use cases or when working directly with Java interop, you can import the `BoxFuture` class and use its static methods:

```javascript
import ortus.boxlang.runtime.async.BoxFuture;

// Create futures using static methods
future = BoxFuture.ofValue( "Direct value" );
completed = BoxFuture.completedFuture( result );
```

{% hint style="info" %}
**For Java Developers:** Java developers can also use BoxFuture directly in their Java code to interact with BoxLang's asynchronous ecosystem seamlessly.
{% endhint %}

## ⚡ Core Methods

### 🥇 Completion Methods

#### `get()` - Blocking Retrieval

```javascript
// Basic get (blocks until completion)
result = future.get();

// Get with timeout (milliseconds)
// Please note that the thread continues to execute even though the timeout is set
result = future.get( 5000 );

// Get with timeout and unit
result = future.get( 5, "seconds" );
```

Please note that even if you pass a timeout, the thread will continue to execute. This is useful for scenarios where you want to ensure the task is running without blocking indefinitely.  You can try to cancel the future if needed, but it is not guaranteed to stop the execution immediately.  The only real way to stop the execution is to attach it to an executor that can handle cancellation properly.

#### `join()` - Non-blocking Alternative

Join is a non-blocking alternative to `get()` that waits for the future to complete without throwing exceptions, if you need to handle exceptions, use `get()` instead.

```javascript
// Join without default
result = future.join();

// Join with default value if result is null
result = future.joinOrDefault( "default value" );
```

#### `getOrDefault()` - Safe Retrieval

```javascript
// Get with fallback if result is null
result = future.getOrDefault( "fallback value" );
```

### 🔄 Transformation Methods

#### `then()` vs `thenAsync()` - Understanding the Difference

The key difference between `then()` and `thenAsync()` lies in **where** and **how** the transformation function executes:

**🔄 `then()` - Synchronous Execution Context**

* Executes in the **same thread** that completes the future
* Uses the **calling thread** or the **completing thread**
* **Blocking** - the transformation runs immediately when the future completes
* Best for **lightweight, fast transformations**

**⚡ `thenAsync()` - Asynchronous Execution Context**

* Executes in a **different thread** from the default executor pool
* **Non-blocking** - the transformation is submitted to an executor
* Best for **heavy computations** or **I/O operations**
* Provides better **thread isolation** and **resource management**

####  Basic Usage Examples

```javascript
// SYNCHRONOUS - runs on completing thread
syncFuture = future.then( (value) => {
    // This runs immediately on the same thread
    return value.toUpperCase();
});

// ASYNCHRONOUS - runs on executor thread pool
asyncFuture = future.thenAsync( (value) => {
    // This runs on a different thread from the executor pool
    return processHeavyComputation( value );
});
```

####  With Custom Executors

When you specify a custom executor, both methods behave similarly but give you **explicit control** over thread management:

```javascript
// THEN with custom executor - still synchronous handoff
customSyncFuture = future.then(
    (value) => transform( value ),
    myCustomExecutor
);

// THEN ASYNC with custom executor - asynchronous handoff
customAsyncFuture = future.thenAsync(
    (value) => asyncTransform( value ),
    myCustomExecutor
);
```

#### 📊 Performance Comparison

| Method | Thread Usage | Best For | Performance |
|--------|-------------|----------|-------------|
| `then()` | Same thread | Light operations | Faster handoff |
| `thenAsync()` | New thread | Heavy operations | Better isolation |
| `then(fn, executor)` | Custom thread | Controlled execution | Predictable resources |
| `thenAsync(fn, executor)` | Custom thread | Controlled async | Maximum flexibility |

#### 🎨 Practical Examples

```javascript
// Light transformation - use then()
future.then( (user) => user.name.toUpperCase() );

// Heavy computation - use thenAsync()
future.thenAsync( (data) => {
    // CPU-intensive operation
    return processLargeDataSet( data );
});

// I/O operation with custom executor
future.thenAsync(
    (userId) => {
        // Database call
        return queryExecute( "SELECT * FROM users WHERE id = ?", [userId] );
    },
    "databasePool"
);

// Chain different execution contexts
future
    .then( (rawData) => parseData( rawData ) )           // Fast parsing on same thread
    .thenAsync( (parsed) => enrichData( parsed ) )       // Heavy enrichment on pool thread
    .then( (enriched) => enriched.summary );             // Quick summary on completing thread
```

### 🛡️ Error Handling

You can handle exceptions that occur during the future's execution using  `onError()` or `exceptionally()` methods.  They are the same method, but `onError()` is more idiomatic in BoxLang.

#### `onError()` - Exception Recovery

```javascript
// Handle errors gracefully
recoveredFuture = future.onError( (error) => {
    writeLog( "Error occurred: " & error.getMessage() );
    return "Recovery value";
});

// Equivalent to exceptionally()
future.exceptionally( (error) => {
    return handleError( error );
});
```

#### ⚡ **IMPORTANT: When Error Handlers Are Applied**

Error handlers like `onError()` and `exceptionally()` only handle exceptions from **previous stages** in the chain. This is crucial to understand for proper error handling:

```javascript
// ❌ WRONG: Error handler won't catch errors from subsequent stages
future = futureNew( () => workThatMightFail() )
    .onError( (error) => "recovered" )  // Only handles errors from futureNew()
    .then( (result) => riskyTransformation( result ) );  // Errors here are NOT caught

// ✅ CORRECT: Error handler catches errors from all previous stages
future = futureNew( () => workThatMightFail() )
    .then( (result) => riskyTransformation( result ) )
    .onError( (error) => "recovered" );  // Handles errors from both stages

// ✅ BEST: Multiple error handlers for different stages
future = futureNew( () => workThatMightFail() )
    .onError( (error) => {
        writeLog( "Initial work failed: " & error.getMessage() );
        return "fallback data";
    })
    .then( (result) => riskyTransformation( result ) )
    .onError( (error) => {
        writeLog( "Transformation failed: " & error.getMessage() );
        return "final fallback";
    });
```

#### 🎯 Error Handling Strategies

##### Strategy 1: Early Recovery

```javascript
// Handle errors as soon as they might occur
future = futureNew( () => fetchFromPrimaryAPI() )
    .onError( (error) => {
        writeLog( "Primary API failed, using fallback" );
        return fetchFromFallbackAPI();
    })
    .then( (data) => processData( data ) )
    .onError( (error) => {
        writeLog( "Processing failed" );
        return processedFallback();
    });
```

##### Strategy 2: Centralized Error Handling

```javascript
// Handle all errors at the end of the chain
future = futureNew( () => step1() )
    .then( (result) => step2( result ) )
    .then( (result) => step3( result ) )
    .onError( (error) => {
        writeLog( "Pipeline failed at: " & error.getMessage() );
        return handleAnyError( error );
    });
```

##### Strategy 3: Mixed Error Handling

```javascript
// Combine both approaches for different error types
future = futureNew( () => authenticateUser() )
    .onError( (error) => {
        // Handle auth errors specifically
        if ( error.getMessage().contains( "auth" ) ) {
            return refreshTokenAndRetry();
        }
        throw error; // Re-throw non-auth errors
    })
    .then( (user) => fetchUserData( user ) )
    .then( (data) => processUserData( data ) )
    .onError( (error) => {
        // Handle any remaining errors
        writeLog( "General error: " & error.getMessage() );
        return defaultUserData();
    });
```

### ⏱️ Timeout Management

Always remember that timeouts are not guaranteed to stop the execution of the future, they will only stop the waiting for the result.  If you need to stop the execution, you need to attach it to an executor that can handle cancellation properly, unless you can listen to interrupts in your code and handle them accordingly.

#### `orTimeout()` - Timeout with Exception

```javascript
// Timeout in milliseconds
timeoutFuture = future.orTimeout( 5000 );

// Timeout with time unit
timeoutFuture = future.orTimeout( 30, "seconds" );
```

#### `completeOnTimeout()` - Timeout with Default

```javascript
// Complete with default value on timeout
defaultFuture = future.completeOnTimeout( "timeout value", 5000 );

// With time unit
defaultFuture = future.completeOnTimeout(
    "timeout value",
    10,
    "seconds"
);
```

## 🎁 Enhanced Features

### 🔍 Attempt Results

BoxFutures provide a unique `getAsAttempt()` method that returns results wrapped in an `Attempt` object, perfect for functional error handling.  To learn more about BoxLang attempts, see [BoxLang Attempts](../../boxlang-language/syntax/attempts.md).

```javascript
// Get result as Attempt
attempt = future.getAsAttempt();

if ( attempt.isSuccess() ) {
    writeOutput( "Success: " & attempt.getResult() );
} else {
    writeOutput( "Error: " & attempt.getError() );
}

// With timeout
attempt = future.getAsAttempt( 5000 );
attempt = future.getAsAttempt( 5, "seconds" );
```

### 🎭 Fluent Aliases

BoxFutures provide intuitive aliases for common operations:

```javascript
// Instead of thenApply
future.then( transform );

// Instead of thenApplyAsync
future.thenAsync( transform );

// Instead of exceptionally
future.onError( recover );
```

## 🔗 Static Utility Methods

Remember you can use these via the bif or the import.

### 🏃 Running Functions

```javascript
import ortus.boxlang.runtime.async.BoxFuture;

// Run a function asynchronously
future = BoxFuture.run( () => {
    return doSomeWork();
});

// Use the bif
future = futureNew().run( () => {
    return doSomeWork();
});

// Run with custom executor
future = BoxFuture.run(
    () => heavyWork(),
    myExecutor
);
```

### 📦 Value Creation

```javascript
import ortus.boxlang.runtime.async.BoxFuture;

// Create completed future
completed = BoxFuture.ofValue( "immediate value" );
completed = BoxFuture.completedFuture( result );

// Same as BIF
completed = futureNew().ofValue( "immediate value" );
completed = futureNew().completedFuture( result );
// Or just pass the value to the futureNew()
completed = futureNew( "immediate value" );

// Create failed future
failed = BoxFuture.failedFuture( "Error message" );
```

### ⏳ Delayed Execution

```javascript
// Create delayed executor
delayedExec = BoxFuture.delayedExecutor( 5, "seconds" );

// With base executor
delayedExec = BoxFuture.delayedExecutor(
    5,
    "seconds",
    baseExecutor
);
```

## 🌊 Working with Multiple Futures

### 📋 Combining Futures

```javascript
// Wait for all futures to complete
allFuture = futureNew().all( context, future1, future2, future3 );
results = allFuture.get(); // Array of results

// With array of futures
futures = [ future1, future2, future3 ];
allFuture = futureNew().all( context, futures );
```

### 🗺️ Parallel Processing

```javascript
// Apply function to array items in parallel
results = futureNew().allApply(
    context,
    [ 1, 2, 3, 4, 5 ],
    (item) => item * 2
);

// With error handler
results = futureNew().allApply(
    context,
    items,
    (item) => processItem( item ),
    (error) => handleError( error )
);

// With timeout
results = futureNew().allApply(
    context,
    items,
    mapper,
    errorHandler,
    30,
    "seconds"
);
```

{% hint style="info" %}
**Learn More:** For detailed information about parallel processing patterns, see [Parallel Computations](parallel-computations.md).
{% endhint %}

## 📚 Common Usage Patterns

### 🔄 Chaining Operations

```javascript
future = futureNew( () => fetchData() )
    .then( (data) => processData( data ) )
    .then( (processed) => saveData( processed ) )
    .onError( (error) => handleError( error ) );
```

### 🎯 Async Pipelines

```javascript
// Create processing pipeline
pipeline = futureNew( () => loadUser( userId ) )
    .then( (user) => enrichUserData( user ) )
    .then( (enriched) => validateUser( enriched ) )
    .then( (validated) => saveUser( validated ) )
    .orTimeout( 30, "seconds" )
    .onError( (error) => logError( error ) );
```

{% hint style="info" %}
**Advanced Patterns:** For complex pipeline patterns and composition strategies, see [Async Pipelines](async-pipelines.md).
{% endhint %}

### 🛡️ Error Recovery

```javascript
future = futureNew( () => riskyOperation() )
    .onError( (error) => {
        writeLog( "Primary failed: " & error.getMessage() );
        return fallbackOperation();
    })
    .onError( (error) => {
        writeLog( "Fallback failed: " & error.getMessage() );
        return "ultimate fallback";
    });
```

### ⏱️ Timeout Handling

```javascript
future = futureNew( () => slowOperation() )
    .completeOnTimeout( "timeout result", 5, "seconds" )
    .then( (result) => {
        if ( result == "timeout result" ) {
            writeOutput( "Operation timed out" );
        } else {
            writeOutput( "Operation completed: " & result );
        }
    });
```

## 🔧 Working with Executors

BoxFutures integrate seamlessly with BoxLang's executor system:

```javascript
// Use specific executor
future = futureNew(
    () => cpuIntensiveTask(),
    "fixedPool"
);

// Chain with different executors
future = futureNew( () => fetchData() )
    .then(
        (data) => processData( data ),
        "processingPool"
    )
    .then(
        (result) => saveData( result ),
        "ioPool"
    );
```

{% hint style="info" %}
**Learn More:** For detailed information about executor types and configuration, see [Executors](executors.md).
{% endhint %}

## 🎯 Best Practices

### ✅ Do's

* **Use appropriate timeouts** for operations that might hang
* **Handle errors gracefully** with `onError()` or `exceptionally()`
* **Chain operations** instead of nesting callbacks
* **Choose the right executor** for your workload type
* **Use `getAsAttempt()`** for functional error handling
* **Combine with other async patterns** for complex workflows
* **Monitor executor health** and adjust pool sizes as needed
* **Use fluent API** for readability and maintainability
* **Shut down executors** properly to release resources

### ❌ Don'ts

* **Don't block unnecessarily** - use non-blocking operations when possible
* **Don't ignore errors** - always provide error handling
* **Don't create too many futures** - consider batching operations
* **Don't forget timeouts** for external operations
* **Don't mix blocking and non-blocking** patterns inconsistently

## 🚦 Performance Considerations

### 🎯 Optimization Tips

* **Batch operations** using `allApply()` for multiple item transformations
* **Use `thenAsync()`** for heavy computations to avoid blocking the main thread
* **Use appropriate executors** based on workload characteristics
* **Set reasonable timeouts** to prevent resource waste
* **Handle errors early** to prevent cascade failures
* **Monitor executor health** and adjust pool sizes as needed

### 📊 Monitoring

```javascript
// Check future status
if ( future.isDone() ) {
    writeOutput( "Future completed" );
}

if ( future.isCompletedExceptionally() ) {
    writeOutput( "Future failed" );
}

if ( future.isCancelled() ) {
    writeOutput( "Future was cancelled" );
}
```

## 🔗 Integration Examples

### HTTP Requests

```javascript
// Async HTTP call
httpFuture = futureNew( () => {
    bx:http url="https://api.example.com/data" result="response";
    return response
})

processedFuture = httpFuture
    .then( (response) -> deserializeJSON( response.fileContent ) )
    .then( (data) -> processApiData( data ) )
    .orTimeout( 30, "seconds" )
    .onError( (error) => handleApiError( error ) )
```

### Database Operations

```javascript
// Async database query
dbFuture = futureNew( () => {
    return queryExecute( "SELECT * FROM users WHERE active = ?", [true] );
});

usersFuture = dbFuture
    .then( (query) => queryToArray( query ) )
    .then( (users) => enrichUserProfiles( users ) )
    .onError( (error) => handleDbError( error ) );
```

### File Processing

```javascript
// Async file operations
fileFuture = futureNew( () -> {
    return fileRead( "/path/to/large/file.txt" );
})
.then( (content) => processFileContent( content ) )
.then( (processed) => saveProcessedData( processed ) )
.orTimeout( 60, "seconds" );
```

BoxFutures provide a powerful foundation for building responsive, scalable applications in BoxLang. By leveraging their fluent API and advanced features, you can create sophisticated asynchronous workflows that handle complex scenarios with elegance and efficiency.  Please continue to learn about async programming with BoxLang by exploring the following sections:

* [Async Pipelines](async-pipelines.md)
* [Executors](executors.md)
* [Parallel Computations](parallel-computations.md)
* [Scheduled Tasks](scheduled-tasks.md)
* [BoxLang Attempts](../../boxlang-language/syntax/attempts.md)