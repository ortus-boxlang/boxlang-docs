---
name: boxlang-core-dev-interceptors
description: "Use this skill when creating BoxLang interceptors: Observer/Intercepting Filter patterns, interceptor pools, BoxLang class vs Java interceptors, lambda interceptors, registration via BIFs/InterceptorService/ModuleConfig, interception points, and announcing custom events."
---

# BoxLang Interceptors

## Overview

BoxLang's interceptor system implements the **Observer** and **Intercepting Filter**
design patterns. Interceptors listen for named events (interception points) announced
by the runtime, modules, or application code. They enable cross-cutting concerns
like logging, security, AOP, routing, and content manipulation without modifying
core code.

## Interceptor Pools

Three pools exist in the runtime. Each pool is an independent event emitter:

| Pool | Scope | Use Case |
|------|-------|---------|
| **Global Runtime** | Entire BoxLang process | Module events, parse events, global AOP |
| **Application Request Listener** | Per-application request lifecycle | Auth, routing, request logging |
| **CacheProviders** | Per cache instance | Cache event hooks |

## Creating a BoxLang Class Interceptor

Method names in the class directly correspond to interception point names:

```boxlang
// interceptors/RequestLogger.bx
class {

    // Auto-injected by the runtime
    property name="name"              setter="false"
    property name="properties"        setter="false"
    property name="log"               setter="false"  // module logger
    property name="interceptorService" setter="false"
    property name="boxRuntime"        setter="false"
    property name="moduleRecord"      setter="false"  // if module-based

    /**
     * Called when the interceptor is registered.
     * Use this to validate properties and set up resources.
     */
    function configure() {
        // Access settings passed at registration time
        log.info( "RequestLogger interceptor configured. Level: #properties.logLevel ?: 'INFO'#" )
    }

    // ---------------------------------------------------------------
    // Interception point methods — name must EXACTLY match the event
    // ---------------------------------------------------------------

    /**
     * Fires before every HTTP request.
     * @event Struct with request context data (mutable)
     */
    function onRequestStart( struct event={} ) {
        log.info( "→ #cgi.request_method# #cgi.script_name##cgi.query_string ?: ''#" )
        event.requestStartTime = getTickCount()
    }

    /**
     * Fires after every HTTP request.
     */
    function onRequestEnd( struct event={} ) {
        var elapsed = getTickCount() - (event.requestStartTime ?: getTickCount())
        log.info( "← #cgi.script_name# completed in #elapsed#ms" )
    }

    /**
     * Fires when an unhandled exception occurs.
     */
    function onException( struct event={} ) {
        var ex = event.exception ?: {}
        log.error( "Exception: #ex.message ?: 'unknown'# | #ex.stackTrace ?: ''#" )
    }

}
```

## Creating a Java Interceptor

```java
// src/main/java/com/example/interceptors/RequestLogger.java
package com.example.interceptors;

import ortus.boxlang.runtime.events.BaseInterceptor;
import ortus.boxlang.runtime.events.InterceptionPoint;
import ortus.boxlang.runtime.scopes.Key;
import ortus.boxlang.runtime.types.IStruct;

@ortus.boxlang.runtime.events.Interceptor
public class RequestLogger extends BaseInterceptor {

    @Override
    public void configure() {
        // this.properties is available for config
        // this.log is available for logging
        // this.interceptorService is available
        // this.boxRuntime is available
    }

    // @InterceptionPoint marks this method as an event handler
    @InterceptionPoint
    public void onRequestStart( IStruct event ) {
        String method = (String) event.getOrDefault( Key.of("requestMethod"), "GET" );
        this.log.info( "Request started: " + method );
        event.put( Key.of("startTime"), System.currentTimeMillis() );
    }

    @InterceptionPoint
    public void onRequestEnd( IStruct event ) {
        Long startTime = (Long) event.getOrDefault( Key.of("startTime"), System.currentTimeMillis() );
        long elapsed   = System.currentTimeMillis() - startTime;
        this.log.info( "Request completed in " + elapsed + "ms" );
    }

    @InterceptionPoint
    public void preFunctionInvoke( IStruct event ) {
        // event contains: functionName, arguments, context
        String fnName = event.getAsString( Key.of("functionName") );
        this.log.debug( "Invoking function: " + fnName );
    }

}
```

## Lambda and Closure Interceptors

Closures/lambdas **must** explicitly specify which events they handle:

```boxlang
// Closure interceptor — must specify states
var myListener = function( struct event={} ) {
    writeOutput( "Request started!" )
}

// Register for specific events
boxRegisterInterceptor(
    myListener,
    ["onRequestStart", "onRequestEnd"]
)

// Lambda form
boxRegisterInterceptor(
    (event) -> logEvent( event ),
    ["onHTTPRequest"]
)
```

## Registering Interceptors

### Method 1: ModuleConfig.bx (Recommended for Modules)

```boxlang
// ModuleConfig.bx
class {

    this.interceptors = [
        {
            // Full invocation path to the interceptor class
            class      : "#moduleRecord.invocationPath#.interceptors.RequestLogger",
            properties : {
                logLevel  : "INFO",
                maxErrors : 100
            }
        },
        {
            class      : "#moduleRecord.invocationPath#.interceptors.SecurityFilter",
            properties : { enabled: true }
        }
    ]

}
```

### Method 2: BIF Registration

```boxlang
// Global runtime interceptor
boxRegisterInterceptor( new interceptors.MyInterceptor() )

// With properties
boxRegisterInterceptor(
    new interceptors.AuditLog(),
    [],           // states: empty = listen to all matching methods
    { logPath: "/var/log/audit.log" }
)

// Application request listener (web context)
boxRegisterRequestInterceptor( new interceptors.AuthFilter() )
```

### Method 3: InterceptorService API (Java)

```java
InterceptorService service = BoxRuntime.getInstance().getInterceptorService();

// Register a Java-based interceptor
service.register( new RequestLogger() );

// Register with properties
IStruct props = new Struct();
props.put( Key.of("logLevel"), "DEBUG" );
service.register( new RequestLogger(), props );

// Register a BoxLang class
IClassRunnable bxInterceptor = (IClassRunnable) context.loadClass("interceptors.MyBxInterceptor");
service.register( bxInterceptor );

// Register a closure for specific states
service.register(
    (IInterceptorLambda) event -> System.out.println("Event: " + event),
    Key.of("onRequestStart"), Key.of("onRequestEnd")
);
```

## Common Interception Points

All canonical event names are defined in the `BoxEvent` enum:
`ortus.boxlang.runtime.events.BoxEvent`

Use `BoxEvent.ON_REQUEST_START.key()` in Java, or the string name in BoxLang.

### Runtime Events

| Event | When | Payload Keys |
|---|---|---|
| `onRuntimeStart` | Runtime fully started | `runtime` |
| `onRuntimeShutdown` | Before shutdown | `runtime` |
| `onRuntimeConfigurationLoad` | Config loaded | `config` |
| `onRuntimeBoxContextStartup` | First context created | `context` |
| `onServerScopeCreation` | Server scope initialized | `serverScope` |
| `onConfigurationLoad` | Config file loaded | `config` |
| `onConfigurationOverrideLoad` | Override config loaded | `config` |
| `onParse` | Before source is parsed | `source`, `result` |
| `onMissingMapping` | Mapping cannot be resolved | `mapping` |
| `onPreSourceInvoke` | Before any source file runs | `context`, `source` |
| `onPostSourceInvoke` | After any source file runs | `context`, `source` |

### Module Events

| Event | When |
|---|---|
| `onModuleServiceStartup` | Module service starts |
| `onModuleServiceShutdown` | Module service stops |
| `afterModuleRegistrations` | All modules registered |
| `preModuleRegistration` | Before a module is registered |
| `postModuleRegistration` | After a module is registered |
| `afterModuleActivations` | All modules activated |
| `preModuleLoad` | Before a module is loaded |
| `postModuleLoad` | After a module is loaded |
| `preModuleUnload` | Before a module is unloaded |
| `postModuleUnload` | After a module is unloaded |

### Application / Request Events (Web Context)

| Event | When | Notes |
|---|---|---|
| `onApplicationStart` | Application started | |
| `onApplicationEnd` | Application ended | |
| `onApplicationRestart` | Application restarted | |
| `onApplicationDefined` | Application.bx found | |
| `beforeApplicationListenerLoad` | Before Application.bx loads | |
| `afterApplicationListenerLoad` | After Application.bx loads | |
| `onRequestStart` | Before request starts | Fires before Application.bx lifecycle |
| `onRequest` | Main request handling | |
| `onRequestEnd` | After request completes | |
| `onClassRequest` | Class/component requested | |
| `onRequestFlushBuffer` | Output buffer flushed | |
| `onSessionStart` | New session created | Session struct available |
| `onSessionEnd` | Session expires or is invalidated | Session data available |
| `onSessionCreated` | Session object created | |
| `onSessionDestroyed` | Session object destroyed | |
| `onError` | Unhandled exception | |
| `onMissingTemplate` | Template not found | |
| `onAbort` | Execution aborted | |
| `onRequestContextConfig` | Request context configured | |

### HTTP Events

| Event | When |
|---|---|
| `onHTTPRequest` | Every HTTP request |
| `onHTTPRawResponse` | Before raw HTTP response sent |
| `onHTTPResponse` | Before HTTP response sent |
| `onWebExecutorRequest` | Web executor request (route modification) |

### BIF / Component Lifecycle Events

| Event | When |
|---|---|
| `onBIFInstance` | BIF instantiated |
| `onBIFInvocation` | Before BIF invoked |
| `postBIFInvocation` | After BIF invoked |
| `onComponentInstance` | Component instantiated |
| `onComponentInvocation` | Component invoked |
| `onCacheComponentAction` | Cache component action |
| `onFileComponentAction` | File component action |
| `onCreateObjectRequest` | `createObject()` called |
| `afterDynamicObjectCreation` | Java object wrapped in DynamicObject |

### Template / Function Events

| Event | When | Payload |
|---|---|---|
| `preTemplateInvoke` | Before template executes | `template`, `context` |
| `postTemplateInvoke` | After template executes | `template`, `context` |
| `preFunctionInvoke` | Before any function call | `functionName`, `arguments`, `context` |
| `postFunctionInvoke` | After any function call | `functionName`, `result` |
| `onFunctionException` | Function throws exception | `functionName`, `exception` |

### Query / Transaction Events

| Event | When |
|---|---|
| `onQueryBuild` | Before query is built |
| `preQueryExecute` | Before query executes |
| `postQueryExecute` | After query executes |
| `queryAddRow` | Row added to query |
| `onTransactionBegin` | Transaction started |
| `onTransactionEnd` | Transaction ended |
| `onTransactionAcquire` | Connection acquired |
| `onTransactionRelease` | Connection released |
| `onTransactionCommit` | Transaction committed |
| `onTransactionRollback` | Transaction rolled back |
| `onTransactionSetSavepoint` | Savepoint created |

### Cache Events

| Event | When |
|---|---|
| `afterCacheElementInsert` | Item inserted |
| `beforeCacheElementRemoved` | Before item removed |
| `afterCacheElementRemoved` | After item removed |
| `afterCacheElementUpdated` | Item updated |
| `afterCacheClearAll` | Cache cleared |
| `afterCacheRegistration` | Cache provider registered |
| `afterCacheRemoval` | Cache provider removed |
| `beforeCacheRemoval` | Before cache provider removed |
| `beforeCacheReplacement` | Before cache entry replaced |
| `beforeCacheShutdown` | Before cache shuts down |
| `afterCacheShutdown` | After cache shuts down |
| `afterCacheServiceStartup` | CacheService started |
| `beforeCacheServiceShutdown` | Before CacheService shuts down |
| `afterCacheServiceShutdown` | After CacheService shuts down |

### Scheduler Events

| Event | When |
|---|---|
| `onSchedulerStartup` | Scheduler started |
| `onSchedulerShutdown` | Scheduler stopped |
| `onSchedulerRestart` | Scheduler restarted |
| `schedulerBeforeAnyTask` | Before any task runs |
| `schedulerAfterAnyTask` | After any task runs |
| `schedulerOnAnyTaskSuccess` | Task succeeded |
| `schedulerOnAnyTaskError` | Task threw an error |
| `onSchedulerServiceStartup` | SchedulerService started |
| `onSchedulerServiceShutdown` | SchedulerService stopped |
| `onAllSchedulersStarted` | All schedulers running |
| `onSchedulerRemoval` | Scheduler removed |
| `onSchedulerRegistration` | Scheduler registered |

### Datasource Events

| Event | When |
|---|---|
| `onDatasourceConfigLoad` | Datasource config loaded |
| `onDatasourceServiceStartup` | DatasourceService started |
| `onDatasourceServiceShutdown` | DatasourceService stopped |
| `onDatasourceStartup` | Datasource initialized |

### Object Marshaller Events

| Event | When |
|---|---|
| `beforeObjectMarshallSerialize` | Before serialization |
| `afterObjectMarshallSerialize` | After serialization |
| `beforeObjectMarshallDeserialize` | Before deserialization |
| `afterObjectMarshallDeserialize` | After deserialization |
| `onJSONQuerySerialize` | Query serialized to JSON |

### Dump / Other Events

| Event | When |
|---|---|
| `onBXDump` | `writeDump()` called |
| `onMissingDumpOutput` | No dump output handler found |
| `logMessage` | Log message emitted |

## Announcing Custom Events

You can announce your own events for other interceptors to listen to:

```boxlang
// Announce a custom event with a data payload
boxAnnounce( "onUserRegistered", {
    userId  : newUser.getId(),
    email   : newUser.getEmail(),
    source  : "web"
})

// Listeners elsewhere can react to this:
// function onUserRegistered( struct event={} ) {
//     sendWelcomeEmail( event.email )
//     createDefaultWorkspace( event.userId )
// }
```

```java
// Java: announce via InterceptorService
IStruct data = new Struct();
data.put( Key.of("userId"), userId );
data.put( Key.of("email"),  email );

BoxRuntime.getInstance()
    .getInterceptorService()
    .announce( Key.of("onUserRegistered"), data );
```

## Use Cases

### A/B Routing and Feature Flags (pre-request)

```boxlang
// interceptors/FeatureFlagRouter.bx
// v1.11+: fires BEFORE Application.bx onRequestStart — enables rerouting
class {
    function onRequestStart( struct event={} ) {
        var userId = session.userId ?: ""
        if ( len(userId) && featureFlags.isEnabled("new-ui", userId) ) {
            event.overridePath = "/new-ui" & cgi.path_info
        }
    }
}
```

### Maintenance Mode

```boxlang
// interceptors/MaintenanceMode.bx
class {
    function onRequestStart( struct event={} ) {
        if ( application.maintenanceMode && !isAdminIp( cgi.remote_addr ) ) {
            include "maintenance.bxm"
            abort
        }
    }
}
```

### AOP Method Tracing

```boxlang
// interceptors/MethodTracer.bx
class {
    function preFunctionInvoke( struct event={} ) {
        var fn    = event.functionName ?: "unknown"
        var start = getTickCount()
        event.traceStart = start
        log.debug( "→ #fn# called" )
    }

    function postFunctionInvoke( struct event={} ) {
        var elapsed = getTickCount() - (event.traceStart ?: getTickCount())
        log.debug( "← #event.functionName ?: 'unknown'# completed in #elapsed#ms" )
    }
}
```

### Content Manipulation

```boxlang
// interceptors/HtmlMinifier.bx
class {
    function onRequestEnd( struct event={} ) {
        // Minify HTML output before sending to client
        var output = event.output ?: ""
        if ( len(output) ) {
            event.output = minifyHtml( output )
        }
    }
}
```

## Unregistering Interceptors

```boxlang
// Unregister by reference
boxUnregisterInterceptor( myInterceptorInstance )

// Via InterceptorService (Java)
BoxRuntime.getInstance().getInterceptorService().unregister( myInterceptor )
```

## References

- [Interceptors](https://boxlang.ortusbooks.com/boxlang-framework/interceptors)
- [BaseInterceptor](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/events/BaseInterceptor.java)
- [InterceptorService](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/services/InterceptorService.java)
- [BoxLang Source](https://github.com/ortus-boxlang/BoxLang)
