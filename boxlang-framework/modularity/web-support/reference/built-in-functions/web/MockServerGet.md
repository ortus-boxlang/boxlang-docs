[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `MockServerGet`

Creates a new mock server and stores it in the request context. If it exists already, it will return the existing one unless `force=true` is specified.

This function is useful for testing web applications by creating a mock HTTP exchange that simulates web server behavior without requiring an actual web server.

## Method Signature

```
MockServerGet(webroot=[string], host=[string], port=[numeric], secure=[boolean], force=[boolean])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `webroot` | `string` | `false` | The webroot to use for the mock server | Module setting |
| `host` | `string` | `false` | The host to use for the mock server | Module setting (localhost) |
| `port` | `numeric` | `false` | The port to use for the mock server | Module setting (8080) |
| `secure` | `boolean` | `false` | Whether the mock server should be secure (HTTPS) | Module setting (false) |
| `force` | `boolean` | `false` | Whether to force the creation of a new mock server | `false` |

## Examples

### Basic Usage

```js
// Get or create a mock server with default settings
mockServer = mockServerGet();

// Access server properties
println( "Host: #mockServer.getRequestServerName()#" );
println( "Port: #mockServer.getRequestServerPort()#" );
```

### Custom Configuration

```js
// Create a mock server with custom settings
mockServer = mockServerGet(
    host: "example.com",
    port: 9090,
    secure: true,
    force: true  // Force new instance
);
```

### Using Fluent API

```js
// Get mock server and configure request
mockServer = mockServerGet()
    .setRequestMethod( "POST" )
    .setRequestPath( "/api/users" )
    .addRequestHeader( "Content-Type", "application/json" )
    .setRequestBody( '{"name": "John Doe"}' );
```

### Caching Behavior

```js
// First call creates the server
server1 = mockServerGet();

// Second call returns cached instance
server2 = mockServerGet();

println( server1.hashCode() == server2.hashCode() );  // true

// Force new instance
server3 = mockServerGet( force: true );
println( server1.hashCode() == server3.hashCode() );  // false
```

## Related

* [MockRequestNew](./MockRequestNew.md)
* [MockRequestRun](./MockRequestRun.md)
* [GetHTTPRequestData](./GetHTTPRequestData.md)
* [Forward](./Forward.md)
