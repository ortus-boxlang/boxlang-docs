[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `MockRequestRun`

Handles the start of a mock request by executing a full web request simulation. This BIF sets up the mock server with the provided request and response parameters, executes the request, and returns the configured MockHTTPExchange instance so you can inspect the response.

This is a convenience function that combines server creation, request configuration, and execution in a single call.

## Method Signature

```
MockRequestRun(path=[string], method=[string], pathInfo=[string], queryString=[string], contentType=[string], body=[string], urlScope=[struct], formScope=[struct], cookieScope=[struct], headers=[struct], responseStatus=[numeric], responseContentType=[string], responseBody=[string], responseHeaders=[struct], webroot=[string], host=[string], port=[numeric], secure=[boolean], force=[boolean])
```

### Arguments

#### Request Settings

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `false` | The request path | `/` |
| `method` | `string` | `false` | The HTTP method (GET, POST, PUT, DELETE, etc.) | `GET` |
| `pathInfo` | `string` | `false` | The path info | Empty string |
| `queryString` | `string` | `false` | The query string | Empty string |
| `contentType` | `string` | `false` | The content type | `text/html` |
| `body` | `string` | `false` | The request body | Empty string |
| `urlScope` | `struct` | `false` | URL parameters | Empty struct |
| `formScope` | `struct` | `false` | Form parameters | Empty struct |
| `cookieScope` | `struct` | `false` | Cookies | Empty struct |
| `headers` | `struct` | `false` | Request headers | Empty struct |

#### Response Mock Settings

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `responseStatus` | `numeric` | `false` | Expected response status | `200` |
| `responseContentType` | `string` | `false` | Expected response content type | `text/html` |
| `responseBody` | `string` | `false` | Expected response body | Empty string |
| `responseHeaders` | `struct` | `false` | Expected response headers | Empty struct |

#### Web Server Settings

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `webroot` | `string` | `false` | The webroot path | Module setting |
| `host` | `string` | `false` | The host name | Module setting (localhost) |
| `port` | `numeric` | `false` | The port number | Module setting (8080) |
| `secure` | `boolean` | `false` | Whether to use HTTPS | Module setting (false) |
| `force` | `boolean` | `false` | Force creation of new mock server | `false` |

## Examples

### Simple GET Request

```js
// Execute a simple GET request
mockResponse = mockRequestRun( path: "/api/users" );

// Inspect the response
status = mockResponse.getResponseStatus();
println( "Response Status: #status#" );
```

### POST Request with JSON Body

```js
// Execute POST request with JSON data
mockResponse = mockRequestRun(
    path: "/api/data",
    method: "POST",
    body: '{"key":"value"}',
    contentType: "application/json",
    responseStatus: 201,
    responseBody: '{"success":true}'
);

// Inspect the response
status = mockResponse.getResponseStatus();
body = mockResponse.getResponseBody();
headers = mockResponse.getMockResponseHeaders();

println( "Status: #status#" );
println( "Body: #body#" );
```

### Request with Headers and Cookies

```js
// Execute request with authentication
mockResponse = mockRequestRun(
    path: "/api/protected",
    method: "GET",
    headers: {
        "Authorization": "Bearer token123",
        "X-API-Key": "abc-xyz-789"
    },
    cookieScope: {
        "sessionId": "sess-456",
        "preferences": "dark-mode"
    }
);
```

### Form Submission

```js
// Simulate form POST
mockResponse = mockRequestRun(
    path: "/contact",
    method: "POST",
    contentType: "application/x-www-form-urlencoded",
    formScope: {
        "name": "John Doe",
        "email": "john@example.com",
        "message": "Hello World"
    }
);
```

### Complex Request with URL Parameters

```js
// Request with query string and URL parameters
mockResponse = mockRequestRun(
    path: "/search",
    method: "GET",
    queryString: "q=boxlang&page=1",
    urlScope: {
        "filter": "recent",
        "sort": "desc",
        "limit": 20
    },
    headers: {
        "Accept": "application/json",
        "User-Agent": "BoxLang Test Client"
    }
);

// Access request data
httpData = getHTTPRequestData();
println( "Request Method: #httpData.method#" );
println( "Headers: #httpData.headers#" );
```

### Mocking Response Data

```js
// Mock complete request/response cycle
mockResponse = mockRequestRun(
    path: "/api/user/profile",
    method: "GET",
    headers: {
        "Authorization": "Bearer token123"
    },
    responseStatus: 200,
    responseContentType: "application/json",
    responseBody: '{"id": 1, "name": "John Doe", "role": "admin"}',
    responseHeaders: {
        "X-RateLimit-Remaining": "99",
        "X-Response-Time": "12ms"
    }
);

// Inspect mocked response
status = mockResponse.getResponseStatus();
body = mockResponse.getResponseBody();
headers = mockResponse.getMockResponseHeaders();

println( "Status: #status#" );
println( "Body: #body#" );
println( "Rate Limit: #headers['X-RateLimit-Remaining']#" );
```

### Testing Different HTTP Methods

```js
// Test GET
getResponse = mockRequestRun( path: "/api/users", method: "GET" );

// Test POST
postResponse = mockRequestRun(
    path: "/api/users",
    method: "POST",
    body: '{"name": "New User"}',
    contentType: "application/json"
);

// Test PUT
putResponse = mockRequestRun(
    path: "/api/users/123",
    method: "PUT",
    body: '{"name": "Updated User"}',
    contentType: "application/json"
);

// Test DELETE
deleteResponse = mockRequestRun( path: "/api/users/123", method: "DELETE" );
```

## Related

* [MockServerGet](./MockServerGet.md)
* [MockRequestNew](./MockRequestNew.md)
* [GetHTTPRequestData](./GetHTTPRequestData.md)
* [Forward](./Forward.md)
