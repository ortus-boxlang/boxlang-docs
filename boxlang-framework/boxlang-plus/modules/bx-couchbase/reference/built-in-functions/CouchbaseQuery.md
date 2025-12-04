# couchbaseQuery

Execute raw N1QL/SQL++ queries with optional parameters.

## Syntax

```js
couchbaseQuery(cacheName, query, [parameters])
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cacheName` | String | Yes | Name of the cache configuration |
| `query` | String | Yes | N1QL/SQL++ query to execute |
| `parameters` | Struct | No | Named parameters for the query |

## Returns

Returns an array of result row structs. Each row contains the selected fields from the query.

## Examples

### Simple Query

```js
// Basic SELECT query
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE type = 'user' LIMIT 10"
);

println("Found #results.len()# users");
results.each(function(row) {
    println("User: #row.mybucket.name#");
});
```

### Parameterized Query

```js
// Use parameters to prevent injection
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE type = $type AND status = $status",
    parameters = {
        type: "order",
        status: "completed"
    }
);

println("Found #results.len()# completed orders");
```

### Count Query

```js
// Get document count
result = couchbaseQuery(
    cacheName = "default",
    query = "SELECT COUNT(*) as total FROM `mybucket` WHERE type = 'user'"
);

println("Total users: #result[1].total#");
```

### Aggregation Query

```js
// Calculate statistics
stats = couchbaseQuery(
    cacheName = "default",
    query = "SELECT 
        COUNT(*) as total,
        AVG(price) as avgPrice,
        SUM(quantity) as totalQty
    FROM `mybucket` 
    WHERE type = 'product'"
);

println("Products: #stats[1].total#");
println("Average price: $#numberFormat(stats[1].avgPrice, '0.00')#");
println("Total quantity: #stats[1].totalQty#");
```

### JOIN Query

```js
// Join multiple buckets
results = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT u.name, o.total, o.createdAt
        FROM `users` u
        JOIN `orders` o ON o.userId = u.id
        WHERE o.status = 'completed'
        ORDER BY o.createdAt DESC
        LIMIT 10
    "
);
```

### Group By Query

```js
// Group and aggregate
results = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT category, COUNT(*) as count
        FROM `products`
        WHERE type = 'product'
        GROUP BY category
        ORDER BY count DESC
    "
);

println("Products by category:");
results.each(function(row) {
    println("- #row.category#: #row.count#");
});
```

### Create Index

```js
// Create a primary index
couchbaseQuery(
    cacheName = "default",
    query = "CREATE PRIMARY INDEX ON `mybucket`"
);

// Create a secondary index
couchbaseQuery(
    cacheName = "default",
    query = "CREATE INDEX idx_type ON `mybucket`(type)"
);

// Create vector index
couchbaseQuery(
    cacheName = "default",
    query = "CREATE INDEX idx_embedding ON `mybucket`(embedding VECTOR) WHERE type = 'vector_document'"
);
```

### Update Documents

```js
// Bulk update with parameters
updated = couchbaseQuery(
    cacheName = "default",
    query = "
        UPDATE `mybucket`
        SET status = $newStatus, updatedAt = $now
        WHERE type = 'user' AND status = $oldStatus
    ",
    parameters = {
        newStatus: "active",
        oldStatus: "pending",
        now: now()
    }
);

println("Updated documents: #updated.len()#");
```

### Delete Documents

```js
// Bulk delete with conditions
deleted = couchbaseQuery(
    cacheName = "default",
    query = "
        DELETE FROM `mybucket`
        WHERE type = 'session' AND expiresAt < $now
    ",
    parameters = {
        now: now()
    }
);

println("Deleted expired sessions");
```

### Complex Search

```js
// Advanced search with multiple conditions
results = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT *
        FROM `mybucket`
        WHERE type = 'article'
        AND (
            LOWER(title) LIKE '%' || $keyword || '%'
            OR LOWER(content) LIKE '%' || $keyword || '%'
        )
        AND publishedAt BETWEEN $startDate AND $endDate
        AND status = 'published'
        ORDER BY publishedAt DESC
        LIMIT 20
    ",
    parameters = {
        keyword: lCase(searchTerm),
        startDate: dateAdd("m", -6, now()),
        endDate: now()
    }
);
```

### Array Contains Query

```js
// Search in arrays
results = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT *
        FROM `mybucket`
        WHERE type = 'user'
        AND ANY tag IN tags SATISFIES tag = $searchTag END
    ",
    parameters = {
        searchTag: "premium"
    }
);
```

### Subquery

```js
// Use subqueries
results = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT u.*
        FROM `users` u
        WHERE u.id IN (
            SELECT DISTINCT o.userId
            FROM `orders` o
            WHERE o.total > $minTotal
        )
    ",
    parameters = {
        minTotal: 1000
    }
);
```

### Vector Search Query

```js
// Manual vector search (or use couchbaseVectorSearch BIF)
embedding = getOpenAIEmbedding("search query");

results = couchbaseQuery(
    cacheName = "default",
    query = "
        SELECT id, text, metadata,
               SEARCH_SCORE() as score
        FROM `mybucket`
        WHERE type = 'vector_document'
        AND SEARCH(embedding, 
            {
                'knn': {
                    'vector': $embedding,
                    'k': $limit
                }
            }
        )
    ",
    parameters = {
        embedding: embedding,
        limit: 5
    }
);
```

### Check Index Status

```js
// Query system indexes
indexes = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM system:indexes WHERE keyspace_id = $bucket",
    parameters = {
        bucket: "mybucket"
    }
);

println("Indexes:");
indexes.each(function(idx) {
    println("- #idx.name# on #idx.keyspace_id# (#idx.state#)");
});
```

## Query Best Practices

### Always Use Parameters

```js
// ❌ DON'T: String concatenation (SQL injection risk!)
query = "SELECT * FROM `mybucket` WHERE id = '" & userInput & "'";

// ✅ DO: Use parameters
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE id = $id",
    parameters = { id: userInput }
);
```

### Escape Bucket Names

```js
// ✅ Always use backticks for bucket/scope/collection names
query = "SELECT * FROM `mybucket`.`_default`.`_default` WHERE ..."
```

### Use Indexes

```js
// Create appropriate indexes for your queries
couchbaseQuery(
    cacheName = "default",
    query = "CREATE INDEX idx_type_status ON `mybucket`(type, status)"
);

// Query uses the index
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE type = $type AND status = $status",
    parameters = { type: "user", status: "active" }
);
```

## Notes

- **N1QL syntax** - Uses Couchbase N1QL/SQL++ query language
- **Backticks required** - Always wrap bucket/scope/collection names in backticks
- **Parameters recommended** - Use parameters to prevent injection attacks
- **Index usage** - Create appropriate indexes for query performance
- **Collection path** - Full path: `` `bucket`.`scope`.`collection` ``
- **Case sensitivity** - Bucket/scope/collection names are case-sensitive

## Error Handling

```js
// Handle query errors
try {
    results = couchbaseQuery(
        cacheName = "default",
        query = "SELECT * FROM `mybucket` WHERE type = $type",
        parameters = { type: "user" }
    );
    
    println("Query returned #results.len()# rows");
} catch (any e) {
    if (findNoCase("syntax error", e.message)) {
        println("Query syntax error: #e.message#");
    } else if (findNoCase("index", e.message)) {
        println("Index issue: #e.message#");
    } else {
        println("Query error: #e.message#");
    }
}
```

## Related Functions

- [couchbaseVectorSearch](CouchbaseVectorSearch.md) - Simplified vector search
- [couchbaseVectorList](CouchbaseVectorList.md) - List vector documents
- [couchbaseGetCluster](CouchbaseGetCluster.md) - Direct cluster access

## See Also

- [N1QL Language Reference](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/index.html)
- [N1QL Query Guide](https://docs.couchbase.com/server/current/n1ql/query.html)
- [API Usage Guide](../../api-usage.md)
- [Troubleshooting](../../troubleshooting.md)
