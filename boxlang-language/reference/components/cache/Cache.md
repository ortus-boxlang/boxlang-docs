
# Component: `Cache`

Component which provides caching functionality, including content, individual entries, and HTTP headers

## Component Signature

```
<bx:Cache action=[string]
key=[string]
value=[any]
name=[any]
cacheName=[string]
metadata=[struct]
directory=[string]
timespan=[double]
idleTime=[double]
metadata=[struct]
stripWhitespace=[boolean]
throwOnError=[boolean]
useCache=[boolean]
expireURL=[string]
password=[string]
port=[integer]
protocol=[string]
region=[string]
useQueryString=[boolean]
username=[string]
dependsOn=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `false` | The cache action - "flush", "clientcache", "servercache", "optimal", "content", "put", "get" | `cache` |
| `key` | `string` | `false` | Cache key - optional for GET, DELETE functions and when body content is present. If not provided, a unique identifier of the body<br>                will provide the key |  |
| `value` | `any` | `false` | - mandatory value for put action |  |
| `name` | `any` | `false` | - a variable name for the result of the cache action. Required for GET action |  |
| `cacheName` | `string` | `false` | - optional cache name. If not provided the default cache will be used |  |
| `metadata` | `struct` | `false` | - any additional metadata to store with the cache object |  |
| `directory` | `string` | `false` | - Optional directory attribute which implements a file storage cache |  |
| `timespan` | `double` | `false` | - The duration to cache the object, defaults to either the cache default or unlimited until a server restart |  |
| `idleTime` | `double` | `false` | - The maximum idle time for an object to remain in the cache, defaults to the timeout |  |
| `metadata` | `struct` | `false` | - any additional metadata to store with the cache object |  |
| `stripWhitespace` | `boolean` | `false` |  | `false` |
| `throwOnError` | `boolean` | `false` |  | `false` |
| `useCache` | `boolean` | `false` |  | `true` |
| `expireURL` | `string` | `false` | - GLOB pattern or regex this string is found in the URL, the cache object will be invalidated. |  |
| `password` | `string` | `false` |  |  |
| `port` | `integer` | `false` | - Legacy CFML attributes. Not implemented |  |
| `protocol` | `string` | `false` | - Legacy CFML attribute. Not implemented |  |
| `region` | `string` | `false` |  |  |
| `useQueryString` | `boolean` | `false` |  | `false` |
| `username` | `string` | `false` |  |  |
| `dependsOn` | `string` | `false` |  |  |

## Examples

### Cache body content

Caches the output of the component body for the specified duration.

```java
<bx:cache action="cache" key="homepage" timespan="1/24">
    <h1>Welcome to our site</h1>
    <p>This content is cached for 1 hour.</p>
</bx:cache>

```

### Get a cached value

Retrieves a cached value and stores it in a variable.

```java
<bx:cache action="get" key="userCount" name="count">
<bx:dump var="#count#">

```

### Put a value into the cache

```java
<bx:cache action="put" key="config" value="#settings#">

```

### Put body content into the cache

```java
<bx:cache action="put" key="report">
    <table>
        <tr><td>Generated at: #now()#</td></tr>
    </table>
</bx:cache>

```

### Delete a cache entry

```java
<bx:cache action="delete" key="userCount">

```

### Flush all cache entries

```java
<bx:cache action="flush">

```

### Flush a specific cache key

```java
<bx:cache action="flush" key="homepage">

```

### Use a named cache region

```java
<bx:cache action="cache" key="productList" cacheName="products" timespan="1">
    #productService.getAll()#
</bx:cache>

```

### Cache with idle timeout

```java
<bx:cache action="cache" key="sessionData" timespan="1" idleTime="0.5">
    #expensiveOperation()#
</bx:cache>

```

### Disable caching temporarily

```java
<bx:cache action="cache" key="data" useCache="false">
    #alwaysFreshData()#
</bx:cache>

```
