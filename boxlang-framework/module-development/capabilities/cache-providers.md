---
description: Register custom cache providers in your BoxLang module (Java only)
icon: database
---

# Cache Providers

{% hint style="warning" %}
Cache providers require **Java**. There is no BoxLang-only mechanism for registering custom cache backends.
{% endhint %}

Cache providers enable custom caching backends (Redis, Couchbase, custom stores) for BoxLang's caching system.

## Creating a Cache Provider

Implement the `ICacheProvider` interface and register via ServiceLoader:

**File:** `src/main/java/ortus/boxlang/modules/mymodule/cache/MyCacheProvider.java`

```java
import ortus.boxlang.runtime.cache.providers.ICacheProvider;
import ortus.boxlang.runtime.scopes.Key;

public class MyCacheProvider implements ICacheProvider {

    @Override
    public Key getName() {
        return Key.of( "MyCache" );
    }

    @Override
    public void configure( IStruct config ) {
        // Configure provider from settings
    }

    @Override
    public Object get( Key key ) {
        // Retrieve from your cache
    }

    @Override
    public void put( Key key, Object value, Long timeout ) {
        // Store in your cache
    }

    @Override
    public void clear( Key key ) {
        // Remove from your cache
    }

    // ... other ICacheProvider methods
}
```

**ServiceLoader Config:** `src/main/resources/META-INF/services/ortus.boxlang.runtime.cache.providers.ICacheProvider`

```
ortus.boxlang.modules.mymodule.cache.MyCacheProvider
```

## Usage

Once registered, users can configure your cache provider in `boxlang.json`:

```json
{
  "caches": {
    "custom": {
      "provider": "MyCache",
      "properties": {
        "maxObjects": 1000,
        "defaultTimeout": 3600
      }
    }
  }
}
```

```boxlang
// Use the custom cache
cachePut( "myKey", "myValue", 60, "custom" )
result = cacheGet( "myKey", "custom" )
```

## Next Steps

- [Services](services.md) — Global runtime services (Java only)
- [Schedulers](schedulers.md) — Scheduled task management (Java only)
- [JDBC Drivers](jdbc-drivers.md) — Database driver registration (Java only)
