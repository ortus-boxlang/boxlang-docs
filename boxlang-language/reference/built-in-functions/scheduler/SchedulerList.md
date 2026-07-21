[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerList`

List all the schedulers registered in the system.

## Method Signature

```
SchedulerList()
```

### Arguments

This function does not accept any arguments

## Examples

### List all registered schedulers

```java
schedulerNew( "listSched", 2 );
list = schedulerList();
writeOutput( isArray( list ) );

```

Result: true

## Related

  * [SchedulerGet](./SchedulerGet.md)
  * [SchedulerGetAll](./SchedulerGetAll.md)
  * [SchedulerNew](./SchedulerNew.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerShutdown](./SchedulerShutdown.md)
  * [SchedulerStart](./SchedulerStart.md)
  * [SchedulerStats](./SchedulerStats.md)
