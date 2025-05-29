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



## Related

  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [IsInThread](./IsInThread.md)
  * [FutureNew](./FutureNew.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [ExecutorList](./ExecutorList.md)
  * [ThreadTerminate](./ThreadTerminate.md)
  * [ThreadNew](./ThreadNew.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
