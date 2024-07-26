[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FutureNew`

Create a new BoxFuture object.

## Method Signature

```
FutureNew(value=[any], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `false` | If passed, the value to set on the BoxFuture object as completed or it can be a lambda/closure<br>                 that will provide the value and it will be executed asynchronously, or it can be a native Java CompletableFuture |  |
| `executor` | `any` | `false` | The executor to use for the BoxFuture object. By default, the BoxFuture object will use the<br>                    default executor (ForkJoinPool.commonPool()). This can be the name of a named executor or a<br>                    custom executor object. |  |

## Examples



## Related

  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [IsInThread](./IsInThread.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
