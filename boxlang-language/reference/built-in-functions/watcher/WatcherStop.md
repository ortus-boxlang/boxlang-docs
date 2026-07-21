[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherStop`

Stops a registered watcher by name.

This operation does not remove the watcher from the registry; it only transitions
 the watcher to a stopped state. Use {@code watcherShutdownAll()} to stop and unregister.

## Method Signature

```
WatcherStop(name=[string], force=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The unique watcher name to stop. |  |
| `force` | `boolean` | `false` | Whether to force an immediate stop by interrupting the watch loop and closing the WatchService, which may cause event loss but allows for faster shutdown in unresponsive scenarios. | `false` |

## Examples

### Stop a file watcher by name

```java
watcherNew( "stopWatcher", getTempDirectory() );
watcherStop( "stopWatcher" );
writeOutput( "stopped" );

```

Result: stopped

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStopAll](./WatcherStopAll.md)
