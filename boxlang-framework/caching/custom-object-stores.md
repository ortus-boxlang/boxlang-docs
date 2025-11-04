---
description: Object stores are the foundational storage layer of the BoxLang cache engine
---

# Custom Object Stores

Object stores are the foundational storage layer of the BoxLang cache engine. They provide the actual mechanism for storing, retrieving, and managing cached objects. While cache providers coordinate user interactions and act as a service layer, object stores handle the low-level data persistence and retrieval operations.

## What are Object Stores?

An object store is a pluggable storage backend that implements the `IObjectStore` interface. It determines how and where your cached data is stored - whether in memory, on disk, or in any custom storage mechanism you design.

### **Key Characteristics:**

* **Storage Abstraction**: Object stores abstract the underlying storage mechanism from the cache provider
* **Key Handling**: They work with `Key` objects, allowing for case-sensitive or case-insensitive storage decisions
* **Entry Management**: All data is stored as `ICacheEntry` objects for consistency across implementations
* **Eviction Support**: Integration with configurable eviction policies (LRU, MRU, LFU, etc.)
* **Lifecycle Management**: Support for initialization, shutdown, and maintenance operations

### Built-in Object Store Types

BoxLang provides several built-in object store implementations:

* **ConcurrentHashMap**: Fast in-memory storage using Java's ConcurrentHashMap
* **ConcurrentSoftReference**: Memory-conscious storage with soft references for automatic GC cleanup
* **Disk**: Persistent disk-based storage for cache durability
* **Custom**: Your own implementations

## The IObjectStore Interface

To create a custom object store, you must implement the `IObjectStore` interface in the Java language or in BoxLang by using `implements="java:ortus.boxlang.runtime.cache.store.IObjectStore`

```java
public interface IObjectStore {
    // Basic metadata
    public String getName();
    public IStruct getConfig();
    public ICacheProvider getProvider();

    // Lifecycle methods
    public IObjectStore init(ICacheProvider provider, IStruct config);
    public void shutdown();

    // Storage operations
    public void set(Key key, ICacheEntry entry);
    public void set(IStruct entries);
    public ICacheEntry get(Key key);
    public ICacheEntry getQuiet(Key key);

    // Bulk operations
    public IStruct get(Key... keys);
    public IStruct get(ICacheKeyFilter filter);
    public IStruct getQuiet(Key... keys);
    public IStruct getQuiet(ICacheKeyFilter filter);

    // Cache management
    public boolean clear(Key key);
    public IStruct clear(Key... keys);
    public void clearAll();
    public boolean clearAll(ICacheKeyFilter filter);

    // Introspection
    public Key[] getKeys();
    public Key[] getKeys(ICacheKeyFilter filter);
    public Stream<Key> getKeysStream();
    public Stream<Key> getKeysStream(ICacheKeyFilter filter);
    public boolean lookup(Key key);
    public IStruct lookup(Key... keys);
    public IStruct lookup(ICacheKeyFilter filter);

    // Maintenance
    public int getSize();
    public int flush();
    public void evict();
}
```

## Creating a Custom Object Store

### Step 1: Extend AbstractStore (Recommended)

While you can implement `IObjectStore` directly, extending `AbstractStore` provides useful functionality like eviction policy management:

```java
public class MyCustomStore extends AbstractStore {

    private Map<String, ICacheEntry> storage;

    @Override
    public IObjectStore init(ICacheProvider provider, IStruct config) {
        // Call parent initialization
        super.init(provider, config);

        // Initialize your storage mechanism
        this.storage = new ConcurrentHashMap<>();

        // Configure based on properties
        var initialCapacity = config.getAsInteger("initialCapacity", 1000);
        // ... additional configuration

        return this;
    }

    @Override
    public void shutdown() {
        // Clean up resources
        if (storage != null) {
            storage.clear();
            storage = null;
        }
    }

    // Implement required methods...
}
```

### Step 2: Implement Core Storage Methods

The most critical methods to implement are the storage operations:

```java
@Override
public void set(Key key, ICacheEntry entry) {
    storage.put(key.getName(), entry);
}

@Override
public ICacheEntry get(Key key) {
    ICacheEntry entry = storage.get(key.getName());
    if (entry != null) {
        // Update last accessed time
        entry.updateLastAccessed();
    }
    return entry;
}

@Override
public ICacheEntry getQuiet(Key key) {
    // Get without updating access metadata
    return storage.get(key.getName());
}

@Override
public boolean clear(Key key) {
    return storage.remove(key.getName()) != null;
}

@Override
public void clearAll() {
    storage.clear();
}

@Override
public int getSize() {
    return storage.size();
}
```

### Step 3: Implement Introspection Methods

Provide methods for cache inspection and filtering:

```java
@Override
public Key[] getKeys() {
    return storage.keySet().stream()
        .map(Key::of)
        .toArray(Key[]::new);
}

@Override
public Key[] getKeys(ICacheKeyFilter filter) {
    return storage.keySet().stream()
        .map(Key::of)
        .filter(filter)
        .toArray(Key[]::new);
}

@Override
public Stream<Key> getKeysStream() {
    return storage.keySet().stream().map(Key::of);
}

@Override
public Stream<Key> getKeysStream(ICacheKeyFilter filter) {
    return getKeysStream().filter(filter);
}

@Override
public boolean lookup(Key key) {
    return storage.containsKey(key.getName());
}
```

### Step 4: Implement Eviction Support

Integrate with the eviction policy system:

```java
@Override
public void evict() {
    ICachePolicy policy = getPolicy(); // From AbstractStore

    if (policy != null && getSize() > 0) {
        // Get eviction candidates
        Key[] candidates = policy.getEvictionCandidates(
            this,
            getKeysStream().collect(Collectors.toList())
        );

        // Remove candidates
        for (Key candidate : candidates) {
            clear(candidate);
        }
    }
}
```

### Step 5: Handle Bulk Operations

Implement bulk operations for better performance:

```java
@Override
public IStruct get(Key... keys) {
    IStruct results = new Struct();
    for (Key key : keys) {
        results.put(key, get(key));
    }
    return results;
}

@Override
public IStruct clear(Key... keys) {
    IStruct results = new Struct();
    for (Key key : keys) {
        results.put(key, clear(key));
    }
    return results;
}

@Override
public void set(IStruct entries) {
    entries.forEach((key, entry) -> {
        if (entry instanceof ICacheEntry) {
            set((Key) key, (ICacheEntry) entry);
        }
    });
}
```



## Configuration

You can register and use your custom object store via the caches configuration section by putting the full Java class path of the object store as the `objectStore` key

```java
// In your cache configuration
objectStore : "my.class.MyStore"
```

Or you can use the `createCache( name, provider, propertes )` method on the `CacheService` and pass in a class or object instance for the `objectStore`

```java
// Create and configure your store instance
MyCustomStore customStore = new MyCustomStore();

// Use it in cache configuration
myCache = cacheService.createCache( "myCache", "BoxCache", {
    "objectStore" : customStore
} );
```

## Best Practices

#### Performance Considerations

1. **Thread Safety**: Ensure your implementation is thread-safe as multiple threads will access it concurrently
2. **Efficient Lookups**: Optimize for fast key lookups as `get()` and `lookup()` are called frequently
3. **Bulk Operations**: Implement bulk operations efficiently rather than iterating single operations
4. **Memory Management**: Consider memory usage patterns, especially for in-memory stores

#### Error Handling

```java
@Override
public ICacheEntry get(Key key) {
    try {
        // Your storage retrieval logic
        return performStorageGet(key);
    } catch (StorageException e) {
        // Log the error but don't throw - return null for cache miss
        logger.warn("Storage error retrieving key {}: {}", key.getName(), e.getMessage());
        return null;
    } catch (Exception e) {
        // Unexpected errors should be thrown
        throw new BoxRuntimeException("Unexpected error in object store", e);
    }
}
```

#### Eviction Integration

```java
@Override
public void evict() {
    ICachePolicy policy = getPolicy();
    int maxObjects = getIntProperty("maxObjects", 10000);

    if (getSize() > maxObjects) {
        int itemsToEvict = getSize() - maxObjects;
        Key[] candidates = policy.selectEvictionCandidates(this, itemsToEvict);

        for (Key candidate : candidates) {
            clear(candidate);
        }
    }
}
```

#### Resource Management

```java
@Override
public void shutdown() {
    try {
        // Flush any pending operations
        flush();

        // Close connections/resources
        closeConnections();

        // Clear references
        cleanup();
    } catch (Exception e) {
        logger.error("Error during object store shutdown", e);
    }
}

@Override
public int flush() {
    int flushedCount = 0;
    // Implement persistence operations if applicable
    return flushedCount;
}
```

### Integration with Cache Providers

Your object store will be used by cache providers like `BoxCacheProvider`. The provider handles:

* Cache entry creation and metadata management
* Event announcements (insert, update, remove)
* Statistics tracking
* Eviction scheduling
* Configuration validation

Your object store focuses purely on storage operations, making the separation of concerns clean and maintainable.

### Testing Your Custom Store

Create comprehensive tests for your custom object store:

```java
@Test
public void testBasicOperations() {
    // Initialize store
    MyCustomStore store = new MyCustomStore();
    store.init(mockProvider, testConfig);

    // Test set/get
    Key testKey = Key.of("testKey");
    ICacheEntry entry = new BoxCacheEntry(/* parameters */);

    store.set(testKey, entry);
    ICacheEntry retrieved = store.get(testKey);

    assertNotNull(retrieved);
    assertEquals(entry.value(), retrieved.value());

    // Test clear
    assertTrue(store.clear(testKey));
    assertNull(store.get(testKey));

    // Cleanup
    store.shutdown();
}
```

### Conclusion

Custom object stores provide powerful extensibility for the BoxLang cache engine. By implementing the `IObjectStore` interface and following these patterns, you can create storage backends that meet your specific requirements, whether for performance, persistence, distribution, or integration with external systems.

The clean separation between cache providers and object stores ensures that your custom storage logic remains focused and testable while integrating seamlessly with the broader caching infrastructure.
