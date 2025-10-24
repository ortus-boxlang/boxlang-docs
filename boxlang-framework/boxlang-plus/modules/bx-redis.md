---
icon: database
---

# Redis +

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

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-redis

# Using CommandBox to install for web servers.
box install bx-redis
```

### Configuration

#### `boxlang.json` configuration

The JSON configuration structure for boxlang for a single redis connection would be placed in the `caches` object in `boxlang.json`

**Single Node Provider Configuration example**

```
{
  "caches" : {
    "sessions": {
      "provider": "Redis",
      "properties": {
        "cacheKeyCaseSensitivity": "false",
        "database": "0",
        "idleConnections": "5",
        "maxConnections": "50",
        "password": "",
        "timeout": "2000",
        "useSSL": "false",
        "host": "127.0.0.1",
        "keyprefix": "resources",
        "port": "6379",
        "timeout" : 2000,
        "readTimeout" : 2000,
        "socketTimeout" : 2000,
        "poolWaittimeout" : 1000,
        "maxAttempts" : 10,
        "maxConnections": 1000,
        "maxIdleTime" : 30000,
        "maxIdleConnections" : 20
      }
    }
  }
}
```

**Cluster Provider Configuration example**

```
{
  "caches" : {
    "resources": {
      "provider": "RedisCluster",
      "properties": {
        "hosts": "node1.myrediscluster,node2.myrediscluster,node3.myrediscluster,",
        "keyprefix": "boxlang-cluster",
        "username": "${REDIS_CLUSTER_USERNAME}",
        "password": "${REDIS_CLUSTER_PASSWORD}",
        "port": "6379",
        "useSSL": "${REDIS_CLUSTER_USE_SSL:false}",
        "timeout" : 2000,
        "readTimeout" : 2000,
        "socketTimeout" : 2000,
        "poolWaittimeout" : 1000,
        "maxAttempts" : 10,
        "maxConnections": 1000,
        "maxIdleTime" : 30000,
        "maxIdleConnections" : 20
        "cacheKeyCaseSensitivity": "false",
      }
    }
  }
}
```

[**Sentinel**](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/) **Provider Configuration example**

```
{
  "caches" : {
    "resources": {
      "provider": "RedisSentinel",
      "properties": {
        "sentinels": "sentinel1.myhost.com:26379,sentinel2.myhost.com:26379",
        "keyprefix": "boxlang-sentinel",
        "username": "${REDIS_SENTINEL_USERNAME}",
        "password": "${REDIS_SENTINEL_PASSWORD}",
        "cacheKeyCaseSensitivity": "false",
        "database": "0",
        "idleConnections": "5",
        "maxConnections": "50",
        "password": "",
        "timeout": "2000",
        "useSSL": "false",
        "keyprefix": "resources",
        "timeout" : 2000,
        "readTimeout" : 2000,
        "socketTimeout" : 2000,
        "poolWaittimeout" : 1000,
        "maxAttempts" : 10,
        "maxConnections": 1000,
        "maxIdleTime" : 30000,
        "maxIdleConnections" : 20
      }
    }
  }
}
```

#### `Application.bx`/`Application.cfc` configuration

**Standalone**

```
this.caches[ "sessions" ] = {
  "provider": "Redis",
  "properties": {
    "cacheKeyCaseSensitivity": "false",
    "database": "0",
    "idleConnections": "5",
    "maxConnections": "50",
    "password": "",
    "timeout": "2000",
    "useSSL": "false",
    "host": "127.0.0.1",
    "keyprefix": "boxlang-sessions",
    "port": "6379",
    "timeout" : 2000,
    "socketTimeout" : 2000,
    "poolWaittimeout" : 1000,
    "maxConnections": 1000,
    "idleConnections": 10
  }
};
```

**Cluster**

```
this.caches[ "resources" ] = {
  "provider": "RedisCluster",
  "properties": {
    "hosts": "node1.myrediscluster,node2.myrediscluster,node3.myrediscluster,",
    "keyprefix": "boxlang-cluster",
    "username": myClusterUsername,
    "password": myClusterPassword,
    "port": "6379",
    "useSSL": false,
    "timeout" : 2000,
    "readTimeout" : 2000,
    "socketTimeout" : 2000,
    "poolWaittimeout" : 1000,
    "maxAttempts" : 10,
    "maxConnections": 1000,
    "maxIdleTime" : 30000,
    "maxIdleConnections" : 20
  }
};
```

#### Settings Summary



**Redis Standalone Server**

**Host**

The Redis server IP address or host name.

**Port**

The port of the Redis server.

**Logical Database**

The logical database to connect to in Redis. By default we connect to database 0.

**Username**

The Redis cluster username - only used when enabling [user-level access](https://docs.redis.com/latest/rs/security/access-control/manage-users/add-users/).

**Password**

The password of the Redis server, if any.

**SSL**

Enable SSL on the connection to the Redis Server.

**Connection Timeout**

The time in milliseconds to wait for a connection or throw an exception.

**Socket Timeout**

The cluster connection socket timeout in milliseconds

**Pool Timeout**

The the maximum amount of time, in milliseconds, to wait for a connection pool resource to become available

**Max Connections**

The maximum number of connections to allow to the Redis server.

**Idle Connections**

The maximum number of idle connections to keep in the pool to the Redis server

**Cache Key Prefix**

The default key prefix is `boxlang-cache`. This will automatically prefix EVERY single cache item that goes into Redis. This will allow you to avoid collisions if you decide to register many Lucee caches or just to distinguish what comes from which cache connection.

**Cache Key Case Sensitivity**

By default all cache keys are transformed to lowercase to avoid any casing issues. However, if you want case sensitivity, then turn this option on.



**Redis Cluster Provider Settings**

**Host(s)**

Enter a comma-delimited list of all the IPs or hosts in the cluster. Not all are needed, but you should at least enter some to have redundancy.

**Port**

The port of the Redis cluster.

**SSL**

Whether SSL transport is enabled

**Username**

The Redis cluster username - only used when enabling [user-level access](https://docs.redis.com/latest/rs/security/access-control/manage-users/add-users/).

**Password**

The Redis cluster password

**Connection Timeout**

The time in milliseconds to wait for a connection or throw an exception.

**Read Timeout**

The timeout for a read of data from the cluster - defaults to the connection timeout

**Socket Timeout**

The cluster connection socket timeout in milliseconds

**Pool Timeout**

The the maximum amount of time, in milliseconds, to wait for a connection pool resource to become available

**Max Connections**

The maximum number of connections to the cluster allowed per pool - defaults to 50

**Idle Timeout**

The max idle time, in milliseconds, for a connection to remain in the pool.

**Max Idle Connections**

The maximum number of concurrently idle connections to retain in the pool

**Max Attempts**

The maximum number of connection attempts to make to the cluster.

**Cache Key Prefix**

The default key prefix is `lucee-cache`. This will automatically prefix EVERY single cache item that goes into Redis. This will allow you to avoid collisions if you decide to register many Lucee caches or just to distinguish what comes from which cache connection.

**Cache Key Case Sensitivity**

By default all cache keys are transformed to lowercase to avoid any casing issues. However, if you want case sensitivity, then turn this option on.



**Redis Sentinels**

**Sentinels**

A comma delimited list of Sentinel servers in `{host}:port` format.  Example:

```
sentinel1.myhost.com:26379,sentinel2.myhost.com:26379
```

**Username**

The Redis cluster username - only used when enabling [user-level access](https://docs.redis.com/latest/rs/security/access-control/manage-users/add-users/).

**Password**

The password of the Redis server, if any.

**SSL**

Enable SSL on the connection to the Redis Server.

**Connection Timeout**

The time in milliseconds to wait for a connection or throw an exception.

**Socket Timeout**

The cluster connection socket timeout in milliseconds

**Pool Timeout**

The the maximum amount of time, in milliseconds, to wait for a connection pool resource to become available

**Max Connections**

The maximum number of connections to allow to the Redis server.

**Idle Connections**

The maximum number of idle connections to keep in the pool to the Redis server

**Cache Key Prefix**

The default key prefix is `boxlang-cache`. This will automatically prefix EVERY single cache item that goes into Redis. This will allow you to avoid collisions if you decide to register many Lucee caches or just to distinguish what comes from which cache connection.

**Cache Key Case Sensitivity**

By default all cache keys are transformed to lowercase to avoid any casing issues. However, if you want case sensitivity, then turn this option on.

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [Forgebox listing](https://forgebox.io/view/bx-redis) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27050\&issuetype=1).
