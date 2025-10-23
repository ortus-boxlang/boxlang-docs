---
description: Premium Redis integration module delivering high-performance caching, data structures, and pub/sub for BoxLang+ applications.
icon: database
---

# 🧠 `bx-redis` Module

The `bx-redis` module adds Redis-backed services to your BoxLang application: advanced caching, pub/sub messaging, atomic counters, simple queues, and structured data operations.

## 🚀 Features

* Transparent cache provider integration (BoxCache)
* Named cache regions mapping to Redis keys/prefixes
* Atomic increment/decrement operations
* Publish/subscribe channels for lightweight messaging
* TTL & eviction control
* Optional JSON serialization for complex values
* Connection pooling & health checks

## 📦 Installation

```bash
box install bx-redis
```

## ⚙ Configuration

Configure via `boxlang.json` or environment variables. Example:

```jsonc
{
  "redis": {
    "host": "127.0.0.1",
    "port": 6379,
    "password": "secret", // optional
    "database": 0,
    "enablePubSub": true,
    "defaultTTLSeconds": 600
  }
}
```

Environment variable pattern:

```bash
export REDIS_HOST=127.0.0.1
export REDIS_PORT=6379
export REDIS_PASSWORD=secret
```

## 🔐 Entitlement

Requires an active BoxLang+ subscription (validated by `bx-plus`). If entitlement fails, the module degrades gracefully or throws a descriptive exception depending on context.

## 🧪 Basic Usage

```js
redis = moduleService.get( "bx-redis" );

// Set a cache value
redis.set( key = "app:welcome", value = "Hello BoxLang", ttl = 300 );

// Retrieve
message = redis.get( "app:welcome" );
writeOutput( message );

// Atomic counters
count = redis.incr( "metrics:visits" );

// Publish/Subscribe
redis.publish( channel = "events:user", message = { type: "login", userId: 42 } );
```

## 📡 Subscribing to Channels

```js
redis.subscribe( channel = "events:user", callback = function( msg ) {
    writeLog( text = "User event received: " & serializeJSON( msg ), type = "info" );
} );
```

## 🧰 Cache Provider Integration

When configured as a BoxCache provider, usage is seamless:

```js
cache = cacheService.getCache( "default" );
cache.put( id = "homepage", value = generateHomePageHTML(), timeout = 300 );
html = cache.get( "homepage" );
```

## 🛡 Error Handling

Use standard try/catch around network operations:

```js
try {
    redis.set( "critical:key", "value" );
} catch ( e ) {
    writeLog( text = "Redis write failed: " & e.message, type = "error" );
}
```

## 📎 Related Modules

{% content-ref url="bx-plus.md" %}
Subscription Bootstrap
{% endcontent-ref %}

{% content-ref url="bx-couchbase.md" %}
Couchbase Integration
{% endcontent-ref %}

---
Next: Process tabular data with the [`bx-csv` module](bx-csv.md).
