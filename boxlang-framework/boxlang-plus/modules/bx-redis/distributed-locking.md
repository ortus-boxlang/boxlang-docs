---
icon: lock-keyhole
description: Implement distributed locking in BoxLang applications using Redis to prevent concurrent access issues.
---

# Distributed Locking

## 🔒 Overview

In clustered environments, it is often necessary to prevent multiple instances from executing methods at the same time, preventing collisions with data access and modification. The `bx:RedisLock` component provides distributed locking across all running instances in a cluster using Redis as the coordination mechanism.

The component functions similarly to the standard `lock` component but uses Redis to coordinate locks across multiple servers, ensuring that only one request can execute the locked code at any given time across the entire cluster.

## 📋 Component Syntax

```xml
<bx:RedisLock
    name="lockName"
    cache="redisCacheName"
    timeout="2"
    expires="60"
    throwOnTimeout="true"
    bypass="false"
>
    <!-- Protected code here -->
</bx:RedisLock>
```

**Script Syntax:**

```js
bx:redisLock name="lockName" cache="redisCacheName" timeout=2 expires=60 throwOnTimeout=true bypass=false {
    // Protected code here
}
```

## ⚙️ Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | string | ✅ Yes | - | Lock name. Only one request can execute code within a lock with a given name at a time. Cannot be an empty string. |
| `cache` | string | ✅ Yes | - | The name of the Redis cache (as defined in application cache settings) to use for the lock |
| `timeout` | integer | No | `2` | Maximum time in seconds to wait to obtain a lock. Must be >= 0. If lock is not obtained within this time, behavior depends on `throwOnTimeout`. |
| `expires` | integer | No | `60` | The length of time in seconds before the lock automatically expires. Must be >= 1. Prevents deadlocks if a process crashes while holding a lock. |
| `throwOnTimeout` | boolean | No | `true` | If `true`, throws a runtime exception if lock is not obtained within timeout period. If `false`, skips the body and continues execution. |
| `bypass` | boolean | No | `false` | If `true`, bypasses the lock entirely and executes the body immediately. Useful for development environments. |

## 💡 Usage Examples

### Basic Distributed Lock

```js
// Protect critical section across all servers
redisLock name="processOrders" cache="redisCache" timeout=5 expires=30 {
    // Only one server can process orders at a time
    var orders = orderService.getPendingOrders();
    for( var order in orders ) {
        orderService.processOrder( order );
    }
}
```

### Lock with Timeout Handling

```js
// Non-blocking lock - skip if unavailable
redisLock
    name="updateCache"
    cache="redisCache"
    timeout=1
    expires=10
    throwOnTimeout=false
{
    cacheService.rebuildExpensiveCache();
}

// Continue execution whether lock was obtained or not
```

### Development Bypass

```js
// Bypass locking in development
var isDevelopment = application.environment == "development";

redisLock
    name="syncInventory"
    cache="redisCache"
    bypass=isDevelopment
{
    inventoryService.synchronizeWithWarehouse();
}
```

### XML Component Syntax

```xml
<bx:RedisLock
    name="dailyReport"
    cache="redisCache"
    timeout="10"
    expires="300"
>
    <bx:set var="reportData" value="#reportService.generateDailyReport()#" />
    <bx:set var="result" value="#emailService.sendReport( reportData )#" />
</bx:RedisLock>
```

## 🎯 Common Use Cases

### Scheduled Task Coordination

```js
// Ensure scheduled task runs on only one server
component {
    function runScheduledTask() {
        redisLock name="dailyCleanup" cache="redisCache" timeout=0 throwOnTimeout=false {
            // Only executes on one server
            cleanupService.performDailyMaintenance();
        }
    }
}
```

### Cache Warming

```js
// Prevent multiple servers from warming cache simultaneously
redisLock name="warmCache" cache="redisCache" timeout=2 expires=120 throwOnTimeout=false {
    if( !cacheService.isWarmed() ) {
        cacheService.warmCache();
    }
}
```

### Database Migration Coordination

```js
// Ensure database migrations run only once across cluster
redisLock name="dbMigration" cache="redisCache" timeout=30 expires=600 {
    migrationService.runPendingMigrations();
}
```

### Sequential Processing

```js
// Process queue items one at a time across all servers
redisLock name="processQueue" cache="redisCache" timeout=5 expires=60 {
    var item = queue.getNextItem();
    if( !isNull( item ) ) {
        processItem( item );
        queue.markComplete( item );
    }
}
```

## 🔧 Configuration Requirements

### Cache Setup

The lock requires a configured Redis cache in your application:

```js
component {
    this.name = "MyApp";
    this.sessionManagement = true;

    // Configure Redis cache
    this.cache.redis = {
        provider: "Redis",
        properties: {
            server: "localhost",
            port: 6379
        }
    };
}
```

### Cluster Configuration

For multi-server environments, ensure all servers point to the same Redis instance:

```js
// Production configuration
this.cache.redis = {
    provider: "Redis",
    properties: {
        server: "redis.production.com",
        port: 6379,
        password: getSystemSetting( "REDIS_PASSWORD" ),
        ssl: true
    }
};
```

## ⚠️ Best Practices

### Lock Naming

* Use descriptive, unique lock names
* Include context in name: `"user_#{userId}_update"` instead of `"update"`
* Avoid hardcoded IDs - use dynamic names when locking specific resources

```js
// Good: Specific resource lock
redisLock name="invoice_#invoiceId#_generate" cache="redisCache" {
    generateInvoice( invoiceId );
}

// Bad: Too generic
redisLock name="generate" cache="redisCache" {
    generateInvoice( invoiceId );
}
```

### Timeout Configuration

* Set `timeout` based on expected wait time
* Set `expires` longer than maximum expected execution time
* Use `throwOnTimeout=false` for non-critical operations

```js
// Critical operation - throw if can't acquire
redisLock name="payment" cache="redisCache" timeout=10 expires=30 throwOnTimeout=true {
    processPayment();
}

// Non-critical - skip if unavailable
redisLock name="analytics" cache="redisCache" timeout=1 expires=60 throwOnTimeout=false {
    updateAnalytics();
}
```

### Error Handling

* Always handle exceptions within locked code
* Keep locked code sections as short as possible
* Consider using `try/catch` inside lock body

```js
redisLock name="criticalUpdate" cache="redisCache" {
    try {
        performCriticalUpdate();
    } catch( any e ) {
        logService.error( "Lock execution failed", e );
        // Lock will be released automatically
        rethrow;
    }
}
```

### Development vs Production

* Use `bypass` attribute for development environments
* Set via environment variables or application settings

```js
var isDev = application.environment == "development";

redisLock name="sync" cache="redisCache" bypass=isDev {
    syncService.synchronize();
}
```

## 🚨 Troubleshooting

### Lock Not Acquired

**Symptoms:** `throwOnTimeout` exceptions or body not executing

**Solutions:**

* Increase `timeout` value
* Check if another process is holding the lock too long
* Verify Redis connectivity
* Check Redis logs for connection issues

### Deadlocks

**Symptoms:** Locks never release, operations hang

**Solutions:**

* Ensure `expires` is set appropriately
* Verify locked code completes normally
* Check for infinite loops in locked sections
* Monitor Redis for stuck lock keys

### Performance Issues

**Symptoms:** High latency acquiring locks

**Solutions:**

* Reduce lock scope - lock smaller code sections
* Increase Redis server resources
* Check network latency to Redis
* Consider Redis Cluster for high-availability

### Cache Not Found

**Error:** "The specified cache [name] is not a Redis cache"

**Solutions:**

* Verify cache name matches application configuration
* Ensure cache provider type is "Redis"
* Check cache is properly initialized before use

## 🔍 Monitoring

### Lock Metrics

Monitor these aspects of distributed locking:

* **Lock acquisition time** - time spent waiting for locks
* **Lock hold duration** - time locks are held
* **Failed acquisitions** - locks that timeout
* **Lock expiration events** - automatic releases

### Redis Key Inspection

Locks are stored in Redis with specific key patterns. Use Redis CLI to inspect:

```bash
# List all lock keys
redis-cli KEYS "*lock*"

# Check lock TTL
redis-cli TTL "lock:lockName"

# View lock details
redis-cli GET "lock:lockName"
```
