# CacheGetAllIds

Get all the keys in the cache.

If no cache name is provided, the default cache is used.\
If a filter is provided, only keys that match the filter will be returned.\
A filter is a simple string that can contain wildcards and will leverage the {@link WildcardFilter} to match keys.

## Method Signature

```
CacheGetAllIds(filter=[string], cacheName=[string], useRegex=[boolean])
```

### Arguments

| Argument    | Type      | Required | Description                                                                                                                       | Default   |
| ----------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `filter`    | `string`  | `false`  | The filter to apply to the keys, this can be a simple Wildcard filter or a regex filter. The default is a simple wildcard filter. |           |
| `cacheName` | `string`  | `false`  | The name of the cache to get the keys from. Default is the default cache.                                                         | `default` |
| `useRegex`  | `boolean` | `false`  | If true, the filter will be treated as a full regular expression filter. Default is false.                                        | `false`   |

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
* [CacheIdExists](CacheIdExists.md)
* [cacheKeyExists](cacheKeyExists.md)
* [CacheRemove](CacheRemove.md)
* [cacheDelete](cacheDelete.md)
* [CacheGetAll](CacheGetAll.md)
* [CacheGetMetadata](CacheGetMetadata.md)
* [CacheGetOrFail](CacheGetOrFail.md)
* [CacheClear](CacheClear.md)
* [CacheRegionNew](CacheRegionNew.md)
