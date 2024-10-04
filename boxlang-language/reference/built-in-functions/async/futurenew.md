# FutureNew

Create a new BoxFuture object.

## Method Signature

```
FutureNew(value=[any], executor=[any])
```

### Arguments

| Argument   | Type  | Required | Description                                                                                                                                                                                                                  | Default |
| ---------- | ----- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `value`    | `any` | `false`  | <p>If passed, the value to set on the BoxFuture object as completed or it can be a lambda/closure<br>that will provide the value and it will be executed asynchronously, or it can be a native Java CompletableFuture</p>    |         |
| `executor` | `any` | `false`  | <p>The executor to use for the BoxFuture object. By default, the BoxFuture object will use the<br>default executor (ForkJoinPool.commonPool()). This can be the name of a named executor or a<br>custom executor object.</p> |         |

## Examples

## Related

* [ExecutorGet](executorget.md)
* [ExecutorHas](executorhas.md)
* [ExecutorList](executorlist.md)
* [ExecutorNew](executornew.md)
* [ExecutorShutdown](executorshutdown.md)
* [ExecutorStatus](executorstatus.md)
* [IsInThread](isinthread.md)
* [RunAsync](runasync.md)
* [ThreadJoin](threadjoin.md)
* [ThreadNew](threadnew.md)
* [ThreadTerminate](threadterminate.md)
