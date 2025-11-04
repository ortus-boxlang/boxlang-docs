---
description: BoxCache object stores provide the storage layer for cached data with different persistence and performance characteristics
icon: database
---

# BoxCache Object Stores

Object stores are the foundational storage layer of the BoxLang cache engine. They provide the actual mechanism for storing, retrieving, and managing cached objects in memory, on disk, or in distributed databases. While cache providers coordinate user interactions and act as a service layer, object stores handle the low-level data persistence and retrieval operations.

## 🏗️ Store Architecture

BoxCache's flexible architecture allows you to choose the right storage backend for your caching needs:

* **In-Memory Stores** - Fast, volatile storage for frequently accessed data
* **Disk-Based Stores** - Persistent storage that survives application restarts
* **Database-Backed Stores** - Distributed caching across multiple application instances
* **Special-Purpose Stores** - Testing and development utilities

## 📦 Available Object Stores

| Store | Type | Distributed | Best For |
|-------|------|-------------|----------|
| [ConcurrentStore](concurrent-store.md) | In-Memory | No | High-performance caching, frequently accessed data |
| [ConcurrentSoftReferenceStore](concurrent-soft-reference-store.md) | In-Memory | No | Memory-sensitive applications, automatic garbage collection support |
| [FileSystemStore](file-system-store.md) | Disk-Based | No | Persistent caching, application restarts, compiled templates |
| [JDBCStore](jdbc-store.md) | Database | Yes | Multi-server deployments, load-balanced environments, horizontal scaling |
| [BlackHoleStore](black-hole-store.md) | Mock | No | Testing, development, cache simulation |

## 🎯 Choosing the Right Store

### Performance Requirements

* **Maximum Speed** → `ConcurrentStore` - Thread-safe in-memory storage with minimal overhead
* **Memory Efficiency** → `ConcurrentSoftReferenceStore` - Allows JVM to reclaim memory under pressure
* **Persistence** → `FileSystemStore` - Survives restarts, ideal for compiled templates and configurations
* **Distribution** → `JDBCStore` - Share cache across multiple servers in clustered environments

### Use Case Examples

**High-Traffic Web Application:**

```json
{
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "ConcurrentStore",
        "maxObjects": 10000,
        "evictionPolicy": "LRU"
    }
}
```

**Multi-Server Deployment:**

```json
{
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "JDBCStore",
        "datasource": "sharedCache",
        "table": "app_cache"
    }
}
```

**Template Compilation Cache:**

```json
{
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "FileSystemStore",
        "directory": "/var/caches/templates"
    }
}
```

## 🔧 Common Configuration Properties

All object stores support the standard BoxCache configuration properties:

* `maxObjects` - Maximum number of cached items
* `evictionPolicy` - LRU, LFU, FIFO, LIFO, or RANDOM
* `evictCount` - Number of items to evict when limit is reached
* `defaultTimeout` - Time-to-live in seconds
* `defaultLastAccessTimeout` - Idle timeout in seconds
* `reapFrequency` - Cleanup frequency in seconds

Store-specific properties are documented on each store's individual page.

## 📚 Store-Specific Documentation

Click on any store below to view detailed configuration options, features, and usage examples:

* **[ConcurrentStore](concurrent-store.md)** - Thread-safe in-memory caching
* **[ConcurrentSoftReferenceStore](concurrent-soft-reference-store.md)** - Memory-sensitive caching with soft references
* **[FileSystemStore](file-system-store.md)** - Disk-based persistent caching
* **[JDBCStore](jdbc-store.md)** - Database-backed distributed caching (New in 1.7.0)
* **[BlackHoleStore](black-hole-store.md)** - Mock store for testing

## 🚀 Next Steps

1. **Choose your store** based on performance, persistence, and distribution requirements
2. **Review the specific store documentation** for configuration details
3. **Configure your cache** in `boxlang.json` or `Application.bx`
4. **Test your configuration** to ensure optimal performance

For general caching concepts and provider configuration, see the [Caching Overview](../README.md).
