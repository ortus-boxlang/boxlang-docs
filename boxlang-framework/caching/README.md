---
description: >-
  BoxLang ships with an enterprise Caching Engine and Cache Agnostic API
  Aggregator!
icon: server
---

# Caching

## BoxLang Cache Engine

<figure><img src="../../.gitbook/assets/BxCache Overview (1).png" alt=""><figcaption><p>BoxCache Diagram</p></figcaption></figure>

The BoxLang Cache Engine is a high-performance caching solution designed to optimize data retrieval speeds for applications using the BoxLang programming language. By leveraging advanced caching algorithms and memory management techniques, it minimizes latency, enhances scalability, and improves the overall efficiency of data access. Whether handling frequent read operations or reducing server load, the BoxLang Cache Engine serves as an essential component for deploying robust and responsive applications.

## Cache Aggregation

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

The BoxLang Cache Engine also functions as a powerful cache aggregator. This capability allows it to aggregate various cache providers under a single, unified interface, simplifying the management and operation of caching systems. By providing a centralized API, BoxLang Cache Engine streamlines access to multiple caching solutions, ensuring seamless integration and enhanced flexibility. This feature is particularly beneficial for applications that require a diverse set of caching tactics, as it reduces complexity and boosts overall system coherence.

## Features at a Glance <a href="#features-at-a-glance" id="features-at-a-glance"></a>

* **Cache Aggregator**
  * Ability to aggregate different caching engines via our `ICacheProvider` interface
  * Ability to aggregate different configurations of the same caches
  * Rich aggregation event model
  * Granular logging
* **Fast and Simple to use**
  * Simple API and configuration parameters
  * Small Footprint
* **Solid Core**
  * Multi-Threaded
  * Based on Java Concurrency Classes
  * Multiple [Eviction Policies](http://en.wikipedia.org/wiki/Cache_algorithms): FIFO, LFU, LIFO, LRU, MFU, MRU, Random
  * Memory Management & Memory Sensitive Caching based on [Java Soft References](http://docs.oracle.com/javase/7/docs/api/java/lang/ref/SoftReference.html)
* **Extensible & Flexible**
  * CachelListeners for event broadcasting
  * Create custom eviction policies
  * Create custom cache providers
  * Create custom cache key filters
  * Create custom object storages
* **Highly Configurable**
  * JVM Threshold Checks
  * Object Limits
  * Ability to time-expire objects
  * Eternal (singletons) and time-lived objects
  * Fully configurable at runtime via dynamic configurations and hot updates

## Configuration

The main BoxLang configuration file configures the BoxCache `boxlang.json` which can be found in your `$BOXLANG_HOME/config/boxlang.json`.  You can find all the [documentation about configuration in the caches area](../../getting-started/configuration/caches.md).

## Default Caches <a href="#default-caches" id="default-caches"></a>

Every BoxLang runtime comes pre-configured with the following mandatory caches for operation.  You can configure them as you see fit. Please see the [caches](../../getting-started/configuration/caches.md) configuration area.

<table><thead><tr><th width="130.6201171875">Cache</th><th width="282.30584716796875">Object Store</th><th>Hint</th></tr></thead><tbody><tr><td><code>default</code></td><td><code>ConcurrentStore</code></td><td>The default cache in BoxLang is used for queries, templates, and many more internal usages.</td></tr><tr><td><code>bxSessions</code></td><td><code>ConcurrentStore</code></td><td>If you activate session management in your web or client applications, user session information will be stored here.</td></tr><tr><td><code>bxRegex</code></td><td><code>ConcurrentSoftReferenceStore</code></td><td>This is where all dynamic regular expressions are compiled and kept.</td></tr></tbody></table>

## Providers

{% include "../../.gitbook/includes/boxcache-providers.md" %}

## Object Stores

{% include "../../.gitbook/includes/boxcache-stores.md" %}

## Eviction Policies

The BoxCache also ships with several different eviction policies that are triggered on eviction conditions like:

* Max objects reached
* Memory threshold
* Garbage collections
* Much more.

<table><thead><tr><th width="254.771484375">Policy</th><th>Purpose</th></tr></thead><tbody><tr><td><strong>LRU</strong> <br>(Least Recently Used)</td><td>Evicts the objects that haven't been accessed for the longest time. Best for applications with temporal locality where recently accessed items are more likely to be accessed again. Ideal for general-purpose caching scenarios.</td></tr><tr><td><strong>MRU</strong> <br>(Most Recently Used)</td><td>Evicts the most recently accessed objects first. Useful when you want to keep older, established data and remove newly added items. Good for scenarios where recent additions are less valuable than historical data.</td></tr><tr><td><strong>LFU</strong> <br>(Least Frequently Used)</td><td>Evicts objects with the lowest access frequency count. Maintains items that are accessed often, regardless of when they were last accessed. Perfect for caching frequently requested data like popular products or common API responses.</td></tr><tr><td><strong>MFU</strong> <br>(Most Frequently Used)</td><td>Evicts the most frequently accessed objects first. Counterintuitive but useful in scenarios where you want to cycle out "hot" data to make room for less popular items that might become important. Rare use case but valuable for specialized applications.</td></tr><tr><td><strong>FIFO</strong> <br>(First In, First Out)</td><td>Evicts objects in the order they were added to the cache. Simple queue-based eviction that doesn't consider access patterns. Good for time-sensitive data where older entries naturally become less relevant, like news feeds or log entries.</td></tr><tr><td><strong>LIFO</strong> <br>(Last In, First Out)</td><td>Evicts the most recently added objects first, like a stack. Keeps older established data while removing newer additions. Useful when you want to maintain a stable core dataset and only temporarily cache additional items.</td></tr><tr><td><strong>Random</strong></td><td>Evicts objects randomly without considering access patterns or insertion order. Provides consistent average performance without the overhead of tracking access metadata. Good for scenarios where no clear access pattern exists or when you want to avoid the worst-case behaviors of other policies.</td></tr></tbody></table>



## Cache BIFs (Built-in Functions)

BoxLang provides a comprehensive set of Built-in Functions (BIFs) that offer convenient access to the caching infrastructure. These BIFs provide a developer-friendly interface for working with caches, filters, and the cache service without requiring direct Java interaction.

### Overview

Cache BIFs serve as the primary interface for BoxLang developers to interact with the caching system. They provide:

* **Simple Access**: Easy retrieval of cache instances and services
* **Functional Approach**: Chainable operations for cache manipulation
* **Filter Support**: Powerful pattern matching for bulk operations
* **Service Discovery**: Introspection capabilities for registered caches and providers
* **BoxLang Integration**: Native BoxLang syntax and conventions

### Available Cache BIFs

#### Summary Table

<table><thead><tr><th width="206.51409912109375">BIF</th><th width="357.0279541015625">Purpose</th><th>Returns</th></tr></thead><tbody><tr><td><code>cache()</code></td><td>Get a cache instance by name</td><td><code>ICacheProvider</code></td></tr><tr><td><code>cacheFilter()</code></td><td>Create filters for cache key operations</td><td><code>ICacheKeyFilter</code></td></tr><tr><td><code>cacheNames()</code></td><td>List all registered cache names</td><td><code>Array</code></td></tr><tr><td><code>cacheProviders()</code></td><td>List all registered cache providers</td><td><code>Array</code></td></tr><tr><td><code>cacheService()</code></td><td>Access the cache service directly</td><td><code>CacheService</code></td></tr></tbody></table>



### cache(cacheName)

The primary BIF for accessing cache instances. Returns a cache provider that implements the `ICacheProvider` interface.

**Syntax:**

```javascript
cache([cacheName="default"])
```

**Parameters:**

* `cacheName` (string, optional): The name of the cache to retrieve. Defaults to "default"

**Returns:** `ICacheProvider` - The requested cache instance

**Examples:**

```javascript
// Get the default cache
myCache = cache();

// Get a named cache
userCache = cache("userSessions");
apiCache = cache("apiResponses");

// Basic cache operations
cache().set("user:123", userData);
user = cache().get("user:123");
cache().clear("user:123");

// Chained operations
cache("userSessions")
    .set("session:abc123", sessionData, 1800) // 30 minutes
    .set("session:def456", otherSession, 3600); // 1 hour

// Check if cache exists and use it
if (arrayContains(cacheNames(), "productCache")) {
    product = cache("productCache").get("product:456");
}
```

### cacheFilter( filter, useRegex )

Creates filter objects for performing bulk operations on cache keys using pattern matching.

**Syntax:**

```javascript
cacheFilter(filter, [useRegex=false])
```

**Parameters:**

* `filter` (string, required): The pattern to match against cache keys
* `useRegex` (boolean, optional): Use regex pattern instead of wildcard. Defaults to false

**Returns:** `ICacheKeyFilter` - A filter object for cache operations

**Wildcard Patterns:**

* `*` - Matches any sequence of characters
* `?` - Matches any single character
* `[abc]` - Matches any character in the brackets
* `[a-z]` - Matches any character in the range

**Examples:**

```javascript
// Wildcard filtering (default)
userFilter = cacheFilter("user:*");
sessionFilter = cacheFilter("session:*");
tempFilter = cacheFilter("temp_*");

// Regex filtering
emailFilter = cacheFilter(".*@domain\.com$", true);
idFilter = cacheFilter("^id_\d{4,6}$", true);

// Use filters with cache operations
cache().clear(cacheFilter("temp_*")); // Clear all temp keys
cache().clear(cacheFilter("user:session_.*", true)); // Regex clear

// Get multiple keys with filter
userSessions = cache().get(cacheFilter("user:*"));
// Returns: { "user:123": userData, "user:456": otherUser, ... }

// Bulk operations with filters
cache().clear(cacheFilter("api:response:*")); // Clear API cache
cache().lookup(cacheFilter("product:*")); // Check which products are cached

// Complex patterns
cache().clear(cacheFilter("cache_temp_[0-9]*")); // Clear numbered temp caches
cache().get(cacheFilter("user_session_????")); // Get 4-char session IDs
```

**Custom Filter Functions:**

You can also use closures/lambdas as filters:

```javascript
// Custom filter using closure
customFilter = function(key) {
    return key.getName().startsWith("special_") && 
           key.getName().length() > 10;
};

cache().clear(customFilter);

// One-liner custom filters
cache().clear(key => key.getName().contains("_expired_"));
cache().get(key => key.getName().endsWith("_active"));
```

### cacheNames()

Returns an array of all registered cache names in the system.

**Syntax:**

```javascript
cacheNames()
```

**Returns:** `Array` - Array of cache names as strings

**Examples:**

```javascript
// Get all cache names
allCaches = cacheNames();
writeOutput("Available caches: " & arrayToList(allCaches));

// Check if specific cache exists
if (arrayContains(cacheNames(), "mySpecialCache")) {
    // Use the cache
    cache("mySpecialCache").set("key", "value");
} else {
    // Create the cache or handle missing cache
    writeOutput("Cache 'mySpecialCache' not found!");
}

// Iterate through all caches
for (cacheName in cacheNames()) {
    cacheInstance = cache(cacheName);
    writeOutput("Cache '#cacheName#' has #cacheInstance.getSize()# items");
}

// Filter cache names
userCaches = arrayFilter(cacheNames(), function(name) {
    return name.startsWith("user");
});
```

### cacheProviders()

Returns an array of all registered cache provider names.

**Syntax:**

```javascript
cacheProviders()
```

**Returns:** `Array` - Array of provider names as strings

**Examples:**

```javascript
// Get all available providers
providers = cacheProviders();
writeOutput("Available providers: " & arrayToList(providers));

// Check provider availability
if (arrayContains(cacheProviders(), "Redis")) {
    // Can create Redis caches
    writeOutput("Redis provider is available");
} else {
    writeOutput("Redis provider not registered");
}

// Display provider information
for (provider in cacheProviders()) {
    writeOutput("Provider available: #provider#");
}
```

### cacheService()

Provides direct access to the underlying cache service for advanced operations.

**Syntax:**

```javascript
cacheService()
```

**Returns:** `CacheService` - The cache service instance

**Examples:**

```javascript
// Get the cache service
service = cacheService();

// Create new caches dynamically
service.createCache("newCache", "BoxLang", {
    "maxObjects": 5000,
    "defaultTimeout": 1800,
    "evictionPolicy": "LRU"
});

// Register custom providers
service.registerProvider("MyProvider", createObject("java", "com.mycompany.MyProvider"));

// Bulk operations
service.clearAllCaches(); // Clear all caches
service.reapAllCaches();  // Run maintenance on all caches

// Advanced cache management
service.replaceCache("oldCache", newCacheInstance);
service.shutdownCache("temporaryCache");
```

## Practical Usage Patterns

#### Basic Caching Pattern

```javascript
// Simple get-or-set pattern
function getUser(userID) {
    var cacheKey = "user:#userID#";
    var user = cache().get(cacheKey);
    
    if (user.isPresent()) {
        return user.get();
    }
    
    // Load from database
    user = userService.loadUser(userID);
    
    // Cache for 30 minutes
    cache().set(cacheKey, user, 1800);
    
    return user;
}
```

#### Session Management

```javascript
// Session cache operations
function storeSession(sessionID, sessionData) {
    cache("sessions").set("session:#sessionID#", sessionData, 3600);
}

function getSession(sessionID) {
    return cache("sessions").get("session:#sessionID#");
}

function clearUserSessions(userID) {
    var filter = cacheFilter("session:*user:#userID#*");
    cache("sessions").clear(filter);
}

function cleanupExpiredSessions() {
    // Custom filter for expired sessions
    var expiredFilter = function(key) {
        var session = cache("sessions").getQuiet(key);
        return session.isPresent() && 
               session.get().lastActivity < dateAdd("h", -2, now());
    };
    
    cache("sessions").clear(expiredFilter);
}
```

#### API Response Caching

```javascript
// API response caching with patterns
function cacheAPIResponse(endpoint, params, response) {
    var cacheKey = "api:#endpoint#:#hash(serialize(params))#";
    cache("apiCache").set(cacheKey, response, 600); // 10 minutes
}

function getCachedAPIResponse(endpoint, params) {
    var cacheKey = "api:#endpoint#:#hash(serialize(params))#";
    return cache("apiCache").get(cacheKey);
}

function clearAPICache(endpoint) {
    if (isNull(endpoint)) {
        // Clear all API cache
        cache("apiCache").clear(cacheFilter("api:*"));
    } else {
        // Clear specific endpoint
        cache("apiCache").clear(cacheFilter("api:#endpoint#:*"));
    }
}
```

#### Cache Warming and Preloading

```javascript
// Cache warming function
function warmupCaches() {
    // Warm user cache with active users
    var activeUsers = userService.getActiveUsers();
    
    for (var user in activeUsers) {
        cache("users").set("user:#user.id#", user, 7200); // 2 hours
    }
    
    // Warm product cache
    var popularProducts = productService.getPopularProducts();
    
    for (var product in popularProducts) {
        cache("products").set("product:#product.id#", product, 3600);
    }
    
    writeOutput("Warmed #arrayLen(activeUsers)# users and #arrayLen(popularProducts)# products");
}
```

#### Cache Statistics and Monitoring

```javascript
// Cache monitoring function
function getCacheReport() {
    var report = {};
    
    for (var cacheName in cacheNames()) {
        var cacheInstance = cache(cacheName);
        var stats = cacheInstance.getStats();
        
        report[cacheName] = {
            "size": cacheInstance.getSize(),
            "hits": stats.getHits(),
            "misses": stats.getMisses(),
            "hitRate": stats.getHitRate(),
            "enabled": cacheInstance.isEnabled()
        };
    }
    
    return report;
}

// Display cache status
function displayCacheStatus() {
    var report = getCacheReport();
    
    for (var cacheName in report) {
        var info = report[cacheName];
        writeOutput("Cache: #cacheName#");
        writeOutput("  Size: #info.size# items");
        writeOutput("  Hit Rate: #numberFormat(info.hitRate * 100, '0.00')#%");
        writeOutput("  Hits: #info.hits#, Misses: #info.misses#");
        writeOutput("  Status: #info.enabled ? 'Enabled' : 'Disabled'#");
        writeOutput("---");
    }
}
```

#### Dynamic Cache Creation

```javascript
// Create caches based on application needs
function createUserCache(maxUsers) {
    var service = cacheService();
    
    if (!service.hasCache("userCache")) {
        service.createCache("userCache", "BoxLang", {
            "maxObjects": maxUsers * 2,
            "defaultTimeout": 3600,
            "evictionPolicy": "LRU",
            "objectStore": "ConcurrentHashMap"
        });
        
        writeOutput("Created user cache for #maxUsers# users");
    }
    
    return cache("userCache");
}
```

#### Error Handling and Fallbacks

```javascript
// Safe cache operations with fallbacks
function safeGet(cacheKey, fallbackFunction) {
    try {
        var result = cache().get(cacheKey);
        if (result.isPresent()) {
            return result.get();
        }
    } catch (any e) {
        writeLog("Cache error: #e.message#", "error");
    }
    
    // Fallback to function
    var data = fallbackFunction();
    
    // Try to cache the result
    try {
        cache().set(cacheKey, data, 1800);
    } catch (any e) {
        writeLog("Cache set error: #e.message#", "warning");
    }
    
    return data;
}
```

## Advanced Patterns

#### Cache Hierarchies

```javascript
// Hierarchical cache clearing
function clearUserData(userID) {
    var filters = [
        cacheFilter("user:#userID#*"),           // User data
        cacheFilter("session:*user:#userID#*"),  // User sessions  
        cacheFilter("profile:#userID#*"),        // User profiles
        cacheFilter("pref:#userID#*")            // User preferences
    ];
    
    for (var filter in filters) {
        cache().clear(filter);
    }
}
```

#### Multi-Cache Operations

```javascript
// Operate across multiple caches
function clearAllUserCaches(userID) {
    var userCaches = arrayFilter(cacheNames(), function(name) {
        return name.contains("user") || name.contains("session");
    });
    
    for (var cacheName in userCaches) {
        var userFilter = cacheFilter("*#userID#*");
        cache(cacheName).clear(userFilter);
    }
}
```

#### Cache Synchronization

```javascript
// Synchronize data across multiple caches
function syncUserAcrossCaches(userID, userData) {
    var caches = ["primaryUsers", "secondaryUsers", "userProfiles"];
    
    for (var cacheName in caches) {
        if (arrayContains(cacheNames(), cacheName)) {
            cache(cacheName).set("user:#userID#", userData, 3600);
        }
    }
}
```

## Best Practices

#### 1. Cache Naming Conventions

```javascript
// Use descriptive, hierarchical cache keys
cache().set("user:profile:#userID#", profile);
cache().set("api:response:v1:#endpoint#:#params#", response);
cache().set("session:data:#sessionID#", sessionData);
cache().set("config:app:#version#", configuration);
```

#### 2. Efficient Filter Usage

```javascript
// Prefer specific patterns over broad wildcards
cache().clear(cacheFilter("temp:session:*"));        // Good
cache().clear(cacheFilter("*"));                     // Avoid - too broad

// Use regex for complex patterns
cache().clear(cacheFilter("^user:temp_\d{8}$", true)); // Complex pattern
```

#### 3. Error Handling

```javascript
// Always handle cache failures gracefully
try {
    return cache().get(key).orElse(fallbackValue);
} catch (any e) {
    writeLog("Cache error: #e.message#", "error");
    return fallbackValue;
}
```

#### 4. Performance Monitoring

```javascript
// Regular cache performance checks
function monitorCachePerformance() {
    for (var cacheName in cacheNames()) {
        var cacheInstance = cache(cacheName);
        var hitRate = cacheInstance.getStats().getHitRate();
        
        if (hitRate < 0.7) { // Less than 70% hit rate
            writeLog("Cache '#cacheName#' has low hit rate: #hitRate#", "warning");
        }
    }
}
```

## Keep Exploring

BoxLang's Cache BIFs provide a powerful and intuitive interface for working with the caching infrastructure. They enable developers to:

* **Access Caches Easily**: Simple syntax for retrieving and using cache instances
* **Filter Operations**: Powerful pattern matching for bulk cache operations
* **Service Discovery**: Easy introspection of available caches and providers
* **Advanced Management**: Direct access to cache service capabilities

By leveraging these BIFs, developers can implement sophisticated caching strategies while maintaining clean, readable BoxLang code. The functional approach supports both simple use cases and complex enterprise caching scenarios.  Now that we have the basics, we will explore more in-depth how to use the BoxCache engine.

