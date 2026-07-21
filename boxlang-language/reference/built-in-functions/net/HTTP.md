[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `HTTP`

Returns a fluent HTTP client for making HTTP requests.

This BIF creates a new or retrieves an existing BoxHttpClient instance based on the provided
 connection parameters. The client can be used to fluently build and execute HTTP requests
 with support for various HTTP versions, redirects, timeouts, proxy configuration, and client certificates.

 Example usage:

 <pre>
 // Simple GET request
 http( "https://api.example.com/data" )
     .invoke()
     .ifSuccess( result -> {
 		// Handle successful response
 	} )
     .ifError( error -> {
 		// Handle error response
 	} )

 // Invoke and get the result immediately, throwing an exception on error
 result = http( "https://api.example.com/data" )
 	.invokeAndGet().
 </pre>

## Method Signature

```
HTTP(URL=[string], connectionTimeout=[numeric], redirect=[boolean], httpVersion=[string], proxyServer=[string], proxyPort=[integer], proxyUser=[string], proxyPassword=[string], clientCert=[string], clientCertPassword=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` |  |  |
| `connectionTimeout` | `numeric` | `false` | The connection timeout in milliseconds (default: BoxHttpClient.DEFAULT_CONNECTION_TIMEOUT) | `15` |
| `redirect` | `boolean` | `false` | Whether to automatically follow HTTP redirects (default: true) | `true` |
| `httpVersion` | `string` | `false` | The HTTP version to use (default: HTTP/2) | `HTTP/2` |
| `proxyServer` | `string` | `false` | The proxy server address (requires proxyPort) |  |
| `proxyPort` | `integer` | `false` | The proxy server port (requires proxyServer) |  |
| `proxyUser` | `string` | `false` | The proxy authentication username (requires proxyPassword) |  |
| `proxyPassword` | `string` | `false` | The proxy authentication password (requires proxyUser) |  |
| `clientCert` | `string` | `false` | The path to the client certificate file |  |
| `clientCertPassword` | `string` | `false` | The password for the client certificate |  |

## Examples

### Make an HTTP request

```java
result = http( method: "GET", url: "https://httpbin.org/get" );
writeOutput( result.statusCode );

```

Result: 200

### POST with body

```java
result = http( method: "POST", url: "https://httpbin.org/post", body: "hello" );
writeOutput( result.statusCode );

```

Result: 200

## Related

  * [GetLocalhostIp](./GetLocalhostIp.md)
  * [SOAP](./SOAP.md)
