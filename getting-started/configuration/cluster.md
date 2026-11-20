---
description: Configure BoxLang cluster coordination through a shared cache
icon: network-wired
---

# Cluster

{% hint style="success" %}
New in BoxLang **1.20.0**.
{% endhint %}

The `cluster` section of `boxlang.json` lets a BoxLang node coordinate with other nodes through a shared cache. Clustered [scheduled tasks](../../boxlang-framework/asynchronous-programming/clustered-scheduled-tasks.md) are the first feature built on it. They run once per occurrence across the fleet instead of once per node, and the work is shared out.

## Configuration Structure

```json
{
  "cluster": {
    "enabled": false,
    "nodeId": null,
    "name": "default",
    "cacheName": "bxcluster",
    "heartbeatSeconds": 5
  }
}
```

## Configuration Properties

### enabled

**Type:** `boolean` **Default:** `false` **Description:** The master switch for this node. When `false`, nothing else in this section is used, and a task marked as clustered refuses to start.

### nodeId

**Type:** `string` **Default:** `null` **Description:** This node's identity. When `null`, BoxLang uses `{hostname}-{pid}`, which is unique per process. Set it when your platform gives you a stable pod or task name.

```json
"nodeId": "${HOSTNAME}"
```

### name

**Type:** `string` **Default:** `"default"` **Description:** The cluster name. Nodes with the same name see each other and share work. Different names never do, so one shared cache can serve several independent clusters.

### cacheName

**Type:** `string` **Default:** `"bxcluster"` **Description:** The cache used for coordination. It must be backed by a store every node can see, such as a distributed provider like Redis, a JDBC store, or a `FileSystemStore` on a shared volume.

```json
{
  "cluster": { "enabled": true, "cacheName": "bxcluster" },
  "caches": {
    "bxcluster": {
      "provider": "Redis",
      "properties": { "host": "redis.internal.example.com", "port": "6379" }
    }
  }
}
```

{% hint style="warning" %}
The bundled `default` cache is local to each JVM. Nodes sharing it never see each other.
{% endhint %}

### heartbeatSeconds

**Type:** `integer` **Default:** `5` **Description:** How often this node rewrites its record in the shared cache. A node is considered gone after three missed beats. The value must be greater than zero.

## Related Scheduler Settings

How occurrences are shared out is a scheduler policy, so it lives in the [`scheduler`](scheduler.md) section: `clusterMode`, `taskOverlapPolicy`, `shutdownGraceSeconds` and `shutdownInterruptGraceSeconds`.

## Related Configuration

* [Clustered Scheduled Tasks](../../boxlang-framework/asynchronous-programming/clustered-scheduled-tasks.md)
* [Scheduler](scheduler.md)
* [Caches](caches.md)
