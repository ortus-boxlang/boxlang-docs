[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherGet`

Retrieves a registered watcher instance by name.

Unlike {@code watcherExists()}, this operation is strict and fails when no
 watcher with the provided name exists.

## Method Signature

```
WatcherGet(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The unique watcher name to retrieve. |  |

## Examples

### Get a file watcher by name

```java
watcherNew( "myWatcher", getTempDirectory() );
w = watcherGet( "myWatcher" );
writeOutput( w.getName() );

```

Result: myWatcher

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
