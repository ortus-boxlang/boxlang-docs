[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetLocalhostIp`

Returns the localhost IP address (string), or all local IP addresses (array) if the 'all' argument is set to true.

The lookup for ALL IP addresses is cached by default, but can be forced to refresh with the 'refresh' argument.
 The 'refresh' argument will clear the cache and perform a new lookup, when called with 'all' set to true.

## Method Signature

```
GetLocalhostIp(all=[boolean], refresh=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `all` | `boolean` | `false` | (optional, boolean) If true, returns an array of all local IP addresses. Default is false (returns only the primary local IP). | `false` |
| `refresh` | `boolean` | `false` | (optional, boolean) If true, forces a refresh of the local IP address cache. Default is false (uses cached value if available). | `false` |

## Examples

### Get the localhost IP address

```java
ip = getLocalhostIp();
writeOutput( isString( ip ) );

```

Result: true

## Related

  * [HTTP](./HTTP.md)
  * [SOAP](./SOAP.md)
