---
description: Disk-based persistent cache store with file system storage for durability across restarts
icon: hard-drive
---

# FileSystemStore

The FileSystemStore leverages disk-based storage to persist cache items as serialized entities on the file system. This store provides durability across application restarts and is highly efficient for caching scenarios that require persistence without the complexity of a database.

## ✨ Features

* **Persistent Storage**: Cache survives application restarts
* **Efficient Serialization**: Uses optimized Java serialization for fast read/write operations
* **File-Based Management**: Each cache entry stored as a separate file for easy inspection
* **Automatic Cleanup**: Expired entries are automatically removed during reaping
* **Directory-Based Organization**: Simple file system structure for cache storage
* **Eviction Support**: Compatible with all BoxCache eviction policies (LRU, LFU, FIFO, LIFO, RANDOM)

## 📋 Configuration Example

```json
"diskCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "FileSystemStore",
        "directory": "/var/caches/app_cache",
        "maxObjects": 5000,
        "evictionPolicy": "LRU",
        "evictCount": 50,
        "defaultTimeout": 7200,
        "defaultLastAccessTimeout": 3600,
        "reapFrequency": 300
    }
}
```

## ⚙️ Configuration Properties

### directory (required)

The absolute path of the directory that will hold all the serialized cache entries on disk. The directory will be created if it doesn't exist (requires appropriate file system permissions).

```json
"directory": "/var/caches/myapp"
```

{% hint style="warning" %}
**File System Permissions:**

* Ensure the BoxLang runtime has read/write permissions to the specified directory
* Use absolute paths to avoid ambiguity
* Consider disk space availability for large caches
* Regular disk maintenance may be needed for long-running applications
{% endhint %}

### Standard BoxCache Properties

The FileSystemStore supports all standard BoxCache configuration properties:

#### maxObjects (recommended)

The maximum number of objects to store in the cache. Default is `1000`.

```json
"maxObjects": 5000
```

#### evictionPolicy

The eviction policy to use when the cache reaches capacity. Options: `LRU`, `LFU`, `FIFO`, `LIFO`, `RANDOM`. Default is `LRU`.

```json
"evictionPolicy": "LRU"
```

#### evictCount

How many objects to evict when the cache reaches capacity. Default is `1`.

```json
"evictCount": 50
```

#### defaultTimeout

The maximum time in seconds to keep an object in the cache regardless of access. `0` = never expire. Default is `3600` (1 hour).

```json
"defaultTimeout": 7200
```

#### defaultLastAccessTimeout

The maximum time in seconds since last access before an object expires. Default is `1800` (30 minutes).

```json
"defaultLastAccessTimeout": 3600
```

#### reapFrequency

How often (in seconds) to check for and remove expired objects. Default is `120` (2 minutes).

```json
"reapFrequency": 300
```

#### resetTimeoutOnAccess

If `true`, the last access timeout resets on every access (session-like behavior). Default is `false`.

```json
"resetTimeoutOnAccess": false
```

#### useLastAccessTimeouts

If `true`, the last access timeout is used for eviction. Default is `true`.

```json
"useLastAccessTimeouts": true
```

## 💡 Usage Examples

### Template Compilation Cache

```json
"templateCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "FileSystemStore",
        "directory": "/var/caches/templates",
        "maxObjects": 10000,
        "evictionPolicy": "LRU",
        "defaultTimeout": 0,
        "reapFrequency": 600
    }
}
```

### Application Configuration Cache

```json
"configCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "FileSystemStore",
        "directory": "/var/caches/config",
        "maxObjects": 500,
        "evictionPolicy": "FIFO",
        "defaultTimeout": 86400
    }
}
```

### Asset Processing Cache

```json
"assetCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "FileSystemStore",
        "directory": "/var/caches/assets",
        "maxObjects": 2000,
        "evictionPolicy": "LFU",
        "defaultTimeout": 3600,
        "defaultLastAccessTimeout": 1800,
        "reapFrequency": 300
    }
}
```

## 🎯 Best Practices

{% hint style="success" %}
**When to Use FileSystemStore:**

* Application configuration caches that should survive restarts
* Compiled template caches for faster startup times
* Asset processing results (image thumbnails, compiled assets)
* Data that's expensive to regenerate but doesn't change frequently
* Development/staging environments where persistence is valuable
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

* **SSD Recommended**: Use solid-state drives for better I/O performance
* **Separate Volume**: Consider using a dedicated disk volume for cache storage
* **Directory Structure**: Each cache entry is a separate file for easy management
* **Disk Space**: Monitor available disk space and set appropriate `maxObjects`
* **Reap Frequency**: Tune `reapFrequency` based on cache churn rate
* **Eviction Strategy**: Use `LRU` for most scenarios, `LFU` for stable access patterns
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

* **Not Distributed**: Each application instance maintains its own file-based cache
* **I/O Performance**: File system performance depends on disk speed (SSDs strongly recommended)
* **Serialization**: Only Java-serializable objects can be cached
* **File System Limits**: Some file systems have limits on files per directory
* **Disk Space**: Monitor disk usage to prevent out-of-space errors
* **Permissions**: Ensure proper file system permissions for the cache directory
* **Backup/Restore**: Cache directories can be backed up but may become stale
{% endhint %}

## 🗂️ File System Structure

The FileSystemStore creates a simple, flat directory structure:

```
/var/caches/app_cache/
├── cache_entry_key1.ser
├── cache_entry_key2.ser
├── cache_entry_key3.ser
└── ...
```

Each cache entry is stored as a separate `.ser` file named after the cache key (with special characters escaped). This makes it easy to:

* Inspect cache contents using file system tools
* Manually clear specific cache entries if needed
* Backup/restore cache data
* Monitor cache size using disk usage tools

## 🔗 Related Resources

* [BoxCache Overview](../README.md)
* [Cache Configuration](../../../getting-started/configuration/caches.md)
* [Eviction Policies](../custom-eviction-policies.md)
* [ConcurrentStore](concurrent-store.md) - For in-memory caching
* [JDBCStore](jdbc-store.md) - For distributed caching scenarios
* [BlackHoleStore](black-hole-store.md) - For testing without persistence
