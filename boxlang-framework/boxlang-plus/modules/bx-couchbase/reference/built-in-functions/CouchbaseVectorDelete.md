# couchbaseVectorDelete

Delete a vector document by its ID.

## Syntax

```js
couchbaseVectorDelete(cacheName, id)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cacheName` | String | Yes | Name of the cache configuration |
| `id` | String | Yes | Document ID to delete |

## Returns

Returns a boolean:
- `true` - Document was successfully deleted
- `false` - Document was not found (nothing to delete)

## Examples

### Basic Deletion

```js
// Delete a vector document
deleted = couchbaseVectorDelete(
    cacheName = "default",
    id = "vec_12345"
);

if (deleted) {
    println("Document deleted");
} else {
    println("Document not found");
}
```

### Delete with Confirmation

```js
// Check before deleting
doc = couchbaseVectorGet("default", "vec_789");

if (!doc.isEmpty()) {
    deleted = couchbaseVectorDelete("default", "vec_789");
    if (deleted) {
        println("Deleted: #doc.text#");
    }
} else {
    println("Document doesn't exist");
}
```

### Delete User Document

```js
// Only delete if owned by user
doc = couchbaseVectorGet("notes", "note_456");

if (!doc.isEmpty() && doc.userId == session.userId) {
    deleted = couchbaseVectorDelete("notes", "note_456");
    if (deleted) {
        println("Your note has been deleted");
    }
} else {
    println("Cannot delete: not found or access denied");
}
```

### Cleanup Old Documents

```js
// Delete documents older than 30 days
oldDocs = couchbaseVectorList(
    cacheName = "temp",
    metadata = {
        createdBefore: dateAdd("d", -30, now())
    }
);

deleteCount = 0;
oldDocs.each(function(doc) {
    if (couchbaseVectorDelete("temp", doc.id)) {
        deleteCount++;
    }
});

println("Deleted #deleteCount# old documents");
```

### Batch Deletion

```js
// Delete multiple documents
ids = ["vec_1", "vec_2", "vec_3", "vec_4"];
deletedCount = 0;

ids.each(function(id) {
    if (couchbaseVectorDelete("default", id)) {
        deletedCount++;
    }
});

println("Deleted #deletedCount# of #ids.len()# documents");
```

### Delete Conversation History

```js
// Delete all messages in a conversation
messages = couchbaseVectorList(
    cacheName = "chat",
    conversationId = "conv_123"
);

messages.each(function(msg) {
    couchbaseVectorDelete("chat", msg.id);
});

println("Deleted conversation history (#messages.len()# messages)");
```

### Safe Deletion with Retry

```js
// Retry deletion if fails
function safeDelete(cacheName, id, maxRetries = 3) {
    for (var i = 1; i <= maxRetries; i++) {
        try {
            if (couchbaseVectorDelete(cacheName, id)) {
                return true;
            }
        } catch (any e) {
            if (i == maxRetries) {
                throw e;
            }
            sleep(100 * i); // Exponential backoff
        }
    }
    return false;
}

// Use it
if (safeDelete("default", "vec_999")) {
    println("Document deleted successfully");
}
```

### Delete with Audit Log

```js
// Log deletions for audit
function deleteWithAudit(cacheName, id, userId) {
    // Get document first
    doc = couchbaseVectorGet(cacheName, id);
    
    if (!doc.isEmpty()) {
        // Delete it
        deleted = couchbaseVectorDelete(cacheName, id);
        
        if (deleted) {
            // Log the deletion
            couchbaseVectorAdd(
                cacheName = "audit",
                text = "Deleted: #doc.text#",
                embedding = doc.embedding,
                metadata = {
                    action: "delete",
                    deletedBy: userId,
                    deletedAt: now(),
                    originalId: id,
                    originalMetadata: doc.metadata
                }
            );
            return true;
        }
    }
    
    return false;
}

// Use it
deleteWithAudit("docs", "doc_456", session.userId);
```

### Delete Article Chunks

```js
// Delete all chunks of an article
function deleteArticle(articleId) {
    // Find all chunks
    chunks = couchbaseVectorList(
        cacheName = "knowledge",
        metadata = {
            articleId: articleId
        }
    );
    
    // Delete each chunk
    deletedCount = 0;
    chunks.each(function(chunk) {
        if (couchbaseVectorDelete("knowledge", chunk.id)) {
            deletedCount++;
        }
    });
    
    return deletedCount;
}

// Use it
deleted = deleteArticle("article-123");
println("Deleted #deleted# chunks");
```

## Notes

- **Returns boolean** - `true` if deleted, `false` if not found
- **No error on missing** - Gracefully handles non-existent documents
- **Immediate effect** - Document is deleted immediately (no undo)
- **Case sensitive** - Document IDs are case-sensitive
- **No cascade** - Does not delete related documents automatically

## Error Handling

```js
// Handle deletion errors
try {
    deleted = couchbaseVectorDelete("default", documentId);
    
    if (deleted) {
        println("Document deleted");
    } else {
        println("Document not found (already deleted?)");
    }
} catch (any e) {
    // Connection error or other issue
    println("Error deleting document: #e.message#");
}
```

## Best Practices

- ✅ **Check existence** - Use `couchbaseVectorGet()` first if you need the data
- ✅ **Verify ownership** - Check userId before deleting user documents
- ✅ **Batch operations** - Delete multiple documents efficiently in loops
- ✅ **Audit trail** - Log important deletions for compliance
- ✅ **Error handling** - Always wrap in try/catch for production code
- ⚠️ **No undo** - Deletion is permanent, consider soft-delete flags instead

## Soft Delete Alternative

```js
// Instead of deleting, mark as deleted
doc = couchbaseVectorGet("default", "doc_123");

if (!doc.isEmpty()) {
    // Update metadata to mark as deleted
    doc.metadata.deleted = true;
    doc.metadata.deletedAt = now();
    doc.metadata.deletedBy = session.userId;
    
    // Store updated document
    couchbaseVectorAdd(
        cacheName = "default",
        text = doc.text,
        embedding = doc.embedding,
        metadata = doc.metadata,
        id = doc.id
    );
    
    println("Document marked as deleted");
}
```

## Related Functions

- [couchbaseVectorAdd](CouchbaseVectorAdd.md) - Store vector document
- [couchbaseVectorGet](CouchbaseVectorGet.md) - Retrieve vector document
- [couchbaseVectorList](CouchbaseVectorList.md) - List vector documents
- [couchbaseQuery](CouchbaseQuery.md) - Delete with complex queries

## See Also

- [API Usage Guide](../../api-usage.md)
- [AI Memory Guide](../../aimemory.md)
