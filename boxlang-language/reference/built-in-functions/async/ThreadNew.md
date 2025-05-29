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
  * [ExecutorHas](./ExecutorHas.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [isThreadAlive](./isThreadAlive.md)
