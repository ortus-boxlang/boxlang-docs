---
icon: bug
description: Debug and troubleshoot Redis connectivity and caching issues in BoxLang applications with step-by-step guidance.
---

# Troubleshooting

When encountering issues with Redis connectivity or caching, follow these debugging steps to identify and resolve problems.

## 📋 BoxLang Application Logs

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

## 💻 BoxLang Console Output

Enable debug output in your BoxLang runtime to see real-time cache operations by starting the server in debug mode.  See the [Configuration](./../../../../getting-started/configuration.md) section for details.

**Console logging:**

```javascript
// Log cache operations
println( "Cache GET: #cacheKey#" );
var result = cacheGet( cacheKey );
println( "Cache result: #isNull(result) ? 'MISS' : 'HIT'#" );
```

## 🔴 Redis Server Logs

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

## 🛠️ Redis CLI Tools

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

## 🖥️ Redis Web Administration Tools

Several web-based tools can help visualize and debug Redis data:

### Redis Commander

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

### RedisInsight

Official Redis GUI by Redis Ltd (free).

**Download:** [https://redis.com/redis-enterprise/redis-insight/](https://redis.com/redis-enterprise/redis-insight/)

**Features:**

* Visual key browser
* Real-time performance monitoring
* Memory analysis
* Cluster topology view
* Command profiler
* Built-in CLI

### P3X Redis UI

Electron-based desktop app for Redis management.

**Download:** [https://github.com/patrikx3/redis-ui](https://github.com/patrikx3/redis-ui)

**Features:**

* Cross-platform desktop app
* Multiple connection management
* Tree view of keys
* JSON/String/Binary viewers

## 🔍 Common Issues & Solutions

### Connection Timeouts

**Symptoms:** `Connection timeout` errors in logs

**Solutions:**

* Verify Redis server is running: `systemctl status redis` (Linux)
* Check network connectivity: `telnet redis-host 6379`
* Review firewall rules
* Increase `timeout` setting in BoxLang configuration
* Check Redis `maxclients` setting

### Authentication Failures

**Symptoms:** `NOAUTH Authentication required` errors

**Solutions:**

* Verify `password` setting matches Redis configuration
* Check Redis ACL permissions: `ACL LIST` in redis-cli
* Ensure `username` is correct (if using ACL)
* Test authentication: `redis-cli -a yourpassword PING`

### Pool Exhaustion

**Symptoms:** `Could not get a resource from the pool` errors

**Solutions:**

* Increase `maxConnections` setting
* Check for connection leaks in application code
* Reduce `poolWaittimeout` to fail faster
* Monitor active connections: `CLIENT LIST` in redis-cli
* Review connection usage patterns

### Cache Misses

**Symptoms:** High cache miss ratio, poor performance

**Solutions:**

* Verify keys are being stored: Use `KEYS` or `SCAN` in redis-cli
* Check `keyprefix` configuration matches
* Review `cacheKeyCaseSensitivity` setting
* Verify TTL values: `TTL keyname` in redis-cli
* Check Redis memory limits: `INFO memory`

### Cluster Connection Issues

**Symptoms:** `MOVED` or `ASK` redirection errors

**Solutions:**

* Verify all cluster nodes are healthy: `CLUSTER INFO`
* Check cluster topology: `CLUSTER NODES`
* Ensure `hosts` includes multiple nodes for failover
* Increase `maxAttempts` for retries
* Review cluster slot assignments

## 📝 Debug Logging Configuration

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

## 🔧 Testing Connectivity

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

## 📞 Getting Help

If you continue to experience issues:

1. **Check BoxLang documentation:** [https://boxlang.io/docs](https://boxlang.io/docs)
2. **Redis documentation:** [https://redis.io/docs](https://redis.io/docs)
3. **Community support:** BoxLang Slack/Discord channels
4. **Professional support:** Contact [Ortus Solutions](https://www.ortussolutions.com) for BoxLang+ support
