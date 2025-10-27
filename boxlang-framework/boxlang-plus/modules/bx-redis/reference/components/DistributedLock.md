[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the component class)

# Component: `<bx:RedisLock>`

Provides a distributed lock around the body of the component using Redis as the locking mechanism. This allows safe concurrent access control across multiple requests or servers using Redis as the coordination backend.

## Supported Actions

This component does not support actions. It operates by wrapping the body content in a distributed lock.

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | `true` | Lock name. Only one request can execute the code within a lock component with a given name at a time. Cannot be an empty string. |  |
| `cache` | `string` | `true` | The name of the Redis cache (as defined in the application cache settings) to use for the lock. |  |
| `timeout` | `numeric` | `false` | Maximum length of time, in seconds, to wait to obtain a lock. If lock is obtained, tag execution continues. Otherwise, behavior depends on throwOnTimeout attribute value. | 2 |
| `expires` | `numeric` | `false` | The length of time, in seconds, before the lock automatically expires. | 60 |
| `throwOnTimeout` | `boolean` | `false` | True: if lock is not obtained within the timeout period, a runtime exception is thrown. False: if lock is not obtained, the body of the component is skipped and execution continues without running the statements in the component. | true |
| `bypass` | `boolean` | `false` | If true, the lock is bypassed and the body is executed immediately without acquiring a lock. | false |

## Examples

### Basic Locking

**Template Syntax:**

```xml
<bx:RedisLock
    name="account-update-lock"
    cache="myRedisCache"
    timeout="5s"
    expires="60s">

    // This code runs only if the lock is acquired
    account.balance = account.balance - 100;
    account.save();
</bx:RedisLock>
```

**Script Syntax:**

```js
// Using the component in script context with attributes
component "bx:RedisLock" {
    name = "account-update-lock";
    cache = "myRedisCache";
    timeout = 5;  // in seconds
    expires = 60;

    // Lock body logic
    account.balance = account.balance - 100;
    account.save();
};
```

### Handling Lock Timeout

**Template Syntax:**

```xml
<bx:RedisLock
    name="report-generation"
    cache="myRedisCache"
    timeout="3s"
    expires="30s"
    throwOnTimeout="false">

    // Generate expensive report
    var report = generateMonthlyReport();
    saveReport( report );
</bx:RedisLock>

<bx:catch type="LockTimeoutException">
    <bx:log text="Could not acquire lock, another process is generating the report" />
</bx:catch>
```

**Script Syntax:**

```js
// Using the component with error handling
try {
    component "bx:RedisLock" {
        name = "report-generation";
        cache = "myRedisCache";
        timeout = 3;
        expires = 30;
        throwOnTimeout = false;

        var report = generateMonthlyReport();
        saveReport( report );
    };
} catch ( LockTimeoutException e ) {
    logError( "Could not acquire lock, another process is generating the report" );
}
```

### Critical Section with Automatic Bypass

**Template Syntax:**

```xml
<bx:RedisLock
    name="cache-refresh"
    cache="myRedisCache"
    timeout="10s"
    expires="120s"
    bypass="isMaintenanceWindow()">

    // Refresh system cache with guaranteed single execution
    clearSystemCache();
    loadSystemCache();
</bx:RedisLock>
```

**Script Syntax:**

```js
// Bypass lock during maintenance windows
component "bx:RedisLock" {
    name = "cache-refresh";
    cache = "myRedisCache";
    timeout = 10;
    expires = 120;
    bypass = isMaintenanceWindow();

    clearSystemCache();
    loadSystemCache();
};
```

### Preventing Concurrent Operations

**Template Syntax:**

```xml
<bx:RedisLock
    name="inventory-deduction-lock"
    cache="myRedisCache"
    timeout="2s"
    expires="10s">

    // Ensure inventory is not over-sold
    var currentStock = inventory.getStock( productId );

    if ( currentStock >= quantity ) {
        inventory.deductStock( productId, quantity );
        order.status = "confirmed";
    } else {
        order.status = "out-of-stock";
    }
</bx:RedisLock>
```

**Script Syntax:**

```js
// Ensure atomic inventory operations
component "bx:RedisLock" {
    name = "inventory-deduction-lock";
    cache = "myRedisCache";
    timeout = 2;
    expires = 10;

    var currentStock = inventory.getStock( productId );

    if ( currentStock >= quantity ) {
        inventory.deductStock( productId, quantity );
        order.status = "confirmed";
    } else {
        order.status = "out-of-stock";
    }
};
```## Related

- [RedisPublish()](../built-in-functions/RedisPublish.md) - Publish messages to channels
- [RedisSubscribe()](../built-in-functions/RedisSubscribe.md) - Subscribe to channels
- [Distributed Locking Guide](../../distributed-locking.md) - Advanced locking patterns
- [Concurrency Patterns](../../concurrency.md) - Handling concurrent operations
- [API Usage Guide](../../api-usage.md) - Redis API documentation
