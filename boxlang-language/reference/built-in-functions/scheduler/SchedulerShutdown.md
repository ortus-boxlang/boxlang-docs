[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerShutdown`

Shutdown a scheduler by name.

<p>
 The default will do a graceful shutdown, but if the force argument is set to true,
 it will force shutdown the scheduler.
 <p>
 If the timeout argument is set, it will wait for the specified amount of time in seconds
 before forcing the shutdown. The default is 30 seconds.

## Method Signature

```
SchedulerShutdown(name=[string], force=[boolean], timeout=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the scheduler to shutdown. |  |
| `force` | `boolean` | `false` | If true, will force shutdown the scheduler. Default is false. | `false` |
| `timeout` | `integer` | `false` | The timeout in seconds to wait for the scheduler to shutdown gracefully. Default is 30 seconds. | `30` |

## Examples



## Related

  * [SchedulerGet](./SchedulerGet.md)
  * [SchedulerGetAll](./SchedulerGetAll.md)
  * [SchedulerList](./SchedulerList.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerStart](./SchedulerStart.md)
  * [SchedulerStats](./SchedulerStats.md)
