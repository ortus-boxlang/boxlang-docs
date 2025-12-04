---
icon: database
description: With the BoxLang Couchbase Module, connect to Couchbase clusters for caching, session storage, and AI vector memory.
---

# 🚀 BoxLang Couchbase Module

Welcome to the BoxLang Couchbase Module! This module provides enterprise-grade caching, session storage, and AI vector memory capabilities powered by Couchbase's distributed NoSQL database.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](bx-plus/README.md) with a limited trial.
{% endhint %}

## 🎯 What is Couchbase?

Couchbase is a distributed NoSQL document database with built-in caching, full-text search, and vector search capabilities. It combines the best of key-value stores with the flexibility of document databases, making it ideal for:

- High-performance caching
- Session and application state storage
- AI vector embeddings and semantic search
- Real-time applications
- Multi-data center deployments

## 📦 Installation

```bash
# For Operating Systems using our Quick Installer.
install-bx-module bx-couchbase

# Using CommandBox to install for web servers.
box install bx-couchbase
```

## ⚡ Key Features

### Distributed Caching
Store cache data across multiple nodes with automatic failover and replication. Sub-millisecond response times for key-value operations.

### Vector Search
Built-in support for AI vector embeddings with semantic search using KNN (K-Nearest Neighbors). Perfect for RAG (Retrieval Augmented Generation) applications, chatbots, and recommendation systems.

### Session Storage
Use Couchbase as your session or application scope storage backend. Automatic serialization and deserialization of BoxLang data types.

### N1QL Queries
Execute SQL++ queries (N1QL) directly from BoxLang. Full support for joins, aggregations, and complex filtering.

### Cluster Support
Configure multi-node clusters with automatic discovery and failover. Supports secure connections with TLS.

## 📖 Documentation Structure

- **[Code Usage](code-usage.md)** - Working with the cache provider
- **[API Usage](api-usage.md)** - Using Built-In Functions (BIFs)
- **[Scope Storage](scope-storage.md)** - Session and application storage
- **[AI Memory](aimemory.md)** - Vector embeddings and semantic search
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions
- **[BIF Reference](reference/built-in-functions/)** - Complete BIF documentation

## 🚀 Quick Example

```js
// In Application.bx
this.caches["default"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "myapp"
    }
};

// In your code
cacheSet("user:123", {
    name: "John Doe",
    email: "john@example.com",
    role: "admin"
});

user = cacheGet("user:123");
println("Welcome, #user.name#!");

// Vector search
embedding = getOpenAIEmbedding("machine learning tutorial");
similar = couchbaseVectorSearch(
    cacheName = "default",
    collection = "myapp._default._default",
    embedding = embedding,
    limit = 5
);
```

## 💡 Use Cases

### 🎯 Application Caching
Cache database query results, API responses, or computed values to reduce latency and database load.

### 👤 Session Management
Store user sessions in a distributed cache that survives application restarts and scales across multiple servers.

### 🤖 AI/ML Applications
Store and search vector embeddings for semantic search, recommendation systems, and RAG chatbots.

### 📊 Real-Time Analytics
Cache aggregated metrics and dashboards with automatic expiration and refresh.

### 🌐 Multi-Region Deployments
Replicate cache data across geographic regions for low-latency access worldwide.

## 🔧 Requirements

- BoxLang 1.0.0+
- Couchbase Server 7.0+ (7.6+ recommended for vector search)
- Java 21+

## 📦 Installation

```bash
# Install via BoxLang CLI
boxlang install bx-couchbase

# Or add to box.json
{
    "dependencies": {
        "bx-couchbase": "^1.0.0"
    }
}
```

## 🎓 Next Steps

Ready to dive in? Start with:

1. **[Code Usage](code-usage.md)** - Learn the basic cache operations
2. **[API Usage](api-usage.md)** - Explore the Built-In Functions
3. **[AI Memory](aimemory.md)** - Build AI-powered applications

Need help? Check out [Troubleshooting](troubleshooting.md) or visit our [community forums](https://community.ortussolutions.com).
