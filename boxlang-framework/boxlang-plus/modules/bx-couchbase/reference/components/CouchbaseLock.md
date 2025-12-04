# CouchbaseLock Component

Distributed locking component that executes a body of code with automatic lock management.

## Syntax

```js
<bx:CouchbaseLock
    name="lockName"
    cache="cacheName"
    [timeout="5"]
    [expires="30"]
    [throwOnTimeout="true"]
    [bypass="false"]>

    // Body executes with lock held

</bx:CouchbaseLock>
```

## Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | String | Yes | - | Unique name of the lock across cluster |
| `cache` | String | Yes | - | Name of the Couchbase cache for locking |
| `timeout` | Integer | No | `5` | Maximum seconds to wait for lock acquisition |
| `expires` | Integer | No | `30` | Lock expiration in seconds (max 30) |
| `throwOnTimeout` | Boolean | No | `true` | Throw exception if lock not acquired |
| `bypass` | Boolean | No | `false` | Skip locking (useful for testing) |

## Examples

### Basic Usage

```js
<bx:CouchbaseLock
    name="user-#userId#-update"
    cache="default"
    timeout="5"
    expires="30">

    // Critical section - only one request at a time
    user = getUser(userId);
    user.balance += amount;
    saveUser(user);

</bx:CouchbaseLock>
```

### Financial Transaction

```js
<bx:CouchbaseLock
    name="payment-#orderId#"
    cache="payments"
    timeout="10"
    expires="30">

    order = getOrder(orderId);

    if (order.status == "pending") {
        chargeCustomer(order.customerId, order.amount);
        order.status = "paid";
        saveOrder(order);
        sendConfirmation(order);
    }

</bx:CouchbaseLock>
```

### Inventory Management

```js
<bx:CouchbaseLock
    name="product-#productId#-stock"
    cache="inventory"
    timeout="5"
    expires="30">

    product = getProduct(productId);

    if (product.stock >= quantity) {
        product.stock -= quantity;
        product.reserved += quantity;
        saveProduct(product);
    } else {
        throw("Insufficient stock");
    }

</bx:CouchbaseLock>
```

### Configuration Update

```js
<bx:CouchbaseLock
    name="config-reload"
    cache="default"
    timeout="2"
    expires="10">

    // Only one server reloads config
    config = loadConfigFromFile();
    application.config = config;
    application.configLastReload = now();

</bx:CouchbaseLock>
```

### Scheduled Job Coordination

```js
<bx:CouchbaseLock
    name="daily-cleanup"
    cache="jobs"
    timeout="2"
    expires="30"
    throwOnTimeout="false">

    // Only one server executes the cleanup
    lastRun = getJobStatus("daily-cleanup").lastRun;

    if (dateDiff("h", lastRun, now()) >= 24) {
        runCleanupJob();
        updateJobStatus("daily-cleanup", now());
    }

</bx:CouchbaseLock>
```

### With No Throw

```js
<bx:CouchbaseLock
    name="optional-task"
    cache="default"
    timeout="1"
    expires="10"
    throwOnTimeout="false">

    // Body executes only if lock acquired
    // If not acquired, silently skips
    processOptionalTask();

</bx:CouchbaseLock>
```

### Bypass for Testing

```js
<bx:CouchbaseLock
    name="production-lock"
    cache="default"
    timeout="5"
    expires="30"
    bypass="#application.isTestMode#">

    // In test mode, executes immediately without locking
    // In production, uses distributed lock
    criticalOperation();

</bx:CouchbaseLock>
```

### Counter Increment

```js
<bx:CouchbaseLock
    name="counter-increment"
    cache="default"
    timeout="5"
    expires="10">

    counter = cacheGet("globalCounter") ?: 0;
    counter++;
    cacheSet("globalCounter", counter);

</bx:CouchbaseLock>
```

### Rate Limiting

```js
<bx:CouchbaseLock
    name="ratelimit-#userId#"
    cache="default"
    timeout="5"
    expires="5">

    key = "ratelimit:#userId#";
    data = cacheGet(key) ?: { count: 0, window: now() };

    if (dateDiff("s", data.window, now()) >= 60) {
        data = { count: 0, window: now() };
    }

    if (data.count >= 100) {
        throw("Rate limit exceeded");
    }

    data.count++;
    cacheSet(key, data, 1);

</bx:CouchbaseLock>
```

### Batch Processing

```js
<bx:CouchbaseLock
    name="batch-processor"
    cache="jobs"
    timeout="2"
    expires="30"
    throwOnTimeout="false">

    records = getUnprocessedRecords();

    records.each(function(record) {
        processRecord(record);
        markProcessed(record.id);
    });

    println("Processed #records.len()# records on server #cgi.server_name#");

</bx:CouchbaseLock>
```

## Behavior

### Lock Acquisition

1. **Attempts to acquire** distributed lock with specified timeout
2. **If acquired**:
   - Executes body
   - Automatically releases lock after body completes
   - Releases lock even if body throws exception
3. **If not acquired**:
   - With `throwOnTimeout=true`: Throws `LockTimeoutException`
   - With `throwOnTimeout=false`: Silently skips body

### Lock Release

The lock is **always released** after the body executes:
- ✅ Normal completion
- ✅ Exception thrown
- ✅ Early return
- ✅ Break/continue in loop

### Bypass Mode

When `bypass=true`:
- No lock acquisition attempted
- Body executes immediately
- Useful for testing or conditional locking

## Error Handling

### With throwOnTimeout=true (default)

```js
try {
    <bx:CouchbaseLock
        name="busy-lock"
        cache="default"
        timeout="1"
        expires="30">

        doWork();

    </bx:CouchbaseLock>
} catch (LockTimeoutException e) {
    println("Could not acquire lock: #e.message#");
}
```

### With throwOnTimeout=false

```js
<bx:CouchbaseLock
    name="optional-work"
    cache="default"
    timeout="1"
    expires="30"
    throwOnTimeout="false">

    // Only executes if lock acquired
    doOptionalWork();

</bx:CouchbaseLock>

// Continues regardless of lock acquisition
```

### Body Exceptions

```js
try {
    <bx:CouchbaseLock
        name="test"
        cache="default"
        timeout="5"
        expires="30">

        doWork();
        throw("Error in body");

    </bx:CouchbaseLock>
} catch (any e) {
    // Lock is automatically released
    println("Error: #e.message#");
}
```

## Notes

- **Distributed**: Works across all servers in cluster
- **30 Second Max**: Cannot exceed 30 seconds expiration
- **Auto-Release**: Always releases lock after body
- **Exception-Safe**: Releases lock even on errors
- **Bypass Testing**: Use `bypass=true` for tests

## Validation

### Expiration Limit

```js
<!-- ❌ This will throw an exception -->
<bx:CouchbaseLock
    name="test"
    cache="default"
    expires="31">

    // Error: expires cannot exceed 30 seconds

</bx:CouchbaseLock>

<!-- ✅ Maximum allowed -->
<bx:CouchbaseLock
    name="test"
    cache="default"
    expires="30">

    // OK

</bx:CouchbaseLock>
```

### Cache Validation

```js
<!-- ❌ Cache must exist -->
<bx:CouchbaseLock
    name="test"
    cache="nonexistent">

    // Error: Cache does not exist

</bx:CouchbaseLock>

<!-- ✅ Must be Couchbase cache -->
<bx:CouchbaseLock
    name="test"
    cache="default">

    // OK if 'default' is Couchbase cache

</bx:CouchbaseLock>
```

## Best Practices

### ✅ DO

**Use descriptive lock names with IDs:**
```js
<bx:CouchbaseLock name="user-#userId#-balance-update" cache="default">
    updateBalance(userId);
</bx:CouchbaseLock>
```

**Keep critical sections short:**
```js
<bx:CouchbaseLock name="counter" cache="default">
    counter = cacheGet("counter") + 1;
    cacheSet("counter", counter);
</bx:CouchbaseLock>
```

**Use throwOnTimeout=false for optional operations:**
```js
<bx:CouchbaseLock name="optional" cache="default" throwOnTimeout="false">
    doOptionalWork();
</bx:CouchbaseLock>
```

### ❌ DON'T

**Don't hold locks during I/O:**
```js
<!-- ❌ Bad - lock held during slow operations -->
<bx:CouchbaseLock name="test" cache="default">
    data = getData();
    http url="http://api.example.com" result="apiResult"; // Slow!
    saveData(data, apiResult);
</bx:CouchbaseLock>

<!-- ✅ Better - I/O outside lock -->
<cfhttp url="http://api.example.com" result="apiResult">
<bx:CouchbaseLock name="test" cache="default">
    data = getData();
    saveData(data, apiResult);
</bx:CouchbaseLock>
```

**Don't nest locks (deadlock risk):**
```js
<!-- ❌ Potential deadlock -->
<bx:CouchbaseLock name="lock-A" cache="default">
    <bx:CouchbaseLock name="lock-B" cache="default">
        // Bad!
    </bx:CouchbaseLock>
</bx:CouchbaseLock>
```

**Don't use for simple caching:**
```js
<!-- ❌ Wrong use case -->
<bx:CouchbaseLock name="expensive-calc" cache="default">
    result = expensiveCalculation();
    cacheSet("calc-result", result);
</bx:CouchbaseLock>

<!-- ✅ Use cacheGetOrSet instead -->
result = cacheGetOrSet("calc-result", function() {
    return expensiveCalculation();
});
```

## Comparison with BIF

### Component (This)

```js
<bx:CouchbaseLock name="test" cache="default" timeout="5" expires="30">
    doWork();
</bx:CouchbaseLock>
```

**Pros:**
- Clean syntax for body execution
- Automatic lock management
- Clear scope of locked section

**Cons:**
- No return value from body
- Less flexible than BIF

### BIF with Callback

```js
result = couchbaseLock(
    cacheName = "default",
    name = "test",
    timeout = 5,
    expires = 30,
    callback = function() {
        doWork();
        return "result";
    }
);
```

**Pros:**
- Can return values
- Can be used in expressions
- More flexible

**Cons:**
- More verbose
- Callback syntax

### BIF Manual Mode

```js
lockInfo = couchbaseLock("default", "test", 5, 30);
if (lockInfo.locked) {
    try {
        doWork();
    } finally {
        couchbaseUnlock("default", "test", lockInfo.cas);
    }
}
```

**Pros:**
- Maximum control
- Can check lock status
- Can release early

**Cons:**
- Must manage unlock manually
- More error-prone

## Related Functions

- [couchbaseLock BIF](../built-in-functions/CouchbaseLock.md) - Function version
- [couchbaseUnlock BIF](../built-in-functions/CouchbaseUnlock.md) - Manual unlock

## See Also

- [Distributed Locking Guide](../../distributed-locking.md)
- [Code Usage](../../code-usage.md)
- [Couchbase Locking](https://docs.couchbase.com/java-sdk/current/howtos/concurrent-document-mutations.html#pessimistic-locking)
