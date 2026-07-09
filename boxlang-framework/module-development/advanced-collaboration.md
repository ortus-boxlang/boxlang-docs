---
description: Advanced integration patterns, system setting providers, custom class resolvers, and inter-module communication
icon: handshake
---

# Advanced Collaboration

Modules can integrate deeply with the BoxLang runtime through system setting providers, custom class resolvers, and runtime configuration APIs.

## System Setting Providers

Modules can register custom providers for the `getSystemSetting()` BIF, enabling centralized configuration management from various sources.

### How It Works

The `getSystemSetting()` BIF checks registered providers in order before falling back to environment variables.

### Registering a Provider

{% tabs %}
{% tab title="ModuleConfig.bx" %}
```js
function onLoad() {
    boxRuntime.getConfiguration().registerSystemSettingProvider(
        "my-settings",
        ( settingName ) => {
            // Only handle your prefixed settings
            if ( settingName.startsWith( "MYAPP_" ) ) {
                return lookupFromDatabase( settingName )
            }
            // Return null to let other providers try
            return null
        }
    )
}

function onUnload() {
    boxRuntime.getConfiguration().unregisterSystemSettingProvider( "my-settings" )
}
```
{% endtab %}

{% tab title="Java IModuleConfig" %}
```java
@Override
public void onLoad( IBoxContext context, ModuleRecord record ) {
    record.boxRuntime.getConfiguration().registerSystemSettingProvider(
        Key.of( "my-settings" ),
        ( settingName, ctx ) -> {
            if ( settingName.startsWith( "MYAPP_" ) ) {
                return lookupFromDatabase( settingName );
            }
            return null;
        }
    );
}

@Override
public void onUnload( IBoxContext context, ModuleRecord record ) {
    record.boxRuntime.getConfiguration()
        .unregisterSystemSettingProvider( Key.of( "my-settings" ) );
}
```
{% endtab %}
{% endtabs %}

### Provider Resolution Order

When `getSystemSetting("MY_KEY")` is called:

1. **Named providers** checked in registration order
2. **Default provider** (environment variables)
3. **Returns null** if not found

{% hint style="warning" %}
Always return `null` from your provider if you don't handle the setting. This allows other providers to attempt resolution.
{% endhint %}

## Custom Class Resolvers

Register custom class resolvers with unique prefixes (extending the built-in `bx:` and `java:` resolvers).

### Built-in Resolvers

| Prefix | Resolver | Purpose |
|--------|----------|---------|
| `java:` | JavaResolver | Load Java classes explicitly |
| `bx:` | BoxResolver | Load BoxLang components/classes |

### Creating a Custom Resolver

Implement the `IClassResolver` interface:

```java
package ortus.boxlang.modules.mymodule.resolvers;

import ortus.boxlang.runtime.context.IBoxContext;
import ortus.boxlang.runtime.loader.ClassLocation;
import ortus.boxlang.runtime.loader.resolvers.IClassResolver;

import java.util.Optional;

public class CustomResolver implements IClassResolver {

    public String getName() { return "Custom Resolver"; }

    public String getPrefix() { return "custom"; }

    public Optional<ClassLocation> resolve(
        IBoxContext context, String name
    ) {
        // Your resolution logic
        try {
            var instance = resolveFromYourSource( name );
            return Optional.of(
                new ClassLocation( instance.getClass(), instance )
            );
        } catch ( Exception e ) {
            return Optional.empty();
        }
    }

    // Also implement the resolve() variant with imports parameter
}
```

**Registration in ModuleConfig.bx:**

```js
function onLoad() {
    var classLocator = boxRuntime.getClassLocator()
    classLocator.registerResolver(
        createObject( "java",
            "ortus.boxlang.modules.mymodule.resolvers.CustomResolver"
        )
    )
}

function onUnload() {
    boxRuntime.getClassLocator().unregisterResolver( "custom" )
}
```

### Usage After Registration

```js
// Import using your custom prefix
import custom:MyService
service = new MyService()

// Create directly
service = new custom:MyService( arg1 = "value" )
```

## Runtime Configuration APIs

### Registering Additional Mappings

```js
function onLoad() {
    // Register a custom mapping beyond the defaults
    boxRuntime.getConfiguration().registerMapping(
        "api",
        moduleRecord.path & "/api"
    )
}
```

### Modifying Runtime Settings

```js
function onLoad() {
    var config = boxRuntime.getConfiguration()

    // Enable nested transactions
    if ( structKeyExists( config, "enableNestedTransactions" ) ) {
        config.enableNestedTransactions = true
    }
}
```

{% hint style="danger" %}
Modifying runtime configuration affects ALL applications. Only do this if you understand the implications. Document changes clearly in your module README.
{% endhint %}

## Best Practices

{% stepper %}
{% step %}
### Always Clean Up

Unregister providers and resolvers in `onUnload()`. Use try/catch so one failure doesn't prevent other cleanup.

{% endstep %}

{% step %}
### Return Null Gracefully

System setting providers must return `null` for settings they don't handle.

{% endstep %}

{% step %}
### Use Unique Names

Prefix provider and resolver names with your module name to avoid conflicts: `mymodule-settings`, `mymodule-custom`.

{% endstep %}

{% step %}
### Test Isolation

Verify your module works when loaded/unloaded multiple times and alongside other modules.
{% endstep %}
{% endstepper %}

## Next Steps

- [Packaging & Publishing](packaging-publishing.md) — Build and distribute your module
- [Testing](testing.md) — TestBox integration and CI/CD patterns
- [Troubleshooting](troubleshooting.md) — Common issues and solutions
