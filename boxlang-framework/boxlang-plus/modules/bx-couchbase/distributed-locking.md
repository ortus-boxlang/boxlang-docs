---
icon: lock-closed
description: True distributed locking across multiple servers using Couchbase's native locking mechanism.
---

# 🔐 Distributed Locking

True distributed locking across multiple servers using Couchbase's native locking mechanism.

## 🎯 What is Distributed Locking?

Distributed locking ensures that only one process across your entire server cluster can execute a critical section of code at a time. This is essential for:

- 💰 **Financial transactions** - Prevent double-charging or race conditions
- 📦 **Inventory updates** - Avoid overselling products
- 🔄 **Batch processing** - Ensure only one server runs the job
- 🎫 **Ticket sales** - Prevent double-booking
- 👤 **User account updates** - Serialize concurrent modifications

## 🚀 Quick Start

### Component Usage (Recommended)

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

### BIF with Callback

```js
result = couchbaseLock(
    cacheName = "default",
    name = "inventory-update-#productId#",
    timeout = 5,
    expires = 30,
    callback = function() {
        // Automatically locked during execution
        stock = getStock(productId);
        stock.quantity -= orderQty;
        saveStock(productId, stock);
        return { success: true };
    }
);
```

### BIF Manual Mode

```js
lockInfo = couchbaseLock(
    cacheName = "default",
    name = "payment-processing",
    timeout = 5,
    expires = 30
);

if (lockInfo.locked) {
    try {
        // Critical section
        processPayment(orderId);
    } finally {
        couchbaseUnlock("default", "payment-processing", lockInfo.cas);
    }
}
```

## 📖 How It Works

### Lock Mechanism

Couchbase provides distributed locking using its `getAndLock()` API:

1. **Lock Document Created**: A special document with prefix `__lock:{cacheName}:{lockName}`
2. **Exclusive Access**: Couchbase ensures only one server can lock the document
3. **Automatic Expiry**: Lock expires after specified duration (max 30 seconds)
4. **CAS-Based Unlock**: Unlock requires the correct CAS value from acquisition

### Lock Key Format

```
__lock:{cacheName}:{lockName}
```

Example: `__lock:sessionCache:user-123-update`

## 🎨 Usage Patterns

### Pattern 1: Component for Simple Cases

Best for straightforward critical sections with no complex logic:

```js
<bx:CouchbaseLock name="config-update" cache="default" timeout="5" expires="30">
    config = loadConfig();
    config.lastUpdate = now();
    saveConfig(config);
</bx:CouchbaseLock>
```

### Pattern 2: Callback for Return Values

When you need to return a value from the locked section:

```js
result = couchbaseLock(
    cacheName = "default",
    name = "reservation-#roomId#",
    timeout = 5,
    expires = 30,
    callback = function() {
        if (isRoomAvailable(roomId)) {
            reserveRoom(roomId, guestId);
            return { reserved: true, roomId: roomId };
        }
        return { reserved: false };
    }
);

if (result.reserved) {
    println("Room reserved!");
}
```

### Pattern 3: Manual for Complex Control

When you need fine-grained control over lock lifecycle:

```js
lockInfo = couchbaseLock(
    cacheName = "default",
    name = "batch-job",
    timeout = 2,
    expires = 30,
    throwOnTimeout = false
);

if (lockInfo.locked) {
    try {
        // Process batch
        while (hasMoreRecords()) {
            processRecord();

            // Optionally release and re-acquire for long operations
            if (shouldYield()) {
                couchbaseUnlock("default", "batch-job", lockInfo.cas);
                sleep(1000);
                lockInfo = couchbaseLock("default", "batch-job", 2, 30);
            }
        }
    } finally {
        couchbaseUnlock("default", "batch-job", lockInfo.cas);
    }
}
```

## 💡 Real-World Examples

### Example 1: Prevent Double-Charging

```js
function chargeCustomer(customerId, amount) {
    return couchbaseLock(
        cacheName = "payments",
        name = "charge-#customerId#",
        timeout = 5,
        expires = 30,
        callback = function() {
            customer = getCustomer(customerId);

            // Check balance
            if (customer.balance < amount) {
                throw("Insufficient funds");
            }

            // Deduct and save
            customer.balance -= amount;
            customer.lastCharge = now();
            saveCustomer(customer);

            // Record transaction
            logTransaction(customerId, amount);

            return { success: true, newBalance: customer.balance };
        }
    );
}
```

### Example 2: Inventory Management

```js
function reserveStock(productId, quantity) {
    return couchbaseLock(
        cacheName = "inventory",
        name = "product-#productId#",
        timeout = 5,
        expires = 30,
        callback = function() {
            product = getProduct(productId);

            if (product.stock < quantity) {
                return {
                    success: false,
                    available: product.stock
                };
            }

            product.stock -= quantity;
            product.reserved += quantity;
            product.lastUpdate = now();
            saveProduct(product);

            return {
                success: true,
                remaining: product.stock
            };
        }
    );
}
```

### Example 3: Scheduled Job Coordination

```js
// Ensure only one server runs the cleanup job
<bx:CouchbaseLock
    name="daily-cleanup"
    cache="jobs"
    timeout="2"
    expires="30"
    throwOnTimeout="false">

    // This code runs on only ONE server, even if 10 servers trigger simultaneously
    lastRun = getJobStatus("daily-cleanup").lastRun;

    if (dateDiff("h", lastRun, now()) >= 24) {
        runCleanupJob();
        updateJobStatus("daily-cleanup", now());
    }

</bx:CouchbaseLock>
```

### Example 4: Sequential Document Processing

```js
function processNextDocument() {
    lockInfo = couchbaseLock(
        cacheName = "processing",
        name = "document-queue",
        timeout = 1,
        expires = 30,
        throwOnTimeout = false
    );

    if (!lockInfo.locked) {
        // Another server is processing, skip
        return { skipped: true };
    }

    try {
        // Get next unprocessed document
        doc = getNextDocument();

        if (isNull(doc)) {
            return { completed: true };
        }

        // Process it
        result = processDocument(doc);
        markDocumentProcessed(doc.id);

        return {
            processed: true,
            documentId: doc.id
        };
    } finally {
        couchbaseUnlock("processing", "document-queue", lockInfo.cas);
    }
}
```

### Example 5: Rate Limiting with Locks

```js
function checkRateLimit(userId, maxPerMinute) {
    return couchbaseLock(
        cacheName = "default",
        name = "ratelimit-#userId#",
        timeout = 5,
        expires = 5,
        callback = function() {
            key = "ratelimit:#userId#";
            requests = cache("default").get(key) ?: { count: 0, window: now() };

            // Reset window if minute has passed
            if (dateDiff("s", requests.window, now()) >= 60) {
                requests = { count: 0, window: now() };
            }

            // Check limit
            if (requests.count >= maxPerMinute) {
                return { allowed: false, remaining: 0 };
            }

            // Increment and save
            requests.count++;
            cache("default").set(key, requests, 1); // 1 minute TTL

            return {
                allowed: true,
                remaining: maxPerMinute - requests.count
            };
        }
    );
}
```

## ⚙️ Configuration

### Component Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | String | Yes | - | Unique lock name across cluster |
| `cache` | String | Yes | - | Couchbase cache name |
| `timeout` | Integer | No | 5 | Seconds to wait for lock |
| `expires` | Integer | No | 30 | Lock expiration (max 30) |
| `throwOnTimeout` | Boolean | No | true | Throw exception on timeout |
| `bypass` | Boolean | No | false | Skip locking (for testing) |

### BIF Parameters

**couchbaseLock():**
- `cacheName` (String, required) - Cache name
- `name` (String, required) - Lock name
- `timeout` (Integer, optional, default: 5) - Acquisition timeout in seconds
- `expires` (Integer, optional, default: 30) - Lock expiration in seconds
- `callback` (Function, optional) - Function to execute with lock held
- `throwOnTimeout` (Boolean, optional, default: true) - Throw on timeout

**couchbaseUnlock():**
- `cacheName` (String, required) - Cache name
- `name` (String, required) - Lock name
- `cas` (Long, required) - CAS value from lock acquisition

## ⚠️ Important Limitations

### 30 Second Maximum

Couchbase limits `getAndLock()` to **30 seconds maximum**:

```js
// ❌ This will throw an exception
<bx:CouchbaseLock name="test" cache="default" expires="31">
    // Error: Lock expiration cannot exceed 30 seconds
</bx:CouchbaseLock>

// ✅ Use maximum 30 seconds
<bx:CouchbaseLock name="test" cache="default" expires="30">
    // OK
</bx:CouchbaseLock>
```

For operations longer than 30 seconds, consider:
- Breaking into smaller locked operations
- Using a different synchronization approach
- Implementing a heartbeat/renewal pattern

### Lock Expiration

Locks **automatically expire** after the specified duration. If your operation takes longer, the lock will be released:

```js
<bx:CouchbaseLock name="test" cache="default" expires="10">
    processStep1(); // 5 seconds
    processStep2(); // 8 seconds - LOCK EXPIRED DURING THIS!
    // Another server could acquire lock here
</bx:CouchbaseLock>
```

**Solution**: Set `expires` longer than your operation needs.

## 🎭 Best Practices

### ✅ DO

**Use descriptive lock names:**
```js
name="user-#userId#-balance-update"
name="product-#productId#-stock-reservation"
name="job-#jobName#-execution"
```

**Keep critical sections short:**
```js
// ✅ Good - minimal lock duration
<bx:CouchbaseLock name="counter" cache="default">
    counter = cache("default").get("counter") + 1;
    cache("default").set("counter", counter);
</bx:CouchbaseLock>

// ❌ Bad - holding lock too long
<bx:CouchbaseLock name="counter" cache="default">
    counter = cache("default").get("counter") + 1;
    sendEmail(); // Slow operation!
    callAPI(); // Network call!
    cache("default").set("counter", counter);
</bx:CouchbaseLock>
```

**Always use try/finally with manual locks:**
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

**Set appropriate timeouts:**
```js
// Short timeout for high-frequency operations
timeout = 1

// Longer timeout for critical operations
timeout = 10
```

### ❌ DON'T

**Don't use locks for caching:**
```js
// ❌ Wrong use case - use cache-aside pattern instead
<bx:CouchbaseLock name="expensive-calc">
    result = expensiveCalculation();
    cache("default").set("calc-result", result);
</bx:CouchbaseLock>
```

**Don't nest locks (deadlock risk):**
```js
// ❌ Potential deadlock
<bx:CouchbaseLock name="lock-A">
    <bx:CouchbaseLock name="lock-B">
        // Bad!
    </bx:CouchbaseLock>
</bx:CouchbaseLock>
```

**Don't hold locks during I/O:**
```js
// ❌ Don't do I/O while holding lock
<bx:CouchbaseLock name="data">
    data = getData();
    http url="http://api.example.com" result="apiResult"; // DON'T!
    saveData(data, apiResult);
</bx:CouchbaseLock>

// ✅ Do I/O outside lock
http url="http://api.example.com" result="apiResult";
<bx:CouchbaseLock name="data">
    data = getData();
    saveData(data, apiResult);
</bx:CouchbaseLock>
```

## 🔍 Testing

### Bypass Mode

Use `bypass=true` for testing without actual locking:

```js
// Production
<bx:CouchbaseLock name="test" cache="default" bypass="#application.isTestMode#">
    criticalOperation();
</bx:CouchbaseLock>

// In tests, set application.isTestMode = true
```

### Mock Scenarios

Test lock behavior with short timeouts:

```js
// Test timeout handling
<bx:CouchbaseLock
    name="test"
    cache="default"
    timeout="1"
    throwOnTimeout="false">
    // If lock acquired, do work
</bx:CouchbaseLock>
```

## 🐛 Troubleshooting

### Lock Timeout Errors

**Problem**: `Failed to acquire lock within X seconds`

**Solutions:**
1. Increase `timeout` parameter
2. Ensure locks are being released properly
3. Check for deadlocks or stuck processes
4. Verify lock expiration is appropriate

### Stale Locks

**Problem**: Lock seems permanently held

**Cause**: Locks auto-expire after `expires` seconds

**Solution**:
- Wait for expiration (max 30 seconds)
- Or manually remove lock document:
```js
couchbaseQuery(
    cacheName = "default",
    query = "DELETE FROM `bucket` WHERE META().id LIKE '__lock:%'"
);
```

### Performance Impact

**Problem**: Locking adds latency

**Solutions:**
1. Reduce lock duration - keep critical sections minimal
2. Use shorter timeouts for better responsiveness
3. Consider if locking is really needed
4. Cache frequently-accessed data outside locks

## 📊 Monitoring

Monitor lock usage:

```js
// Query all active locks
locks = couchbaseQuery(
    cacheName = "default",
    query = "SELECT META().id as lockKey, *
             FROM `bucket`
             WHERE META().id LIKE '__lock:%'"
);

println("Active locks: #locks.len()#");
locks.each(function(lock) {
    println("Lock: #lock.lockKey#");
});
```

## 🔗 Related Functions

- [couchbaseLock](reference/built-in-functions/CouchbaseLock.md) - Acquire lock
- [couchbaseUnlock](reference/built-in-functions/CouchbaseUnlock.md) - Release lock
- [CouchbaseLock Component](reference/components/CouchbaseLock.md) - Component reference

## 📚 See Also

- [Code Usage](code-usage.md) - Cache operations
- [Troubleshooting](troubleshooting.md) - Common issues
- [Couchbase Locking Documentation](https://docs.couchbase.com/java-sdk/current/howtos/concurrent-document-mutations.html#pessimistic-locking)
