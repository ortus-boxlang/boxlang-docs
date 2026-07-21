[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `isThreadAlive`

Tests if this thread is alive.

A thread is alive if it has been started and has not yet terminated.
 <p>
 Example:

 <pre>
 if ( isThreadAlive( "myThread " ) ) {
     // wiat
 }
 </pre>

## Method Signature

```
isThreadAlive(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the thread to check |  |

## Examples

### Check if the current thread is alive

```java
alive = isThreadAlive();
writeOutput( isBoolean( alive ) );

```

Result: true

### Returns true when called from the main thread

```java
writeOutput( isThreadAlive() );

```

Result: true

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
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadCurrent](./ThreadCurrent.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
