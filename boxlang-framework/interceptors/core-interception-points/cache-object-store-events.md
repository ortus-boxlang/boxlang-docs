# Cache Object Store Events

These events occur when individual cache elements are manipulated inside a cache store. They are announced on the **cache provider's interceptor pool**, meaning listeners must be registered directly on a specific cache provider instance — not on the global interceptor pool.

> **Note:** `afterCacheElementInsert` and `afterCacheElementUpdated` are mutually exclusive — a single `set()` call fires only one of them depending on whether the key already existed.

| Event Name                  | Cancellable | Description                                                              |
| --------------------------- | :---------: | ------------------------------------------------------------------------ |
| `afterCacheElementInsert`   |     No      | Fired after a **new** cache key is inserted for the first time.          |
| `beforeCacheElementRemoved` |     No      | Fired before a cache element is removed, allowing pre-removal reactions. |
| `afterCacheElementRemoved`  |     No      | Fired after a cache element removal attempt completes.                   |
| `afterCacheElementUpdated`  |     No      | Fired after an **existing** cache key's value is replaced.               |

* [`afterCacheElementInsert`](cache-object-store-events.md#aftercacheelementinsert)
* [`beforeCacheElementRemoved`](cache-object-store-events.md#beforecacheelementremoved)
* [`afterCacheElementRemoved`](cache-object-store-events.md#aftercacheelementremoved)
* [`afterCacheElementUpdated`](cache-object-store-events.md#aftercacheelementupdated)

## afterCacheElementInsert

Fired after a brand-new key-value pair is stored in the cache (i.e., the key did not previously exist).

### Data Structure

| Data Key | Type             | Description                              |
| -------- | ---------------- | ---------------------------------------- |
| `cache`  | `ICacheProvider` | The cache provider the entry belongs to. |
| `key`    | `Key`            | The cache key that was inserted.         |
| `entry`  | `ICacheEntry`    | The newly created cache entry object.    |

### Example

```groovy
class myListener{
	function afterCacheElementInsert( struct data ){
		var cache = data.cache;
		var key   = data.key;
		var entry = data.entry;
		// React to the new cache entry
	}
}
```

## beforeCacheElementRemoved

Fired before a cache element is removed from the store. Use this for pre-removal reactions such as cleanup, logging, or dependent invalidations.

### Data Structure

| Data Key | Type             | Description                              |
| -------- | ---------------- | ---------------------------------------- |
| `cache`  | `ICacheProvider` | The cache provider the entry belongs to. |
| `key`    | `Key`            | The cache key about to be removed.       |
| `entry`  | `ICacheEntry`    | The cache entry about to be removed.     |

### Example

```groovy
class myListener{
	function beforeCacheElementRemoved( struct data ){
		var cache = data.cache;
		var key   = data.key;
		var entry = data.entry;
		// Perform pre-removal cleanup or logging
	}
}
```

## afterCacheElementRemoved

Fired after a cache element removal attempt completes, whether or not the key existed.

### Data Structure

| Data Key | Type             | Description                              |
| -------- | ---------------- | ---------------------------------------- |
| `cache`  | `ICacheProvider` | The cache provider the entry belongs to. |
| `key`    | `Key`            | The cache key that was removed.          |
| `entry`  | `ICacheEntry`    | The cache entry that was removed.        |

### Example

```groovy
class myListener{
	function afterCacheElementRemoved( struct data ){
		var cache = data.cache;
		var key   = data.key;
		var entry = data.entry;
		// React to the completed removal
	}
}
```

## afterCacheElementUpdated

Fired after an existing cache key's value has been replaced with a new value.

### Data Structure

| Data Key | Type             | Description                              |
| -------- | ---------------- | ---------------------------------------- |
| `cache`  | `ICacheProvider` | The cache provider the entry belongs to. |
| `key`    | `Key`            | The cache key that was updated.          |
| `entry`  | `ICacheEntry`    | The updated cache entry object.          |

### Example

```groovy
class myListener{
	function afterCacheElementUpdated( struct data ){
		var cache = data.cache;
		var key   = data.key;
		var entry = data.entry;
		// React to the updated cache entry
	}
}
```
