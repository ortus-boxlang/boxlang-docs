---
description: This configures the caches in the runtime
icon: server
---

# Caches

<figure><img src="../../.gitbook/assets/BxCache Overview.png" alt=""><figcaption><p>Overview</p></figcaption></figure>

BoxLang comes bundled with an enterprise caching engine that can be configured with different settings and backend object stores.  It is also can give you the ability to register caches that adhere to our BoxCache interface (`ICacheProvider`) to create an implementation agnostic API.  Apart from the core providers we create, we also have several in our + subscriptions and anybody can build custom providers as well.

You can also define [per-application caches](../../boxlang-framework/applicationbx.md) by defining them in the `Application.bx` file in your applications.

## Default Caches

Every BoxLang runtime comes pre-configured with the following caches that are mandatory for operation:

<table><thead><tr><th width="180">Cache</th><th>Hint</th></tr></thead><tbody><tr><td><code>default</code></td><td>The default cache in BoxLang is used for queries, templates, and many more internal usages.</td></tr><tr><td><code>bxSessions</code></td><td>If you activate session management in your web or client applications, user session information will be stored here.</td></tr><tr><td><code>bxRegex</code></td><td>This is where all dynamic regular expressions are compiled and kept.</td></tr></tbody></table>

{% code title="boxlang.json" %}
```json
"caches": {
	// The configuration for the BoxLang `default` cache.  If empty, we use the defaults
	// See the ortus.boxlang.runtime.config.segments.CacheConfig for all the available settings
	// This is used by query caching, template caching, and other internal caching.
	// You can use the cache() BIF in order to get access to the default cache.
	"default": {
		"provider": "BoxCacheProvider",
		"properties": {
			// How many to evict at a time once a policy is triggered
			"evictCount": 1,
			// The eviction policy to use: Least Recently Used
			// Other policies are: LRU, LFU, FIFO, LIFO, RANDOM
			"evictionPolicy": "LRU",
			// The free memory percentage threshold to trigger eviction
			// 0 = disabled, 1-100 = percentage of available free memory in heap
			// If the threadhold is reached, the eviction policy is triggered
			"freeMemoryPercentageThreshold": 0,
			// The maximum number of objects to store in the cache
			"maxObjects": 1000,
			// The maximum in seconds to keep an object in the cache since it's last access
			// So if an object is not accessed in this time or greater, it will be removed from the cache
			"defaultLastAccessTimeout": 1800,
			// The maximum time in seconds to keep an object in the cache regardless if it's used or not
			// A default timeout of 0 = never expire, careful with this setting
			"defaultTimeout": 3600,
			// The object store to use to store the objects.
			// The default is a ConcurrentStore which is a memory sensitive store
			"objectStore": "ConcurrentStore",
			// The frequency in seconds to check for expired objects and expire them using the policy
			// This creates a BoxLang task that runs every X seconds to check for expired objects
			"reapFrequency": 120,
			// If enabled, the last access timeout will be reset on every access
			// This means that the last access timeout will be reset to the defaultLastAccessTimeout on every access
			// Usually for session caches or to simulate a session
			"resetTimeoutOnAccess": false,
			// If enabled, the last access timeout will be used to evict objects from the cache
			"useLastAccessTimeouts": true
		}
	},
	// This is the holder of all sessions in a BoxLang runtime.
	// The keys are prefixed by application to create separation.
	"bxSessions": {
		"provider": "BoxCacheProvider",
		"properties": {
			// How many objects to evict when the cache is full
			"evictCount": 1,
			// The eviction policy to use: FIFO, LFU, LIFO, LRU, MFU, MRU, Random
			"evictionPolicy": "LRU",
			// The maximum number of objects the cache can hold
			"maxObjects": 100000,
			// How long should sessions last for in seconds. Default is 60 minutes.
			"defaultTimeout": 3600,
			// The object store to use to store the objects.
			// The default is a ConcurrentStore which is a thread safe and fast storage.
			// Available Stores are: BlackHoleStore, ConcurrentSoftReferenceStore, ConcurrentStore, FileSystemStore, Your own.
			"objectStore": "ConcurrentStore",
			// The free memory percentage threshold to start evicting objects
			// Only use if memory is constricted and you need to relieve cache pressure
			// Please note that this only makes sense depending on which object store you use.
			"freeMemoryPercentageThreshold": 0,
			// The frequency in seconds to check for expired objects and expire them using the policy
			// This creates a BoxLang task that runs every X seconds to check for expired objects
			// Default is every 2 minutes
			"reapFrequency": 120,
			// This makes a session extend it's life when accessed.  So if a users uses anything or puts anything
			// In session, it will re-issue the timeout.
			"resetTimeoutOnAccess": true,
			// Sessions don't rely on the last access timeouts but on the default timeout only.
			"useLastAccessTimeouts": false
		}
	},
	// Stores all dynamic regular expressions used in the runtime
	"bxRegex": {
		"provider": "BoxCacheProvider",
		"properties": {
			"evictCount": 1,
			"evictionPolicy": "LRU",
			"freeMemoryPercentageThreshold": 0,
			"maxObjects": 500,
			// 30 minutes ifnot used
			"defaultLastAccessTimeout": 1800,
			// 60 minutes default
			"defaultTimeout": 3600,
			"objectStore": "ConcurrentSoftReferenceStore",
			"reapFrequency": 120,
			"resetTimeoutOnAccess": false,
			"useLastAccessTimeouts": true
		}
	}
},
```
{% endcode %}

{% include "../../.gitbook/includes/boxcache-providers.md" %}

## Configuration

Every cache must be placed inside the `caches`object with a unique name key.  The value of that key contains:

* `provider` - The name of a core provider or a full classpath to use. Ex: `BoxCacheProvider` which is the core one, or a module collaborated class or class path class: `ortus.boxlang.modules.redis.RedisCache`
* `properties` - An object of configuration for the provider.

```json
"myCache" : {
    "provider" : "BoxCacheProvider",
    "properties" : {}
}
```



## BoxCache Provider

Our `BoxCacheProvider`is an enterprise-level cache designed to be fast and event-driven.  Here are the available configuration options.

### Object Stores

{% include "../../.gitbook/includes/boxcache-stores.md" %}

### Global Properties

Here are the global properties for all object stores.

#### evictCount

How many objects can be evicted once a policy is triggered?  The default is **1.**

```json
"evictCount" : 1
```

#### evictionPolicy

The eviction policy to use.  The available policies are:

* **LRU** (default): Least Recently Used
* **LFU**: Least Frequently Used
* **FIFO**: First in First out
* **LIFO**: Last in Last Out
* **RANDOM**: Randomly evict objects

```json
"evictionPolicy" : "Random"
```

#### freeMemoryPercentageThreshold

The free memory percentage threshold to trigger eviction 0 = disabled, 1-100 = percentage of available free memory in heap.   If the threshold is reached, the eviction policy is triggered.  The default is 0.

```json
"freeMemoryPercentageThreshold" : 10
```

#### maxObjects

The maximum number of objects to store in the cache. The default is 1000

```json
"maxObjects" : 1000
```

#### defaultLastAccessTimeout

The maximum number of seconds an object can be kept in the cache since its last access. If an object is not accessed at this time or greater, it will be removed from the cache. The default is 1800 seconds or 30 minutes.

```json
"defaultLastAccessTimeout" : 1800
```

#### defaultTimeout

The maximum time in seconds to keep an object in the cache regardless if it's used or not.  A default timeout of 0 = never expire, careful with this setting.  The default is 3600 seconds or 60 minutes.

```json
"defaultTimeout" : 3600
```

#### objectStore

The object store to use to store the objects.  The default is a `ConcurrentStore.`

```json
"objectStore" : "FileSystemStore"
```

#### `reapFrequency`

The frequency in seconds to check for expired objects and expire them using the policy.  This creates a BoxLang task that runs every X seconds to check for expired objects.  The default is 120 seconds or 2 minutes.

```json
"reapFrequency" : 240
```

#### resetTimeoutOnAccess

If enabled, the last access timeout will be reset on every access for the cache entry.  This means that the last access timeout will be reset to the `defaultLastAccessTimeout` on every access. Usually for session caches or to simulate a session.  The default is false.

```json
"resetTimeoutOnAccess" : true
```

#### useLastAccessTimeouts

If enabled, the last access timeout will be used to evict objects from the cache.  The default is true.

```json
"useLastAccessTimeouts" : true
```



### File System Store

The file system store leverages a destination `directory` and stores all cache items as serialized entities on disk.  It is highly efficient and fast considering it's a disk cache.

#### directory

The absolute path of the directory that will hold all the serialized cache entries on disk.

