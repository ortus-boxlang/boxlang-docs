---
icon: brackets-curly
description: Comprehensive guide to using the BoxLang Redis Module API for advanced caching and data management in BoxLang applications.
---

# API Usage

## 🔌 Overview

If you need more power or are familiar with the Redis Java API and want to use features beyond the standard cache interface, the bx-redis module provides direct access to the underlying Redis connections and providers. Behind the scenes, the module leverages the [Jedis library](https://github.com/redis/jedis) for Redis connectivity.

This page documents the low-level API functions available for advanced Redis operations.

## 🛠️ Available Functions

The module provides several global BoxLang functions to access the underlying Redis infrastructure:

| Function | Purpose | Returns |
|----------|---------|---------|
| `redisGetProvider()` | Get the cache provider implementation | `IRedisCache` interface |
| `redisGetConnectionPool()` | Get the Jedis connection pool (non-clustered) | `JedisPool` |
| `redisGetCluster()` | Get the Redis cluster connection | `JedisCluster` |
| `redisGetClusterNodes()` | Get map of cluster node connections | `Map<String, JedisPool>` |

## 📋 Function Reference

### redisGetProvider()

Returns the BoxLang Redis cache provider implementation. This gives you access to the `IRedisCache` interface, which extends BoxLang's standard `ICacheProvider` with Redis-specific functionality.

**Syntax:**

```js
provider = redisGetProvider( [ cacheName ] )
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | string | No | `"default"` | The name of the configured Redis cache |

**Returns:** `ortus.boxlang.modules.redis.cache.IRedisCache`

**Throws:** `InvalidCacheType` if the specified cache is not a Redis cache

**Example:**

```js
// Get the provider for the default cache
provider = redisGetProvider();

// Get the provider for a named cache
sessionProvider = redisGetProvider( "sessions" );

// Access Redis-specific methods
keys = provider.getKeys();
stats = provider.getStats();
```

**Use Cases:**

* Accessing Redis-specific cache operations
* Getting cache statistics and metadata
* Performing bulk operations
* Direct cache provider manipulation

### redisGetConnectionPool()

Returns the Jedis connection pool for non-clustered Redis caches. This provides direct access to the `redis.clients.jedis.JedisPool` for low-level Redis operations.

**Syntax:**

```js
pool = redisGetConnectionPool( [ cacheName ] )
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | string | No | `"default"` | The name of the configured Redis cache (must be non-clustered) |

**Returns:** `redis.clients.jedis.JedisPool`

**Throws:**

* `InvalidCacheType` if the cache is not a Redis cache
* Exception if called on a clustered cache

**Example:**

```js
// Get connection pool
pool = redisGetConnectionPool( "sessions" );

// Get a connection from the pool
try {
    var jedis = pool.getResource();

    // Perform Redis operations
    jedis.set( "mykey", "myvalue" );
    var value = jedis.get( "mykey" );

    // Connection is auto-closed via try-with-resources
} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}
```

**Use Cases:**

* Direct Jedis API access
* Redis commands not exposed through cache interface
* Performance-critical operations requiring connection pooling
* Custom Redis operations

{% hint style="warning" %}
**Important:** Always return connections to the pool using `jedis.close()` or use try-with-resources patterns to prevent connection leaks.
{% endhint %}

### redisGetCluster()

Returns the Redis cluster connection for clustered deployments. Provides access to `redis.clients.jedis.JedisCluster` for cluster-specific operations.

**Syntax:**

```js
cluster = redisGetCluster( [ cacheName ] )
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | string | No | `"default"` | The name of the configured Redis cache (must be clustered) |

**Returns:** `redis.clients.jedis.JedisCluster`

**Throws:**

* `InvalidCacheType` if the cache is not a Redis cache
* Exception if called on a non-clustered cache

**Example:**

```js
// Get cluster connection
cluster = redisGetCluster( "distributedCache" );

// Perform cluster operations
cluster.set( "user:123", serializeJSON( userData ) );
var user = cluster.get( "user:123" );

// Get cluster info
var clusterInfo = cluster.clusterNodes();
var clusterSlots = cluster.clusterSlots();
```

**Use Cases:**

* Cluster-specific Redis commands
* Cluster topology inspection
* Slot management
* Multi-key operations across cluster

### redisGetClusterNodes()

Returns a map of all cluster node connections. Each entry provides a `JedisPool` for a specific cluster node.

**Syntax:**

```js
nodes = redisGetClusterNodes( [ cacheName ] )
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | string | No | `"default"` | The name of the configured Redis cache (must be clustered) |

**Returns:** `Map<String, redis.clients.jedis.JedisPool>`

**Throws:**

* `InvalidCacheType` if the cache is not a Redis cache
* Exception if called on a non-clustered cache

**Example:**

```js
// Get all cluster nodes
nodes = redisGetClusterNodes( "distributedCache" );

// Iterate through nodes
for( var nodeKey in nodes ) {
    var nodePool = nodes[ nodeKey ];

    try {
        var jedis = nodePool.getResource();
        var info = jedis.info();
        writeOutput( "Node: #nodeKey# - #info#<br>" );
    } finally {
        if( !isNull( jedis ) ) {
            jedis.close();
        }
    }
}
```

**Use Cases:**

* Node-specific operations
* Health checking individual nodes
* Gathering per-node statistics
* Debugging cluster issues

## 💡 Advanced Usage Examples

### Custom Redis Command Execution

```js
// Execute raw Redis commands
pool = redisGetConnectionPool( "default" );

try {
    var jedis = pool.getResource();

    // Use Redis commands not in standard cache API
    jedis.lpush( "queue:tasks", "task1" );
    jedis.lpush( "queue:tasks", "task2" );

    var task = jedis.rpop( "queue:tasks" );

    // Set expiration in milliseconds
    jedis.pexpire( "temp:data", 5000 );

} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}
```

### Pipeline Operations

```js
// Batch multiple commands for better performance
pool = redisGetConnectionPool( "default" );

try {
    var jedis = pool.getResource();
    var pipeline = jedis.pipelined();

    // Queue multiple operations
    for( var i = 1; i <= 100; i++ ) {
        pipeline.set( "key:#i#", "value:#i#" );
    }

    // Execute all at once
    pipeline.sync();

} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}
```

### Transaction Support

```js
// Execute atomic transactions
pool = redisGetConnectionPool( "default" );

try {
    var jedis = pool.getResource();

    // Start transaction
    var transaction = jedis.multi();

    transaction.set( "account:123:balance", "1000" );
    transaction.set( "account:456:balance", "2000" );
    transaction.incr( "total:accounts" );

    // Execute transaction
    var results = transaction.exec();

} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}
```

### Cluster Slot Information

```js
// Get cluster slot mappings
cluster = redisGetCluster( "distributedCache" );

// Get slot assignments
var slots = cluster.clusterSlots();

// Find which node handles a specific key
var keySlot = jedis.clusterKeySlot( "mykey" );
```

### Monitoring and Statistics

```js
// Gather Redis statistics
provider = redisGetProvider( "default" );

// Get cache statistics
var stats = provider.getStats();
writeOutput( "Hits: #stats.hits#<br>" );
writeOutput( "Misses: #stats.misses#<br>" );
writeOutput( "Size: #stats.size#<br>" );

// Get all keys (use with caution in production)
var allKeys = provider.getKeys();
```

## ⚠️ Best Practices

### Connection Management

* **Always close Jedis resources** - Use try/finally blocks or BoxLang's try-with-resources
* **Don't hold connections** - Get, use, and return connections quickly
* **Pool size configuration** - Configure appropriate connection pool sizes in your cache settings

```js
// GOOD: Proper connection handling
try {
    var jedis = pool.getResource();
    jedis.set( "key", "value" );
} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}

// BAD: Connection leak
var jedis = pool.getResource();
jedis.set( "key", "value" );
// Connection never returned!
```

### Error Handling

* **Catch Redis-specific exceptions** - Handle `JedisException` and connection errors
* **Implement retry logic** - For transient network failures
* **Validate cache type** - Check cache is Redis before calling these functions

```js
try {
    var provider = redisGetProvider( "myCache" );
    // Use provider
} catch( InvalidCacheType e ) {
    writeLog( "Cache is not a Redis cache: #e.message#" );
}
```

### Performance Considerations

* **Use pipelining** - For bulk operations to reduce round trips
* **Avoid KEYS command** - Use SCAN in production environments
* **Connection pooling** - Reuse connections via the pool
* **Cluster awareness** - Use cluster-aware operations for distributed caches

### Security

* **Protect credentials** - Use environment variables for Redis passwords
* **Limit command access** - Use Redis ACLs if available
* **Network security** - Use SSL/TLS for production deployments
* **Connection validation** - Enable pool validation to detect stale connections

## 🔍 Debugging

### Enable Debug Logging

```js
// Log connection pool statistics
pool = redisGetConnectionPool( "default" );
writeOutput( "Active: #pool.getNumActive()#<br>" );
writeOutput( "Idle: #pool.getNumIdle()#<br>" );
writeOutput( "Waiting: #pool.getNumWaiters()#<br>" );
```

### Test Connectivity

```js
// Test Redis connection
try {
    var jedis = pool.getResource();
    var response = jedis.ping();
    writeOutput( "Redis responded: #response#" );
} catch( any e ) {
    writeOutput( "Connection failed: #e.message#" );
} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}
```

### Monitor Commands

```js
// Enable Redis command monitoring (development only)
try {
    var jedis = pool.getResource();

    // MONITOR command streams all Redis commands
    // WARNING: Very high performance impact
    var monitor = jedis.monitor( function( command ) {
        writeLog( "Redis: #command#" );
    } );

} finally {
    if( !isNull( jedis ) ) {
        jedis.close();
    }
}
```
