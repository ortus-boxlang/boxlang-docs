---
icon: globe-wifi
description: Make HTTP/S requests with BoxLang's powerful and flexible HTTP component
---

# 🌐 HTTP/S Calls

BoxLang provides **two powerful approaches** for making HTTP/S requests: the **`http()` BIF** for fluent, programmatic requests and the **`bx:http` component** for template-based requests. Both use the same underlying `BoxHttpClient`, ensuring consistent behavior across your application.

Both approaches provide full support for:

- ⚡ HTTP/1.1 and HTTP/2 protocols
- 🔄 All HTTP methods (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, TRACE)
- 🔒 Authentication (Basic Auth)
- 📤 File uploads (multipart/form-data)
- 📥 File downloads
- 🌐 Proxy server support
- 🔐 Client certificates (mutual TLS)
- ⏱️ Configurable timeouts and redirects
- 📡 **Server-Sent Events (SSE) consumption**
- 🎯 Response streaming with callbacks

## 📋 Table of Contents

- [Quick Start Examples](#quick-start-examples)
- [Choosing Your Approach](#choosing-your-approach)
- [HTTP Request Callbacks Overview](#http-request-callbacks-overview)
- [The Result Structure](#the-result-structure)
- [HTTP Attributes](#http-attributes)
- [HTTPParam Component](#httpparam-component)
- [Common Usage Examples](#common-usage-examples)
- [Downloading Files](#downloading-files)
- [Authentication](#authentication)
- [Proxy Server Support](#proxy-server-support)
- [Timeouts and Error Handling](#timeouts-and-error-handling)
- [Redirects](#redirects)
- [Response Caching](#response-caching)
- [Client Certificates](#client-certificates)
- [Binary Responses](#binary-responses)
- [Advanced Examples](#advanced-examples)
- [The http() BIF - Fluent API Reference](#the-http-bif---fluent-api-reference)
- [Server-Sent Events (SSE) Consumption](#server-sent-events-sse-consumption)
- [Interceptor Events](#interceptor-events)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [Related Documentation](#related-documentation)

## 🚀 Quick Start Examples

### Using the `http()` BIF (Fluent API)

```js
// Simple GET request
result = http( "https://api.example.com/users" )
    .send();

// POST with JSON
result = http( "https://api.example.com/users" )
    .post()
    .jsonBody( '{"name":"John","email":"john@example.com"}' )
    .send();

// With query parameters
result = http( "https://api.example.com/users" )
    .urlParam( "q", "john" )
    .send();
```

### Using the `bx:http` Component (Template Syntax)

```js
bx:http url="https://api.example.com/users" result="result" {
    bx:httpparam name="q" type="url" value="john";
}
dump( result );
```

{% hint style="info" %}
**When to use which approach:**

- **`http()` BIF**: Best for programmatic code, services, APIs, and fluent chaining patterns
- **`bx:http` Component**: Best for templates, views, and declarative request configurations

Both approaches support ALL HTTP methods: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `TRACE`, `OPTIONS`
{% endhint %}

---

## 🎯 Choosing Your Approach

### The `http()` BIF - Fluent API

**New in BoxLang 1.8.0** - The `http()` BIF provides a modern, fluent interface for building HTTP requests programmatically.

**Advantages:**

- ✨ Fluent, chainable API for readable code
- 🎯 Intellisense-friendly method names
- 🔧 Programmatic request building
- 🚀 Built-in response transformers (`asJSON()`, `asXML()`, `asText()`)
- 📡 Native SSE consumption with callbacks
- ⚡ Async execution with `BoxFuture` integration
- 🎨 Conditional request building with `when()`, `ifNull()`, `ifNotNull()`

**Example:**

```js
result = http( "https://api.github.com/repos/ortus-boxlang/boxlang" )
    .header( "Accept", "application/json" )
    .userAgent( "BoxLang-App/1.0" )
    .timeout( 30 )
    .asJSON() // Auto-parse JSON response
    .send();

println( result.name ); // Direct access to parsed JSON
```

### The `bx:http` Component - Template Syntax

The `bx:http` component provides a familiar, tag-based approach for making HTTP requests in templates.

**Advantages:**

- 📝 Declarative, template-friendly syntax
- 🔄 Familiar to CFML developers
- 📦 Great for view-layer HTTP calls
- 🎯 Child `bx:httpparam` components for parameters
- 📡 SSE consumption with callbacks
- 🎨 Easy to read and maintain in templates

**Example:**

```js
bx:http url="https://api.github.com/repos/ortus-boxlang/boxlang" result="repo" {
    bx:httpparam type="header" name="Accept" value="application/json";
}
repoData = deserializeJSON( repo.fileContent );
println( repoData.name );
```

---

## 🎯 HTTP Request Callbacks Overview

BoxLang provides **four powerful callbacks** for monitoring and processing HTTP requests in real-time. These callbacks work with both the `http()` BIF and the `bx:http` component, enabling you to:

- 📊 Track request lifecycle events
- 🌊 Stream and process response data incrementally
- 📡 Consume Server-Sent Events (SSE) from remote servers
- ⚠️ Handle errors and implement retry logic
- 📈 Monitor progress for large uploads/downloads

### Callback Reference

| Callback | When It's Called | Primary Use Cases | Parameters |
|----------|------------------|-------------------|------------|
| **`onRequestStart`** | Before the HTTP request begins | Logging, request ID generation, pre-request validation | `httpResult`, `httpClient` |
| **`onChunk`** | For each chunk of data received | Streaming responses, SSE consumption, progress tracking | `chunk`, `lastEventId`, `httpResult`, `httpClient`, `response` |
| **`onComplete`** | After successful request completion | Cleanup, final logging, success notifications | `httpResult` |
| **`onError`** | When an error occurs | Error handling, retry logic, alerting | `error`, `httpResult` |

<details open>
<summary>Callback Signatures</summary>

#### `onRequestStart( httpResult, httpClient )`

Called immediately before the HTTP request is sent to the server.

**Parameters:**

- `httpResult` (struct) - Partial result structure with request details (URL, method, headers, etc.)
- `httpClient` (BoxHttpClient) - The client instance making the request

**Use Cases:**

- Generate and log request IDs for tracing
- Validate request configuration before sending
- Start timing/monitoring operations
- Log request details for debugging

**Example:**

```js
http( "https://api.example.com/users" )
    .onRequestStart( ( httpResult, httpClient ) => {
        requestId = createUUID();
        logger.info( "Starting request #requestId# to #httpResult.request.URL#" );
        startTime = getTickCount();
    } )
    .send();
```

#### `onChunk( chunk, lastEventId, httpResult, httpClient, response )`

Called for each chunk of data received from the server. Essential for streaming and SSE consumption.

**Parameters:**

- `chunk` (any) - The data chunk received:
  - **Regular HTTP**: String or binary data chunk
  - **SSE mode**: Struct with `{ data, event, id, retry }` fields
- `lastEventId` (string) - Most recent SSE event ID (for reconnection support)
- `httpResult` (struct) - The result structure (partially populated during streaming)
- `httpClient` (BoxHttpClient) - The client instance
- `response` (java.net.http.HttpResponse) - Raw Java HTTP response object

**Use Cases:**

- Process streaming API responses (OpenAI, Claude, etc.)
- Consume Server-Sent Events from remote servers
- Monitor download progress
- Process large responses incrementally without loading into memory

**Example (Streaming JSON):**

```js
fullResponse = "";

http( "https://api.example.com/stream" )
    .onChunk( ( chunk, lastEventId, httpResult ) => {
        fullResponse &= chunk;
        writeOutput( chunk );
        flush;
    } )
    .send();
```

**Example (SSE Consumption):**

```js
http( "https://api.example.com/events" )
    .sse( true )
    .onChunk( ( event, lastEventId, httpResult ) => {
        // event is a struct: { data, event, id, retry }
        println( "Event Type: " & event.event );
        println( "Event Data: " & event.data );
        println( "Event ID: " & event.id );
        println( "Last Event ID: " & lastEventId );
    } )
    .send();
```

#### `onComplete( httpResult )`

Called after the HTTP request completes successfully.

**Parameters:**

- `httpResult` (struct) - Complete result structure with all response data

**Use Cases:**

- Final cleanup operations
- Success logging and metrics
- Trigger downstream processes
- Send completion notifications

**Example:**

```js
http( "https://api.example.com/process" )
    .post()
    .jsonBody( '{"data":"value"}' )
    .onComplete( ( httpResult ) => {
        logger.info( "Request completed in #httpResult.executionTime#ms" );
        logger.info( "Status: #httpResult.statusCode# #httpResult.statusText#" );
        metrics.recordSuccess( httpResult.executionTime );
    } )
    .send();
```

#### `onError( error, httpResult )`

Called when an error occurs during the HTTP request.

**Parameters:**

- `error` (Exception) - The error/exception that occurred
- `httpResult` (struct) - Partial result structure (may contain partial data)

**Use Cases:**

- Implement retry logic with exponential backoff
- Log errors with context
- Send error notifications/alerts
- Graceful degradation and fallback handling

**Example:**

```js
retryCount = 0;
maxRetries = 3;

function makeRequest() {
    http( "https://api.example.com/data" )
        .timeout( 10 )
        .onError( ( error, httpResult ) => {
            logger.error( "Request failed: #error.message#" );

            if ( retryCount < maxRetries ) {
                retryCount++;
                sleepTime = 2 ^ retryCount * 1000; // Exponential backoff
                logger.info( "Retrying in #sleepTime#ms (attempt #retryCount#/#maxRetries#)" );
                sleep( sleepTime );
                makeRequest(); // Retry
            } else {
                logger.error( "Max retries reached, giving up" );
                throw error;
            }
        } )
        .onComplete( ( httpResult ) => {
            logger.info( "Request succeeded after #retryCount# retries" );
        } )
        .send();
}

makeRequest();
```

</details>

### Callback Execution Order

The callbacks execute in this order:

1. **`onRequestStart`** - Before request begins
2. **`onChunk`** - Multiple times during response (if streaming/SSE)
3. **`onComplete`** OR **`onError`** - After request finishes
   - `onComplete` for successful requests
   - `onError` for failed requests

### Using Callbacks with Both Approaches

#### With `http()` BIF (Fluent API)

```js
http( "https://api.example.com/data" )
    .onRequestStart( ( httpResult, httpClient ) => {
        // Pre-request logic
    } )
    .onChunk( ( chunk, lastEventId, httpResult ) => {
        // Process streaming data
    } )
    .onComplete( ( httpResult ) => {
        // Success handling
    } )
    .onError( ( error, httpResult ) => {
        // Error handling
    } )
    .send();
```

#### With `bx:http` Component

```js
function handleRequestStart( httpResult, httpClient ) {
    // Pre-request logic
}

function handleChunk( chunk, lastEventId, httpResult ) {
    // Process streaming data
}

function handleComplete( httpResult ) {
    // Success handling
}

function handleError( error, httpResult ) {
    // Error handling
}

bx:http
    url="https://api.example.com/data"
    onRequestStart=handleRequestStart
    onChunk=handleChunk
    onComplete=handleComplete
    onError=handleError
    result="result";
```

<details>
<summary>Real-World Callback Patterns</summary>

#### Pattern 1: Progress Tracking

```js
bytesReceived = 0;
totalBytes = 0;

http( "https://example.com/large-file.zip" )
    .outputFile( "downloads/large-file.zip" )
    .onRequestStart( ( httpResult, httpClient ) => {
        println( "Starting download..." );
    } )
    .onChunk( ( chunk, lastEventId, httpResult ) => {
        bytesReceived += len( chunk );
        if ( totalBytes == 0 && structKeyExists( httpResult.responseHeader, "content-length" ) ) {
            totalBytes = val( httpResult.responseHeader["content-length"] );
        }
        if ( totalBytes > 0 ) {
            percent = round( ( bytesReceived / totalBytes ) * 100 );
            println( "Progress: #percent#% (#bytesReceived# / #totalBytes# bytes)" );
        }
    } )
    .onComplete( ( httpResult ) => {
        println( "Download complete! Total: #bytesReceived# bytes in #httpResult.executionTime#ms" );
    } )
    .onError( ( error, httpResult ) => {
        println( "Download failed: #error.message#" );
    } )
    .send();
```

#### Pattern 2: Request/Response Logging

```js
http( "https://api.example.com/users" )
    .post()
    .jsonBody( userPayload )
    .onRequestStart( ( httpResult, httpClient ) => {
        requestId = createUUID();
        httpResult.requestId = requestId;

        logger.info( "[#requestId#] Starting POST to #httpResult.request.URL#" );
        logger.debug( "[#requestId#] Headers: #serializeJSON( httpResult.request.headers )#" );
    } )
    .onComplete( ( httpResult ) => {
        logger.info(
            "[#httpResult.requestId#] Completed: #httpResult.statusCode# " &
            "in #httpResult.executionTime#ms"
        );
    } )
    .onError( ( error, httpResult ) => {
        logger.error(
            "[#httpResult.requestId#] Failed: #error.message#",
            error
        );
    } )
    .send();
```

#### Pattern 3: Retry with Circuit Breaker

```js
circuitBreaker = {
    failures: 0,
    threshold: 5,
    resetAfter: 60000, // 1 minute
    lastFailureTime: 0,
    isOpen: false
};

function checkCircuit() {
    if ( circuitBreaker.isOpen ) {
        if ( getTickCount() - circuitBreaker.lastFailureTime > circuitBreaker.resetAfter ) {
            // Reset circuit after timeout
            circuitBreaker.isOpen = false;
            circuitBreaker.failures = 0;
            logger.info( "Circuit breaker reset" );
        } else {
            throw new Exception( "Circuit breaker is OPEN, request blocked" );
        }
    }
}

http( "https://api.example.com/data" )
    .onRequestStart( ( httpResult, httpClient ) => {
        checkCircuit();
    } )
    .onComplete( ( httpResult ) => {
        // Success - reset failure count
        circuitBreaker.failures = 0;
    } )
    .onError( ( error, httpResult ) => {
        circuitBreaker.failures++;
        circuitBreaker.lastFailureTime = getTickCount();

        if ( circuitBreaker.failures >= circuitBreaker.threshold ) {
            circuitBreaker.isOpen = true;
            logger.error( "Circuit breaker OPENED after #circuitBreaker.failures# failures" );
        }

        logger.error( "Request failed (#circuitBreaker.failures#/#circuitBreaker.threshold#): #error.message#" );
    } )
    .send();
```

{% hint style="success" %}

**Callback Best Practices:**

1. **Keep callbacks lightweight** - Avoid heavy processing in `onChunk` to prevent blocking
2. **Use try-catch** - Protect against errors in callback code
3. **Store context carefully** - Use closure variables or pass context through httpResult
4. **Log appropriately** - Use different log levels (DEBUG for chunks, INFO for completion, ERROR for failures)
5. **Handle SSE disconnects** - Implement reconnection logic in `onError` for SSE streams
6. **Monitor memory** - Process and discard data incrementally in `onChunk` for large responses
7. **Use request IDs** - Generate IDs in `onRequestStart` for correlation across callbacks
8. **Implement timeouts** - Don't rely solely on callbacks for timeout handling
{% endhint %}

</details>

---

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
| `result` | string | bxhttp | The name of the variable to store the result structure. If not specified, BoxLang creates a `bxHTTP` variable in the variables scope. **Best practice: Always specify this attribute explicitly.** |
| `file` | string | | The filename for saving the response. If `path` is not provided, this can be a full file path. |
| `path` | string | | The directory path where the response file should be saved. If `file` is not specified, the filename is extracted from the Content-Disposition header. |
| `multipart` | boolean | false | If `true`, sends form fields as multipart/form-data. |
| `multipartType` | string | form-data | The multipart content type: `form-data` or `related`. |
| `authType` | string | BASIC | The authentication type to use: `BASIC`. |
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

### 📝 Result Variable Best Practice

By default, if you don't specify the `result` attribute, BoxLang will create a variable named `bxHTTP` in the variables scope to store the HTTP response.

```js
// Without result attribute - creates variables.bxHTTP
bx:http url="https://api.example.com/users";
dump( bxHTTP ); // Works, but not recommended

// With result attribute - explicit and clear (RECOMMENDED)
bx:http url="https://api.example.com/users" result="apiResponse";
dump( apiResponse ); // Better approach
```

{% hint style="danger" %}
**Warning: State Bleeding in Classes**

When using the HTTP component inside classes **without** specifying the `result` attribute, the `bxHTTP` variable can bleed into the class's variables scope, potentially causing:

- **Unintended state persistence** across method calls
- **Memory leaks** if the HTTP response is large
- **Race conditions** in concurrent scenarios
- **Difficult debugging** due to implicit variable creation

**Always use the `result` attribute** when making HTTP calls inside classes:

```js
class UserService {
    function fetchUsers() {
        // ❌ BAD - bxHTTP bleeds into class state
        bx:http url="https://api.example.com/users";
        return bxHTTP.fileContent;
    }

    function fetchUsers() {
        // ✅ GOOD - Explicit result variable
        bx:http url="https://api.example.com/users" result="response";
        return response.fileContent;
    }
}
```

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

<details>
<summary>Client Certificates</summary>

BoxLang supports mutual TLS authentication using client certificates. This allows your application to authenticate to servers that require client-side SSL/TLS certificates, commonly used in enterprise environments and B2B integrations.

### 🔹 Basic Client Certificate Authentication

```js
bx:http
    url="https://secure-api.example.com/data"
    clientCert="/path/to/client-cert.p12"
    clientCertPassword="certpassword"
    result="result";
```

### 🔹 Supported Certificate Formats

BoxLang supports PKCS#12 (`.p12` or `.pfx`) certificate files, which bundle the client certificate and private key in a single encrypted file.

```js
// Using .p12 format
bx:http
    url="https://api.partner.com/secure-endpoint"
    clientCert="/secure/certs/client-certificate.p12"
    clientCertPassword="mySecurePassword123"
    result="result";

// Using .pfx format (same as .p12)
bx:http
    url="https://api.partner.com/secure-endpoint"
    clientCert="/secure/certs/client-certificate.pfx"
    clientCertPassword="mySecurePassword123"
    result="result";
```

### 🔹 Common Use Cases

**Enterprise API Integration:**

```js
// Connect to corporate API requiring client cert
bx:http
    url="https://internal-api.company.com/employee/data"
    clientCert="/etc/ssl/certs/company-client.p12"
    clientCertPassword="#getSystemSetting('CERT_PASSWORD')#"
    result="employeeData" {
    bx:httpparam type="header" name="Accept" value="application/json";
}
```

**B2B Partner Integration:**

```js
// Secure communication with business partner
bx:http
    url="https://partner-api.example.com/orders"
    method="POST"
    clientCert="/certs/partner-auth.p12"
    clientCertPassword="#application.certPassword#"
    result="orderResult" {
    bx:httpparam type="header" name="Content-Type" value="application/json";
    bx:httpparam type="body" value=serializeJson( orderData );
}
```

**Government/Regulated APIs:**

```js
// Access government service requiring client authentication
bx:http
    url="https://gov-api.example.gov/verify"
    clientCert="/secure/gov-client-cert.p12"
    clientCertPassword="#decrypt(application.encryptedCertPwd, application.certKey)#"
    timeout="60"
    result="verificationResult";
```

### 🔹 Security Best Practices

{% hint style="warning" %}
**Certificate Security Guidelines:**

1. **Never hardcode passwords** - Use environment variables or encrypted configuration
2. **Restrict file permissions** - Ensure certificate files are readable only by the application user
3. **Rotate certificates** - Regularly update certificates before expiration
4. **Use secure storage** - Store certificates in protected directories outside web root
5. **Monitor expiration** - Set up alerts for certificate expiration dates
{% endhint %}

```js
// ✅ GOOD - Password from environment variable
bx:http
    url="https://secure-api.com/data"
    clientCert="/etc/certs/client.p12"
    clientCertPassword="#getSystemSetting('CLIENT_CERT_PASSWORD')#"
    result="result";

// ❌ BAD - Hardcoded password
bx:http
    url="https://secure-api.com/data"
    clientCert="/certs/client.p12"
    clientCertPassword="password123"
    result="result";
```

### 🔹 Error Handling

```js
try {
    bx:http
        url="https://secure-api.example.com/data"
        clientCert="/path/to/client-cert.p12"
        clientCertPassword="certpassword"
        throwOnError="false"
        result="result";

    if ( result.statusCode == 200 ) {
        writeOutput( "Authenticated successfully" );
    } else if ( result.statusCode == 401 || result.statusCode == 403 ) {
        writeOutput( "Authentication failed - check certificate validity" );
    }
} catch ( any e ) {
    if ( findNoCase( "certificate", e.message ) ) {
        writeLog( type="error", text="Certificate error: #e.message#" );
        // Handle certificate-specific errors (wrong password, expired cert, etc.)
    }
    rethrow;
}
```

### 🔹 Troubleshooting

**Common Issues:**

| Issue | Solution |
| :--- | :--- |
| "Certificate password incorrect" | Verify the password matches the certificate file |
| "Certificate not found" | Check file path is absolute and file exists |
| "Certificate expired" | Renew and replace the certificate file |
| "Certificate format not supported" | Ensure certificate is in PKCS#12 (.p12/.pfx) format |
| "SSL handshake failed" | Verify server trusts your certificate's CA |

</details>

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

<details>
<summary>Advanced Examples</summary>

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

</details>

---

<details>
<summary>The `http()` BIF - Fluent API Reference</summary>

**New in BoxLang 1.8.0** - The `http()` BIF provides a modern, fluent API for building and executing HTTP requests programmatically.

### Basic Syntax

```js
result = http( url )
    .method()        // Chain configuration methods
    .header()
    .body()
    .send();         // Execute the request
```

### HTTP Method Shortcuts

The BIF provides convenient method shortcuts:

```js
http( url ).get().send();     // GET request
http( url ).post().send();    // POST request
http( url ).put().send();     // PUT request
http( url ).delete().send();  // DELETE request
http( url ).patch().send();   // PATCH request
http( url ).head().send();    // HEAD request
http( url ).options().send(); // OPTIONS request
http( url ).trace().send();   // TRACE request
```

### Configuration Methods

#### Request Configuration

```js
http( url )
    .method( "POST" )           // Set HTTP method
    .timeout( 30 )              // Timeout in seconds
    .port( 8080 )               // Custom port
    .httpVersion( "HTTP/1.1" )  // HTTP version
    .http1()                    // Shortcut for HTTP/1.1
    .http2()                    // Shortcut for HTTP/2
    .charset( "UTF-8" )         // Character encoding
    .userAgent( "MyApp/1.0" )   // Custom user agent
    .throwOnError( true )       // Throw on 4xx/5xx responses
    .multipart( true )          // Enable multipart mode
    .send();
```

#### Headers and Parameters

```js
http( url )
    .header( "Content-Type", "application/json" )
    .header( "Authorization", "Bearer token123" )
    .urlParam( "q", "search" )           // Query string parameter
    .urlParam( "page", "1", false )      // With encoding control
    .formField( "username", "john" )     // Form field
    .formField( "email", "j@example.com", true )  // With encoding
    .cookie( "session", "abc123" )       // Cookie
    .send();
```

#### Request Body

```js
// Plain body
http( url )
    .post()
    .body( "Raw request body" )
    .send();

// JSON body (auto-sets Content-Type header)
http( url )
    .post()
    .jsonBody( '{"name":"John","age":30}' )
    .send();

// XML body (auto-sets Content-Type header)
http( url )
    .post()
    .xmlBody( '<user><name>John</name></user>' )
    .send();
```

#### File Uploads

```js
http( url )
    .post()
    .multipart( true )
    .file( "document", "/path/to/file.pdf" )
    .file( "image", "/path/to/image.png", "image/png" )  // With MIME type
    .formField( "description", "File upload" )
    .send();
```

#### File Downloads

```js
http( url )
    .outputDirectory( "/downloads" )
    .outputFile( "report.pdf" )
    .send();
```

#### Authentication

```js
http( url )
    .withBasicAuth( "username", "password" )
    .send();
```

### Response Transformers

Transform the response automatically before returning:

```js
// Parse JSON response
users = http( "https://api.example.com/users" )
    .asJSON()
    .send();
println( users[ 1 ].name );  // Direct access to parsed data

// Get text content only
content = http( "https://example.com/page.html" )
    .asText()
    .send();
println( content );  // Just the text, not the full result struct

// Parse XML response
xmlDoc = http( "https://example.com/feed.xml" )
    .asXML()
    .send();
println( xmlDoc.xmlRoot );

// Custom transformer
result = http( url )
    .transform( ( httpResult ) => {
        return {
            status: httpResult.statusCode,
            data: deserializeJSON( httpResult.fileContent ),
            headers: httpResult.responseHeader
        };
    } )
    .send();
```

### Conditional Building

Build requests conditionally:

```js
request = http( "https://api.example.com/data" );

// Execute lambda only if condition is true
request.when( userIsAdmin, ( req ) => {
    req.header( "X-Admin-Token", adminToken );
} );

// Execute if value is null
request.ifNull( customTimeout, ( req ) => {
    req.timeout( 30 );  // Use default
} );

// Execute if value is not null
request.ifNotNull( authToken, ( req ) => {
    req.header( "Authorization", "Bearer " & authToken );
} );

result = request.send();
```

### Streaming and Callbacks

**New in BoxLang 1.8.0** - Stream responses with callbacks:

```js
http( "https://api.example.com/large-file" )
    .onRequestStart( () => {
        println( "Request starting..." );
    } )
    .onChunk( ( chunk, httpResult, httpClient, response ) => {
        println( "Received chunk: " & len( chunk ) & " bytes" );
        // Process chunk data
    } )
    .onComplete( ( httpResult ) => {
        println( "Request completed. Status: " & httpResult.statusCode );
    } )
    .onError( ( error, httpResult ) => {
        println( "Error occurred: " & error.message );
    } )
    .send();
```

### Server-Sent Events (SSE) Consumption

**New in BoxLang 1.8.0** - Consume SSE streams:

```js
// Basic SSE consumption
http( "https://api.example.com/events" )
    .sse( true )
    .onChunk( ( event, lastEventId, httpResult, httpClient, response ) => {
        // event struct contains: data, event (type), id
        println( "Event: " & event.event );
        println( "Data: " & event.data );
        println( "ID: " & event.id );
        println( "Last Event ID: " & lastEventId );
    } )
    .send();

// AI streaming example
fullResponse = "";
http( "https://api.openai.com/v1/chat/completions" )
    .post()
    .header( "Authorization", "Bearer " & apiKey )
    .jsonBody( '{
        "model": "gpt-4",
        "messages": [{"role": "user", "content": "Tell me a story"}],
        "stream": true
    }' )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        if ( event.event == "message" ) {
            token = deserializeJSON( event.data ).choices[ 1 ].delta.content;
            fullResponse &= token;
            writeOutput( token );  // Stream to browser
            flush;
        }
    } )
    .onComplete( ( httpResult ) => {
        println( "\n\nFull response length: " & len( fullResponse ) );
    } )
    .send();
```

### Request Inspection

Debug your request before sending:

```js
requestDetails = http( "https://api.example.com/data" )
    .post()
    .header( "Content-Type", "application/json" )
    .jsonBody( '{"test":"data"}' )
    .inspect();  // Returns struct of request configuration

dump( requestDetails );
// Shows: method, url, headers, params, timeout, etc.
```

### Error Handling

```js
try {
    result = http( "https://api.example.com/data" )
        .throwOnError( true )  // Throws on 4xx/5xx
        .send();

    println( "Success: " & result.fileContent );
} catch ( any e ) {
    println( "Error: " & e.message );
}

// Or check result manually
result = http( "https://api.example.com/data" )
    .throwOnError( false )
    .send();

if ( result.statusCode >= 400 ) {
    println( "Error: " & result.statusCode );
} else {
    println( "Success: " & result.fileContent );
}
```

</details>

---

<details>
<summary>Server-Sent Events (SSE) Consumption</summary>

**New in BoxLang 1.8.0** - Both the `http()` BIF and `bx:http` component support consuming Server-Sent Events (SSE) streams from remote servers.

### What is SSE Consumption?

While the `SSE()` BIF creates SSE streams (server-to-client), SSE consumption allows you to **connect to existing SSE endpoints** and process events as they arrive. This is perfect for:

- 🤖 Consuming AI streaming APIs (OpenAI, Claude, etc.)
- 📊 Real-time dashboard data feeds
- 🔔 Event notifications from third-party services
- 📈 Live metrics and monitoring streams
- 🔄 Real-time updates from microservices

### Using the `http()` BIF for SSE

```js
// Basic SSE consumption
http( "https://api.example.com/events" )
    .sse( true )
    .onChunk( ( event, lastEventId, httpResult, httpClient, response ) => {
        // event struct contains:
        // - data: The event data
        // - event: Event type (e.g., "message", "update", "ping")
        // - id: Event ID for reconnection

        println( "Received event type: " & event.event );
        println( "Event data: " & event.data );
        println( "Event ID: " & event.id );
    } )
    .send();
```

### Using the `bx:http` Component for SSE

```js
// Declare callback function
function processEvent( event, lastEventId, httpResult, httpClient, response ) {
    println( "Event: " & event.event );
    println( "Data: " & event.data );
}

// Use component with SSE
bx:http
    url="https://api.example.com/events"
    sse=true
    onChunk=processEvent
    result="result";
```

### Real-World SSE Examples

#### OpenAI Streaming Chat

```js
// Stream AI responses token-by-token
fullResponse = "";

http( "https://api.openai.com/v1/chat/completions" )
    .post()
    .header( "Authorization", "Bearer " & apiKey )
    .header( "Content-Type", "application/json" )
    .jsonBody( '{
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain quantum computing"}
        ],
        "stream": true
    }' )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        if ( event.data == "[DONE]" ) {
            return;  // Stream complete
        }

        try {
            chunk = deserializeJSON( event.data );
            if ( structKeyExists( chunk.choices[ 1 ].delta, "content" ) ) {
                token = chunk.choices[ 1 ].delta.content;
                fullResponse &= token;
                writeOutput( token );  // Stream to browser
                flush;
            }
        } catch ( any e ) {
            // Handle parse errors
        }
    } )
    .onComplete( ( httpResult ) => {
        println( "\n\nStream complete. Total tokens: " & len( fullResponse ) );
    } )
    .onError( ( error, httpResult ) => {
        println( "Error: " & error.message );
    } )
    .send();
```

#### Live Dashboard Metrics

```js
// Consume real-time metrics feed
http( "https://metrics.example.com/stream" )
    .header( "Authorization", "Bearer " & metricsToken )
    .sse( true )
    .onChunk( ( event, lastEventId, httpResult ) => {
        if ( event.event == "metrics" ) {
            metrics = deserializeJSON( event.data );

            // Update dashboard
            updateDashboard( {
                cpu: metrics.cpu,
                memory: metrics.memory,
                requests: metrics.requestsPerSecond,
                lastUpdate: now()
            } );
        }
    } )
    .send();
```

#### Real-Time Notifications

```js
// Listen for notification events
http( "https://notifications.example.com/stream" )
    .header( "X-User-ID", userID )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        switch ( event.event ) {
            case "notification":
                notification = deserializeJSON( event.data );
                showNotification( notification.title, notification.body );
                break;

            case "badge-update":
                badgeData = deserializeJSON( event.data );
                updateBadgeCount( badgeData.count );
                break;

            case "ping":
                // Keep-alive event, do nothing
                break;
        }

        // Store last event ID for reconnection
        session.lastEventId = lastEventId;
    } )
    .onError( ( error, httpResult ) => {
        // Reconnect with last event ID
        reconnectSSE( session.lastEventId );
    } )
    .send();
```

### SSE Event Structure

Each SSE event received in the `onChunk` callback contains:

```js
{
    data: "Event data content",        // The event payload
    event: "message",                  // Event type (default: "message")
    id: "123",                         // Event ID (for reconnection)
    retry: 3000                        // Retry interval in ms (if specified)
}
```

### SSE Callback Parameters

The `onChunk` callback for SSE receives:

| Parameter | Type | Description |
|-----------|------|-------------|
| `event` | struct | The SSE event structure (data, event, id, retry) |
| `lastEventId` | string | The most recent event ID received (for reconnection) |
| `httpResult` | struct | The HTTP result structure |
| `httpClient` | object | The BoxHttpClient instance |
| `response` | object | The raw Java HttpResponse object |

### SSE Best Practices

{% hint style="success" %}
**Best Practices:**

1. **Always handle errors** - Network issues can interrupt streams
2. **Store `lastEventId`** - Use it to reconnect and resume from last event
3. **Parse event types** - Different event types may need different handling
4. **Handle `[DONE]` signals** - Many APIs use this to indicate stream end
5. **Set appropriate timeouts** - SSE streams can be long-lived
6. **Flush output immediately** - For real-time display to end users
7. **Use try-catch** - JSON parsing of event data can fail
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

- SSE connections are **unidirectional** (server → client)
- Network interruptions will terminate the stream
- Use `lastEventId` to resume from where you left off
- Some proxies/firewalls may interfere with long-lived connections
- Set appropriate timeouts for long-running streams
- Memory usage grows with accumulated data - process and discard chunks promptly
{% endhint %}

</details>

---

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

<details>
<summary>Troubleshooting</summary>

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

</details>

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
