[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExecutorStatus`

Get a struct map of a specific executor and its stats.

If no parameters are passed, it will return a struct map of all executors and their stats.

## Method Signature

```
ExecutorStatus(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | The name of the executor to get. |  |

## Examples

### Get executor status information

```java
executorNew( "statusPool", "fixed", 4 );
status = executorStatus( "statusPool" );
writeOutput( status.containsKey( "name" ) );

```

Result: true

### Status includes pool type and thread count

```java
executorNew( "infoPool", "fixed", 8 );
status = executorStatus( "infoPool" );
writeOutput( status.name() & "," & status.type() );

```

Result: infoPool,FIXED

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
