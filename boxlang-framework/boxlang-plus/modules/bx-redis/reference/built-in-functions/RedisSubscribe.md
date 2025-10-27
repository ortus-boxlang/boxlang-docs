[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `RedisSubscribe`

Subscribes to a Redis channel for messages.

## Method Signature

```
RedisSubscribe(cacheName=[any], channel=[any], callback=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `any` | `true` | The name of the redis cache to use. |  |
| `channel` | `any` | `true` | The channel name to subscribe to. |  |
| `callback` | `any` | `true` | The callback function to invoke when messages are received. |  |

## Examples

Subscribe to a Redis channel:

```js
// Subscribe to a channel with a callback handler
RedisSubscribe(
    cache = "myRedisCache",
    channel = "notifications",
    callback = function( message ) {
        println( "Received message: " & message );
    }
);
```

Handle multiple message types:

```js
// Subscribe to events channel and parse JSON messages
RedisSubscribe(
    cache = "myRedisCache",
    channel = "events",
    callback = function( message ) {
        var event = deserializeJSON( message );

        switch( event.type ) {
            case "user.created":
                println( "New user created: " & event.userId );
                break;
            case "user.updated":
                println( "User updated: " & event.userId );
                break;
            default:
                println( "Unknown event type: " & event.type );
        }
    }
);
```

Subscribe to multiple channels:

```js
// Subscribe to multiple channels with pattern matching
RedisSubscribe(
    cache = "myRedisCache",
    channel = "events:*",
    callback = function( message ) {
        println( "Event received: " & message );
    }
);
```

## Related

- [RedisPublish()](./RedisPublish.md) - Publish messages to Redis channels
- [RedisGetProvider()](./RedisGetProvider.md) - Get the Redis cache provider
- [Pub/Sub Patterns Guide](../../pub-sub-patterns.md) - Advanced publish/subscribe patterns
- [API Usage Guide](../../api-usage.md) - Redis API documentation
