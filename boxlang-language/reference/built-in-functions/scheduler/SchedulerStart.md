[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerStart`

Create, register and start a scheduler with the given instantiation class path.

<p>
 The className would be the same as instantiang the class via <code>new {className}</code>.

## Method Signature

```
SchedulerStart(className=[string], name=[string], force=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `className` | `string` | `true` | The className to the scheduler class to be instantiated: Example: "models.myapp.MyScheduler" |  |
| `name` | `string` | `false` | The name of the scheduler to start, which overrides whatever is in the class. |  |
| `force` | `boolean` | `false` | If true, will force start the scheduler. Default is true | `true` |

## Examples



## Related

  * [SchedulerGet](./SchedulerGet.md)
  * [SchedulerGetAll](./SchedulerGetAll.md)
  * [SchedulerList](./SchedulerList.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerShutdown](./SchedulerShutdown.md)
  * [SchedulerStats](./SchedulerStats.md)
