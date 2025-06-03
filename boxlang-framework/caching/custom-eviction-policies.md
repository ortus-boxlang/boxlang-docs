---
description: >-
  Eviction policies determine which cached objects should be removed when the
  cache reaches its capacity limits or memory thresholds.
---

# Custom Eviction Policies

Eviction policies determine which cached objects should be removed when the cache reaches its capacity limits or memory thresholds. While BoxLang provides several built-in eviction policies, you can create custom policies to implement specialized eviction strategies tailored to your application's specific needs.

## Understanding Eviction Policies

#### What are Eviction Policies?

Eviction policies are algorithms that decide which cached entries to remove when:

* The cache reaches its maximum object count (`maxObjects`)
* Memory usage exceeds the configured threshold (`freeMemoryPercentageThreshold`)
* Manual eviction is triggered through cache maintenance operations

#### When Eviction Occurs

Eviction is triggered automatically by the cache system during:

* **Object Storage**: When adding new items would exceed cache limits
* **Memory Pressure**: When JVM memory usage crosses the configured threshold
* **Scheduled Maintenance**: During periodic reaping operations
* **Manual Triggers**: When explicitly calling eviction methods

#### Policy Selection Impact

The choice of eviction policy significantly affects:

* **Cache Hit Rates**: How often requested data is found in the cache
* **Application Performance**: Response times for cached vs. uncached operations
* **Memory Efficiency**: How well the cache utilizes available memory
* **Data Consistency**: Whether important data remains accessible

## Built-in Eviction Policies

BoxLang includes seven core eviction policies:

<table><thead><tr><th width="266.56622314453125">Policy</th><th>Purpose</th></tr></thead><tbody><tr><td><strong>LRU</strong> <br>(Least Recently Used)</td><td>Evicts the objects that haven't been accessed for the longest time. Best for applications with temporal locality where recently accessed items are more likely to be accessed again. Ideal for general-purpose caching scenarios.</td></tr><tr><td><strong>MRU</strong> <br>(Most Recently Used)</td><td>Evicts the most recently accessed objects first. Useful when you want to keep older, established data and remove newly added items. Good for scenarios where recent additions are less valuable than historical data.</td></tr><tr><td><strong>LFU</strong><br> (Least Frequently Used)</td><td>Evicts objects with the lowest access frequency count. Maintains items that are accessed often, regardless of when they were last accessed. Perfect for caching frequently requested data like popular products or common API responses.</td></tr><tr><td><strong>MFU</strong> <br>(Most Frequently Used)</td><td>Evicts the most frequently accessed objects first. Counterintuitive but useful in scenarios where you want to cycle out "hot" data to make room for less popular items that might become important. Rare use case but valuable for specialized applications.</td></tr><tr><td><strong>FIFO</strong> <br>(First In, First Out)</td><td>Evicts objects in the order they were added to the cache. Simple queue-based eviction that doesn't consider access patterns. Good for time-sensitive data where older entries naturally become less relevant, like news feeds or log entries.</td></tr><tr><td><strong>LIFO</strong> <br>(Last In, First Out)</td><td>Evicts the most recently added objects first, like a stack. Keeps older established data while removing newer additions. Useful when you want to maintain a stable core dataset and only temporarily cache additional items.</td></tr><tr><td><strong>Random</strong></td><td>Evicts objects randomly without considering access patterns or insertion order. Provides consistent average performance without the overhead of tracking access metadata. Good for scenarios where no clear access pattern exists or when you want to avoid worst-case behaviors of other policies.</td></tr></tbody></table>

## The ICachePolicy Interface

To create a custom eviction policy, you must implement the `ICachePolicy` interface:

```java
public interface ICachePolicy {
    
    /**
     * Select candidates for eviction from the cache
     *
     * @param store The object store containing cached entries
     * @param keys The available keys to consider for eviction
     * @param evictionCount The number of items that should be evicted
     *
     * @return An array of keys that should be evicted
     */
    Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount);
    
    /**
     * Get the name of this eviction policy
     *
     * @return The policy name
     */
    String getName();
    
    /**
     * Initialize the policy with configuration options
     *
     * @param config Configuration parameters specific to this policy
     */
    void init(IStruct config);
    
    /**
     * Reset any internal state or statistics
     */
    void reset();
}
```

## Creating Custom Eviction Policies

#### Language Support

Custom eviction policies can be implemented in both **Java** and **BoxLang**:

* **Java**: Standard Java class implementation using the `ICachePolicy` interface
* **BoxLang**: BoxLang component using the `implements="java:classpath"` approach to implement the Java interface

**BoxLang Implementation Example**

```javascript
/**
 * Custom eviction policy implemented in BoxLang
 */
class implements="java:ortus.boxlang.runtime.cache.policies.ICachePolicy" {
    
    property name="policyName" default="BoxLangCustom";
    property name="config" type="struct";
    
    /**
     * Initialize the policy
     */
    function init( required struct config ) {
        variables.config = arguments.config;
    }
    
    /**
     * Get the policy name
     */
    function getName() {
        return variables.policyName;
    }
    
    /**
     * Reset policy state
     */
     function reset() {
        // Reset any internal state
    }
    
    /**
     * Select eviction candidates
     */
     array function selectEvictionCandidates(
        required any store,
        required array keys,
        required numeric evictionCount
    ) {
        // Your BoxLang eviction logic here
        var candidates = [];
        
        // Example: simple FIFO approach
        for (var i = 1; i <= min(arrayLen(arguments.keys), arguments.evictionCount); i++) {
            arrayAppend(candidates, arguments.keys[i]);
        }
        
        return candidates;
    }
}
```

#### Step 1: Implement the Interface (Java)

```java
package com.mycompany.cache.policies;

import java.util.List;
import java.util.stream.Collectors;
import ortus.boxlang.runtime.cache.policies.ICachePolicy;
import ortus.boxlang.runtime.cache.store.IObjectStore;
import ortus.boxlang.runtime.scopes.Key;
import ortus.boxlang.runtime.types.IStruct;

public class CustomEvictionPolicy implements ICachePolicy {
    
    private String name = "Custom";
    private IStruct config;
    
    @Override
    public String getName() {
        return this.name;
    }
    
    @Override
    public void init(IStruct config) {
        this.config = config;
        // Initialize any policy-specific configuration
    }
    
    @Override
    public void reset() {
        // Reset any internal counters or state
    }
    
    @Override
    public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
        // Implement your custom eviction logic here
        return new Key[0];
    }
}
```

#### Step 2: Implement Selection Logic

Here are several examples of custom eviction policies:

**Size-Based Eviction Policy**

Evicts the largest objects first to free up the most memory:

```java
public class SizeBasedEvictionPolicy implements ICachePolicy {
    
    @Override
    public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
        return keys.stream()
            .map(key -> {
                ICacheEntry entry = store.getQuiet(key);
                return new KeySizePair(key, calculateSize(entry));
            })
            .sorted((a, b) -> Long.compare(b.size, a.size)) // Largest first
            .limit(evictionCount)
            .map(pair -> pair.key)
            .toArray(Key[]::new);
    }
    
    private long calculateSize(ICacheEntry entry) {
        if (entry == null) return 0;
        
        Object value = entry.value().get();
        if (value == null) return 0;
        
        // Implement size calculation logic based on your needs
        if (value instanceof String) {
            return ((String) value).length() * 2; // Rough char size
        } else if (value instanceof byte[]) {
            return ((byte[]) value).length;
        } else {
            // Use serialization size or estimated object size
            return estimateObjectSize(value);
        }
    }
    
    private static class KeySizePair {
        final Key key;
        final long size;
        
        KeySizePair(Key key, long size) {
            this.key = key;
            this.size = size;
        }
    }
}
```

**Priority-Based Eviction Policy**

Evicts objects based on custom priority metadata:

```java
public class PriorityBasedEvictionPolicy implements ICachePolicy {
    
    private static final String PRIORITY_KEY = "priority";
    private static final int DEFAULT_PRIORITY = 5;
    
    @Override
    public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
        return keys.stream()
            .map(key -> {
                ICacheEntry entry = store.getQuiet(key);
                int priority = getPriority(entry);
                return new KeyPriorityPair(key, priority, entry.lastAccessed());
            })
            .sorted(this::comparePriority)
            .limit(evictionCount)
            .map(pair -> pair.key)
            .toArray(Key[]::new);
    }
    
    private int getPriority(ICacheEntry entry) {
        if (entry == null || entry.metadata() == null) {
            return DEFAULT_PRIORITY;
        }
        
        Object priorityObj = entry.metadata().get(PRIORITY_KEY);
        if (priorityObj instanceof Number) {
            return ((Number) priorityObj).intValue();
        }
        
        return DEFAULT_PRIORITY;
    }
    
    private int comparePriority(KeyPriorityPair a, KeyPriorityPair b) {
        // Lower priority numbers are evicted first
        int priorityComparison = Integer.compare(a.priority, b.priority);
        if (priorityComparison != 0) {
            return priorityComparison;
        }
        
        // Same priority: evict least recently accessed
        return a.lastAccessed.compareTo(b.lastAccessed);
    }
    
    private static class KeyPriorityPair {
        final Key key;
        final int priority;
        final Instant lastAccessed;
        
        KeyPriorityPair(Key key, int priority, Instant lastAccessed) {
            this.key = key;
            this.priority = priority;
            this.lastAccessed = lastAccessed;
        }
    }
}
```

**Time-Window Eviction Policy**

Evicts objects based on time windows and access patterns:

```java
public class TimeWindowEvictionPolicy implements ICachePolicy {
    
    private Duration recentThreshold = Duration.ofMinutes(15);
    private Duration oldThreshold = Duration.ofHours(2);
    
    @Override
    public void init(IStruct config) {
        if (config.containsKey("recentThresholdMinutes")) {
            this.recentThreshold = Duration.ofMinutes(
                IntegerCaster.cast(config.get("recentThresholdMinutes"))
            );
        }
        
        if (config.containsKey("oldThresholdHours")) {
            this.oldThreshold = Duration.ofHours(
                IntegerCaster.cast(config.get("oldThresholdHours"))
            );
        }
    }
    
    @Override
    public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
        Instant now = Instant.now();
        Instant recentCutoff = now.minus(recentThreshold);
        Instant oldCutoff = now.minus(oldThreshold);
        
        List<Key> candidates = keys.stream()
            .map(key -> {
                ICacheEntry entry = store.getQuiet(key);
                return new KeyTimePair(key, entry);
            })
            .filter(pair -> pair.entry != null)
            .sorted((a, b) -> compareByTimeWindow(a, b, recentCutoff, oldCutoff))
            .limit(evictionCount)
            .map(pair -> pair.key)
            .collect(Collectors.toList());
        
        return candidates.toArray(new Key[0]);
    }
    
    private int compareByTimeWindow(KeyTimePair a, KeyTimePair b, 
                                   Instant recentCutoff, Instant oldCutoff) {
        // Prioritize eviction: very old > old unused > recent unused > recent used
        boolean aVeryOld = a.entry.created().isBefore(oldCutoff);
        boolean bVeryOld = b.entry.created().isBefore(oldCutoff);
        
        if (aVeryOld != bVeryOld) {
            return aVeryOld ? -1 : 1; // Very old items first
        }
        
        boolean aRecentlyAccessed = a.entry.lastAccessed().isAfter(recentCutoff);
        boolean bRecentlyAccessed = b.entry.lastAccessed().isAfter(recentCutoff);
        
        if (aRecentlyAccessed != bRecentlyAccessed) {
            return aRecentlyAccessed ? 1 : -1; // Not recently accessed first
        }
        
        // Same category: sort by last access time (oldest first)
        return a.entry.lastAccessed().compareTo(b.entry.lastAccessed());
    }
    
    private static class KeyTimePair {
        final Key key;
        final ICacheEntry entry;
        
        KeyTimePair(Key key, ICacheEntry entry) {
            this.key = key;
            this.entry = entry;
        }
    }
}
```

#### Step 3: Advanced Pattern - Adaptive Policy

An adaptive policy that changes behavior based on cache performance:

```java
public class AdaptiveEvictionPolicy implements ICachePolicy {
    
    private volatile ICachePolicy currentPolicy;
    private final ICachePolicy lruPolicy = new LRUPolicy();
    private final ICachePolicy lfuPolicy = new LFUPolicy();
    
    private long lastEvaluationTime = 0;
    private double lastHitRate = 0.0;
    private final long evaluationInterval = 300000; // 5 minutes
    
    @Override
    public void init(IStruct config) {
        this.currentPolicy = lruPolicy; // Start with LRU
        this.lruPolicy.init(config);
        this.lfuPolicy.init(config);
    }
    
    @Override
    public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
        adaptPolicyIfNeeded(store);
        return currentPolicy.selectEvictionCandidates(store, keys, evictionCount);
    }
    
    private void adaptPolicyIfNeeded(IObjectStore store) {
        long now = System.currentTimeMillis();
        
        if (now - lastEvaluationTime < evaluationInterval) {
            return; // Not time to evaluate yet
        }
        
        // Get current hit rate from cache provider
        ICacheProvider provider = store.getProvider();
        if (provider != null) {
            ICacheStats stats = provider.getStats();
            double currentHitRate = stats.getHitRate();
            
            // Switch policy if hit rate is declining
            if (currentHitRate < lastHitRate - 0.05) { // 5% threshold
                switchPolicy();
            }
            
            lastHitRate = currentHitRate;
        }
        
        lastEvaluationTime = now;
    }
    
    private void switchPolicy() {
        if (currentPolicy == lruPolicy) {
            currentPolicy = lfuPolicy;
            logger.info("Switched to LFU eviction policy due to declining hit rate");
        } else {
            currentPolicy = lruPolicy;
            logger.info("Switched to LRU eviction policy due to declining hit rate");
        }
    }
    
    @Override
    public String getName() {
        return "Adaptive(" + currentPolicy.getName() + ")";
    }
    
    @Override
    public void reset() {
        currentPolicy.reset();
        lastEvaluationTime = 0;
        lastHitRate = 0.0;
    }
}
```

## Configuration

You can register and use your custom eviction policies via the caches configuration section by putting the full Java class path of the object store as the `evictionPolicy` key

```java
// In your cache configuration
evictionPolicy : "my.class.MyPolicy"
```

Or you can use the `createCache( name, provider, propertes )` method on the `CacheService` and pass in a class or object instance for the `evictionPolicy`

```java
// Create and configure your store instance
customPolicy = new MyPolicy();

// Use it in cache configuration
myCache = cacheService.createCache( "myCache", "BoxCache", {
    "evictionPolicy" : customPolicy
} );
```

## Testing Custom Policies

#### Unit Testing Framework

```java
@Test
public void testCustomEvictionPolicy() {
    // Setup
    CustomEvictionPolicy policy = new CustomEvictionPolicy();
    policy.init(new Struct());
    
    IObjectStore mockStore = createMockStore();
    List<Key> testKeys = createTestKeys();
    
    // Execute
    Key[] candidates = policy.selectEvictionCandidates(mockStore, testKeys, 3);
    
    // Verify
    assertEquals(3, candidates.length);
    // Add specific assertions for your policy logic
}

private IObjectStore createMockStore() {
    IObjectStore store = mock(IObjectStore.class);
    
    // Mock cache entries with different characteristics
    when(store.getQuiet(Key.of("key1"))).thenReturn(
        createMockEntry("key1", Instant.now().minusSeconds(3600), 5)
    );
    when(store.getQuiet(Key.of("key2"))).thenReturn(
        createMockEntry("key2", Instant.now().minusSeconds(1800), 10)
    );
    
    return store;
}

private ICacheEntry createMockEntry(String key, Instant lastAccessed, int hits) {
    ICacheEntry entry = mock(ICacheEntry.class);
    when(entry.key()).thenReturn(Key.of(key));
    when(entry.lastAccessed()).thenReturn(lastAccessed);
    when(entry.hits()).thenReturn(hits);
    return entry;
}
```

#### Performance Testing

```java
@Test
public void testEvictionPerformance() {
    CustomEvictionPolicy policy = new CustomEvictionPolicy();
    IObjectStore store = createLargeTestStore(10000); // 10k entries
    List<Key> keys = Arrays.asList(store.getKeys());
    
    long startTime = System.nanoTime();
    
    Key[] candidates = policy.selectEvictionCandidates(store, keys, 1000);
    
    long duration = System.nanoTime() - startTime;
    
    // Verify performance requirements
    assertTrue("Eviction should complete within 100ms", 
               duration < 100_000_000); // 100ms in nanoseconds
    assertEquals(1000, candidates.length);
}
```

#### Integration Testing

```java
@Test
public void testPolicyIntegrationWithCache() {
    // Create cache with custom policy
    IStruct properties = Struct.of(
        "evictionPolicy", new CustomEvictionPolicy(),
        "maxObjects", 100
    );
    
    ICacheProvider cache = cacheService.createCache("testCache", "BoxLang", properties);
    
    // Fill cache beyond capacity
    for (int i = 0; i < 150; i++) {
        cache.set("key" + i, "value" + i);
    }
    
    // Verify eviction occurred
    assertTrue("Cache should not exceed max size", cache.getSize() <= 100);
    
    // Verify your specific eviction behavior
    // (depends on your custom policy logic)
}
```

## Best Practices

#### Performance Considerations

1. **Efficient Sorting**: Use efficient sorting algorithms for large key sets
2. **Minimize Object Creation**: Reuse objects and avoid unnecessary allocations
3. **Lazy Evaluation**: Only calculate expensive metrics when needed
4. **Batch Operations**: Process multiple eviction candidates efficiently

```java
// Efficient candidate selection
@Override
public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
    // Use streams for efficient processing
    return keys.stream()
        .parallel() // Use parallel processing for large sets
        .map(key -> createEvaluationData(store, key))
        .filter(Objects::nonNull)
        .sorted(getComparator())
        .limit(evictionCount)
        .map(data -> data.key)
        .toArray(Key[]::new);
}
```

#### Memory Management

```java
public class MemoryEfficientPolicy implements ICachePolicy {
    
    private WeakHashMap<Key, CachedMetrics> metricsCache = new WeakHashMap<>();
    
    @Override
    public void reset() {
        metricsCache.clear(); // Help GC
    }
    
    // Use weak references for cached calculations
    private CachedMetrics getOrCalculateMetrics(Key key, ICacheEntry entry) {
        return metricsCache.computeIfAbsent(key, k -> calculateMetrics(entry));
    }
}
```

#### Configuration Validation

```java
@Override
public void init(IStruct config) {
    // Validate configuration parameters
    if (config.containsKey("threshold")) {
        Object threshold = config.get("threshold");
        if (!(threshold instanceof Number)) {
            throw new BoxRuntimeException("Threshold must be a number");
        }
        
        double thresholdValue = ((Number) threshold).doubleValue();
        if (thresholdValue < 0.0 || thresholdValue > 1.0) {
            throw new BoxRuntimeException("Threshold must be between 0.0 and 1.0");
        }
    }
    
    this.config = config;
}
```

#### Error Handling

```java
@Override
public Key[] selectEvictionCandidates(IObjectStore store, List<Key> keys, int evictionCount) {
    try {
        return performEvictionSelection(store, keys, evictionCount);
    } catch (Exception e) {
        logger.warn("Custom eviction policy failed, falling back to random selection", e);
        return fallbackToRandomSelection(keys, evictionCount);
    }
}

private Key[] fallbackToRandomSelection(List<Key> keys, int evictionCount) {
    Collections.shuffle(keys);
    return keys.stream()
        .limit(evictionCount)
        .toArray(Key[]::new);
}
```

## Conclusion

Custom eviction policies provide powerful control over cache behavior, allowing you to optimize for your specific application patterns and requirements. By implementing the `ICachePolicy` interface, you can create sophisticated eviction strategies that consider multiple factors such as object size, access patterns, business priority, and temporal characteristics.

Key benefits of custom eviction policies include:

* **Tailored Performance**: Optimize cache hit rates for your specific data access patterns
* **Business Logic Integration**: Incorporate application-specific priorities and rules
* **Advanced Algorithms**: Implement cutting-edge eviction algorithms from research
* **Adaptive Behavior**: Create policies that adapt to changing conditions
* **Multi-Criteria Optimization**: Balance multiple factors in eviction decisions

Whether you need simple priority-based eviction or complex adaptive algorithms, BoxLang's eviction policy framework provides the flexibility to implement precisely the caching behavior your application requires.
