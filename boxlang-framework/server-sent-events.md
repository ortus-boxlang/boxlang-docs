---
description: Real-time server-to-client event streaming for building AI agents, live dashboards, and real-time notifications
icon: satellite-dish
---

# Server-Sent Events (SSE)

**New in BoxLang 1.7.0** - Server-Sent Events (SSE) enable real-time, unidirectional server-to-client event streaming over HTTP. The `SSE()` BIF and Emitter API provide a simple yet powerful way to build AI agents, live dashboards, progressive loading experiences, and real-time notifications in web applications.

## 🌐 What are Server-Sent Events?

Server-Sent Events is a standard web technology that allows servers to push data to web clients over HTTP. Unlike WebSockets (which are bidirectional), SSE provides a simple, efficient one-way communication channel from server to client, perfect for:

* **AI Agent Streaming** - Stream AI responses token-by-token for better UX
* **Live Dashboards** - Push real-time metrics and updates to dashboards
* **Progressive Loading** - Load and display content as it becomes available
* **Real-Time Notifications** - Push notifications without polling
* **Log Streaming** - Stream server logs to browser console
* **Status Updates** - Track long-running processes in real-time

## 📋 SSE() BIF

The `SSE()` function establishes a Server-Sent Events connection and streams data to the client.

### Syntax

```js
SSE(
    callback: function,
    async: boolean = false,
    retry: number = 0,
    keepAliveInterval: number = 0,
    timeout: number = 0,
    cors: string = ""
)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `callback` | function | Yes | - | Closure/lambda that receives the emitter object for sending events |
| `async` | boolean | No | `false` | Run callback in background thread (non-blocking) |
| `retry` | number | No | `0` | Client reconnect interval in milliseconds (0 = no reconnect) |
| `keepAliveInterval` | number | No | `0` | Auto-send keep-alive comments interval in milliseconds (0 = disabled) |
| `timeout` | number | No | `0` | Maximum execution time for async mode in milliseconds (0 = no timeout) |
| `cors` | string | No | `""` | CORS origin header (`*` for all origins, specific domain, or empty for none) |

### Emitter Methods

The callback function receives an `emitter` object with the following methods:

#### send( data, [event], [id] )

Send an SSE event to the client. Complex data is automatically serialized to JSON.

**Parameters:**

* `data` (required) - Data to send (string, number, struct, array, etc.)
* `event` (optional) - Event type/name for client-side filtering
* `id` (optional) - Event ID for client-side tracking

```js
emitter.send( "Simple message" );
emitter.send( { status: "processing", progress: 50 }, "update" );
emitter.send( { complete: true }, "done", 123 );
```

#### comment( text )

Send an SSE comment (not visible to client, used for keep-alive).

```js
emitter.comment( "Connection alive" );
```

#### close()

Gracefully close the SSE stream.

```js
emitter.close();
```

#### isClosed()

Check if the client has disconnected.

```js
if ( emitter.isClosed() ) {
    // Stop processing
    break;
}
```

## 💡 Usage Examples

### Basic Synchronous Streaming

```js
SSE( ( emitter ) => {
    emitter.send( "Hello from server!" );
    emitter.send( { status: "processing", progress: 25 }, "update" );
    emitter.send( { status: "processing", progress: 50 }, "update" );
    emitter.send( { status: "processing", progress: 75 }, "update" );
    emitter.send( { complete: true }, "done" );
    emitter.close();
} );
```

### AI Streaming with Async Execution

```js
// Stream AI responses token-by-token (non-blocking)
SSE(
    callback: ( emitter ) => {
        var response = openAI.chat( prompt: request.prompt );

        while ( !emitter.isClosed() && response.hasMoreTokens() ) {
            var token = response.getNextToken();
            emitter.send( token, "token" );

            // Optional: Add small delay for better client rendering
            sleep( 10 );
        }

        emitter.send( { complete: true, total: response.getTotalTokens() }, "done" );
    },
    async: true,
    keepAliveInterval: 30000,  // Keep-alive every 30s
    timeout: 300000            // 5 minute max timeout
);
```

### Cross-Origin Streaming

```js
// Enable CORS for cross-domain requests
SSE(
    callback: ( emitter ) => {
        emitter.send( { message: "Hello from API" }, "greeting", 1 );
        emitter.send( { data: "Cross-origin data" }, "data", 2 );
        emitter.close();
    },
    cors: "*"  // Allow all origins
);

// Or specify specific origin
SSE(
    callback: ( emitter ) => {
        emitter.send( { secure: "data" }, "secure" );
    },
    cors: "https://app.example.com"
);
```

### Live Dashboard Updates

```js
SSE(
    callback: ( emitter ) => {
        var startTime = now();
        var maxDuration = 3600000; // 1 hour

        while ( !emitter.isClosed() && ( now() - startTime ) < maxDuration ) {
            // Fetch current metrics
            var metrics = {
                cpu: getCPUUsage(),
                memory: getMemoryUsage(),
                requests: getRequestCount(),
                timestamp: now()
            };

            emitter.send( metrics, "metrics" );

            // Update every 5 seconds
            sleep( 5000 );
        }

        emitter.close();
    },
    async: true,
    keepAliveInterval: 30000,
    timeout: 3600000
);
```

### Progress Tracking

```js
SSE(
    callback: ( emitter ) => {
        var tasks = [ "Initialize", "Load Data", "Process", "Validate", "Complete" ];
        var totalTasks = tasks.len();

        tasks.each( ( task, index ) => {
            if ( emitter.isClosed() ) {
                return; // Client disconnected
            }

            emitter.send( {
                task: task,
                progress: ( index / totalTasks ) * 100,
                step: index,
                total: totalTasks
            }, "progress" );

            // Simulate task execution
            performTask( task );
        } );

        emitter.send( { complete: true }, "done" );
        emitter.close();
    },
    async: true
);
```

### Log Streaming

```js
SSE(
    callback: ( emitter ) => {
        var logFile = "/var/logs/app.log";
        var lastPosition = 0;

        while ( !emitter.isClosed() ) {
            // Read new log entries
            var newLogs = readLogsSince( logFile, lastPosition );

            if ( newLogs.len() > 0 ) {
                newLogs.each( ( logEntry ) => {
                    emitter.send( {
                        level: logEntry.level,
                        message: logEntry.message,
                        timestamp: logEntry.timestamp
                    }, "log" );
                } );

                lastPosition = getFilePosition( logFile );
            }

            // Check every second
            sleep( 1000 );
        }
    },
    async: true,
    keepAliveInterval: 15000,
    timeout: 0 // No timeout - keep streaming until client disconnects
);
```

### Real-Time Notifications

```js
SSE(
    callback: ( emitter ) => {
        var userId = session.userId;
        var lastCheck = now();

        while ( !emitter.isClosed() ) {
            // Check for new notifications
            var notifications = getNotificationsForUser( userId, lastCheck );

            notifications.each( ( notification ) => {
                emitter.send( {
                    id: notification.id,
                    type: notification.type,
                    title: notification.title,
                    message: notification.message,
                    timestamp: notification.created
                }, "notification" );
            } );

            lastCheck = now();

            // Check every 10 seconds
            sleep( 10000 );
        }
    },
    async: true,
    keepAliveInterval: 30000
);
```

## 🎨 Client-Side JavaScript

### Basic EventSource Usage

```js
// Connect to SSE endpoint
const eventSource = new EventSource('/api/sse/stream');

// Listen for default message events
eventSource.onmessage = function(event) {
    console.log('Received:', event.data);
    const data = JSON.parse(event.data);
    // Handle data
};

// Listen for specific event types
eventSource.addEventListener('update', function(event) {
    const data = JSON.parse(event.data);
    console.log('Update:', data);
});

eventSource.addEventListener('done', function(event) {
    console.log('Stream complete');
    eventSource.close();
});

// Handle errors
eventSource.onerror = function(error) {
    console.error('SSE Error:', error);
    eventSource.close();
};
```

### AI Streaming Example

```js
const eventSource = new EventSource('/api/ai/stream?prompt=' + encodeURIComponent(prompt));
let fullResponse = '';

eventSource.addEventListener('token', function(event) {
    const token = event.data;
    fullResponse += token;
    document.getElementById('response').textContent = fullResponse;
});

eventSource.addEventListener('done', function(event) {
    const data = JSON.parse(event.data);
    console.log('Complete! Total tokens:', data.total);
    eventSource.close();
});
```

### Dashboard Updates Example

```js
const eventSource = new EventSource('/api/metrics/stream');

eventSource.addEventListener('metrics', function(event) {
    const metrics = JSON.parse(event.data);

    // Update dashboard
    document.getElementById('cpu').textContent = metrics.cpu + '%';
    document.getElementById('memory').textContent = metrics.memory + 'MB';
    document.getElementById('requests').textContent = metrics.requests;
});
```

## ⚙️ Implementation Features

### Automatic First-Byte Flush

BoxLang's SSE implementation automatically flushes the first byte to establish the connection quickly, ensuring minimal latency before streaming begins.

### Large Data Chunking

Data larger than 32KB is automatically split into properly formatted SSE chunks, ensuring reliable delivery of large payloads.

### Multi-Line Data Support

Complex data with newlines is automatically formatted according to SSE specification with proper `data:` line prefixing.

### Client Disconnect Detection

The emitter automatically detects when clients disconnect, allowing your callback to gracefully stop processing with `emitter.isClosed()`.

### Proxy/Nginx Compatibility

Response headers are automatically configured to disable buffering in proxies (nginx, Apache) for true real-time delivery:

```
X-Accel-Buffering: no
Cache-Control: no-cache
```

### Keep-Alive Support

Configure automatic keep-alive comments to keep connections alive through proxies and firewalls:

```js
SSE(
    callback: ( emitter ) => {
        // Your streaming logic
    },
    keepAliveInterval: 30000 // Send keep-alive every 30s
);
```

## 🎯 Best Practices

{% hint style="success" %}
**When to Use SSE:**

* AI response streaming for better user experience
* Real-time dashboard updates
* Live log streaming
* Progress tracking for long-running operations
* Real-time notifications and alerts
* One-way server-to-client communication (server pushes data)
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

* Use `async: true` for long-running streams to avoid blocking request threads
* Set appropriate `timeout` values for async streams to prevent resource leaks
* Use `keepAliveInterval` for long-lived connections (30-60 seconds recommended)
* Check `emitter.isClosed()` frequently in loops to detect disconnects early
* Implement proper error handling in callback functions
* Consider rate limiting for high-frequency updates
* Use event types to allow client-side filtering
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

* **Browser Compatibility**: SSE is supported in all modern browsers (not IE11)
* **Connection Limits**: Browsers limit concurrent SSE connections (typically 6 per domain)
* **Reconnection**: Clients automatically reconnect - use `retry` parameter to control interval
* **Async Mode**: Always use `async: true` for streams lasting more than a few seconds
* **Resource Management**: Set `timeout` for async streams to prevent orphaned threads
* **Proxy Buffering**: Ensure proxies/CDNs don't buffer SSE responses (headers handled automatically)
* **Memory Usage**: Long-running streams consume server resources - monitor and limit as needed
* **Security**: Implement authentication/authorization before establishing SSE connections
{% endhint %}

## 🔒 Security Considerations

### Authentication

Always authenticate users before establishing SSE connections:

```js
// Check authentication first
if ( !session.isAuthenticated() ) {
    header statuscode="401" statustext="Unauthorized";
    writeOutput( "Not authenticated" );
    abort;
}

// Then establish SSE
SSE( callback: ( emitter ) => {
    var userId = session.userId;
    // Stream user-specific data
} );
```

### Authorization

Verify user permissions for the requested data stream:

```js
if ( !hasPermission( session.userId, "view_metrics" ) ) {
    header statuscode="403" statustext="Forbidden";
    writeOutput( "Access denied" );
    abort;
}

SSE( callback: ( emitter ) => {
    // Stream authorized metrics
} );
```

### CORS Configuration

Be specific with CORS origins in production:

```js
// Development: Allow all origins
SSE( callback: ( emitter ) => {
    // ...
}, cors: "*" );

// Production: Specify exact origin
SSE( callback: ( emitter ) => {
    // ...
}, cors: "https://app.example.com" );
```

### Rate Limiting

Implement rate limiting to prevent abuse:

```js
if ( !checkRateLimit( session.userId, "sse_connections" ) ) {
    header statuscode="429" statustext="Too Many Requests";
    writeOutput( "Rate limit exceeded" );
    abort;
}

SSE( callback: ( emitter ) => {
    // Stream data
} );
```

## 🔗 Related Resources

* [HTTP/S Calls](http-calls.md)
* [Asynchronous Programming](asynchronous-programming/)
* [BoxLang Web Runtime](../getting-started/running-boxlang/)
* [Release Notes 1.7.0](../readme/release-history/1.7.0.md)

## 📚 Additional Examples

### Multi-Channel Chat Streaming

```js
SSE(
    callback: ( emitter ) => {
        var channels = session.subscribedChannels;
        var lastMessageId = 0;

        while ( !emitter.isClosed() ) {
            // Fetch new messages across all subscribed channels
            var messages = getNewMessages( channels, lastMessageId );

            messages.each( ( message ) => {
                emitter.send( {
                    channel: message.channel,
                    user: message.user,
                    text: message.text,
                    timestamp: message.created
                }, "message", message.id );

                lastMessageId = max( lastMessageId, message.id );
            } );

            sleep( 1000 );
        }
    },
    async: true,
    keepAliveInterval: 30000,
    timeout: 7200000 // 2 hour max
);
```

### Stock Price Updates

```js
SSE(
    callback: ( emitter ) => {
        var symbols = url.symbols.listToArray(); // ["AAPL", "GOOGL", "MSFT"]

        while ( !emitter.isClosed() ) {
            symbols.each( ( symbol ) => {
                var price = getStockPrice( symbol );
                emitter.send( {
                    symbol: symbol,
                    price: price.current,
                    change: price.change,
                    percentChange: price.percentChange,
                    timestamp: now()
                }, "quote" );
            } );

            // Update every 5 seconds
            sleep( 5000 );
        }
    },
    async: true,
    keepAliveInterval: 30000
);
```

Server-Sent Events in BoxLang provides a powerful, standards-based way to build real-time web applications with minimal complexity. The automatic handling of connection management, keep-alive, and client disconnect detection makes it easy to create robust streaming experiences.
