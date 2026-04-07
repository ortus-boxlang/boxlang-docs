---
description: BoxLang Futures, Executors, Async/Parallel Programming and much more.
icon: waves-sine
---

# Async Programming

We've already covered basic threading in our core syntax and semantics section. In this section, we will discover the power behind the asynchronous framework behind Boxlang which is powered by the JDKs CompletableFutures, Executors, and much more.

**Note: This section of our documentation covers features coming soon to BoxLang 1.4.0.**

{% hint style="success" %}
We leverage Java `Executors`, `CompletableFutures` and many more classes from the concurrent packages in the JDK.
{% endhint %}

## BoxLang Async Framework

BoxLang's async framework provides a comprehensive suite of tools for modern concurrent programming, built on top of Java's proven concurrency primitives but enhanced with dynamic language features and developer-friendly APIs.

<figure><img src="../../.gitbook/assets/BoxLangAsync.png" alt=""><figcaption></figcaption></figure>

### ⚙️ Async Service

The AsyncService in BoxLang is in charge of coordinating executors, schedulers and configuration for the runtime.  Any executor you use via our BIFs or internal facitlities will end up being managed by this service.

### 🧵 Executors

All of our tasks and computing futures execute in the server's common `ForkJoin` pool the JDK provides. However, JDK 8+ provides you a framework for simplifying the execution of asynchronous tasks. It can automatically provide you with a pool of threads and a simple API for assigning tasks or work loads to them.

Learn more in [Executors](executors.md).

### 🎛️ Scheduler Service

Our scheduler service is in charge of creating and managing all BoxLang schedulers, whether they are global, dynamic or from contributed modules.

Learn more in [Scheduling Component](scheduling-component.md).

### ⏰ Schedulers

Schedulers can be written in BoxLang or in Java and will end up being managed by the scheduler service.  Each scheduler has a collection of scheduled tasks it can monitor, execute and manage.  Each scheduler is bound to a specific executor.

Learn more in [Scheduling Component](scheduling-component.md).

### 📅 Scheduled Tasks

Schedule tasks execute in an executor of choice and will be most likely managed by a scheduler.  There are times where tasks can be sent for execution directly to executors as well.

Learn more in [Scheduled Tasks](scheduled-tasks.md).

### 👀 Directory + File Watchers

The watcher service monitors one or more directories and dispatches filesystem change events to BoxLang listeners. This allows you to react to file creations, updates, and deletions in near real time.

Learn more in [Directory + File Watchers](directory-file-watchers.md).

### 🚀 BoxFuture

Our `BoxFuture` is a subclass of the JDKs `CompletableFuture` but enhanced for dynamic programming.

Learn more in [Box Futures](box-futures.md) and [Async Pipelines](async-pipelines.md).

## 🚀 What You Can Build

With BoxLang's async framework, you can create:

### High-Performance Applications

- **Non-blocking I/O operations** that scale to thousands of concurrent requests
- **CPU-intensive computations** distributed across multiple cores
- **Real-time data processing** pipelines with backpressure handling
- **Microservices** with async inter-service communication

### Robust Background Processing

- **Scheduled tasks** with cron-like flexibility and fluent configuration
- **Event-driven workflows** that respond to system changes
- **Batch processing** jobs that can be paused, resumed, and monitored
- **Queue-based processing** with automatic retry and error handling

### Advanced Coordination Patterns

- **Pipeline architectures** for streaming data transformation
- **Fan-out/Fan-in patterns** for parallel processing and aggregation
- **Circuit breakers** for fault-tolerant service integration
- **Rate limiting** and throttling for resource protection

## 🛠️ Core Capabilities

### ⚡ BoxFutures - Promise-Like Programming

Transform callback hell into readable, chainable operations:

```javascript
// Sequential async operations
userProfile = futureNew( () => authenticateUser( credentials ) )
    .then( token => fetchUserProfile( token ) )
    .then( profile => enrichWithPermissions( profile ) )
    .then( enrichedProfile => cacheProfile( enrichedProfile ) )
    .onError( ex => handleAuthError( ex ) )
    .orTimeout( 30, "SECONDS" )
```

### 🔄 Parallel Computing

Execute operations concurrently with automatic result aggregation:

```javascript
// Process multiple data sources in parallel
results = asyncAll([
    () => fetchFromDatabase(),
    () => fetchFromAPI(),
    () => fetchFromCache()
]).then( dataSources => mergeAndProcess( dataSources ) )

// Transform collections in parallel
processedUsers = asyncAllApply(
    userIds,
    userId => enhanceUserProfile( userId )
)
```

### ⏰ Intelligent Scheduling

Create sophisticated scheduling patterns with minimal code:

```javascript
// Complex scheduling with conditions
scheduler.task( "data-sync" )
    .call( () => syncExternalData() )
    .every( 15, "MINUTES" )
    .when( () => isBusinessHours() )
    .onError( ex => notifyOpsTeam( ex ) )
```

### 🎛️ Flexible Executors

Choose the right execution strategy for your workload:

```java
// I/O intensive tasks - unlimited virtual threads
ioExecutor = executorGet( "io-tasks" )  // Virtual threads for massive concurrency

// CPU intensive tasks - controlled thread pool
cpuExecutor = executorGet( "cpu-tasks" )  // Fixed pool for CPU-bound work

// Custom executors for specific needs
customExecutor = executorNew( "image-processing", "work-stealing", 8 )
```

### 👀 Directory/File Watchers

Monitor filesystem changes with ease:

```js
watcher = watcherNew(
    name = "source-watcher",
    paths = [ "./src", "./config" ],
    recursive = true,
    debounce = 250,
    listener = {
        "onCreate" : ( event ) => println( "Created: #event.relativePath#" ),
        "onModify" : ( event ) => println( "Modified: #event.relativePath#" ),
        "onDelete" : ( event ) => println( "Deleted: #event.relativePath#" ),
        "onOverflow" : ( event ) => println( "Watcher overflow detected, consider re-syncing state" )
    }
).start()
```

## 🎯 Real-World Use Cases

### API Gateway Pattern

```javascript
// Orchestrate multiple backend services
response = asyncAll([
    () => userService.getProfile( userId ),
    () => orderService.getOrders( userId ),
    () => recommendationService.getRecommendations( userId )
])
.then( results => aggregateApiResponse( results ) )
.orTimeout( 5, "SECONDS" )
.onError( ex => fallbackResponse() )
```

#### Data Pipeline Processing

```javascript
// ETL pipeline with error recovery
pipeline = futureNew( () => extractFromSource() )
    .then( data => validateData( data ), "cpu-tasks" )
    .then( validData => transformData( validData ), "cpu-tasks" )
    .then( transformedData => loadToDestination( transformedData ), "io-tasks" )
    .onError( ex => handlePipelineFailure( ex ) )
```

### Background Job Processing

```javascript
// Resilient background job with monitoring
scheduler.task( "report-generation" )
    .call( () => generateMonthlyReports() )
    .delay( 5, "MINUTES" )  // Allow system to stabilize
    .every( 1, "DAYS" )
    .at( "02:00" )  // Run at 2 AM
    .onSuccess( result => notifyCompletion( result ) )
    .onError( ex => escalateFailure( ex ) )
```

### Race Conditions and Fallbacks

```javascript
// Multiple data sources with automatic fallback
fastestData = asyncAny([
    () => primaryDatabase.query( sql ),
    () => readOnlyReplica.query( sql ),
    () => cache.get( cacheKey )
])
.then( data => processData( data ) )
.onError( ex => useDefaultData() )
```

## 🔧 Advanced Features

### Resource Management

- **Automatic cleanup** of threads and resources
- **Graceful shutdown** with configurable timeouts
- **Memory-efficient** virtual threads for I/O operations
- **CPU-aware** thread pools for compute-intensive tasks

### Error Handling & Resilience

- **Centralized exception management** with typed error handling
- **Automatic retry logic** with exponential backoff
- **Circuit breaker patterns** for external service protection
- **Timeout management** at multiple levels (operation, pipeline, system)

### Monitoring & Observability

- **Real-time metrics** for executor performance
- **Task execution statistics** with completion rates
- **Async logging** for debugging and monitoring
- **Health checks** for scheduler and executor states

### Integration & Interoperability

- **Java interop** with existing concurrent libraries
- **Module system** for extending async capabilities
- **Configuration-driven** executor and scheduler setup
- **Hot-swappable** task definitions and schedules
