---
description: Complete module lifecycle from discovery through registration, activation, and deactivation
icon: arrows-spin
---

# Module Lifecycle

BoxLang modules follow a well-defined lifecycle with distinct phases, each firing events that your module can listen to.

## Lifecycle Overview

```mermaid
graph TD
    A[Discovery] --> B[Registration]
    B --> C[Activation]
    C --> D[Running]
    D --> E[Deactivation]
    E --> F[Unloaded]

    B --> |interceptors registered| B1[PRE_MODULE_REGISTRATION]
    B --> |BIFs, components, services loaded| B2[POST_MODULE_REGISTRATION]
    C --> |dependencies activated first| C1[PRE_MODULE_LOAD]
    C --> |onLoad() called| C2[POST_MODULE_LOAD]
    E --> |onUnload() called| E1[PRE_MODULE_UNLOAD]
    E --> |cleanup complete| E2[POST_MODULE_UNLOAD]
```

## Phase 1: Discovery

When the runtime starts, the `ModuleService` scans configured paths for directories containing `ModuleConfig.bx` or `box.json`.

**What happens:**
- Each discovered module becomes a `ModuleRecord` in the registry
- Duplicates are resolved first-come-first-served
- Module name is determined from `box.json` `boxlang.moduleName` or directory name

**No events fire during discovery.**

## Phase 2: Registration

Each module is registered in the order discovered. Registration loads the descriptor and prepares the module but does **not** make it active.

{% stepper %}
{% step %}
### PRE_MODULE_REGISTRATION Event

Fires before the module descriptor is loaded. The `moduleRecord` and `moduleName` are available in the event data.

```boxlang
function preModuleRegistration( event ) {
    var moduleName = event.getData().moduleName
    log.info( "About to register: #moduleName#" )
}
```

{% endstep %}

{% step %}
### Load Descriptor

The descriptor (`ModuleConfig.bx` or Java `IModuleConfig`) is loaded. The module's class loader is created with isolation from other modules.

{% endstep %}

{% step %}
### Configure the Module

The `configure()` method is called:
- Module `settings` struct is populated
- Interceptors are registered from the `interceptors` array
- Custom interception points are added

{% endstep %}

{% step %}
### Discover Capabilities

Auto-discovery scans for:
- `bifs/` → BoxLang BIF files compiled and registered
- `components/` → BoxLang components registered
- ServiceLoader entries → Java BIFs, components, services, schedulers, cache providers
- `public/` → Public web folder mapping

{% endstep %}

{% step %}
### POST_MODULE_REGISTRATION Event

Fires after the module is fully registered. All module capabilities are available.

{% endstep %}
{% endstepper %}

**After all modules are registered**, the `AFTER_MODULE_REGISTRATIONS` event fires.

## Phase 3: Activation

Activation makes the module "live" in the runtime. Dependencies are activated first (recursively).

{% stepper %}
{% step %}
### Resolve Dependencies

Dependencies declared in `this.dependencies` are activated in order before this module.

{% endstep %}

{% step %}
### PRE_MODULE_LOAD Event

Fires before `onLoad()` is called. All dependencies are already active at this point.

{% endstep %}

{% step %}
### onLoad() Called

The `onLoad()` lifecycle method executes. This is where you:
- Register system setting providers
- Register custom class resolvers
- Modify runtime configuration
- Initialize module state
- Check for other loaded modules

{% endstep %}

{% step %}
### POST_MODULE_LOAD Event

Fires after `onLoad()` completes successfully.

{% endstep %}
{% endstepper %}

**After all modules are activated**, the `AFTER_MODULE_ACTIVATIONS` event fires, followed by `ON_MODULE_SERVICE_STARTUP`.

## Phase 4: Running

The module is active and all its capabilities are available to the runtime:
- BIFs are callable from BoxLang code
- Components are usable as `bx:` tags
- Interceptors are listening for events
- Services are available via `BoxRuntime`

## Phase 5: Deactivation (Shutdown)

When the runtime shuts down or a module is explicitly unloaded:

{% stepper %}
{% step %}
### ON_MODULE_SERVICE_SHUTDOWN Event

Fires when the module service begins shutdown.

{% endstep %}

{% step %}
### PRE_MODULE_UNLOAD Event

Fires before `onUnload()` is called.

{% endstep %}

{% step %}
### onUnload() Called

The `onUnload()` lifecycle method executes. Clean up:
- Unregister system setting providers
- Unregister class resolvers
- Close connections and resources
- Remove any runtime modifications

{% hint style="warning" %}
Always wrap `onUnload()` cleanup in try/catch blocks. If one module's cleanup fails, it shouldn't prevent other modules from unloading.
{% endhint %}

{% endstep %}

{% step %}
### Cleanup

The module service automatically:
- Unregisters all interceptors
- Unregisters JDBC drivers
- Removes global services
- Unregisters mappings
- Closes the module class loader

{% endstep %}

{% step %}
### POST_MODULE_UNLOAD Event

Fires after cleanup is complete.

{% endstep %}
{% endstepper %}

## Lifecycle Events Reference

| Event | Phase | Data |
|-------|-------|------|
| `PRE_MODULE_REGISTRATION` | Registration | `moduleRecord`, `moduleName` |
| `POST_MODULE_REGISTRATION` | Registration | `moduleRecord`, `moduleName` |
| `AFTER_MODULE_REGISTRATIONS` | Registration | `moduleRegistry` |
| `PRE_MODULE_LOAD` | Activation | `moduleRecord`, `moduleName` |
| `POST_MODULE_LOAD` | Activation | `moduleRecord`, `moduleName` |
| `AFTER_MODULE_ACTIVATIONS` | Activation | `moduleRegistry` |
| `ON_MODULE_SERVICE_STARTUP` | Activation | `moduleService` |
| `ON_MODULE_SERVICE_SHUTDOWN` | Deactivation | `moduleService` |
| `PRE_MODULE_UNLOAD` | Deactivation | `moduleRecord`, `moduleName` |
| `POST_MODULE_UNLOAD` | Deactivation | `moduleRecord`, `moduleName` |

## Listening to Events

Your `ModuleConfig.bx` can listen to any lifecycle event by defining a matching method:

```boxlang
class {
    // Called when any module finishes loading
    function postModuleLoad( event ) {
        var moduleName = event.getData().moduleName
        log.info( "Module loaded: #moduleName#" )
    }

    // Called when all modules are active
    function onModuleServiceStartup( event ) {
        log.info( "All modules are ready!" )
        initializeIntegrations()
    }
}
```

{% hint style="info" %}
Your module config file is also registered as an interceptor automatically, so any runtime event method you define will be called.
{% endhint %}

## Version Compatibility

During registration, the module's `minimumVersion` (from `box.json`) is checked against the running BoxLang version using semver:

- **Major version lower** → Module is rejected with an error
- **Minor/patch version lower** → Module loads but logs a warning

{% hint style="info" %}
In development mode (BoxLang version `0.x.x`), version checks are skipped entirely.
{% endhint %}

## Next Steps

- [Capabilities](capabilities/) — Learn what modules can provide
- [Configuration](configuration.md) — Settings and runtime overrides
- [Advanced Collaboration](advanced-collaboration.md) — System settings providers and class resolvers
