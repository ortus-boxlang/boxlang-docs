[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ThreadJoin`

Waits for the given thread object to finish running

## Method Signature

```
ThreadJoin(threadName=[string], timeout=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `threadName` | `string` | `false` | The name of the thread to join to the main thread.<br>                      This can be the name of the thread or a comma-separated list of thread names. |  |
| `timeout` | `numeric` | `false` | The maximum time in milliseconds to wait for the thread to finish running. If the thread does not finish running within this time, the join operation will be aborted. | `0` |

## Examples

### Wait for a thread to complete

```java
future = asyncRun( () => {
    sleep( 100 );
    return "finished";
} );
threadJoin( future.getThread() );
writeOutput( future.isDone() );

```

Result: true

### Join with a timeout

```java
future = asyncRun( () => {
    sleep( 50 );
    return "done";
} );
threadJoin( future.getThread(), 1000 );
writeOutput( future.get() );

```

Result: done

## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncAny](./AsyncAny.md)
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
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
