[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherStart`

Starts a registered watcher by name.

If the watcher is already running, the underlying watcher implementation returns
 the same instance without duplicating execution loops.

## Method Signature

```
WatcherStart(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The unique watcher name to start. |  |

## Examples

### Start a file watcher

```java
watcherNew( "startWatcher", getTempDirectory() );
watcherStart( "startWatcher" );
writeOutput( "started" );

```

Result: started

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
