# couchbaseVectorList

List vector documents with optional filters for user, conversation, and metadata.

## Syntax

```js
couchbaseVectorList(
    cacheName,
    [userId],
    [conversationId],
    [metadata],
    [limit],
    [offset]
)
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | String | Yes | - | Name of the cache configuration |
| `userId` | String | No | - | Filter by user ID |
| `conversationId` | String | No | - | Filter by conversation ID |
| `metadata` | Struct | No | - | Filter by metadata fields |
| `limit` | Number | No | `100` | Maximum number of results |
| `offset` | Number | No | `0` | Number of results to skip (pagination) |

## Returns

Returns an array of vector document structs, ordered by `createdAt DESC`. Each struct contains:
- `id` - Document ID
- `type` - Document type (`"vector_document"`)
- `text` - Text content
- `embedding` - Vector embedding array
- `metadata` - Custom metadata
- `userId` - User ID (if set)
- `conversationId` - Conversation ID (if set)
- `createdAt` - Creation timestamp
- `updatedAt` - Last update timestamp

## Examples

### List All Documents

```js
// Get all vector documents (up to limit)
docs = couchbaseVectorList(cacheName = "default");

println("Found #docs.len()# documents");
docs.each(function(doc) {
    println("#doc.id#: #doc.text#");
});
```

### List by User

```js
// Get all documents for a specific user
userDocs = couchbaseVectorList(
    cacheName = "notes",
    userId = "user123"
);

println("User has #userDocs.len()# documents");
```

### List by Conversation

```js
// Get conversation history
messages = couchbaseVectorList(
    cacheName = "chat",
    conversationId = "conv456"
);

messages.each(function(msg) {
    println("[#msg.createdAt#] #msg.text#");
});
```

### Filter by Metadata

```js
// Get documents with specific metadata
docs = couchbaseVectorList(
    cacheName = "docs",
    metadata = {
        category: "tutorial",
        version: "2.0"
    }
);

println("Found #docs.len()# matching documents");
```

### Combined Filters

```js
// Combine user, conversation, and metadata filters
results = couchbaseVectorList(
    cacheName = "app",
    userId = "user123",
    conversationId = "conv456",
    metadata = {
        type: "note",
        important: true
    }
);
```

### Pagination

```js
// Get documents in pages
pageSize = 20;
page = 1;

docs = couchbaseVectorList(
    cacheName = "default",
    limit = pageSize,
    offset = (page - 1) * pageSize
);

println("Page #page#: #docs.len()# documents");

// Next page
page++;
nextDocs = couchbaseVectorList(
    cacheName = "default",
    limit = pageSize,
    offset = (page - 1) * pageSize
);
```

### List User's Recent Documents

```js
// Get user's recent documents
recentDocs = couchbaseVectorList(
    cacheName = "notes",
    userId = session.userId,
    limit = 10
);

println("Your recent notes:");
recentDocs.each(function(doc) {
    println("- #doc.text.left(50)#...");
});
```

### List by Category

```js
// Get all documents in a category
tutorials = couchbaseVectorList(
    cacheName = "docs",
    metadata = { category: "tutorial" }
);

guides = couchbaseVectorList(
    cacheName = "docs",
    metadata = { category: "guide" }
);

println("Tutorials: #tutorials.len()#");
println("Guides: #guides.len()#");
```

### Get Conversation Participants

```js
// Get all users in a conversation
messages = couchbaseVectorList(
    cacheName = "chat",
    conversationId = "conv789"
);

// Extract unique users
users = [];
messages.each(function(msg) {
    if (msg.userId && !users.contains(msg.userId)) {
        users.append(msg.userId);
    }
});

println("Conversation has #users.len()# participants");
```

### List with Statistics

```js
// Get documents and calculate stats
docs = couchbaseVectorList(cacheName = "vectors");

totalChars = 0;
categories = {};

docs.each(function(doc) {
    totalChars += doc.text.len();

    if (structKeyExists(doc.metadata, "category")) {
        cat = doc.metadata.category;
        if (!structKeyExists(categories, cat)) {
            categories[cat] = 0;
        }
        categories[cat]++;
    }
});

println("Total documents: #docs.len()#");
println("Average text length: #round(totalChars / docs.len())# chars");
println("Categories: #jsonSerialize(categories)#");
```

### Export User Data

```js
// Export all user's data
function exportUserData(userId) {
    docs = couchbaseVectorList(
        cacheName = "default",
        userId = userId
    );

    export = {
        userId: userId,
        exportDate: now(),
        documentCount: docs.len(),
        documents: docs
    };

    return jsonSerialize(export);
}

// Use it
userData = exportUserData("user123");
fileWrite("/exports/user123.json", userData);
```

### Cleanup Old Documents

```js
// List and delete old documents
function cleanupOldDocuments(cacheName, daysOld) {
    allDocs = couchbaseVectorList(cacheName = cacheName);
    cutoffDate = dateAdd("d", -daysOld, now());

    deletedCount = 0;
    allDocs.each(function(doc) {
        docDate = parseDateTime(doc.createdAt);
        if (docDate < cutoffDate) {
            if (couchbaseVectorDelete(cacheName, doc.id)) {
                deletedCount++;
            }
        }
    });

    return deletedCount;
}

// Use it
deleted = cleanupOldDocuments("temp", 30);
println("Deleted #deleted# documents older than 30 days");
```

### Build Document Index

```js
// Create searchable index of documents
docs = couchbaseVectorList(cacheName = "docs");

index = {};
docs.each(function(doc) {
    // Index by category
    if (structKeyExists(doc.metadata, "category")) {
        cat = doc.metadata.category;
        if (!structKeyExists(index, cat)) {
            index[cat] = [];
        }
        index[cat].append({
            id: doc.id,
            text: doc.text,
            createdAt: doc.createdAt
        });
    }
});

// Use the index
tutorialDocs = index["tutorial"];
println("Found #tutorialDocs.len()# tutorials");
```

## Notes

- **Default ordering** - Results are ordered by `createdAt DESC` (newest first)
- **Limit default** - Default limit is 100 documents
- **AND filters** - All specified filters must match (not OR)
- **Metadata matching** - All specified metadata fields must match exactly
- **Case sensitivity** - userId, conversationId, and metadata values are case-sensitive
- **Performance** - Use limit and offset for large result sets

## Pagination Pattern

```js
// Complete pagination example
function getPaginatedDocs(cacheName, page, pageSize) {
    offset = (page - 1) * pageSize;

    docs = couchbaseVectorList(
        cacheName = cacheName,
        limit = pageSize,
        offset = offset
    );

    return {
        page: page,
        pageSize: pageSize,
        count: docs.len(),
        hasMore: docs.len() == pageSize,
        documents: docs
    };
}

// Use it
result = getPaginatedDocs("default", page = 1, pageSize = 20);
println("Page #result.page#: #result.count# documents");
if (result.hasMore) {
    println("More results available");
}
```

## Use Cases

- 📝 **User dashboards** - Show user's documents
- 💬 **Conversation history** - Display chat messages
- 🗂️ **Category browsing** - List documents by category
- 🔍 **Content management** - Browse and manage documents
- 📊 **Analytics** - Analyze document metadata and patterns
- 🗑️ **Cleanup** - Find and delete old documents

## Related Functions

- [couchbaseVectorAdd](CouchbaseVectorAdd.md) - Store vector documents
- [couchbaseVectorGet](CouchbaseVectorGet.md) - Get specific document
- [couchbaseVectorDelete](CouchbaseVectorDelete.md) - Delete documents
- [couchbaseVectorSearch](CouchbaseVectorSearch.md) - Semantic search
- [couchbaseQuery](CouchbaseQuery.md) - Complex queries

## See Also

- [API Usage Guide](../../api-usage.md)
- [AI Memory Guide](../../aimemory.md)
