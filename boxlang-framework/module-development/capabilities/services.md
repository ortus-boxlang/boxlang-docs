---
description: Register global runtime services in your BoxLang module (Java only)
icon: server
---

# Services

{% hint style="warning" %}
Services require **Java**. There is no BoxLang-only mechanism for registering global runtime services.
{% endhint %}

Global services extend the BoxLang runtime with persistent, singleton functionality available across the entire application lifecycle.

## Creating a Service

Implement the `IService` interface and register via ServiceLoader:

**File:** `src/main/java/ortus/boxlang/modules/mymodule/services/MyService.java`

```java
import ortus.boxlang.runtime.services.IService;
import ortus.boxlang.runtime.BoxRuntime;
import ortus.boxlang.runtime.scopes.Key;

public class MyService implements IService {

    @Override
    public Key getName() {
        return Key.of( "MyService" );
    }

    @Override
    public void onStartup( BoxRuntime runtime ) {
        System.out.println( "MyService started!" );
    }

    @Override
    public void onShutdown( Boolean force ) {
        System.out.println( "MyService shutting down!" );
    }

    @Override
    public void onConfigurationLoad() {
        // Called when configuration is loaded
    }
}
```

**ServiceLoader Config:** `src/main/resources/META-INF/services/ortus.boxlang.runtime.services.IService`

```
ortus.boxlang.modules.mymodule.services.MyService
```

## Accessing Services

Once registered, your service can be accessed via:

```java
// From Java
MyService service = (MyService) BoxRuntime.getInstance()
    .getGlobalService( Key.of( "MyService" ) );
```

```boxlang
// From BoxLang
var service = boxRuntime.getGlobalService( "MyService" )
```

## Service Lifecycle

Services follow the same lifecycle as the runtime:

1. `onConfigurationLoad()` — Called when `boxlang.json` is loaded
2. `onStartup()` — Called when the runtime starts
3. `onShutdown()` — Called when the runtime shuts down

{% hint style="info" %}
Services are registered during module registration and activated during module activation. See [Lifecycle](../lifecycle.md) for details.
{% endhint %}

## Next Steps

- [Schedulers](schedulers.md) — Scheduled task management (Java only)
- [Cache Providers](cache-providers.md) — Custom caching backends (Java only)
- [JDBC Drivers](jdbc-drivers.md) — Database driver registration (Java only)
