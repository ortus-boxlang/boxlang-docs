---
description: Extend the BoxCache your way!
icon: gear-code
---

# Custom Cache Providers

## Overview

BoxLang's caching system provides a flexible architecture that allows you to create custom cache providers to integrate with any caching backend. Whether you want to integrate with Caffeine, Hazelcast, database storage, or any other caching solution, BoxLang's provider interface makes it straightforward.

### Architecture Overview

The BoxLang cache system consists of several key components:

* **ICacheProvider** - The main interface that all cache providers must implement
* **AbstractCacheProvider** - An optional base class that provides common functionality
* **ICacheEntry** - Interface representing individual cache entries
* **ICacheStats** - Interface for tracking cache performance statistics
* **@BoxCache** - Annotation for registering cache provider metadata

## Required Interfaces

### ICacheProvider

All cache providers must implement the `ICacheProvider` interface, which defines the contract for cache operations:

```java
public interface ICacheProvider {
    // Configuration and lifecycle
    ICacheProvider configure( CacheService cacheService, CacheConfig config );
    void shutdown();
    
    // Basic operations
    Attempt<Object> get( String key );
    void set( String key, Object value );
    boolean clear( String key );
    void clearAll();
    
    // Bulk operations
    IStruct get( String... keys );
    void set( IStruct entries );
    
    // Cache management
    Array getKeys();
    boolean lookup( String key );
    int getSize();
    void reap();
    
    // Advanced operations
    Object getOrSet( String key, Supplier<Object> provider );
    CompletableFuture<Attempt<Object>> getAsync( String key );
    
    // Statistics and reporting
    ICacheStats getStats();
    IStruct getStoreMetadataReport();
}
```

### ICacheStats

Cache providers must track performance statistics through the `ICacheStats` interface:

```java
public interface ICacheStats {
    // Performance metrics
    int hitRate();
    long hits();
    long misses();
    
    // Cache status
    int objectCount();
    int expiredCount();
    long size();
    
    // Maintenance operations
    long garbageCollections();
    long evictionCount();
    long reapCount();
    Instant lastReapDatetime();
    Instant started();
    
    // Recording methods
    ICacheStats recordHit();
    ICacheStats recordMiss();
    ICacheStats recordEviction();
    ICacheStats recordGCHit();
    ICacheStats recordReap();
    ICacheStats reset();
    
    // Conversion
    IStruct toStruct();
}
```

### ICacheEntry

Cache entries encapsulate the stored data along with metadata:

```java
public interface ICacheEntry extends Serializable {
    Key key();
    Attempt<Object> value();
    Object rawValue();
    
    long timeout();
    long lastAccessTimeout();
    boolean isEternal();
    
    Instant created();
    Instant lastAccessed();
    long hits();
    
    IStruct metadata();
    IStruct toStruct();
    
    // Modification methods
    ICacheEntry setValue( Object value );
    ICacheEntry setMetadata( Struct metadata );
    ICacheEntry touchLastAccessed();
    ICacheEntry incrementHits();
}
```

## Step-by-Step Implementation Guide

#### Step 1: Create the Provider Class

Create a new class that extends `AbstractCacheProvider` (recommended) or implements `ICacheProvider` directly:

```java
package com.mycompany.cache;

import com.github.benmanes.caffeine.cache.Cache;
import com.github.benmanes.caffeine.cache.Caffeine;
import com.github.benmanes.caffeine.cache.RemovalListener;
import ortus.boxlang.runtime.cache.BoxCache;
import ortus.boxlang.runtime.cache.providers.AbstractCacheProvider;

@BoxCache( 
    alias = "Caffeine", 
    description = "Caffeine-based high-performance cache provider",
    distributed = false,
    distributedLocking = false,
    tags = { "caffeine", "memory", "high-performance" }
)
public class CaffeineCacheProvider extends AbstractCacheProvider {
    
    private Cache<String, ICacheEntry> caffeineCache;
    private Duration defaultTimeout;
    private Duration defaultLastAccessTimeout;
    private int maxSize;
    
    @Override
    public synchronized ICacheProvider configure( CacheService cacheService, CacheConfig config ) {
        // Call parent configuration
        super.configure( cacheService, config );
        
        // Get configuration properties
        this.maxSize = IntegerCaster.cast( config.properties.get( Key.maxObjects ) );
        this.defaultTimeout = Duration.ofSeconds( 
            IntegerCaster.cast( config.properties.get( Key.defaultTimeout ) ) 
        );
        this.defaultLastAccessTimeout = Duration.ofSeconds(
            IntegerCaster.cast( config.properties.get( Key.defaultLastAccessTimeout ) )
        );
        
        // Build Caffeine cache
        Caffeine<Object, Object> builder = Caffeine.newBuilder()
            .maximumSize( this.maxSize )
            .removalListener( createRemovalListener() );
            
        // Add expiration if configured
        if ( this.defaultTimeout.toSeconds() > 0 ) {
            builder.expireAfterWrite( this.defaultTimeout );
        }
        
        if ( this.defaultLastAccessTimeout.toSeconds() > 0 ) {
            builder.expireAfterAccess( this.defaultLastAccessTimeout );
        }
        
        this.caffeineCache = builder.build();
        
        // Enable the provider
        this.enabled.set( true );
        
        logger.info( "Caffeine cache provider [{}] initialized with max size [{}]", 
                    getName().getName(), this.maxSize );
        
        return this;
    }
    
    @Override
    public void shutdown() {
        if ( this.caffeineCache != null ) {
            this.caffeineCache.invalidateAll();
        }
        logger.info( "Caffeine cache provider [{}] shutdown", getName().getName() );
    }
    
    /**
     * Create a removal listener for cache events
     */
    private RemovalListener<String, ICacheEntry> createRemovalListener() {
        return ( key, entry, cause ) -> {
            if ( entry != null ) {
                // Announce removal event
                announce(
                    BoxEvent.AFTER_CACHE_ELEMENT_REMOVED,
                    Struct.of( 
                        "cache", this, 
                        "key", key, 
                        "entry", entry,
                        "cause", cause.toString()
                    )
                );
                
                // Record eviction stats
                if ( cause.wasEvicted() ) {
                    getStats().recordEviction();
                }
            }
        };
    }
}
```

#### Step 2: Implement Core Cache Operations

```java
@Override
public Attempt<Object> get( String key ) {
    try {
        ICacheEntry entry = this.caffeineCache.getIfPresent( key );
        
        if ( entry == null ) {
            getStats().recordMiss();
            return Attempt.empty();
        }
        
        // Check if expired (for custom expiration logic)
        if ( isExpired( entry ) ) {
            this.caffeineCache.invalidate( key );
            getStats().recordMiss();
            return Attempt.empty();
        }
        
        // Update access time and hits
        entry.touchLastAccessed();
        entry.incrementHits();
        
        getStats().recordHit();
        return entry.value();
        
    } catch ( Exception e ) {
        logger.error( "Error getting key [{}] from Caffeine cache", key, e );
        getStats().recordMiss();
        return Attempt.empty();
    }
}

@Override
public void set( String key, Object value, Object timeout, Object lastAccessTimeout ) {
    try {
        Duration dTimeout = toDuration( timeout, this.defaultTimeout );
        Duration dLastAccessTimeout = toDuration( lastAccessTimeout, this.defaultLastAccessTimeout );
        
        // Check if updating or not
        ICacheEntry oldEntry = this.caffeineCache.getIfPresent( key );
        
        // Create cache entry
        ICacheEntry entry = new BoxCacheEntry(
            getName(),
            dTimeout.toSeconds(),
            dLastAccessTimeout.toSeconds(),
            Key.of( key ),
            value,
            new Struct()
        );
        
        // Store in Caffeine cache
        this.caffeineCache.put( key, entry );
        
        // Announce the event
        if ( oldEntry != null ) {
            announce(
                BoxEvent.AFTER_CACHE_ELEMENT_UPDATED,
                Struct.of(
                    "cache", this,
                    "key", Key.of( key ),
                    "oldEntry", oldEntry,
                    "newEntry", entry
                )
            );
        } else {
            announce(
                BoxEvent.AFTER_CACHE_ELEMENT_INSERT,
                Struct.of(
                    "cache", this,
                    "key", Key.of( key ),
                    "entry", entry
                )
            );
        }
        
    } catch ( Exception e ) {
        logger.error( "Error setting key [{}] in Caffeine cache", key, e );
    }
}

@Override
public boolean clear( String key ) {
    try {
        // Announce before clearing
        announce(
            BoxEvent.BEFORE_CACHE_ELEMENT_REMOVED,
            Struct.of( "cache", this, "key", key )
        );
        
        ICacheEntry entry = this.caffeineCache.getIfPresent( key );
        boolean existed = entry != null;
        
        if ( existed ) {
            this.caffeineCache.invalidate( key );
        }
        
        // Announce after clearing
        announce(
            BoxEvent.AFTER_CACHE_ELEMENT_REMOVED,
            Struct.of( "cache", this, "key", key, "cleared", existed )
        );
        
        return existed;
        
    } catch ( Exception e ) {
        logger.error( "Error clearing key [{}] from Caffeine cache", key, e );
        return false;
    }
}

@Override
public void clearAll() {
    try {
        this.caffeineCache.invalidateAll();
        
        // Announce it
        announce(
            BoxEvent.AFTER_CACHE_CLEAR_ALL,
            Struct.of( "cache", this )
        );
        
    } catch ( Exception e ) {
        logger.error( "Error clearing all entries from Caffeine cache", e );
    }
}
```

#### Step 3: Implement Bulk Operations

```java
@Override
public IStruct get( String... keys ) {
    IStruct results = new Struct();
    
    try {
        // Use Caffeine's bulk get for efficiency
        Map<String, ICacheEntry> entries = this.caffeineCache.getAllPresent( Arrays.asList( keys ) );
        
        for ( String key : keys ) {
            ICacheEntry entry = entries.get( key );
            
            if ( entry != null && !isExpired( entry ) ) {
                entry.touchLastAccessed();
                entry.incrementHits();
                results.put( key, entry.value() );
                getStats().recordHit();
            } else {
                if ( entry != null ) {
                    // Entry was expired, remove it
                    this.caffeineCache.invalidate( key );
                }
                getStats().recordMiss();
                results.put( key, Attempt.empty() );
            }
        }
        
    } catch ( Exception e ) {
        logger.error( "Error getting multiple keys from Caffeine cache", e );
        // Return empty attempts for all keys
        for ( String key : keys ) {
            results.put( key, Attempt.empty() );
        }
    }
    
    return results;
}

@Override
public Array getKeys() {
    try {
        return this.caffeineCache.asMap().keySet()
            .stream()
            .collect( BLCollector.toArray() );
    } catch ( Exception e ) {
        logger.error( "Error getting keys from Caffeine cache", e );
        return new Array();
    }
}

@Override
public Array getKeys( ICacheKeyFilter filter ) {
    try {
        return this.caffeineCache.asMap().keySet()
            .stream()
            .map( Key::of )
            .filter( filter )
            .map( Key::getName )
            .collect( BLCollector.toArray() );
    } catch ( Exception e ) {
        logger.error( "Error getting filtered keys from Caffeine cache", e );
        return new Array();
    }
}

@Override
public int getSize() {
    return ( int ) this.caffeineCache.estimatedSize();
}

@Override
public boolean lookup( String key ) {
    boolean found = this.caffeineCache.getIfPresent( key ) != null;
    
    // Update stats
    if ( found ) {
        getStats().recordHit();
    } else {
        getStats().recordMiss();
    }
    
    return found;
}

@Override
public boolean lookupQuiet( String key ) {
    return this.caffeineCache.getIfPresent( key ) != null;
}
```

#### Step 4: Implement Advanced Features

```java
@Override
public void reap() {
    try {
        long start = System.currentTimeMillis();
        
        // Caffeine handles most cleanup automatically, but we can clean up
        // entries that have exceeded their lastAccessTimeout manually
        Instant now = Instant.now();
        Map<String, ICacheEntry> allEntries = this.caffeineCache.asMap();
        
        allEntries.entrySet().removeIf( entrySet => {
            ICacheEntry entry = entrySet.getValue();
            
            // Check last access timeout if configured
            if ( BooleanCaster.cast( config.properties.get( Key.useLastAccessTimeouts ) ) &&
                 entry.lastAccessTimeout() > 0 &&
                 entry.lastAccessed().plusSeconds( entry.lastAccessTimeout() ).isBefore( now ) ) {
                return true;
            }
            
            // Check main timeout for non-eternal entries
            if ( !entry.isEternal() &&
                 entry.created().plusSeconds( entry.timeout() ).isBefore( now ) ) {
                return true;
            }
            
            return false;
        } );
        
        // Trigger Caffeine's own cleanup
        this.caffeineCache.cleanUp();
        
        getStats().recordReap();
        
        logger.debug(
            "Finished reaping Caffeine cache [{}] in [{}]ms",
            getName().getName(),
            System.currentTimeMillis() - start
        );
        
    } catch ( Exception e ) {
        logger.error( "Error during Caffeine cache reap", e );
    }
}

@Override
public Object getOrSet( String key, Supplier<Object> provider, Object timeout, Object lastAccessTimeout ) {
    // Try to get the value first
    Attempt<Object> result = get( key );
    if ( result.isPresent() ) {
        return result.get();
    }
    
    // Use synchronized block for thread safety
    String lockKey = this.getName().getNameNoCase() + "-" + key;
    
    synchronized ( lockKey.intern() ) {
        // Double-check pattern
        result = get( key );
        if ( result.isPresent() ) {
            return result.get();
        }
        
        try {
            // Generate the value
            Object value = provider.get();
            
            // Store it
            set( key, value, timeout, lastAccessTimeout );
            
            return value;
            
        } catch ( Exception e ) {
            logger.error( "Error in getOrSet for key [{}]", key, e );
            throw new BoxRuntimeException( "Failed to generate value for key: " + key, e );
        }
    }
}

@Override
public Attempt<Object> getQuiet( String key ) {
    try {
        ICacheEntry entry = this.caffeineCache.getIfPresent( key );
        
        if ( entry == null ) {
            return Attempt.empty();
        }
        
        // Check if expired
        if ( isExpired( entry ) ) {
            this.caffeineCache.invalidate( key );
            return Attempt.empty();
        }
        
        return entry.value();
        
    } catch ( Exception e ) {
        logger.error( "Error getting key [{}] quietly from Caffeine cache", key, e );
        return Attempt.empty();
    }
}

/**
 * Check if an entry is expired based on custom business rules
 */
private boolean isExpired( ICacheEntry entry ) {
    if ( entry.isEternal() ) {
        return false;
    }
    
    Instant now = Instant.now();
    
    // Check main timeout
    if ( entry.timeout() > 0 && 
         entry.created().plusSeconds( entry.timeout() ).isBefore( now ) ) {
        return true;
    }
    
    // Check last access timeout
    if ( BooleanCaster.cast( config.properties.get( Key.useLastAccessTimeouts ) ) &&
         entry.lastAccessTimeout() > 0 &&
         entry.lastAccessed().plusSeconds( entry.lastAccessTimeout() ).isBefore( now ) ) {
        return true;
    }
    
    return false;
}
```

#### Step 5: Implement Statistics and Reporting

```java
@Override
public IStruct getStoreMetadataReport( int limit ) {
    IStruct report = new Struct();
    
    try {
        Stream<Map.Entry<String, ICacheEntry>> entryStream = 
            this.caffeineCache.asMap().entrySet().stream();
        
        if ( limit > 0 ) {
            entryStream = entryStream.limit( limit );
        }
        
        entryStream.forEach( entry => {
            try {
                String key = entry.getKey();
                ICacheEntry cacheEntry = entry.getValue();
                
                if ( cacheEntry != null ) {
                    report.put( key, cacheEntry.toStruct() );
                } else {
                    report.put( key, new Struct() );
                }
            } catch ( Exception e ) {
                logger.debug( "Error getting metadata for key [{}]", entry.getKey(), e );
                report.put( entry.getKey(), new Struct() );
            }
        } );
        
    } catch ( Exception e ) {
        logger.error( "Error generating store metadata report", e );
    }
    
    return report;
}

@Override
public IStruct getStoreMetadataReport() {
    return getStoreMetadataReport( 0 ); // No limit
}

@Override
public IStruct getStoreMetadataKeyMap() {
    return Struct.of(
        "cacheName", "cacheName",
        "hits", "hits",
        "timeout", "timeout",
        "lastAccessTimeout", "lastAccessTimeout",
        "created", "created",
        "lastAccessed", "lastAccessed",
        "metadata", "metadata",
        "key", "key",
        "isEternal", "isEternal"
    );
}

@Override
public IStruct getCachedObjectMetadata( String key ) {
    try {
        ICacheEntry entry = this.caffeineCache.getIfPresent( key );
        if ( entry != null ) {
            return entry.toStruct();
        }
    } catch ( Exception e ) {
        logger.error( "Error getting metadata for key [{}]", key, e );
    }
    
    return new Struct();
}

/**
 * Get Caffeine's native statistics if recording is enabled
 */
public IStruct getCaffeineStats() {
    try {
        com.github.benmanes.caffeine.cache.stats.CacheStats caffeineStats = 
            this.caffeineCache.stats();
            
        return Struct.of(
            "requestCount", caffeineStats.requestCount(),
            "hitCount", caffeineStats.hitCount(),
            "hitRate", caffeineStats.hitRate(),
            "missCount", caffeineStats.missCount(),
            "missRate", caffeineStats.missRate(),
            "loadCount", caffeineStats.loadCount(),
            "loadExceptionCount", caffeineStats.loadExceptionCount(),
            "totalLoadTime", caffeineStats.totalLoadTime(),
            "averageLoadPenalty", caffeineStats.averageLoadPenalty(),
            "evictionCount", caffeineStats.evictionCount()
        );
    } catch ( Exception e ) {
        logger.debug( "Caffeine stats not available (recording may not be enabled)", e );
        return new Struct();
    }
}

// Additional utility methods for the Caffeine provider

@Override
public void set( String key, Object value ) {
    set( key, value, this.defaultTimeout, this.defaultLastAccessTimeout );
}

@Override
public void set( String key, Object value, Object timeout ) {
    set( key, value, timeout, this.defaultLastAccessTimeout );
}

@Override
public void set( String key, Object value, Object timeout, Object lastAccessTimeout ) {
    set( key, value, timeout, lastAccessTimeout, new Struct() );
}

@Override
public void set( IStruct entries ) {
    entries.forEach( ( key, value ) => {
        set( key.getName(), value, this.defaultTimeout, this.defaultLastAccessTimeout );
    } );
}

@Override
public void set( IStruct entries, Object timeout, Object lastAccessTimeout ) {
    entries.forEach( ( key, value ) => {
        set( key.getName(), value, timeout, lastAccessTimeout );
    } );
}

@Override
public void setQuiet( Key key, ICacheEntry value ) {
    this.caffeineCache.put( key.getName(), value );
}

@Override
public Object getOrSet( String key, Supplier<Object> provider ) {
    return getOrSet( key, provider, this.defaultTimeout, this.defaultLastAccessTimeout );
}

@Override
public Object getOrSet( String key, Supplier<Object> provider, Object timeout ) {
    return getOrSet( key, provider, timeout, this.defaultLastAccessTimeout );
}

@Override
public Object getOrSet( String key, Supplier<Object> provider, Object timeout, Object lastAccessTimeout ) {
    return getOrSet( key, provider, timeout, lastAccessTimeout, new Struct() );
}
```

## Configuration

#### Provider Configuration

Define your cache provider configuration in the BoxLang configuration:

```json
{
    "caches": {
        "caffeine-cache": {
            "provider": "Caffeine",
            "properties": {
                "maxObjects": 10000,
                "defaultTimeout": 3600,
                "defaultLastAccessTimeout": 1800,
                "reapFrequency": 300,
                "useLastAccessTimeouts": true,
                "recordStats": true,
                "weakKeys": false,
                "weakValues": false,
                "softValues": false
            }
        }
    }
}
```

#### Configuration Properties

The Caffeine cache provider supports the following configuration properties:

* **maxObjects** - Maximum number of entries in the cache (default: 10000)
* **defaultTimeout** - Default expiration time in seconds (default: 3600)
* **defaultLastAccessTimeout** - Default idle time before expiration in seconds (default: 1800)
* **reapFrequency** - How often to run cleanup tasks in seconds (default: 300)
* **useLastAccessTimeouts** - Whether to enforce idle timeouts (default: true)
* **recordStats** - Enable Caffeine's built-in statistics recording (default: true)
* **weakKeys** - Use weak references for keys (default: false)
* **weakValues** - Use weak references for values (default: false)
* **softValues** - Use soft references for values (default: false)

#### Registration

Register your custom provider with BoxLang:

```java
// In your module or application startup
public class CaffeineModule implements IBoxModule {
    
    @Override
    public void onStartup( BoxRuntime runtime ) {
        // Register the custom cache provider
        CacheService cacheService = runtime.getCacheService();
        cacheService.registerProvider( "Caffeine", CaffeineCacheProvider.class );
        
        logger.info( "Caffeine cache provider registered successfully" );
    }
}
```

## Best Practices

#### 1. Error Handling

Always wrap cache operations in try-catch blocks and provide fallback behavior:

```java
@Override
public Attempt<Object> get( String key ) {
    try {
        // Cache operation
        return getCacheValue( key );
    } catch ( Exception e ) {
        logger.error( "Cache get failed for key [{}]", key, e );
        getStats().recordMiss();
        return Attempt.empty();
    }
}
```

#### 2. Serialization

Implement robust serialization for complex objects when needed:

```java
private String serializeValue( Object value ) throws JsonProcessingException {
    if ( value instanceof String || value instanceof Number || value instanceof Boolean ) {
        return value.toString();
    }
    return objectMapper.writeValueAsString( value );
}

private Object deserializeValue( String serialized, Class<?> expectedType ) throws JsonProcessingException {
    if ( expectedType == String.class ) {
        return serialized;
    }
    return objectMapper.readValue( serialized, expectedType );
}
```

#### 3. Resource Management

Implement proper resource cleanup and lifecycle management:

```java
@Override
public void shutdown() {
    try {
        if ( cache != null ) {
            cache.cleanUp();
            cache.invalidateAll();
        }
        
        if ( scheduledReaper != null ) {
            scheduledReaper.cancel( false );
        }
        
        logger.info( "Cache provider [{}] shutdown completed", getName().getName() );
        
    } catch ( Exception e ) {
        logger.error( "Error during cache provider shutdown", e );
    }
}
```

#### 4. Thread Safety

Ensure your provider is thread-safe:

```java
private final ConcurrentHashMap<String, Object> locks = new ConcurrentHashMap<>();

private Object getLock( String key ) {
    return locks.computeIfAbsent( key, k => new Object() );
}

@Override
public Object getOrSet( String key, Supplier<Object> provider, Object timeout, Object lastAccessTimeout ) {
    synchronized ( getLock( key ) ) {
        // Double-check pattern implementation
        Attempt<Object> result = get( key );
        if ( result.isPresent() ) {
            return result.get();
        }
        
        Object value = provider.get();
        set( key, value, timeout, lastAccessTimeout );
        return value;
    }
}
```

#### 5. Performance Optimization

* Use bulk operations when possible to reduce overhead
* Implement efficient key filtering and streaming
* Consider memory usage and implement appropriate eviction policies
* Use async operations for better throughput when appropriate

```java
@Override
public IStruct get( String... keys ) {
    // Bulk operation implementation
    Map<String, ICacheEntry> bulkResult = cache.getAllPresent( Arrays.asList( keys ) );
    
    IStruct results = new Struct();
    for ( String key : keys ) {
        ICacheEntry entry = bulkResult.get( key );
        if ( entry != null && !isExpired( entry ) ) {
            results.put( key, entry.value() );
            getStats().recordHit();
        } else {
            results.put( key, Attempt.empty() );
            getStats().recordMiss();
        }
    }
    
    return results;
}
```

#### 6. Statistics and Monitoring

Implement comprehensive statistics tracking:

```java
@Override
public ICacheProvider configure( CacheService cacheService, CacheConfig config ) {
    super.configure( cacheService, config );
    
    // Create custom stats implementation or use BoxCacheStats
    this.stats = new BoxCacheStats();
    
    // Enable monitoring if configured
    boolean enableMetrics = BooleanCaster.cast( config.properties.get( Key.of( "enableMetrics" ) ) );
    if ( enableMetrics ) {
        // Register with metrics system
        registerMetrics();
    }
    
    return this;
}

private void registerMetrics() {
    // Register cache metrics with monitoring system
    MetricsRegistry.register( "cache." + getName().getName() + ".hits", () => getStats().hits() );
    MetricsRegistry.register( "cache." + getName().getName() + ".misses", () => getStats().misses() );
    MetricsRegistry.register( "cache." + getName().getName() + ".size", () => getSize() );
}
```

#### 7. Configuration Validation

Validate configuration parameters during setup:

```java
@Override
public ICacheProvider configure( CacheService cacheService, CacheConfig config ) {
    super.configure( cacheService, config );
    
    // Validate required properties
    validateConfiguration( config );
    
    // Extract and validate numeric properties
    this.maxSize = IntegerCaster.cast( config.properties.get( Key.maxObjects ) );
    if ( this.maxSize <= 0 ) {
        throw new BoxRuntimeException( "maxObjects must be greater than 0" );
    }
    
    return this;
}

private void validateConfiguration( CacheConfig config ) {
    // Check for required properties
    String[] requiredProps = { "maxObjects", "defaultTimeout" };
    
    for ( String prop : requiredProps ) {
        if ( !config.properties.containsKey( Key.of( prop ) ) ) {
            throw new BoxRuntimeException( "Required property missing: " + prop );
        }
    }
}
```
