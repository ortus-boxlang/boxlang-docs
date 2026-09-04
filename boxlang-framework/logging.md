---
description: A complete guide to logging in BoxLang — from quick one-liners to structured JSON logs, named loggers, and interceptors.
icon: file-lines
---

# Logging

BoxLang ships with a production-ready logging system built on top of [Logback](https://logback.qos.ch/), one of the most trusted logging frameworks in the Java ecosystem. Every piece of BoxLang — the runtime, modules, async engine, caching, and your own applications — funnels through this unified system, giving you a single place to configure, query, and extend logging behavior.

{% hint style="info" %}
BoxLang logging is powered by **Logback** under the hood, which means all of its rolling-file, encoder, and appender semantics apply directly. You do not need to configure Logback yourself — BoxLang wraps it cleanly — but knowledge of Logback concepts (loggers, appenders, encoders, additivity) will help you understand the more advanced options.
{% endhint %}

---

## Quick Start

The easiest way to log anything in BoxLang is `writeLog()`:

```js
// Log to the default application logger
writeLog( "User #userID# logged in" );

// Log to a named logger with an explicit level
writeLog( text="Order #orderID# failed payment", type="error", log="orders" );

// Log to an absolute file path (creates a file appender on the fly)
writeLog( text="Audit event", log="/var/log/myapp/audit.log" );
```

Using the tag/component syntax:

```xml
<bx:log text="User #userID# logged in" type="information" log="application" />
```

---

## Log Levels

BoxLang supports five severity levels, listed from most to least severe:

| Level | Constant | When to use |
|-------|----------|-------------|
| `ERROR` | `"error"` | Failures that need immediate attention |
| `WARN` | `"warning"` | Unexpected situations that are recoverable |
| `INFO` | `"information"` | Normal operational events |
| `DEBUG` | `"debug"` | Developer-facing detail for diagnosing issues |
| `TRACE` | `"trace"` | Very fine-grained tracing, highest verbosity |

There is also a special value `OFF` that silences a logger entirely.

A logger set to a given level will capture that level **and all more-severe levels**. For example, a logger at `INFO` captures `INFO`, `WARN`, and `ERROR`, but not `DEBUG` or `TRACE`.

---

## writeLog() BIF

`writeLog()` is a global built-in function (BIF) available everywhere in BoxLang scripts.

```
writeLog( text, [type], [application], [log] )
```

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `text` | `string` | Yes | — | The message to log |
| `type` | `string` | No | `"information"` | Log level: `"information"`, `"warning"`, `"error"`, `"debug"`, `"trace"` |
| `application` | `boolean` | No | `true` | When `true`, prepends the application name to the log entry |
| `log` | `string` | No | `"application"` | Name of the target logger, or an absolute file path |

### Basic Examples

```js
// Informational message (default level)
writeLog( "Application started" );

// Warning
writeLog( text="Disk usage above 80%", type="warning" );

// Error with named logger
writeLog( text="Payment gateway timeout", type="error", log="payments" );

// Debug detail (only captured when the logger level allows DEBUG)
writeLog( text="Query executed in #queryTime#ms", type="debug", log="performance" );

// Suppress app name prefix
writeLog( text="Raw system event", application=false );
```

### Logging to a File Path

If the `log` argument is an **absolute path**, BoxLang automatically creates a rolling file appender at that location. This is useful for audit trails or legacy compatibility:

```js
writeLog(
    text="User #userID# exported report",
    type="information",
    log="/var/log/myapp/audit.log"
);
```

### Dynamic Logger Creation

If you pass a logger name that does not yet exist in the configuration, BoxLang creates it dynamically as a rolling file appender inside the configured logs directory. The file will be named `<loggerName>.log`.

```js
// Creates {logsDirectory}/orders.log if it doesn't exist yet
writeLog( text="Order #orderID# shipped", type="information", log="orders" );
```

---

## bx:log Component

The `bx:log` component provides the same functionality as `writeLog()` but in tag/template syntax. It is useful in `.bxm` template files or when mixing markup and logic.

```
<bx:log text="..." [log="..."] [type="..."] [application="..."] />
```

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `text` | `string` | No | — | The message to log |
| `log` | `string` | No | `"application"` | Named logger or absolute file path |
| `type` | `string` | No | `"information"` | Log level |
| `application` | `boolean` | No | `true` | Prepend application name |

{% hint style="info" %}
The `file` attribute is accepted for CFML compatibility but is deprecated. Use `log` instead.
{% endhint %}

### Template Examples

```xml
<!-- Basic info log -->
<bx:log text="Page rendered: #cgi.script_name#" />

<!-- Error to a specific logger -->
<bx:log text="Template error: #getException().getMessage()#"
        type="error"
        log="application" />

<!-- Debug without app name -->
<bx:log text="Cache miss for key: #cacheKey#"
        type="debug"
        application="false"
        log="cache" />
```

### Script Syntax

`bx:log` can also be used in `.bx` script files:

```js
bx:log text="Processing batch #batchID#" type="debug" log="scheduler";
```

---

## Built-In Named Loggers

BoxLang registers several named loggers automatically at startup. Each one writes to its own rotating log file inside `{logsDirectory}/`:

| Logger Name | Default Level | Purpose |
|-------------|---------------|---------|
| `runtime` | inherits root | Core runtime events, startup, shutdown |
| `application` | `TRACE` | Application-level events; default target for `writeLog()` |
| `modules` | inherits root | Module loading, activation, and deactivation |
| `async` | inherits root | Thread pools, futures, scheduled task execution |
| `cache` | inherits root | Cache provider activity and evictions |
| `datasource` | inherits root | Datasource creation, query logging, connection pool |
| `scheduler` | `INFO` | Scheduled task runs and outcomes |
| `http` | `INFO` | `bx:http` request lifecycle — raise to `DEBUG` to log each request's start/completion, status code, and elapsed time |

You can target any of these by name:

```js
writeLog( text="Cache cleared by admin", type="info", log="cache" );
writeLog( text="Datasource reconnected", type="warn", log="datasource" );
```

---

## Configuration Reference

All logging configuration lives in `boxlang.json` under the `logging` key. Below is a fully annotated example:

{% code title="boxlang.json" %}
```json
"logging": {
    // Directory where log files are written
    "logsDirectory": "${boxlang-home}/logs",

    // Maximum age of a log file before rotation (days). 0 = never rotate.
    "maxLogDays": 90,

    // Maximum size of a single log file before rotation
    "maxFileSize": "100MB",

    // Total size cap across all log files before oldest are pruned
    "totalCapSize": "5GB",

    // Root logger level. All loggers without an explicit level inherit this.
    // Values (most → least severe): ERROR, WARN, INFO, DEBUG, TRACE, OFF
    "rootLevel": "WARN",

    // Default encoder for all file appenders: "text" or "json"
    "defaultEncoder": "text",

    // Print the resolved Logback configuration on startup (useful for debugging)
    "statusPrinterOnLoad": false,

    "loggers": {
        "application": {
            "level": "TRACE",
            "appender": "file",
            "appenderArguments": {},
            "encoder": "text",
            "additive": true
        },
        "scheduler": {
            "level": "INFO",
            "appender": "file",
            "appenderArguments": {},
            "encoder": "text",
            "additive": true
        }
    }
}
```
{% endcode %}

### Global Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `logsDirectory` | `${boxlang-home}/logs` | Where log files are written. Supports BoxLang home variable interpolation. |
| `maxLogDays` | `90` | Days to retain log files. `0` disables time-based rotation. |
| `maxFileSize` | `"100MB"` | Per-file size limit before rotation. Supports `KB`, `MB`, `GB` suffixes. |
| `totalCapSize` | `"5GB"` | Total disk cap across all log files. Oldest archives are removed first. |
| `rootLevel` | `"WARN"` | Minimum level for the root (catch-all) logger. Automatically raised to `DEBUG` when BoxLang debug mode is active. |
| `defaultEncoder` | `"text"` | Encoding format for all appenders unless overridden per-logger. `"text"` or `"json"`. |
| `statusPrinterOnLoad` | `false` | Print resolved Logback config at startup. Helpful when diagnosing misconfiguration. |

### Logger Settings

Each named logger under `loggers` supports:

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `level` | `string` | inherits `rootLevel` | Logger-specific level threshold. Omit to inherit from root. |
| `appender` | `string` | `"file"` | Output target. Currently `"file"` and `"console"`. Coming soon: `"smtp"`, `"socket"`, `"db"`, `"syslog"`. |
| `appenderArguments` | `object` | `{}` | Appender-specific key-value configuration. |
| `encoder` | `string` | `defaultEncoder` | Override the encoder for this logger: `"text"` or `"json"`. |
| `additive` | `boolean` | `true` | When `true` the logger propagates messages to its parent loggers (including root). Set to `false` to isolate this logger's output. |
| `categories` | `array` | `[]` | List of Java package or class names whose log output should be routed to this logger. Entries are matched by logger name prefix. Leading/trailing whitespace is trimmed automatically. |

---

## Custom Named Loggers

You can define your own loggers in `boxlang.json` and then target them by name in your code. This is the recommended approach for separating concerns across different parts of your application:

{% code title="boxlang.json" %}
```json
"logging": {
    "loggers": {
        "orders": {
            "level": "INFO",
            "appender": "file",
            "encoder": "json",
            "additive": false
        },
        "payments": {
            "level": "DEBUG",
            "appender": "file",
            "encoder": "json",
            "additive": false
        },
        "audit": {
            "level": "TRACE",
            "appender": "file",
            "encoder": "json",
            "additive": false
        }
    }
}
```
{% endcode %}

```js
// Now use them anywhere in your application
writeLog( text="Order #orderID# placed by user #userID#", type="information", log="orders" );
writeLog( text="Payment #paymentID# authorised for $#amount#", type="information", log="payments" );
writeLog( text="Admin #adminID# deleted record #recordID#", type="warning", log="audit" );
```

{% hint style="success" %}
Setting `"additive": false` on a custom logger stops its messages from also appearing in the root/runtime log, keeping your custom log files clean and focused.
{% endhint %}

---

## Logger Categories

Logger categories let you route third-party Java library log output into a BoxLang-managed logger. Any Java package or class name listed in a logger's `categories` array will be redirected to that logger — using its configured level and appender — instead of being handled by the default Logback root configuration.

This is especially useful for silencing chatty libraries or capturing their output in a dedicated file.

### How It Works

- Each entry in `categories` is a Java package or class name (e.g. `"com.zaxxer.hikari"`).
- Log events originating from that package or any sub-package are captured by the target logger.
- The category logger inherits the target logger's **level** threshold and **appender**.
- Routing is non-additive: matched events do not bubble up further.
- Leading/trailing whitespace in category names is trimmed automatically.
- Loggers with `"level": "OFF"` skip appender creation entirely, making them a zero-overhead sink.

### Routing Noisy Libraries

Configure a dedicated logger to capture (or suppress) output from a specific library:

{% code title="boxlang.json" %}
```json
"logging": {
    "loggers": {
        "hikari": {
            "level": "WARN",
            "appender": "file",
            "encoder": "text",
            "additive": false,
            "categories": [
                "com.zaxxer.hikari"
            ]
        }
    }
}
```
{% endcode %}

All log events from `com.zaxxer.hikari.*` will now be written to `hikari.log` at `WARN` level or above, and will not appear in `runtime.log`.

### The Built-In Blackhole Logger

BoxLang ships with a pre-configured `blackhole` logger in the default `boxlang.json`. Its level is set to `OFF`, so any categories assigned to it are completely silenced with no I/O overhead:

```json
"blackhole": {
    "level": "OFF",
    "appender": "file",
    "appenderArguments": {},
    "encoder": "text",
    "additive": false,
    "categories": []
}
```

To suppress a noisy library, add its package to the `blackhole` categories list:

```json
"blackhole": {
    "level": "OFF",
    "appender": "file",
    "appenderArguments": {},
    "encoder": "text",
    "additive": false,
    "categories": [
        "com.zaxxer.hikari",
        "org.springframework"
    ]
}
```

{% hint style="warning" %}
`additive` must be `false` on the blackhole logger (and any silencing logger) to prevent matched events from propagating to the root logger and appearing in `runtime.log`.
{% endhint %}

### Multiple Categories Across Loggers

You can spread categories across multiple loggers. For example, route database connection pool noise to a dedicated file while silencing framework internals entirely:

{% code title="boxlang.json" %}
```json
"logging": {
    "loggers": {
        "thirdparty-db": {
            "level": "WARN",
            "appender": "file",
            "encoder": "text",
            "additive": false,
            "categories": [
                "com.zaxxer.hikari",
                "org.apache.commons.dbcp2"
            ]
        },
        "blackhole": {
            "level": "OFF",
            "appender": "file",
            "appenderArguments": {},
            "encoder": "text",
            "additive": false,
            "categories": [
                "org.springframework",
                "io.netty"
            ]
        }
    }
}
```
{% endcode %}

---

## JSON Structured Logging

Switch a logger's encoder to `"json"` to emit [JSON Lines](https://jsonlines.org/) — one JSON object per log entry. This is ideal for log aggregators (Splunk, Datadog, Loki, OpenSearch, etc.) that parse structured data.

{% code title="boxlang.json" %}
```json
"logging": {
    "defaultEncoder": "json"
}
```
{% endcode %}

Or selectively for a single logger:

```json
"orders": {
    "appender": "file",
    "encoder": "json",
    "additive": false
}
```

Each line in the log file will look like:

```json
{"timestamp":"2026-04-01T12:34:56.789Z","level":"INFO","logger":"orders","message":"Order 1042 placed by user 77","application":"MyApp"}
```

---

## LoggingService API

For advanced scenarios you can interact with the logging subsystem directly through the BoxLang `LoggingService`. Retrieve it from the BoxLang runtime:

```js
// Get the runtime and its logging service
runtime = getBoxRuntime();
loggingService = runtime.getLoggingService();

// Get an existing or auto-created named logger (returns a org.slf4j.Logger)
logger = loggingService.getLogger( "orders" );

// Log at specific levels directly via the SLF4J Logger API
logger.info( "Order {} placed", orderID );
logger.warn( "Low inventory on product {}", productID );
logger.error( "Payment failed for order {}", orderID );
logger.debug( "Cart total recalculated: {}", cartTotal );
logger.trace( "Entering checkout step {}", stepName );

// Check whether a level is enabled before building an expensive message
if( logger.isDebugEnabled() ) {
    logger.debug( "Full cart dump: {}", serializeJSON( cart ) );
}
```

### Registering a Logger at Runtime

If you need a logger that isn't in `boxlang.json` and you want more control than the auto-creation provided by `writeLog()`, you can register one programmatically:

```js
loggingService = getBoxRuntime().getLoggingService();

// Register a new named logger with a specific level
loggingService.registerLogger( "myFeature", "DEBUG" );

// Now use it via writeLog or the service
writeLog( text="Feature flag evaluated", type="debug", log="myFeature" );
```

---

## Logging Interceptors

BoxLang fires an interception event every time a log message is processed. You can intercept these events to add custom sinks (e.g. send errors to Slack, record to a database, stream to a monitoring service) without modifying your application code.

The event name is `logMessage`.

### Registering an Interceptor in Application.bx

```js
class {

    function onLoad() {
        // Register a listener for all log messages
        boxRegisterInterceptor(
            interceptor : this,
            points      : [ "logMessage" ]
        );
    }

    function logMessage( event, data, interceptData ) {
        // data contains: level, message, logger, application, timestamp
        if ( data.level == "ERROR" ) {
            // Forward errors to an external alerting system
            sendSlackAlert( data.message );
        }
    }

}
```

### Standalone Interceptor Class

```js
class LoggingInterceptor {

    function logMessage( event, data, interceptData ) {
        // data.level    — the log level (e.g. "ERROR")
        // data.message  — the log text
        // data.logger   — the logger name
        param data.application = "";

        if ( data.level == "ERROR" ) {
            // Persist to a database error table
            queryExecute(
                "INSERT INTO error_log (level, message, logger, logged_at) VALUES (?, ?, ?, NOW())",
                [ data.level, data.message, data.logger ]
            );
        }
    }

}
```

{% hint style="info" %}
See [Interceptors](./interceptors/README.md) for a full guide to the interception framework, and [Logging Events](./interceptors/core-interception-points/logging-events.md) for the complete list of logging interception points.
{% endhint %}

---

## Best Practices

### Choose the Right Level

```js
// ERROR — something broke and needs fixing
writeLog( text="Unhandled exception in checkout: #e.getMessage()#", type="error", log="application" );

// WARN — something unexpected happened but the app recovered
writeLog( text="Cache miss rate elevated: #missRate#%", type="warning", log="cache" );

// INFO — normal events worth recording
writeLog( text="User #userID# completed checkout, order #orderID#", type="information", log="orders" );

// DEBUG — developer-facing context (gate behind isDebugEnabled() for expensive calls)
writeLog( text="SQL: #sql# | params: #serializeJSON(params)#", type="debug", log="datasource" );

// TRACE — very high-volume detail, only during active development
writeLog( text="Entering method processLineItem() with #lineItems.len()# items", type="trace" );
```

### Isolate Concerns with Named Loggers

Avoid dumping everything into `application.log`. Create dedicated loggers for distinct subsystems so that logs are easy to find, tail, and rotate independently:

```json
"loggers": {
    "orders":    { "level": "INFO",  "encoder": "json", "additive": false },
    "payments":  { "level": "DEBUG", "encoder": "json", "additive": false },
    "audit":     { "level": "TRACE", "encoder": "json", "additive": false },
    "scheduler": { "level": "INFO",  "encoder": "text", "additive": false }
}
```

### Use JSON Encoding for Machine-Readable Logs

If you route logs to a SIEM, APM, or log aggregator, switch to JSON encoding so fields are parsed correctly:

```json
"defaultEncoder": "json"
```

### Do Not Build Expensive Strings at TRACE/DEBUG Unless Necessary

```js
// Bad — serialiseJSON() runs even if DEBUG is disabled
writeLog( text="Payload: #serializeJSON( payload )#", type="debug" );

// Better — use the LoggingService API to guard the call
logger = getBoxRuntime().getLoggingService().getLogger( "api" );
if ( logger.isDebugEnabled() ) {
    logger.debug( "Payload: {}", serializeJSON( payload ) );
}
```

### Use Additive = false for Custom Loggers

Setting `"additive": false` stops entries from bubbling up into the root logger and appearing in the `runtime.log`. This keeps your focused logs clean:

```json
"payments": {
    "appender": "file",
    "encoder": "json",
    "additive": false
}
```

### Rotate and Cap Aggressively in Production

```json
"maxLogDays": 30,
"maxFileSize": "50MB",
"totalCapSize": "2GB"
```

Smaller caps prevent runaway disk usage, especially at `DEBUG` or `TRACE` levels.

---

## Related Documentation

- [Logging Configuration Reference](../getting-started/configuration/logging.md) — Full `boxlang.json` logging options
- [writeLog() BIF Reference](../boxlang-language/reference/built-in-functions/system/WriteLog.md)
- [bx:log Component Reference](../boxlang-language/reference/components/system/Log.md)
- [Interceptors](./interceptors/README.md) — Intercept and extend BoxLang events
- [Logging Interception Points](./interceptors/core-interception-points/logging-events.md)
- [Application.bx](./applicationbx.md) — Application lifecycle and configuration
