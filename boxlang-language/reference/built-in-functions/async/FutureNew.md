[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FutureNew`

Create a new BoxFuture object.

## Method Signature

```
FutureNew(value=[any], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `false` | If passed, the value to set on the BoxFuture object as completed or it can be a lambda/closure<br>                 that will provide the value and it will be executed asynchronously, or it can be a native Java CompletableFuture |  |
| `executor` | `any` | `false` | The executor to use for the BoxFuture object. By default, the BoxFuture object will use the<br>                    default executor (ForkJoinPool.commonPool()). This can be the name of a named executor or a<br>                    custom executor object. |  |

## Examples

### Create a new future for async execution

```java
future = futureNew( () => 42 );
writeOutput( future.get() );

```

Result: 42

### Create a completed future with a value

```java
future = futureNew( "already done" );
writeOutput( future.isDone() & "," & future.get() );

```

Result: true,already done

### Create an incomplete future and complete it later

```java
future = futureNew();
future.complete( "later" );
writeOutput( future.get() );

```

Result: later

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
  * [IsInThread](./IsInThread.md)
  * [isThreadAlive](./isThreadAlive.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadCurrent](./ThreadCurrent.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
