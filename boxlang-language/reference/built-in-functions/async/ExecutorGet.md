# ExecutorGet

Get an executor by name.

If no name is provided, the default executor is returned "io-tasks".\
BoxLang registers 3 executors by default for you:

* **io-tasks**: For IO bound tasks, which are not scheduled and uses virtual threads
* **cpu-tasks**: For CPU bound tasks, which can be scheduled. (20 threads by default)
* **scheduled-tasks**: For scheduled tasks (20 threads by default)

## Method Signature

```
ExecutorGet(name=[string])
```

### Arguments

| Argument | Type     | Required | Description                      | Default    |
| -------- | -------- | -------- | -------------------------------- | ---------- |
| `name`   | `string` | `true`   | The name of the executor to get. | `io-tasks` |

## Examples

## Related

* [ExecutorHas](ExecutorHas.md)
* [ExecutorList](ExecutorList.md)
* [ExecutorNew](ExecutorNew.md)
* [ExecutorShutdown](ExecutorShutdown.md)
* [ExecutorStatus](ExecutorStatus.md)
* [FutureNew](FutureNew.md)
* [IsInThread](IsInThread.md)
* [isThreadAlive](isThreadAlive.md)
* [IsThreadInterrupted](IsThreadInterrupted.md)
* [RunAsync](RunAsync.md)
* [ThreadInterrupt](ThreadInterrupt.md)
* [ThreadJoin](ThreadJoin.md)
* [ThreadNew](ThreadNew.md)
* [ThreadTerminate](ThreadTerminate.md)
