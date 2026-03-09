
# Component: `HTTP`

Makes an HTTP request with comprehensive control over request configuration and response handling.

## Component Signature

```
<bx:HTTP URL=[string]
port=[numeric]
httpVersion=[string]
timeout=[numeric]
connectionTimeout=[numeric]
redirect=[boolean]
resolveUrl=[boolean]
encodeUrl=[boolean]
method=[string]
userAgent=[string]
charset=[string]
compression=[string]
multipart=[boolean]
multipartType=[string]
result=[string]
getAsBinary=[string]
throwOnError=[boolean]
file=[string]
path=[string]
cachedWithin=[string]
username=[string]
password=[string]
clientCert=[string]
clientCertPassword=[string]
sse=[boolean]
onRequestStart=[function]
onChunk=[function]
onMessage=[function]
onError=[function]
onComplete=[function]
proxyServer=[string]
proxyPort=[any]
proxyUser=[string]
proxyPassword=[string]
name=[string]
delimiter=[string]
columns=[string]
firstRowAsHeaders=[boolean]
textQualifier=[string]
authType=[string]
domain=[string]
workstation=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` | The URL to which to make the HTTP request. Must start with http:// or https://. Required. |  |
| `port` | `numeric` | `false` | The port number to use for the connection. If not specified, uses the standard port for the protocol (80 for HTTP, 443 for HTTPS). |  |
| `httpVersion` | `string` | `false` | The HTTP protocol version to use. One of "HTTP/1.1" or "HTTP/2". Default is "HTTP/2". | `HTTP/2` |
| `timeout` | `numeric` | `false` | The request timeout in seconds. How long to wait for the server to respond. Default is 60 seconds. | `0` |
| `connectionTimeout` | `numeric` | `false` | The connection timeout in seconds. How long to wait when establishing the connection. Default is 30 seconds. | `15` |
| `redirect` | `boolean` | `false` | Whether to automatically follow HTTP redirects (3xx status codes). Default is true. | `true` |
| `resolveUrl` | `boolean` | `false` | Whether to resolve relative URLs before making the request. Default is false. | `false` |
| `encodeUrl` | `boolean` | `false` | Whether to URL-encode the query string parameters. Default is true. | `true` |
| `method` | `string` | `true` | The HTTP method to use. One of GET, POST, PUT, DELETE, HEAD, TRACE, OPTIONS, PATCH. Default is GET. Required. | `GET` |
| `userAgent` | `string` | `false` | The User-Agent header value to send with the request. Default is "BoxLang-HttpClient/1.0". | `BoxLang-HttpClient/1.0` |
| `charset` | `string` | `false` | The character encoding to use for the request and response. Default is "UTF-8". | `UTF-8` |
| `compression` | `string` | `false` | The compression type to accept for the response (e.g., "gzip", "deflate"). Optional. |  |
| `multipart` | `boolean` | `false` | Whether the request should be sent as multipart/form-data. Used for file uploads. Default is false. | `false` |
| `multipartType` | `string` | `true` | The type of multipart request. One of "form-data" or "related". Default is "form-data". Required when multipart is true. | `form-data` |
| `result` | `string` | `true` | The name of the variable in which to store the HTTP response struct. Default is "bxhttp". Required. | `bxhttp` |
| `getAsBinary` | `string` | `true` | Controls how binary responses are handled. One of "true", "false", "auto", "yes", "no", or "never". Default is "auto". "auto" detects based on content-type, "never" throws an error if binary is received. Required. | `auto` |
| `throwOnError` | `boolean` | `false` | Whether to throw an exception if the HTTP response status code is 400 or greater. Default is false. | `false` |
| `file` | `string` | `false` | The filename to use when saving the response to disk. Can be a full path if path attribute is not provided. Optional. |  |
| `path` | `string` | `false` | The directory path where the response file should be saved. If file attribute is not provided, attempts to extract filename from Content-Disposition header. Optional. |  |
| `cachedWithin` | `string` | `false` | If set, uses cached response if available within the specified duration (e.g., "10m" for 10 minutes, "1h" for 1 hour). Optional. (Note: Caching not yet implemented) |  |
| `username` | `string` | `false` | The username for HTTP Basic or NTLM authentication. Optional. |  |
| `password` | `string` | `false` | The password for HTTP Basic or NTLM authentication. Optional. |  |
| `clientCert` | `string` | `false` | The file path to the PKCS12 (.p12/.pfx) client certificate for SSL/TLS mutual authentication. Optional. |  |
| `clientCertPassword` | `string` | `false` | The password for the client certificate keystore. Optional. |  |
| `sse` | `boolean` | `false` |  | `false` |
| `onRequestStart` | `function` | `false` | A callback function called before the HTTP request is sent. Receives a struct with: request (HTTPRequest builder object), url (target URL), method (HTTP method), headers (struct of headers). Useful for logging, modifying<br>                           request, or performing pre-flight checks. Optional. |  |
| `onChunk` | `function` | `false` | A callback function for streaming/chunked response processing. Receives a struct with: chunk (data), chunkNumber (1-based), totalReceived (bytes), headers (first chunk only), result (HTTPResult struct). Optional. |  |
| `onMessage` | `function` | `false` |  |  |
| `onError` | `function` | `false` | A callback function to handle errors during the HTTP request. Receives a struct with: error (exception), message (error message), result (HTTPResult struct with partial data). Called for both streaming and non-streaming<br>                    requests. Optional. |  |
| `onComplete` | `function` | `false` | A callback function called when the HTTP request completes successfully. Receives a struct with: result (HTTPResult struct), statusCode, success (boolean). Called after all chunks in streaming mode. Optional. |  |
| `proxyServer` | `string` | `false` | The hostname or IP address of the proxy server. Required if using a proxy. |  |
| `proxyPort` | `any` | `false` | The port number of the proxy server. Required if using a proxy. |  |
| `proxyUser` | `string` | `false` | The username for proxy authentication. Required if proxyPassword is provided. |  |
| `proxyPassword` | `string` | `false` | The password for proxy authentication. Required if proxyUser is provided. |  |
| `name` | `string` | `false` |  |  |
| `delimiter` | `string` | `false` |  |  |
| `columns` | `string` | `false` |  |  |
| `firstRowAsHeaders` | `boolean` | `false` |  |  |
| `textQualifier` | `string` | `false` |  |  |
| `authType` | `string` | `true` | The authentication type to use. One of "BASIC" or "NTLM". Default is "BASIC". Required when username/password provided. | `BASIC` |
| `domain` | `string` | `false` |  |  |
| `workstation` | `string` | `false` |  |  |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJwtjEEOwiAQAM%2Fyis2e9GC5mjbcNH7AD1DcFhMQCotojH8XU08zh8mMz94yR%2FDENlwVnk8XBGN1ysQKC0%2F7A0JJTuEvy72UtdZuDmF21JngJUKiXFyLVyK8xWZcr1En7eGuPSlcEPgVm7QZwkO70txM3uEgPqKmG9Ox%2BLj972A3iC9hPzS%2B" target="_blank">Run Example</a>

```java
bx:http method="GET" charset="utf-8" url="https://www.google.com/" result="result" {
	bx:httpparam name="q" type="url" value="bx";
}
writeDump( result );

```


### Alternate Script Syntax




```java
httpService = new http( method="GET", charset="utf-8", url="https://www.google.com/" );
httpService.addParam( name="q", type="url", value="bx" );
result = httpService.send().getPrefix();
writeDump( result );

```


### BX:HTTP Tag Syntax




```java
<bx:http result="result" method="GET" charset="utf-8" url="https://www.google.com/">
    <bx:httpparam name="q" type="url" value="bx">
</bx:http>
<bx:dump var="#result#">
```


