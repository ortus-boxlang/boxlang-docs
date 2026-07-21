[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerGet`

Get a specific scheduler by name.

## Method Signature

```
SchedulerGet(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the scheduler to get. |  |

## Examples

### Get a registered scheduler by name

```java
schedulerNew( "myScheduler", 2 );
sched = schedulerGet( "myScheduler" );
writeOutput( sched.getName() );

```

Result: myScheduler

## Related

  * [SchedulerGetAll](./SchedulerGetAll.md)
  * [SchedulerList](./SchedulerList.md)
  * [SchedulerNew](./SchedulerNew.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerShutdown](./SchedulerShutdown.md)
  * [SchedulerStart](./SchedulerStart.md)
  * [SchedulerStats](./SchedulerStats.md)
