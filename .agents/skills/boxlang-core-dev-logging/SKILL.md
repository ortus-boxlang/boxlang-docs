---
name: boxlang-core-dev-logging
description: "Use this skill when working with BoxLang logging: obtaining loggers via LoggingService, using BoxLangLogger (trace/debug/info/warn/error), pre-configured common loggers, creating named loggers, parameterized messages, accessing loggers from context and interceptors, and logging configuration in boxlang.json."
---

# BoxLang Logging

## Overview

BoxLang uses a centralized logging system built on **Logback** (SLF4J implementation).
All logging MUST go through `LoggingService` — never use `System.out.println()` or
create SLF4J `Logger` instances directly.

Key classes:
- `ortus.boxlang.runtime.logging.LoggingService` — singleton service managing all loggers
- `ortus.boxlang.runtime.logging.BoxLangLogger` — wrapper around SLF4J `LocationAwareLogger`

## Getting a Logger

### Pre-Configured Common Loggers

```java
import ortus.boxlang.runtime.logging.BoxLangLogger;
import ortus.boxlang.runtime.services.LoggingService;

LoggingService loggingService = BoxRuntime.getInstance().getLoggingService();

// Common loggers — already initialized, ready to use
BoxLangLogger logger = loggingService.RUNTIME_LOGGER;    // Core runtime events
BoxLangLogger logger = loggingService.ASYNC_LOGGER;      // Async operations
BoxLangLogger logger = loggingService.CACHE_LOGGER;      // Cache operations
BoxLangLogger logger = loggingService.EXCEPTION_LOGGER;  // Exception tracking
BoxLangLogger logger = loggingService.DATASOURCE_LOGGER; // Database operations
BoxLangLogger logger = loggingService.MODULES_LOGGER;    // Module loading/lifecycle
BoxLangLogger logger = loggingService.SCHEDULER_LOGGER;  // Scheduled tasks
BoxLangLogger logger = loggingService.APPLICATION_LOGGER;// Application-level events
```

### Creating Named Loggers

```java
LoggingService loggingService = BoxRuntime.getInstance().getLoggingService();

// Named logger (logs to logs/myfeature.log)
BoxLangLogger logger = loggingService.getLogger( "myfeature" );

// Relative path (relative to configured logs directory)
BoxLangLogger logger = loggingService.getLogger( "subsystem/component" );

// Absolute path
BoxLangLogger logger = loggingService.getLogger( "/var/log/boxlang/custom.log" );
```

`getLogger()` automatically appends `.log` if no extension is present, creates the
logger lazily, and caches it for reuse (case-insensitive).

### From Context

```java
// Any IBoxContext provides a logger
BoxLangLogger logger = context.getLogger();

// From BaseInterceptor subclass
BoxLangLogger logger = this.getLogger();

// From BaseScheduler subclass
BoxLangLogger logger = this.getLogger();
```

## Logging Methods

```java
logger.trace( "Entering method with params: {}", params );       // Very detailed
logger.debug( "Processing {} items in batch", items.size() );    // Debug info
logger.info( "Server started on port {}", port );                // Key events
logger.warn( "Cache threshold exceeded: {} of {}", size, max );  // Warnings
logger.error( "Connection failed: {}", e.getMessage() );         // Errors
logger.error( "Unexpected exception", e );                       // With stack trace
```

## Key Practices

### Always Use Parameterized Messages

```java
// CORRECT — message built only when level is enabled
logger.debug( "User {} logged in from {}", username, ipAddress );

// WRONG — concatenation happens regardless of log level
logger.debug( "User " + username + " logged in from " + ipAddress );
```

### Include Exceptions When Logging Errors

```java
try {
    processRequest( context );
} catch ( Exception e ) {
    logger.error( "Failed to process request for {}", requestPath, e );
}
```

### Choose the Right Logger

| Logger | Use for |
|---|---|
| `RUNTIME_LOGGER` | Core runtime events, service start/stop |
| `MODULES_LOGGER` | Module loading, registration, unloading |
| `ASYNC_LOGGER` | Thread pools, futures, async work |
| `SCHEDULER_LOGGER` | Scheduled tasks, cron jobs |
| `CACHE_LOGGER` | Cache hits, misses, eviction |
| `DATASOURCE_LOGGER` | Query execution, connection management |
| `EXCEPTION_LOGGER` | Caught exceptions for audit/analysis |
| `APPLICATION_LOGGER` | Application lifecycle events |
| Named logger | New features or subsystems needing isolation |

## Logging in Common Patterns

### Service Initialization

```java
public class MyService extends BaseService {

    private BoxLangLogger logger;

    @Override
    public void onStartup() {
        this.logger = BoxRuntime.getInstance().getLoggingService().getLogger( "myservice" );
        logger.info( "MyService starting up..." );
    }

    @Override
    public void onShutdown( Boolean force ) {
        logger.info( "MyService shutting down (force={})", force );
    }
}
```

### BIF with Logging

```java
@BoxBIF
public class MyBIF extends BIF {

    private static final BoxLangLogger logger =
        BoxRuntime.getInstance().getLoggingService().getLogger( "bifs.mybif" );

    @Override
    public Object invoke( IBoxContext context, ArgumentsScope arguments ) {
        String input = arguments.getAsString( Key.of( "input" ) );
        logger.debug( "Processing input of length {}", input.length() );

        try {
            Object result = doWork( input );
            logger.trace( "Result computed successfully" );
            return result;
        } catch ( Exception e ) {
            logger.error( "BIF processing failed for input: {}", input, e );
            throw new BoxRuntimeException( "Processing error: " + e.getMessage(), e );
        }
    }
}
```

### Interceptor with Logging

```java
@Interceptor
public class AuditInterceptor extends BaseInterceptor {

    @Override
    public void configure() {
        // this.log is automatically injected by BaseInterceptor
        this.log.info( "AuditInterceptor configured" );
    }

    @InterceptionPoint
    public void onRequestStart( IStruct event ) {
        this.log.info( "Request started: {}", event.getAsString( Key.of("path") ) );
    }
}
```

### Scheduler with Logging

```java
public class MyScheduler extends BaseScheduler {

    public MyScheduler() {
        super( "my-scheduler" );
        // this.logger is available in BaseScheduler
    }

    @Override
    public void configure() {
        task( "cleanupTask" )
            .call( () -> {
                this.logger.info( "Running cleanup task" );
                performCleanup();
            })
            .everyHour();
    }
}
```

### ModuleConfig.bx (BoxLang)

```boxlang
// ModuleConfig.bx — log is auto-injected
class {

    function onLoad() {
        // log is already available — no setup needed
        log.info( "Module loaded. API URL: #settings.baseUrl#" )
    }

    function configure() {
        log.debug( "Configuring module with apiKey length: #len(settings.apiKey)#" )
    }

    function onUnload() {
        log.info( "Module unloaded." )
    }

}
```

## Logging Configuration (`boxlang.json`)

```json
{
    "logging": {
        "logsDirectory": "./logs",
        "level": "INFO",
        "loggers": {
            "scheduler": { "level": "DEBUG", "async": true },
            "cache":     { "level": "WARN"  }
        }
    }
}
```

Supported levels (from most to least verbose): `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`

## What NOT to Do

```java
// ❌ Never use System.out / System.err
System.out.println( "My debug message" );
System.err.println( "My error" );

// ❌ Never create SLF4J loggers directly
private static final Logger log = LoggerFactory.getLogger( MyClass.class );

// ❌ Never concatenate in log calls
logger.info( "Processing " + count + " items" );  // Use {} placeholders instead

// ❌ Never log sensitive data
logger.debug( "Password: {}", user.getPassword() );
logger.trace( "Token: {}", authToken );
```

## References

- [LoggingService.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/logging/LoggingService.java)
- [BoxLangLogger.java](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/logging/BoxLangLogger.java)
- [BoxLang Source](https://github.com/ortus-boxlang/BoxLang)
