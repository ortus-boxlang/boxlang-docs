# couchbaseGetCollection

Get a Couchbase collection instance for document operations.

## Syntax

```js
couchbaseGetCollection(cacheName, [scopeName], [collectionName])
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | String | Yes | - | Name of the cache configuration |
| `scopeName` | String | No | `_default` | Name of the scope within the bucket |
| `collectionName` | String | No | `_default` | Name of the collection within the scope |

## Returns

Returns the Couchbase `Collection` instance with access to:
- Document CRUD operations (get, insert, upsert, replace, remove)
- Binary operations
- Subdocument operations
- Query execution
- Full-text search

## Examples

### Get Default Collection

```js
// Get default collection (most common)
collection = couchbaseGetCollection("default");

// Perform document operations
collection.upsert("user:123", { name: "John", email: "john@example.com" });
doc = collection.get("user:123");
```

### Get Custom Collection

```js
// Get specific collection
usersCollection = couchbaseGetCollection("default", "myapp", "users");

// Insert user document
usersCollection.insert("user:456", {
    name: "Jane Doe",
    email: "jane@example.com",
    role: "admin"
});
```

### Multiple Collections

```js
// Different collections for different data types
usersCol = couchbaseGetCollection("default", "myapp", "users");
ordersCol = couchbaseGetCollection("default", "myapp", "orders");
productsCol = couchbaseGetCollection("default", "myapp", "products");

// Operate on each independently
usersCol.upsert("user:1", { name: "John" });
ordersCol.upsert("order:1", { userId: "user:1", total: 99.99 });
productsCol.upsert("product:1", { name: "Widget", price: 9.99 });
```

### Document Operations

```js
collection = couchbaseGetCollection("default");

// Insert (fails if exists)
collection.insert("doc:1", { data: "new" });

// Upsert (insert or update)
collection.upsert("doc:2", { data: "updated" });

// Replace (fails if not exists)
collection.replace("doc:1", { data: "replaced" });

// Remove
collection.remove("doc:1");

// Get
result = collection.get("doc:2");
content = result.contentAsObject();
```

### Subdocument Operations

```js
collection = couchbaseGetCollection("default");

// Get specific field
result = collection.lookupIn("user:123")
    .get("email")
    .execute();
email = result.contentAs(0, "java.lang.String");

// Update specific field
collection.mutateIn("user:123")
    .upsert("lastLogin", now())
    .execute();
```

### Binary Operations

```js
collection = couchbaseGetCollection("default");

// Store binary data
collection.upsert("image:123", toBinary(imageData));

// Get binary data
result = collection.get("image:123");
binary = result.contentAs("byte[]");
```

## Notes

- Default collection is `_default` in `_default` scope
- Collections provide document-level organization within scopes
- Collection names are case-sensitive
- Collection must exist in Couchbase or operation will fail
- Most cache operations use the default collection automatically
- Direct collection access is for advanced scenarios

## Collection Benefits

- **Document type isolation** - Separate users, orders, products, etc.
- **Schema flexibility** - Different document structures per collection
- **Index optimization** - Create indexes specific to collection
- **Access control** - Grant permissions per collection
- **Query performance** - Queries run faster on smaller collections

## Related Functions

- [couchbaseGetBucket](CouchbaseGetBucket.md) - Get bucket instance
- [couchbaseGetScope](CouchbaseGetScope.md) - Get scope instance
- [couchbaseQuery](CouchbaseQuery.md) - Execute queries

## See Also

- [API Usage Guide](../../api-usage.md)
- [Couchbase Collections](https://docs.couchbase.com/server/current/learn/data/scopes-and-collections.html)
- [Document Operations](https://docs.couchbase.com/java-sdk/current/howtos/kv-operations.html)
