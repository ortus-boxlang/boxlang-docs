[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerNew`

Create and register a new scheduler.

## Method Signature

```
SchedulerNew(name=[string], timezone=[string], force=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the scheduler to create. |  |
| `timezone` | `string` | `false` | The timezone for the scheduler. Defaults to the system default timezone. |  |
| `force` | `boolean` | `false` | Whether to replace an existing scheduler with the same name. Defaults to false. | `false` |

## Examples

### Create a new scheduler

```java
sched = schedulerNew( "myScheduler", 4 );
writeOutput( sched.getName() );

```

Result: myScheduler

### Scheduler with custom thread count

```java
sched = schedulerNew( "heavyTasks", 10 );
writeOutput( isObject( sched ) );

```

Result: true

## Related

  * [SchedulerGet](./SchedulerGet.md)
  * [SchedulerGetAll](./SchedulerGetAll.md)
  * [SchedulerList](./SchedulerList.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerShutdown](./SchedulerShutdown.md)
  * [SchedulerStart](./SchedulerStart.md)
  * [SchedulerStats](./SchedulerStats.md)
