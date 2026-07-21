[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherRestart`

Restarts a registered watcher by performing {@code stop()} then {@code start()}.

This is useful when refreshing watcher state after path changes or listener updates.

## Method Signature

```
WatcherRestart(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The unique watcher name to restart. |  |

## Examples

### Restart a file watcher

```java
watcherNew( "restartWatcher", getTempDirectory() );
watcherRestart( "restartWatcher" );
writeOutput( "restarted" );

```

Result: restarted

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
