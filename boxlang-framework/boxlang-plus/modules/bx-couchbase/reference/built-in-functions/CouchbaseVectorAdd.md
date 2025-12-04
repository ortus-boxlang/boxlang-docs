# couchbaseVectorAdd

Store a vector document with text content, embedding, and metadata.

## Syntax

```js
couchbaseVectorAdd(
    cacheName,
    text,
    embedding,
    [metadata],
    [userId],
    [conversationId],
    [id]
)
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | String | Yes | - | Name of the cache configuration |
| `text` | String | Yes | - | Text content to store |
| `embedding` | Array | Yes | - | Vector embedding array (e.g., 1536 dimensions) |
| `metadata` | Struct | No | `{}` | Custom metadata to store with document |
| `userId` | String | No | - | User ID to associate with document |
| `conversationId` | String | No | - | Conversation ID to associate with document |
| `id` | String | No | Auto-generated | Custom document ID (otherwise generates `vec_UUID`) |

## Returns

Returns the document ID (string) of the stored vector document.

## Examples

### Basic Storage

```js
// Get embedding from OpenAI
text = "BoxLang sessions can be stored in Couchbase for distributed applications.";
embedding = getOpenAIEmbedding(text);

// Store vector document
id = couchbaseVectorAdd(
    cacheName = "default",
    text = text,
    embedding = embedding
);

println("Stored with ID: #id#");
```

### Store with Metadata

```js
text = "Configure session storage using this.sessionStorage in Application.bx";
embedding = getOpenAIEmbedding(text);

id = couchbaseVectorAdd(
    cacheName = "docs",
    text = text,
    embedding = embedding,
    metadata = {
        category: "configuration",
        docType: "guide",
        version: "1.0",
        importance: "high"
    }
);
```

### Store with User Context

```js
// Store user-specific document
userNote = "Remember to check the API documentation for rate limits";
embedding = getOpenAIEmbedding(userNote);

id = couchbaseVectorAdd(
    cacheName = "notes",
    text = userNote,
    embedding = embedding,
    userId = "user123",
    metadata = {
        type: "note",
        category: "reminder"
    }
);
```

### Store Conversation Memory

```js
// Store message in conversation history
message = "User asked about database connection pooling";
embedding = getOpenAIEmbedding(message);

id = couchbaseVectorAdd(
    cacheName = "chat",
    text = message,
    embedding = embedding,
    userId = "user456",
    conversationId = "conv789",
    metadata = {
        role: "user",
        timestamp: now()
    }
);
```

### Custom Document ID

```js
// Use custom ID instead of auto-generated
text = "Important: Always validate user input before processing";
embedding = getOpenAIEmbedding(text);

id = couchbaseVectorAdd(
    cacheName = "docs",
    text = text,
    embedding = embedding,
    id = "security-rule-001",
    metadata = {
        category: "security",
        priority: "critical"
    }
);
```

### Batch Storage

```js
// Store multiple documents
documents = [
    "How to install BoxLang",
    "BoxLang configuration options",
    "BoxLang debugging tips"
];

ids = [];
documents.each(function(doc) {
    embedding = getOpenAIEmbedding(doc);
    id = couchbaseVectorAdd(
        cacheName = "docs",
        text = doc,
        embedding = embedding,
        metadata = { category: "tutorial" }
    );
    ids.append(id);
});

println("Stored #ids.len()# documents");
```

### Knowledge Base Builder

```js
function addToKnowledgeBase(article) {
    // Split long article into chunks
    chunks = splitIntoChunks(article.content, 500);
    
    // Store each chunk
    chunkIds = [];
    chunks.each(function(chunk, index) {
        embedding = getOpenAIEmbedding(chunk);
        
        id = couchbaseVectorAdd(
            cacheName = "knowledge",
            text = chunk,
            embedding = embedding,
            metadata = {
                articleId: article.id,
                articleTitle: article.title,
                chunkIndex: index,
                totalChunks: chunks.len(),
                category: article.category
            }
        );
        
        chunkIds.append(id);
    });
    
    return chunkIds;
}

// Use it
article = {
    id: "article-123",
    title: "Getting Started with Couchbase",
    content: "...", // Long content
    category: "tutorial"
};

chunkIds = addToKnowledgeBase(article);
println("Stored article in #chunkIds.len()# chunks");
```

## Document Structure

The stored document contains:
```js
{
    "type": "vector_document",
    "text": "Document content",
    "embedding": [0.1, 0.2, ...], // Array of numbers
    "metadata": { ... }, // Custom metadata
    "userId": "user123", // Optional
    "conversationId": "conv456", // Optional
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-15T10:30:00Z"
}
```

## Notes

- **Embedding dimensions** - Must be consistent across all documents (e.g., 1536)
- **Text chunking** - For large documents, split into smaller chunks (500-1000 words)
- **ID format** - Auto-generated IDs are `vec_` + UUID
- **Timestamps** - `createdAt` and `updatedAt` are set automatically
- **Type field** - Always set to `"vector_document"` for vector search
- **Metadata** - Can contain any JSON-serializable data
- **Updates** - Use same ID to update existing document

## Best Practices

- 📏 **Chunk size** - Keep chunks 200-1000 words for best results
- 🔗 **Metadata linking** - Use metadata to link chunks back to source documents
- 🏷️ **Categorization** - Use metadata categories for filtered searches
- 👤 **User isolation** - Always set userId for user-specific data
- 💬 **Conversation tracking** - Use conversationId for chat history
- 🔄 **Batch processing** - Process multiple documents efficiently

## Related Functions

- [couchbaseVectorSearch](CouchbaseVectorSearch.md) - Search by similarity
- [couchbaseVectorGet](CouchbaseVectorGet.md) - Retrieve vector document
- [couchbaseVectorDelete](CouchbaseVectorDelete.md) - Delete vector document
- [couchbaseVectorList](CouchbaseVectorList.md) - List vector documents

## See Also

- [AI Memory Guide](../../aimemory.md)
- [API Usage Guide](../../api-usage.md)
