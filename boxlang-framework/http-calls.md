---
icon: globe-wifi
description: Make HTTP/S requests with BoxLang's powerful and flexible HTTP component
---

# 🌐 HTTP/S Calls

BoxLang makes it really **easy** to interact with **any** HTTP/S endpoint via the `http` component. The `http` component generates HTTP/S requests and parses responses into convenient BoxLang structures, providing full support for modern HTTP features including HTTP/2, multipart uploads, authentication, proxy servers, and more.

## 🚀 Quick Start

```js
bx:http url="https://api.example.com/users" result="result" {
    bx:httpparam name="q" type="url" value="john";
}
dump( result )
```

{% hint style="info" %}
You can use ANY HTTP method in the `http` calls. The default method is `GET`, but you can specify `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `TRACE`, or `OPTIONS`.
{% endhint %}

## 📋 Overview

The HTTP component provides a comprehensive way to:

- 🔄 Make requests using any HTTP method (GET, POST, PUT, DELETE, etc.)
- 🔒 Handle authentication (Basic, NTLM)
- 📤 Upload files with multipart/form-data
- 📥 Download files and save to disk
- 🌐 Work with proxy servers
- ⚡ Support HTTP/1.1 and HTTP/2
- 🔐 Use client certificates for secure connections
- ⏱️ Configure timeouts and redirects
- 📦 Handle binary and text responses automatically

## 🎯 HTTP Parameters

As you can see from the example above, you can pass parameters to the HTTP request by using the child `httpparam` component. This parameter can be of many different types: `header, body, xml, cgi, file, url, formfield, cookie` depending on the requirements of the http endpoint.

## 📊 The Result Structure

The result structure will contain the following keys:

| Key | Description |
| :--- | :--- |
| `statusCode` | The HTTP response code (e.g., 200, 404, 500). |
| `statusText` | The HTTP response reason phrase (e.g., "OK", "Not Found", "Internal Server Error"). |
| `fileContent` | The body of the HTTP response. Usually a string, but could also be a Byte Array depending on the content type and `getAsBinary` setting. |
| `responseHeader` | A structure of response headers. Keys are header names and values are either the header value or an array of values if multiple headers with the same name exist. |
| `header` | All the HTTP response headers as a single formatted string. |
| `errorDetail` | An error message if the request failed (e.g., connection timeout, unknown host). |
| `mimeType` | The MIME type returned in the Content-Type response header. |
| `charset` | The character set returned in the Content-Type header (e.g., "UTF-8", "ISO-8859-1"). |
| `text` | A boolean indicating if the response body is text or binary. |
| `cookies` | A query object containing cookies returned by the server with columns: name, value, path, domain, expires, secure, httpOnly, samesite. |
| `HTTP_Version` | The HTTP version used for the response (e.g., "HTTP/1.1", "HTTP/2"). |
| `requestID` | A unique identifier (UUID) for this request, useful for logging and tracing. |
| `userAgent` | The User-Agent string that was sent with the request. |
| `executionTime` | The time taken to execute the request in milliseconds. |
| `request` | A structure containing request details: URL, method, timeout, multipart, headers. |

### Example Result Structure

```js
{
    "statusCode": 200,
    "statusText": "OK",
    "fileContent": "{\"users\": [...]}",
    "responseHeader": {
        "content-type": "application/json; charset=UTF-8",
        "content-length": "1234",
        "cache-control": "no-cache"
    },
    "mimeType": "application/json",
    "charset": "UTF-8",
    "HTTP_Version": "HTTP/2",
    "executionTime": 245,
    "requestID": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
    "cookies": query(...),
    "request": {
        "URL": "https://api.example.com/users",
        "method": "GET",
        "timeout": PT30S,
        "multipart": false,
        "headers": {...}
    }
}
```

## ⚙️ HTTP Attributes

The HTTP component accepts many attributes to control request behavior. Below are all available attributes:

| Attribute | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `url` | string | **required** | The HTTP/S endpoint URL to hit. Must start with `http://` or `https://`. |
| `port` | numeric | 80/443 | The port of the endpoint. Defaults to 80 for HTTP and 443 for HTTPS. |
| `method` | string | GET | The HTTP method to use: `GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `TRACE`, `OPTIONS`, `PATCH`. |
| `username` | string | | The username for HTTP authentication. |
| `password` | string | | The password for HTTP authentication. |
| `userAgent` | string | BoxLang | The User-Agent header to send with the request. |
| `charset` | string | UTF-8 | The character encoding to use for the request and response. |
| `resolveUrl` | boolean | false | If `true`, resolves relative URLs in the response body to absolute URLs. |
| `throwOnError` | boolean | true | If `true`, throws an error when the HTTP response status code is 400 or greater. |
| `redirect` | boolean | true | If `true`, follows HTTP redirects (301, 302, etc.). |
| `timeout` | numeric | unlimited | The request timeout in seconds. No timeout if not specified. |
| `getAsBinary` | string | auto | Controls binary response handling: `true`/`yes` (force binary), `false`/`no` (force text), `auto` (detect based on MIME type), `never` (throw error if binary). |
| `result` | string | bxhttp | The name of the variable to store the result structure. |
| `file` | string | | The filename for saving the response. If `path` is not provided, this can be a full file path. |
| `path` | string | | The directory path where the response file should be saved. If `file` is not specified, the filename is extracted from the Content-Disposition header. |
| `multipart` | boolean | false | If `true`, sends form fields as multipart/form-data. |
| `multipartType` | string | form-data | The multipart content type: `form-data` or `related`. |
| `authType` | string | BASIC | The authentication type to use: `BASIC` or `NTLM`. |
| `clientCert` | string | | The path to a client certificate file for SSL/TLS mutual authentication. |
| `clientCertPassword` | string | | The password for the client certificate. |
| `compression` | string | | The compression type for the request body. |
| `encodeUrl` | boolean | true | If `true`, encodes the URL. Default is `true` (encoding enabled). |
| `cachedWithin` | string | | If set, caches the response for the specified duration (e.g., `10m` for 10 minutes, `1h` for 1 hour). Returns cached response if available. |
| `proxyServer` | string | | The proxy server hostname or IP address. Requires `proxyPort`. |
| `proxyPort` | numeric | | The proxy server port. Requires `proxyServer`. |
| `proxyUser` | string | | The proxy server username for authentication. Requires `proxyPassword`. |
| `proxyPassword` | string | | The proxy server password for authentication. Requires `proxyUser`. |
| `httpVersion` | string | HTTP/2 | The HTTP protocol version to use: `HTTP/1.1` or `HTTP/2`. |

### ⚡ HTTP/2 Support

BoxLang defaults to **HTTP/2** for better performance and efficiency. HTTP/2 provides:

- Multiplexed streams over a single connection
- Header compression
- Server push capabilities
- Binary protocol for faster parsing

If you need to use HTTP/1.1 (for compatibility with older servers), set the `httpVersion` attribute:

```js
bx:http url="https://legacy-api.example.com" httpVersion="HTTP/1.1" result="result";
```

{% hint style="warning" %}
When using HTTP/2, the `TE` header is only supported with the value `trailers`. If you need to use `TE` with other values, BoxLang will automatically downgrade to HTTP/1.1.
{% endhint %}

## 📤 HTTPParam Component

The `httpparam` component allows you to add parameters to HTTP requests in various formats. Parameters can be headers, form fields, URL query strings, cookies, file uploads, or request body content.

### Basic Syntax

```js
bx:httpparam
    type="[type]"
    name="[name]"
    value="[value]"
    file="[filepath]"
    encoded="[boolean]"
    mimetype="[mimetype]";
```

### 🔖 Parameter Types

| Type | Description | URL Encoding |
| :--- | :--- | :--- |
| `header` | Specifies an HTTP header. | **No** (not encoded) |
| `body` | Specifies the request body content. | N/A |
| `xml` | Sets Content-Type to `text/xml` and uses `value` as the request body. | N/A |
| `cgi` | Similar to `header` but URL encodes the value by default (unless `encoded=false`). | **Yes** (by default) |
| `file` | Sends the contents of the specified file as part of a multipart request. | N/A |
| `url` | Appends a name-value pair to the URL query string. **Always URL encoded**. | **✅ Always** |
| `formfield` | Sends a form field value. URL encodes by default (unless `encoded=false`). | **Yes** (by default) |
| `cookie` | Sends a cookie as an HTTP header. URL encodes the value. | **Yes** (always) |

{% hint style="success" %}
**BoxLang 1.6.0 Change**: The `url` param type **now always URL encodes values** for security and RFC compliance. Previously, encoding could be controlled with the `encoded` attribute, but as of 1.6.0, URL parameters are **always encoded** to prevent injection attacks and ensure proper URL formatting.
{% endhint %}

### 🔧 HTTPParam Attributes

| Attribute | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `type` | string | **required** | The parameter type from the available types above. |
| `name` | string | conditional | The variable name for the parameter. Required for all types except `body`, `xml`, and `file`. |
| `value` | any | conditional | The value of the parameter. Required for all types except `file`. |
| `file` | string | conditional | The absolute path to the file to send. Required when `type="file"`. |
| `encoded` | boolean | false | For `formfield` and `cgi` types, specifies whether to URL encode the value. Ignored for other types. **Note**: For `url` type, encoding is always applied regardless of this setting (as of 1.6.0). |
| `mimetype` | string | auto-detected | For `file` type only. Specifies the MIME type of the file. If not provided, BoxLang attempts to detect it from the file extension. |

## 💡 Common Usage Examples

### 🔹 Simple GET Request

```js
bx:http url="https://api.example.com/users" result="users";
dump( users.fileContent );
```

### 🔹 POST with JSON Body

```js
bx:http url="https://api.example.com/users" method="POST" result="result" {
    bx:httpparam type="header" name="Content-Type" value="application/json";
    bx:httpparam type="header" name="x-api-token" value="your-api-token";
    bx:httpparam type="body" value=serializeJson( {
        "name": "Luis Majano",
        "email": "luis@example.com",
        "age": 42
    } );
}
dump( result );
```

### 🔹 POST with Form Fields

```js
bx:http url="https://api.example.com/login" method="POST" result="result" {
    bx:httpparam type="formfield" name="username" value="admin";
    bx:httpparam type="formfield" name="password" value="secret123";
}
```

### 🔹 GET with URL Parameters

URL parameters are **always encoded** as of BoxLang 1.6.0:

```js
bx:http url="https://api.example.com/search" result="result" {
    bx:httpparam type="url" name="q" value="hello world";
    bx:httpparam type="url" name="filter" value="active&verified";
    bx:httpparam type="url" name="limit" value="50";
}
// URL becomes: https://api.example.com/search?q=hello+world&filter=active%26verified&limit=50
```

### 🔹 Custom Headers

```js
bx:http url="https://api.example.com/data" result="result" {
    bx:httpparam type="header" name="Authorization" value="Bearer eyJhbGc...";
    bx:httpparam type="header" name="Accept" value="application/json";
    bx:httpparam type="header" name="User-Agent" value="MyApp/1.0";
}
```

### 🔹 XML Request

```js
bx:http url="https://api.example.com/soap" method="POST" result="result" {
    bx:httpparam type="xml" value='
        <?xml version="1.0"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
            <soap:Body>
                <m:GetUser>
                    <m:UserId>123</m:UserId>
                </m:GetUser>
            </soap:Body>
        </soap:Envelope>
    ';
}
```

### 🔹 File Upload (Multipart)

```js
bx:http url="https://api.example.com/upload" method="POST" multipart="true" result="result" {
    bx:httpparam type="file" name="avatar" file="/path/to/photo.jpg" mimetype="image/jpeg";
    bx:httpparam type="formfield" name="description" value="My profile picture";
    bx:httpparam type="formfield" name="userId" value="12345";
}
```

### 🔹 Multiple File Upload

```js
bx:http url="https://api.example.com/upload-multiple" method="POST" multipart="true" result="result" {
    bx:httpparam type="file" name="file1" file="/path/to/document1.pdf";
    bx:httpparam type="file" name="file2" file="/path/to/document2.pdf";
    bx:httpparam type="file" name="file3" file="/path/to/image.png" mimetype="image/png";
    bx:httpparam type="formfield" name="category" value="documents";
}
```

## 📥 Downloading Files

### 🔹 Download to Specific Path

```js
// Download and save to a specific directory with a specific filename
bx:http
    url="https://example.com/files/report.pdf"
    path="/downloads/reports"
    file="monthly-report.pdf"
    result="download";

dump( download.statusCode ); // 200
```

### 🔹 Download Using Content-Disposition

```js
// Let BoxLang extract the filename from the Content-Disposition header
bx:http
    url="https://example.com/download/file"
    path="/downloads"
    result="download";

// The filename will be extracted from: Content-Disposition: attachment; filename="report.pdf"
```

### 🔹 Download with Full File Path

```js
// Provide the complete file path
bx:http
    url="https://example.com/files/data.csv"
    file="/var/data/downloads/data.csv"
    result="download";
```

## 🔒 Authentication

### 🔹 Basic Authentication

```js
bx:http
    url="https://api.example.com/secure"
    username="admin"
    password="secret123"
    authType="BASIC"
    result="result";
```

This automatically adds the `Authorization: Basic base64(username:password)` header.

### 🔹 Bearer Token Authentication

```js
bx:http url="https://api.example.com/protected" result="result" {
    bx:httpparam type="header" name="Authorization" value="Bearer YOUR_ACCESS_TOKEN_HERE";
}
```

### 🔹 API Key Authentication

```js
bx:http url="https://api.example.com/data" result="result" {
    bx:httpparam type="header" name="X-API-Key" value="your-api-key-here";
}
```

## 🌐 Proxy Server Support

BoxLang supports routing HTTP requests through proxy servers:

```js
bx:http
    url="https://api.example.com/data"
    proxyServer="proxy.company.com"
    proxyPort="8080"
    result="result";
```

### 🔹 Proxy with Authentication

```js
bx:http
    url="https://api.example.com/data"
    proxyServer="proxy.company.com"
    proxyPort="8080"
    proxyUser="proxyuser"
    proxyPassword="proxypass"
    result="result";
```

## ⏱️ Timeouts and Error Handling

### 🔹 Setting Timeouts

```js
// Timeout after 30 seconds
bx:http
    url="https://slow-api.example.com/data"
    timeout="30"
    result="result";

if ( result.statusCode == 408 ) {
    writeOutput( "Request timed out!" );
}
```

### 🔹 Disabling Error Throwing

By default, BoxLang throws an error when the status code is 400 or greater. You can disable this:

```js
bx:http
    url="https://api.example.com/might-fail"
    throwOnError="false"
    result="result";

if ( result.statusCode >= 400 ) {
    writeOutput( "Error: #result.statusCode# - #result.statusText#" );
    writeOutput( "Details: #result.errorDetail#" );
} else {
    writeOutput( "Success: #result.fileContent#" );
}
```

### 🔹 Handling Different HTTP Status Codes

```js
bx:http url="https://api.example.com/resource/123" throwOnError="false" result="result";

switch ( result.statusCode ) {
    case 200:
        writeOutput( "Success!" );
        break;
    case 404:
        writeOutput( "Resource not found" );
        break;
    case 500:
        writeOutput( "Server error: #result.errorDetail#" );
        break;
    default:
        writeOutput( "Unexpected status: #result.statusCode#" );
}
```

## 🔄 Redirects

BoxLang automatically follows HTTP redirects (301, 302, etc.) by default:

```js
// Follows redirects automatically
bx:http url="https://example.com/old-url" result="result";
```

To disable redirect following:

```js
// Don't follow redirects
bx:http url="https://example.com/old-url" redirect="false" result="result";

if ( result.statusCode == 301 || result.statusCode == 302 ) {
    newLocation = result.responseHeader[ "location" ];
    writeOutput( "Redirects to: #newLocation#" );
}
```

## 💾 Response Caching

Cache HTTP responses to improve performance and reduce server load:

```js
// Cache for 10 minutes
bx:http
    url="https://api.example.com/data"
    cachedWithin="10m"
    result="result";

// Cache for 1 hour
bx:http
    url="https://api.example.com/data"
    cachedWithin="1h"
    result="result";

// Cache for 1 day
bx:http
    url="https://api.example.com/data"
    cachedWithin="1d"
    result="result";
```

## 🔐 Client Certificates

For mutual TLS authentication, you can provide a client certificate:

```js
bx:http
    url="https://secure-api.example.com/data"
    clientCert="/path/to/client-cert.p12"
    clientCertPassword="certpassword"
    result="result";
```

## 📦 Binary Responses

Control how binary content is handled:

```js
// Auto-detect based on MIME type (default)
bx:http url="https://example.com/image.png" getAsBinary="auto" result="result";
dump( result.fileContent ); // Byte array if image

// Force binary
bx:http url="https://example.com/data" getAsBinary="yes" result="result";

// Force text
bx:http url="https://example.com/data" getAsBinary="no" result="result";

// Throw error if binary
bx:http url="https://example.com/might-be-binary" getAsBinary="never" result="result";
// Throws error if response is binary
```

## 🎯 Advanced Examples

### 🔹 RESTful API CRUD Operations

```js
// CREATE
bx:http url="https://api.example.com/users" method="POST" result="createResult" {
    bx:httpparam type="header" name="Content-Type" value="application/json";
    bx:httpparam type="body" value=serializeJson( { name: "John", email: "john@example.com" } );
}

// READ
bx:http url="https://api.example.com/users/123" result="readResult";

// UPDATE
bx:http url="https://api.example.com/users/123" method="PUT" result="updateResult" {
    bx:httpparam type="header" name="Content-Type" value="application/json";
    bx:httpparam type="body" value=serializeJson( { name: "John Doe", email: "john.doe@example.com" } );
}

// DELETE
bx:http url="https://api.example.com/users/123" method="DELETE" result="deleteResult";
```

### 🔹 GraphQL Query

```js
query = {
    "query": "query { users(limit: 10) { id name email } }"
};

bx:http url="https://api.example.com/graphql" method="POST" result="result" {
    bx:httpparam type="header" name="Content-Type" value="application/json";
    bx:httpparam type="body" value=serializeJson( query );
}

userData = deserializeJson( result.fileContent );
dump( userData.data.users );
```

### 🔹 Handling Cookies

```js
// Send cookies with request
bx:http url="https://example.com/api" result="result" {
    bx:httpparam type="cookie" name="sessionId" value="abc123xyz";
    bx:httpparam type="cookie" name="preference" value="dark-mode";
}

// Access cookies from response
dump( result.cookies );

// Iterate through cookies
loop query="result.cookies" {
    writeOutput( "Cookie: #result.cookies.name# = #result.cookies.value#<br>" );
}
```

### 🔹 Custom User Agent

```js
bx:http
    url="https://api.example.com/data"
    userAgent="MyApplication/2.0 (BoxLang; https://example.com/contact)"
    result="result";
```

### 🔹 Request with Multiple Headers

```js
bx:http url="https://api.example.com/data" result="result" {
    bx:httpparam type="header" name="Accept" value="application/json";
    bx:httpparam type="header" name="Accept-Language" value="en-US,en;q=0.9";
    bx:httpparam type="header" name="Accept-Encoding" value="gzip, deflate";
    bx:httpparam type="header" name="Authorization" value="Bearer token123";
    bx:httpparam type="header" name="X-Request-ID" value="unique-request-id";
    bx:httpparam type="header" name="X-Client-Version" value="1.0.0";
}
```

## 🎪 Interceptor Events

BoxLang fires interceptor events during HTTP requests for advanced monitoring and manipulation:

### Available Events

| Event | Description | Data Provided |
| :--- | :--- | :--- |
| `onHTTPRequest` | Fired before the HTTP request is sent. | `requestID`, `httpClient`, `httpRequest`, `targetURI`, `attributes` |
| `onHTTPRawResponse` | Fired immediately after receiving the raw response, before processing. | `requestID`, `response`, `httpClient`, `httpRequest`, `targetURI`, `attributes` |
| `onHTTPResponse` | Fired after the response is fully processed. | `requestID`, `response`, `result` |

### Example Interceptor

```js
component {
    function onHTTPRequest( event, interceptData, buffer, rc, prc ) {
        // Log all outgoing requests
        log.info( "HTTP Request to: #interceptData.targetURI#" );
        log.info( "Request ID: #interceptData.requestID#" );
        log.info( "Method: #interceptData.attributes.method#" );
    }

    function onHTTPRawResponse( event, interceptData, buffer, rc, prc ) {
        // Track response times
        writeLog( "Response received for request #interceptData.requestID# with status #interceptData.response.statusCode()#" );
    }

    function onHTTPResponse( event, interceptData, buffer, rc, prc ) {
        // Monitor API usage
        if ( interceptData.result.statusCode >= 400 ) {
            writeLog( type="error", text="HTTP Error #interceptData.result.statusCode#: #interceptData.result.errorDetail#" );
        }
    }
}
```

## 🔍 Troubleshooting

### Common Issues

**Issue**: Connection timeout

```js
// Solution: Increase timeout
bx:http url="https://slow-api.com" timeout="60" result="result";
```

**Issue**: SSL certificate errors

```js
// Note: BoxLang validates SSL certificates. For development/testing with self-signed certs,
// you may need to import the certificate into your Java keystore.
```

**Issue**: Large file uploads timing out

```js
// Solution: Increase timeout and consider chunking
bx:http
    url="https://api.com/upload"
    method="POST"
    timeout="300"
    multipart="true"
    result="result" {
    bx:httpparam type="file" name="largefile" file="/path/to/large.zip";
}
```

**Issue**: URL parameters not encoded properly

```js
// As of BoxLang 1.6.0, URL params are ALWAYS encoded
bx:http url="https://api.com/search" result="result" {
    // This is automatically encoded
    bx:httpparam type="url" name="query" value="hello & goodbye";
}
// Results in: ?query=hello+%26+goodbye
```

## 🎓 Best Practices

1. **Always specify timeouts** for external API calls to prevent hanging requests
2. **Use `throwOnError="false"`** when you need to handle errors gracefully
3. **Cache responses** when data doesn't change frequently using `cachedWithin`
4. **Use appropriate HTTP methods** - GET for reading, POST for creating, PUT/PATCH for updating, DELETE for removing
5. **Set proper Content-Type headers** when sending JSON, XML, or other content types
6. **Handle different status codes** - don't assume success, check `statusCode`
7. **Use HTTPS** for secure communications, especially when sending sensitive data
8. **Leverage HTTP/2** (the default) for better performance
9. **Monitor with interceptors** for logging, metrics, and debugging
10. **Use `requestID`** from the result structure for request tracing and correlation

## 📚 Related Documentation

- [File Handling](file-handling.md) - For working with uploaded/downloaded files
- [Caching](caching/) - For understanding response caching strategies
- [Interceptors](interceptors/) - For advanced request/response manipulation
- [Java Integration](java-integration.md) - For accessing Java HTTP client directly

---

With BoxLang's HTTP component, you have a powerful and flexible tool for all your HTTP/S communication needs! 🚀
