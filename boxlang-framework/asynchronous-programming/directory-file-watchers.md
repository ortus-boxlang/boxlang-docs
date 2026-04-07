---
description: Watch directories and react to file changes in real time
icon: folder-tree
---

# Directory + File Watchers

BoxLang ships with a runtime `WatcherService` that lets you watch directories and respond to filesystem activity with BoxLang listeners.

Watchers are useful for:

- hot reload workflows
- build and asset pipelines
- ingest/ETL drop folders
- automation on create, modify, and delete events

## Event Model

Watchers emit events for:

- created
- modified
- deleted
- overflow

A listener receives an event payload that includes event kind, watched root, path details, and timestamp.

## Quick Start (Programmatic)

```js
watcher = watcherNew(
  name = "sourceWatcher",
  paths = [ "./src" ],
  listener = ( event ) => {
    println( "[" & event.kind & "] " & event.path )
  },
  recursive = true,
  debounce = 250,
  atomicWrites = true
)

watcherStart( "sourceWatcher" )
```

Stop and clean up:

```js
watcherStop( "sourceWatcher" )
watcherShutdownAll( true )
```

## Class Listener Example

For long-lived production watchers, use a class listener so logic is reusable and testable:

```js
class {

  function onEvent( required struct event ) {
    if ( event.kind == "MODIFIED" ) {
      println( "File changed: " & event.path )
    }
  }

  function onError( required string message, any exception ) {
    println( "Watcher error: " & message )
  }

}
```

Then reference the class in global configuration definitions.

{% hint style="info" %}
Listener callbacks receive event/error payloads only.
`watcherContext` is internal to the runtime and is not passed as a public callback argument.
{% endhint %}

## Global Startup Watchers

You can register auto-start watchers in `boxlang.json`:

```json
{
  "watcher": {
    "definitions": {
      "hot-reload": {
        "paths": [ "${user-dir}/src" ],
        "listener": "app.listeners.HotReloadListener",
        "debounce": 300,
        "recursive": true
      }
    }
  }
}
```

See [Watcher configuration](../../getting-started/configuration/watcher.md) for all options.

## Watcher BIFs

| BIF                    | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| `watcherNew()`         | Create and register a watcher             |
| `watcherStart()`       | Start a watcher                           |
| `watcherStop()`        | Stop a watcher                            |
| `watcherRestart()`     | Restart a watcher                         |
| `watcherGet()`         | Retrieve one watcher                      |
| `watcherGetAll()`      | Retrieve all watchers                     |
| `watcherList()`        | List watcher names                        |
| `watcherExists()`      | Check if watcher exists                   |
| `watcherShutdown()`    | Stop and unregister one watcher           |
| `watcherStopAll()`     | Stop all watchers without unregistering   |
| `watcherShutdownAll()` | Stop and unregister all watchers          |

## WatcherInstance API

`watcherNew()` and `watcherGet()` return a `WatcherInstance` object you can inspect and control directly.

- `start()` → `WatcherInstance`: Start this watcher.
- `stop( force )` → `WatcherInstance`: Stop this watcher (`force` defaults to `false`).
- `restart()` → `WatcherInstance`: Stop and start this watcher.
- `isRunning()` → `boolean`: True when watcher state is `RUNNING`.
- `isStopped()` → `boolean`: True when watcher state is `STOPPED`.
- `getState()` → `State`: Raw enum state (`CREATED`, `RUNNING`, `STOPPED`).
- `getStateAsString()` → `string`: String state value.
- `getName()` → `Key`: Watcher identifier.
- `getWatchPaths()` → `array`: Configured watch roots.
- `getListener()` → `IWatcherListener`: Listener instance.
- `getStats()` → `struct`: Snapshot of watcher configuration and runtime status.

`getStats()` includes:

- `name`
- `state`
- `paths`
- `recursive`
- `debounce`
- `throttle`
- `atomicWrites`
- `errorThreshold`
- `consecutiveErrors`

## Watcher Event Payload

Listeners receive a struct with these keys:

- `kind` (`created`, `modified`, `deleted`, `overflow`)
- `path` (absolute path, blank string for overflow)
- `relativePath` (relative to watch root, blank string for overflow)
- `watchRoot` (registered root, blank string for overflow)
- `timestamp` (ISO-8601 timestamp)

## Best Practices

- Use `debounce` to avoid duplicate triggers from editor save behavior.
- Use `throttle` for noisy directories with heavy write bursts.
- Keep listener logic fast; hand off heavy work to async executors.
- Set `errorThreshold` to prevent infinite noisy failures.
- Prefer class listeners for production systems and shared logic.

{% hint style="info" %}
Watcher lifecycle and errors are logged through the runtime watcher logger. See [logging configuration](../../getting-started/configuration/logging.md) for logger tuning.
{% endhint %}
