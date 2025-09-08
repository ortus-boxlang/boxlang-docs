[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CacheGetAsAttempt`

Get an item from the cache and return it as a Java {@link Optional}.

By default, the {@code cacheName} is set to {@code default}.

## Method Signature

```
CacheGetAsAttempt(id=[string], cacheName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `id` | `string` | `true` | The cache id to retrieve |  |
| `cacheName` | `string` | `false` | The cache name to retrieve the id from, defaults to {@code default} | `default` |

## Examples



## Related

  * [CacheClear](./CacheClear.md)
  * [CacheCount](./CacheCount.md)
  * [cacheDelete](./cacheDelete.md)
  * [CacheGet](./CacheGet.md)
  * [CacheGetAll](./CacheGetAll.md)
  * [CacheGetAllIds](./CacheGetAllIds.md)
  * [CacheGetDefaultCacheName](./CacheGetDefaultCacheName.md)
  * [CacheGetEngineProperties](./CacheGetEngineProperties.md)
  * [CacheGetMetadata](./CacheGetMetadata.md)
  * [CacheGetOrFail](./CacheGetOrFail.md)
  * [CacheGetProperties](./CacheGetProperties.md)
  * [CacheGetSession](./CacheGetSession.md)
  * [CacheIdExists](./CacheIdExists.md)
  * [cacheKeyExists](./cacheKeyExists.md)
  * [CachePut](./CachePut.md)
  * [CacheRegionExists](./CacheRegionExists.md)
  * [CacheRegionNew](./CacheRegionNew.md)
  * [CacheRegionRemove](./CacheRegionRemove.md)
  * [CacheRemove](./CacheRemove.md)
  * [CacheRemoveAll](./CacheRemoveAll.md)
  * [CacheSetProperties](./CacheSetProperties.md)
