---
description: Understanding BoxLang module isolation, class loading, and service discovery architecture
icon: diagram-project
---

# Module Architecture

BoxLang modules operate within an isolated architecture that prevents classpath conflicts, enables independent lifecycle management, and supports automatic discovery of capabilities.

## Core Principles

{% columns %}
{% column %}

**Isolation**
Each module receives its own class loader, preventing dependency conflicts between modules.

{% endcolumn %}

{% column %}

**Convention over Configuration**
Standard folder names (`bifs/`, `components/`, `libs/`, `public/`) are auto-discovered without explicit registration.

{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}

**Unified Interface**
Both BoxLang descriptors (`ModuleConfig.bx`) and Java descriptors (`IModuleConfig`) share the same lifecycle contract.

{% endcolumn %}

{% column %}

**ServiceLoader Discovery**
Java capabilities (BIFs, services, schedulers) are discovered via Java's standard ServiceLoader mechanism.

{% endcolumn %}
{% endcolumns %}

## Class Loader Isolation

```
Runtime ClassLoader (BoxLang core)
    ├── Module A ClassLoader
    │   ├── modules.moduleA.*  (compiled classes)
    │   ├── libs/*.jar         (dependencies)
    │   └── bifs/*.bx          (compiled at runtime)
    │
    ├── Module B ClassLoader
    │   ├── modules.moduleB.*
    │   ├── libs/*.jar
    │   └── components/*.bx
    │
    └── (parent fallback for runtime classes)
```

Each module's class loader loads:

1. **Compiled classes** from the `modules.{moduleName}` package prefix
2. **JAR files** from the module's `libs/` directory
3. **BoxLang files** from `bifs/` and `components/` (compiled at runtime)

If a class isn't found, the loader falls back to the parent (runtime) class loader.

{% hint style="info" %}
This isolation means two modules can bundle different versions of the same library without conflict.
{% endhint %}

## Discovery Process

When the runtime starts, modules are discovered through a multi-step process:

{% stepper %}
{% step %}
### Scan Module Paths

The `ModuleService` walks configured module directories (from `boxlang.json` `modulesDirectory` setting) looking for folders containing `ModuleConfig.bx` or `box.json`.

**Default paths:**
- `./modules/`
- `{runtime-home}/modules/`
- Any paths added via `addModulePath()`

{% endstep %}

{% step %}
### Build Registry

Each discovered module becomes a `ModuleRecord` in the registry. Duplicates are resolved first-come-first-served (first path scanned wins).

The module name is determined by:
1. `box.json` → `boxlang.moduleName`
2. Falls back to the directory name

{% endstep %}

{% step %}
### Load Descriptor

The descriptor (`ModuleConfig.bx` or Java `IModuleConfig`) is loaded to determine:
- Module metadata (version, author, dependencies)
- Configuration (settings, interceptors)
- Custom registration logic

{% endstep %}

{% step %}
### Discover Capabilities

Auto-discovery scans for:
- `bifs/` → BoxLang BIF files
- `components/` → BoxLang component files
- ServiceLoader entries → Java BIFs, components, services, schedulers, cache providers, JDBC drivers
- `public/` → Public web folder mapping

{% endstep %}
{% endstepper %}

## Module Class Packaging

Java-compiled classes in a module must follow the package convention:

```
modules.{moduleName}.{rest-of-package}
```

For example, a module named `myModule` with a class `MyService`:

```
src/main/java/modules/myModule/MyService.java
```

This ensures the module's class loader can find and isolate the class correctly.

{% hint style="warning" %}
Classes not under the `modules.{moduleName}` package prefix are loaded from the parent class loader, which may cause version conflicts with other modules.
{% endhint %}

## Dual Descriptor Priority

A module can provide both `ModuleConfig.bx` and a Java `IModuleConfig`. When both exist:

**Java `IModuleConfig` wins** — the `ModuleConfig.bx` is ignored entirely.

This allows hybrid modules to use the most appropriate descriptor while keeping a BoxLang fallback for simpler configurations.

For details on both descriptor formats, see [Module Descriptor](module-descriptor.md).

## Next Steps

- [Module Descriptor](module-descriptor.md) — Configure `box.json` and your descriptor
- [Lifecycle](lifecycle.md) — Complete registration and activation flow
- [Mappings & Class Resolution](mappings.md) — How classes are addressed and loaded
