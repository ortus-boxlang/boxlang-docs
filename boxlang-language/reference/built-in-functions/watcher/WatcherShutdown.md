[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherShutdown`

Stops and removes a registered watcher from the watcher registry.

This is the destructive single-watcher lifecycle operation. After this call,
 the watcher is no longer registered and must be recreated before use.

## Method Signature

```
WatcherShutdown(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The unique watcher name to shut down. |  |

## Examples

### Shutdown a file watcher by name

```java
watcherNew( "shutdownWatcher", getTempDirectory() );
watcherShutdown( "shutdownWatcher" );
writeOutput( "shutdown" );

```

Result: shutdown

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
