[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WatcherNew`

Creates and registers a new watcher instance in the watcher service.

The watcher is registered but not started. Call {@code watcherStart( name )} to
 begin processing filesystem events or {@code start()} on the returned WatcherInstance.

 You can register three types of listeners, which BoxLang will automatically wrap into an IWatcherListener implementation:
 <ul>
 <li>{@link Function}: wrapped as a {@code ClosureListener}. Can only handle the {@code onEvent} method.</li>
 <li>{@link IStruct}: wrapped as a {@code StructListener}. Can handle {@code onEvent} and {@code onError} methods.</li>
 <li>{@link String}: treated as a class name and wrapped as a {@code ClassListener}. The class must implement {@code IWatcherListener}.</li>
 </ul>

 If {@code name} is omitted or blank, a unique watcher name is auto-generated.

## Method Signature

```
WatcherNew(name=[string], paths=[any], listener=[any], recursive=[boolean], debounce=[long], throttle=[long], atomicWrites=[boolean], delay=[long], errorThreshold=[integer], force=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | Optional watcher name. If blank, an auto-generated name is used. |  |
| `paths` | `any` | `true` | A directory path string or an array of directory path strings to watch. |  |
| `listener` | `any` | `true` | Listener definition: function, struct listener map, or listener class name string. |  |
| `recursive` | `boolean` | `false` | Whether to watch subdirectories recursively. | `true` |
| `debounce` | `long` | `false` | Debounce window in milliseconds. | `0` |
| `throttle` | `long` | `false` | Throttle window in milliseconds. | `0` |
| `atomicWrites` | `boolean` | `false` | Whether atomic write filtering is enabled. | `true` |
| `delay` | `long` | `false` | Startup delay in milliseconds. | `0` |
| `errorThreshold` | `integer` | `false` | Consecutive listener errors before auto-stop. | `10` |
| `force` | `boolean` | `false` | Whether to replace an existing watcher with the same name. | `false` |

## Examples

### Create a new file watcher

```java
w = watcherNew( "myWatcher", getTempDirectory() );
writeOutput( w.getName() );

```

Result: myWatcher

### Watcher with event callback

```java
w = watcherNew( "callbackWatcher", getTempDirectory(), ( event ) => {
    println( event.type() & " on " & event.path() );
} );
writeOutput( isObject( w ) );

```

Result: true

## Related

  * [WatcherExists](./WatcherExists.md)
  * [WatcherGet](./WatcherGet.md)
  * [WatcherGetAll](./WatcherGetAll.md)
  * [WatcherList](./WatcherList.md)
  * [WatcherRestart](./WatcherRestart.md)
  * [WatcherShutdown](./WatcherShutdown.md)
  * [WatcherShutdownAll](./WatcherShutdownAll.md)
  * [WatcherStart](./WatcherStart.md)
  * [WatcherStop](./WatcherStop.md)
  * [WatcherStopAll](./WatcherStopAll.md)
