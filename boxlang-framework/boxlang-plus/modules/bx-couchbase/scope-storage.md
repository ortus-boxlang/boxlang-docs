---
icon: microscope
description: Use Couchbase as the storage backend for BoxLang session and application scopes, providing distributed, fault-tolerant scope storage that scales across multiple servers.
---

# 🗄️ Scope Storage

Use Couchbase as the storage backend for your BoxLang session and application scopes. This provides distributed, fault-tolerant scope storage that survives application restarts and scales across multiple servers.

## 🎯 Session Storage

### Configuration

Configure Couchbase as your session storage provider in `Application.bx`:

```js
component {
    this.name = "MyApp";
    this.sessionManagement = true;
    this.sessionStorage = "couchbase-sessions";
    this.sessionTimeout = createTimeSpan(0, 2, 0, 0); // 2 hours

    this.caches["couchbase-sessions"] = {
        "provider": "Couchbase",
        "properties": {
            "connectionString": "couchbase://localhost",
            "username": "Administrator",
            "password": "password",
            "bucket": "myapp",
            "scope": "sessions",
            "collection": "user_sessions"
        }
    };
}
```

### Using Session Scope

Once configured, use the session scope normally:

```js
// Store data in session
session.userID = 123;
session.username = "john_doe";
session.cart = {
    items: [],
    total: 0
};

// Read from session
if (structKeyExists(session, "userID")) {
    println("Welcome back, #session.username#!");
}

// Session data is automatically stored in Couchbase
```

### Benefits

- ✅ **Distributed**: Sessions survive server restarts
- ✅ **Scalable**: Share sessions across multiple servers
- ✅ **Fast**: Sub-millisecond access times
- ✅ **Secure**: Sessions stored in dedicated collection

## 🌐 Application Scope Storage

### Configuration

```js
component {
    this.name = "MyApp";
    this.applicationTimeout = createTimeSpan(1, 0, 0, 0); // 1 day
    this.applicationStorage = "couchbase-app";

    this.caches["couchbase-app"] = {
        "provider": "Couchbase",
        "properties": {
            "connectionString": "couchbase://localhost",
            "username": "Administrator",
            "password": "password",
            "bucket": "myapp",
            "scope": "application",
            "collection": "app_data"
        }
    };
}
```

### Using Application Scope

```js
// Store application-wide data
application.startTime = now();
application.config = {
    apiKey: "secret123",
    maxUsers: 1000,
    features: ["chat", "notifications"]
};

// Cache frequently accessed data
application.activeUsers = queryExecute(
    "SELECT COUNT(*) as count FROM sessions WHERE lastActivity > :cutoff",
    { cutoff: dateAdd("n", -30, now()) }
).count;
```

## 🔧 Advanced Configuration

### Separate Collections for Different Scope Types

```js
this.caches["sessions"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": env("COUCHBASE_URL"),
        "username": env("COUCHBASE_USER"),
        "password": env("COUCHBASE_PASS"),
        "bucket": "myapp",
        "scope": "sessions",
        "collection": "user_sessions",
        "kvTimeout": "1000" // Fast timeout for sessions
    }
};

this.caches["application"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": env("COUCHBASE_URL"),
        "username": env("COUCHBASE_USER"),
        "password": env("COUCHBASE_PASS"),
        "bucket": "myapp",
        "scope": "application",
        "collection": "app_data",
        "kvTimeout": "2500" // Standard timeout
    }
};
```

### Session Clustering

For load-balanced applications:

```js
this.caches["sessions"] = {
    "provider": "Couchbase",
    "properties": {
        // Multiple nodes for high availability
        "connectionString": "couchbase://node1.example.com,node2.example.com,node3.example.com",
        "username": "appuser",
        "password": env("DB_PASSWORD"),
        "bucket": "sessions",
        "scope": "_default",
        "collection": "_default"
    }
};
```

## 📊 Monitoring Session Activity

### Query Active Sessions

```js
provider = couchbaseGetProvider("sessions");
cluster = couchbaseGetCluster("sessions");

// Count active sessions
result = couchbaseQuery(
    cacheName = "sessions",
    query = "SELECT COUNT(*) as total FROM `myapp`.`sessions`.`user_sessions` WHERE lastActivity > $cutoff",
    parameters = { cutoff: dateAdd("n", -30, now()) }
);

println("Active sessions: #result[1].total#");
```

### Find Sessions by User

```js
userSessions = couchbaseQuery(
    cacheName = "sessions",
    query = "SELECT META().id, * FROM `myapp`.`sessions`.`user_sessions` WHERE userID = $userId",
    parameters = { userId: 123 }
);
```

## 🧹 Session Cleanup

### Manual Cleanup

```js
// Delete expired sessions
couchbaseQuery(
    cacheName = "sessions",
    query = "DELETE FROM `myapp`.`sessions`.`user_sessions` WHERE lastActivity < $cutoff",
    parameters = { cutoff: dateAdd("h", -2, now()) }
);
```

### Automatic Expiration

Configure TTL (Time To Live) at the cache level:

```js
this.caches["sessions"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "myapp",
        "defaultExpiration": 7200 // 2 hours in seconds
    }
};
```

## 🔐 Security Best Practices

### 1. Use Dedicated Credentials

```js
// Don't use Administrator account in production!
this.caches["sessions"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbases://cluster.example.com",
        "username": "session_app", // Limited permissions
        "password": env("SESSION_DB_PASSWORD"),
        "bucket": "sessions"
    }
};
```

### 2. Use TLS/SSL

```js
// Use couchbases:// for encrypted connections
"connectionString": "couchbases://secure-cluster.example.com"
```

### 3. Separate Sensitive Data

```js
// Don't store passwords or credit cards in session
session.userID = 123;
session.username = "john";
// ❌ session.password = "secret123";
// ❌ session.creditCard = "1234-5678-9012-3456";
```

## 🎯 Performance Optimization

### Session Granularity

```js
// Instead of storing entire user object
session.user = {
    id: 123,
    name: "John",
    email: "john@example.com",
    preferences: {...},
    history: [...] // Large array
};

// Store only what you need
session.userID = 123;
session.username = "John";
// Load full profile on demand
```

### Lazy Loading

```js
function getUserProfile() {
    if (!structKeyExists(session, "profile")) {
        session.profile = queryExecute(
            "SELECT * FROM users WHERE id = :id",
            { id: session.userID }
        ).getRow(1);
    }
    return session.profile;
}
```

## 🐛 Troubleshooting

### Sessions Not Persisting

Check that `sessionStorage` matches your cache name:

```js
this.sessionStorage = "couchbase-sessions"; // Must match cache key
this.caches["couchbase-sessions"] = { ... };
```

### Connection Errors

Verify Couchbase is running and accessible:

```bash
curl -u Administrator:password http://localhost:8091/pools
```

### Performance Issues

Monitor cache statistics:

```js
stats = cache("sessions").getStats();
println("Object Count: #stats.getObjectCount()#");
println("Cache Size: #stats.getSize()# bytes");
```

## 🔗 Next Steps

- **[Code Usage](code-usage.md)** - Learn basic cache operations
- **[API Usage](api-usage.md)** - Explore the BIFs
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions
