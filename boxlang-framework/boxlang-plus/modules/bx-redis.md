---
icon: database
---

# 🔴 Redis +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](./bx-plus.md) with a limited trial.
{% endhint %}

This module will enhance your language by allowing you to connect to Redis instances, clusters, or sentinel instances. Here are some features:

* Add native Redis functionality to the language
* Connect to a Redis server or a Redis cluster, or Redis Sentinel
* Store session variables in a distributed Redis cluster
* Leverage the Redis publish/subscribe features to create real-time messaging
* Get rid of sticky session load balancers, come to the round-robin world!
* Session variable persistence even after server restarts
* Cache connection capabilities for providing distributed & highly scalable query, object, template, and function caching
* Much more

## 📦 Installation

```bash
# For Operating Systems using our Quick Installer.
install-bx-module bx-redis

# Using CommandBox to install for web servers.
box install bx-redis
```

## 🗄️ About Redis

Redis (Remote Dictionary Server) is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. Here are the different deployment modes supported by this module:

### 🖥️ Redis Standalone

A single Redis server instance - the simplest deployment mode. Ideal for:

* Development and testing environments
* Small applications with low traffic
* Non-critical caching scenarios
* Session storage for single-server applications

**Key Characteristics:**

* Single point of failure
* Simplest to configure and maintain
* Lower resource requirements
* Best performance for single-node operations

### 🔗 Redis Cluster

A distributed implementation of Redis with automatic sharding and high availability. Ideal for:

* High-availability production environments
* Large-scale applications with high throughput
* Horizontal scaling requirements
* Automatic failover and data partitioning

**Key Characteristics:**

* Automatic data sharding across multiple nodes
* Built-in replication and failover
* No single point of failure
* Can scale to 1000+ nodes
* Provides horizontal scalability

### 🛡️ Redis Sentinel

A high-availability solution for Redis that provides monitoring, notifications, and automatic failover. Ideal for:

* Production environments requiring high availability
* Applications that need automatic failover
* Monitoring and alerting requirements
* Master-slave replication scenarios

**Key Characteristics:**

* Automatic failover for master-slave setups
* Configuration provider for clients
* Monitoring and health checks
* Notification system for events
* Provides high availability without clustering

## ⚙️ Configuration

### 📋 Configuration Settings Overview

This table shows all available settings across all Redis deployment modes:

| Setting | Standalone | Cluster | Sentinel | Type | Default | Description |
|---------|------------|---------|----------|------|---------|-------------|
| `host` | ✅ | ❌ | ❌ | string | `127.0.0.1` | Redis server IP or hostname |
| `hosts` | ❌ | ✅ | ❌ | string | - | Comma-delimited cluster node list |
| `sentinels` | ❌ | ❌ | ✅ | string | - | Comma-delimited sentinel servers (host:port) |
| `port` | ✅ | ✅ | ✅ | numeric | `6379` | Redis server/cluster port |
| `database` | ✅ | ❌ | ✅ | numeric | `0` | Logical database number (0-15) |
| `username` | ✅ | ✅ | ✅ | string | - | Redis username (ACL authentication) |
| `password` | ✅ | ✅ | ✅ | string | - | Redis password |
| `useSSL` | ✅ | ✅ | ✅ | boolean | `false` | Enable SSL/TLS encryption |
| `keyprefix` | ✅ | ✅ | ✅ | string | `boxlang-cache` | Prefix for all cache keys |
| `cacheKeyCaseSensitivity` | ✅ | ✅ | ✅ | boolean | `false` | Enable case-sensitive keys |
| `timeout` | ✅ | ✅ | ✅ | numeric | `2000` | Connection timeout (ms) |
| `readTimeout` | ❌ | ✅ | ✅ | numeric | `2000` | Read operation timeout (ms) |
| `socketTimeout` | ✅ | ✅ | ✅ | numeric | `2000` | Socket timeout (ms) |
| `poolWaittimeout` | ✅ | ✅ | ✅ | numeric | `1000` | Pool resource wait timeout (ms) |
| `maxConnections` | ✅ | ✅ | ✅ | numeric | `50` | Maximum connections per pool |
| `maxIdleConnections` | ✅ | ✅ | ✅ | numeric | `20` | Maximum idle connections |
| `idleConnections` | ✅ | ❌ | ✅ | numeric | `5` | Initial idle connections |
| `maxIdleTime` | ❌ | ✅ | ✅ | numeric | `30000` | Max idle time before eviction (ms) |
| `maxAttempts` | ❌ | ✅ | ✅ | numeric | `10` | Maximum connection attempts |

### 🔧 boxlang.json Configuration

The JSON configuration structure for BoxLang should be placed in the `caches` object in `boxlang.json`.

#### 🖥️ Single Node (Standalone) Configuration

```json
{
  "caches": {
    "sessions": {
      "provider": "Redis",
      "properties": {
        "host": "127.0.0.1",
        "port": "6379",
        "database": "0",
        "username": "",
        "password": "",
        "useSSL": "false",
        "keyprefix": "boxlang-sessions",
        "cacheKeyCaseSensitivity": "false",
        "timeout": 2000,
        "socketTimeout": 2000,
        "poolWaittimeout": 1000,
        "maxConnections": 50,
        "idleConnections": 5,
        "maxIdleConnections": 20
      }
    }
  }
}
```

#### 🔗 Cluster Configuration

```json
{
  "caches": {
    "resources": {
      "provider": "RedisCluster",
      "properties": {
        "hosts": "node1.myrediscluster,node2.myrediscluster,node3.myrediscluster",
        "port": "6379",
        "username": "${REDIS_CLUSTER_USERNAME}",
        "password": "${REDIS_CLUSTER_PASSWORD}",
        "useSSL": "${REDIS_CLUSTER_USE_SSL:false}",
        "keyprefix": "boxlang-cluster",
        "cacheKeyCaseSensitivity": "false",
        "timeout": 2000,
        "readTimeout": 2000,
        "socketTimeout": 2000,
        "poolWaittimeout": 1000,
        "maxAttempts": 10,
        "maxConnections": 1000,
        "maxIdleTime": 30000,
        "maxIdleConnections": 20
      }
    }
  }
}
```

#### 🛡️ Sentinel Configuration

[Redis Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/) provides high availability through monitoring and automatic failover.

```json
{
  "caches": {
    "resources": {
      "provider": "RedisSentinel",
      "properties": {
        "sentinels": "sentinel1.myhost.com:26379,sentinel2.myhost.com:26379",
        "port": "6379",
        "database": "0",
        "username": "${REDIS_SENTINEL_USERNAME}",
        "password": "${REDIS_SENTINEL_PASSWORD}",
        "useSSL": "false",
        "keyprefix": "boxlang-sentinel",
        "cacheKeyCaseSensitivity": "false",
        "timeout": 2000,
        "readTimeout": 2000,
        "socketTimeout": 2000,
        "poolWaittimeout": 1000,
        "maxAttempts": 10,
        "maxConnections": 1000,
        "maxIdleTime": 30000,
        "maxIdleConnections": 20
      }
    }
  }
}
```

### 📝 Application.bx Configuration

#### 🖥️ Standalone Example

```javascript
this.caches["sessions"] = {
  "provider": "Redis",
  "properties": {
    "host": "127.0.0.1",
    "port": "6379",
    "database": "0",
    "password": "",
    "useSSL": false,
    "keyprefix": "boxlang-sessions",
    "cacheKeyCaseSensitivity": false,
    "timeout": 2000,
    "socketTimeout": 2000,
    "poolWaittimeout": 1000,
    "maxConnections": 50,
    "idleConnections": 10
  }
};
```

#### 🔗 Cluster Example

```javascript
this.caches["resources"] = {
  "provider": "RedisCluster",
  "properties": {
    "hosts": "node1.myrediscluster,node2.myrediscluster,node3.myrediscluster",
    "port": "6379",
    "username": myClusterUsername,
    "password": myClusterPassword,
    "useSSL": false,
    "keyprefix": "boxlang-cluster",
    "timeout": 2000,
    "readTimeout": 2000,
    "socketTimeout": 2000,
    "poolWaittimeout": 1000,
    "maxAttempts": 10,
    "maxConnections": 1000,
    "maxIdleTime": 30000,
    "maxIdleConnections": 20
  }
};
```

#### 🛡️ Sentinel Example

```javascript
this.caches["resources"] = {
  "provider": "RedisSentinel",
  "properties": {
    "sentinels": "sentinel1.myhost.com:26379,sentinel2.myhost.com:26379",
    "port": "6379",
    "database": "0",
    "username": mySentinelUsername,
    "password": mySentinelPassword,
    "useSSL": false,
    "keyprefix": "boxlang-sentinel",
    "timeout": 2000,
    "readTimeout": 2000,
    "socketTimeout": 2000,
    "poolWaittimeout": 1000,
    "maxAttempts": 10,
    "maxConnections": 1000,
    "maxIdleTime": 30000,
    "maxIdleConnections": 20
  }
};
```

## 📚 Settings Reference

### 🔌 Connection Settings

#### host

**Applies to:** Standalone only
**Type:** string
**Default:** `127.0.0.1`

The Redis server IP address or hostname for standalone deployments.

#### hosts

**Applies to:** Cluster only
**Type:** string
**Required:** Yes

Comma-delimited list of cluster node IPs or hostnames. You don't need all nodes, but include multiple for redundancy.

**Example:** `node1.redis.local,node2.redis.local,node3.redis.local`

#### sentinels

**Applies to:** Sentinel only
**Type:** string
**Required:** Yes

Comma-delimited list of Sentinel servers in `{host}:port` format.

**Example:** `sentinel1.myhost.com:26379,sentinel2.myhost.com:26379`

#### port

**Applies to:** All modes
**Type:** numeric
**Default:** `6379`

The port number for Redis server/cluster connections.

#### database

**Applies to:** Standalone, Sentinel
**Type:** numeric
**Default:** `0`

The logical database to connect to in Redis (0-15). Redis Cluster does not support multiple databases.

### 🔐 Authentication & Security

#### username

**Applies to:** All modes
**Type:** string
**Default:** Empty

The Redis username for [ACL-based authentication](https://docs.redis.com/latest/rs/security/access-control/manage-users/add-users/). Only required when user-level access control is enabled.

#### password

**Applies to:** All modes
**Type:** string
**Default:** Empty

The password for Redis authentication. Leave empty if no password is set.

#### useSSL

**Applies to:** All modes
**Type:** boolean
**Default:** `false`

Enable SSL/TLS encryption for the connection to Redis. Recommended for production environments.

### 🏷️ Cache Key Management

#### keyprefix

**Applies to:** All modes
**Type:** string
**Default:** `boxlang-cache`

Prefix automatically added to every cache key. This helps:

* Avoid key collisions between multiple caches
* Distinguish cache sources
* Namespace different applications
* Organize keys by environment

**Example:** `boxlang-sessions:user123` instead of just `user123`

#### cacheKeyCaseSensitivity

**Applies to:** All modes
**Type:** boolean
**Default:** `false`

By default, all cache keys are converted to lowercase to avoid casing issues. Set to `true` to enable case-sensitive keys.

**Warning:** Changing this setting on an existing cache will make previously stored keys inaccessible.

### ⏱️ Timeout Settings

#### timeout

**Applies to:** All modes
**Type:** numeric
**Default:** `2000`

Connection timeout in milliseconds. If a connection cannot be established within this time, an exception is thrown.

#### readTimeout

**Applies to:** Cluster, Sentinel
**Type:** numeric
**Default:** `2000`

Read operation timeout in milliseconds. Defaults to connection timeout if not specified.

#### socketTimeout

**Applies to:** All modes
**Type:** numeric
**Default:** `2000`

Socket-level timeout in milliseconds for network operations.

#### poolWaittimeout

**Applies to:** All modes
**Type:** numeric
**Default:** `1000`

Maximum time in milliseconds to wait for a connection from the pool before throwing an exception.

### 🔗 Connection Pool Settings

#### maxConnections

**Applies to:** All modes
**Type:** numeric
**Default:** `50` (Standalone/Sentinel), `1000` (Cluster)

Maximum number of concurrent connections allowed per pool. Adjust based on:

* Expected concurrent requests
* Available system resources
* Redis server capacity

#### maxIdleConnections

**Applies to:** All modes
**Type:** numeric
**Default:** `20`

Maximum number of idle connections to retain in the pool. Idle connections above this limit will be closed.

#### idleConnections

**Applies to:** Standalone, Sentinel
**Type:** numeric
**Default:** `5`

Initial number of idle connections to create when the pool starts. These connections are immediately available for use.

#### maxIdleTime

**Applies to:** Cluster, Sentinel
**Type:** numeric
**Default:** `30000`

Maximum time in milliseconds a connection can remain idle before being evicted from the pool.

### 🔄 Retry & Failover Settings

#### maxAttempts

**Applies to:** Cluster, Sentinel
**Type:** numeric
**Default:** `10`

Maximum number of connection attempts before failing. Useful for handling:

* Temporary network issues
* Node failovers in cluster mode
* Sentinel leader elections

## 💡 Best Practices

### 🎯 Choosing a Deployment Mode

**Use Standalone when:**

* Running in development/testing
* Building a proof of concept
* Caching non-critical data
* Running a small application

**Use Cluster when:**

* Need horizontal scalability
* Have large datasets requiring sharding
* Require high availability
* Running mission-critical applications

**Use Sentinel when:**

* Need high availability without clustering
* Using master-slave replication
* Want automatic failover
* Need monitoring and notifications

### ⚡ Performance Tuning

**Connection Pooling:**

* Set `maxConnections` based on concurrent load
* Keep `idleConnections` reasonable to avoid overhead
* Monitor pool exhaustion in production

**Timeouts:**

* Keep timeouts short to fail fast
* Adjust based on network latency
* Consider retry logic for transient failures

**Key Prefixes:**

* Always use meaningful prefixes
* Helps with debugging and monitoring
* Enables easy key pattern matching

### 🔒 Security Recommendations

* Always use SSL/TLS in production (`useSSL: true`)
* Enable Redis ACL and use username/password authentication
* Use strong, unique passwords
* Consider using Redis behind a VPN or firewall
* Regularly rotate passwords
* Monitor failed authentication attempts

### 📊 Monitoring

Consider monitoring these metrics:

* Connection pool utilization
* Cache hit/miss ratios
* Network latency
* Memory usage
* Failed connection attempts
* Timeout occurrences

## 🐛 Debugging & Troubleshooting

When encountering issues with Redis connectivity or caching, follow these debugging steps to identify and resolve problems.

### 📋 BoxLang Application Logs

Start by checking your BoxLang application logs for Redis-related errors:

**Location:** Depends on your runtime environment

* **CommandBox:** Check `{server-home}/logs/` directory
* **Tomcat/Jetty:** Check application server logs directory
* **Docker:** Use `docker logs <container-name>`

**Look for:**

* Connection timeout errors
* Authentication failures
* Pool exhaustion warnings
* Serialization/deserialization errors
* Cache key conflicts

**Example error patterns:**

```
redis.clients.jedis.exceptions.JedisConnectionException
Connection timed out
Could not get a resource from the pool
NOAUTH Authentication required
```

### 💻 BoxLang Console Output

Enable debug output in your BoxLang runtime to see real-time cache operations:

**Development Mode:**

```javascript
// In Application.bx
this.debugSettings = {
    "showCacheEvents": true,
    "showExecutionTime": true
};
```

**Console logging:**

```javascript
// Log cache operations
println( "Cache GET: #cacheKey#" );
var result = cacheGet( cacheKey );
println( "Cache result: #isNull(result) ? 'MISS' : 'HIT'#" );
```

### 🔴 Redis Server Logs

Redis logs provide detailed information about server-side operations and errors.

**Log locations by installation method:**

* **Linux (systemd):** `/var/log/redis/redis-server.log`
* **MacOS (Homebrew):** `/usr/local/var/log/redis.log`
* **Docker:** `docker logs <redis-container-name>`
* **Windows:** Check your Redis installation directory

**Access logs:**

```bash
# Linux/Mac - Follow logs in real-time
tail -f /var/log/redis/redis-server.log

# Docker
docker logs -f redis-container

# Search for specific errors
grep "error\|warning\|timeout" /var/log/redis/redis-server.log
```

**Common log indicators:**

* `# Server started` - Successful startup
* `# Connection from {ip}` - Client connections
* `# Client closed connection` - Disconnections
* `# Warning: memory usage high` - Memory issues
* `NOAUTH` - Authentication failures
* `READONLY` - Cluster failover states

### 🛠️ Redis CLI Tools

Use the Redis command-line interface to test connectivity and inspect data:

**Connect to Redis:**

```bash
# Standalone
redis-cli -h 127.0.0.1 -p 6379 -a yourpassword

# With SSL
redis-cli -h 127.0.0.1 -p 6379 -a yourpassword --tls

# Cluster
redis-cli -c -h node1.cluster -p 6379 -a yourpassword
```

**Useful diagnostic commands:**

```bash
# Test connection
PING
# Response: PONG

# Check server info
INFO server
INFO clients
INFO memory
INFO stats

# View all keys with prefix
KEYS boxlang-cache:*

# Check specific key
GET boxlang-cache:mykey
TTL boxlang-cache:mykey

# Monitor all commands in real-time
MONITOR

# Check client connections
CLIENT LIST

# Check cluster status (if using cluster)
CLUSTER INFO
CLUSTER NODES
```

### 🖥️ Redis Web Administration Tools

Several web-based tools can help visualize and debug Redis data:

#### Redis Commander

Open-source web management tool for Redis.

**Installation:**

```bash
# Using npm
npm install -g redis-commander

# Run
redis-commander --redis-host 127.0.0.1 --redis-port 6379 --redis-password yourpassword
```

**Access:** `http://localhost:8081`

**Features:**

* Browse keys by pattern
* View key values and TTLs
* Delete keys
* Monitor server stats
* Real-time key search

#### RedisInsight

Official Redis GUI by Redis Ltd (free).

**Download:** [https://redis.com/redis-enterprise/redis-insight/](https://redis.com/redis-enterprise/redis-insight/)

**Features:**

* Visual key browser
* Real-time performance monitoring
* Memory analysis
* Cluster topology view
* Command profiler
* Built-in CLI

#### P3X Redis UI

Electron-based desktop app for Redis management.

**Download:** [https://github.com/patrikx3/redis-ui](https://github.com/patrikx3/redis-ui)

**Features:**

* Cross-platform desktop app
* Multiple connection management
* Tree view of keys
* JSON/String/Binary viewers

### 🔍 Common Issues & Solutions

#### Connection Timeouts

**Symptoms:** `Connection timeout` errors in logs

**Solutions:**

* Verify Redis server is running: `systemctl status redis` (Linux)
* Check network connectivity: `telnet redis-host 6379`
* Review firewall rules
* Increase `timeout` setting in BoxLang configuration
* Check Redis `maxclients` setting

#### Authentication Failures

**Symptoms:** `NOAUTH Authentication required` errors

**Solutions:**

* Verify `password` setting matches Redis configuration
* Check Redis ACL permissions: `ACL LIST` in redis-cli
* Ensure `username` is correct (if using ACL)
* Test authentication: `redis-cli -a yourpassword PING`

#### Pool Exhaustion

**Symptoms:** `Could not get a resource from the pool` errors

**Solutions:**

* Increase `maxConnections` setting
* Check for connection leaks in application code
* Reduce `poolWaittimeout` to fail faster
* Monitor active connections: `CLIENT LIST` in redis-cli
* Review connection usage patterns

#### Cache Misses

**Symptoms:** High cache miss ratio, poor performance

**Solutions:**

* Verify keys are being stored: Use `KEYS` or `SCAN` in redis-cli
* Check `keyprefix` configuration matches
* Review `cacheKeyCaseSensitivity` setting
* Verify TTL values: `TTL keyname` in redis-cli
* Check Redis memory limits: `INFO memory`

#### Cluster Connection Issues

**Symptoms:** `MOVED` or `ASK` redirection errors

**Solutions:**

* Verify all cluster nodes are healthy: `CLUSTER INFO`
* Check cluster topology: `CLUSTER NODES`
* Ensure `hosts` includes multiple nodes for failover
* Increase `maxAttempts` for retries
* Review cluster slot assignments

### 📝 Debug Logging Configuration

Enable detailed logging in your BoxLang application:

```javascript
// Application.bx
this.caches["sessions"] = {
    "provider": "Redis",
    "properties": {
        // ... other settings ...
    },
    // Enable debug logging
    "debug": true
};
```

**View cache statistics:**

```javascript
// Get cache metadata
var cacheMetadata = getCacheMetadata( "sessions" );
println( "Hit count: #cacheMetadata.hitCount#" );
println( "Miss count: #cacheMetadata.missCount#" );
println( "Hit ratio: #cacheMetadata.hitRatio#" );
```

### 🔧 Testing Connectivity

Create a simple test script to verify Redis connectivity:

```javascript
// test-redis.bx
try {
    // Test cache put
    cachePut( "test-key", "test-value", createTimeSpan(0,0,5,0), "sessions" );
    println( "✓ Cache PUT successful" );

    // Test cache get
    var result = cacheGet( "test-key", "sessions" );
    println( "✓ Cache GET successful: #result#" );

    // Test cache remove
    cacheRemove( "test-key", "sessions" );
    println( "✓ Cache REMOVE successful" );

    println( "✓ All Redis operations successful!" );

} catch( any e ) {
    println( "✗ Redis error: #e.message#" );
    println( "✗ Detail: #e.detail#" );
    println( "✗ Stack trace: #e.stackTrace#" );
}
```

### 📞 Getting Help

If you continue to experience issues:

1. **Check BoxLang documentation:** [https://boxlang.io/docs](https://boxlang.io/docs)
2. **Redis documentation:** [https://redis.io/docs](https://redis.io/docs)
3. **Community support:** BoxLang Slack/Discord channels
4. **Professional support:** Contact [Ortus Solutions](https://www.ortussolutions.com) for BoxLang+ support

## 📡 Publish/Subscribe

### What is Pub/Sub?

![Redis Pub/Sub Architecture](https://dingyuliang.me/wp-content/uploads/2018/02/redis-pubsub-768x407.png)

The Redis module provides native messaging capabilities through Redis Publish/Subscribe constructs. This allows your BoxLang applications to implement real-time messaging and event-driven architectures using Redis as the message broker.

{% embed url="https://redis.io/topics/pubsub" %}

> Redis Pub/Sub implements the Publish/Subscribe messaging paradigm. This decoupling of publishers and subscribers can allow for greater scalability and a more dynamic network topology.

**How it works:**

1. **Subscribers** express interest in one or more channels (literal channels or pattern channels)
2. **Publishers** send messages into channels
3. **Redis** pushes these messages to all subscribers that have matched the channel

### 📋 Pub/Sub BIFs Overview

The module provides two main functions for implementing pub/sub patterns:

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `redisPublish()` | `channel`, `message`, `cacheName` | numeric | Publishes a message to a Redis channel. Returns the number of subscribers that received the message. |
| `redisSubscribe()` | `subscriber`, `channels`, `cacheName` | struct | Subscribes to one or more channels using a closure/lambda or listener class. Returns a struct with `future` and `subscriber` keys. |

{% hint style="warning" %}
Pattern-based publishing and subscriptions are not yet implemented in this version.
{% endhint %}

### 📤 Publishing Messages

Use `redisPublish()` to send messages to a Redis channel. The function returns the number of subscribers that received the message.

#### Function Signature

```javascript
numeric function redisPublish(
    required string channel,
    required any message,
    string cacheName = "default"
)
```

#### Parameters

* **channel** - The Redis channel name to publish to
* **message** - The message content to send (will be serialized)
* **cacheName** - The name of the Redis cache connection to use (default: "default")

#### Publishing Example

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

#### Use Cases for Publishing

* **System notifications** - Broadcast status updates
* **Real-time updates** - Push data changes to connected clients
* **Event broadcasting** - Notify multiple services of events
* **Cache invalidation** - Signal cache updates across servers
* **Workflow triggers** - Initiate processes across distributed systems

### 📥 Subscribing to Channels

Use `redisSubscribe()` to listen for messages on Redis channels. You can subscribe using either a closure/lambda or a listener class.

#### Function Signature

```javascript
struct function redisSubscribe(
    required any subscriber,
    required any channels,
    string cacheName = "default"
)
```

#### Parameters

* **subscriber** - A closure/lambda function or listener class instance
* **channels** - A single channel name (string) or array of channel names
* **cacheName** - The name of the Redis cache connection to use (default: "default")

#### Return Value

Returns a struct with two keys:

* **future** - A `BoxFuture` that is running your subscriber asynchronously
* **subscriber** - The Java Redis subscriber object for inspection or unsubscribing

#### Subscribing with a Closure

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

#### Subscribing with a Listener Class

For more complex subscription handling, create a listener class:

```javascript
// Create and use a listener class
var listener = new NotificationListener();
var subscription = redisSubscribe( listener, "notifications" );

println( "<h1>Listener subscribed! Monitoring for messages.</h1>" );
```

#### Unsubscribing

To stop receiving messages, use the `unsubscribe()` method on the subscriber:

```javascript
// Unsubscribe from all channels
subscription.subscriber.unsubscribe();

// Unsubscribe from specific channels
subscription.subscriber.unsubscribe( "notifications" );

// Cancel the future to stop the subscription thread
subscription.future.cancel();
```

### 🎧 Subscriber Listener Class

When using a class as a subscriber, implement one or more of the following callback methods. Each method is optional and will only be called if defined.

#### Complete Listener Class Example

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

#### Listener Method Reference

| Method | Parameters | Description | When Called |
|--------|-----------|-------------|-------------|
| `onMessage()` | `channel`, `message` | Handles messages from subscribed channels | When a message arrives on a literal channel subscription |
| `onPMessage()` | `pattern`, `channel`, `message` | Handles messages from pattern subscriptions | When a message arrives on a pattern-matched channel |
| `onSubscribe()` | `channel`, `subscribedChannels` | Confirms channel subscription | After successfully subscribing to a channel |
| `onUnsubscribe()` | `channel`, `subscribedChannels` | Confirms channel unsubscription | After unsubscribing from a channel |
| `onPSubscribe()` | `pattern`, `subscribedChannels` | Confirms pattern subscription | After successfully subscribing to a pattern |
| `onPUnsubscribe()` | `pattern`, `subscribedChannels` | Confirms pattern unsubscription | After unsubscribing from a pattern |

### 💡 Pub/Sub Best Practices

#### Message Design

* **Keep messages small** - Pub/sub is optimized for many small messages
* **Use JSON** - Serialize complex data structures as JSON for interoperability
* **Include metadata** - Add timestamps, message IDs, or version info
* **Document message formats** - Maintain a schema for each channel

#### Channel Naming

* **Use namespaces** - Prefix channels by domain: `app:notifications`, `system:alerts`
* **Be descriptive** - Channel names should indicate purpose: `user:login`, `order:created`
* **Avoid special characters** - Stick to alphanumeric and basic punctuation
* **Use hierarchy** - Structure channels logically: `analytics:users:signup`

#### Subscriber Management

* **Handle errors gracefully** - Wrap message processing in try/catch
* **Avoid blocking operations** - Process messages quickly or queue for async processing
* **Implement reconnection logic** - Handle connection failures
* **Monitor subscription health** - Track message counts and processing times

#### Performance Considerations

* **Pub/sub is fire-and-forget** - Messages are not persisted; offline subscribers miss messages
* **No delivery guarantees** - Unlike queues, pub/sub doesn't guarantee delivery
* **Use streams for reliability** - Consider Redis Streams for persistent messaging
* **Limit subscribers** - Too many subscribers can impact Redis performance
* **Consider message size** - Large messages can slow down the pub/sub system

### 🔧 Complete Pub/Sub Example

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

### 🎯 Use Cases

#### Real-Time Notifications

Broadcast system notifications, user alerts, or status updates across multiple application servers or clients.

#### Cache Invalidation

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

#### Event-Driven Architecture

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

#### Real-Time Monitoring

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

#### Chat Applications

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
