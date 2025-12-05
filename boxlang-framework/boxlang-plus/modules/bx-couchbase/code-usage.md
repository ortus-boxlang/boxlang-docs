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
cache("default").set("username", "john_doe");

// Complex data structures
cache("default").set("user:123", {
    id: 123,
    name: "John Doe",
    email: "john@example.com",
    preferences: {
        theme: "dark",
        language: "en"
    }
});

// With expiration (in minutes)
cache("default").set("session:abc", sessionData, 60);

// Using a different cache
cache("sessions").set("temp:data", value, 5);
```

### Getting Cache Values

```js
// Simple get
username = cache("default").get("username");

// With default value if not found
username = cache("default").get("username") ?: "guest";

// From specific cache
data = cache("products").get("key");
```

### Checking Existence

```js
if (cache("default").lookup("user:123")) {
    println("User exists in cache");
}

// Get keys matching pattern
keys = cache("default").getKeys("user:*");
println("Total users in cache: #keys.len()#");
```

### Deleting Cache Values

```js
// Delete single key
cache("default").clear("user:123");

// Delete multiple keys
keys = ["user:123", "user:456", "user:789"];
keys.each(function(key) {
    cache("default").clear(key);
});

// Clear entire cache
cache("default").clearAll();
```

## 🔍 Advanced Operations

### Get Multiple Keys

```js
// Get multiple keys at once
keys = ["user:123", "user:456", "user:789"];
users = cache("default").getMulti(keys);

for (key in users) {
    println("#key#: #users[key].name#");
}
```

### Get All Keys

```js
// Get all keys (use with caution on large datasets)
allKeys = cache("default").getKeys();

// Get keys matching a pattern
userKeys = cache("default").getKeys("user:*");
```

### Get Cache Metadata

```js
metadata = cache("default").getCachedObjectMetadata("user:123");
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
    var user = cache("default").get(cacheKey);

    if (isNull(user)) {
        // Cache miss - load from database
        user = queryExecute(
            "SELECT * FROM users WHERE id = :id",
            { id: id }
        ).getRow(1);

        // Store in cache for 30 minutes
        cache("default").set(cacheKey, user, 30);
    }

    return user;
}
```

### Namespace Your Keys

```js
// Good - organized by prefix
cache("default").set("user:#userId#", userData);
cache("default").set("session:#sessionId#", sessionData);
cache("default").set("product:#sku#", productData);

// Easier to manage and clear
userKeys = cache("default").getKeys("user:*");
userKeys.each(function(key) {
    cache("default").clear(key);
});
```

### Handle Cache Failures Gracefully

```js
try {
    return cache("default").get("expensive:calculation");
} catch (any e) {
    // Cache is down, compute directly
    logError("Cache error: #e.message#");
    return computeExpensiveValue();
}
```

### Use Appropriate TTLs

```js
// Short-lived - frequently changing data
cache("default").set("stock:price:AAPL", price, 1); // 1 minute

// Medium-lived - relatively stable data
cache("default").set("user:profile:#id#", profile, 60); // 1 hour

// Long-lived - rarely changing data
cache("default").set("config:settings", settings, 1440); // 24 hours
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
cache("products").set("SKU12345", productData);
```

## 📊 Performance Tips

### Batch Operations

```js
// Instead of multiple individual operations
for (user in users) {
    cache("default").set("user:#user.id#", user);
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
stats = cache("default").getStats();
println("Object Count: #stats.getObjectCount()#");
println("Cache Size: #stats.getSize()# bytes");
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
