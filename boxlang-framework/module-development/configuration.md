---
description: Configure module settings, dependencies, and runtime overrides
icon: sliders
---

# Configuration

Module settings are defined in `configure()` and can be overridden at runtime through `boxlang.json`. Modules can also declare dependencies on other modules.

## Module Settings

Define settings in your descriptor's `configure()` method:

{% tabs %}
{% tab title="ModuleConfig.bx" %}
```boxlang
function configure() {
    settings = {
        apiKey: "",
        timeout: 30,
        debug: false,
        endpoints: {
            primary: "https://api.example.com/v1",
            fallback: "https://api.example.com/v2"
        }
    };
}
```
{% endtab %}

{% tab title="Java IModuleConfig" %}
```java
@Override
public void configure( IBoxContext context, ModuleRecord record ) {
    record.settings.put( Key.of( "apiKey" ), "" );
    record.settings.put( Key.of( "timeout" ), 30 );
    record.settings.put( Key.of( "debug" ), false );

    IStruct endpoints = new Struct();
    endpoints.put( Key.of( "primary" ), "https://api.example.com/v1" );
    endpoints.put( Key.of( "fallback" ), "https://api.example.com/v2" );
    record.settings.put( Key.of( "endpoints" ), endpoints );
}
```
{% endtab %}
{% endtabs %}

## Runtime Overrides

Users can override module settings in `boxlang.json`:

```json
{
  "modules": {
    "myModule": {
      "enabled": true,
      "settings": {
        "apiKey": "sk-abc123",
        "debug": true
      }
    }
  }
}
```

### Merge Behavior

Runtime settings are **deep-merged** on top of `configure()` defaults:

| configure() setting | boxlang.json override | Effective value |
|---------------------|-----------------------|-----------------|
| `apiKey: ""` | `apiKey: "sk-abc123"` | `"sk-abc123"` (overridden) |
| `timeout: 30` | (not set) | `30` (default preserved) |
| `debug: false` | `debug: true` | `true` (overridden) |
| `endpoints.primary` | (not set) | `"https://api..."` (nested preserved) |

## Disabling Modules

Modules can be disabled via runtime config:

```json
{
  "modules": {
    "myModule": {
      "enabled": false
    }
  }
}
```

The module is still discovered but skipped during registration — no BIFs, components, or services are loaded.

## Accessing Settings

Access module settings from anywhere:

```boxlang
// From ModuleConfig.bx
var timeout = settings.timeout

// From module code
var moduleService = boxRuntime.getModuleService()
var settings = moduleService.getModuleSettings( "myModule" )
var timeout = settings.timeout
```

## Dependencies

Declare module dependencies to control activation order:

{% tabs %}
{% tab title="ModuleConfig.bx" %}
```boxlang
class {
    this.dependencies = [ "bx-plus", "bx-compat-cfml" ];
}
```
{% endtab %}

{% tab title="Java @BoxModule" %}
```java
@BoxModule( dependencies = { "bx-plus", "bx-compat-cfml" } )
public class MyModuleConfig implements IModuleConfig { }
```
{% endtab %}
{% endtabs %}

**How dependencies work:**
- Dependencies are activated **before** the dependent module
- Resolution is recursive (a dependency's dependencies are also activated first)
- Missing dependencies cause a warning but don't prevent activation
- Use `box.json` `dependencies` for ForgeBox package dependencies

{% hint style="info" %}
`this.dependencies` controls activation order, while `box.json` `dependencies` controls package installation. Both should list your module's dependencies.
{% endhint %}

## Inter-Module Communication

Check for and interact with other loaded modules:

```boxlang
function onLoad() {
    var moduleService = boxRuntime.getModuleService()

    // Check if another module is loaded
    if ( moduleService.hasModule( "bx-spreadsheet" ) ) {
        var spreadsheetSettings = moduleService.getModuleSettings( "bx-spreadsheet" )
        // Read or modify (use cautiously)
    }
}
```

## Next Steps

- [Advanced Collaboration](advanced-collaboration.md) — System settings providers and class resolvers
- [Packaging & Publishing](packaging-publishing.md) — Build and distribute your module
- [Testing](testing.md) — TestBox integration and CI/CD patterns
