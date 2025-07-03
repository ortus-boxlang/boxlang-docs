# cacheKeyExists

Lookup the id in the cache to see if it exists or not.

The id can be a single id or an array of IDs\
By default, the {@code cacheName} is set to {@code default}.\
You can also pass in a filter

## Method Signature

```
cacheKeyExists(id=[any], cacheName=[string])
```

### Arguments

| Argument    | Type     | Required | Description                                                         | Default   |
| ----------- | -------- | -------- | ------------------------------------------------------------------- | --------- |
| `id`        | `any`    | `true`   | The cache id to retrieve, or an array of ids to retrieve            |           |
| `cacheName` | `string` | `false`  | The cache name to retrieve the id from, defaults to {@code default} | `default` |

## Examples

## Related

* [CacheCount](CacheCount.md)
* [CacheGetAsAttempt](CacheGetAsAttempt.md)
* [CacheRegionRemove](CacheRegionRemove.md)
* [CacheRemoveAll](CacheRemoveAll.md)
* [CachePut](CachePut.md)
* [CacheRegionExists](CacheRegionExists.md)
* [CacheGetSession](CacheGetSession.md)
* [CacheGetEngineProperties](CacheGetEngineProperties.md)
* [CacheGet](CacheGet.md)
* [CacheGetDefaultCacheName](CacheGetDefaultCacheName.md)
* [CacheGetProperties](CacheGetProperties.md)
* [CacheSetProperties](CacheSetProperties.md)
* [CacheGetAllIds](CacheGetAllIds.md)
* [CacheIdExists](CacheIdExists.md)
* [CacheRemove](CacheRemove.md)
* [cacheDelete](cacheDelete.md)
* [CacheGetAll](CacheGetAll.md)
* [CacheGetMetadata](CacheGetMetadata.md)
* [CacheGetOrFail](CacheGetOrFail.md)
* [CacheClear](CacheClear.md)
* [CacheRegionNew](CacheRegionNew.md)
