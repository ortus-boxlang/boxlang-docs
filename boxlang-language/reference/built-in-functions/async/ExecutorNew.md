[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExecutorNew`

Creates and registers a new executor by name and type.

The return value is an BoxExecutor object that can be used to interact with the executor.

 Available types are:
 - "cached" - Creates a cached thread pool executor.
 - "fixed" - Creates a fixed thread pool executor.
 - "fork_join" - Creates a fork join pool executor.
 - "scheduled" - Creates a scheduled thread pool executor.
 - "single" - Creates a single thread executor.
 - "virtual" - Creates a virtual thread executor.
 - "work_stealing" - Creates a work stealing thread pool executor.

## Method Signature

```
ExecutorNew(name=[string], type=[string], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the executor to create if not already created |  |
| `type` | `string` | `true` | The type of executor to create |  |
| `maxThreads` | `integer` | `false` |  | `10` |

## Examples

### Create a new executor service

```java
exec = executorNew( "myPool", "fixed", 4 );
writeOutput( exec.name() & "," & exec.type() );

```

Result: myPool,FIXED

### Available executor types

```java
executorNew( "cachedPool", "cached" );
executorNew( "singleThread", "single" );
executorNew( "virtualThreads", "virtual" );
writeOutput( executorHas( "cachedPool" ) & executorHas( "singleThread" ) & executorHas( "virtualThreads" ) );

```

Result: truetruetrue

### Cached thread pool (unbounded)

```java
exec = executorNew( "workPool", "cached" );
writeOutput( exec.type() );

```

Result: CACHED

## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncAny](./AsyncAny.md)
  * [AsyncRun](./AsyncRun.md)
  * [ExecutorDelete](./ExecutorDelete.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [FutureNew](./FutureNew.md)
  * [IsInThread](./IsInThread.md)
  * [isThreadAlive](./isThreadAlive.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadCurrent](./ThreadCurrent.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
