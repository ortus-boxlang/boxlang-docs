[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerGetAll`

Get a specific scheduler by name.

## Method Signature

```
SchedulerGetAll()
```

### Arguments

This function does not accept any arguments

## Examples

### Get all registered schedulers

```java
schedulerNew( "sched1", 2 );
schedulerNew( "sched2", 4 );
all = schedulerGetAll();
writeOutput( all.len() gte 2 );

```

Result: true

## Related

  * [SchedulerGet](./SchedulerGet.md)
  * [SchedulerList](./SchedulerList.md)
  * [SchedulerNew](./SchedulerNew.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerShutdown](./SchedulerShutdown.md)
  * [SchedulerStart](./SchedulerStart.md)
  * [SchedulerStats](./SchedulerStats.md)
