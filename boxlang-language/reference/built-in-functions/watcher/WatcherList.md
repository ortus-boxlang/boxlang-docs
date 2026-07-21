[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherList`

Lists the names of all watchers currently registered in the watcher service.

This returns only watcher identifiers and does not include watcher metadata.
 Use {@code watcherGetAll()} when you need full watcher instances.

## Method Signature

```
WatcherList()
```

### Arguments

This function does not accept any arguments

## Examples

### List all registered file watchers

```java
watcherNew( "listWatcher", getTempDirectory() );
list = watcherList();
writeOutput( isArray( list ) );

```

Result: true

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
