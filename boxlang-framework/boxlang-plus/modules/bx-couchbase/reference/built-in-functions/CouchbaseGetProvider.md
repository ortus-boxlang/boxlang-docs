# couchbaseGetProvider

Get the Couchbase cache provider instance for direct access to provider methods.

## Syntax

```js
couchbaseGetProvider(cacheName)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cacheName` | String | Yes | Name of the cache configuration |

## Returns

Returns the `CouchbaseCache` provider instance with access to:
- Cache statistics and metadata
- Connection management
- Provider-specific methods

## Examples

### Basic Usage

```js
// Get provider instance
provider = couchbaseGetProvider("default");

// Access provider information
println("Provider name: #provider.getName()#");
println("Provider type: #provider.getType()#");
```

### Get Cache Statistics

```js
provider = couchbaseGetProvider("default");
stats = provider.getStatistics();

println("Cache hits: #stats.hits#");
println("Cache misses: #stats.misses#");
println("Hit rate: #stats.hitRate#%");
```

### Multiple Cache Configurations

```js
// Different caches for different purposes
sessionProvider = couchbaseGetProvider("sessions");
appProvider = couchbaseGetProvider("application");
vectorProvider = couchbaseGetProvider("vectors");

// Use them independently
sessionStats = sessionProvider.getStatistics();
appStats = appProvider.getStatistics();
vectorStats = vectorProvider.getStatistics();
```

## Notes

- The cache name must exist in your cache configuration
- Throws an error if the cache is not configured or not a Couchbase provider
- Provider instance is shared across requests (singleton)
- Useful for accessing provider-specific functionality not available through standard cache functions

## Related Functions

- [couchbaseGetCluster](CouchbaseGetCluster.md) - Get cluster connection
- [couchbaseGetBucket](CouchbaseGetBucket.md) - Get bucket instance
- [couchbaseGetCollection](CouchbaseGetCollection.md) - Get collection instance

## See Also

- [API Usage Guide](../../api-usage.md)
- [Code Usage Patterns](../../code-usage.md)
