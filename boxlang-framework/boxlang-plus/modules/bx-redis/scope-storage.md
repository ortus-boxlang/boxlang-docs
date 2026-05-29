---
icon: microscope
description: Store and retrieve scope data using Redis as the backend storage.
---

# Scope Storage

BoxLang allows you to seamlessly store session and client scopes in Redis as the backend storage. You will set and access these scopes like you normally would in BoxLang, but behind the scenes, BoxLang stores a cache entry for each user containing their session/client variables in the Redis cluster.

## 🎯 Benefits

Using Redis for scope storage provides several important advantages:

* **Persistence** - Scopes survive server restarts without data loss
* **Lower Memory Usage** - Variables are stored in Redis, not in the JVM heap
* **Distributed Sessions** - User sessions can be shared across multiple web servers (eliminates sticky sessions)
* **Horizontal Scalability** - Redis cluster can scale to handle millions of users
* **High Availability** - Redis replication and clustering provide failover capabilities
* **Performance** - In-memory storage provides fast read/write operations

## 💡 Use Cases

### Scale Out Applications

Take your single-server application with heavy session/client variable usage and scale it to multiple web servers behind a round-robin load balancer. Users can connect to any web server, and their session variables follow them automatically with no extra overhead.

### Handle High Traffic

If you have millions of website visitors and are running out of heap space due to session storage, push those sessions to a distributed Redis layer that can scale out to meet demand. Your application servers are no longer the bottleneck.

### Microservices Architecture

Share session data across different applications or microservices by using the same Redis cache. Enable true single sign-on and shared user context across your entire platform.

## ⚙️ Configuration

{% stepper %}

{% step %}
### Configure Redis Cache

First, configure your Redis cache(s) as per the [Configuration](README.md#configuration) instructions. You can configure caches for session and client storage separately or use a single cache for both.

#### Session Storage Cache Example

```json
{
  "caches": {
    "sessions": {
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
        "idleConnections": 5,
        "maxIdleConnections": 20
      }
    }
  }
}
```

#### Client Storage Cache Example

This is only if you have CFML applications and are using the `bx-compat-cfml` module.  In BoxLang native applications, the `client` scope is not available since it's particularily the same as session scope.

```json
{
  "caches": {
    "clients": {
      "provider": "Redis",
      "properties": {
        "host": "127.0.0.1",
        "port": "6379",
        "database": "1",
        "password": "",
        "useSSL": false,
        "keyprefix": "boxlang-clients",
        "cacheKeyCaseSensitivity": false,
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

{% endstep %}

{% step %}
### Configure Session Storage

You can configure session storage in two ways: using `Application.bx` or using `boxlang.json` for runtime-level configuration.

#### Option A: Application.bx Configuration

Configure session storage at the application level using the `Application.bx` file:

```javascript
class {
    this.name = "myApp";

    // Enable session management
    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan( 0, 0, 30, 0 ); // 30 minutes

    // Configure Redis session storage
    this.sessionStorage = "sessions"; // Name of the Redis cache to use
    this.sessionCluster = true;       // Enable distributed sessions
}
```

#### Option B: boxlang.json Configuration

Configure session storage at the runtime level using `boxlang.json`. This applies to all applications unless overridden in `Application.bx`.

See the [BoxLang Configuration Documentation](https://boxlang.ortusbooks.com/getting-started/configuration/directives#session-storage) for complete details.

```json
"sessionManagement": true,
// Use Timespan syntax: "days, hours, minutes, seconds"
"sessionTimeout": "0,0,30,0",
"sessionStorage": "sessions",
"sessionCluster": true
```

{% endstep %}

{% step %}
### Configure Client Storage (Optional)

{% hint style="warning" %}
**Client Scope Compatibility:** The `client` scope is ONLY supported when using the `bx-compat-cfml` module for CFML application modes. This is a legacy CFML feature and is not available in native BoxLang applications.
{% endhint %}

Client scope storage requires the `bx-compat-cfml` module. Configure it similarly to session storage:

```javascript
class {
    this.name = "myApp";

    // Enable client management
    this.clientManagement = true;
    this.clientTimeout = createTimeSpan( 90, 0, 0, 0 ); // 90 days

    // Configure Redis client storage
    this.clientStorage = "clients"; // Name of the Redis cache
    this.clientCluster = true;      // Enable distributed client scopes
}

```

{% endstep %}

{% endstepper %}

## 🔧 Session Storage Settings

### sessionStorage

**Type:** string
**Required:** Yes

The name of the cache defined in your `boxlang.json`  or the `Application.bx` that you wish to store sessions in. This must match a cache name in your `caches` configuration.

**Example:**

```javascript
this.sessionStorage = "sessions";
```

### sessionCluster

**Type:** boolean
**Default:** `false`

Controls whether servers operate in isolated cluster mode when using distributed session storage:

| Value | Behavior | Use Case |
|-------|----------|----------|
| `true` | Servers operate independently within a cluster. Each server maintains its own session state without announcing shutdown events to other cluster members. Sessions remain operational on other servers even when individual servers go down. | Multi-server environments where servers should operate independently without coordinating lifecycle events. Useful for zero-downtime deployments and rolling restarts. |
| `false` | Normal single-server operation. Session data is stored in Redis for persistence across restarts but no cluster coordination is performed. | Single server deployments or when you want standard single-server behavior with Redis-backed session persistence. |

**Best Practices:**

* **Use `true` when:**
  * Running multiple web servers in a load-balanced environment
  * You need servers to operate independently without coordinated shutdowns
  * Implementing rolling restarts or zero-downtime deployments
  * Sessions should remain active on other servers when one server goes down

* **Use `false` when:**
  * Single server deployment
  * Session persistence across restarts is the primary goal
  * You don't need cluster-aware session management

## 🔧 Client Storage Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `clientManagement` | boolean | `false` | Enable client scope management |
| `clientTimeout` | timespan | - | How long client variables persist (typically days/weeks) |
| `clientStorage` | string | - | Name of the cache to use for client storage |
| `clientCluster` | boolean | `false` | Enable cluster mode for distributed client scopes |

## 📋 Complete Configuration Examples

### Example 1: Basic Session Storage

Single application with session persistence across restarts:

```javascript
// Application.bx
class {
    this.name = "MyBasicApp";

    // Session configuration
    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan( 0, 0, 30, 0 );
    this.sessionStorage = "sessions";
    this.sessionCluster = false; // Single server
}
```

```json
// boxlang.json
{
  "caches": {
    "sessions": {
      "provider": "Redis",
      "properties": {
        "host": "127.0.0.1",
        "port": "6379",
        "keyprefix": "myapp-sessions"
      }
    }
  }
}
```

### Example 2: Distributed Sessions (Load-Balanced)

Multiple web servers sharing session data:

```javascript
// Application.bx
class {
    this.name = "MyDistributedApp";

    // Session configuration
    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan( 0, 1, 0, 0 ); // 1 hour
    this.sessionStorage = "sessions";
    this.sessionCluster = true; // Enable for multiple servers
}
```

```json
// boxlang.json
{
  "caches": {
    "sessions": {
      "provider": "RedisCluster",
      "properties": {
        "hosts": "node1.redis.local,node2.redis.local,node3.redis.local",
        "port": "6379",
        "password": "${REDIS_PASSWORD}",
        "useSSL": true,
        "keyprefix": "myapp-sessions",
        "maxConnections": 1000,
        "maxAttempts": 10
      }
    }
  }
}
```

### Example 3: Session + Client Storage

Combined session and client scope storage:

```javascript
// Application.bx
class {
    this.name = "MyFullApp";

    // Session configuration
    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan( 0, 0, 45, 0 ); // 45 minutes
    this.sessionStorage = "sessions";
    this.sessionCluster = true;

    // Client configuration
    this.clientManagement = true;
    this.clientTimeout = createTimeSpan( 90, 0, 0, 0 ); // 90 days
    this.clientStorage = "clients";
    this.clientCluster = true;
}
```

```json
// boxlang.json
{
  "caches": {
    "sessions": {
      "provider": "Redis",
      "properties": {
        "host": "redis.mycompany.com",
        "port": "6379",
        "database": "0",
        "password": "${REDIS_PASSWORD}",
        "useSSL": true,
        "keyprefix": "myapp-sessions",
        "maxConnections": 100
      }
    },
    "clients": {
      "provider": "Redis",
      "properties": {
        "host": "redis.mycompany.com",
        "port": "6379",
        "database": "1",
        "password": "${REDIS_PASSWORD}",
        "useSSL": true,
        "keyprefix": "myapp-clients",
        "maxConnections": 50
      }
    }
  }
}
```

### Example 4: High-Availability Production Setup

Production-ready configuration with Redis Sentinel:

```javascript
// Application.bx
class {
    this.name = "ProductionApp";

    // Session configuration
    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan( 0, 2, 0, 0 ); // 2 hours
    this.sessionStorage = "sessions";
    this.sessionCluster = true;
}
```

```json
// boxlang.json
{
  "caches": {
    "sessions": {
      "provider": "RedisSentinel",
      "properties": {
        "sentinels": "sentinel1.mycompany.com:26379,sentinel2.mycompany.com:26379,sentinel3.mycompany.com:26379",
        "database": "0",
        "password": "${REDIS_PASSWORD}",
        "useSSL": true,
        "keyprefix": "prodapp-sessions",
        "timeout": 2000,
        "readTimeout": 2000,
        "maxConnections": 500,
        "maxAttempts": 10,
        "maxIdleConnections": 50
      }
    }
  }
}
```

## 🔧 Usage

Once configured, use session and client scopes as you normally would. BoxLang handles Redis storage automatically:

```javascript
// Set session variables
session.userID = 12345;
session.username = "john.doe";
session.preferences = {
    "theme": "dark",
    "language": "en"
};

// Read session variables
var userID = session.userID;
var username = session.username;

// Client scope (requires bx-compat-cfml)
client.lastVisit = now();
client.visitCount = ( client.visitCount ?: 0 ) + 1;

// Check if variable exists
if( structKeyExists( session, "userID" ) ) {
    // User is logged in
}

// Remove session variable
structDelete( session, "tempData" );

// Clear entire session
sessionInvalidate();
```

## 🎯 Best Practices

### Cache Naming and Prefixes

* Use descriptive cache names: `sessions`, `clients`, `user-sessions`
* Always use unique key prefixes to avoid collisions: `myapp-sessions`, `myapp-clients`
* Different applications should use different prefixes
* Use different databases or prefixes for session vs. client storage

### Timeout Configuration

* **Session timeout** - Typically 15-60 minutes for web applications
* **Client timeout** - Typically 30-90 days for long-term client tracking
* Consider your application's security requirements
* Shorter timeouts = better security but more frequent re-authentication

### Database Organization

* Use separate Redis databases for different scope types:
  * Database 0: Sessions
  * Database 1: Clients
  * Database 2: Application cache
* This allows independent monitoring and clearing of different data types

### Security Considerations

* Always use SSL/TLS in production (`useSSL: true`)
* Use strong passwords for Redis authentication
* Consider using Redis ACL for fine-grained access control
* Store sensitive configuration in environment variables
* Never commit passwords to version control

### Performance Optimization

* Set `sessionCluster = false` for single-server deployments
* Adjust `maxConnections` based on concurrent user load
* Monitor Redis memory usage and configure eviction policies
* Use connection pooling settings appropriate for your traffic
* Consider using Redis Cluster or Sentinel for high-traffic applications

### Monitoring

Track these metrics in production:

* Session count (active users)
* Cache hit/miss ratios
* Redis memory usage
* Connection pool utilization
* Session creation/expiration rates

## 🚨 Troubleshooting

### Sessions Not Persisting

**Check:**

* Verify cache name matches between `Application.bx` and `boxlang.json`
* Ensure Redis server is running and accessible
* Check Redis logs for connection errors
* Verify `sessionStorage` is set correctly

### Performance Issues

**Solutions:**

* Increase `maxConnections` if you see pool exhaustion
* Enable `sessionCluster = false` for single-server setups
* Check network latency between application and Redis server
* Monitor Redis memory and CPU usage

### Session Data Not Shared Across Servers

**Check:**

* Verify `sessionCluster = true` on all servers
* Ensure all servers point to the same Redis instance/cluster
* Check that `keyprefix` is identical across all servers
* Verify time synchronization across servers (for TTL)

### Client Scope Not Working

**Check:**

* Ensure `bx-compat-cfml` module is installed
* Verify `clientManagement = true` in Application.bx
* Check that client cache is configured properly
* Verify cookies are enabled in the browser
