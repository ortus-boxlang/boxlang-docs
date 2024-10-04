# ExecutorStatus

Get a struct map of a specific executor and its stats.

If no parameters are passed, it will return a struct map of all executors and their stats.

## Method Signature

```
ExecutorStatus(name=[string])
```

### Arguments

| Argument | Type     | Required | Description                      | Default |
| -------- | -------- | -------- | -------------------------------- | ------- |
| `name`   | `string` | `false`  | The name of the executor to get. |         |

## Examples

## Related

* [ExecutorGet](executorget.md)
* [ExecutorHas](executorhas.md)
* [ExecutorList](executorlist.md)
* [ExecutorNew](executornew.md)
* [ExecutorShutdown](executorshutdown.md)
* [FutureNew](futurenew.md)
* [IsInThread](isinthread.md)
* [RunAsync](runasync.md)
* [ThreadJoin](threadjoin.md)
* [ThreadNew](threadnew.md)
* [ThreadTerminate](threadterminate.md)
