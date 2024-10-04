# RunAsync

Executes the given code asynchronously and returns to you a BoxFuture object that you can use to interact with the asynchronously executed code.

A BoxFuture is a subclass of CompletableFuture.

## Method Signature

```
RunAsync(callback=[function], executor=[any])
```

### Arguments

| Argument   | Type       | Required | Description                                                                                                                                                 | Default |
| ---------- | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `callback` | `function` | `true`   | The code to execute asynchronously, this can be a closure or lambda.                                                                                        |         |
| `executor` | `any`      | `false`  | The executor to use for the asynchronous execution. This can be an instance of an Executor class, or the name of a registered executor in the AsyncService. |         |

## Examples

## Related

* [ExecutorGet](executorget.md)
* [ExecutorHas](executorhas.md)
* [ExecutorList](executorlist.md)
* [ExecutorNew](executornew.md)
* [ExecutorShutdown](executorshutdown.md)
* [ExecutorStatus](executorstatus.md)
* [FutureNew](futurenew.md)
* [IsInThread](isinthread.md)
* [ThreadJoin](threadjoin.md)
* [ThreadNew](threadnew.md)
* [ThreadTerminate](threadterminate.md)
