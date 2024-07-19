[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExecutorShutdown`

Shuts down an executor by name.

By default
 the executors are shutdown gracefully. However, if you want to force the shutdown
 you can set the force argument to true. If you want to wait for the executor to shutdown
 you can set the timeout argument to the number of milliseconds to wait.

## Method Signature

```
ExecutorShutdown(name=[string], force=[boolean], timeout=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the executor to shutdown |  |
| `force` | `boolean` | `true` | Whether to force the shutdown, default is false | `false` |
| `timeout` | `numeric` | `true` | The number of milliseconds to wait for the executor to shutdown | `0` |

## Examples



## Related

  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [FutureNew](./FutureNew.md)
  * [IsInThread](./IsInThread.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadTerminate](./ThreadTerminate.md)
