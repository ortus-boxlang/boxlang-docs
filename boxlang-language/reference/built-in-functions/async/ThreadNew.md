[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ThreadNew`

Creates a new thread of execution based on the passed closure/lambda.

## Method Signature

```
ThreadNew(runnable=[function], attributes=[struct], name=[string], priority=[string], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `runnable` | `function` | `true` | The closure/lambda to execute in the new thread. |  |
| `attributes` | `struct` | `false` | A struct of data to bind into the thread's scope. | `{}` |
| `name` | `string` | `false` |  |  |
| `priority` | `string` | `false` | The priority of the thread. Possible values are "high", "low", and "normal". Default is "normal". | `normal` |
| `virtual` | `boolean` | `false` | If true, the thread will be a <a href="https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html">virtual thread</a>. Default is false. | `false` |

## Examples



## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncAny](./AsyncAny.md)
  * [AsyncRun](./AsyncRun.md)
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
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadTerminate](./ThreadTerminate.md)
