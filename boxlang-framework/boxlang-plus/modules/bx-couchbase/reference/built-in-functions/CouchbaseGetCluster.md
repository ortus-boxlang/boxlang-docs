# couchbaseGetCluster

Get the Couchbase cluster connection for cluster-level operations.

## Syntax

```js
couchbaseGetCluster(cacheName)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cacheName` | String | Yes | Name of the cache configuration |

## Returns

Returns the Couchbase `Cluster` instance with access to:
- Bucket management
- Query execution
- Cluster analytics
- User management
- Search operations

## Examples

### Basic Usage

```js
// Get cluster connection
cluster = couchbaseGetCluster("default");

// Execute cluster-level query
result = cluster.query("SELECT COUNT(*) as total FROM `mybucket`");
```

### Bucket Management

```js
cluster = couchbaseGetCluster("default");
buckets = cluster.buckets();

// List all buckets
allBuckets = buckets.getAllBuckets();
allBuckets.each(function(bucket) {
    println("Bucket: #bucket.name()#, RAM: #bucket.ramQuota()# MB");
});
```

### Query Execution

```js
cluster = couchbaseGetCluster("default");

// Simple query
result = cluster.query(
    "SELECT * FROM `mybucket` WHERE type = 'user' LIMIT 10"
);

// Parameterized query
queryOptions = createObject("java", "com.couchbase.client.java.query.QueryOptions");
queryOptions.parameters(createObject("java", "com.couchbase.client.core.json.JsonObject")
    .put("type", "user")
    .put("status", "active")
);

result = cluster.query(
    "SELECT * FROM `mybucket` WHERE type = $type AND status = $status",
    queryOptions
);
```

### Analytics

```js
cluster = couchbaseGetCluster("default");

// Run analytics query
result = cluster.analyticsQuery(
    "SELECT AVG(responseTime) as avgTime FROM `mybucket` WHERE type = 'request'"
);
```

## Notes

- Cluster instance is shared and reused (singleton per cache configuration)
- Use for cluster-level operations that span multiple buckets
- For most operations, use higher-level functions like `couchbaseQuery()`
- Direct cluster access is useful for advanced operations not covered by BIFs

## Related Functions

- [couchbaseGetProvider](CouchbaseGetProvider.md) - Get provider instance
- [couchbaseGetBucket](CouchbaseGetBucket.md) - Get bucket instance
- [couchbaseQuery](CouchbaseQuery.md) - Execute N1QL queries

## See Also

- [API Usage Guide](../../api-usage.md)
- [Couchbase Cluster API](https://docs.couchbase.com/java-sdk/current/howtos/managing-connections.html)
