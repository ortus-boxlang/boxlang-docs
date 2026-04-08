---
description: Configure runtime directory and file watchers
icon: binoculars
---

# Watchers

BoxLang includes a built-in `WatcherService` for monitoring directories and reacting to filesystem events. Watchers can be configured globally in `boxlang.json` and/or managed dynamically at runtime.

Use this when you want to:

- trigger hot-reload flows
- rebuild assets after file changes
- run custom automation from filesystem events

## Configuration Structure

The watcher configuration lives in the `watcher` segment of your `boxlang.json` file:

```json
{
  "watcher": {
    "recursive": true,
    "debounce": 0,
    "throttle": 0,
    "atomicWrites": true,
    "delay": 0,
    "errorThreshold": 10,
    "definitions": {}
  }
}
```

## Configuration Properties

### recursive

**Type:** `boolean`
**Default:** `true`

Whether watchers recurse into subdirectories.

```json
"recursive": true
```

### debounce

**Type:** `long` (milliseconds)
**Default:** `0`

Debounce window in milliseconds. When set above `0`, events are held until no new events arrive during the window.

```json
"debounce": 300
```

### throttle

**Type:** `long` (milliseconds)
**Default:** `0`

Throttle window in milliseconds. When set above `0`, only one event is emitted per window and additional events are dropped.

```json
"throttle": 1000
```

### atomicWrites

**Type:** `boolean`
**Default:** `true`

When enabled, noisy intermediate events from atomic save patterns (temp file + rename) are reduced.

```json
"atomicWrites": true
```

### delay

**Type:** `long` (milliseconds)
**Default:** `0`

Startup delay before watchers begin processing events.

```json
"delay": 2000
```

### errorThreshold

**Type:** `integer`
**Default:** `10`

Number of consecutive listener errors before a watcher auto-stops. Set to `0` to disable this auto-shutdown behavior.

```json
"errorThreshold": 5
```

### definitions

**Type:** `object`
**Default:** `{}`

Map of named watcher definitions that are auto-registered and started at runtime startup.

Each entry supports:

| Property         | Type            | Required | Description                                       |
| ---------------- | --------------- | -------- | ------------------------------------------------- |
| `paths`          | string or array | Yes      | Directory path or list of directories to watch    |
| `listener`       | string          | Yes      | BoxLang class path implementing listener behavior |
| `recursive`      | boolean         | No       | Per-watcher override for recursion                |
| `debounce`       | long            | No       | Per-watcher debounce override                     |
| `throttle`       | long            | No       | Per-watcher throttle override                     |
| `atomicWrites`   | boolean         | No       | Per-watcher atomic write filtering override       |
| `delay`          | long            | No       | Per-watcher startup delay override                |
| `errorThreshold` | integer         | No       | Per-watcher error threshold override              |

{% hint style="warning" %}
Inside `boxlang.json`, the `listener` must be a class name string. If you want to use closures or struct listeners, create watchers programmatically with `watcherNew()`.
{% endhint %}

{% hint style="info" %}
Programmatic `watcherNew()` listeners support closures, structs of closures, class name strings, and class instances.
{% endhint %}

## Definition Example

```json
{
  "watcher": {
    "recursive": true,
    "debounce": 300,
    "atomicWrites": true,
    "errorThreshold": 5,
    "definitions": {
      "hot-reload": {
        "paths": ["${user-dir}/src"],
        "listener": "app.listeners.HotReloadListener"
      },
      "assets": {
        "paths": [
          "${user-dir}/resources/css",
          "${user-dir}/resources/js"
        ],
        "recursive": false,
        "throttle": 500,
        "listener": "app.listeners.AssetPipelineListener"
      }
    }
  }
}
```

## Runtime Management

You can also create and manage watchers dynamically with BIFs:

- `watcherNew()`
- `watcherStart()`
- `watcherStop()`
- `watcherRestart()`
- `watcherList()`
- `watcherGet()`
- `watcherGetAll()`
- `watcherExists()`
- `watcherShutdown()`
- `watcherStopAll()`
- `watcherShutdownAll()`

For full usage examples, see [Directory + File Watchers](../../boxlang-framework/asynchronous-programming/directory-file-watchers.md).

## Related Configuration

- [Executors](executors.md)
- [Logging](logging.md)
- [Scheduler](scheduler.md)
