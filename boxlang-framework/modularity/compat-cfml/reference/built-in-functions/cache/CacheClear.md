[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CacheClear`

Clear an id or an array of id's from the specified cache.

If no cache name is provided, the default cache is used.

## Method Signature

```
CacheClear(filterOrTags=[any], cacheName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filterOrTags` | `any` | `false` |  |  |
| `cacheName` | `string` | `false` | The name of the cache to get the keys from. Default is the default cache. | `default` |

## Examples



## Related

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
  * [CacheRemove](./CacheRemove.md)
  * [CacheRemoveAll](./CacheRemoveAll.md)
  * [CacheSetProperties](./CacheSetProperties.md)
