[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ThreadInterrupt`

Interrupt the specific thread by name or all threads managed by the thread manager.

<p>
 Example:

 <pre>
 ThreadInterrupt( "myThread" );
 </pre>
 <p>
 This will interrupt the thread with the name "myThread".
 <p>
 Example:

 <pre>

 ThreadInterrupt();
 </pre>
 <p>
 This will interrupt all threads managed by the thread manager.

## Method Signature

```
ThreadInterrupt(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | The name of the thread to interrupt. If not passed, we interrupt ALL threads. |  |

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
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [isThreadAlive](./isThreadAlive.md)
