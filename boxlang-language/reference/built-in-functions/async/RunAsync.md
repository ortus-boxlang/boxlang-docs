[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `RunAsync`

Executes the given code asynchronously and returns to you a BoxFuture object that you can use to interact with the
 asynchronously executed code.

A BoxFuture is a subclass of CompletableFuture.

## Method Signature

```
RunAsync(callback=[function], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function` | `true` | The code to execute asynchronously, this can be a closure or lambda. |  |
| `executor` | `any` | `false` | The executor to use for the asynchronous execution. This can be an instance of an Executor class, or the name of a registered executor in the AsyncService. |  |

## Examples



## Related

  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [FutureNew](./FutureNew.md)
  * [IsInThread](./IsInThread.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
