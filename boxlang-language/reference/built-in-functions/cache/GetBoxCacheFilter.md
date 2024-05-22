[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetBoxCacheFilter`

This method creates a cache filter that can be used to operate on a cache instance and its keys.

## Method Signature
```
GetBoxCacheFilter(filter=[string], useRegex=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filter` | `string` | `true` | The string pattern to match against. |  |
| `useRegex` | `boolean` | `false` | Use the regex filter instead of the wildcard filter. | `false` |

## Examples

```
GetBoxCacheFilter(filter=[string], useRegex=[boolean])
```

## Related
  * [GetBoxCache](./GetBoxCache.md)
  * [GetBoxCacheNames](./GetBoxCacheNames.md)
  * [GetBoxCacheProviders](./GetBoxCacheProviders.md)
