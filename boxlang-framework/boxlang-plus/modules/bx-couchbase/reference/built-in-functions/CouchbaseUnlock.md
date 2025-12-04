# couchbaseUnlock

Release a distributed lock acquired with `couchbaseLock()` in manual mode.

## Syntax

```js
couchbaseUnlock(cacheName, name, cas)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cacheName` | String | Yes | Name of the Couchbase cache used for locking |
| `name` | String | Yes | Unique name of the lock to release |
| `cas` | Long | Yes | CAS value returned from `couchbaseLock()` |

## Returns

Returns boolean:
- `true` - Lock successfully released
- `false` - Lock not found or already released (no error thrown)

## Examples

### Basic Manual Lock/Unlock

```js
// Acquire lock
lockInfo = couchbaseLock(
    cacheName = "default",
    name = "user-update",
    timeout = 5,
    expires = 30
);

if (lockInfo.locked) {
    try {
        // Critical section
        updateUser(userId);
    } finally {
        // Always unlock!
        couchbaseUnlock("default", "user-update", lockInfo.cas);
    }
}
```

### With Error Handling

```js
lockInfo = couchbaseLock("default", "data-sync", 5, 30);

if (lockInfo.locked) {
    try {
        syncData();
    } catch (any e) {
        // Handle error
        logError(e);
    } finally {
        // Unlock even on error
        unlocked = couchbaseUnlock("default", "data-sync", lockInfo.cas);
        if (unlocked) {
            println("Lock released successfully");
        } else {
            println("Lock was already released or expired");
        }
    }
}
```

### Multiple Operations

```js
lockInfo = couchbaseLock("default", "batch-process", 5, 30);

if (lockInfo.locked) {
    try {
        processStep1();
        processStep2();
        processStep3();
    } finally {
        couchbaseUnlock("default", "batch-process", lockInfo.cas);
    }
}
```

### Conditional Unlock

```js
lockInfo = couchbaseLock("default", "config-update", 5, 30);
needsUnlock = lockInfo.locked;

if (lockInfo.locked) {
    try {
        if (shouldUpdateConfig()) {
            updateConfig();
        } else {
            // Early exit
            couchbaseUnlock("default", "config-update", lockInfo.cas);
            needsUnlock = false;
            return;
        }
    } finally {
        if (needsUnlock) {
            couchbaseUnlock("default", "config-update", lockInfo.cas);
        }
    }
}
```

### Long-Running Operation with Re-acquisition

```js
lockInfo = couchbaseLock("default", "long-task", 2, 30);

if (lockInfo.locked) {
    try {
        // Process in chunks
        while (hasMoreWork()) {
            processChunk();

            // Release lock periodically to let others in
            if (shouldYield()) {
                couchbaseUnlock("default", "long-task", lockInfo.cas);
                sleep(1000);

                // Re-acquire lock
                lockInfo = couchbaseLock("default", "long-task", 2, 30);
                if (!lockInfo.locked) {
                    println("Could not re-acquire lock");
                    break;
                }
            }
        }
    } finally {
        if (lockInfo.locked) {
            couchbaseUnlock("default", "long-task", lockInfo.cas);
        }
    }
}
```

### Inventory Management

```js
function reserveStock(productId, quantity) {
    lockInfo = couchbaseLock(
        cacheName = "inventory",
        name = "product-#productId#",
        timeout = 5,
        expires = 30
    );

    if (!lockInfo.locked) {
        return { success: false, error: "Could not acquire lock" };
    }

    try {
        product = getProduct(productId);

        if (product.stock < quantity) {
            return {
                success: false,
                error: "Insufficient stock",
                available: product.stock
            };
        }

        product.stock -= quantity;
        product.reserved += quantity;
        saveProduct(product);

        return {
            success: true,
            remaining: product.stock
        };
    } finally {
        couchbaseUnlock("inventory", "product-#productId#", lockInfo.cas);
    }
}
```

### Payment Processing

```js
function processPayment(orderId, amount) {
    lockInfo = couchbaseLock(
        cacheName = "payments",
        name = "order-#orderId#",
        timeout = 5,
        expires = 30
    );

    if (!lockInfo.locked) {
        throw("Payment already being processed");
    }

    try {
        order = getOrder(orderId);

        if (order.status != "pending") {
            throw("Order already processed");
        }

        // Process payment
        chargeResult = chargeCustomer(order.customerId, amount);

        if (chargeResult.success) {
            order.status = "paid";
            order.paidAt = now();
            saveOrder(order);

            sendConfirmation(order);

            return { success: true, orderId: orderId };
        } else {
            throw("Payment failed: #chargeResult.error#");
        }
    } finally {
        couchbaseUnlock("payments", "order-#orderId#", lockInfo.cas);
    }
}
```

## Notes

- **Safe to call**: Returns false if lock not found (no exception)
- **CAS required**: Must provide CAS from lock acquisition
- **Auto-expiry**: Locks expire after specified duration anyway
- **No-op if expired**: If lock already expired, returns false
- **Always call**: Use in finally block to ensure cleanup

## When to Use

Use `couchbaseUnlock()` when you need:
- **Fine-grained control** over lock lifecycle
- **Early release** before lock expiration
- **Conditional locking** based on runtime logic
- **Long operations** with periodic lock release/re-acquisition

For simpler use cases, prefer **callback mode** in `couchbaseLock()` which handles unlock automatically.

## Error Handling

`couchbaseUnlock()` does NOT throw exceptions:

```js
// Safe to call - returns false if lock not found
unlocked = couchbaseUnlock("default", "nonexistent", 12345);
println(unlocked); // false

// Safe to call multiple times
couchbaseUnlock("default", "test", cas); // true
couchbaseUnlock("default", "test", cas); // false (already unlocked)
```

## Best Practices

### ✅ DO

```js
// Always use finally block
lockInfo = couchbaseLock("default", "test", 5, 30);
if (lockInfo.locked) {
    try {
        doWork();
    } finally {
        couchbaseUnlock("default", "test", lockInfo.cas);
    }
}

// Check lock acquisition before unlock
if (lockInfo.locked) {
    // work
    couchbaseUnlock("default", "test", lockInfo.cas);
}
```

### ❌ DON'T

```js
// ❌ Forgetting to unlock
lockInfo = couchbaseLock("default", "test", 5, 30);
if (lockInfo.locked) {
    doWork();
    // FORGOT TO UNLOCK - lock will hold for 30 seconds!
}

// ❌ Unlock without try/finally
lockInfo = couchbaseLock("default", "test", 5, 30);
if (lockInfo.locked) {
    doWork(); // If this throws, lock won't be released!
    couchbaseUnlock("default", "test", lockInfo.cas);
}
```

## Callback Mode Alternative

Instead of manual lock/unlock, consider callback mode:

```js
// Manual mode (you unlock)
lockInfo = couchbaseLock("default", "test", 5, 30);
if (lockInfo.locked) {
    try {
        doWork();
    } finally {
        couchbaseUnlock("default", "test", lockInfo.cas);
    }
}

// Callback mode (automatic unlock)
couchbaseLock(
    cacheName = "default",
    name = "test",
    timeout = 5,
    expires = 30,
    callback = function() {
        doWork();
    }
);
```

Callback mode is simpler and safer for most use cases.

## Related Functions

- [couchbaseLock](CouchbaseLock.md) - Acquire lock
- [CouchbaseLock Component](../components/CouchbaseLock.md) - Component version

## See Also

- [Distributed Locking Guide](../../distributed-locking.md)
- [Code Usage](../../code-usage.md)
