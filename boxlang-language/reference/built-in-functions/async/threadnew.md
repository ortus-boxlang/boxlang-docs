# ThreadNew

Creates a new thread of execution based on the passed closure/lambda.

## Method Signature

```
ThreadNew(runnable=[function], attributes=[struct], name=[string], priority=[string])
```

### Arguments

| Argument     | Type       | Required | Description                                                                                       | Default  |
| ------------ | ---------- | -------- | ------------------------------------------------------------------------------------------------- | -------- |
| `runnable`   | `function` | `true`   | The closure/lambda to execute in the new thread.                                                  |          |
| `attributes` | `struct`   | `false`  | A struct of data to bind into the thread's scope.                                                 | `{}`     |
| `name`       | `string`   | `false`  |                                                                                                   |          |
| `priority`   | `string`   | `false`  | The priority of the thread. Possible values are "high", "low", and "normal". Default is "normal". | `normal` |

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
* [RunAsync](runasync.md)
* [ThreadJoin](threadjoin.md)
* [ThreadTerminate](threadterminate.md)
