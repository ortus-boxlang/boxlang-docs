[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `RedisGetConnectionPool`

Returns the Redis connection pool for a given cache.

## Method Signature

```
RedisGetConnectionPool(cacheName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `any` | `true` | The name of the redis cache to get. |  |

## Examples

Get the connection pool from a Redis cache:

```js
// Retrieve the connection pool for a cache
var pool = RedisGetConnectionPool( "myRedisCache" );

// Check if pool is available
if ( pool != null ) {
    println( "Successfully retrieved Redis connection pool" );
}
```

Access pool metrics:

```js
// Get connection pool for monitoring
var pool = RedisGetConnectionPool( "myRedisCache" );

// Access pool statistics
var poolStats = pool.getPoolStats();
println( "Active connections: " & poolStats.activeConnections );
println( "Idle connections: " & poolStats.idleConnections );
```

## Related

- [RedisGetCluster()](./RedisGetCluster.md) - Get the Redis cluster instance
- [RedisGetProvider()](./RedisGetProvider.md) - Get the Redis cache provider
- [RedisGetClusterNodes()](./RedisGetClusterNodes.md) - Get cluster node information
- [API Usage Guide](../../api-usage.md) - Redis API documentation
