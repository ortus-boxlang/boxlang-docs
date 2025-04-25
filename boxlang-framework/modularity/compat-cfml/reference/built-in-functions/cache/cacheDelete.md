[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `cacheDelete`

Deletes a single element from the cache.

## Method Signature

```
cacheDelete(id=[any], throwOnError=[boolean], cacheName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `id` | `any` | `true` | A single ID or an array of IDs to remove from the cache. |  |
| `throwOnError` | `boolean` | `false` | If true, throw an exception if the key is not found. Default is false. | `false` |
| `cacheName` | `string` | `false` | The name of the cache to get the keys from. Default is the default cache. | `default` |

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
  * [CacheGetAll](./CacheGetAll.md)
  * [CacheGetMetadata](./CacheGetMetadata.md)
  * [CacheGetOrFail](./CacheGetOrFail.md)
  * [CacheClear](./CacheClear.md)
  * [CacheRegionNew](./CacheRegionNew.md)
