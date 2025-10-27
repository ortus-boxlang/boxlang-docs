---
icon: bullhorn
description: Implement real-time messaging in BoxLang applications using Redis Publish/Subscribe.
---

# Publish/Subscribe

## What is Pub/Sub?

![Redis Pub/Sub Architecture](https://dingyuliang.me/wp-content/uploads/2018/02/redis-pubsub-768x407.png)

The Redis module provides native messaging capabilities through Redis Publish/Subscribe constructs. This allows your BoxLang applications to implement real-time messaging and event-driven architectures using Redis as the message broker.

{% embed url="https://redis.io/topics/pubsub" %}

> Redis Pub/Sub implements the Publish/Subscribe messaging paradigm. This decoupling of publishers and subscribers can allow for greater scalability and a more dynamic network topology.

**How it works:**

1. **Subscribers** express interest in one or more channels (literal channels or pattern channels)
2. **Publishers** send messages into channels
3. **Redis** pushes these messages to all subscribers that have matched the channel

## 📋 Pub/Sub BIFs Overview

The module provides two main functions for implementing pub/sub patterns:

| Function           | Parameters                            | Returns | Description                                                                                                                        |
| ------------------ | ------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `redisPublish()`   | `channel`, `message`, `cacheName`     | numeric | Publishes a message to a Redis channel. Returns the number of subscribers that received the message.                               |
| `redisSubscribe()` | `subscriber`, `channels`, `cacheName` | struct  | Subscribes to one or more channels using a closure/lambda or listener class. Returns a struct with `future` and `subscriber` keys. |

{% hint style="warning" %}
Pattern-based publishing and subscriptions are not yet implemented in this version.
{% endhint %}

## 📤 Publishing Messages

Use `redisPublish()` to send messages to a Redis channel. The function returns the number of subscribers that received the message.

### Function Signature

```javascript
numeric function redisPublish(
    required string channel,
    required any message,
    string cacheName = "default"
)
```

### Parameters

* **channel** - The Redis channel name to publish to
* **message** - The message content to send (will be serialized)
* **cacheName** - The name of the Redis cache connection to use (default: "default")

### Publishing Example

```javascript
// Publish messages to a channel
println( "<h2>Publishing messages...</h2>" );

// Publish single messages
var subscriberCount = redisPublish( "notifications", "System maintenance starting" );
println( "Message sent to #subscriberCount# subscriber(s)" );

redisPublish( "notifications", "Deployment complete" );
redisPublish( "notifications", "All systems operational" );

// Publish structured data
redisPublish( "user-events", {
    "event": "login",
    "userId": 12345,
    "timestamp": now()
} );

println( "<h2>Finished publishing messages</h2>" );
```

### Use Cases for Publishing

* **System notifications** - Broadcast status updates
* **Real-time updates** - Push data changes to connected clients
* **Event broadcasting** - Notify multiple services of events
* **Cache invalidation** - Signal cache updates across servers
* **Workflow triggers** - Initiate processes across distributed systems

## 📥 Subscribing to Channels

Use `redisSubscribe()` to listen for messages on Redis channels. You can subscribe using either a closure/lambda or a listener class.

### Function Signature

```javascript
struct function redisSubscribe(
    required any subscriber,
    required any channels,
    string cacheName = "default"
)
```

### Parameters

* **subscriber** - A closure/lambda function or listener class instance
* **channels** - A single channel name (string) or array of channel names
* **cacheName** - The name of the Redis cache connection to use (default: "default")

### Return Value

Returns a struct with two keys:

* **future** - A `BoxFuture` that is running your subscriber asynchronously
* **subscriber** - The Java Redis subscriber object for inspection or unsubscribing

### Subscribing with a Closure

```javascript
// Subscribe using a lambda function
var subscription = redisSubscribe(
    ( channel, message ) => {
        println( "Received on channel [#channel#]: #message#" );

        // Process the message
        if( message contains "maintenance" ) {
            // Handle maintenance notification
            enableMaintenanceMode();
        }
    },
    "notifications"
);

println( "<h1>Subscription active! Check the logs.</h1>" );

// Subscribe to multiple channels
var multiSubscription = redisSubscribe(
    ( channel, message ) => {
        println( "Channel: #channel#, Message: #message#" );
    },
    [ "notifications", "alerts", "user-events" ]
);
```

### Subscribing with a Listener Class

For more complex subscription handling, create a listener class:

```javascript
// Create and use a listener class
var listener = new NotificationListener();
var subscription = redisSubscribe( listener, "notifications" );

println( "<h1>Listener subscribed! Monitoring for messages.</h1>" );
```

### Unsubscribing

To stop receiving messages, use the `unsubscribe()` method on the subscriber:

```javascript
// Unsubscribe from all channels
subscription.subscriber.unsubscribe();

// Unsubscribe from specific channels
subscription.subscriber.unsubscribe( "notifications" );

// Cancel the future to stop the subscription thread
subscription.future.cancel();
```

## 🎧 Subscriber Listener Class

When using a class as a subscriber, implement one or more of the following callback methods. Each method is optional and will only be called if defined.

### Complete Listener Class Example

```javascript
class {

    /**
     * Called when a message is received on a subscribed channel
     * @channel The channel that received the message
     * @message The message content
     */
    public void function onMessage( string channel, string message ) {
        println( "Message received on #arguments.channel#: #arguments.message#" );

        // Process message based on channel
        switch( arguments.channel ) {
            case "notifications":
                handleNotification( arguments.message );
                break;
            case "alerts":
                handleAlert( arguments.message );
                break;
            default:
                logMessage( arguments.channel, arguments.message );
        }
    }

    /**
     * Called when a message is received on a pattern-subscribed channel
     * @pattern The pattern that matched
     * @channel The actual channel name
     * @message The message content
     */
    public void function onPMessage( string pattern, string channel, string message ) {
        println( "Pattern message: pattern=#arguments.pattern#, channel=#arguments.channel#, message=#arguments.message#" );
    }

    /**
     * Called when successfully subscribed to a channel
     * @channel The channel subscribed to
     * @subscribedChannels Total number of channels now subscribed to
     */
    public void function onSubscribe( string channel, numeric subscribedChannels ) {
        println( "Subscribed to #arguments.channel# (total channels: #arguments.subscribedChannels#)" );
    }

    /**
     * Called when unsubscribed from a channel
     * @channel The channel unsubscribed from
     * @subscribedChannels Remaining subscribed channels
     */
    public void function onUnsubscribe( string channel, numeric subscribedChannels ) {
        println( "Unsubscribed from #arguments.channel# (remaining: #arguments.subscribedChannels#)" );
    }

    /**
     * Called when successfully subscribed to a pattern
     * @pattern The pattern subscribed to
     * @subscribedChannels Total number of patterns now subscribed to
     */
    public void function onPSubscribe( string pattern, numeric subscribedChannels ) {
        println( "Subscribed to pattern #arguments.pattern# (total patterns: #arguments.subscribedChannels#)" );
    }

    /**
     * Called when unsubscribed from a pattern
     * @pattern The pattern unsubscribed from
     * @subscribedChannels Remaining subscribed patterns
     */
    public void function onPUnsubscribe( string pattern, numeric subscribedChannels ) {
        println( "Unsubscribed from pattern #arguments.pattern# (remaining: #arguments.subscribedChannels#)" );
    }

    // Helper methods
    private void function handleNotification( string message ) {
        // Custom notification handling logic
    }

    private void function handleAlert( string message ) {
        // Custom alert handling logic
    }

    private void function logMessage( string channel, string message ) {
        // Custom logging logic
    }

}
```

### Listener Method Reference

| Method             | Parameters                      | Description                                 | When Called                                              |
| ------------------ | ------------------------------- | ------------------------------------------- | -------------------------------------------------------- |
| `onMessage()`      | `channel`, `message`            | Handles messages from subscribed channels   | When a message arrives on a literal channel subscription |
| `onPMessage()`     | `pattern`, `channel`, `message` | Handles messages from pattern subscriptions | When a message arrives on a pattern-matched channel      |
| `onSubscribe()`    | `channel`, `subscribedChannels` | Confirms channel subscription               | After successfully subscribing to a channel              |
| `onUnsubscribe()`  | `channel`, `subscribedChannels` | Confirms channel unsubscription             | After unsubscribing from a channel                       |
| `onPSubscribe()`   | `pattern`, `subscribedChannels` | Confirms pattern subscription               | After successfully subscribing to a pattern              |
| `onPUnsubscribe()` | `pattern`, `subscribedChannels` | Confirms pattern unsubscription             | After unsubscribing from a pattern                       |

## 💡 Pub/Sub Best Practices

### Message Design

* **Keep messages small** - Pub/sub is optimized for many small messages
* **Use JSON** - Serialize complex data structures as JSON for interoperability
* **Include metadata** - Add timestamps, message IDs, or version info
* **Document message formats** - Maintain a schema for each channel

### Channel Naming

* **Use namespaces** - Prefix channels by domain: `app:notifications`, `system:alerts`
* **Be descriptive** - Channel names should indicate purpose: `user:login`, `order:created`
* **Avoid special characters** - Stick to alphanumeric and basic punctuation
* **Use hierarchy** - Structure channels logically: `analytics:users:signup`

### Subscriber Management

* **Handle errors gracefully** - Wrap message processing in try/catch
* **Avoid blocking operations** - Process messages quickly or queue for async processing
* **Implement reconnection logic** - Handle connection failures
* **Monitor subscription health** - Track message counts and processing times

### Performance Considerations

* **Pub/sub is fire-and-forget** - Messages are not persisted; offline subscribers miss messages
* **No delivery guarantees** - Unlike queues, pub/sub doesn't guarantee delivery
* **Use streams for reliability** - Consider Redis Streams for persistent messaging
* **Limit subscribers** - Too many subscribers can impact Redis performance
* **Consider message size** - Large messages can slow down the pub/sub system

## 🔧 Complete Pub/Sub Example

Here's a complete example demonstrating publishing and subscribing in a real-world scenario:

```javascript
// Application.bx - Configure Redis cache
this.caches["redis"] = {
    "provider": "Redis",
    "properties": {
        "host": "127.0.0.1",
        "port": "6379",
        "password": "",
        "keyprefix": "myapp"
    }
};
```

```javascript
// NotificationService.bx - Publisher service
class {

    function sendNotification( required string type, required struct data ) {
        var message = {
            "type": arguments.type,
            "data": arguments.data,
            "timestamp": now().getTime(),
            "messageId": createUUID()
        };

        var channel = "app:notifications:#arguments.type#";
        var count = redisPublish( channel, serializeJSON( message ), "redis" );

        println( "Notification sent to #count# subscriber(s)" );
        return message;
    }

}
```

```javascript
// NotificationSubscriber.bx - Subscriber listener
class {

    property name="emailService" inject="EmailService";
    property name="logService" inject="LogService";

    public void function onMessage( string channel, string message ) {
        try {
            var data = deserializeJSON( arguments.message );

            println( "Processing notification: #data.type#" );

            // Route based on notification type
            switch( data.type ) {
                case "user:signup":
                    emailService.sendWelcomeEmail( data.data.email );
                    break;
                case "order:completed":
                    emailService.sendOrderConfirmation( data.data.orderId );
                    break;
                case "system:alert":
                    logService.logAlert( data.data );
                    break;
            }

        } catch( any e ) {
            println( "Error processing message: #e.message#" );
            logService.logError( e );
        }
    }

    public void function onSubscribe( string channel, numeric subscribedChannels ) {
        println( "✓ Subscribed to #arguments.channel#" );
    }

    public void function onUnsubscribe( string channel, numeric subscribedChannels ) {
        println( "✗ Unsubscribed from #arguments.channel#" );
    }

}
```

```javascript
// Start subscriber in Application.bx onApplicationStart()
function onApplicationStart() {
    // Create subscriber instance
    var subscriber = new NotificationSubscriber();

    // Subscribe to notification channels
    application.notificationSubscription = redisSubscribe(
        subscriber,
        [
            "app:notifications:user:signup",
            "app:notifications:order:completed",
            "app:notifications:system:alert"
        ],
        "redis"
    );

    println( "✓ Notification subscriber started" );
}

// Clean up on application stop
function onApplicationEnd() {
    if( structKeyExists( application, "notificationSubscription" ) ) {
        application.notificationSubscription.subscriber.unsubscribe();
        application.notificationSubscription.future.cancel();
        println( "✓ Notification subscriber stopped" );
    }
}
```

```javascript
// Usage in your application
var notificationService = new NotificationService();

// Send notifications
notificationService.sendNotification( "user:signup", {
    "userId": 12345,
    "email": "user@example.com",
    "name": "John Doe"
});

notificationService.sendNotification( "order:completed", {
    "orderId": "ORD-2025-001",
    "total": 99.99,
    "customerId": 12345
});
```

## 🎯 Use Cases

### Real-Time Notifications

Broadcast system notifications, user alerts, or status updates across multiple application servers or clients.

### Cache Invalidation

Signal cache updates across a distributed application when data changes:

```javascript
// Publisher - invalidate cache across all servers
function updateUser( required numeric userId, required struct data ) {
    // Update database
    userDAO.update( userId, data );

    // Invalidate local cache
    cacheRemove( "user:#userId#" );

    // Tell other servers to invalidate
    redisPublish( "cache:invalidate:user", userId );
}

// Subscriber - listen for cache invalidation
var subscription = redisSubscribe(
    ( channel, message ) => {
        cacheRemove( "user:#message#" );
    },
    "cache:invalidate:user"
);
```

### Event-Driven Architecture

Implement loosely coupled microservices that react to events:

```javascript
// Order service publishes events
redisPublish( "events:order:created", {
    "orderId": newOrder.id,
    "customerId": newOrder.customerId,
    "total": newOrder.total
});

// Multiple services subscribe
// Email service sends confirmation
// Inventory service updates stock
// Analytics service tracks metrics
```

### Real-Time Monitoring

Push metrics and monitoring data to dashboards:

```javascript
// Publish metrics
redisPublish( "metrics:server:cpu", {
    "server": "web-01",
    "cpu": 45.2,
    "timestamp": now()
});

// Dashboard subscribes and updates in real-time
```

### Chat Applications

Build real-time chat or messaging features:

```javascript
// User sends message
redisPublish( "chat:room:#roomId#", {
    "userId": session.userId,
    "username": session.username,
    "message": form.message,
    "timestamp": now()
});

// All room participants receive message
var chatSubscription = redisSubscribe(
    ( channel, message ) => {
        var data = deserializeJSON( message );
        displayChatMessage( data );
    },
    "chat:room:#roomId#"
);
```
