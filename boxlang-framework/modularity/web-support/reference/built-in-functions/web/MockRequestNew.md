[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `MockRequestNew`

Creates a new mock request builder for fluent configuration. This function allows you to configure the request step-by-step using fluent methods before executing it.

This is the recommended approach when you need fine-grained control over request configuration or want to set up complex request scenarios.

## Method Signature

```
MockRequestNew(webroot=[string], host=[string], port=[numeric], secure=[boolean], method=[string], path=[string], body=[string], contentType=[string], headers=[struct], urlScope=[struct], formScope=[struct], cookieScope=[struct])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `webroot` | `string` | `false` | The webroot to use for the mock server | Module setting |
| `host` | `string` | `false` | The host to use for the mock server | Module setting (localhost) |
| `port` | `numeric` | `false` | The port to use for the mock server | Module setting (8080) |
| `secure` | `boolean` | `false` | Whether the mock server should be secure (HTTPS) | Module setting (false) |
| `method` | `string` | `false` | The HTTP method | `GET` |
| `path` | `string` | `false` | The request path | `/` |
| `body` | `string` | `false` | The request body | Empty string |
| `contentType` | `string` | `false` | The content type | `text/html` |
| `headers` | `struct` | `false` | Request headers | Empty struct |
| `urlScope` | `struct` | `false` | URL parameters (query string) | Empty struct |
| `formScope` | `struct` | `false` | Form parameters | Empty struct |
| `cookieScope` | `struct` | `false` | Cookies | Empty struct |

## Examples

### Basic Builder Pattern

```js
// Create request with fluent API
mockRequest = mockRequestNew()
    .setRequestMethod( "POST" )
    .setRequestPath( "/api/users" )
    .setRequestBodyJSON( { "name": "John", "age": 30 } )
    .addRequestHeader( "Authorization", "Bearer token123" )
    .addURLParam( "debug", true );

// Execute when ready
mockRequest.execute();
```

### Inline Configuration

```js
// Configure request with initial parameters
mockRequest = mockRequestNew(
    method: "PUT",
    path: "/api/users/123",
    contentType: "application/json",
    body: '{"name": "Jane Doe", "email": "jane@example.com"}',
    headers: {
        "Authorization": "Bearer token456",
        "X-Request-ID": "abc-123"
    }
);

// Execute immediately
mockRequest.execute();
```

### Complex Request Setup

```js
// Build complex request step-by-step
mockRequest = mockRequestNew()
    .setRequestMethod( "POST" )
    .setRequestPath( "/api/orders" )
    .setRequestContentType( "application/json" )
    .setRequestBody( '{"product": "Widget", "quantity": 5}' )
    .addRequestHeader( "Content-Type", "application/json" )
    .addRequestHeader( "Accept", "application/json" )
    .addRequestHeader( "Authorization", "Bearer xyz789" )
    .addURLParam( "locale", "en-US" )
    .addURLParam( "currency", "USD" )
    .addFormField( "orderId", "ORD-001" )
    .addRequestCookie( "sessionId", "sess123" )
    .addRequestCookie( "preferences", "dark-mode" );

// Execute and get result
result = mockRequest.execute();

// Inspect response
httpData = getHTTPRequestData();
println( "Method: #httpData.method#" );
println( "Headers: #httpData.headers#" );
```

### Testing Multiple Requests

```js
// Create and execute multiple requests
request1 = mockRequestNew( method: "GET", path: "/api/users" ).execute();
request2 = mockRequestNew( method: "POST", path: "/api/users", body: '{"name":"Test"}' ).execute();
request3 = mockRequestNew( method: "DELETE", path: "/api/users/123" ).execute();
```

### Chaining with Execute

```js
// Chain configuration and execution in one statement
mockRequestNew(
    method: "POST",
    path: "/api/test",
    headers: {
        "Content-Type": "application/json",
        "X-Test-Header": "TestValue"
    },
    body: '{"name": "BoxLang", "type": "test"}'
).execute();

// Now use web-aware BIFs
httpData = getHTTPRequestData();
println( "Request Method: #httpData.method#" );
```

## Related

* [MockServerGet](./MockServerGet.md)
* [MockRequestRun](./MockRequestRun.md)
* [GetHTTPRequestData](./GetHTTPRequestData.md)
* [Forward](./Forward.md)
