[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CacheGetOrFail`

Get an item from the cache, it will throw an exception if the id is not found in the cache.

By default, the {@code cacheName} is set to {@code default}.

## Method Signature

```
CacheGetOrFail(id=[string], cacheName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `id` | `string` | `true` | The cache id to retrieve |  |
| `cacheName` | `string` | `false` | The cache name to retrieve the id from, defaults to {@code default} | `default` |

## Examples



## Related

  * [CacheCount](./CacheCount.md)
  * [CacheGetAsAttempt](./CacheGetAsAttempt.md)
  * [CacheRegionRemove](./CacheRegionRemove.md)
  * [CacheRemoveAll](./CacheRemoveAll.md)
  * [CachePut](./CachePut.md)
  * [CacheRegionExists](./CacheRegionExists.md)
  * [CacheGetSession](./CacheGetSession.md)
  * [CacheGetEngineProperties](./CacheGetEngineProperties.md)
  * [CacheGet](./CacheGet.md)
  * [CacheGetDefaultCacheName](./CacheGetDefaultCacheName.md)
  * [CacheGetProperties](./CacheGetProperties.md)
  * [CacheSetProperties](./CacheSetProperties.md)
  * [CacheGetAllIds](./CacheGetAllIds.md)
  * [CacheIdExists](./CacheIdExists.md)
  * [cacheKeyExists](./cacheKeyExists.md)
  * [CacheRemove](./CacheRemove.md)
  * [cacheDelete](./cacheDelete.md)
  * [CacheGetAll](./CacheGetAll.md)
  * [CacheGetMetadata](./CacheGetMetadata.md)
  * [CacheClear](./CacheClear.md)
  * [CacheRegionNew](./CacheRegionNew.md)
