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
