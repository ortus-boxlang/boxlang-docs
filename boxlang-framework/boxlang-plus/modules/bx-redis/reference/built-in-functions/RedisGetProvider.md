[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `RedisGetProvider`

Returns the Redis Cache Provider by name.

## Method Signature

```
RedisGetProvider(cacheName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `any` | `true` | The name of the redis cache to get. |  |

## Examples

Get a Redis cache provider by name:

```js
// Retrieve the provider for a named Redis cache
var provider = RedisGetProvider( "myRedisCache" );

// Check if provider is available
if ( provider != null ) {
    println( "Successfully retrieved Redis provider" );
}
```

Use provider to access cache features:

```js
// Get the provider
var provider = RedisGetProvider( "myRedisCache" );

// Access provider capabilities
var cacheConfig = provider.getCacheConfig();
println( "Provider type: " & cacheConfig.type );
println( "Host: " & cacheConfig.host );
println( "Port: " & cacheConfig.port );
```

## Related

- [RedisGetCluster()](./RedisGetCluster.md) - Get the Redis cluster instance
- [RedisGetConnectionPool()](./RedisGetConnectionPool.md) - Get the connection pool
- [RedisGetClusterNodes()](./RedisGetClusterNodes.md) - Get cluster node information
- [API Usage Guide](../../api-usage.md) - Redis API documentation
