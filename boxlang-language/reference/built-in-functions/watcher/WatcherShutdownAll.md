[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherShutdownAll`

Stops all watchers and removes them from the watcher registry.

This is the destructive bulk operation for watcher lifecycle management.
 After this call, all previous watcher registrations are cleared and must be
 recreated before use.

## Method Signature

```
WatcherShutdownAll(force=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `force` | `boolean` | `false` | Whether the shutdown should be treated as a forced shutdown. | `false` |

## Examples

### Shutdown all registered file watchers

```java
watcherNew( "w1", getTempDirectory() );
watcherNew( "w2", getTempDirectory() );
watcherShutdownAll();
writeOutput( "all shutdown" );

```

Result: all shutdown

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
