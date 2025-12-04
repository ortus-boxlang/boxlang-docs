# couchbaseVectorSearch

Search documents by vector similarity using semantic search with KNN (K-Nearest Neighbors).

## Syntax

```js
couchbaseVectorSearch(
    cacheName,
    collection,
    embedding,
    [limit],
    [userId],
    [conversationId],
    [metadata]
)
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | String | Yes | - | Name of the cache configuration |
| `collection` | String | Yes | - | Full collection path: `bucket.scope.collection` |
| `embedding` | Array | Yes | - | Vector embedding to search for (e.g., 1536 dimensions) |
| `limit` | Number | No | `10` | Maximum number of results to return |
| `userId` | String | No | - | Filter results by user ID |
| `conversationId` | String | No | - | Filter results by conversation ID |
| `metadata` | Struct | No | - | Additional metadata filters |

## Returns

Returns an array of structs, each containing:
- `id` - Document ID
- `text` - Document text content
- `embedding` - Vector embedding array
- `metadata` - Document metadata
- `score` - Similarity score (higher is better)
- `distance` - Vector distance (lower is better)
- `userId` - User ID (if set)
- `conversationId` - Conversation ID (if set)

## Examples

### Basic Semantic Search

```js
// Get embedding for search query
query = "How do I configure sessions?";
embedding = getOpenAIEmbedding(query);

// Search for similar documents
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 5
);

// Display results
results.each(function(result) {
    println("Score: #result.score# - #result.text#");
});
```

### Filter by User

```js
// Search only this user's documents
embedding = getOpenAIEmbedding("my previous orders");
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "app._default._default",
    embedding = embedding,
    userId = "user123",
    limit = 10
);
```

### Filter by Conversation

```js
// Search within a specific conversation context
embedding = getOpenAIEmbedding("what did we discuss about pricing?");
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "chat._default._default",
    embedding = embedding,
    conversationId = "conv456",
    limit = 5
);
```

### Filter by Metadata

```js
// Search with metadata filters
embedding = getOpenAIEmbedding("authentication documentation");
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 10,
    metadata = {
        category: "security",
        version: "2.0"
    }
);
```

### Combined Filters

```js
// Combine multiple filters
embedding = getOpenAIEmbedding(query);
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "app._default._default",
    embedding = embedding,
    limit = 20,
    userId = "user123",
    conversationId = "conv456",
    metadata = {
        type: "note",
        important: true
    }
);
```

### RAG Implementation

```js
function askAI(question) {
    // 1. Get embedding for question
    embedding = getOpenAIEmbedding(question);
    
    // 2. Search relevant documents
    context = couchbaseVectorSearch(
        cacheName = "docs",
        collection = "knowledge._default._default",
        embedding = embedding,
        limit = 3
    );
    
    // 3. Build prompt with context
    prompt = "Context:\n";
    context.each(function(doc) {
        prompt &= doc.text & "\n\n";
    });
    prompt &= "Question: #question#\n\nAnswer:";
    
    // 4. Get AI response
    return callOpenAI(prompt);
}

// Use it
answer = askAI("How do I configure Couchbase sessions?");
```

### Filtering Results by Score

```js
// Get results and filter by confidence
allResults = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 20
);

// Only keep high-confidence matches
relevant = allResults.filter(function(r) {
    return r.score >= 0.75; // 75% similarity threshold
});

if (relevant.len() > 0) {
    println("Found #relevant.len()# relevant documents");
} else {
    println("No relevant documents found");
}
```

## Notes

- **Embedding dimensions must match** - All vectors must have the same dimensions (e.g., 1536 for OpenAI)
- **Same model required** - Use the same embedding model for storage and search
- **Collection path format** - Use `bucket.scope.collection` format
- **KNN algorithm** - Uses SEARCH() with KNN for efficient similarity search
- **Performance** - Limit parameter controls result count; higher limits = slower queries
- **Filters are AND conditions** - All specified filters must match

## Use Cases

- 📚 **Documentation search** - Find relevant docs by semantic meaning
- 💬 **Chatbot memory** - Search previous conversations
- 🎯 **Recommendation systems** - Find similar products/content
- 🔍 **FAQ matching** - Match user questions to answers
- 📝 **Content discovery** - Find related articles/posts

## Related Functions

- [couchbaseVectorAdd](CouchbaseVectorAdd.md) - Store vector documents
- [couchbaseVectorGet](CouchbaseVectorGet.md) - Retrieve vector document
- [couchbaseVectorList](CouchbaseVectorList.md) - List vector documents
- [couchbaseQuery](CouchbaseQuery.md) - Execute custom queries

## See Also

- [AI Memory Guide](../../aimemory.md)
- [API Usage Guide](../../api-usage.md)
- [Couchbase Vector Search](https://docs.couchbase.com/server/current/fts/fts-vector-search.html)
