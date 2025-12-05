---
description: Real-time server-to-client event streaming and consumption for building AI agents, live dashboards, and real-time notifications
icon: satellite-dish
---

# Server-Sent Events (SSE)

**New in BoxLang 1.7.0** - Server-Sent Events (SSE) enable real-time, unidirectional event streaming over HTTP. BoxLang provides **two powerful SSE capabilities**:

1. **SSE Creation** (`SSE()` BIF) - Push events from your BoxLang server to clients
2. **SSE Consumption** (`http()` BIF / `bx:http` component) - Connect to and consume SSE streams from remote servers (**New in BoxLang 1.8.0**)

## 🌐 What are Server-Sent Events?

Server-Sent Events is a standard web technology that allows servers to push data to web clients over HTTP. Unlike WebSockets (which are bidirectional), SSE provides a simple, efficient one-way communication channel, perfect for:

* **AI Agent Streaming** - Stream AI responses token-by-token for better UX (creation & consumption)
* **Live Dashboards** - Push real-time metrics and updates to dashboards (creation & consumption)
* **Progressive Loading** - Load and display content as it becomes available (creation)
* **Real-Time Notifications** - Push notifications without polling (creation)
* **Log Streaming** - Stream server logs to browser console (creation)
* **Status Updates** - Track long-running processes in real-time (creation & consumption)
* **Consuming Third-Party Streams** - Connect to AI APIs (OpenAI, Claude), monitoring services, event feeds (consumption)

---

## 🔄 SSE Creation vs Consumption

BoxLang provides both sides of the SSE equation:

### SSE Creation - `SSE()` BIF

**Create SSE streams** that push events to web browsers and clients:

```js
// Server endpoint: /api/stream
SSE( ( emitter ) => {
    emitter.send( "Hello from server!" );
    emitter.send( { status: "processing" }, "update" );
    emitter.close();
} );
```

**Use cases:**

- Push real-time updates to your web UI
- Stream AI responses from your BoxLang backend
- Build live dashboards
- Send notifications to connected clients

### SSE Consumption - `http()` BIF / `bx:http` Component

**New in BoxLang 1.8.0** - **Consume SSE streams** from remote servers:

```js
// Connect to external SSE endpoint
http( "https://api.openai.com/v1/chat/completions" )
    .post()
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        println( "Received: " & event.data );
    } )
    .send();
```

**Use cases:**

- Consume AI streaming APIs (OpenAI, Claude, Gemini)
- Connect to real-time monitoring feeds
- Subscribe to third-party event streams
- Integrate with microservices using SSE

---

## 📋 SSE() BIF - Creating Streams

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

---

## 📥 SSE Consumption - Connecting to Remote Streams

**New in BoxLang 1.8.0** - BoxLang now provides built-in support for **consuming Server-Sent Events** from remote servers using the `http()` BIF or `bx:http` component.

### Why Consume SSE?

SSE consumption allows you to connect to external SSE endpoints and process events in real-time:

* 🤖 **AI Streaming APIs** - Consume token-by-token responses from OpenAI, Claude, Gemini, and other AI services
* 📊 **Real-Time Data Feeds** - Connect to stock tickers, weather updates, sports scores
* 🔔 **Event Notifications** - Subscribe to third-party notification services
* 📈 **Monitoring Services** - Receive alerts and metrics from monitoring platforms
* 🔄 **Microservices** - Integrate with SSE-based microservices architecture

### Basic SSE Consumption

#### Using the `http()` BIF

```js
// Connect to SSE endpoint
http( "https://api.example.com/events" )
    .sse( true )
    .onChunk( ( event, lastEventId, httpResult, httpClient, response ) => {
        // Process each SSE event as it arrives
        println( "Event Type: " & event.event );
        println( "Event Data: " & event.data );
        println( "Event ID: " & event.id );
        println( "Last Event ID: " & lastEventId );
    } )
    .send();
```

#### Using the `bx:http` Component

```js
// Define callback function
function handleSSEEvent( event, lastEventId, httpResult, httpClient, response ) {
    println( "Received: " & event.event & " - " & event.data );
}

// Use component with SSE
bx:http
    url="https://api.example.com/events"
    sse=true
    onChunk=handleSSEEvent
    result="result";
```

### SSE Event Structure

Each event received in the `onChunk` callback contains:

```js
{
    data: "Event payload content",
    event: "message",              // Event type (default: "message")
    id: "123",                     // Event ID for reconnection
    retry: 3000                    // Retry interval in ms (optional)
}
```

### Callback Parameters

The `onChunk` callback receives five parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `event` | struct | The SSE event (data, event, id, retry) |
| `lastEventId` | string | Most recent event ID (for reconnection) |
| `httpResult` | struct | HTTP result structure |
| `httpClient` | object | BoxHttpClient instance |
| `response` | object | Raw Java HttpResponse |

### Real-World SSE Consumption Examples

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
            {"role": "user", "content": "' & userPrompt & '"}
        ],
        "stream": true
    }' )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        // OpenAI sends "[DONE]" when stream completes
        if ( event.data == "[DONE]" ) {
            return;
        }

        try {
            chunk = deserializeJSON( event.data );
            if ( structKeyExists( chunk.choices[1].delta, "content" ) ) {
                token = chunk.choices[1].delta.content;
                fullResponse &= token;

                // Stream to client in real-time
                writeOutput( token );
                flush;
            }
        } catch ( any e ) {
            // Handle parsing errors
            logger.error( "Error parsing SSE chunk", e );
        }
    } )
    .onComplete( ( httpResult ) => {
        logger.info( "Stream complete. Tokens received: " & len( fullResponse ) );
    } )
    .onError( ( error, httpResult ) => {
        logger.error( "SSE stream error: " & error.message );
    } )
    .send();

println( "\n\nComplete response: " & fullResponse );
```

#### Claude AI Streaming

```js
// Consume Claude streaming API
fullResponse = "";

http( "https://api.anthropic.com/v1/messages" )
    .post()
    .header( "x-api-key", claudeApiKey )
    .header( "anthropic-version", "2023-06-01" )
    .header( "content-type", "application/json" )
    .jsonBody( '{
        "model": "claude-3-opus-20240229",
        "messages": [
            {"role": "user", "content": "' & userPrompt & '"}
        ],
        "max_tokens": 1024,
        "stream": true
    }' )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        if ( event.event == "content_block_delta" ) {
            data = deserializeJSON( event.data );
            token = data.delta.text;
            fullResponse &= token;
            writeOutput( token );
            flush;
        }
    } )
    .send();
```

#### Real-Time Stock Quotes

```js
// Consume live stock price feed
http( "https://stockstream.example.com/quotes?symbols=AAPL,GOOGL,MSFT" )
    .header( "Authorization", "Bearer " & stockAPIKey )
    .sse( true )
    .onChunk( ( event, lastEventId, httpResult ) => {
        if ( event.event == "quote" ) {
            quote = deserializeJSON( event.data );

            // Update database or cache
            cacheSet(
                "stock_" & quote.symbol,
                quote,
                createTimeSpan( 0, 0, 0, 10 ) // 10 seconds
            );

            // Broadcast to connected WebSocket clients
            broadcastStockUpdate( {
                symbol: quote.symbol,
                price: quote.price,
                change: quote.change,
                percentChange: quote.percentChange,
                timestamp: quote.timestamp
            } );
        }
    } )
    .onError( ( error, httpResult ) => {
        logger.error( "Stock stream disconnected, reconnecting..." );
        reconnectStockStream();
    } )
    .send();
```

#### Server Monitoring Feed

```js
// Consume monitoring metrics stream
http( "https://monitoring.example.com/metrics/stream" )
    .header( "X-API-Key", monitoringAPIKey )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        switch ( event.event ) {
            case "metric":
                metric = deserializeJSON( event.data );

                // Store in time-series database
                influxDB.write( {
                    measurement: metric.name,
                    tags: metric.tags,
                    fields: { value: metric.value },
                    timestamp: metric.timestamp
                } );

                // Check thresholds
                if ( metric.value > metric.threshold ) {
                    sendAlert( "Metric " & metric.name & " exceeded threshold" );
                }
                break;

            case "alert":
                alert = deserializeJSON( event.data );
                handleAlert( alert );
                break;

            case "heartbeat":
                // Update last seen timestamp
                session.lastHeartbeat = now();
                break;
        }
    } )
    .onComplete( ( httpResult ) => {
        logger.info( "Monitoring stream closed" );
    } )
    .send();
```

#### GitHub Events Stream

```js
// Monitor GitHub repository events
http( "https://api.github.com/repos/ortus-boxlang/boxlang/events" )
    .header( "Accept", "text/event-stream" )
    .header( "Authorization", "Bearer " & githubToken )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        if ( event.event == "push" ) {
            pushEvent = deserializeJSON( event.data );

            // Notify team
            slackNotify( {
                channel: "#github",
                message: "New push to " & pushEvent.ref & " by " & pushEvent.pusher.name,
                commits: pushEvent.commits.len()
            } );

            // Trigger CI/CD
            if ( pushEvent.ref == "refs/heads/main" ) {
                triggerBuild( pushEvent.after );
            }
        }
    } )
    .send();
```

### Advanced SSE Consumption Patterns

#### Reconnection with Last Event ID

```js
// Store last event ID for reconnection
application.lastEventId = "";

function connectToSSE() {
    request = http( "https://api.example.com/events" );

    // Resume from last event if we have one
    if ( len( application.lastEventId ) ) {
        request.header( "Last-Event-ID", application.lastEventId );
    }

    request
        .sse( true )
        .onChunk( ( event, lastEventId ) => {
            // Store last event ID
            application.lastEventId = lastEventId;

            // Process event
            processEvent( event );
        } )
        .onError( ( error, httpResult ) => {
            logger.error( "Connection lost, reconnecting in 5 seconds..." );
            sleep( 5000 );
            connectToSSE();  // Reconnect with Last-Event-ID
        } )
        .send();
}

// Start connection
connectToSSE();
```

#### Multiple Event Types

```js
// Handle different event types
http( "https://api.example.com/events" )
    .sse( true )
    .onChunk( ( event, lastEventId ) => {
        switch ( event.event ) {
            case "message":
                handleMessage( deserializeJSON( event.data ) );
                break;

            case "notification":
                handleNotification( deserializeJSON( event.data ) );
                break;

            case "update":
                handleUpdate( deserializeJSON( event.data ) );
                break;

            case "ping":
                // Keep-alive ping, do nothing
                break;

            default:
                logger.warn( "Unknown event type: " & event.event );
        }
    } )
    .send();
```

#### Timeout and Error Handling

```js
// Robust SSE connection with comprehensive error handling
http( "https://api.example.com/events" )
    .timeout( 300 )  // 5 minute timeout
    .sse( true )
    .onRequestStart( () => {
        logger.info( "Connecting to SSE stream..." );
    } )
    .onChunk( ( event, lastEventId, httpResult ) => {
        try {
            processEvent( event );
        } catch ( any e ) {
            logger.error( "Error processing event", e );
            // Don't let one bad event break the stream
        }
    } )
    .onError( ( error, httpResult ) => {
        logger.error( "SSE error: " & error.message );

        // Decide whether to retry based on error type
        if ( httpResult.statusCode == 429 ) {
            // Rate limited, wait before retry
            sleep( 60000 );
            retryConnection();
        } else if ( httpResult.statusCode >= 500 ) {
            // Server error, retry with exponential backoff
            sleep( retryDelay );
            retryDelay *= 2;  // Double delay each time
            retryConnection();
        } else {
            // Client error, don't retry
            logger.error( "Client error, not retrying: " & httpResult.statusCode );
        }
    } )
    .onComplete( ( httpResult ) => {
        logger.info( "SSE stream completed normally" );
    } )
    .send();
```

### SSE Consumption Best Practices

{% hint style="success" %}
**Best Practices for SSE Consumption:**

1. **Always handle errors** - Network failures will interrupt streams
2. **Store `lastEventId`** - Use it to reconnect and resume from last event
3. **Implement reconnection logic** - Connections will drop, be ready to reconnect
4. **Parse event types** - Different event types require different handling
5. **Handle stream termination signals** - Look for `[DONE]`, empty data, or specific event types
6. **Set appropriate timeouts** - Long-lived streams need longer timeouts
7. **Use try-catch for parsing** - JSON parsing can fail on malformed data
8. **Log connection state** - Track connects, disconnects, and errors
9. **Implement exponential backoff** - Don't hammer failing endpoints
10. **Monitor memory usage** - Accumulating data can grow quickly
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

- **Unidirectional** - SSE is server → client only (no client → server messages)
- **Network sensitive** - Interruptions terminate the stream
- **Proxy buffering** - Some proxies buffer responses (check your infrastructure)
- **Browser connection limits** - Browsers limit concurrent SSE connections (typically 6 per domain)
- **Long-lived connections** - Consumes server resources, monitor connection count
- **Error handling is critical** - Always implement robust retry logic
- **Memory management** - Process and discard events, don't accumulate indefinitely
- **Authentication** - Include proper API keys/tokens in headers
{% endhint %}

---

## 🎯 Summary

Server-Sent Events in BoxLang provides a powerful, standards-based way to build real-time web applications with minimal complexity:

- **SSE Creation** (`SSE()` BIF) - Push events from BoxLang to web clients with automatic connection management, keep-alive, and client disconnect detection
- **SSE Consumption** (`http()` BIF / `bx:http` component) - Connect to and consume SSE streams from remote servers with built-in event parsing, reconnection support, and error handling

Whether you're building real-time dashboards, streaming AI responses, or integrating with third-party event feeds, BoxLang's SSE support makes it easy to create robust streaming experiences.
