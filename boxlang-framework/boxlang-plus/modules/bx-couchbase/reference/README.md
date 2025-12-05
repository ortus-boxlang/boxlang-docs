---
icon: books
description: Complete reference for all Couchbase module functions and configuration options.
---

# 📚 Reference Documentation

Complete reference for all Couchbase module functions and configuration options.

## 📖 Built-In Functions (BIFs)

The Couchbase module provides 13 BIFs for interacting with Couchbase Server:

### 🔌 Provider & Connection Functions

Functions for accessing Couchbase components:

- [**couchbaseGetProvider**](built-in-functions/CouchbaseGetProvider.md) - Get the Couchbase cache provider instance
- [**couchbaseGetCluster**](built-in-functions/CouchbaseGetCluster.md) - Get the Couchbase cluster connection
- [**couchbaseGetBucket**](built-in-functions/CouchbaseGetBucket.md) - Get a specific Couchbase bucket
- [**couchbaseGetScope**](built-in-functions/CouchbaseGetScope.md) - Get a specific scope within a bucket
- [**couchbaseGetCollection**](built-in-functions/CouchbaseGetCollection.md) - Get a specific collection within a scope

### 🤖 Vector Search Functions

Functions for AI/ML vector operations:

- [**couchbaseVectorSearch**](built-in-functions/CouchbaseVectorSearch.md) - Search documents by vector similarity
- [**couchbaseVectorAdd**](built-in-functions/CouchbaseVectorAdd.md) - Store vector documents with embeddings
- [**couchbaseVectorGet**](built-in-functions/CouchbaseVectorGet.md) - Retrieve vector document by ID
- [**couchbaseVectorDelete**](built-in-functions/CouchbaseVectorDelete.md) - Delete vector document by ID
- [**couchbaseVectorList**](built-in-functions/CouchbaseVectorList.md) - List vector documents with filters

### 📝 Query Functions

Functions for N1QL/SQL++ queries:

- [**couchbaseQuery**](built-in-functions/CouchbaseQuery.md) - Execute raw N1QL queries with parameters

### 🔒 Distributed Locking Functions

Functions for coordinating operations across multiple servers:

- [**couchbaseLock**](built-in-functions/CouchbaseLock.md) - Acquire distributed lock with optional callback
- [**couchbaseUnlock**](built-in-functions/CouchbaseUnlock.md) - Release distributed lock manually

## 🧩 Components

The Couchbase module provides components for advanced functionality:

### 🔒 Distributed Locking Components

- [**CouchbaseLock**](components/CouchbaseLock.md) - Execute code with automatic distributed lock management

## 🗄️ Cache Provider Functions

All standard BoxLang cache operations work with Couchbase:

```js
// Set cache value
cache("default").set("key", value, timeoutMinutes);

// Get cache value
data = cache("default").get("key");

// Delete cache value
cache("default").clear("key");

// Check if key exists
exists = cache("default").lookup("key");

// Clear all cache entries
cache("default").clearAll();

// Get cache statistics
stats = cache("default").getStats();
```

See [BoxLang Cache Documentation](https://boxlang.ortusbooks.com/) for complete cache API reference.

## ⚙️ Configuration Reference

### Cache Provider Properties

```js
this.caches["cacheName"] = {
    "provider": "Couchbase",
    "properties": {
        // Required
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "default",

        // Optional
        "scope": "_default",
        "collection": "_default",
        "connectTimeout": "10000",
        "kvTimeout": "2500",
        "maxConnections": 20,

        // TTL settings
        "defaultTimeout": 60,
        "evictionPolicy": "LRU"
    }
};
```

### Property Descriptions

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `connectionString` | String | Yes | - | Couchbase connection string (e.g., `couchbase://localhost`) |
| `username` | String | Yes | - | Couchbase username |
| `password` | String | Yes | - | Couchbase password |
| `bucket` | String | Yes | - | Bucket name to use |
| `scope` | String | No | `_default` | Scope within the bucket |
| `collection` | String | No | `_default` | Collection within the scope |
| `connectTimeout` | Number | No | `10000` | Connection timeout in milliseconds |
| `kvTimeout` | Number | No | `2500` | Key-value operation timeout in milliseconds |
| `maxConnections` | Number | No | `20` | Maximum number of connections in pool |
| `defaultTimeout` | Number | No | `60` | Default TTL for cache entries (minutes) |
| `evictionPolicy` | String | No | `LRU` | Cache eviction policy (set in Couchbase) |

### Session Storage Configuration

```js
this.sessionManagement = true;
this.sessionStorage = "couchbase-sessions";
this.sessionTimeout = createTimeSpan(0, 0, 30, 0); // 30 minutes

this.caches["couchbase-sessions"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "sessions",
        "scope": "_default",
        "collection": "boxlang_sessions",
        "defaultTimeout": 30
    }
};
```

### Application Storage Configuration

```js
this.applicationStorage = "couchbase-app";

this.caches["couchbase-app"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "applications",
        "scope": "_default",
        "collection": "boxlang_apps"
    }
};
```

## 🔐 Security Configuration

### Secure Connections (TLS/SSL)

```js
"connectionString": "couchbases://cluster.example.com" // Note the 's'
```

### Certificate-Based Authentication

```js
"properties": {
    "connectionString": "couchbases://cluster.example.com",
    "certificatePath": "/path/to/cert.pem",
    "keyPath": "/path/to/key.pem"
}
```

### Environment Variables

```js
"properties": {
    "connectionString": env("COUCHBASE_CONNECTION"),
    "username": env("COUCHBASE_USER"),
    "password": env("COUCHBASE_PASS"),
    "bucket": env("COUCHBASE_BUCKET")
}
```

## 📊 Vector Search Configuration

### Vector Index Creation

```js
// Create vector index for semantic search
couchbaseQuery(
    cacheName = "default",
    query = "CREATE INDEX idx_embedding ON `mybucket`(embedding VECTOR) WHERE type = 'vector_document'"
);
```

### Recommended Vector Settings

```js
// Document structure for vectors
{
    "type": "vector_document",
    "text": "Document content",
    "embedding": [0.1, 0.2, ...], // 1536 dimensions for OpenAI
    "metadata": {
        "category": "docs",
        "importance": "high"
    },
    "userId": "user123",
    "conversationId": "conv456",
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-15T10:30:00Z"
}
```

## 🔗 Related Documentation

- [Code Usage Guide](../code-usage.md) - Examples and patterns
- [Distributed Locking Guide](../distributed-locking.md) - Lock patterns and best practices
- [Scope Storage Guide](../scope-storage.md) - Session and application storage
- [API Usage](../api-usage.md) - Complete BIF documentation
- [AI Memory Guide](../aimemory.md) - Vector search and RAG patterns
- [Troubleshooting](../troubleshooting.md) - Common issues and solutions

## 📖 External Resources

- [Couchbase Server Documentation](https://docs.couchbase.com/)
- [N1QL Language Reference](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/index.html)
- [Couchbase Java SDK](https://docs.couchbase.com/java-sdk/current/hello-world/start-using-sdk.html)
- [BoxLang Documentation](https://boxlang.ortusbooks.com/)
