---
description: Overview of module capabilities that extend the BoxLang runtime with BIFs, components, interceptors, services, and more
icon: puzzle-piece
---

# Module Capabilities

Modules extend the BoxLang runtime by providing **capabilities** — new functionality that integrates seamlessly with the core language. Choose pure BoxLang for rapid development or Java for performance-critical features.

## What Are Capabilities?

Capabilities are the building blocks modules contribute to BoxLang:

{% columns %}
{% column %}

**Built-In Functions (BIFs)**
Custom functions available globally or as member methods

**Components**
XML-style tags (`<bx:mytag>`) for markup-based logic

**Interceptors**
Event listeners responding to runtime lifecycle events

{% endcolumn %}

{% column %}

**Services**
Singleton runtime services accessible globally

**Schedulers**
Cron-like scheduled tasks with fluent API

**Cache Providers**
Custom caching backends (Redis, Memcached, etc.)

**JDBC Drivers**
Database connectivity implementations

{% endcolumn %}
{% endcolumns %}

## Discovery Mechanism

BoxLang uses two discovery patterns:

{% tabs %}
{% tab title="Convention-Based (BoxLang)" %}

Place `.bx` files in standard folders:

```
mymodule/
├── bifs/           ← Auto-discovered BIFs
├── components/     ← Auto-discovered components
└── ModuleConfig.bx
```

Files are automatically:
- Compiled at runtime
- Registered with appropriate services
- Made available globally

**No configuration required** — just create the file.

{% endtab %}

{% tab title="ServiceLoader (Java)" %}

Register Java implementations via `META-INF/services/`:

```
src/main/resources/
└── META-INF/
    └── services/
        ├── ortus.boxlang.runtime.bifs.BIF
        ├── ortus.boxlang.runtime.services.IService
        └── ortus.boxlang.runtime.async.tasks.IScheduler
```

Java classes are:
- Discovered via ServiceLoader at module registration
- Loaded with the module's isolated class loader
- Registered during module activation

**Requires ServiceLoader config** files listing implementations.

{% endtab %}
{% endtabs %}

## Capability Matrix

| Capability | BoxLang | Java | Discovery | Primary Use Cases |
|------------|---------|------|-----------|-------------------|
| **[BIFs](bifs.md)** | ✅ `.bx` | ✅ `@BoxBIF` | Auto-discovery (BX) or ServiceLoader (Java) | String manipulation, data transformation, utilities |
| **[Components](components.md)** | ✅ `.bx` | ✅ `@BoxComponent` | Auto-discovery (BX) or ServiceLoader (Java) | UI widgets, markup generators, template logic |
| **[Interceptors](interceptors.md)** | ✅ via `configure()` | ✅ `@BoxInterceptor` | Registration in descriptor | Cross-cutting concerns, validation, security |
| **[Services](services.md)** | ❌ | ✅ `IService` | ServiceLoader | Global singletons, runtime integration |
| **[Schedulers](schedulers.md)** | ❌ | ✅ `IScheduler` | ServiceLoader | Cron jobs, periodic tasks, cleanup routines |
| **[Cache Providers](cache-providers.md)** | ❌ | ✅ `ICacheProvider` | ServiceLoader | Redis, Memcached, custom backends |
| **[JDBC Drivers](jdbc-drivers.md)** | ❌ | ✅ `java.sql.Driver` | ServiceLoader + runtime registration | MySQL, PostgreSQL, custom databases |

{% hint style="info" %}
**Java-only capabilities** require implementing specific interfaces and registering via ServiceLoader. They cannot be created in pure BoxLang.
{% endhint %}

## Decision Guide

### When to Use Each Capability

**Choose BIFs when:**
- Adding utility functions (string manipulation, data formatting)
- Creating domain-specific calculations
- Exposing simple APIs to BoxLang code
- Performance is not critical (BoxLang BIFs work well for most use cases)

**Choose Components when:**
- Building UI widgets or markup generators
- Creating template-based logic with attributes
- Generating HTML/XML output
- Wrapping complex operations in declarative syntax

**Choose Interceptors when:**
- Implementing cross-cutting concerns (logging, auditing, validation)
- Adding security guards or authorization checks
- Modifying request/response flow
- Integrating with runtime lifecycle events

**Choose Services when:**
- Building global runtime features (Java only)
- Managing shared state across the application
- Integrating with external systems that require initialization
- Providing APIs to other modules

**Choose Schedulers when:**
- Running periodic maintenance tasks (Java only)
- Implementing cron-like background jobs
- Scheduling cleanup or data synchronization
- Building task management systems

**Choose Cache Providers when:**
- Integrating custom caching backends (Java only)
- Wrapping Redis, Memcached, or proprietary systems
- Implementing application-specific caching strategies

**Choose JDBC Drivers when:**
- Adding database connectivity (Java only)
- Supporting proprietary or custom databases
- Wrapping existing JDBC drivers with BoxLang-specific features

### Combining Capabilities

Modules often combine multiple capabilities:

```
bx-redis (Java + BoxLang)
├── BIFs           → redisGet(), redisSet() (Java)
├── Cache Provider → Redis backend (Java)
├── Service        → Connection pooling (Java)
└── Interceptors   → Session storage (BoxLang)

bx-compat-cfml (BoxLang)
├── BIFs           → CF-compatible functions (BoxLang)
├── Components     → CF tags (BoxLang)
└── Interceptors   → Compatibility shims (BoxLang)
```

## Capability Reference

| Capability | Description | Link |
|------------|-------------|------|
| **Built-In Functions (BIFs)** | Custom functions available globally or as member methods | [BIFs →](bifs.md) |
| **Components** | XML-style tags for markup-based logic | [Components →](components.md) |
| **Interceptors** | Event listeners for runtime lifecycle hooks | [Interceptors →](interceptors.md) |
| **Services** | Global runtime services (Java only) | [Services →](services.md) |
| **Schedulers** | Scheduled tasks with fluent API (Java only) | [Schedulers →](schedulers.md) |
| **Cache Providers** | Custom caching backends (Java only) | [Cache Providers →](cache-providers.md) |
| **JDBC Drivers** | Database connectivity (Java only) | [JDBC Drivers →](jdbc-drivers.md) |

## Best Practices

{% stepper %}
{% step %}
### Start Simple

Begin with pure BoxLang BIFs and components for rapid prototyping. Migrate to Java only when:
- Performance profiling shows bottlenecks
- External Java libraries are required
- Global services or schedulers are needed

{% endstep %}

{% step %}
### Organize by Capability

Structure your module with clear capability folders:

```
mymodule/
├── bifs/              ← All BIFs here
├── components/        ← All components here
├── interceptors/      ← Interceptor classes
└── src/main/java/
    ├── services/      ← Service implementations
    └── schedulers/    ← Scheduler implementations
```

{% endstep %}

{% step %}
### Document Each Capability

Use Javadoc-style comments for all capabilities:

```boxlang
/**
 * Converts a string to title case
 *
 * @param input The string to convert
 * @return The title-cased string
 */
function invoke( required string input ) {
    // ...
}
```

See [Code Documenter](../../boxlang-code-documenter/) for conventions.

{% endstep %}

{% step %}
### Test Capabilities in Isolation

Write tests for each capability type:

```boxlang
describe( "MyBIF", () => {
    it( "should format strings correctly", () => {
        expect( myBIF( "hello world" ) ).toBe( "Hello World" )
    })
})
```

See [Testing Modules](../testing.md) for strategies.

{% endstep %}
{% endstepper %}

## Next Steps

- **[Getting Started](../getting-started.md)** — Set up your first module
- **[Architecture](../architecture.md)** — Understand module isolation and discovery
- **[Module Descriptor](../module-descriptor.md)** — Configure your module metadata
- **[Lifecycle](../lifecycle.md)** — Learn the module activation flow