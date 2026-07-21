[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherGetAll`

Retrieves all registered watchers as a struct keyed by watcher name.

The returned struct is a snapshot of the service registry at invocation time,
 where each key is the watcher name and each value is the corresponding
 {@link ortus.boxlang.runtime.async.watchers.WatcherInstance}.

## Method Signature

```
WatcherGetAll()
```

### Arguments

This function does not accept any arguments

## Examples

### Get all registered file watchers

```java
watcherNew( "w1", getTempDirectory() );
watcherNew( "w2", getTempDirectory() );
all = watcherGetAll();
writeOutput( all.len() gte 2 );

```

Result: true

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
