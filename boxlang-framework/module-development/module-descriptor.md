---
description: Configure your BoxLang module with box.json, ModuleConfig.bx, and Java IModuleConfig descriptors
icon: file-code
---

# Module Descriptor

Every BoxLang module needs a descriptor that defines its identity, metadata, and configuration. You can use **`box.json`** (required metadata file) plus either **`ModuleConfig.bx`** (BoxLang) or a Java **`IModuleConfig`** class.

## box.json — Module Metadata

The `box.json` file is the standard CommandBox package descriptor with BoxLang-specific extensions:

```json
{
  "name": "My Amazing Module",
  "version": "1.0.0",
  "author": "Your Name",
  "slug": "bx-my-module",
  "shortDescription": "Does amazing things",
  "type": "boxlang-modules",
  "keywords": ["boxlang", "module"],
  "boxlang": {
    "minimumVersion": "1.14.0",
    "moduleName": "myModule",
    "executable": "my-module",
    "completions": "completions/my-module.bash"
  },
  "dependencies": {
    "bx-plus": "*"
  },
  "devDependencies": {
    "commandbox-boxlang": "*",
    "testbox": "*"
  },
  "ignore": [
    "**/.*",
    "build.gradle",
    "/src/**",
    "gradle/**"
  ]
}
```

### Key Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Display name of the module |
| `version` | ✅ | Semver version |
| `slug` | ✅ | Unique identifier (used by ForgeBox) |
| `boxlang.moduleName` | ⚠️ | Runtime registration name. Falls back to directory name |
| `boxlang.minimumVersion` | ⚠️ | Minimum BoxLang version required |
| `boxlang.executable` | | Name of a CLI wrapper script the OS installer generates for this module. See [CLI Executables and Completions](#cli-executables-and-completions) |
| `boxlang.executables` | | Map of `name` → script content for multiple CLI wrapper scripts. See [CLI Executables and Completions](#cli-executables-and-completions) |
| `boxlang.completions` | | Path (relative to the module root) to a bash completion script the OS installer installs. See [CLI Executables and Completions](#cli-executables-and-completions) |
| `dependencies` | | Runtime dependencies (other modules) |
| `ignore` | | Files to exclude from distribution |
| `type` | | Set to `"boxlang-modules"` for BoxLang modules |

## CLI Executables and Completions

{% hint style="info" %}
These `boxlang.*` fields are only processed by the **operating system installer** (`install-bx-module`, part of the [BoxLang Quick Installer](../../getting-started/installation/boxlang-quick-installer.md) / [BVM](../../getting-started/installation/boxlang-version-manager-bvm.md)). They have no effect when a module is installed via CommandBox's `box install`.
{% endhint %}

A module installed with `install-bx-module` can ship its own CLI wrapper script(s) and a bash completion script. The installer wires them up automatically — no extra steps for the end user.

### `boxlang.executable` — Single CLI Wrapper

Declare a single executable name, and the installer generates a wrapper script that calls your module through `boxlang module:<moduleName>`:

```json
{
  "boxlang": {
    "moduleName": "myModule",
    "executable": "my-module"
  }
}
```

Installing this module creates an executable named `my-module` (equivalent to `boxlang module:myModule "$@"`) on the `PATH` — at `~/.boxlang/bin/my-module` for a global install, or `./boxlang_modules/.bin/my-module` with `install-bx-module --local`.

### `boxlang.executables` — Multiple CLI Wrappers

For more than one entry point, or a wrapper that needs custom logic, declare a map of executable name to the wrapper script's full content:

```json
{
  "boxlang": {
    "moduleName": "myModule",
    "executables": {
      "my-module": "#!/bin/sh\nboxlang module:myModule \"$@\"\n",
      "my-module-admin": "#!/bin/sh\nboxlang module:myModule admin \"$@\"\n"
    }
  }
}
```

Each key becomes an executable file in the same bin directory as `boxlang.executable`, written verbatim from its value and marked executable.

{% hint style="warning" %}
`boxlang.executable` and `boxlang.executables` can be combined — both are processed independently.
{% endhint %}

### `boxlang.completions` — Bash Completions

Ship a bash completion script inside your module and point `boxlang.completions` at its path, relative to the module root:

```json
{
  "boxlang": {
    "completions": "completions/my-module.bash"
  }
}
```

The script itself is a normal, self-registering bash completion function:

```bash
#!/usr/bin/env bash
_my_module_complete() {
    local current_word="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=($(compgen -W "migrate seed generate" -- "$current_word"))
}
complete -F _my_module_complete my-module
```

On install, the script is copied to `~/.boxlang/completions/<module-name>.sh` (or `./boxlang_modules/.completions/<module-name>.sh` with `--local`), and removed again when the module is removed. Every script in that directory is auto-sourced by `bvm-init.sh` in new Bash/Zsh sessions — nothing further is required in the user's shell profile as long as [BVM's shell initialization](../../getting-started/installation/boxlang-version-manager-bvm.md) is installed.

## ModuleConfig.bx — BoxLang Descriptor

The `ModuleConfig.bx` file defines your module's behavior through properties and lifecycle methods. It's a BoxLang class that gets several properties injected at runtime.

### Anatomy

```js
class {
    // ── Injected Properties ──────────────────────────
    property name="moduleRecord";
    property name="boxRuntime";
    property name="log";
    property name="interceptorService";
    property name="functionService";
    property name="componentService";
    property name="cacheService";
    property name="asyncService";
    property name="schedulerService";
    property name="datasourceService";

    // ── Module Properties ────────────────────────────
    this.version      = "1.0.0";
    this.mapping      = "myModule";       // Internal mapping name
    this.author       = "Your Name";
    this.description  = "My module";
    this.webURL       = "https://example.com";
    this.enabled      = true;             // false = skip registration
    this.dependencies = [];               // Module names to activate first

    // ── Lifecycle: Registration ──────────────────────
    function configure() {
        // Module settings (merged with runtime boxlang.json)
        settings = {
            key: "value"
        };

        // Interceptors to register
        interceptors = [
            { class: "interceptors.Listener", properties: {} }
        ];

        // Custom interception points
        customInterceptionPoints = [
            "onMyCustomEvent"
        ];
    }

    // ── Lifecycle: Activation ────────────────────────
    function onLoad() {
        log.info( "Module activated!" );
    }

    // ── Lifecycle: Deactivation ──────────────────────
    function onUnload() {
        log.info( "Module deactivated!" );
    }
}
```

### Module Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `this.version` | string | ✅ | Semver version |
| `this.mapping` | string | | Custom internal mapping name. Default: module name |
| `this.author` | string | | Module author |
| `this.description` | string | | Module description |
| `this.webURL` | string | | Module website URL |
| `this.enabled` | boolean | | If `false`, module is skipped entirely |
| `this.dependencies` | string[] | | Module names that must activate first |

### Lifecycle Methods

| Method | When Called | Purpose |
|--------|-------------|---------|
| `configure()` | Registration | Define settings, interceptors, interception points |
| `onLoad()` | Activation | Module startup — dependencies are already active |
| `onUnload()` | Deactivation | Cleanup resources, unregister providers |

## Java IModuleConfig

For Java-based modules, implement the `IModuleConfig` interface:

```java
import ortus.boxlang.runtime.modules.BoxMapping;
import ortus.boxlang.runtime.modules.BoxModule;
import ortus.boxlang.runtime.modules.IModuleConfig;
import ortus.boxlang.runtime.context.IBoxContext;
import ortus.boxlang.runtime.modules.ModuleRecord;

@BoxModule(
    version     = "1.0.0",
    author      = "Your Name",
    description = "My module",
    webURL      = "https://example.com",
    enabled     = true,
    dependencies = {},
    mapping     = @BoxMapping("myModule")
)
public class MyModuleConfig implements IModuleConfig {

    @Override
    public void configure(IBoxContext context, ModuleRecord record) {
        record.settings.put(Key.of("key"), "value");
    }

    @Override
    public void onLoad(IBoxContext context, ModuleRecord record) {
        System.out.println("Module activated!");
    }

    @Override
    public void onUnload(IBoxContext context, ModuleRecord record) {
        System.out.println("Module deactivated!");
    }
}
```

Register via ServiceLoader in `META-INF/services/ortus.boxlang.runtime.modules.IModuleConfig`:

```
ortus.boxlang.modules.mymodule.MyModuleConfig
```

### @BoxModule Annotation Fields

| Field | Type | Description |
|-------|------|-------------|
| `version` | String | Semver version |
| `author` | String | Module author |
| `description` | String | Module description |
| `webURL` | String | Module website URL |
| `enabled` | boolean | If `false`, module is skipped |
| `dependencies` | String[] | Module names to activate first |
| `mapping` | @BoxMapping | Internal mapping configuration |
| `publicMapping` | @BoxMapping | Public web mapping configuration |

## Descriptor Priority

If both `ModuleConfig.bx` and a Java `IModuleConfig` exist:

{% hint style="warning" %}
**Java wins.** The `ModuleConfig.bx` is completely ignored when a Java `IModuleConfig` is discovered via ServiceLoader.
{% endhint %}

This means:
- Use `ModuleConfig.bx` only for pure BoxLang modules
- Use Java `IModuleConfig` for Java+BoxLang modules
- You can keep a `ModuleConfig.bx` as fallback/documentation, but it won't be used if Java is present

## Next Steps

- [Lifecycle](lifecycle.md) — Understand the registration and activation flow
- [Configuration](configuration.md) — Settings, overrides, and dependency management
- [Mappings & Class Resolution](mappings.md) — Module mappings and `@moduleName` notation
