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

  * [CacheCount](./CacheCount.md)
  * [CacheGetAsAttempt](./CacheGetAsAttempt.md)
  * [CacheRegionRemove](./CacheRegionRemove.md)
  * [CacheRemoveAll](./CacheRemoveAll.md)
  * [CachePut](./CachePut.md)
  * [CacheRegionExists](./CacheRegionExists.md)
  * [CacheGetSession](./CacheGetSession.md)
  * [CacheGetEngineProperties](./CacheGetEngineProperties.md)
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
  * [CacheGetOrFail](./CacheGetOrFail.md)
  * [CacheClear](./CacheClear.md)
  * [CacheRegionNew](./CacheRegionNew.md)
