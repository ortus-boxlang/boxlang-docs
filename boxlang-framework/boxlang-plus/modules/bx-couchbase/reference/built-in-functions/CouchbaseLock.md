# couchbaseLock

Acquire a distributed lock using Couchbase, with optional callback for automatic lock management.

## Syntax

```js
// With callback (automatic lock management)
couchbaseLock(cacheName, name, [timeout], [expires], [callback], [throwOnTimeout])

// Without callback (manual lock management)
couchbaseLock(cacheName, name, [timeout], [expires], [throwOnTimeout])
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | String | Yes | - | Name of the Couchbase cache for locking |
| `name` | String | Yes | - | Unique name of the lock |
| `timeout` | Integer | No | `5` | Maximum seconds to wait for lock acquisition |
| `expires` | Integer | No | `30` | Lock expiration in seconds (max 30) |
| `callback` | Function | No | - | Function to execute while holding lock |
| `throwOnTimeout` | Boolean | No | `true` | Throw exception if lock not acquired |

## Returns

**With callback**: Returns the result of the callback function

**Without callback**: Returns struct:
```js
{
    "locked": boolean,      // Whether lock was acquired
    "lockId": string,       // Full lock key in Couchbase
    "cas": long,           // CAS value for unlock
    "lockName": string     // Lock name
}
```

## Examples

### Callback Mode (Recommended)

```js
// Execute function with automatic lock/unlock
result = couchbaseLock(
    cacheName = "default",
    name = "user-#userId#-update",
    timeout = 5,
    expires = 30,
    callback = function() {
        // Critical section - automatically locked
        user = getUser(userId);
        user.balance += amount;
        saveUser(user);
        return { success: true, newBalance: user.balance };
    }
);

println("New balance: #result.newBalance#");
```

### Manual Mode

```js
// Acquire lock manually
lockInfo = couchbaseLock(
    cacheName = "default",
    name = "inventory-#productId#",
    timeout = 5,
    expires = 30
);

if (lockInfo.locked) {
    try {
        // Critical section
        stock = getStock(productId);
        stock.quantity -= orderQty;
        saveStock(productId, stock);
    } finally {
        // Always unlock!
        couchbaseUnlock("default", "inventory-#productId#", lockInfo.cas);
    }
} else {
    println("Could not acquire lock");
}
```

### With Custom Timeout

```js
// Quick check with 1 second timeout
result = couchbaseLock(
    cacheName = "default",
    name = "config-reload",
    timeout = 1,
    expires = 30,
    throwOnTimeout = false,
    callback = function() {
        reloadConfiguration();
        return true;
    }
);

if (isNull(result)) {
    println("Another server is reloading config");
}
```

### Payment Processing

```js
function chargeCustomer(customerId, amount) {
    return couchbaseLock(
        cacheName = "payments",
        name = "charge-#customerId#",
        timeout = 5,
        expires = 30,
        callback = function() {
            customer = getCustomer(customerId);

            if (customer.balance < amount) {
                throw("Insufficient funds");
            }

            customer.balance -= amount;
            saveCustomer(customer);

            logTransaction(customerId, amount);

            return {
                success: true,
                newBalance: customer.balance,
                transactionId: createUUID()
            };
        }
    );
}

// Use it
try {
    result = chargeCustomer("user123", 99.99);
    println("Charged successfully. New balance: #result.newBalance#");
} catch (any e) {
    println("Payment failed: #e.message#");
}
```

### Batch Job Coordination

```js
// Ensure only one server processes the batch
function processDailyBatch() {
    return couchbaseLock(
        cacheName = "jobs",
        name = "daily-batch",
        timeout = 2,
        expires = 30,
        throwOnTimeout = false,
        callback = function() {
            println("Processing batch on server: #cgi.server_name#");

            records = getPendingRecords();
            records.each(function(record) {
                processRecord(record);
            });

            return {
                processed: records.len(),
                server: cgi.server_name
            };
        }
    );
}

// Run across all servers - only one will execute
result = processDailyBatch();
if (!isNull(result)) {
    println("Processed #result.processed# records on #result.server#");
} else {
    println("Another server is processing the batch");
}
```

### Rate Limiting

```js
function checkRateLimit(userId, maxPerMinute) {
    return couchbaseLock(
        cacheName = "default",
        name = "ratelimit-#userId#",
        timeout = 5,
        expires = 5,
        callback = function() {
            key = "ratelimit:#userId#";
            data = cache("default").get(key) ?: { count: 0, window: now() };

            // Reset if minute passed
            if (dateDiff("s", data.window, now()) >= 60) {
                data = { count: 0, window: now() };
            }

            // Check limit
            if (data.count >= maxPerMinute) {
                return {
                    allowed: false,
                    remaining: 0,
                    resetIn: 60 - dateDiff("s", data.window, now())
                };
            }

            // Increment
            data.count++;
            cache("default").set(key, data, 1);

            return {
                allowed: true,
                remaining: maxPerMinute - data.count
            };
        }
    );
}

// Use it
limit = checkRateLimit("user123", 100);
if (!limit.allowed) {
    throw("Rate limit exceeded. Try again in #limit.resetIn# seconds");
}
```

### Sequential Processing

```js
// Process documents one at a time across cluster
function processNextDocument() {
    lockInfo = couchbaseLock(
        cacheName = "processing",
        name = "document-queue",
        timeout = 1,
        expires = 30,
        throwOnTimeout = false
    );

    if (!lockInfo.locked) {
        return { skipped: true };
    }

    try {
        doc = getNextUnprocessedDocument();

        if (isNull(doc)) {
            return { completed: true };
        }

        processDocument(doc);
        markProcessed(doc.id);

        return {
            processed: true,
            documentId: doc.id
        };
    } finally {
        couchbaseUnlock("processing", "document-queue", lockInfo.cas);
    }
}
```

## Notes

- **Distributed**: Lock works across all servers in the cluster
- **30 Second Max**: Couchbase limits lock duration to 30 seconds
- **Auto-Expiry**: Locks automatically expire after specified duration
- **CAS-Based**: Unlock requires correct CAS value from acquisition
- **Callback Safer**: Callback mode ensures lock is always released
- **Manual Control**: Manual mode provides fine-grained control

## Lock Behavior

### With Callback

- Lock acquired before callback execution
- Callback executes with lock held
- Lock automatically released after callback (even on exception)
- Returns callback result or throws callback exception

### Without Callback

- Returns lock info immediately
- **You must manually unlock** using `couchbaseUnlock()`
- Always use try/finally to ensure unlock
- Lock auto-expires after `expires` seconds

## Error Handling

### With throwOnTimeout=true (default)

```js
try {
    couchbaseLock(
        cacheName = "default",
        name = "busy-lock",
        timeout = 1,
        callback = function() {
            doWork();
        }
    );
} catch (LockTimeoutException e) {
    println("Could not acquire lock: #e.message#");
}
```

### With throwOnTimeout=false

```js
result = couchbaseLock(
    cacheName = "default",
    name = "optional-lock",
    timeout = 1,
    throwOnTimeout = false,
    callback = function() {
        doWork();
        return "done";
    }
);

if (isNull(result)) {
    println("Lock not acquired, skipping operation");
} else {
    println("Operation completed: #result#");
}
```

## Best Practices

### ✅ DO

- Use callback mode for automatic cleanup
- Keep critical sections short
- Set appropriate timeouts
- Use descriptive lock names with IDs
- Always unlock in finally block (manual mode)

### ❌ DON'T

- Don't hold locks during I/O operations
- Don't nest locks (deadlock risk)
- Don't set expires > 30 seconds
- Don't forget to unlock (manual mode)
- Don't use locks for simple caching

## Related Functions

- [couchbaseUnlock](CouchbaseUnlock.md) - Release lock manually
- [CouchbaseLock Component](../components/CouchbaseLock.md) - Component version

## See Also

- [Distributed Locking Guide](../../distributed-locking.md)
- [Code Usage](../../code-usage.md)
- [Couchbase Locking](https://docs.couchbase.com/java-sdk/current/howtos/concurrent-document-mutations.html#pessimistic-locking)
