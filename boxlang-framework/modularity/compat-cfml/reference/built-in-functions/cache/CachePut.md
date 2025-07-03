# CachePut

Get an item from the cache.

If the item is not found, the default value will be returned if provided, else null will be returned.\
By default, the {@code cacheName} is set to {@code default}.

## Method Signature

```
CachePut(id=[any], value=[any], timespan=[any], idleTime=[any], cacheName=[string])
```

### Arguments

| Argument    | Type     | Required | Description                                                         | Default   |
| ----------- | -------- | -------- | ------------------------------------------------------------------- | --------- |
| `id`        | `any`    | `true`   | The cache id to store                                               |           |
| `value`     | `any`    | `true`   | The value to store in the cache                                     |           |
| `timespan`  | `any`    | `false`  | The duration for the cache to expire in seconds                     |           |
| `idleTime`  | `any`    | `false`  | The duration for the cache to expire after last access in seconds   |           |
| `cacheName` | `string` | `false`  | The cache name to retrieve the id from, defaults to {@code default} | `default` |

## Examples

## Related

* [CacheCount](CacheCount.md)
* [CacheGetAsAttempt](CacheGetAsAttempt.md)
* [CacheRegionRemove](CacheRegionRemove.md)
* [CacheRemoveAll](CacheRemoveAll.md)
* [CacheRegionExists](CacheRegionExists.md)
* [CacheGetSession](CacheGetSession.md)
* [CacheGetEngineProperties](CacheGetEngineProperties.md)
* [CacheGet](CacheGet.md)
* [CacheGetDefaultCacheName](CacheGetDefaultCacheName.md)
* [CacheGetProperties](CacheGetProperties.md)
* [CacheSetProperties](CacheSetProperties.md)
* [CacheGetAllIds](CacheGetAllIds.md)
* [CacheIdExists](CacheIdExists.md)
* [cacheKeyExists](cacheKeyExists.md)
* [CacheRemove](CacheRemove.md)
* [cacheDelete](cacheDelete.md)
* [CacheGetAll](CacheGetAll.md)
* [CacheGetMetadata](CacheGetMetadata.md)
* [CacheGetOrFail](CacheGetOrFail.md)
* [CacheClear](CacheClear.md)
* [CacheRegionNew](CacheRegionNew.md)
