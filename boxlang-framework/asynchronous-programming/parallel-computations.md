---
description: Powerful Parallel Computing with BoxLang's Async Framework
icon: list-timeline
---

# 🔄 Parallel Computations

> Introduced in v1.4.0

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

## 🔢 Collection Parallel Methods

BoxLang provides powerful parallel processing capabilities for all collection types (arrays, lists, queries, and structs) through parallel versions of common iteration methods. These methods can dramatically improve performance when processing large collections or when the callback functions involve expensive operations.

Just make sure you understand the intricacies of creating and managing parallel tasks, as improper use can lead to resource contention or inefficient execution.

### 📋 Supported Collection Types

All parallel methods work across these data types:

| Type | Methods |
|------|---------|
| **Array** | `arrayEach()`, `arrayEvery()`, `arrayFilter()`, `arrayMap()`, `arrayNone()`, `arraySome()` |
| **List** | `listEach()`, `listEvery()`, `listFilter()`, `listMap()`, `listNone()`, `listSome()` |
| **Query** | `queryEach()`, `queryEvery()`, `queryFilter()`, `queryMap()`, `queryNone()`, `querySome()` |
| **Struct** | `structEach()`, `structEvery()`, `structFilter()`, `structMap()`, `structNone()`, `structSome()` |

### 🎯 Collection Method Purposes

Each collection method serves a specific purpose in data processing:

| Method | Purpose | Input | Output | Use Case |
|--------|---------|-------|--------|----------|
| **`Each`** | **Iteration with side effects** | Collection + callback | `void` | Logging, notifications, updating external state |
| **`Every`** | **Universal validation** | Collection + predicate | `boolean` | Check if ALL items meet the criteria predicate |
| **`Filter`** | **Selective extraction** | Collection + predicate | New collection | Extract items matching conditions |
| **`Map`** | **Transformation** | Collection + mapper | New collection | Transform each item to new form |
| **`None`** | **Negative validation** | Collection + predicate | `boolean` | Ensure NO items meet the criteria predicate |
| **`Some`** | **Existence check** | Collection + predicate | `boolean` | Check if ANY items meet the criteria predicate |

#### 🔄 **Each** - Perform Actions

Execute side effects for each item without returning results:

```javascript
// Purpose: Do something with each item (logging, notifications, updates)
arrayEach( users, user => {
    logUserActivity( user );
    sendWelcomeEmail( user );
    updateUserMetrics( user );
} );
// Returns: nothing (void)
```

#### ✅ **Every** - Validate All

Test whether ALL items in a collection meet a condition:

```javascript
// Purpose: Ensure every item passes validation
allUsersValid = arrayEvery( users, user => {
    return user.age >= 18 && user.hasValidEmail();
} );
// Returns: true if ALL users are valid, false if ANY fail
```

#### 🔍 **Filter** - Extract Matching Items

Create a new collection containing only items that meet criteria:

```javascript
// Purpose: Get subset of items matching conditions
activeUsers = arrayFilter( users, user => {
    return user.status == "active" && user.lastLogin > lastWeek;
} );
// Returns: new array with only active users
```

#### 🔄 **Map** - Transform Items

Transform each item into a new form, creating a new collection:

```javascript
// Purpose: Convert each item to something else
userSummaries = arrayMap( users, user => {
    return {
        id: user.id,
        name: user.fullName,
        summary: "Active since " & user.createdDate
    };
} );
// Returns: new array of transformed objects
```

#### ❌ **None** - Ensure Absence

Verify that NO items in the collection meet a condition:

```javascript
// Purpose: Security/safety checks - ensure bad conditions don't exist
noSuspiciousActivity = arrayNone( transactions, transaction => {
    return transaction.amount > 10000 && transaction.location == "suspicious";
} );
// Returns: true if NO transactions are suspicious, false if ANY are found
```

#### 🔎 **Some** - Check Existence

Test whether AT LEAST ONE item meets a condition:

```javascript
// Purpose: Find if something exists without needing the actual item
hasAdminUser = arraySome( users, user => {
    return user.role == "admin" && user.isActive;
} );
// Returns: true if ANY admin exists, false if none found
```

### 🎛️ Parallel Execution Parameters

All collection parallel methods support these consistent parameters:

```javascript
// Universal parallel parameters (positions vary by collection type)
parallel: boolean = false        // Enable parallel execution
maxThreads: integer = null       // Custom thread count (optional)
virtual: boolean = false         // Use virtual threads (optional)
```

**Execution Modes:**

- **`parallel: false`** - Sequential execution (default)
- **`parallel: true, maxThreads: null`** - Uses common ForkJoinPool (automatic thread count)
- **`parallel: true, maxThreads: N`** - Creates custom ForkJoinPool with N threads
- **`parallel: true, virtual: true`** - Uses virtual threads for unlimited concurrency
- **`parallel: true, maxThreads: true`** - Shorthand for virtual threads (positional syntax)

### 🔄 Array Parallel Processing

```javascript
// Large dataset processing
bigData = arrayRange( 1, 100000 );

// Parallel transformation with custom thread count
results = arrayMap(
    bigData,
    item => expensiveComputation( item ),
    true,  // parallel
    8      // maxThreads
);

// Using virtual threads for I/O intensive operations
ioResults = arrayMap(
    urls,
    url => httpGet( url ), // Network I/O benefits from virtual threads
    true,   // parallel
    null,   // maxThreads (not used with virtual)
    true    // virtual threads
);

// Shorthand syntax for virtual threads (using positional)
virtualResults = arrayMap(
    urls,
    url => httpGet( url ),
    true,  // parallel
    true   // maxThreads: true = virtual threads
);

// Using member method with virtual threads
results = bigData.arrayMap(
    item => expensiveComputation( item ),
    true,  // parallel
    8      // maxThreads
);

// Member method with virtual threads
ioResults = urls.arrayMap(
    url => httpGet( url ),
    true,  // parallel
    null,  // maxThreads
    true   // virtual
);

// Parallel filtering with automatic thread count
filtered = arrayFilter(
    bigData,
    item => complexValidation( item ),
    true   // parallel, automatic threads
);

// Parallel validation with virtual threads
allValid = arrayEvery(
    dataItems,
    item => validateBusinessRules( item ),
    true,  // parallel
    true   // virtual threads (shorthand)
);
```

### 📝 List Parallel Processing

List methods include additional delimiter parameters before parallel options:

```javascript
// Process CSV data in parallel
csvData = "user1,active,admin|user2,inactive,user|user3,active,guest";

// Parallel list processing
processedUsers = listMap(
    csvData,
    userRecord => {
        parts = listToArray( userRecord );
        return {
            username: parts[1],
            status: parts[2],
            role: parts[3],
            processed: true
        };
    },
    "|",     // delimiter
    false,   // includeEmptyFields
    true,    // multiCharacterDelimiter
    true,    // parallel
    6        // maxThreads
);

// Using virtual threads for I/O heavy list processing
apiData = "api1.com/users|api2.com/users|api3.com/users";
apiResults = listMap(
    apiData,
    apiUrl => httpGet( apiUrl ), // Network I/O
    "|",     // delimiter
    false,   // includeEmptyFields
    true,    // multiCharacterDelimiter
    true,    // parallel
    null,    // maxThreads
    true     // virtual threads
);

// Shorthand virtual threads (positional)
apiResultsShort = listMap(
    apiData,
    apiUrl => httpGet( apiUrl ),
    "|",     // delimiter
    false,   // includeEmptyFields
    true,    // multiCharacterDelimiter
    true,    // parallel
    true     // maxThreads: true = virtual
);

// Parallel validation
allUsersValid = listEvery(
    csvData,
    userRecord => validateUserRecord( userRecord ),
    "|",     // delimiter
    false,   // includeEmptyFields
    true,    // multiCharacterDelimiter
    true     // parallel
);
```

### 🗄️ Query Parallel Processing

```javascript
// Process large query results in parallel
largeQuery = queryExecute( "SELECT * FROM transactions WHERE amount > 1000" );

// Parallel transformation
enrichedData = queryMap(
    largeQuery,
    row => {
        return {
            id: row.id,
            amount: row.amount,
            category: categorizeTransaction( row ),
            risk_score: calculateRiskScore( row ),
            processed_at: now()
        };
    },
    true,  // parallel
    8      // maxThreads
);

// Using virtual threads for I/O intensive operations
apiEnrichedData = queryMap(
    largeQuery,
    row => {
        // Each row requires external API calls
        return {
            id: row.id,
            amount: row.amount,
            geocode: geocodeAPI( row.location ),      // API call
            creditCheck: creditAPI( row.customer ),   // API call
            fraudCheck: fraudAPI( row.details )       // API call
        };
    },
    true,  // parallel
    true   // virtual threads (shorthand)
);

// Explicit virtual threads syntax
virtualEnrichedData = queryMap(
    largeQuery,
    row => enrichWithAPIs( row ),
    true,  // parallel
    null,  // maxThreads (ignored with virtual)
    true   // virtual threads
);

// Parallel filtering with virtual threads
suspiciousTransactions = queryFilter(
    largeQuery,
    row => detectFraud( row ), // May involve external fraud detection APIs
    true,  // parallel
    true   // virtual threads
);
```

### 🏗️ Struct Parallel Processing

```javascript
// Process configuration object in parallel
appConfig = {
    database: { host: "db1", port: 3306 },
    cache: { host: "redis1", port: 6379 },
    queue: { host: "rabbit1", port: 5672 },
    api: { host: "api1", port: 8080 }
};

// Parallel service validation with platform threads
serviceStatus = structMap(
    appConfig,
    ( key, config ) => {
        return {
            service: key,
            status: checkServiceHealth( config ),
            latency: measureLatency( config ),
            last_check: now()
        };
    },
    true,  // parallel
    4      // maxThreads
);

// Using virtual threads for connection testing
connectivityStatus = structMap(
    appConfig,
    ( key, config ) => {
        // Each service check involves network I/O
        return {
            service: key,
            connected: testConnection( config ),
            ping_time: measurePing( config ),
            ssl_valid: checkSSLCert( config )
        };
    },
    true,  // parallel
    true   // virtual threads (shorthand)
);

// Explicit virtual threads syntax
detailedStatus = structMap(
    appConfig,
    ( key, config ) => performDetailedHealthCheck( config ),
    true,  // parallel
    null,  // maxThreads (ignored with virtual)
    true   // virtual threads
);

// Parallel connectivity check with virtual threads
allServicesUp = structEvery(
    appConfig,
    ( key, config ) => testConnection( config ), // Network I/O
    true,  // parallel
    true   // virtual threads
);
```

### 🎯 Method-Specific Examples

#### `Each` - Side Effects

```javascript
// Parallel logging/notification with platform threads
arrayEach(
    criticalAlerts,
    alert => {
        logAlert( alert );
        sendNotification( alert );
        updateMetrics( alert );
    },
    true,  // parallel
    6      // maxThreads
);

// Using virtual threads for I/O intensive notifications
arrayEach(
    criticalAlerts,
    alert => {
        // All of these involve network I/O
        emailAlert( alert );         // SMTP I/O
        slackNotification( alert );  // HTTP API I/O
        smsAlert( alert );          // SMS API I/O
        pushNotification( alert );   // Push service I/O
    },
    true,  // parallel
    true   // virtual threads - perfect for I/O
);
```

#### `Every` - Validation

```javascript
// Parallel data validation with platform threads
allDataValid = arrayEvery(
    dataRecords,
    record => {
        return validateSchema( record ) &&
               validateBusinessRules( record ) &&
               checkDataIntegrity( record );
    },
    true,  // parallel
    8      // maxThreads
);

// Using virtual threads for external validation services
allExternallyValid = arrayEvery(
    dataRecords,
    record => {
        // Each validation involves external API calls
        return validateWithAPI( record ) &&      // HTTP API call
               checkCreditBureau( record ) &&     // External service
               verifyWithThirdParty( record );    // Another API
    },
    true,  // parallel
    true   // virtual threads - handles external I/O
);
```

#### `Some` - Existence Check

```javascript
// Parallel search
foundSuspicious = arraySome(
    transactions,
    transaction => detectAnomalies( transaction ),
    true,  // parallel
    4      // maxThreads
);
```

#### `None` - Negative Validation

```javascript
// Parallel security check
noThreatsFound = arrayNone(
    requests,
    request => detectSecurityThreat( request ),
    true,  // parallel
    6      // maxThreads
);
```

### ⚡ Performance Benefits

```text
Sequential Processing (10,000 items):
[██████████] Item 1-10,000 processed sequentially
⏱️ Time: ~100 seconds (0.01 sec per item)

Parallel Processing (10,000 items, 8 threads):
Thread 1: [███] Items 1-1,250    ↘
Thread 2: [███] Items 1,251-2,500 → Combined
Thread 3: [███] Items 2,501-3,750 ↗  Results
Thread 4: [███] Items 3,751-5,000 ↙
Thread 5: [███] Items 5,001-6,250 ↘
Thread 6: [███] Items 6,251-7,500 → (~8x faster)
Thread 7: [███] Items 7,501-8,750 ↗
Thread 8: [███] Items 8,751-10,000 ↙
⏱️ Time: ~12.5 seconds (8x speedup!)

Virtual Thread Processing (10,000 items, unlimited virtual threads):
VThread 1: [█] Item 1      ↘
VThread 2: [█] Item 2       → Nearly
VThread 3: [█] Item 3       → Instant
...                         → Results
VThread 10k: [█] Item 10k  ↙
⏱️ Time: ~0.5 seconds (200x speedup for I/O intensive!)
```

<details>

<summary>🌟 Virtual Threads: The Game Changer</summary>

> Introduced in BoxLang v1.5.0

Virtual threads are lightweight, managed by the JVM, and perfect for I/O-intensive operations. Unlike platform threads, you can create millions of virtual threads without performance degradation.

### 🎯 When to Use Virtual Threads

**✅ Perfect for Virtual Threads:**

- **Network I/O**: API calls, database queries, file downloads
- **File Operations**: Reading/writing many files
- **External Service Calls**: Microservice communication
- **Blocking Operations**: Any operation that waits

**❌ Better with Platform Threads:**

- **CPU-Intensive Work**: Mathematical calculations, data processing
- **Memory-Intensive Operations**: Large object manipulation
- **Short-Running Tasks**: Operations that complete quickly

### 🔄 Virtual Thread Examples

### Network I/O Operations

```javascript
// Perfect use case: Multiple API calls
urls = [
    "https://api1.example.com/data",
    "https://api2.example.com/users",
    "https://api3.example.com/config",
    // ... potentially thousands of URLs
];

// Virtual threads can handle massive concurrency
responses = arrayMap(
    urls,
    url => httpGet( url ), // Each blocks on network I/O
    true,  // parallel
    true   // virtual threads - can handle thousands!
);
```

### Database Operations

```javascript
### Database Operations

```javascript
// Process many database queries concurrently
customerIds = arrayRange( 1, 10000 );

customerData = arrayMap(
    customerIds,
    id => queryExecute(
        "SELECT * FROM customers WHERE id = ?",
        [ id ]
    ),
    true,  // parallel
    true   // virtual threads - perfect for DB I/O
);
```

### File Processing

```javascript
### File Processing

```javascript
// Process thousands of files
files = directoryList( "/data/files" );

processedFiles = arrayMap(
    files,
    filePath => {
        content = fileRead( filePath );           // I/O operation
        processed = processContent( content );     // CPU work
        fileWrite( filePath & ".processed", processed ); // I/O operation
        return { file: filePath, status: "complete" };
    },
    true,  // parallel
    true   // virtual threads - handles I/O efficiently
);
```

### 🆚 Virtual vs Platform Threads Comparison

| Aspect | Platform Threads | Virtual Threads |
|--------|------------------|-----------------|
| **Max Concurrent** | ~1,000-5,000 | Millions+ |
| **Memory per Thread** | ~2MB stack | ~Few KB |
| **Creation Cost** | Expensive | Cheap |
| **Best For** | CPU-intensive | I/O-intensive |
| **JVM Management** | OS-scheduled | JVM-managed |
| **Blocking Behavior** | Blocks OS thread | Suspends virtually |

### 📊 Performance Comparison

```javascript
// Example: Processing 1000 URLs

// Platform threads (limited concurrency)
platformResults = arrayMap(
    urls,
    url => httpGet( url ),
    true,  // parallel
    50     // Limited to 50 threads
);
// ⏱️ Time: ~20 seconds (limited by thread count)

// Virtual threads (unlimited concurrency)
virtualResults = arrayMap(
    urls,
    url => httpGet( url ),
    true,  // parallel
    true   // Virtual threads - all 1000 concurrent!
);
// ⏱️ Time: ~2 seconds (limited only by network speed)
```

### 🎛️ Best Practices for Collection Parallel Processing

#### 1. **Choose Appropriate Thread Count**

```javascript
// Consider your system's CPU cores
cpuCores = runtime.availableProcessors();

// Rule of thumb for CPU-intensive work
optimalThreads = cpuCores;

// For I/O-intensive work, you can use more threads
ioThreads = cpuCores * 2;

// Apply to collection processing
results = arrayMap( data, mapper, true, optimalThreads );
```

#### 2. **Use Parallel Processing for Right-Sized Collections**

```javascript
// Small collections: sequential is often faster
smallData = range( 1, 100 );
arrayMap( smallData, mapper ); // No parallel needed

// Large collections: parallel shines
largeData = range( 1, 100000 );
arrayMap( largeData, mapper, true, 8 ); // Parallel recommended
```

#### 3. **Expensive Operations Benefit Most**

```javascript
// GOOD: Expensive operations
arrayMap(
    urls,
    url => httpGet( url ), // Network I/O
    true, 8
);

// GOOD: CPU-intensive work
arrayMap(
    images,
    image => resizeImage( image ), // Image processing
    true, 4
);

// CONSIDER: Simple operations might not benefit
arrayMap(
    numbers,
    n => n * 2, // Very simple operation
    false // Sequential might be faster
);
```

</details>

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

<details>

<summary>🎛️ Advanced Patterns</summary>

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

</details>

<details>

<summary>🛠️ Executor Management</summary>

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

</details>

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

<details open>

<summary>🎯 Best Practices (Do's and Don'ts)</summary>

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

2. **Choose the Right Threading Model:**

   ```javascript
   // CPU-intensive work: use platform threads
   cpuResults = arrayMap(
       data,
       item => intensiveCalculation( item ),
       true,  // parallel
       8      // platform threads
   );

   // I/O-intensive work: use virtual threads
   ioResults = arrayMap(
       urls,
       url => httpGet( url ),
       true,  // parallel
       true   // virtual threads
   );
   ```

3. **Handle Errors Gracefully:**

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

4. **Use Appropriate Executors:**

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

2. **Don't Use Virtual Threads for CPU-Intensive Work:**

   ```javascript
   // BAD: Virtual threads for CPU work
   arrayMap(
       numbers,
       n => intensiveMathCalculation( n ),
       true,  // parallel
       true   // virtual threads - bad for CPU work
   );

   // GOOD: Platform threads for CPU work
   arrayMap(
       numbers,
       n => intensiveMathCalculation( n ),
       true,  // parallel
       8      // platform threads
   );
   ```

3. **Don't Create Too Many Platform Threads:**

   ```javascript
   // BAD: One thread per item
   bigData = range( 1, 10000 );
   asyncAllApply( bigData, item => process( item ) ); // 10,000 threads!

   // GOOD: Use virtual threads for high concurrency
   asyncAllApply( bigData, item => process( item ), null, null, true );

   // OR: Batch processing with platform threads
   batches = chunk( bigData, 100 );
   asyncAllApply( batches, batch => processBatch( batch ) );
   ```

4. **Don't Forget Resource Cleanup:**

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

</details>

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
