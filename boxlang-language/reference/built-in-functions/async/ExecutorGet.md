[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExecutorGet`

Get an executor by name.

If no name is provided, the default executor is returned "io-tasks".
 BoxLang registers 3 executors by default for you:
 <ul>
 <li><strong>io-tasks</strong>: For IO bound tasks, which are not scheduled and uses virtual threads</li>
 <li><strong>cpu-tasks</strong>: For CPU bound tasks, which can be scheduled. (20 threads by default)</li>
 <li><strong>scheduled-tasks</strong>: For scheduled tasks (20 threads by default)</li>
 </ul>

## Method Signature

```
ExecutorGet(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the executor to get. | `io-tasks` |

## Examples



## Related

  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
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
