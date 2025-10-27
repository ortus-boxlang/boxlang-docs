[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `RedisGetCluster`

Returns the Redis Cache Cluster provider by name.

## Method Signature

```
RedisGetCluster(cacheName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `any` | `true` | The name of the redis cache to get. |  |

## Examples

Get a Redis cluster instance for cache operations:

```js
// Get the cluster from a Redis cache
var cluster = RedisGetCluster( "myRedisCache" );

// Check if it's a cluster
if ( cluster != null ) {
    println( "Successfully retrieved Redis cluster" );
}
```

Access cluster information:

```js
// Get cluster and perform cluster-specific operations
var cluster = RedisGetCluster( "myRedisCache" );

// Get cluster info
var info = cluster.clusterInfo();
println( info );
```

## Related

- [RedisGetProvider()](./RedisGetProvider.md) - Get the Redis cache provider
- [RedisGetConnectionPool()](./RedisGetConnectionPool.md) - Get the connection pool
- [RedisGetClusterNodes()](./RedisGetClusterNodes.md) - Get cluster node information
- [API Usage Guide](../../api-usage.md) - Redis API documentation