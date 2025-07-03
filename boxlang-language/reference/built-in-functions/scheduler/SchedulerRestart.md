# SchedulerRestart

Restart a scheduler by name.

The default will do a graceful shutdown, but if the force argument is set to true,\
it will force shutdown the scheduler.

If the timeout argument is set, it will wait for the specified amount of time in seconds\
before forcing the shutdown. The default is 30 seconds.

## Method Signature

```
SchedulerRestart(name=[string], force=[boolean], timeout=[integer])
```

### Arguments

| Argument  | Type      | Required | Description                                                                                    | Default |
| --------- | --------- | -------- | ---------------------------------------------------------------------------------------------- | ------- |
| `name`    | `string`  | `true`   | The name of the scheduler to restart.                                                          |         |
| `force`   | `boolean` | `false`  | If true, will force restart the scheduler. Default is false.                                   | `false` |
| `timeout` | `integer` | `false`  | The timeout in seconds to wait for the scheduler to restart gracefully. Default is 30 seconds. | `30`    |

## Examples

## Related

* [SchedulerGet](SchedulerGet.md)
* [SchedulerGetAll](SchedulerGetAll.md)
* [SchedulerList](SchedulerList.md)
* [SchedulerShutdown](SchedulerShutdown.md)
* [SchedulerStart](SchedulerStart.md)
* [SchedulerStats](SchedulerStats.md)
