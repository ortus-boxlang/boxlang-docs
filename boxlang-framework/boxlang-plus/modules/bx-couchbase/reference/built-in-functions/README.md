# Built-In Functions

Complete reference for all Couchbase module BIFs.

## 🔌 Provider & Connection Functions

Functions to access Couchbase components and manage connections:

* [**couchbaseGetProvider**](CouchbaseGetProvider.md) - Get cache provider instance
* [**couchbaseGetCluster**](CouchbaseGetCluster.md) - Get cluster connection
* [**couchbaseGetBucket**](CouchbaseGetBucket.md) - Get bucket instance
* [**couchbaseGetScope**](CouchbaseGetScope.md) - Get scope instance
* [**couchbaseGetCollection**](CouchbaseGetCollection.md) - Get collection instance

## 🤖 Vector Search Functions

AI/ML vector operations for semantic search and RAG applications:

* [**couchbaseVectorSearch**](CouchbaseVectorSearch.md) - Search by vector similarity
* [**couchbaseVectorAdd**](CouchbaseVectorAdd.md) - Store vector documents
* [**couchbaseVectorGet**](CouchbaseVectorGet.md) - Retrieve vector document
* [**couchbaseVectorDelete**](CouchbaseVectorDelete.md) - Delete vector document
* [**couchbaseVectorList**](CouchbaseVectorList.md) - List vector documents

## 📝 Query Functions

Execute N1QL/SQL++ queries:

* [**couchbaseQuery**](CouchbaseQuery.md) - Execute raw N1QL queries

## 🔒 Distributed Locking Functions

Coordinate operations across multiple servers with distributed locks:

* [**couchbaseLock**](CouchbaseLock.md) - Acquire distributed lock with optional callback
* [**couchbaseUnlock**](CouchbaseUnlock.md) - Release distributed lock manually

## 📖 Usage Patterns

### Basic Provider Access

```js
// Get provider
provider = couchbaseGetProvider("default");

// Get cluster
cluster = couchbaseGetCluster("default");

// Get bucket
bucket = couchbaseGetBucket("default");

// Get collection
collection = couchbaseGetCollection(
    cacheName = "default",
    scope = "_default",
    collection = "_default"
);
```

### Vector Operations Workflow

```js
// 1. Store vector
id = couchbaseVectorAdd(
    cacheName = "default",
    text = "Document content",
    embedding = getEmbedding(text),
    metadata = { category: "docs" }
);

// 2. Search vectors
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "mybucket._default._default",
    embedding = getEmbedding(query),
    limit = 5
);

// 3. Retrieve specific vector
doc = couchbaseVectorGet(cacheName = "default", id = id);

// 4. Delete vector
deleted = couchbaseVectorDelete(cacheName = "default", id = id);
```

### Query Patterns

```js
// Simple query
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE type = 'user'"
);

// Parameterized query
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE type = $type AND status = $status",
    parameters = {
        type: "user",
        status: "active"
    }
);
```

### Distributed Locking Patterns

```js
// Callback mode (automatic lock/unlock)
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
        return { success: true };
    }
);

// Manual mode (you control unlock)
lockInfo = couchbaseLock(
    cacheName = "default",
    name = "inventory-#productId#",
    timeout = 5,
    expires = 30
);

if (lockInfo.locked) {
    try {
        // Critical section
        updateInventory(productId);
    } finally {
        couchbaseUnlock("default", "inventory-#productId#", lockInfo.cas);
    }
}
```

## 🔗 Related Documentation

* [API Usage Guide](../../api-usage.md) - Detailed examples
* [AI Memory Guide](../../aimemory.md) - Vector search patterns
* [Distributed Locking Guide](../../distributed-locking.md) - Lock patterns and best practices
* [Reference Overview](../) - Configuration and settings
* [Troubleshooting](../../troubleshooting.md) - Common issues
