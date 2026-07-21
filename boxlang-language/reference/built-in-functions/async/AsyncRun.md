[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `AsyncRun`

Executes the given code asynchronously and returns to you a BoxFuture object which inherits from CompletableFuture.

This way you can create fluent asynchronous code that can be chained and composed.

## Method Signature

```
AsyncRun(callback=[function], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function` | `true` | The code to execute asynchronously, this can be a closure<br>                    or lambda. |  |
| `executor` | `any` | `false` | The executor to use for the asynchronous execution. This<br>                    can be an instance of an Executor class, or the name of a<br>                    registered executor in the AsyncService. |  |

## Examples

### Execute code asynchronously

Runs the callback in a separate thread and returns a BoxFuture.

```java
future = asyncRun( () => sleep( 100 ) && return "done" );
writeOutput( future.get() );

```

Result: done

### Chain async operations with then()

```java
asyncRun( () => 10 )
    .then( ( v ) => v * 2 )
    .then( ( v ) => v + 5 )
    .thenAccept( ( v ) => writeOutput( v ) );

```

Result: 25

### Using the runAsync() alias

```java
future = runAsync( () => "hello from async" );
writeOutput( future.get() );

```

Result: hello from async

## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncAny](./AsyncAny.md)
  * [ExecutorDelete](./ExecutorDelete.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorNew](./ExecutorNew.md)
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
