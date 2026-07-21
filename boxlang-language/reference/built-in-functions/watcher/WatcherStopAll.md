[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherStopAll`

Stops all registered watchers in the watcher service.

Watchers remain registered after this call and can be started again later.

## Method Signature

```
WatcherStopAll(force=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `force` | `boolean` | `false` |  | `false` |

## Examples

### Stop all registered file watchers

```java
watcherNew( "w1", getTempDirectory() );
watcherNew( "w2", getTempDirectory() );
watcherStopAll();
writeOutput( "all stopped" );

```

Result: all stopped

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
  * [WatcherStop](./WatcherStop.md)
