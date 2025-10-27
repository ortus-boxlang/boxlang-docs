[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `RedisGetClusterNodes`

Returns the cluster nodes information from a Redis cluster.

## Method Signature

```
RedisGetClusterNodes(cacheName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `any` | `true` | The name of the redis cache to get. |  |

## Examples

Get cluster node information:

```js
// Get the cluster nodes from a Redis cache
var nodes = RedisGetClusterNodes( "myRedisCache" );

// Iterate through nodes
for ( var node in nodes ) {
    println( "Node: " & node );
}
```

Monitor cluster topology:

```js
// Get cluster nodes for diagnostics
var nodes = RedisGetClusterNodes( "myRedisCache" );

// Check cluster health
if ( nodes.size() > 0 ) {
    println( "Cluster has " & nodes.size() & " nodes" );
}
```

## Related

- [RedisGetCluster()](./RedisGetCluster.md) - Get the Redis cluster instance
- [RedisGetProvider()](./RedisGetProvider.md) - Get the Redis cache provider
- [API Usage Guide](../../api-usage.md) - Redis API documentation
