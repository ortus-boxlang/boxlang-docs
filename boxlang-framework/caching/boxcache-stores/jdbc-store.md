---
description: Database-backed distributed cache store for multi-instance cache sharing across load-balanced environments
icon: database
---

# JDBCStore

**New in BoxLang 1.7.0** - The JDBCStore is a distributed cache store backed by JDBC databases, enabling cache sharing across multiple BoxLang instances. Perfect for horizontal scaling scenarios where multiple application servers need to share cached data in load-balanced or clustered environments.

## ✨ Features

* **Distributed Caching**: Share cache data across multiple application servers
* **Multi-Database Support**: Works with Oracle, MySQL, MariaDB, PostgreSQL, SQL Server, Derby, HSQLDB, and SQLite
* **Automatic Schema Management**: Creates tables and indexes automatically on first use
* **Optimized SQL**: Database-specific query optimization for each vendor
* **Full Eviction Support**: Compatible with all BoxCache eviction policies (LRU, LFU, FIFO, LIFO, RANDOM)
* **Production-Ready**: Battle-tested for enterprise environments
* **Distribution Detection**: Marks itself as `distributed = true` for ecosystem tool integration

## 📋 Configuration Example

```json
"distributedCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "JDBCStore",
        "datasource": "myDatasource",
        "table": "boxlang_cache",
        "autoCreate": true,
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

### datasource (required)

The name of the datasource to use for cache storage. The datasource must be configured in your BoxLang runtime.

```json
"datasource": "myDatasource"
```

The datasource should point to one of the supported databases with appropriate credentials and connection settings.

### table

The database table name for cache storage. Default is `"boxlang_cache"`.

```json
"table": "app_cache"
```

You can use different table names for different caches, allowing multiple cache instances to share the same database.

### autoCreate

Automatically create the cache table and indexes if they don't exist. Default is `true`.

```json
"autoCreate": true
```

When enabled, the JDBCStore will create a table with this structure:

```sql
CREATE TABLE boxlang_cache (
    objectKey VARCHAR(255) PRIMARY KEY,
    objectValue CLOB,
    hits INTEGER DEFAULT 0,
    timeout INTEGER DEFAULT 0,
    lastAccessTimeout INTEGER DEFAULT 0,
    created BIGINT,
    lastAccessed BIGINT,
    lastUpdated BIGINT,
    isExpired BOOLEAN DEFAULT FALSE
)
```

Indexes are automatically created on frequently queried columns for optimal performance:

* Primary key on `objectKey`
* Indexes on `created`, `lastAccessed`, and `hits` for efficient eviction queries
* Index on `isExpired` for faster reaping operations

{% hint style="info" %}
**Schema Management:**

* The table structure is optimized for each database vendor
* Indexes are created to support efficient eviction policies
* Data types are adjusted per database (CLOB vs TEXT vs NVARCHAR(MAX))
* No manual schema management required when `autoCreate = true`
{% endhint %}

### Standard BoxCache Properties

The JDBCStore supports all standard BoxCache configuration properties:

#### maxObjects (recommended)

The maximum number of objects to store in the cache. Default is `1000`.

```json
"maxObjects": 10000
```

#### evictionPolicy

The eviction policy to use when the cache reaches capacity. Options: `LRU`, `LFU`, `FIFO`, `LIFO`, `RANDOM`. Default is `LRU`.

```json
"evictionPolicy": "LRU"
```

#### evictCount

How many objects to evict when the cache reaches capacity. Default is `1`.

```json
"evictCount": 100
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

## 🗄️ Supported Databases

The JDBCStore automatically detects the database vendor and generates optimized SQL for:

| Database | Data Type | Eviction Strategy | Notes |
|----------|-----------|-------------------|-------|
| **Oracle** | CLOB | Optimized queries | Enterprise-grade performance |
| **MySQL / MariaDB** | LONGTEXT | LIMIT-based | Efficient bulk eviction |
| **PostgreSQL** | TEXT | Index-optimized | Advanced indexing strategies |
| **Microsoft SQL Server** | NVARCHAR(MAX) | TOP-based | Native SQL Server syntax |
| **Apache Derby** | CLOB | FETCH FIRST | Embedded database support |
| **HSQLDB** | CLOB | Vendor-specific | In-memory/disk hybrid |
| **SQLite** | TEXT | Simple queries | File-based database |

Each database vendor receives tailored SQL queries for:

* Efficient data insertion and updates
* Optimized eviction queries based on policy (LRU, LFU, etc.)
* Fast expiration checking and cleanup
* Index-aware query planning

## 💡 Usage Examples

### Multi-Server Web Application

```json
"sharedCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "JDBCStore",
        "datasource": "clusterDB",
        "table": "app_shared_cache",
        "autoCreate": true,
        "maxObjects": 10000,
        "evictionPolicy": "LRU",
        "evictCount": 500,
        "defaultTimeout": 3600,
        "reapFrequency": 300
    }
}
```

### Session Storage Across Instances

```json
"distributedSessions": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "JDBCStore",
        "datasource": "sessionDB",
        "table": "boxlang_sessions",
        "autoCreate": true,
        "maxObjects": 100000,
        "evictionPolicy": "LRU",
        "defaultTimeout": 1800,
        "resetTimeoutOnAccess": true,
        "reapFrequency": 120
    }
}
```

### API Rate Limiting Cache

```json
"rateLimitCache": {
    "provider": "BoxCacheProvider",
    "properties": {
        "objectStore": "JDBCStore",
        "datasource": "rateLimitDB",
        "table": "api_rate_limits",
        "autoCreate": true,
        "maxObjects": 50000,
        "evictionPolicy": "FIFO",
        "defaultTimeout": 60,
        "reapFrequency": 30
    }
}
```

## 🎯 Best Practices

{% hint style="success" %}
**When to Use JDBCStore:**

* Load-balanced environments with multiple application servers
* Horizontal scaling scenarios requiring shared cache state
* Session management across clustered instances
* Distributed rate limiting or feature flags
* Applications requiring cache persistence with multi-instance access
* Microservices architectures with shared data requirements
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

* **Connection Pool**: Ensure your datasource connection pool is properly sized (recommended: 10-50 connections per instance)
* **Database Selection**: Use PostgreSQL or MySQL for best performance in production
* **Indexing**: Let `autoCreate = true` handle index creation for optimal queries
* **Eviction**: Use higher `evictCount` values (100-500) for bulk eviction efficiency
* **Reaping**: Tune `reapFrequency` based on cache churn (300-600 seconds for most cases)
* **Network Latency**: Consider database proximity to application servers
* **Read Replicas**: Use database read replicas for read-heavy workloads
{% endhint %}

{% hint style="warning" %}
**Performance Considerations:**

* **Database I/O**: Cache operations depend on database performance - monitor query times
* **Network Overhead**: Distributed caching adds network latency compared to in-memory stores
* **Connection Pool**: Ensure datasource connection pool is sized for concurrent cache operations
* **Database Storage**: Monitor database size and implement regular maintenance (vacuuming, optimization)
* **Serialization**: Objects are Base64-encoded for storage - consider object size
* **Scaling**: Database can become a bottleneck - consider database clustering or read replicas
* **Maintenance**: Regular database maintenance (VACUUM on PostgreSQL, OPTIMIZE on MySQL) recommended
{% endhint %}

## 🔍 Distribution Detection

The JDBCStore marks itself as `distributed = true`, allowing ecosystem tools and monitoring systems to detect distribution capabilities:

```js
cache = cacheGet( "distributedCache" );
if ( cache.isDistributed() ) {
    // This cache is shared across multiple instances
    // Handle accordingly
}
```

This enables smart caching strategies where code can adapt behavior based on whether a cache is distributed or local.

## 🗂️ Database Schema Details

When `autoCreate = true`, the JDBCStore creates an optimized schema:

### Table Structure

* **objectKey** (VARCHAR/PRIMARY KEY): Unique cache key
* **objectValue** (CLOB/TEXT): Base64-encoded serialized object
* **hits** (INTEGER): Access count for LFU eviction
* **timeout** (INTEGER): TTL in seconds
* **lastAccessTimeout** (INTEGER): Idle timeout in seconds
* **created** (BIGINT): Creation timestamp
* **lastAccessed** (BIGINT): Last access timestamp
* **lastUpdated** (BIGINT): Last update timestamp
* **isExpired** (BOOLEAN): Expiration flag

### Indexes

* **Primary Key**: `objectKey` for fast lookups
* **LRU Index**: `lastAccessed` for least-recently-used eviction
* **LFU Index**: `hits` for least-frequently-used eviction
* **FIFO Index**: `created` for first-in-first-out eviction
* **Expiration Index**: `isExpired` for efficient reaping

Database-specific optimizations are applied automatically based on vendor detection.

## 🔗 Related Resources

* [BoxCache Overview](../README.md)
* [Cache Configuration](../../../getting-started/configuration/caches.md)
* [Custom Object Stores](../custom-object-stores.md)
* [Eviction Policies](../custom-eviction-policies.md)
* [Datasource Configuration](../../../getting-started/configuration/)
* [ConcurrentStore](concurrent-store.md) - For single-instance in-memory caching
* [FileSystemStore](file-system-store.md) - For persistent single-instance caching
