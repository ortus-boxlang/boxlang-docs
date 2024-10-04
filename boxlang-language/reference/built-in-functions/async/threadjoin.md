# ThreadJoin

Waits for the given thread object to finish running

## Method Signature

```
ThreadJoin(threadName=[string], timeout=[numeric])
```

### Arguments

| Argument     | Type      | Required | Description                                                                                                                                                            | Default |
| ------------ | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `threadName` | `string`  | `false`  | <p>The name of the thread to join to the main thread.<br>This can be the name of the thread or a comma-separated list of thread names.</p>                             |         |
| `timeout`    | `numeric` | `false`  | The maximum time in milliseconds to wait for the thread to finish running. If the thread does not finish running within this time, the join operation will be aborted. | `0`     |

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
* [ThreadNew](threadnew.md)
* [ThreadTerminate](threadterminate.md)
