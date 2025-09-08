[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CacheGetAllIds`

Get all the keys in the cache.

If no cache name is provided, the default cache is used.
 If a filter is provided, only keys that match the filter will be returned.
 A filter is a simple string that can contain wildcards and will leverage the {@link WildcardFilter} to match keys.

## Method Signature

```
CacheGetAllIds(filter=[string], cacheName=[string], useRegex=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filter` | `string` | `false` | The filter to apply to the keys, this can be a simple Wildcard filter or a regex filter. The default is a simple wildcard filter. |  |
| `cacheName` | `string` | `false` | The name of the cache to get the keys from. Default is the default cache. | `default` |
| `useRegex` | `boolean` | `false` | If true, the filter will be treated as a full regular expression filter. Default is false. | `false` |

## Examples



## Related

  * [CacheClear](./CacheClear.md)
  * [CacheCount](./CacheCount.md)
  * [cacheDelete](./cacheDelete.md)
  * [CacheGet](./CacheGet.md)
  * [CacheGetAll](./CacheGetAll.md)
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
