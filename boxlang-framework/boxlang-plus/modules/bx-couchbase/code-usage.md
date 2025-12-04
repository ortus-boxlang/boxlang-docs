---
icon: rectangle-code
description: Learn how to use the Couchbase cache provider in your BoxLang applications using the standard cache functions.
---

# 💻 Code Usage

Learn how to use the Couchbase cache provider in your BoxLang applications using the standard cache functions.

## 🎯 Cache Configuration

Configure Couchbase as a cache provider in your `Application.bx`:

```js
this.caches["default"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "myapp",
        "scope": "_default",
        "collection": "_default"
    }
};
```

## 📝 Basic Operations

### Setting Cache Values

```js
// Simple value
cacheSet("username", "john_doe");

// Complex data structures
cacheSet("user:123", {
    id: 123,
    name: "John Doe",
    email: "john@example.com",
    preferences: {
        theme: "dark",
        language: "en"
    }
});

// With expiration (in minutes)
cacheSet("session:abc", sessionData, 60);

// With specific cache name
cacheSet("temp:data", value, 5, "default");
```

### Getting Cache Values

```js
// Simple get
username = cacheGet("username");

// With default value if not found
username = cacheGet("username", "guest");

// Throw exception if not found
user = cacheGet("user:123", throwOnError=true);

// From specific cache
data = cacheGet("key", cacheName="default");
```

### Checking Existence

```js
if (cacheKeyExists("user:123")) {
    println("User exists in cache");
}

// Count keys matching pattern
count = cacheCount("user:*");
println("Total users in cache: #count#");
```

### Deleting Cache Values

```js
// Delete single key
cacheDelete("user:123");

// Delete multiple keys
cacheDelete(["user:123", "user:456", "user:789"]);

// Clear entire cache
cacheClear();

// Clear all caches
cacheClearAll();
```

## 🔍 Advanced Operations

### Get Multiple Keys

```js
// Get multiple keys at once
keys = ["user:123", "user:456", "user:789"];
users = cacheGetAll(keys);

for (key in users) {
    println("#key#: #users[key].name#");
}
```

### Get All Keys

```js
// Get all keys (use with caution on large datasets)
allKeys = cacheGetAllKeys();

// Get keys matching a pattern
userKeys = cacheGetAllKeys("user:*");
```

### Get Cache Metadata

```js
metadata = cacheGetMetadata("user:123");
println("Created: #metadata.createdTime#");
println("Hits: #metadata.hitCount#");
println("Expires: #metadata.timeout#");
```

## 🎨 Patterns and Best Practices

### Cache-Aside Pattern

```js
function getUser(id) {
    var cacheKey = "user:#id#";

    // Try cache first
    var user = cacheGet(cacheKey, null);

    if (isNull(user)) {
        // Cache miss - load from database
        user = queryExecute(
            "SELECT * FROM users WHERE id = :id",
            { id: id }
        ).getRow(1);

        // Store in cache for 30 minutes
        cacheSet(cacheKey, user, 30);
    }

    return user;
}
```

### Namespace Your Keys

```js
// Good - organized by prefix
cacheSet("user:#userId#", userData);
cacheSet("session:#sessionId#", sessionData);
cacheSet("product:#sku#", productData);

// Easier to manage and clear
cacheDelete(cacheGetAllKeys("user:*"));
```

### Handle Cache Failures Gracefully

```js
try {
    return cacheGet("expensive:calculation");
} catch (any e) {
    // Cache is down, compute directly
    logError("Cache error: #e.message#");
    return computeExpensiveValue();
}
```

### Use Appropriate TTLs

```js
// Short-lived - frequently changing data
cacheSet("stock:price:AAPL", price, 1); // 1 minute

// Medium-lived - relatively stable data
cacheSet("user:profile:#id#", profile, 60); // 1 hour

// Long-lived - rarely changing data
cacheSet("config:settings", settings, 1440); // 24 hours
```

## 🔄 Integration with Query Caching

```js
// Cache query results
query = queryExecute(
    sql = "SELECT * FROM products WHERE category = :cat",
    params = { cat: "electronics" },
    options = {
        cachedWithin: createTimeSpan(0, 1, 0, 0), // 1 hour
        cacheName: "default",
        cacheRegion: "queries"
    }
);
```

## 🎯 Working with Scopes

Couchbase supports scopes and collections for logical data organization:

```js
// Configure with specific scope/collection
this.caches["products"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "myapp",
        "scope": "inventory",
        "collection": "products"
    }
};

// Use the scoped cache
cacheSet("SKU12345", productData, cacheName="products");
```

## 📊 Performance Tips

### Batch Operations

```js
// Instead of multiple individual operations
for (user in users) {
    cacheSet("user:#user.id#", user);
}

// Use bulk operations when available
userData = {};
for (user in users) {
    userData["user:#user.id#"] = user;
}
// Note: Use couchbaseGetProvider() for bulk operations via Java SDK
```

### Connection Pooling

Connection pooling is automatic! The module manages connections efficiently behind the scenes.

### Monitor Cache Performance

```js
stats = cacheGetStatistics();
println("Hit Rate: #stats.hitRate#%");
println("Miss Rate: #stats.missRate#%");
println("Average Get Time: #stats.avgGetTime#ms");
```

## 🐛 Debugging

Enable debug logging in your `boxlang.json`:

```json
{
    "modules": {
        "bx-couchbase": {
            "debug": true
        }
    }
}
```

## 🔗 Next Steps

- **[API Usage](api-usage.md)** - Learn about the Built-In Functions
- **[Scope Storage](scope-storage.md)** - Use Couchbase for sessions
- **[AI Memory](aimemory.md)** - Explore vector search capabilities
