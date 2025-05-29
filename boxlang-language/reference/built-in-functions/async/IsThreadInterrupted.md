[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsThreadInterrupted`

Verifies if the current thread is interrupted or not.

You can also pass in a thread name to check if that thread is interrupted.
 <p>
 Example:

 <pre>
 if ( !IsThreadInterrupted() ) {
     // Do work
 }
 </pre>

## Method Signature

```
IsThreadInterrupted(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | The name of the thread to check or empty for the current thread. |  |

## Examples



## Related

  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
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
  * [isThreadAlive](./isThreadAlive.md)
