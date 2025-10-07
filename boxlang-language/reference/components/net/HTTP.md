
# Component: `HTTP`

I make an HTTP call using tons of attributes to control the request.

## Component Signature

```
<bx:HTTP URL=[string]
port=[numeric]
method=[string]
username=[string]
password=[string]
userAgent=[string]
charset=[string]
resolveUrl=[boolean]
throwOnError=[boolean]
redirect=[boolean]
timeout=[numeric]
getAsBinary=[string]
result=[string]
file=[string]
multipart=[boolean]
multipartType=[string]
clientCertPassword=[string]
path=[string]
clientCert=[string]
compression=[string]
authType=[string]
cachedWithin=[string]
encodeUrl=[boolean]
proxyServer=[string]
proxyPort=[integer]
proxyUser=[string]
proxyPassword=[string]
name=[string]
delimiter=[string]
columns=[string]
firstRowAsHeaders=[boolean]
textQualifier=[string]
domain=[string]
workstation=[string]
httpVersion=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` | The URL to which to make the HTTP request. Must start with http:// or https:// |  |
| `port` | `numeric` | `false` | The port to which to make the HTTP request. Defaults to the standard port for the protocol (80 for http, 443 for https) |  |
| `method` | `string` | `true` | The HTTP method to use. One of GET, POST, PUT, DELETE, HEAD, TRACE, OPTIONS, PATCH. Default is GET. | `GET` |
| `username` | `string` | `false` | The username to use for authentication, if any. |  |
| `password` | `string` | `false` | The password to use for authentication, if any. |  |
| `userAgent` | `string` | `false` | The User-Agent string to send with the request. Default is "BoxLang". | `BoxLang` |
| `charset` | `string` | `false` | The character set to use for the request. Default is UTF-8. | `UTF-8` |
| `resolveUrl` | `boolean` | `false` | Whether to resolve the URL before making the request. Default is false. | `false` |
| `throwOnError` | `boolean` | `false` | Whether to throw an error if the HTTP response status code is 400 or greater. Default is true. | `true` |
| `redirect` | `boolean` | `false` | Whether to follow redirects. Default is true. | `true` |
| `timeout` | `numeric` | `false` | The timeout for the request, in seconds. Default is no timeout. |  |
| `getAsBinary` | `string` | `true` | Whether to return the response body as binary. One of true, false, auto, yes, no, never. Default is auto. | `auto` |
| `result` | `string` | `true` | The name of the variable in which to store the result Struct. Default is "bxhttp". | `bxhttp` |
| `file` | `string` | `false` | The name of the file in which to store the response body. If not set, the response body is stored in the result Struct. If not provided with a `path`, the file attribute can be a full path to the file to write. |  |
| `multipart` | `boolean` | `false` | Whether the request is a multipart request. Default is false. | `false` |
| `multipartType` | `string` | `true` | The type of multipart request. One of form-data, related. Default is form-data. | `form-data` |
| `clientCertPassword` | `string` | `false` | The password for the client certificate, if any. |  |
| `path` | `string` | `false` | The directory in which to store the response file, if any. If a file attribute is not provided, the file name will be extracted from the Content-Disposition header if present. If no disposition header is present with the file name,<br>                 an error will be thrown |  |
| `clientCert` | `string` | `false` | The path to the client certificate, if any. |  |
| `compression` | `string` | `false` | The compression type to use for the request, if any. |  |
| `authType` | `string` | `true` | The authentication type to use. One of BASIC, NTLM. Default is BASIC. | `BASIC` |
| `cachedWithin` | `string` | `false` | If set, and a cached response is available within the specified duration (e.g. 10m for 10 minutes, 1h for 1 hour), the cached response will be returned instead of making a new request. |  |
| `encodeUrl` | `boolean` | `false` | Whether to encode the URL. Default is true. | `true` |
| `proxyServer` | `string` | `false` | The proxy server to use, if any. |  |
| `proxyPort` | `integer` | `false` | The proxy server port to use, if any. |  |
| `proxyUser` | `string` | `false` | The proxy server username to use, if any. |  |
| `proxyPassword` | `string` | `false` | The proxy server password to use, if any. |  |
| `name` | `string` | `false` |  |  |
| `delimiter` | `string` | `false` |  |  |
| `columns` | `string` | `false` |  |  |
| `firstRowAsHeaders` | `boolean` | `false` |  |  |
| `textQualifier` | `string` | `false` |  |  |
| `domain` | `string` | `false` |  |  |
| `workstation` | `string` | `false` |  |  |
| `httpVersion` | `string` | `false` |  | `HTTP/2` |

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


