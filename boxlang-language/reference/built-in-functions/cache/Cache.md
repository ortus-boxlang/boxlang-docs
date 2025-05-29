[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Cache`

The entry BIF into the BoxCache.

This BIF will retrieve a named cache registered in our cache service.
 If you don't pass a cache name, it will default to the {@code default} cache.

 Once you have an instance to a cache, you can use the various methods to interact with the cache.
 Every cache must adhere to the {@link ICacheProvider} interface.

## Method Signature

```
Cache(cacheName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `string` | `false` | The cache name to retrieve the id from, defaults to {@code default} | `default` |

## Examples

### Adding a page to the cache

Puts HTML page into the cache and uses the cached version on subsequent calls to the page.


```java
<bx:cache action="optimal" directory="/path/to/directory" timespan="#createTimeSpan( 1, 0, 0, 0 )#" idletime="#createTimeSpan( 0, 12, 0, 0 )#">
	<div id="some-id">Hello World!</div>
</bx:cache>
```

Result: <div id="some-id">Hello World!</div>

### Flushing a page from the cache

Flushes the 'hello-world.bxm' page from the cache.


```java
<bx:cache action="flush" directory="/path/to/directory" expireURL="/hello-world.bxm"/>
```



## Related

  * [CacheNames](./CacheNames.md)
  * [CacheFilter](./CacheFilter.md)
  * [CacheService](./CacheService.md)
  * [CacheProviders](./CacheProviders.md)
