# Cache

The entry BIF into the BoxCache.

This BIF will retrieve a named cache registered in our cache service. If you don't pass a cache name, it will default to the ,{@code default}, cache.

Once you have an instance to a cache, you can use the various methods to interact with the cache. Every cache must adhere to the ,{@link ICacheProvider}, interface.

## Method Signature

```
Cache(cacheName=[string])
```

### Arguments

| Argument    | Type     | Required | Description                                                         | Default   |
| ----------- | -------- | -------- | ------------------------------------------------------------------- | --------- |
| `cacheName` | `string` | `false`  | The cache name to retrieve the id from, defaults to {@code default} | `default` |

## Examples

## Related

* [CacheFilter](cachefilter.md)
* [CacheNames](cachenames.md)
* [CacheProviders](cacheproviders.md)
* [CacheService](cacheservice.md)
