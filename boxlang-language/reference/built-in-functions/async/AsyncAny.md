[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `AsyncAny`

This BIF accepts an array of futures/closures/lambdas and executes them all in parallel,
 returning a BoxFuture that will contain the result of the first future that completes successfully.

## Method Signature

```
AsyncAny(futures=[array], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `futures` | `array` | `true` | An array of BoxFuture objects to process in parallel |  |
| `executor` | `any` | `false` | The executor to use for the asynchronous execution. This<br>                    can be an instance of an Executor class, or the name of a<br>                    registered executor in the AsyncService. |  |

## Examples

### Return the first future to complete

Executes all futures in parallel and returns the result of the fastest one.

```java
slow = asyncRun( () => sleep( 200 ) && return "slow" );
fast = asyncRun( () => sleep( 50 ) && return "fast" );
result = anyOf( [ slow, fast ] ).get();
writeOutput( result );

```

Result: fast

### Race multiple computations

```java
results = anyOf( [
    () => sleep( 100 ) && return "A",
    () => sleep( 10 ) && return "B",
    () => sleep( 50 ) && return "C"
] ).get();
writeOutput( results );

```

Result: B

## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncRun](./AsyncRun.md)
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
