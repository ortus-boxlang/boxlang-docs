[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `RedisPublish`

Publishes a message to a Redis channel.

## Method Signature

```
RedisPublish(cacheName=[any], channel=[any], message=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `cacheName` | `any` | `true` | The name of the redis cache to use. |  |
| `channel` | `any` | `true` | The channel name to publish to. |  |
| `message` | `any` | `true` | The message to publish. |  |

## Examples

Publish a message to a Redis channel:

```js
// Publish a simple message
var numSubscribers = RedisPublish(
    cache = "myRedisCache",
    channel = "notifications",
    message = "System update in progress"
);

println( "Message published to " & numSubscribers & " subscribers" );
```

Publish structured data as JSON:

```js
// Publish a structured message
var eventData = {
    type = "user.created",
    userId = 12345,
    timestamp = now()
};

var subscribers = RedisPublish(
    cache = "myRedisCache",
    channel = "events",
    message = serializeJSON( eventData )
);

println( "Event published to " & subscribers & " subscribers" );
```

## Related

- [RedisSubscribe()](./RedisSubscribe.md) - Subscribe to Redis channels
- [RedisGetProvider()](./RedisGetProvider.md) - Get the Redis cache provider
- [Pub/Sub Patterns Guide](../../pub-sub-patterns.md) - Advanced publish/subscribe patterns
- [API Usage Guide](../../api-usage.md) - Redis API documentation
