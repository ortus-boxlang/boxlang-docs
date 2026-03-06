# Cache Object Store Events

These events occur when individual cache elements are manipulated inside a cache store. They are announced on the **cache provider's interceptor pool**, meaning listeners must be registered directly on a specific cache provider instance — not on the global interceptor pool.

| Event Name                  | Cancellable | Description                                                              |
| --------------------------- | :---------: | ------------------------------------------------------------------------ |
| `afterCacheElementInsert`   |     No      | Fired after a **new** cache key is inserted for the first time.          |
| `beforeCacheElementRemoved` |     No      | Fired before a cache element is removed, allowing pre-removal reactions. |
| `afterCacheElementRemoved`  |     No      | Fired after a cache element removal attempt completes.                   |
| `afterCacheElementUpdated`  |     No      | Fired after an **existing** cache key's value is replaced.               |

> **Note:** `afterCacheElementInsert` and `afterCacheElementUpdated` are mutually exclusive — a single `set()` call fires only one of them depending on whether the key already existed.

---

## `afterCacheElementInsert`

Fired after a brand-new key-value pair is stored in the cache (i.e., the key did not previously exist).

**Event Data:**

| Key     | Type             | Description                              |
| ------- | ---------------- | ---------------------------------------- |
| `cache` | `ICacheProvider` | The cache provider the entry belongs to. |
| `key`   | `Key`            | The cache key that was inserted.         |
| `entry` | `ICacheEntry`    | The newly created cache entry object.    |

**Example:**

```java
cache.getInterceptorPool().register( data -> {
    ICacheProvider provider = ( ICacheProvider ) data.get( "cache" );
    Key            key      = ( Key ) data.get( "key" );
    ICacheEntry    entry    = ( ICacheEntry ) data.get( "entry" );
    // react to the new entry
    return false;
}, BoxEvent.AFTER_CACHE_ELEMENT_INSERT.key() );
