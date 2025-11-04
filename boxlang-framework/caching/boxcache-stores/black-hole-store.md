---
description: Mock cache store for testing and development that discards all data
icon: flask
---

# BlackHoleStore

The BlackHoleStore is a special-purpose mock cache store that simulates cache behavior without actually storing any data. All cache operations (set, get, clear) succeed immediately but no data is retained. This store is invaluable for testing, development, and performance benchmarking scenarios where you need to isolate application logic from caching concerns.

## ✨ Features

* **Zero Storage**: No data is actually stored - all operations are no-ops
* **Instant Operations**: All cache operations complete immediately with minimal overhead
* **Testing-Friendly**: Perfect for unit tests and integration tests
* **Cache Simulation**: Provides a valid cache interface without side effects
* **No Dependencies**: No memory, disk, or database requirements
* **Performance Benchmarking**: Isolate application performance from cache overhead

## 📋 Configuration Example

```json
"mockCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "BlackHoleStore"
    }
}
```

## ⚙️ Configuration Properties

The BlackHoleStore has no store-specific configuration properties and ignores all standard BoxCache properties since no data is stored. You can include standard BoxCache properties for compatibility, but they have no effect:

```json
"testCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "BlackHoleStore",
        "maxObjects": 1000,
        "evictionPolicy": "LRU",
        "defaultTimeout": 3600
    }
}
```

All configuration properties are accepted but ignored since the BlackHoleStore never stores data.

## 💡 Usage Examples

### Unit Testing Cache

```json
"testCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "BlackHoleStore"
    }
}
```

### Development Environment

```json
"devCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "BlackHoleStore"
    }
}
```

### Performance Benchmarking

```json
"benchmarkCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "BlackHoleStore"
    }
}
```

## 🎯 Best Practices

{% hint style="success" %}
**When to Use BlackHoleStore:**

* **Unit Tests**: Test cache-dependent code without actual caching side effects
* **Integration Tests**: Isolate tests from cache state and persistence
* **Development**: Quickly disable caching without code changes
* **Performance Testing**: Measure application performance without cache overhead
* **Debugging**: Isolate caching-related issues by disabling cache storage
* **CI/CD Pipelines**: Fast test execution without cache setup/teardown
{% endhint %}

{% hint style="info" %}
**Behavior Details:**

* **set()**: Always succeeds immediately, discards the value
* **get()**: Always returns `null` (cache miss)
* **clear()**: Always succeeds immediately (no-op)
* **getKeys()**: Always returns empty array
* **getSize()**: Always returns `0`
* **lookup()**: Always returns `false` (not found)
* **eviction**: Never triggers (no data to evict)
* **expiration**: Never occurs (no data to expire)
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

* **No Data Storage**: All cached data is immediately discarded
* **Always Cache Miss**: All get operations return null/not found
* **Not for Production**: Never use in production environments
* **Testing Only**: Designed exclusively for testing and development
* **No Persistence**: Obviously provides no persistence across restarts
* **No Distribution**: Not distributed (but also not local - it's nowhere!)
{% endhint %}

## 🧪 Testing Patterns

### Testing Cache-Dependent Code

```js
// Application code works the same way
cache = cacheGet( "testCache" );

// Set always succeeds (but stores nothing)
cache.set( "key", "value" );

// Get always returns null (cache miss)
result = cache.get( "key" ); // null

// Your code should handle cache misses gracefully
if ( isNull( result ) ) {
    result = loadFromDatabase();
}
```

### Performance Benchmarking

```js
// Benchmark with caching
cache = cacheGet( "realCache" );
startTime = getTickCount();
for ( i = 1; i <= 10000; i++ ) {
    cache.set( "key_#i#", generateData() );
}
cacheTime = getTickCount() - startTime;

// Benchmark without caching overhead
cache = cacheGet( "blackHoleCache" );
startTime = getTickCount();
for ( i = 1; i <= 10000; i++ ) {
    cache.set( "key_#i#", generateData() );
}
noCacheTime = getTickCount() - startTime;

// Compare results
cacheOverhead = cacheTime - noCacheTime;
```

### Environment-Specific Configuration

Use the BlackHoleStore in specific environments by configuring different cache providers:

```js
// Application.bx
this.caches = {
    "myCache": {
        "provider": "BoxCacheProvider",
        "properties": {
            // Production: Use real cache
            "objectStore": isProduction() ? "ConcurrentStore" : "BlackHoleStore",
            "maxObjects": 1000,
            "evictionPolicy": "LRU"
        }
    }
};
```

## 🔍 Implementation Notes

The BlackHoleStore implements the full BoxCache object store interface but all operations are optimized to do nothing:

* **Zero Allocation**: No memory allocation for cached objects
* **No I/O**: No disk or network operations
* **Minimal CPU**: Operations complete in nanoseconds
* **Thread-Safe**: Safe for concurrent access (by doing nothing!)
* **GC-Friendly**: Generates no garbage for collection

This makes it perfect for high-iteration tests where actual cache storage would create overhead or side effects.

## 🔗 Related Resources

* [BoxCache Overview](../README.md)
* [Cache Configuration](../../../getting-started/configuration/caches.md)
* [Testing Guide](../../../extra-credit/testing.md)
* [ConcurrentStore](concurrent-store.md) - For real in-memory caching
* [FileSystemStore](file-system-store.md) - For persistent caching
* [JDBCStore](jdbc-store.md) - For distributed caching
