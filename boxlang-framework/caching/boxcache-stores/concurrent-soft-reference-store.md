---
description: Memory-sensitive cache store using Java soft references for automatic memory management
icon: memory
---

# ConcurrentSoftReferenceStore

The ConcurrentSoftReferenceStore is a memory-aware variant of the ConcurrentStore that uses Java's soft references to allow the JVM's garbage collector to reclaim memory when the system is under memory pressure. This store is ideal for applications with constrained memory or highly variable memory requirements.

## ✨ Features

* **Memory-Sensitive**: Automatically releases memory when the JVM needs it
* **Soft Reference Management**: Leverages Java's `SoftReference` for intelligent memory handling
* **Thread-Safe**: Built-in concurrency control for multi-threaded environments
* **Automatic Cleanup**: JVM garbage collector manages memory reclamation
* **Eviction Support**: Compatible with all BoxCache eviction policies (LRU, LFU, FIFO, LIFO, RANDOM)
* **No Memory Leaks**: Cached objects can be garbage collected when memory is low

## 📋 Configuration Example

```json
"memorySensitiveCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentSoftReferenceStore",
        "maxObjects": 5000,
        "evictionPolicy": "LRU",
        "evictCount": 250,
        "defaultTimeout": 3600,
        "defaultLastAccessTimeout": 1800,
        "reapFrequency": 300,
        "freeMemoryPercentageThreshold": 15
    }
}
```

## ⚙️ Configuration Properties

The ConcurrentSoftReferenceStore uses all standard BoxCache properties and has no store-specific configuration options. The `freeMemoryPercentageThreshold` property is particularly useful with this store for proactive eviction before memory pressure occurs.

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
"evictCount": 250
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

### freeMemoryPercentageThreshold (recommended)

Trigger eviction when free memory falls below this percentage (0-100). `0` = disabled. Default is `0`.

**This property is especially important for ConcurrentSoftReferenceStore** to proactively manage memory before the JVM triggers garbage collection.

```json
"freeMemoryPercentageThreshold": 15
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

## 💡 Usage Examples

### Large Object Cache

```json
"largeObjectCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentSoftReferenceStore",
        "maxObjects": 1000,
        "evictionPolicy": "LRU",
        "evictCount": 100,
        "defaultTimeout": 3600,
        "freeMemoryPercentageThreshold": 20
    }
}
```

### Image/Asset Cache

```json
"assetCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentSoftReferenceStore",
        "maxObjects": 500,
        "evictionPolicy": "LFU",
        "defaultTimeout": 7200,
        "defaultLastAccessTimeout": 3600,
        "freeMemoryPercentageThreshold": 15
    }
}
```

### Document Processing Cache

```json
"documentCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentSoftReferenceStore",
        "maxObjects": 2000,
        "evictionPolicy": "LRU",
        "defaultTimeout": 1800,
        "reapFrequency": 600,
        "freeMemoryPercentageThreshold": 10
    }
}
```

## 🎯 Best Practices

{% hint style="success" %}
**When to Use ConcurrentSoftReferenceStore:**

* Applications with limited or variable memory availability
* Caching large objects (images, documents, parsed data)
* Environments where memory pressure varies significantly
* Development/testing with constrained resources
* Caching data that can be easily regenerated if evicted by GC
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

* Set `freeMemoryPercentageThreshold` to trigger proactive eviction (recommended: 10-20%)
* Use lower `maxObjects` values than ConcurrentStore due to soft reference overhead
* Tune `evictCount` for bulk eviction to reduce GC pressure
* Monitor GC logs to understand memory reclamation patterns
* Consider using `LRU` eviction policy for predictable behavior
* Objects may disappear between checks due to GC - design for cache misses
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

* **Unpredictable Eviction**: JVM may reclaim objects at any time when memory is low
* **Performance Overhead**: Soft references have slight overhead compared to strong references
* **Not Persistent**: All cached data is lost on application restart
* **Not Distributed**: Each application instance maintains its own cache
* **GC Dependency**: Cache behavior depends on JVM garbage collection strategy
* **Cache Misses**: Applications must handle cache misses gracefully as objects can be GC'd unexpectedly
{% endhint %}

## 🔬 How Soft References Work

Soft references in Java allow the garbage collector to reclaim objects when memory is needed, but keep them around as long as memory is available. This provides a balance between performance and memory efficiency:

1. **Normal Operation**: Objects remain cached as long as memory is available
2. **Memory Pressure**: JVM automatically reclaims soft-referenced objects during GC
3. **Cache Miss Handling**: Application regenerates data when soft references are cleared
4. **Automatic Recovery**: Cache rebuilds naturally as data is accessed again

This makes ConcurrentSoftReferenceStore ideal for "nice-to-have" caches where performance is important but not critical, and data can be regenerated when needed.

## 🔗 Related Resources

* [BoxCache Overview](../README.md)
* [Cache Configuration](../../../getting-started/configuration/caches.md)
* [Eviction Policies](../custom-eviction-policies.md)
* [ConcurrentStore](concurrent-store.md) - For guaranteed in-memory caching
* [FileSystemStore](file-system-store.md) - For persistent caching needs
* [JDBCStore](jdbc-store.md) - For distributed caching scenarios
