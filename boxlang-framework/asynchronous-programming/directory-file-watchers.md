---
description: Watch directories and react to file changes in real time
icon: binoculars
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

| Event      | Trigger                      | Explanation                                                 |
| ---------- | ---------------------------- | ----------------------------------------------------------- |
| `created`  | New file or directory exists | Fired when a new entry is added under a watched path.      |
| `modified` | Existing entry changes       | Fired when content or metadata updates are detected.       |
| `deleted`  | Existing entry is removed    | Fired when an entry that previously existed is deleted.    |
| `overflow` | Watch queue overflows        | Indicates dropped events; re-sync state if needed.         |

A listener receives an event payload that includes event kind, watched root, path details, and timestamp.

## Watcher Event Payload

Listeners receive a struct with these keys:

| Key            | Type     | Description                                                   |
| -------------- | -------- | ------------------------------------------------------------- |
| `kind`         | `string` | Event kind: `created`, `modified`, `deleted`, or `overflow`. |
| `path`         | `string` | Absolute path for the affected entry; blank for `overflow`.  |
| `relativePath` | `string` | Path relative to `watchRoot`; blank for `overflow`.          |
| `watchRoot`    | `string` | Registered watcher root; blank for `overflow`.               |
| `timestamp`    | `string` | ISO-8601 timestamp for when the event was emitted.           |

## How Watchers Work

Watchers monitor filesystem changes and route events to your listener code. Here's how the flow works:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   Filesystem Activity     ┃
┃  (create/modify/delete)   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            │
            ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Watcher Detection      ┃
┃  (monitors watch paths)   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            │
            ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   Debounce/Throttle       ┃
┃  (optional rate limiting) ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            │
            ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   Your Listener Logic     ┃
┃  (closure/struct/class)   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### Event Processing Pipeline

```
File Event → [ Queue ] → Debounce Timer → Listener Invocation
                           (250ms)              │
                                                ▼
                                         ┌─────────────┐
                                         │  Success?   │
                                         └─────────────┘
                                            │       │
                                         Yes│       │No
                                            │       │
                                            ▼       ▼
                                        Continue  Error
                                                  Counter++
```

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
).start()
```

## Watcher Listeners

BoxLang watchers support three listener patterns: **closures**, **struct of closures**, and **listener classes**. Choose the pattern that fits your complexity and reusability needs.

### 🔹 Closure Listener

The simplest approach—pass a closure that receives the event struct:

```js
watcher = watcherNew(
  name = "logWatcher",
  paths = [ "./logs" ],
  listener = ( event ) => {
    println( "📁 [" & event.kind & "] " & event.relativePath )

    if ( event.kind == "created" ) {
      println( "New file detected: " & event.path )
    }
  }
).start()
```

**Best for:** Quick prototypes, simple logging, and single-action handlers.

### 🔹 Struct of Closures

Map event kinds to specific handler closures for cleaner separation:

```js
watcher = watcherNew(
  name = "buildWatcher",
  paths = [ "./src" ],
  listener = {
    "onCreate": ( event ) => {
      println( "✨ New file: " & event.relativePath )
      runBuild( event.path )
    },
    "onModify": ( event ) => {
      println( "🔄 Modified: " & event.relativePath )
      rebuildAsset( event.path )
    },
    "onDelete": ( event ) => {
      println( "🗑️  Deleted: " & event.relativePath )
      cleanCache( event.path )
    },
    "overflow": ( event ) => {
      println( "⚠️  Event overflow detected—resyncing..." )
      fullBuildSync()
    },
    "onEvent": ( event ) => {
      // Optional catch-all for any event kind
      println( "📢 Event: [" & event.kind & "] " & event.relativePath )
    }
  },
  recursive = true,
  debounce = 300
).start()
```

**Best for:** Event-specific logic without creating a full class, medium complexity handlers.

### 🔹 Class Listener

For production systems for full control and error handling.  A class can maintain internal state, helper methods, and complex logic.
**It is mandatory to have a `onEvent()` method that receives the event struct.**

The available methods are:

| Method Name   | Required | Description                                                           |
| ------------- | -------- | --------------------------------------------------------------------- |
| `onEvent()`   | **Yes**  | Main event handler receiving all events. Must accept an event struct. |
| `onCreate()`  | No       | Called for `created` events. Receives event struct.                  |
| `onModify()`  | No       | Called for `modified` events. Receives event struct.                 |
| `onDelete()`  | No       | Called for `deleted` events. Receives event struct.                  |
| `onOverflow()` | No       | Called for `overflow` events. Receives event struct.                 |

{% hint style="info" %}
When specific event methods (`onCreate()`, `onModify()`, `onDelete()`, `onOverflow()`) are defined, they are called **in addition to** `onEvent()`. Use `onEvent()` for centralized routing or implement specific methods for targeted handling.
{% endhint %}

```js
// HotReloadListener.bx
class {

  property name="reloadCount" default="0";

  function onEvent( required struct event ) {
    // Central logging for all events
    writeLog( text: "Event received: #event.kind# for #event.relativePath#", level: "debug" )
  }

  function onCreate( required struct event ) {
    writeLog( text: "New file: #event.path#", level: "debug" )

    if ( event.path.endsWith( ".bx" ) ) {
      reloadComponent( event.path )
      variables.reloadCount++
    }
  }

  function onModify( required struct event ) {
    writeLog( text: "Modified file: #event.path#", level: "debug" )

    if ( event.path.endsWith( ".bx" ) ) {
      reloadComponent( event.path )
      variables.reloadCount++
    }
  }

  function onDelete( required struct event ) {
    writeLog( text: "Deleted file: #event.path#", level: "debug" )
    clearComponentCache( event.path )
  }

  function onOverflow( required struct event ) {
    writeLog( text: "Event overflow detected. Reload count: #variables.reloadCount#", level: "warn" )
    fullReload()
  }

  private function reloadComponent( required string path ) {
    // Component reload logic
    writeLog( text: "Reloading: #path#", level: "info" )
  }

  private function clearComponentCache( required string path ) {
    // Cache clearing logic
    writeLog( text: "Clearing cache for: #path#", level: "info" )
  }

  private function fullReload() {
    // Full application reload logic
    writeLog( text: "Performing full reload", level: "info" )
    variables.reloadCount = 0
  }

}
```

**Usage:**

```js
watcher = watcherNew(
  name = "hotReloadWatcher",
  paths = [ "./src" ],
  listener = new HotReloadListener(),
  recursive = true,
  debounce = 250,
  atomicWrites = true
).start()
```

**Best for:** Production systems, shared listener logic, complex error handling, testable code.

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

### getStats() Properties

The `getStats()` method returns a struct with the following keys:

| Property            | Type      | Description                                                    |
| ------------------- | --------- | -------------------------------------------------------------- |
| `name`              | `string`  | Watcher identifier                                             |
| `state`             | `string`  | Current watcher state (`CREATED`, `RUNNING`, `STOPPED`)        |
| `paths`             | `array`   | Array of watch root paths                                      |
| `recursive`         | `boolean` | Whether subdirectories are monitored                           |
| `debounce`          | `numeric` | Debounce delay in milliseconds (0 = disabled)                  |
| `throttle`          | `numeric` | Throttle limit in milliseconds (0 = disabled)                  |
| `atomicWrites`      | `boolean` | Whether atomic write detection is enabled                      |
| `errorThreshold`    | `numeric` | Maximum consecutive errors before watcher stops                |
| `consecutiveErrors` | `numeric` | Current count of consecutive errors since last success         |

**Example:**

```js
watcher = watcherNew(
  name = "myWatcher",
  paths = [ "./src" ],
  listener = ( event ) => println( event.kind )
).start()

stats = watcher.getStats()
println( "Watcher: #stats.name#" )
println( "State: #stats.state#" )
println( "Paths: #stats.paths.toList()#" )
println( "Recursive: #stats.recursive#" )
println( "Errors: #stats.consecutiveErrors# / #stats.errorThreshold#" )
```

## Best Practices

- Use `debounce` to avoid duplicate triggers from editor save behavior.
- Use `throttle` for noisy directories with heavy write bursts.
- Keep listener logic fast; hand off heavy work to async executors.
- Set `errorThreshold` to prevent infinite noisy failures.
- Prefer class listeners for production systems and shared logic.

{% hint style="info" %}
Watcher lifecycle and errors are logged through the runtime watcher logger. See [logging configuration](../../getting-started/configuration/logging.md) for logger tuning.
{% endhint %}
