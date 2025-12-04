---
icon: brackets-curly
description: Explore the powerful Built-In Functions (BIFs) provided by the BoxLang Couchbase Module for advanced caching, session storage, and AI vector search capabilities.
---

# 🛠️ API Usage - Built-In Functions

This module provides powerful Built-In Functions (BIFs) for direct interaction with Couchbase, including vector search capabilities for AI applications.

## 🎯 Core Provider Functions

### couchbaseGetProvider()

Get the Couchbase cache provider instance for advanced operations.

```js
provider = couchbaseGetProvider("default");
// Returns: CouchbaseCache instance
```

**Parameters:**
- `cacheName` (required) - Name of the configured cache

**Example:**
```js
provider = couchbaseGetProvider("myCache");
collection = provider.getCollection();
```

### couchbaseGetCluster()

Get the Java Cluster instance for advanced Couchbase operations.

```js
cluster = couchbaseGetCluster("default");
// Returns: com.couchbase.client.java.Cluster
```

**Use Cases:**
- Execute raw N1QL queries
- Access cluster-level operations
- Manage indexes and buckets

### couchbaseGetBucket()

Get the Java Bucket instance.

```js
bucket = couchbaseGetBucket("default");
// Returns: com.couchbase.client.java.Bucket
```

### couchbaseGetScope()

Get the Java Scope instance.

```js
scope = couchbaseGetScope("default");
// Returns: com.couchbase.client.java.Scope
```

### couchbaseGetCollection()

Get the Java Collection instance for direct document operations.

```js
collection = couchbaseGetCollection("default");
// Returns: com.couchbase.client.java.Collection
```

## 🤖 Vector Search Functions

### couchbaseVectorSearch()

Perform semantic vector search using KNN (K-Nearest Neighbors).

```js
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "myapp._default._default",
    embedding = embeddingArray,
    limit = 10,
    userId = "user123",
    conversationId = "conv456"
);
```

**Parameters:**
- `cacheName` (required) - Cache provider name
- `collection` (required) - Full collection path: `bucket.scope.collection`
- `embedding` (required) - Vector embedding array (e.g., from OpenAI)
- `limit` (optional) - Max results to return (default: 10)
- `filter` (optional) - Struct with metadata filters
- `userId` (optional) - Filter by user ID
- `conversationId` (optional) - Filter by conversation ID

**Returns:** Array of structs with:
```js
[
    {
        "id": "vec_abc123",
        "text": "Original text content",
        "embedding": [0.1, 0.2, ...],
        "metadata": { "category": "tech" },
        "userId": "user123",
        "conversationId": "conv456",
        "score": 0.95,
        "distance": 0.05
    }
]
```

**Example:**
```js
// Get embedding from OpenAI
embedding = getOpenAIEmbedding("machine learning tutorial");

// Search similar content
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 5,
    filter = { "category": "tutorials" }
);

for (doc in results) {
    println("#doc.text# (Score: #doc.score#)");
}
```

### couchbaseVectorAdd()

Store a vector document with embeddings.

```js
docId = couchbaseVectorAdd(
    cacheName = "default",
    text = "My document content",
    embedding = embeddingArray,
    metadata = { "category": "tech", "author": "John" },
    userId = "user123",
    conversationId = "conv456",
    id = "custom_id" // optional
);
```

**Parameters:**
- `cacheName` (required) - Cache provider name
- `text` (required) - Text content
- `embedding` (required) - Vector embedding array
- `metadata` (optional) - Struct with custom metadata
- `userId` (optional) - User ID
- `conversationId` (optional) - Conversation ID
- `id` (optional) - Custom document ID (auto-generated if omitted)

**Returns:** Document ID (string)

**Example:**
```js
// Store a document with embedding
embedding = getOpenAIEmbedding("BoxLang is awesome!");

docId = couchbaseVectorAdd(
    cacheName = "default",
    text = "BoxLang is awesome!",
    embedding = embedding,
    metadata = {
        "category": "testimonial",
        "rating": 5
    },
    userId = "john_doe"
);

println("Stored document: #docId#");
```

### couchbaseVectorGet()

Retrieve a vector document by ID.

```js
doc = couchbaseVectorGet(
    cacheName = "default",
    id = "vec_abc123"
);
```

**Returns:** Struct with document data or empty struct if not found
```js
{
    "id": "vec_abc123",
    "type": "vector_document",
    "text": "Document content",
    "embedding": [0.1, 0.2, ...],
    "metadata": { "category": "tech" },
    "userId": "user123",
    "conversationId": "conv456",
    "createdAt": 1701234567890,
    "updatedAt": 1701234567890
}
```

### couchbaseVectorDelete()

Delete a vector document.

```js
success = couchbaseVectorDelete(
    cacheName = "default",
    id = "vec_abc123"
);
// Returns: true if deleted, false if not found
```

### couchbaseVectorList()

List vector documents with optional filters.

```js
docs = couchbaseVectorList(
    cacheName = "default",
    collection = "myapp._default._default",
    userId = "user123",
    conversationId = "conv456",
    filter = { "category": "tech" },
    limit = 100
);
```

**Parameters:**
- `cacheName` (required) - Cache provider name
- `collection` (required) - Full collection path
- `userId` (optional) - Filter by user ID
- `conversationId` (optional) - Filter by conversation ID
- `filter` (optional) - Struct with metadata filters
- `limit` (optional) - Max results (default: 100)

**Returns:** Array of document structs

## 📝 Query Functions

### couchbaseQuery()

Execute raw N1QL/SQL++ queries.

```js
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `myapp`.`_default`.`_default` WHERE type = $type",
    parameters = { "type": "user" }
);
```

**Parameters:**
- `cacheName` (required) - Cache provider name
- `query` (required) - N1QL query string
- `parameters` (optional) - Struct with query parameters

**Returns:** Array of result rows (structs)

**Examples:**

```js
// Simple query
users = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `myapp` WHERE role = 'admin'"
);

// Parameterized query
products = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `products` WHERE category = $cat AND price < $maxPrice",
    parameters = {
        "cat": "electronics",
        "maxPrice": 1000
    }
);

// Aggregation
stats = couchbaseQuery(
    cacheName = "default",
    query = "SELECT category, COUNT(*) as count, AVG(price) as avgPrice FROM `products` GROUP BY category"
);

// Join query
orders = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT o.*, u.name as userName
        FROM `orders` o
        JOIN `users` u ON o.userId = META(u).id
        WHERE o.status = $status
    ",
    parameters = { "status": "pending" }
);
```

## 🎯 Complete Example: AI Chatbot

```js
component {
    this.name = "AIChatbot";

    this.caches["default"] = {
        "provider": "Couchbase",
        "properties": {
            "connectionString": "couchbase://localhost",
            "username": "Administrator",
            "password": "password",
            "bucket": "chatbot"
        }
    };

    function storeMessage(userId, conversationId, message) {
        // Get embedding from OpenAI
        var embedding = getOpenAIEmbedding(message);

        // Store in Couchbase
        return couchbaseVectorAdd(
            cacheName = "default",
            text = message,
            embedding = embedding,
            metadata = {
                "timestamp": now(),
                "type": "user_message"
            },
            userId = userId,
            conversationId = conversationId
        );
    }

    function searchSimilarMessages(userId, query, limit=5) {
        var embedding = getOpenAIEmbedding(query);

        return couchbaseVectorSearch(
            cacheName = "default",
            collection = "chatbot._default._default",
            embedding = embedding,
            userId = userId,
            limit = limit
        );
    }

    function getConversationHistory(userId, conversationId) {
        return couchbaseVectorList(
            cacheName = "default",
            collection = "chatbot._default._default",
            userId = userId,
            conversationId = conversationId,
            limit = 50
        );
    }

    function deleteConversation(conversationId) {
        // Get all messages in conversation
        var messages = couchbaseQuery(
            cacheName = "default",
            query = "SELECT META().id FROM `chatbot` WHERE conversationId = $convId",
            parameters = { "convId": conversationId }
        );

        // Delete each message
        for (var msg in messages) {
            couchbaseVectorDelete(
                cacheName = "default",
                id = msg.id
            );
        }
    }
}
```

## 🎨 Helper Function: Get OpenAI Embedding

```js
function getOpenAIEmbedding(text) {
    var apiKey = env("OPENAI_API_KEY");

    var response = httpRequest(
        url = "https://api.openai.com/v1/embeddings",
        method = "POST",
        headers = {
            "Authorization": "Bearer #apiKey#",
            "Content-Type": "application/json"
        },
        body = serializeJSON({
            "model": "text-embedding-3-small",
            "input": text
        })
    );

    var result = deserializeJSON(response.fileContent);
    return result.data[1].embedding;
}
```

## 🔗 Next Steps

- **[AI Memory Documentation](aimemory.md)** - Deep dive into vector search
- **[BIF Reference](reference/built-in-functions/)** - Complete API documentation
- **[Code Usage](code-usage.md)** - Basic cache operations
