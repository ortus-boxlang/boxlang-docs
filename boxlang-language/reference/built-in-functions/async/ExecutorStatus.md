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



## Related

  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [IsInThread](./IsInThread.md)
  * [FutureNew](./FutureNew.md)
  * [ExecutorList](./ExecutorList.md)
  * [ThreadTerminate](./ThreadTerminate.md)
  * [ThreadNew](./ThreadNew.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [isThreadAlive](./isThreadAlive.md)
