# Runtime Events

These events relate to the overall lifecycle of the BoxLang runtime itself — from startup and configuration loading through to shutdown. They are announced on the **global interceptor pool**.

> **Note:** `onRuntimeConfigurationLoad` exists in `BoxEvent` but is not currently announced anywhere in the core runtime. Do not rely on it until this is resolved.

| Event Name                    | Cancellable | Description                                                                                  |
| ----------------------------- | :---------: | -------------------------------------------------------------------------------------------- |
| `onRuntimeStart`              |     No      | Fired when the runtime has fully started and is ready to process requests.                   |
| `onRuntimeShutdown`           |     No      | Fired at the beginning of the runtime shutdown sequence.                                     |
| `onRuntimeBoxContextStartup`  |     No      | Fired after the root `RuntimeBoxContext` and `server` scope are initialized.                 |
| `onServerScopeCreation`       |     No      | Fired when the `server` scope is being initialized.                                          |
| `onConfigurationLoad`         |     No      | Fired after the core `boxlang.json` configuration is loaded.                                 |
| `onConfigurationOverrideLoad` |     No      | Fired each time a configuration override file is applied.                                    |
| `onParse`                     |   **Yes**   | Fired after every parse of a BoxLang source file, string, or expression. The `result` can be replaced by an interceptor. |
| `onMissingMapping`            |   **Yes**   | Fired when a path cannot be resolved to a mapping. An interceptor can supply the resolved path. |
| `onPreSourceInvoke`           |     No      | Fired before a BoxLang script source is invoked.                                             |
| `onPostSourceInvoke`          |     No      | Fired after a BoxLang script source finishes (always, even on exception).                    |

* [`onRuntimeStart`](runtime-events.md#onruntimestart)
* [`onRuntimeShutdown`](runtime-events.md#onruntimeshutdown)
* [`onRuntimeBoxContextStartup`](runtime-events.md#onruntimeboxcontextstartup)
* [`onServerScopeCreation`](runtime-events.md#onserverscopecreation)
* [`onConfigurationLoad`](runtime-events.md#onconfigurationload)
* [`onConfigurationOverrideLoad`](runtime-events.md#onconfigurationoverrideload)
* [`onParse`](runtime-events.md#onparse)
* [`onMissingMapping`](runtime-events.md#onmissingmapping)
* [`onPreSourceInvoke`](runtime-events.md#onpresourceinvoke)
* [`onPostSourceInvoke`](runtime-events.md#onpostsourceinvoke)

## onRuntimeStart

Fired once the runtime has completed its full startup sequence — all services are running, modules are loaded, and the runtime is ready to process requests. No event data is passed.

### Data Structure

_None_

### Example

```groovy
class myListener{
	function onRuntimeStart( struct data ){
		// Runtime is fully up — safe to interact with all services
	}
}
```

## onRuntimeShutdown

Fired at the very beginning of the shutdown sequence, before any services are stopped. Use this to perform cleanup or flush state before the runtime tears down.

### Data Structure

| Data Key  | Type         | Description                                       |
| --------- | ------------ | ------------------------------------------------- |
| `runtime` | `BoxRuntime` | The runtime instance that is shutting down.       |
| `force`   | `Boolean`    | Whether this is a forced (non-graceful) shutdown. |

### Example

```groovy
class myListener{
	function onRuntimeShutdown( struct data ){
		var runtime = data.runtime;
		var force   = data.force;
		// Flush state, close connections, etc.
	}
}
```

## onRuntimeBoxContextStartup

Fired after the root `RuntimeBoxContext` has been initialized and the `server` scope is fully seeded. This is the earliest point at which the full runtime context and server scope are available to interceptors.

### Data Structure

| Data Key        | Type                | Description                              |
| --------------- | ------------------- | ---------------------------------------- |
| `context`       | `RuntimeBoxContext` | The root runtime box context.            |
| `configuration` | `IStruct`           | The active runtime configuration struct. |
| `serverScope`   | `ServerScope`       | The initialized `server` scope.          |

### Example

```groovy
class myListener{
	function onRuntimeBoxContextStartup( struct data ){
		var context     = data.context;
		var config      = data.configuration;
		var serverScope = data.serverScope;
		// Augment the server scope, read config, etc.
	}
}
```

## onServerScopeCreation

Fired during initialization of the `server` scope, before it is fully populated. Use this to add custom keys or metadata to the server scope at startup.

### Data Structure

| Data Key | Type          | Description                           |
| -------- | ------------- | ------------------------------------- |
| `scope`  | `ServerScope` | The `server` scope being initialized. |
| `name`   | `String`      | The name of the scope (`"server"`).   |

### Example

```groovy
class myListener{
	function onServerScopeCreation( struct data ){
		// Add custom keys to the server scope
		data.scope[ "myKey" ] = "myValue";
	}
}
```

## onConfigurationLoad

Fired after the core `boxlang.json` configuration file has been loaded and deserialized. This fires before any override files are applied, so the configuration at this point represents the base defaults.

### Data Structure

| Data Key | Type                   | Description                           |
| -------- | ---------------------- | ------------------------------------- |
| `config` | `BoxLangConfiguration` | The loaded core configuration object. |

### Example

```groovy
class myListener{
	function onConfigurationLoad( struct data ){
		var config = data.config;
		// Inspect or mutate base configuration before overrides are applied
	}
}
```

## onConfigurationOverrideLoad

Fired each time an override configuration file is merged into the active configuration. This may fire multiple times — once for the runtime home override (`${boxlang-home}/config/boxlang.json`) and again for any CLI/ENV-supplied config path.

### Data Structure

| Data Key         | Type                   | Description                                              |
| ---------------- | ---------------------- | -------------------------------------------------------- |
| `config`         | `BoxLangConfiguration` | The configuration object after the override was applied. |
| `configOverride` | `String`               | The absolute path of the override file that was applied. |

### Example

```groovy
class myListener{
	function onConfigurationOverrideLoad( struct data ){
		var config         = data.config;
		var configOverride = data.configOverride;
		// React to which override file was applied
	}
}
```

## onParse

Fired after every parse operation — whether parsing a file, a code string, an expression, or a statement. The `result` key in the event data is **mutable**: an interceptor can replace it with a modified `ParsingResult` to alter the AST before execution.

This event fires on every parse, including during compilation, so interceptors should be lightweight.

`ParsingResult` contains: `root` (`BoxNode` — the AST root), `issues` (`List<Issue>`), and `comments` (`List<BoxComment>`).

### Data Structure (file parse)

| Data Key | Type            | Description                                               |
| -------- | --------------- | --------------------------------------------------------- |
| `file`   | `File`          | The source file that was parsed.                          |
| `result` | `ParsingResult` | The result of the parse. **Replaceable by interceptors.** |

### Data Structure (string / expression parse)

| Data Key | Type            | Description                                               |
| -------- | --------------- | --------------------------------------------------------- |
| `code`   | `String`        | The source code string that was parsed.                   |
| `result` | `ParsingResult` | The result of the parse. **Replaceable by interceptors.** |

### Example

```groovy
class myListener{
	function onParse( struct data ){
		var result = data.result;
		// Inspect or replace the AST
		// data.result = myModifiedResult;
	}
}
```

## onMissingMapping

Fired when a path cannot be resolved against any registered mapping. An interceptor can supply a `ResolvedFilePath` to handle the resolution — if `resolvedFilePath` is set in the event data, the runtime uses it and skips the fallback to the root mapping.

This makes it possible for modules to implement custom path resolution strategies (e.g., virtual filesystems, classpath lookups).

### Data Structure

| Data Key           | Type               | Description                                                                                         |
| ------------------ | ------------------ | --------------------------------------------------------------------------------------------------- |
| `path`             | `String`           | The path that could not be resolved.                                                                |
| `resolvedFilePath` | `ResolvedFilePath` | Initially `null`. Set this in your interceptor to provide a resolved path and short-circuit the fallback. |

### Example

```groovy
class myListener{
	function onMissingMapping( struct data ){
		if ( data.path.startsWith( "/virtual/" ) ) {
			// Supply a resolved path to short-circuit the fallback
			data.resolvedFilePath = myResolvedFilePath;
		}
	}
}
```

## onPreSourceInvoke

Fired immediately before a BoxLang script source (`BoxScript`) is invoked. Use this to inject context, log execution, or set up pre-invocation state.

### Data Structure

| Data Key  | Type          | Description                                   |
| --------- | ------------- | --------------------------------------------- |
| `context` | `IBoxContext` | The context in which the source is executing. |
| `source`  | `BoxScript`   | The script source about to be invoked.        |

### Example

```groovy
class myListener{
	function onPreSourceInvoke( struct data ){
		var context = data.context;
		var source  = data.source;
		// Set up pre-invocation state or logging
	}
}
```

## onPostSourceInvoke

Fired after a BoxLang script source finishes executing — in a `finally` block, so this fires whether the invocation succeeded or threw an exception. Use this for cleanup, metrics, or post-execution logic.

### Data Structure

| Data Key  | Type          | Description                                  |
| --------- | ------------- | -------------------------------------------- |
| `context` | `IBoxContext` | The context in which the source executed.    |
| `source`  | `BoxScript`   | The script source that was invoked.          |

### Example

```groovy
class myListener{
	function onPostSourceInvoke( struct data ){
		var context = data.context;
		var source  = data.source;
		// Cleanup, metrics collection, etc.
	}
}
```
