# couchbaseVectorGet

Retrieve a vector document by its ID.

## Syntax

```js
couchbaseVectorGet(cacheName, id)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cacheName` | String | Yes | Name of the cache configuration |
| `id` | String | Yes | Document ID to retrieve |

## Returns

Returns a struct containing the vector document:
- `id` - Document ID
- `type` - Document type (`"vector_document"`)
- `text` - Text content
- `embedding` - Vector embedding array
- `metadata` - Custom metadata struct
- `userId` - User ID (if set)
- `conversationId` - Conversation ID (if set)
- `createdAt` - Creation timestamp
- `updatedAt` - Last update timestamp

Returns an empty struct `{}` if document not found.

## Examples

### Basic Retrieval

```js
// Get vector document
doc = couchbaseVectorGet(
    cacheName = "default",
    id = "vec_12345"
);

if (!doc.isEmpty()) {
    println("Text: #doc.text#");
    println("Created: #doc.createdAt#");
}
```

### Check if Exists

```js
// Check if document exists
doc = couchbaseVectorGet("default", "vec_12345");

if (doc.isEmpty()) {
    println("Document not found");
} else {
    println("Found document: #doc.id#");
}
```

### Get with Metadata

```js
// Retrieve and use metadata
doc = couchbaseVectorGet("docs", "article-chunk-1");

if (!doc.isEmpty()) {
    println("Article: #doc.metadata.articleTitle#");
    println("Chunk: #doc.metadata.chunkIndex# of #doc.metadata.totalChunks#");
    println("Category: #doc.metadata.category#");
}
```

### Get User Document

```js
// Retrieve user-specific document
doc = couchbaseVectorGet("notes", "note_456");

if (!doc.isEmpty() && doc.userId == session.userId) {
    println("Your note: #doc.text#");
} else {
    println("Note not found or access denied");
}
```

### Verify Before Update

```js
// Get document before updating
doc = couchbaseVectorGet("default", "vec_789");

if (!doc.isEmpty()) {
    // Update the text but keep same embedding
    newId = couchbaseVectorAdd(
        cacheName = "default",
        text = "Updated content",
        embedding = doc.embedding, // Reuse embedding
        metadata = doc.metadata,
        id = doc.id // Update in place
    );
    println("Document updated");
}
```

### Get Conversation Context

```js
// Get specific message from conversation
messageId = "msg_123";
doc = couchbaseVectorGet("chat", messageId);

if (!doc.isEmpty()) {
    println("Conversation: #doc.conversationId#");
    println("User: #doc.userId#");
    println("Message: #doc.text#");
    println("Time: #doc.createdAt#");
}
```

### Retrieve Multiple Documents

```js
// Get multiple documents by IDs
ids = ["vec_1", "vec_2", "vec_3"];
documents = [];

ids.each(function(id) {
    doc = couchbaseVectorGet("default", id);
    if (!doc.isEmpty()) {
        documents.append(doc);
    }
});

println("Retrieved #documents.len()# of #ids.len()# documents");
```

### Validate Document Structure

```js
// Get and validate document
doc = couchbaseVectorGet("default", "vec_999");

if (!doc.isEmpty()) {
    // Check required fields
    hasText = structKeyExists(doc, "text");
    hasEmbedding = structKeyExists(doc, "embedding");
    hasMetadata = structKeyExists(doc, "metadata");
    
    if (hasText && hasEmbedding && hasMetadata) {
        println("Valid vector document");
        println("Embedding dimensions: #doc.embedding.len()#");
    } else {
        println("Invalid document structure");
    }
}
```

### Export Document

```js
// Get document and export to JSON
doc = couchbaseVectorGet("docs", "export_me");

if (!doc.isEmpty()) {
    // Convert to JSON for export
    jsonData = jsonSerialize(doc);
    fileWrite("/exports/document.json", jsonData);
    println("Document exported");
}
```

## Notes

- **Empty struct returned** - If document doesn't exist, returns `{}` instead of throwing error
- **Check existence** - Use `doc.isEmpty()` or `structKeyExists(doc, "id")` to check
- **Java HashMap** - Document is returned as HashMap (BoxLang is fully Java interop compatible)
- **No caching** - Always fetches fresh data from Couchbase
- **Case sensitivity** - Document IDs are case-sensitive

## Error Handling

```js
// Robust error handling
try {
    doc = couchbaseVectorGet("default", documentId);
    
    if (doc.isEmpty()) {
        // Document not found
        println("Document #documentId# not found");
    } else {
        // Process document
        processDocument(doc);
    }
} catch (any e) {
    // Connection or other error
    println("Error retrieving document: #e.message#");
}
```

## Related Functions

- [couchbaseVectorAdd](CouchbaseVectorAdd.md) - Store vector document
- [couchbaseVectorSearch](CouchbaseVectorSearch.md) - Search by similarity
- [couchbaseVectorDelete](CouchbaseVectorDelete.md) - Delete vector document
- [couchbaseVectorList](CouchbaseVectorList.md) - List vector documents

## See Also

- [API Usage Guide](../../api-usage.md)
- [AI Memory Guide](../../aimemory.md)
