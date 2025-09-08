[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CacheGet`

Get an item from the cache.

If the item is not found, the default value will be returned if provided, else null will be returned.
 By default, the {@code cacheName} is set to {@code default}.

## Method Signature

```
CacheGet(id=[any], cacheName=[any], throwWhenNotExist=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `id` | `any` | `true` | The cache id to retrieve, or an array of ids to retrieve |  |
| `cacheName` | `any` | `false` | The cache name to retrieve the id from, defaults to {@code default} | `default` |
| `throwWhenNotExist` | `any` | `false` |  | `false` |

## Examples



## Related

  * [CacheClear](./CacheClear.md)
  * [CacheCount](./CacheCount.md)
  * [cacheDelete](./cacheDelete.md)
  * [CacheGetAll](./CacheGetAll.md)
  * [CacheGetAllIds](./CacheGetAllIds.md)
  * [CacheGetAsAttempt](./CacheGetAsAttempt.md)
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
