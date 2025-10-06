---
description: Create virtual applications in memory with isolated settings, lifecycle events, and persistence scopes across all BoxLang runtimes
icon: rocket-launch
---

# 🚀 Application.bx

## 🌏 Overview

`Application.bx` is BoxLang's **application framework** - a powerful feature that allows you to define virtual applications in memory with isolated settings, lifecycle events, and persistence scopes. This works across **all BoxLang runtimes**: web servers (CommandBox, MiniServer), CLI applications, Lambda functions, desktop applications, and more.

{% hint style="success" %}
**Key Feature**: With a single `Application.bx` file or a hierarchy of them, you can create virtual applications in memory, each with its own isolated `application`, `session`, and configuration space - all within the same JVM process.
{% endhint %}

### What is Application.bx?

`Application.bx` is a special BoxLang class file that serves two primary purposes:

1. **Application Configuration** - Define application-wide settings in the pseudo-constructor using the `this` scope:
   * Application name and timeouts
   * Datasource configurations
   * Caching strategies
   * Session management
   * File mappings and class paths
   * Java library integration
   * Security settings
   * Custom schedulers and much more

2. **Lifecycle Event Handlers** - Implement callback methods that BoxLang executes automatically at key points:
   * Application startup/shutdown
   * Session creation/destruction
   * Request processing (start, execute, end)
   * Error handling
   * Missing templates
   * Class invocations

### How It Works

When BoxLang executes any code (web request, CLI script, Lambda function), it searches for `Application.bx` starting from the current directory and traversing **upward** through parent directories until found or reaching the root.

```
📁 /projects/myapp/
   📄 Application.bx          ← Found! Used for entire app
   📁 /admin/
      📄 Application.bx       ← Nested app with different settings
      📄 dashboard.bxm
   📁 /api/
      📄 handler.bx
   📄 index.bxm
```

{% hint style="info" %}
**Directory Scope**: The `Application.bx` file applies to its directory and all subdirectories. Any BoxLang code in that tree will automatically use this application context.
{% endhint %}

### Transient Nature

`Application.bx` is **instantiated on every request** - this is a critical feature that provides:

✅ **Dynamic Configuration** - Modify settings per-request based on conditions:

* Switch datasources based on subdomain or user
* Adjust session timeouts for bot detection
* Enable/disable features based on environment
* Dynamic security rules

✅ **Request-Level Customization** - Each request can have unique behavior while sharing the same application memory space

⚠️ **Performance Consideration** - Since it runs on every request, keep the pseudo-constructor logic optimized. Use the `application` scope for expensive operations that should only run once.

```js
class {
    this.name = "MyApp";

    // ✅ Good: Simple configuration
    this.datasource = "mainDB";

    // ❌ Avoid: Expensive operations in pseudo-constructor
    // this.data = queryExecute("SELECT * FROM huge_table");

    function onApplicationStart() {
        // ✅ Good: Expensive operations run once
        application.cachedData = queryExecute("SELECT * FROM huge_table");
    }
}
```

### Multi-Runtime Support

`Application.bx` works seamlessly across all BoxLang deployment targets:

| Runtime | Use Case | Application.bx Behavior |
| :--- | :--- | :--- |
| **Web Servers** | CommandBox, MiniServer, JEE | Full support with sessions, cookies, web scopes |
| **CLI** | Scripts, automation, tools | Application scope, no web-specific features |
| **Lambda** | Serverless functions | Application scope, cold start optimization |
| **Desktop** | Electron, JavaFX apps | Application scope, local persistence |

{% hint style="warning" %}
**Web-Only Scopes**: Features like `session`, `cookie`, `form`, `url`, and `cgi` scopes only exist in web runtimes. Structure your code to handle different runtime contexts gracefully.
{% endhint %}

## 📝 Complete Example

{% code title="Application.bx" %}

```js
class {

    // ========================================
    // APPLICATION IDENTITY
    // ========================================

    this.name = "MyAwesomeApp";
    // Never expires (preferred) - only set if you need auto-restart
    this.applicationTimeout = createTimeSpan( 0, 0, 0, 0 );

    // ========================================
    // SESSION MANAGEMENT (Web Runtime Only)
    // ========================================

    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan( 0, 0, 60, 0 ); // 1 hour
    this.sessionStorage = "default"; // Cache name or "memory"
    this.setClientCookies = true;
    this.setDomainCookies = false;

    // Session cookie configuration (web runtime only)
    this.sessionCookie = {
        httpOnly : true,      // Prevent JavaScript access
        secure : false,       // HTTPS only when true
        sameSite : false,     // Third-party cookie access
        sameSiteMode : "Lax", // "Strict", "Lax", or "None"
        timeout : createTimeSpan( 365, 0, 0, 0 )
    };

    // ========================================
    // DATASOURCES
    // ========================================

    this.datasource = "mainDB"; // Default datasource for any query or ORM

    this.datasources = {
        "mainDB" : {
            driver : "mysql",
            host : "localhost",
            port : 3306,
            database : "myapp",
            username : getSystemSetting( "DB_USER" ),
            password : getSystemSetting( "DB_PASS" )
        }
    };

    // ========================================
    // CACHING
    // ========================================

    this.caches = {
        "template" : {
            provider : "BoxCache",
            properties : {
                maxObjects : 200,
                defaultTimeout : 3600,
                evictionPolicy : "LRU"
            }
        }
    };

    // ========================================
    // MAPPINGS
    // ========================================

    this.mappings = {
        "/app" : expandPath( "./app" ),
        "/models" : expandPath( "./models" )
    };

    // ========================================
    // JAVA INTEGRATION
    // ========================================

    this.javaSettings = {
        loadPaths : [ expandPath( "./lib" ) ],
        loadSystemClassPath : false,
        reloadOnChange : false
    };

    // ========================================
    // CUSTOM SCHEDULERS
    // ========================================

    this.schedulers = [ "tasks.MaintenanceScheduler" ];

    // ========================================
    // LIFECYCLE EVENTS
    // ========================================

    function onApplicationStart() {
        application.startedAt = now();
        application.version = "1.0.0";
        return true;
    }

    function onApplicationEnd( struct applicationScope ) {
        // Cleanup logic
    }

    function onSessionStart() {
        session.startedAt = now();
    }

    function onSessionEnd( struct sessionScope, struct applicationScope ) {
        // Log session end, cleanup resources
    }

    function onRequestStart( string targetPage ) {
        // Security checks, request initialization
        return true; // Return false to abort request
    }

    function onRequest( string targetPage ) {
        // Wrap request with custom logic
        include arguments.targetPage;
    }

    function onRequestEnd() {
        // Cleanup, logging, metrics
    }

    function onError( any exception, string eventName ) {
        // Custom error handling
        writeLog( "Error in #eventName#: #exception.message#" );
        return true; // Return true if handled
    }

    function onAbort( required string targetPage ) {
        // Handle abort() calls
    }

    function onMissingTemplate( required string targetPage ) {
        // Custom 404 handling
        return false; // Return true if handled
    }

    function onClassRequest( className, method, struct args ) {
        // Intercept remote class invocations
    }
}
```
{% endcode %}

## ⚙️ Configuration Settings

All configuration settings are defined in the pseudo-constructor using the `this` scope. Here's a comprehensive reference of available settings:

### Core Application Settings

| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `this.name` | string | *Generated* | Unique application name. Defines the memory space reservation |
| `this.applicationTimeout` | timespan | 0,0,0,0 | Application lifetime. Default `0,0,0,0` = **never expires** (recommended) |
| `this.locale` | string | JVM locale | Default locale (e.g., "en_US", "es-ES") |
| `this.timezone` | string | JVM timezone | IANA timezone (e.g., "UTC", "America/New_York") |

### Session Management (Web Runtime)

| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `this.sessionManagement` | boolean | `false` | Enable session tracking |
| `this.sessionTimeout` | timespan | 0,0,30,0 | Session lifetime (30 minutes default) |
| `this.sessionStorage` | string | `"memory"` | Cache name for session storage or "memory" |
| `this.setClientCookies` | boolean | `true` | Automatically set session cookies |
| `this.setDomainCookies` | boolean | `false` | Share cookies across subdomains |

### Session Cookie Configuration (Web Runtime)

```js
this.sessionCookie = {
    httpOnly : true,              // Prevent JavaScript access
    secure : false,               // HTTPS only
    sameSite : false,             // Third-party cookie access
    sameSiteMode : "Lax",         // "Strict", "Lax", "None"
    timeout : createTimeSpan( 365, 0, 0, 0 )
};
```

### Datasources

| Setting | Type | Description |
| :--- | :--- | :--- |
| `this.datasource` | string | Default datasource name |
| `this.defaultDatasource` | string | Alias for `this.datasource` |
| `this.datasources` | struct | Datasource definitions |

**Example:**

```js
this.datasources = {
    "myDB" : {
        driver : "mysql",
        host : "localhost",
        database : "appdb",
        username : getSystemSetting( "DB_USER" ),
        password : getSystemSetting( "DB_PASS" )
    }
};
```

See [datasource configuration](/boxlang-language/syntax/datasources#datasource-configuration) for full configuration details.

### Caching

Define application-specific caches that BoxLang manages automatically:

```js
this.caches = {
    "template" : {
        provider : "BoxCache",
        properties : {
            maxObjects : 200,
            defaultTimeout : 3600,
            evictionPolicy : "LRU",
            objectStore : "ConcurrentStore"
        }
    }
};
```

See [Caching documentation](caching/) for full configuration details.

### Mappings

Define virtual paths for class and file resolution:

```js
this.mappings = {
    "/app" : expandPath( "./app" ),
    "/models" : expandPath( "./models" ),
    "/shared" : "/var/shared/libraries"
};
```

As of BoxLang 1.6.0, mappings support both simple (string) and complex (struct) formats:

```js
this.mappings = {
    // Simple format (external by default)
    "/public" : expandPath( "./public" ),

    // Complex format with external flag
    "/internal" : {
        path : expandPath( "./internal" ),
        external : false  // Not accessible via web
    }
};
```

### Java Integration

Load Java libraries and manage class loading:

```js
this.javaSettings = {
    loadPaths : [
        expandPath( "./lib" ),
        expandPath( "./jars/mylib.jar" )
    ],
    loadSystemClassPath : false,  // Include system classpath
    reloadOnChange : false        // Hot-reload on JAR changes
};
```

See [Java Integration documentation](java-integration.md) for details.

### Custom Schedulers

Register scheduler classes that run automatically:

```js
this.schedulers = [
    "schedulers.DailyMaintenance",
    "schedulers.HourlyReports"
];
```

See [Asynchronous Programming documentation](asynchronous-programming/) for scheduler details.

### Security Settings

| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `this.invokeImplicitAccessor` | boolean | *Context* | Enable implicit getters/setters |
| `this.allowedFileOperationExtensions` | array | *Runtime* | File extensions allowed for file operations |
| `this.disallowedFileOperationExtensions` | array | *Runtime* | File extensions disallowed for file operations |

### Advanced Settings

| Setting | Type | Description |
| :--- | :--- | :--- |
| `this.classPaths` | array | Global class paths for `.bx` files |
| `this.componentPaths` | array | Alias for `classPaths` |
| `this.customComponentPaths` | array | Custom component directories |

## 🔄 Lifecycle Events

`Application.bx` acts as a comprehensive event listener, with BoxLang automatically invoking callback methods at key moments in your application's lifecycle.

### Application Lifecycle

#### `onApplicationStart()`

**Executed once** when the application first starts - when the first request arrives and the application doesn't exist in memory.

```js
function onApplicationStart() {
    application.startTime = now();
    application.config = loadConfiguration();
    application.cache = createCache();

    // Return true to continue, false to abort
    return true;
}
```

**When it runs:**

* First request after server startup
* After application timeout expires
* After `applicationStop()` is called

#### `onApplicationEnd( struct applicationScope )`

**Executed once** when the application shuts down due to timeout or explicit stop.

```js
function onApplicationEnd( struct applicationScope ) {
    // Cleanup: close connections, save state, log metrics
    writeLog( "Application ended after #dateDiff( 's', applicationScope.startTime, now() )# seconds" );
}
```

### Session Lifecycle (Web Runtime Only)

#### `onSessionStart()`

**Executed** when a new user session begins.

```js
function onSessionStart() {
    session.userID = createUUID();
    session.startTime = now();
    session.requestCount = 0;
}
```

#### `onSessionEnd( struct sessionScope, struct applicationScope )`

**Executed** when a session expires or is explicitly terminated.

```js
function onSessionEnd( struct sessionScope, struct applicationScope ) {
    // Log user activity, cleanup session resources
    writeLog( "Session #sessionScope.userID# ended after #sessionScope.requestCount# requests" );
}
```

{% hint style="warning" %}
Session events only fire in **web runtimes** with `sessionManagement = true`.
{% endhint %}

### Request Lifecycle

#### `onRequestStart( string targetPage )`

**Executed** at the start of every request, **before** the target page is processed.

```js
function onRequestStart( string targetPage ) {
    // Security checks
    if ( !isUserLoggedIn() && !isPublicPage( arguments.targetPage ) ) {
        relocate( "/login" );
        return false; // Abort request
    }

    // Request initialization
    request.startTime = getTickCount();
    session.requestCount++;

    return true; // Continue processing
}
```

**Return Value:**

* `true` - Continue processing the request
* `false` - Abort the request (no further processing)

#### `onRequest( string targetPage )`

**Wraps** the entire request execution. You control if/how the target page is included.

```js
function onRequest( string targetPage ) {
    try {
        // Before advice
        setupRequestContext();

        // Execute the target page
        include arguments.targetPage;

        // After advice (only if no errors)
        logSuccessfulRequest();
    }
    catch ( any e ) {
        // Handle request-level errors
        renderErrorPage( e );
    }
}
```

{% hint style="info" %}
**Pattern**: Think of `onRequestStart()` as "before advice" and `onRequest()` as "around advice" in AOP terms. If you implement `onRequest()`, you **must** include the target page yourself.
{% endhint %}

#### `onRequestEnd()`

**Executed** after the request completes, even if errors occurred.

```js
function onRequestEnd() {
    // Logging, metrics, cleanup
    var duration = getTickCount() - request.startTime;
    writeLog( "Request completed in #duration#ms" );
}
```

### Error Handling

#### `onError( any exception, string eventName )`

**Global error handler** - catches any unhandled exceptions in your application.

```js
function onError( any exception, string eventName ) {
    // Log the error
    writeLog(
        type = "error",
        file = "application",
        text = "Error in #eventName#: #exception.message#"
    );

    // Custom error page
    include "errors/500.bxm";

    // Return true if handled, false to let BoxLang handle it
    return true;
}
```

**Parameters:**

* `exception` - The exception struct with `message`, `detail`, `type`, `stacktrace`, etc.
* `eventName` - Which lifecycle event threw the error (e.g., "onRequestStart", "onApplicationStart")

#### `onAbort( required string targetPage )`

**Executed** when `abort()` is called anywhere in the request.

```js
function onAbort( required string targetPage ) {
    writeLog( "Request aborted from: #arguments.targetPage#" );
}
```

### Special Handlers

#### `onMissingTemplate( required string targetPage )`

**Executed** when a requested template doesn't exist - your custom 404 handler.

```js
function onMissingTemplate( required string targetPage ) {
    // Custom 404 logic
    response.setStatus( 404 );
    include "errors/404.bxm";

    // Return true if handled, false for BoxLang's default 404
    return true;
}
```

#### `onClassRequest( className, method, struct args )`

**Intercepts** remote class invocations (HTTP/AMF calls to BoxLang classes).

```js
function onClassRequest( className, method, struct args ) {
    // Security, logging, custom routing
    if ( !hasRemoteAccess( arguments.className, arguments.method ) ) {
        throw( "Access denied" );
    }

    // Delegate to the actual class
    var instance = createObject( arguments.className );
    return invoke( instance, arguments.method, arguments.args );
}
```

### Execution Order

```
📍 Application Starts (first request)
   ↓
1. onApplicationStart()
   ↓
📍 New Session (web runtime)
   ↓
2. onSessionStart()
   ↓
📍 Request Arrives
   ↓
3. onRequestStart( targetPage )
   ↓
4. onRequest( targetPage )  ← Your template executes here
   ↓
5. onRequestEnd()
   ↓
📍 Session Expires
   ↓
6. onSessionEnd( sessionScope, applicationScope )
   ↓
📍 Application Expires
   ↓
7. onApplicationEnd( applicationScope )
```

{% hint style="success" %}
**Framework Integration**: The [ColdBox HMVC Framework](https://www.coldbox.org) leverages these lifecycle methods to provide a rich event-driven architecture. Create a ColdBox app: `coldbox create app MyApp`
{% endhint %}

## 🏗️ Virtual Applications - A Critical Feature

One of BoxLang's most powerful capabilities is the ability to create **multiple virtual applications** within a single JVM process. Each application is a **memory space reservation** with isolated scopes and settings.

### How Virtual Applications Work

Each `Application.bx` with a unique `this.name` creates a separate virtual application. These applications:

✅ Have their own isolated `application` scope
✅ Have their own isolated `session` scopes (web runtime)
✅ Can have completely different settings and configurations
✅ Share the same JVM but are logically independent
✅ Can be nested or side-by-side in the directory structure

### Example: Multiple Apps in One Server

```
📁 /var/www/
   📄 Application.bx                    ← Public website app
      this.name = "PublicSite"
   📄 index.bxm

   📁 /admin/
      📄 Application.bx                 ← Admin console app
         this.name = "AdminConsole"
      📄 dashboard.bxm

   📁 /api/
      📄 Application.bx                 ← REST API app
         this.name = "RestAPI"
      📄 handler.bx
```

**Result**: Three independent applications running in the same JVM:
* `PublicSite` - Public website with 30-day application timeout
* `AdminConsole` - Admin area with 1-hour session timeout and different datasource
* `RestAPI` - API endpoints with no session management

### Practical Example

{% code title="/Application.bx (Root)" %}
```js
class {
    this.name = "PublicWebsite";
    this.sessionTimeout = createTimeSpan( 0, 0, 30, 0 ); // 30 minutes
    this.datasource = "public_db";

    function onApplicationStart() {
        application.maxUsers = 10000;
        application.theme = "light";
    }
}
```
{% endcode %}

{% code title="/admin/Application.bx (Nested)" %}
```js
class {
    this.name = "AdminPanel"; // Different application!
    this.sessionTimeout = createTimeSpan( 0, 0, 5, 0 ); // 5 minutes for security
    this.datasource = "admin_db";

    this.sessionCookie = {
        httpOnly : true,
        secure : true,
        sameSiteMode : "Strict"
    };

    function onApplicationStart() {
        application.maxUsers = 10; // Admin-specific setting
        application.theme = "admin-dark";
    }

    function onRequestStart( string targetPage ) {
        // Admin-specific security
        if ( !session.isAdmin ) {
            relocate( "/admin/login" );
            return false;
        }
        return true;
    }
}
```
{% endcode %}

### Scope Isolation

```js
// In /index.bxm (PublicWebsite app)
application.counter = 100;
echo( application.counter ); // 100

// In /admin/dashboard.bxm (AdminPanel app)
echo( application.counter ); // undefined! Different application scope
application.counter = 500;

// Back in /index.bxm
echo( application.counter ); // Still 100! Isolated
```

### Application Longevity

**Applications live in memory** for the duration specified by `this.applicationTimeout`:

```js
// Default: Never expires (preferred)
this.applicationTimeout = createTimeSpan( 0, 0, 0, 0 );

// Or set a specific timeout if you need auto-restart
this.applicationTimeout = createTimeSpan( 7, 0, 0, 0 ); // 7 days
```

{% hint style="success" %}
**Recommended**: Keep the default `0,0,0,0` (never expires) unless you have a specific need for applications to restart automatically. This provides better performance and stability.
{% endhint %}

**When an application expires:**
1. `onApplicationEnd()` is called
2. Application scope is destroyed
3. Next request triggers `onApplicationStart()` and creates a new application instance

**Manual Control:**

```js
// Force application restart
applicationStop();

// Check if application exists
isDefined( "application" );

// Application-specific cache clearing
cacheRemoveAll( cacheName = "template" );
```

{% hint style="info" %}
**Why you can't "kill" the application scope**: Applications are time-based memory reservations. They expire automatically based on `applicationTimeout` or when explicitly stopped with `applicationStop()`.
{% endhint %}

### Use Cases for Virtual Applications

🎯 **Multi-Tenant SaaS**
```
/tenant1/Application.bx (name: "Tenant1", datasource: "tenant1_db")
/tenant2/Application.bx (name: "Tenant2", datasource: "tenant2_db")
```

🎯 **Microservices Architecture**
```
/users/Application.bx     (name: "UserService")
/orders/Application.bx    (name: "OrderService")
/payments/Application.bx  (name: "PaymentService")
```

🎯 **Environment Separation**
```
/dev/Application.bx  (name: "DevApp", datasource: "dev_db")
/qa/Application.bx   (name: "QAApp", datasource: "qa_db")
/prod/Application.bx (name: "ProdApp", datasource: "prod_db")
```

🎯 **Legacy Migration**
```
/legacy/Application.bx (name: "OldApp", CFML compatibility mode)
/modern/Application.bx (name: "NewApp", pure BoxLang features)
```

{% hint style="success" %}
**Best Practice**: Use descriptive, unique application names. Avoid dynamic names unless you understand the implications for memory management.
{% endhint %}

## 📚 Additional Resources

* **Configuration**: See [Configuration documentation](../getting-started/configuration/) for runtime-level settings
* **Caching**: See [Caching documentation](caching/) for cache strategies
* **Async**: See [Asynchronous Programming](asynchronous-programming/) for schedulers and executors
* **Datasources**: See [Datasource configuration](../getting-started/configuration/datasources.md)
* **Java Integration**: See [Java Integration](java-integration.md) for loading Java libraries

{% hint style="info" %}
**CFML Compatibility**: For CFML compatibility reference, see [CFDocs Application.cfc](https://cfdocs.org/application-cfc). BoxLang supports the majority of CFML Application.cfc features with enhanced capabilities.
{% endhint %}
