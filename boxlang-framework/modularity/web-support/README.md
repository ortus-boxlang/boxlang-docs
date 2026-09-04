---
description: >-
  Mock HTTP exchanges for testing web applications in BoxLang CLI runtime without a web server.
icon: globe-pointer
---

# 🌐 BoxLang Web Support Module

Mock web server for testing BoxLang web applications in CLI runtime. Simulates HTTP requests/responses without needing an actual web server.

## ⚠️ Warning

**DO NOT install this module into a BoxLang web-runtime!** This module is for CLI runtime testing or mocking only and will cause JAR conflicts in web server environments. Not needed for CommandBox or MiniServer.

## 📦 Installation

```bash
# OS Quick Installer
install-bx-module bx-web-support

# CommandBox
box install bx-web-support
```

## ⚙️ Configuration

Configure in your `ModuleConfig.bx`:

```js
settings = {
    port       : 8080,                          // Mock server port
    host       : "localhost",                   // Mock server host
    webRoot    : server.java.executionPath,    // Web root path
    secure     : false,                         // Enable HTTPS
    requestKey : "bxMockServer"                 // Request scope key
};
```

## 🚀 Quick Start

```js
// Get mock server
mockServer = mockServerGet()
    .setRequestMethod( "POST" )
    .setRequestPath( "/api/users" )
    .addRequestHeader( "Content-Type", "application/json" )
    .setRequestBody( '{"name": "John"}' );

// Use web-aware BIFs
httpData = getHTTPRequestData();
println( httpData.method ); // POST
```

## 🔧 BIF Reference

### mockServerGet()

Creates or retrieves cached mock server exchange.

**Arguments:**

- `webroot` (string) - Web root path
- `host` (string) - Server host (default: localhost)
- `port` (numeric) - Server port (default: 8080)
- `secure` (boolean) - Enable HTTPS (default: false)
- `force` (boolean) - Force new instance (default: false)

**Returns:** `MockHTTPExchange`

```js
// Get or create server
server = mockServerGet();

// Force new instance
server = mockServerGet( force: true );

// Custom configuration
server = mockServerGet( host: "example.com", port: 9090, secure: true );
```

### mockRequestNew()

Creates mock request builder for fluent configuration.

**Arguments:**

- `method` (string) - HTTP method (default: GET)
- `path` (string) - Request path (default: /)
- `body` (string) - Request body
- `contentType` (string) - Content type (default: text/html)
- `headers` (struct) - Request headers
- `urlScope` (struct) - URL parameters
- `formScope` (struct) - Form fields
- `cookieScope` (struct) - Cookies
- Plus: `webroot`, `host`, `port`, `secure`

**Returns:** `MockHTTPExchange` (builder pattern)

```js
// Builder pattern
mockRequestNew()
    .setRequestMethod( "POST" )
    .setRequestBodyJSON( { name: "John" } )
    .addRequestHeader( "Authorization", "Bearer token" )
    .execute();

// Inline configuration
mockRequestNew(
    method: "PUT",
    path: "/api/users/123",
    body: '{"name": "Jane"}',
    headers: { "Authorization": "Bearer token" }
).execute();
```

### mockRequestRun()

Executes full mock request with all-in-one configuration.

**Arguments:**

- **Request:** `path`, `method`, `pathInfo`, `queryString`, `contentType`, `body`, `urlScope`, `formScope`, `cookieScope`, `headers`
- **Response:** `responseStatus`, `responseContentType`, `responseBody`, `responseHeaders`
- **Server:** `webroot`, `host`, `port`, `secure`, `force`

**Returns:** `MockHTTPExchange` (executed)

```js
// Simple request
mockRequestRun( path: "/api/users", method: "GET" );

// Complex request
mockRequestRun(
    path: "/api/data",
    method: "POST",
    body: '{"key": "value"}',
    contentType: "application/json",
    headers: { "Authorization": "Bearer token" },
    responseStatus: 201,
    responseBody: '{"success": true}'
);
```

## 💡 Examples

### Basic GET Request

```js
mockRequestRun( path: "/api/users" );
httpData = getHTTPRequestData();
println( httpData.method ); // GET
```

### POST with JSON

```js
mockRequestNew(
    method: "POST",
    path: "/api/users",
    contentType: "application/json",
    body: '{"name": "John", "email": "john@example.com"}'
).execute();
```

### Request with Authentication

```js
mockServer = mockServerGet()
    .setRequestMethod( "GET" )
    .setRequestPath( "/api/protected" )
    .addRequestHeader( "Authorization", "Bearer xyz789" )
    .addRequestCookie( "sessionId", "sess-123" );
```

### Form Submission

```js
mockRequestRun(
    path: "/contact",
    method: "POST",
    formScope: {
        name: "Jane Doe",
        email: "jane@example.com",
        message: "Hello!"
    }
);
```

## 🔗 Fluent API

`MockHTTPExchange` provides fluent methods for request configuration:

**Request Configuration:**

- `setRequestMethod(method)` - Set HTTP method
- `setRequestPath(path)` - Set request path
- `setRequestBody(body)` - Set request body
- `setRequestBodyJSON(struct)` - Set JSON body (auto content-type)
- `setRequestBodyXML(string)` - Set XML body (auto content-type)
- `setRequestContentType(type)` - Set content type

**Headers & Parameters:**

- `addRequestHeader(name, value)` - Add single header
- `addRequestHeaders(struct)` - Add multiple headers
- `addURLParam(name, value)` - Add URL parameter
- `addURLParams(struct)` - Add multiple URL parameters
- `addFormField(name, value)` - Add form field
- `addFormFields(struct)` - Add multiple form fields
- `addRequestCookie(name, value)` - Add cookie

**Execution & Inspection:**

- `execute()` - Execute the request
- `getResponseBody()` - Get response body
- `getResponseStatus()` - Get status code
- `getMockRequestHeaders()` - Get request headers
- `getMockResponseHeaders()` - Get response headers
- `getMockForm()` - Get form scope
- `getMockURL()` - Get URL scope

**Test Utilities:**

- `clearRequestData()` - Reset request data
- `clearResponseData()` - Reset response data
- `clearAll()` - Reset everything

## 🧪 Testing Patterns

### Test Isolation

```js
// Reset between tests
mockServer = mockServerGet();
mockServer.clearAll();

// Or force new instance
mockServer = mockServerGet( force: true );
```

### Multiple Requests

```js
// Test different methods
mockRequestNew( method: "GET", path: "/api/users" ).execute();
mockRequestNew( method: "POST", path: "/api/users", body: "{}" ).execute();
mockRequestNew( method: "DELETE", path: "/api/users/123" ).execute();
```

### Response Inspection

```js
mockServer = mockRequestRun(
    path: "/api/test",
    method: "POST",
    body: '{"test": true}'
);

// Inspect
status = mockServer.getResponseStatus();
body = mockServer.getResponseBody();
headers = mockServer.getMockResponseHeaders();
```

## 📚 Resources

- [GitHub Repository](https://github.com/ortus-boxlang/bx-web-support)
- [Issue Tracker](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359&components=27030&issuetype=1)
- [BoxLang Documentation](https://boxlang.io)
