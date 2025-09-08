[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CacheRemove`

Deletes a single element from the cache.

## Method Signature

```
CacheRemove(id=[any], throwOnError=[boolean], cacheName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `id` | `any` | `true` | A single ID or an array of IDs to remove from the cache. |  |
| `throwOnError` | `boolean` | `false` | If true, throw an exception if the key is not found. Default is false. | `false` |
| `cacheName` | `string` | `false` | The name of the cache to get the keys from. Default is the default cache. | `default` |

## Examples



## Related

  * [CacheClear](./CacheClear.md)
  * [CacheCount](./CacheCount.md)
  * [cacheDelete](./cacheDelete.md)
  * [CacheGet](./CacheGet.md)
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
  * [CacheRemoveAll](./CacheRemoveAll.md)
  * [CacheSetProperties](./CacheSetProperties.md)
