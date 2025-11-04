---
description: High-performance thread-safe in-memory cache store using concurrent hash maps
icon: gauge-high
---

# ConcurrentStore

The ConcurrentStore is the default and most commonly used object store in BoxCache. It provides high-performance, thread-safe in-memory caching using Java's `ConcurrentHashMap` for optimal concurrent access patterns. This store is ideal for frequently accessed data that doesn't need to persist across application restarts.

## ✨ Features

* **High Performance**: Lightning-fast read/write operations using concurrent hash maps
* **Thread-Safe**: Built-in concurrency control for multi-threaded environments
* **Memory-Based**: Stores all data in RAM for maximum speed
* **Eviction Support**: Compatible with all BoxCache eviction policies (LRU, LFU, FIFO, LIFO, RANDOM)
* **No External Dependencies**: Pure in-memory storage with no disk or database requirements

## 📋 Configuration Example

```json
"myCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentStore",
        "maxObjects": 1000,
        "evictionPolicy": "LRU",
        "evictCount": 100,
        "defaultTimeout": 3600,
        "defaultLastAccessTimeout": 1800,
        "reapFrequency": 300
    }
}
```

## ⚙️ Configuration Properties

The ConcurrentStore uses all standard BoxCache properties and has no store-specific configuration options. All caching behavior is controlled through the global BoxCache properties:

### maxObjects (recommended)

The maximum number of objects to store in the cache. Default is `1000`.

```json
"maxObjects": 5000
```

### evictionPolicy

The eviction policy to use when the cache reaches capacity. Options: `LRU`, `LFU`, `FIFO`, `LIFO`, `RANDOM`. Default is `LRU`.

```json
"evictionPolicy": "LRU"
```

### evictCount

How many objects to evict when the cache reaches capacity. Default is `1`.

```json
"evictCount": 100
```

### defaultTimeout

The maximum time in seconds to keep an object in the cache regardless of access. `0` = never expire. Default is `3600` (1 hour).

```json
"defaultTimeout": 7200
```

### defaultLastAccessTimeout

The maximum time in seconds since last access before an object expires. Default is `1800` (30 minutes).

```json
"defaultLastAccessTimeout": 3600
```

### reapFrequency

How often (in seconds) to check for and remove expired objects. Default is `120` (2 minutes).

```json
"reapFrequency": 300
```

### resetTimeoutOnAccess

If `true`, the last access timeout resets on every access (session-like behavior). Default is `false`.

```json
"resetTimeoutOnAccess": true
```

### useLastAccessTimeouts

If `true`, the last access timeout is used for eviction. Default is `true`.

```json
"useLastAccessTimeouts": true
```

### freeMemoryPercentageThreshold

Trigger eviction when free memory falls below this percentage (0-100). `0` = disabled. Default is `0`.

```json
"freeMemoryPercentageThreshold": 10
```

## 💡 Usage Examples

### High-Performance Application Cache

```json
"appCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentStore",
        "maxObjects": 10000,
        "evictionPolicy": "LRU",
        "evictCount": 500,
        "defaultTimeout": 3600,
        "reapFrequency": 300
    }
}
```

### Query Result Cache

```json
"queryCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentStore",
        "maxObjects": 5000,
        "evictionPolicy": "LFU",
        "defaultTimeout": 1800,
        "defaultLastAccessTimeout": 900
    }
}
```

### API Response Cache

```json
"apiCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentStore",
        "maxObjects": 2000,
        "evictionPolicy": "LRU",
        "defaultTimeout": 600,
        "freeMemoryPercentageThreshold": 15
    }
}
```

## 🎯 Best Practices

{% hint style="success" %}
**When to Use ConcurrentStore:**

* High-traffic applications requiring fast cache access
* Frequently accessed data that changes regularly
* Query caching and API response caching
* Session-like data that doesn't need persistence
* Development and testing environments
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

* Set `maxObjects` based on your memory availability and data size
* Use `LRU` eviction for most general-purpose caching scenarios
* Tune `reapFrequency` based on your cache churn rate (lower for high churn)
* Monitor memory usage and adjust `freeMemoryPercentageThreshold` if needed
* Consider `evictCount` for bulk eviction when cache pressure is high
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

* **Not Persistent**: All cached data is lost on application restart
* **Memory Usage**: Stored objects consume heap memory - monitor JVM heap size
* **Not Distributed**: Each application instance maintains its own cache
* **Garbage Collection**: Large caches can impact GC performance - tune appropriately
{% endhint %}

## 🔗 Related Resources

* [BoxCache Overview](../README.md)
* [Cache Configuration](../../../getting-started/configuration/caches.md)
* [Eviction Policies](../custom-eviction-policies.md)
* [ConcurrentSoftReferenceStore](concurrent-soft-reference-store.md) - Memory-sensitive alternative
* [FileSystemStore](file-system-store.md) - For persistent caching needs
* [JDBCStore](jdbc-store.md) - For distributed caching scenarios
