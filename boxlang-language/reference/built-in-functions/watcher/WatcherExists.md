[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherExists`

Checks whether a named watcher is currently registered in the watcher service.

## Method Signature

```
WatcherExists(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The unique watcher name to look up. |  |

## Examples

### Check if a file watcher exists by name

```java
watcherNew( "myWatcher", getTempDirectory() );
writeOutput( watcherExists( "myWatcher" ) );

```

Result: true

### Returns false for non-existent watcher

```java
writeOutput( watcherExists( "nonexistent" ) );

```

Result: false

## Related

  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherNew](./WatcherNew.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
