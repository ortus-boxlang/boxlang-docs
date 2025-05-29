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



## Related

  * [RunAsync](./RunAsync.md)
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
  * [isThreadAlive](./isThreadAlive.md)
