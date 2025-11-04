---
description: >-
  The BoxCache Provider is BoxLang's default, high-performance cache
  implementation.
---

# BoxCache Provider

The BoxCache Provider is BoxLang's default, high-performance cache implementation. It provides a comprehensive caching solution with pluggable object stores, configurable eviction policies, automatic maintenance, and extensive monitoring capabilities. The BoxCache Provider serves as the foundation for most caching needs in BoxLang applications.

## Overview

The BoxCache Provider (`BoxCacheProvider`) is designed to be:

* **High Performance**: Uses efficient concurrent data structures and async operations
* **Flexible Storage**: Supports multiple object store backends (memory, disk, custom)
* **Intelligent Eviction**: Configurable eviction policies (LRU, MRU, LFU, etc.)
* **Self-Maintaining**: Automatic expiration, reaping, and memory management
* **Event-Driven**: Comprehensive event broadcasting for cache operations
* **Thread-Safe**: Fully concurrent and thread-safe for multi-threaded applications
* **Observable**: Rich statistics and monitoring capabilities

## Accessing the BoxCache Provider

The primary way to access BoxCache instances in BoxLang is through the `cache()` BIF:

```javascript
// Get the default cache (usually BoxCache provider)
defaultCache = cache();

// Get a named BoxCache instance
userCache = cache("userSessions");
productCache = cache("productCatalog");

// Check cache type
println( "Cache type: " & cache().getType() ); // Outputs: BoxLang
```

## Core Storage Operations

### Setting Data

The BoxCache Provider offers multiple ways to store data with flexible timeout options:

```javascript
myCache = cache("myCache");

// Basic storage (uses default timeouts)
myCache.set("user:123", userData);

// With custom timeout (in seconds)
myCache.set("session:abc", sessionData, 1800); // 30 minutes

// With both timeout and last access timeout
myCache.set("temp:xyz", tempData, 3600, 900); // 1 hour total, 15 min idle

// With metadata
metadata = {"priority": 5, "category": "user"};
myCache.set("user:456", userData, 3600, 1800, metadata);

// Bulk storage with same timeouts
entries = {
    "product:100": product1,
    "product:101": product2,
    "product:102": product3
};
myCache.set(entries); // Uses default timeouts
myCache.set(entries, 7200, 3600); // 2 hours, 1 hour idle
```

### Getting Data

Retrieve data with built-in null safety using the `Attempt` pattern.  Please see the [Attempt](../../boxlang-language/syntax/attempts.md) construct section.

**Basic Retrieval Patterns**

```javascript
// Traditional approach with explicit checking
result = cache().get( "user:123" )
if ( result.isPresent() ) {
    user = result.get()
    processUser( user )
} else {
    // Handle cache miss
    user = loadUserFromDatabase( 123 )
    cache().set( "user:123", user, 1800 )
}

// Functional approach with orElse fallback
user = cache().get( "user:123" )
    .orElse( loadUserFromDatabase( 123 ) )

// Lazy fallback with orElseGet (only executed if cache miss)
user = cache().get( "user:123" )
    .orElseGet( function() {
        var freshUser = loadUserFromDatabase( 123 )
        cache().set( "user:123", freshUser, 1800 )
        return freshUser
    } )

// Get with default value
config = cache().get( "app:config" )
    .orElse( getDefaultConfiguration() )
```

**Functional Transformations**

```javascript
// Transform cached data with map()
userDisplayName = cache().get( "user:123" )
    .map( ( user ) -> user.firstName & " " & user.lastName )
    .orElse( "Unknown User" )

// Chain multiple transformations
userPermissions = cache().get( "user:123" )
    .map( ( user ) -> user.roleID )
    .map( ( roleID ) -> loadRolePermissions( roleID ) )
    .orElse( [ ] )

// Conditional processing with filter()
activeUser = cache().get( "user:123" )
    .filter( ( user ) -> user.status == "active" )
    .orElse( null )

// Complex transformation with flatMap()
userPreferences = cache().get( "user:123" )
    .flatMap( function( user ) {
        return cache().get( "preferences:" & user.userID )
    } )
    .orElse( getDefaultPreferences() )
```

**Validation and Type Safety**

```javascript
// Validate cached data before use
validatedUser = cache().get( "user:123" )
    .toBeType( "struct" )
    .toSatisfy( ( user ) -> structKeyExists( user, "userID" ) && structKeyExists( user, "email" ) )

if ( validatedUser.isValid() ) {
    user = validatedUser.get()
    // Safe to use user data
} else {
    // Invalid or corrupted cache data
    cache().clear( "user:123" )
    user = loadUserFromDatabase( 123 )
}

// Validate numeric ranges
score = cache().get( "game:score:123" )
    .toBeBetween( 0, 1000 )
    .orElse( 0 )

// Validate with regex patterns
email = cache().get( "user:email:123" )
    .toMatchRegex( "^[A-Za-z0-9+_.-]+@(.+)$" )
    .orElse( "no-email@example.com" )
```

**Side Effects and Actions**

```javascript
// Execute side effects with ifPresent()
cache().get( "user:123" )
    .ifPresent( function( user ) {
        updateLastAccessed( user.userID )
        logUserActivity( user.userID, "cache_hit" )
    } )
    .ifEmpty( function() {
        logCacheMiss( "user:123" )
    } )

// Conditional actions based on validation
cache().get( "session:abc123" )
    .toSatisfy( ( session ) -> session.expiresAt > now() )
    .ifValid( function( session ) {
        extendSessionTimeout( session.sessionID )
    } )
    .ifInvalid( function( session ) {
        cache().clear( "session:abc123" )
        invalidateSession( session.sessionID )
    } )

// Chain multiple conditional actions
cache().get( "user:123" )
    .ifPresent( function( user ) {
        writeLog( "User " & user.userID & " loaded from cache", "info" )
    } )
    .filter( ( user ) -> user.lastLogin > dateAdd( "d", -30, now() ) )
    .ifPresent( function( user ) {
        writeLog( "Recent user activity detected", "info" )
    } )
    .ifEmpty( function() {
        writeLog( "User not recently active or not cached", "warn" )
    } )
```

**Error Handling and Recovery**

```javascript
// Graceful error handling with orThrow()
function getRequiredUser( userID ) {
    return cache().get( "user:" & userID )
        .orThrow( "UserNotFound", "User " & userID & " not found in cache" )
}

// Try cache with multiple fallbacks
userData = cache().get( "user:primary:123" )
    .or( function() {
        return cache().get( "user:backup:123" )
    } )
    .orElseGet( function() {
        return loadUserFromDatabase( 123 )
    } )

// Attempt with validation and recovery
safeUserData = cache().get( "user:123" )
    .toBeType( "struct" )
    .filter( ( user ) -> !structIsEmpty( user ) )
    .or( function() {
        // Try backup cache
        return cache( "backup" ).get( "user:123" )
    } )
    .orElseGet( function() {
        // Last resort - load from database
        var user = loadUserFromDatabase( 123 )
        // Cache for next time
        cache().set( "user:123", user, 3600 )
        return user
    } )
```

**Stream Operations**

```javascript
// Process cached data as streams
cache().get( "user:123" )
    .stream()
    .map( ( user ) -> user.departmentID )
    .forEach( function( deptID ) {
        processDepartment( deptID )
    } )

// Combine multiple cache results
userIDs = [ "123", "456", "789" ]
activeUsers = userIDs
    .map( function( id ) {
        return cache().get( "user:" & id )
    } )
    .filter( ( attempt ) -> attempt.isPresent() )
    .map( ( attempt ) -> attempt.get() )
    .filter( ( user ) -> user.status == "active" )
```

**Advanced Functional Patterns**

```javascript
// Memoization pattern with cache
function getMemoizedData( key, expensiveFunction, timeout = 3600 ) {
    return cache().get( key )
        .orElseGet( function() {
            var result = expensiveFunction()
            cache().set( key, result, timeout )
            return result
        } )
}

// Usage
reportData = getMemoizedData( "report:monthly:2024", function() {
    return generateComplexReport( "2024" )
}, 86400 )

// Circuit breaker pattern
function getWithCircuitBreaker( key, fallbackFunction ) {
    var circuitKey = "circuit:" & key
    var circuitState = cache().get( circuitKey ).orElse( "closed" )

    if ( circuitState == "open" ) {
        // Circuit is open, use fallback
        return fallbackFunction()
    }

    return cache().get( key )
        .ifEmpty( function() {
            // Track failures
            var failures = cache().get( "failures:" & key ).orElse( 0 ) + 1
            cache().set( "failures:" & key, failures, 300 )

            if ( failures >= 5 ) {
                // Open circuit
                cache().set( circuitKey, "open", 60 )
            }
        } )
        .orElseGet( fallbackFunction )
}

// Cached computation with dependency invalidation
function getCachedWithDependencies( key, dependencies, computeFunction ) {
    var cacheKey = key & ":" & hash( serialize( dependencies ) )

    return cache().get( cacheKey )
        .filter( function( cached ) {
            // Validate dependencies haven't changed
            return dependencies.every( function( dep ) {
                var depValue = cache().get( "dep:" & dep )
                return depValue.isPresent() &&
                       depValue.get().timestamp == cached.depTimestamp
            } )
        } )
        .orElseGet( function() {
            var result = computeFunction()
            result.depTimestamp = now()
            cache().set( cacheKey, result, 3600 )
            return result
        } )
}
```

**Bulk Retrieval with Functional Processing**

```javascript
// Process bulk results functionally
keys = [ "user:123", "user:456", "user:789" ]
results = cache().get( keys )

// Extract successful results and handle misses
users = [ ]
missingKeys = [ ]

for ( var key in results ) {
    var attempt = results[ key ]
    attempt
        .ifPresent( function( user ) {
            arrayAppend( users, user )
        } )
        .ifEmpty( function() {
            arrayAppend( missingKeys, key )
        } )
}

// Load missing users and cache them
if ( !arrayIsEmpty( missingKeys ) ) {
    var missingUserIDs = missingKeys.map( ( key ) -> listLast( key, ":" ) )

    var loadedUsers = loadUsersFromDatabase( missingUserIDs )
    var cacheEntries = { }

    for ( var user in loadedUsers ) {
        arrayAppend( users, user )
        cacheEntries[ "user:" & user.userID ] = user
    }

    cache().set( cacheEntries, 3600 )
}
```

**Silent Retrieval and Internal Operations**

```javascript
// Silent retrieval (no stats tracking)
internalConfig = cache().getQuiet( "internal:config" )
    .orElseGet( function() {
        return loadInternalConfiguration()
    } )

// System operations without affecting cache statistics
systemHealth = cache().getQuiet( "system:health" )
    .filter( ( health ) -> health.timestamp > dateAdd( "m", -5, now() ) )
    .orElseGet( function() {
        return performHealthCheck()
    } )
```

**Filtered Retrieval with Complex Processing**

```javascript
// Get all user sessions and process them
userFilter = cacheFilter( "user:session:*" )
userSessions = cache().get( userFilter )

// Process each session attempt
activeSessions = [ ]
expiredSessions = [ ]

for ( var key in userSessions ) {
    userSessions[ key ]
        .filter( ( session ) -> session.expiresAt > now() )
        .ifPresent( function( session ) {
            arrayAppend( activeSessions, session )
        } )
        .ifEmpty( function() {
            arrayAppend( expiredSessions, key )
        } )
}

// Clean up expired sessions
if ( !arrayIsEmpty( expiredSessions ) ) {
    cache().clear( expiredSessions )
}
```

### Get-or-Set Pattern

The BoxCache Provider includes the powerful `getOrSet()` method to eliminate double-lookup patterns:

```javascript
// Basic get-or-set with default timeouts
userData = cache().getOrSet("user:123", () => {
    return loadUserFromDatabase(123)
})

// With custom timeouts
productData = cache().getOrSet("product:456", () => {
    return loadProductFromAPI(456)
}, 3600, 1800) // 1 hour, 30 min idle

// With metadata
reportData = cache().getOrSet("report:monthly", () => {
    return generateMonthlyReport()
}, 86400, 43200, {"priority": 10}) // 24 hours, 12 hour idle
```

### Clearing Data

Remove data from the cache with various options:

```javascript
// Clear single key
cleared = cache().clear("user:123") // Returns true/false

// Clear multiple keys
results = cache().clear(["user:123", "user:456", "user:789"])
// Returns: {"user:123": true, "user:456": false, ...}

// Clear with pattern filter
userFilter = cacheFilter("user:session:*"
cache().clear(userFilter);

// Clear all data
cache().clearAll()

// Silent clear (no events or stats)
cache().clearQuiet("internal:temp")
```

### Key Management and Filtering

#### Getting Cache Keys

```javascript
// Get all keys
allKeys = cache().getKeys()

// Get keys with filter
sessionKeys = cache().getKeys(cacheFilter("session:*"))
userKeys = cache().getKeys(cacheFilter("user:*"))

// Stream processing for large caches
cache().getKeysStream()
    .filter( (key) => {
        return key.startsWith("temp:") &&
               cache().getQuiet(key).isPresent()
    })
    .forEach( (key) => {
        cache().clear(key)
    })
```

#### Using Cache Filters

Cache filters provide powerful pattern matching for bulk operations:

```javascript
// Wildcard filters
tempFilter = cacheFilter("temp:*")           // All temp keys
userFilter = cacheFilter("user:session:*")   // User sessions
apiFilter = cacheFilter("api:v?:*")          // API versions (v1, v2, etc.)

// Regex filters
emailFilter = cacheFilter(".*@domain\.com$", true )
idFilter = cacheFilter("^id_\d{4,6}$", true)

// Custom filter functions
expiredFilter = (key) => {
    var entry = cache().getQuiet(key)
    if (!entry.isPresent()) return false;

    var data = entry.get();
    return structKeyExists(data, "expiry") &&
           data.expiry < now();
};

// Use filters in operations
cache().clear(tempFilter)
cache().get(userFilter)
cache().lookup(expiredFilter)
```

### Lookup Operations

Check for key existence without retrieving data:

```javascript
// Basic lookup (with stats tracking)
exists = cache().lookup("user:123")

// Silent lookup (no stats)
exists = cache().lookupQuiet("internal:config")

// Bulk lookup
results = cache().lookup(["user:123", "user:456"])
// Returns: {"user:123": true, "user:456": false}

// Filtered lookup
userFilter = cacheFilter("user:*")
userExistence = cache().lookup(userFilter)
```

### Statistics and Monitoring

The BoxCache Provider includes comprehensive statistics tracking:

```javascript
// Get cache statistics
stats = cache().getStats()
writeOutput("Hit Rate: " & numberFormat(stats.getHitRate() * 100, "0.00") & "%")
writeOutput("Hits: " & stats.getHits())
writeOutput("Misses: " & stats.getMisses())
writeOutput("Cache Size: " & cache().getSize())

// Cache metadata
writeOutput("Cache Name: " & cache().getName())
writeOutput("Provider Type: " & cache().getType())
writeOutput("Is Enabled: " & cache().isEnabled())
writeOutput("Reporting Enabled: " & cache().isReportingEnabled()

// Clear statistics
cache().clearStats()

// Object-specific metadata
metadata = cache().getCachedObjectMetadata("user:123")
if (!structIsEmpty(metadata)) {
    writeOutput("Last Accessed: " & metadata.lastAccessed)
    writeOutput("Hit Count: " & metadata.hits)
    writeOutput("Created: " & metadata.created)
}

// Bulk metadata for reporting
metadataReport = cache().getStoreMetadataReport(100) // Limit to 100 entries
```

### Configuration and Properties

Access and understand cache configuration:

```javascript
// Get cache configuration
config = cache().getConfig(
properties = config.properties;

writeOutput("Max Objects: " & properties.maxObjects)
writeOutput("Default Timeout: " & properties.defaultTimeout)
writeOutput("Eviction Policy: " & properties.evictionPolicy)
writeOutput("Object Store: " & properties.objectStore)

// Key configuration properties:
// - maxObjects: Maximum number of cached objects
// - defaultTimeout: Default expiration time in seconds
// - defaultLastAccessTimeout: Default idle timeout
// - evictionPolicy: LRU, MRU, LFU, MFU, FIFO, LIFO, Random
// - objectStore: ConcurrentHashMap, ConcurrentSoftReference, Disk, Custom
// - reapFrequency: How often to run maintenance (seconds)
// - freeMemoryPercentageThreshold: Memory threshold for eviction
// - useLastAccessTimeouts: Enable/disable idle timeouts
```

### Async Operations

BoxCache supports asynchronous operations for high-performance scenarios:

```javascript
// Async get operation
future = cache().getAsync("user:123")

// Process the result when ready
future.thenAccept( (result) => {
    if (result.isPresent()) {
        user = result.get()
        processUser(user)
    }
});

// Or wait for completion
result = future.get() // Blocks until complete
```

### Cache Maintenance

#### Manual Maintenance Operations

```javascript
// Trigger reaping (cleanup expired entries)
cache().reap()

// Get cache size
size = cache().getSize()

// Check if cache is operational
if ( cache().isEnabled() ) {
    // Cache is ready for operations
}
```

#### Automatic Maintenance

BoxCache automatically handles:

* **Expiration Checking**: Removes expired entries based on timeouts
* **Idle Timeout Management**: Removes entries that haven't been accessed
* **Memory Threshold Eviction**: Triggers eviction when memory usage is high
* **Scheduled Reaping**: Periodic cleanup based on `reapFrequency` setting

## Event Integration

BoxCache broadcasts events for all major operations:

```javascript
// Cache events are automatically announced:
// - BEFORE_CACHE_ELEMENT_REMOVED / AFTER_CACHE_ELEMENT_REMOVED
// - AFTER_CACHE_ELEMENT_INSERT
// - AFTER_CACHE_ELEMENT_UPDATED
// - AFTER_CACHE_CLEAR_ALL

// Listen to events (if you have interceptor components)
class {

    function afterCacheElementInsert(event, data) {
        writeLog("Cache item added: " & data.key, "info")
    }

    function afterCacheElementRemoved(event, data) {
        writeLog("Cache item removed: " & data.key & ", cleared: " & data.cleared, "info")
    }
}
```

## Practical Usage Patterns

#### User Session Management

```javascript
class {

    function storeUserSession(sessionID, userData) {
        var sessionKey = "session:" & sessionI
        cache("sessions").set(sessionKey, userData, 3600, 180 ) // 1 hour, 30 min idle
    }

    function getUserSession(sessionID) {
        var sessionKey = "session:" & sessionID
        return cache("sessions").get(sessionKey)
    }

    function updateSessionActivity(sessionID) {
        var sessionKey = "session:" & sessionID
        var session = cache("sessions").get(sessionKey)

        if (session.isPresent()) {
            var sessionData = session.get()
            sessionData.lastActivity = now()
            cache("sessions").set(sessionKey, sessionData, 3600, 1800)
        }
    }

    function clearUserSessions(userID) {
        var filter = cacheFilter("session:*:user:" & userID)
        cache("sessions").clear(filter)
    }
}
```

#### API Response Caching

```javascript
class {

    function getCachedAPIResponse(endpoint, params) {
        var cacheKey = "api:" & endpoint & ":" & hash(serialize(params));

        return cache("api").getOrSet(cacheKey, function() {
            return makeAPICall(endpoint, params);
        }, 600); // 10 minutes
    }

    function invalidateAPICache(endpoint) {
        if (isNull(endpoint)) {
            // Clear all API cache
            cache("api").clear(cacheFilter("api:*"));
        } else {
            // Clear specific endpoint
            cache("api").clear(cacheFilter("api:" & endpoint & ":*"));
        }
    }

    function warmAPICache() {
        var popularEndpoints = getPopularEndpoints();

        for (var endpoint in popularEndpoints) {
            getCachedAPIResponse(endpoint.name, endpoint.defaultParams);
        }
    }
}
```

#### Database Query Caching

```javascript
class {

    function getCachedQuery(sql, params, timeout = 1800) {
        var cacheKey = "query:" & hash(sql & params.tostring() );

        return cache("queries").getOrSet(cacheKey, function() {
            return queryExecute(sql, params);
        }, timeout);
    }

    function invalidateQueryCache(tables) {
        for (var table in tables) {
            var filter = cacheFilter("query:*" & table & "*");
            cache("queries").clear(filter);
        }
    }

    function getQueryCacheStats() {
        var stats = cache("queries").getStats();
        return {
            "hitRate": stats.getHitRate(),
            "size": cache("queries").getSize(),
            "hits": stats.getHits(),
            "misses": stats.getMisses()
        };
    }
}
```

#### Multi-Level Caching

```javascript
class {

    function getData(key) {
        // Try L1 cache (fast, small)
        var l1Result = cache("l1").get(key);
        if (l1Result.isPresent()) {
            return l1Result.get();
        }

        // Try L2 cache (slower, larger)
        var l2Result = cache("l2").get(key);
        if (l2Result.isPresent()) {
            var data = l2Result.get();
            // Promote to L1
            cache("l1").set(key, data, 300); // 5 minutes in L1
            return data;
        }

        // Load from source
        var data = loadFromDatabase(key);

        // Store in both levels
        cache("l1").set(key, data, 300);     // 5 minutes
        cache("l2").set(key, data, 3600);    // 1 hour

        return data;
    }

    function invalidateData(key) {
        cache("l1").clear(key);
        cache("l2").clear(key);
    }
}
```

## Performance Optimization

#### Efficient Key Design

```javascript
// Good key patterns - hierarchical and descriptive
"user:profile:" & userID
"product:inventory:" & productID & ":" & warehouseID
"api:response:v1:" & endpoint & ":" & hash(params)

// Avoid overly complex keys
"user:" & userID & ":profile:settings:theme:color" // Too deep

// Use consistent naming conventions
"session:user:" & userID & ":" & sessionID
"session:admin:" & adminID & ":" & sessionID
```

#### Batch Operations

```javascript
// Efficient bulk operations
function loadMultipleUsers(userIDs) {
    var cacheKeys = {};
    var missingIDs = [];

    // Build cache keys
    for (var userID in userIDs) {
        cacheKeys["user:" & userID] = userID;
    }

    // Bulk lookup
    var results = cache("users").get(arrayToList(structKeyArray(cacheKeys)));
    var users = {};

    // Process results and identify misses
    for (var key in results) {
        var result = results[key];
        var userID = cacheKeys[key];

        if (result.isPresent()) {
            users[userID] = result.get();
        } else {
            arrayAppend(missingIDs, userID);
        }
    }

    // Load missing users
    if (!arrayIsEmpty(missingIDs)) {
        var missingUsers = loadUsersFromDatabase(missingIDs);
        var entriesToCache = {};

        for (var userID in missingUsers) {
            users[userID] = missingUsers[userID];
            entriesToCache["user:" & userID] = missingUsers[userID];
        }

        // Bulk cache the missing users
        cache("users").set(entriesToCache, 3600);
    }

    return users;
}
```

#### Memory Management

```javascript
// Monitor cache memory usage
function monitorCacheMemory() {
    var caches = cacheNames();
    var report = {};

    for (var cacheName in caches) {
        var cacheInstance = cache(cacheName);
        var config = cacheInstance.getConfig();
        var size = cacheInstance.getSize();
        var maxSize = config.properties.maxObjects;

        report[cacheName] = {
            "size": size,
            "maxSize": maxSize,
            "utilizationPercent": (size / maxSize) * 100,
            "stats": cacheInstance.getStats()
        };

        // Alert if approaching capacity
        if ((size / maxSize) > 0.8) {
            writeLog("Cache " & cacheName & " is " &
                    numberFormat((size/maxSize)*100, "0.0") & "% full", "warn");
        }
    }

    return report;
}
```

## Error Handling and Resilience

#### Graceful Degradation

```javascript
function resilientCacheOperation(key, fallbackFunction) {
    try {
        var result = cache().get(key);
        if (result.isPresent()) {
            return result.get();
        }
    } catch (any e) {
        writeLog("Cache get error for key " & key & ": " & e.message, "error");
    }

    // Fallback to direct operation
    var data = fallbackFunction();

    // Try to cache the result
    try {
        cache().set(key, data, 1800);
    } catch (any e) {
        writeLog("Cache set error for key " & key & ": " & e.message, "warn");
    }

    return data;
}
```

#### Health Checks

```javascript
function checkCacheHealth() {
    var health = {
        "status": "healthy",
        "issues": []
    };

    try {
        var testKey = "healthcheck:" & createUUID();
        var testValue = "test";

        // Test write
        cache().set(testKey, testValue, 60);

        // Test read
        var result = cache().get(testKey);
        if (!result.isPresent() || result.get() != testValue) {
            arrayAppend(health.issues, "Cache read/write test failed");
            health.status = "unhealthy";
        }

        // Test delete
        cache().clear(testKey);

        // Check stats
        var stats = cache().getStats();
        if (stats.getHitRate() < 0.5 && stats.getHits() > 100) {
            arrayAppend(health.issues, "Low hit rate: " & numberFormat(stats.getHitRate() * 100, "0.00") & "%");
            health.status = "degraded";
        }

        // Check size
        var size = cache().getSize();
        var config = cache().getConfig();
        var maxSize = config.properties.maxObjects;

        if (size > (maxSize * 0.9)) {
            arrayAppend(health.issues, "Cache nearly full: " & size & "/" & maxSize);
            health.status = "degraded";
        }

    } catch (any e) {
        arrayAppend(health.issues, "Cache operation failed: " & e.message);
        health.status = "unhealthy";
    }

    return health;
}
```

## Best Practices

#### 1. Key Naming Conventions

```javascript
// Use consistent, hierarchical naming
"user:profile:" & userID
"session:data:" & sessionID
"product:details:" & productID
"api:response:" & version & ":" & endpoint

// Include versioning for data structures
"user:profile:v2:" & userID
"config:app:v1:" & environment
```

#### 2. Appropriate Timeouts

```javascript
// Short-lived dynamic data
cache().set("stock:price:" & symbol, price, 30); // 30 seconds

// User sessions
cache().set("session:" & sessionID, sessionData, 3600, 1800 // 1 hour, 30 min idle

// Reference data
cache().set("config:app", appConfig, 86400) // 24 hours

// Computed reports
cache().set("report:daily", reportData, 43200) // 12 hours
```

#### 3. Memory Efficiency

```javascript
// Store minimal necessary data
cache().set("user:summary:" & userID, {
    "name": user.name,
    "email": user.email,
    "role": user.role
}, 3600)

// Instead of storing the entire user object
// cache().set("user:full:" & userID, entireUserObject, 3600);
```

#### 4. Strategic Cache Warming

```javascript
function warmCriticalCaches() {
    // Warm high-traffic reference data
    var appConfig = loadApplicationConfig()
    cache().set("config:app", appConfig, 86400)

    // Warm popular user sessions
    var activeUsers = getActiveUserIDs()
    for (var userID in activeUsers) {
        var userData = loadUserProfile(userID)
        cache().set("user:profile:" & userID, userData, 3600)
    }

    // Warm frequently accessed products
    var popularProducts = getPopularProductIDs()
    for (var productID in popularProducts) {
        var productData = loadProductDetails(productID)
        cache().set("product:details:" & productID, productData, 7200)
    }
}
```

## Conclusion

The BoxCache Provider offers a comprehensive, high-performance caching solution for BoxLang applications. By leveraging its rich feature set including flexible storage options, intelligent eviction policies, comprehensive monitoring, and powerful filtering capabilities, developers can build scalable, efficient applications.

Key advantages of BoxCache Provider:

* **Developer Friendly**: Simple BIF-based access with powerful functionality
* **High Performance**: Concurrent operations, async support, and efficient data structures
* **Flexible Configuration**: Pluggable object stores and eviction policies
* **Production Ready**: Comprehensive monitoring, event integration, and automatic maintenance
* **Scalable**: Supports everything from simple key-value caching to complex multi-level architectures

Whether you're caching user sessions, API responses, database queries, or computed data, the BoxCache Provider provides the tools and flexibility needed to optimize your application's performance and scalability.
