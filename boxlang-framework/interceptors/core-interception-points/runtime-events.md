# Runtime Events

These events relate to the overall lifecycle of the BoxLang runtime itself — from startup and configuration loading through to shutdown. They are announced on the **global interceptor pool**.

| Event Name                    | Cancellable | Description                                                                 |
| ----------------------------- | :---------: | --------------------------------------------------------------------------- |
| `onRuntimeStart`              |     No      | Fired when the runtime has fully started and is ready to process requests.  |
| `onRuntimeShutdown`           |     No      | Fired at the beginning of the runtime shutdown sequence.                    |
| `onRuntimeBoxContextStartup`  |     No      | Fired after the root `RuntimeBoxContext` and `server` scope are initialized.|
| `onServerScopeCreation`       |     No      | Fired when the `server` scope is being initialized.                         |
| `onConfigurationLoad`         |     No      | Fired after the core `boxlang.json` configuration is loaded.                |
| `onConfigurationOverrideLoad` |     No      | Fired each time a configuration override file is applied.                   |
| `onParse`                     |   **Yes**   | Fired after every parse of a BoxLang source file, string, or expression. The `result` can be replaced by an interceptor.   |
| `onMissingMapping`            |   **Yes**   | Fired when a path cannot be resolved to a mapping. An interceptor can supply the resolved path. |
| `onPreSourceInvoke`           |     No      | Fired before a BoxLang script source is invoked.                            |
| `onPostSourceInvoke`          |     No      | Fired after a BoxLang script source finishes (always, even on exception).   |

> **Note:** `onRuntimeConfigurationLoad` exists in `BoxEvent` but is not currently announced anywhere in the core runtime. Do not rely on it until this is resolved.

---

## `onRuntimeStart`

Fired once the runtime has completed its full startup sequence — all services are running, modules are loaded, and the runtime is ready to process requests. No event data is passed.

**Event Data:** _None_

**Example:**

```java
interceptorService.register( data -> {
    // Runtime is fully up — safe to interact with all services
    return false;
}, BoxEvent.ON_RUNTIME_START.key() );
```

---

## `onRuntimeShutdown`

Fired at the very beginning of the shutdown sequence, before any services are stopped. Use this to perform cleanup or flush state before the runtime tears down.

**Event Data:**

| Key      | Type         | Description                                           |
| -------- | ------------ | ----------------------------------------------------- |
| `runtime`| `BoxRuntime` | The runtime instance that is shutting down.           |
| `force`  | `Boolean`    | Whether this is a forced (non-graceful) shutdown.     |

**Example:**

```java
interceptorService.register( data -> {
    BoxRuntime runtime = ( BoxRuntime ) data.get( "runtime" );
    boolean    force   = ( boolean ) data.get( "force" );
    // flush state, close connections, etc.
    return false;
}, BoxEvent.ON_RUNTIME_SHUTDOWN.key() );
```

---

## `onRuntimeBoxContextStartup`

Fired after the root `RuntimeBoxContext` has been initialized and the `server` scope is fully seeded. This is the earliest point at which the full runtime context and server scope are available to interceptors.

**Event Data:**

| Key           | Type                 | Description                                           |
| ------------- | -------------------- | ----------------------------------------------------- |
| `context`     | `RuntimeBoxContext`  | The root runtime box context.                         |
| `configuration`| `IStruct`           | The active runtime configuration struct.              |
| `serverScope` | `ServerScope`        | The initialized `server` scope.                       |

**Example:**

```java
interceptorService.register( data -> {
    RuntimeBoxContext context     = ( RuntimeBoxContext ) data.get( "context" );
    IStruct           config      = ( IStruct ) data.get( "configuration" );
    ServerScope       serverScope = ( ServerScope ) data.get( "serverScope" );
    // Augment the server scope, read config, etc.
    return false;
}, BoxEvent.ON_RUNTIME_BOX_CONTEXT_STARTUP.key() );
```

---

## `onServerScopeCreation`

Fired during initialization of the `server` scope, before it is fully populated. Use this to add custom keys or metadata to the server scope at startup.

**Event Data:**

| Key    | Type          | Description                          |
| ------ | ------------- | ------------------------------------ |
| `scope`| `ServerScope` | The `server` scope being initialized.|
| `name` | `String`      | The name of the scope (`"server"`).  |

**Example:**

```java
interceptorService.register( data -> {
    ServerScope scope = ( ServerScope ) data.get( "scope" );
    // Add custom keys to the server scope
    scope.put( "myKey", "myValue" );
    return false;
}, BoxEvent.ON_SERVER_SCOPE_CREATION.key() );
```

---

## `onConfigurationLoad`

Fired after the core `boxlang.json` configuration file has been loaded and deserialized. This fires before any override files are applied, so the configuration at this point represents the base defaults.

**Event Data:**

| Key      | Type                   | Description                              |
| -------- | ---------------------- | ---------------------------------------- |
| `config` | `BoxLangConfiguration` | The loaded core configuration object.    |

**Example:**

```java
interceptorService.register( data -> {
    BoxLangConfiguration config = ( BoxLangConfiguration ) data.get( "config" );
    // Inspect or mutate base configuration before overrides are applied
    return false;
}, BoxEvent.ON_CONFIGURATION_LOAD.key() );
```

---

## `onConfigurationOverrideLoad`

Fired each time an override configuration file is merged into the active configuration. This may fire multiple times — once for the runtime home override (`${boxlang-home}/config/boxlang.json`) and again for any CLI/ENV-supplied config path.

**Event Data:**

| Key              | Type                   | Description                                             |
| ---------------- | ---------------------- | ------------------------------------------------------- |
| `config`         | `BoxLangConfiguration` | The configuration object after the override was applied.|
| `configOverride` | `String`               | The absolute path of the override file that was applied.|

**Example:**

```java
interceptorService.register( data -> {
    BoxLangConfiguration config         = ( BoxLangConfiguration ) data.get( "config" );
    String               configOverride = ( String ) data.get( "configOverride" );
    // React to which override file was applied
    return false;
}, BoxEvent.ON_CONFIGURATION_OVERRIDE_LOAD.key() );
```

---

## `onParse`

Fired after every parse operation — whether parsing a file, a code string, an expression, or a statement. The `result` key in the event data is **mutable**: an interceptor can replace it with a modified `ParsingResult` to alter the AST before execution.

This event fires on every parse, including during compilation, so interceptors should be lightweight.

**Event Data (file parse):**

| Key      | Type            | Description                                               |
| -------- | --------------- | --------------------------------------------------------- |
| `file`   | `File`          | The source file that was parsed.                          |
| `result` | `ParsingResult` | The result of the parse. **Replaceable by interceptors.** |

**Event Data (string/expression parse):**

| Key      | Type            | Description                                               |
| -------- | --------------- | --------------------------------------------------------- |
| `code`   | `String`        | The source code string that was parsed.                   |
| `result` | `ParsingResult` | The result of the parse. **Replaceable by interceptors.** |

> `ParsingResult` contains: `root` (`BoxNode` — the AST root), `issues` (`List<Issue>`), and `comments` (`List<BoxComment>`).

**Example:**

```java
interceptorService.register( data -> {
    ParsingResult result = ( ParsingResult ) data.get( "result" );
    // Inspect or replace the AST
    // data.put( "result", myModifiedResult );
    return false;
}, BoxEvent.ON_PARSE.key() );
```

---

## `onMissingMapping`

Fired when a path cannot be resolved against any registered mapping. An interceptor can supply a `ResolvedFilePath` to handle the resolution — if `resolvedFilePath` is set in the event data, the runtime uses it and skips the fallback to the root mapping.

This makes it possible for modules to implement custom path resolution strategies (e.g., virtual filesystems, classpath lookups).

**Event Data:**

| Key                | Type               | Description                                                                                    |
| ------------------ | ------------------ | ---------------------------------------------------------------------------------------------- |
| `path`             | `String`           | The path that could not be resolved.                                                           |
| `resolvedFilePath` | `ResolvedFilePath` | Initially `null`. Set this in your interceptor to provide a resolved path and short-circuit the fallback. |

**Example:**

```java
interceptorService.register( data -> {
    String path = ( String ) data.get( "path" );
    if ( path.startsWith( "/virtual/" ) ) {
        data.put( "resolvedFilePath", ResolvedFilePath.of(
            "/virtual/",
            "/virtual/",
            path,
            Path.of( "/actual/path/on/disk" )
        ) );
    }
    return false;
}, BoxEvent.ON_MISSING_MAPPING.key() );
```

---

## `onPreSourceInvoke`

Fired immediately before a BoxLang script source (`BoxScript`) is invoked. Use this to inject context, log execution, or set up pre-invocation state.

**Event Data:**

| Key      | Type          | Description                                    |
| -------- | ------------- | ---------------------------------------------- |
| `context`| `IBoxContext` | The context in which the source is executing.  |
| `source` | `BoxScript`   | The script source about to be invoked.         |

**Example:**

```java
interceptorService.register( data -> {
    IBoxContext context = ( IBoxContext ) data.get( "context" );
    BoxScript   source  = ( BoxScript ) data.get( "source" );
    // Set up pre-invocation state or logging
    return false;
}, BoxEvent.ON_PRE_SOURCE_INVOKE.key() );
```

---

## `onPostSourceInvoke`

Fired after a BoxLang script source finishes executing — in a `finally` block, so this fires whether the invocation succeeded or threw an exception. Use this for cleanup, metrics, or post-execution logic.

**Event Data:**

| Key      | Type          | Description                                    |
| -------- | ------------- | ---------------------------------------------- |
| `context`| `IBoxContext` | The context in which the source executed.      |
| `source` | `BoxScript`   | The script source that was invoked.            |

**Example:**

```java
interceptorService.register( data -> {
    IBoxContext context = ( IBoxContext ) data.get( "context" );
    BoxScript   source  = ( BoxScript ) data.get( "source" );
    // Cleanup, metrics collection, etc.
    return false;
}, BoxEvent.ON_POST_SOURCE_INVOKE.key() );
```