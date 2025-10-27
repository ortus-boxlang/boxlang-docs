---
icon: rectangle-code
description: Learn how to leverage Redis caching in BoxLang applications using built-in functions and components for objects, queries, and content.
---

# Code Usage

## 🎯 Overview

Once you have configured your Redis cache provider in your `Application.bx` or `boxlang.json`, you can leverage BoxLang's built-in caching BIFs and components to interact with Redis. This page demonstrates practical examples of caching various types of data using the standard BoxLang caching API.

{% hint style="info" %}
**Important:** Cache `get()` operations return an [Attempt](../../../../boxlang-language/reference/built-in-functions/decision/Attempt.md) object - a functional wrapper that elegantly handles the presence or absence of cached data without null-related issues. Other operations like `set()`, `clear()`, and `lookup()` return their respective types (void, boolean, etc.).
{% endhint %}

## 📦 Cache BIFs

BoxLang provides several Built-In Functions for cache operations:

| BIF | Purpose | Returns |
|-----|---------|---------|
| `cache()` | Get a cache instance by name | `ICacheProvider` |
| `cacheFilter()` | Create pattern filters for bulk operations | `ICacheKeyFilter` |
| `cacheNames()` | List all registered cache names | `Array` |
| `cacheProviders()` | List all registered cache providers | `Array` |
| `cacheService()` | Access the cache service directly | `CacheService` |

{% hint style="success" %}
The `cache()` BIF returns an instance of [ICacheProvider](https://s3.amazonaws.com/apidocs.ortussolutions.com/boxlang/1.6.0/ortus/boxlang/runtime/cache/providers/ICacheProvider.html) which provides a rich interface for working with caches. See the complete [BoxLang Cache API Documentation](https://s3.amazonaws.com/apidocs.ortussolutions.com/boxlang/1.6.0/ortus/boxlang/runtime/cache/package-summary.html) for all available methods.
{% endhint %}

## 🗄️ Caching Objects

### Basic Object Caching

```js
// Store user data in Redis
userData = {
    "userID": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "preferences": { "theme": "dark", "language": "en" }
};

// Cache for 30 minutes (1800 seconds)
cache( "redis" ).set( "user:123", userData, 1800 );

// Retrieve from cache
userAttempt = cache( "redis" ).get( "user:123" );

// Handle the Attempt safely
if ( userAttempt.isPresent() ) {
    user = userAttempt.get();
    writeOutput( "Welcome back, #user.name#!" );
} else {
    // Load from database if not cached
    user = loadUserFromDatabase( 123 );
    cache( "redis" ).set( "user:123", user, 1800 );
}
```

### Functional Approach with Attempt

```js
// Elegant one-liner with default value
user = cache( "redis" )
    .get( "user:123" )
    .getOrDefault( { "userID": 0, "name": "Guest" } );

// Chain with fallback loading
user = cache( "redis" )
    .get( "user:123" )
    .orElseGet( () => {
        var loadedUser = loadUserFromDatabase( 123 );
        cache( "redis" ).set( "user:123", loadedUser, 1800 );
        return loadedUser;
    } );

// Throw if not found
user = cache( "redis" )
    .get( "user:123" )
    .orThrow( "UserNotFound", "User 123 not found in cache" );
```

### Complex Object Caching

```js
// Cache application configuration
appConfig = {
    "database": {
        "host": "db.example.com",
        "port": 5432
    },
    "features": {
        "enableBeta": true,
        "maxUploadSize": 10485760
    },
    "apiKeys": {
        "stripe": getSystemSetting( "STRIPE_KEY" ),
        "sendgrid": getSystemSetting( "SENDGRID_KEY" )
    }
};

// Cache for 1 hour
cache( "redis" ).set( "app:config", appConfig, 3600 );

// Retrieve and use
config = cache( "redis" ).get( "app:config" ).get();
dbHost = config.database.host;
```

### Bulk Object Operations

```js
// Cache multiple objects at once
users = {
    "user:123": { "name": "John", "email": "john@example.com" },
    "user:456": { "name": "Jane", "email": "jane@example.com" },
    "user:789": { "name": "Bob", "email": "bob@example.com" }
};

// Set all at once (30 minute timeout)
cache( "redis" ).set( users, 1800 );

// Retrieve multiple objects
userIDs = [ "user:123", "user:456", "user:789" ];
cachedUsers = cache( "redis" ).get( userIDs );

// Process results
for ( var key in cachedUsers ) {
    cachedUsers[ key ]
        .ifPresent( ( user ) => {
            writeOutput( "Found: #user.name#<br>" );
        } )
        .ifEmpty( () => {
            writeOutput( "Not cached: #key#<br>" );
        } );
}
```

### Get-or-Set Pattern

The `getOrSet()` method provides an atomic operation that retrieves a cached value or computes and stores it if not found - eliminating race conditions and double-lookup patterns:

```js
// Basic get-or-set with default timeouts
userData = cache( "redis" ).getOrSet( "user:123", () => loadUserFromDatabase( 123 ) );

// With custom timeout (30 minutes)
productData = cache( "redis" ).getOrSet(
    "product:456",
    () => loadProductFromAPI( 456 ),
    1800
);

// With timeout and idle timeout (1 hour total, 30 min idle)
reportData = cache( "redis" ).getOrSet(
    "report:monthly",
    () => generateMonthlyReport(),
    3600,  // timeout
    1800   // idleTimeout
);

// With metadata
apiData = cache( "redis" ).getOrSet(
    "api:response:123",
    () => callExternalAPI( 123 ),
    600,   // 10 minutes
    0,     // no idle timeout
    { "source": "api", "cached": now() }  // metadata
);

// Practical example: Expensive computation
function getComputedData( key ) {
    return cache( "redis" ).getOrSet(
        "computed:#key#",
        () => {
            // This expensive operation only runs on cache miss
            var result = performExpensiveCalculation( key );
            writeLog( "Computed data for key: #key#", "info" );
            return result;
        },
        3600  // Cache for 1 hour
    );
}

// Multiple calls - only first one computes
data1 = getComputedData( "report1" );  // Computes and caches
data2 = getComputedData( "report1" );  // Returns from cache
data3 = getComputedData( "report1" );  // Returns from cache
```

## 📊 Caching Queries

### Basic Query Caching

```js
// Cache query results in Redis
qry = queryExecute(
    "SELECT * FROM users WHERE status = :status",
    { status: "active" },
    {
        cache: true,
        cacheTimeout: createTimespan( 0, 0, 30, 0 ), // 30 minutes
        cacheProvider: "redis"
    }
);

// Subsequent calls use cached results
qry = queryExecute(
    "SELECT * FROM users WHERE status = :status",
    { status: "active" },
    {
        cache: true,
        cacheProvider: "redis"
    }
);
```

### Manual Query Caching

```js
// Build custom cache key
cacheKey = "query:users:active";

// Try to get from cache first
qryAttempt = cache( "redis" ).get( cacheKey );

if ( qryAttempt.isPresent() ) {
    // Use cached query
    qry = qryAttempt.get();
} else {
    // Execute query and cache result
    qry = queryExecute( "SELECT * FROM users WHERE status = 'active'" );

    // Cache for 15 minutes
    cache( "redis" ).set( cacheKey, qry, 900 );
}
```

### Query Caching Function

```js
// Reusable query caching function
function getCachedQuery( sql, params = {}, timeout = 1800 ) {
    var cacheKey = "query:" & hash( sql & serializeJSON( params ) );

    return cache( "redis" )
        .get( cacheKey )
        .orElseGet( () => {
            var result = queryExecute( sql, params );
            cache( "redis" ).set( cacheKey, result, timeout );
            return result;
        } );
}

// Alternative: Using getOrSet() for cleaner code
function getCachedQuerySimple( sql, params = {}, timeout = 1800 ) {
    var cacheKey = "query:" & hash( sql & serializeJSON( params ) );

    return cache( "redis" ).getOrSet(
        cacheKey,
        () => queryExecute( sql, params ),
        timeout
    );
}

// Usage
users = getCachedQuery(
    "SELECT * FROM users WHERE department = :dept",
    { dept: "Engineering" },
    3600 // 1 hour
);
```

### Query Invalidation

```js
// Invalidate specific query
cache( "redis" ).clear( "query:users:active" );

// Invalidate all user queries using pattern
cache( "redis" ).clear( cacheFilter( "query:users:*" ) );

// Invalidate after data changes
function saveUser( userData ) {
    // Save to database
    queryExecute(
        "UPDATE users SET name = :name WHERE userID = :id",
        { name: userData.name, id: userData.userID }
    );

    // Clear related cached queries
    cache( "redis" ).clear( cacheFilter( "query:users:*" ) );
    cache( "redis" ).clear( "user:#userData.userID#" );
}
```

## 📄 Caching Content/HTML

### Using the Cache Component

```xml
<!-- Cache expensive HTML generation -->
<bx:cache
    action="content"
    cacheName="redis"
    key="homepage:hero"
    timespan="#createTimespan( 0, 1, 0, 0 )#"
>
    <div class="hero">
        <h1>Welcome to Our Site</h1>
        <bx:set var="latestProducts" value="#productService.getFeatured()#" />
        <bx:loop array="#latestProducts#" item="product">
            <div class="product">
                <h3>#product.name#</h3>
                <p>#product.description#</p>
            </div>
        </bx:loop>
    </div>
</bx:cache>
```

### Manual Content Caching

```js
// Generate cache key for page content
cacheKey = "page:content:" & cgi.script_name & ":" & cgi.query_string;

// Try to get cached content
contentAttempt = cache( "redis" ).get( cacheKey );

if ( contentAttempt.isPresent() ) {
    // Output cached HTML
    writeOutput( contentAttempt.get() );
} else {
    // Capture output
    savecontent variable="htmlContent" {
        writeOutput( "<div class='dynamic-content'>" );
        // Expensive operations here
        products = productService.getAll();
        for ( product in products ) {
            writeOutput( "<div>#product.name#</div>" );
        }
        writeOutput( "</div>" );
    }

    // Cache for 1 hour
    cache( "redis" ).set( cacheKey, htmlContent, 3600 );
    writeOutput( htmlContent );
}
```

### Component-Based Content Caching

```js
// Cacheable component method
component {

    function getProductHTML( productID ) {
        var cacheKey = "html:product:#productID#";

        return cache( "redis" )
            .get( cacheKey )
            .orElseGet( () => {
                var html = "";
                savecontent variable="html" {
                    var product = productService.get( productID );
                    writeOutput( "
                        <div class='product'>
                            <h2>#product.name#</h2>
                            <p>#product.description#</p>
                            <span class='price'>#dollarFormat( product.price )#</span>
                        </div>
                    " );
                }
                cache( "redis" ).set( cacheKey, html, 1800 );
                return html;
            } );
    }

}
```

## 🎨 Advanced Caching Patterns

### Cache-Aside Pattern

```js
// Standard cache-aside implementation
function getUserData( userID ) {
    var cacheKey = "user:#userID#";

    // 1. Try cache first
    return cache( "redis" )
        .get( cacheKey )
        .orElseGet( () => {
            // 2. Cache miss - load from database
            var user = queryExecute(
                "SELECT * FROM users WHERE userID = :id",
                { id: userID }
            );

            // 3. Store in cache for next time
            if ( user.recordCount ) {
                var userData = queryRowToStruct( user, 1 );
                cache( "redis" ).set( cacheKey, userData, 1800 );
                return userData;
            }

            return {};
        } );
}
```

### Write-Through Caching

```js
// Update cache immediately when writing data
function updateUser( userID, userData ) {
    // 1. Update database
    queryExecute(
        "UPDATE users SET name = :name, email = :email WHERE userID = :id",
        {
            id: userID,
            name: userData.name,
            email: userData.email
        }
    );

    // 2. Update cache immediately
    cache( "redis" ).set( "user:#userID#", userData, 1800 );

    return userData;
}
```

### Lazy Loading with Locking

```js
// Prevent cache stampede with distributed locking
function getExpensiveData( key ) {
    var cacheKey = "expensive:#key#";

    // Try cache first
    var attempt = cache( "redis" ).get( cacheKey );
    if ( attempt.isPresent() ) {
        return attempt.get();
    }

    // Use distributed lock to prevent multiple processes from computing
    redisLock name="compute:#key#" cache="redis" timeout=10 expires=30 throwOnTimeout=false {
        // Check cache again (another process might have computed it)
        attempt = cache( "redis" ).get( cacheKey );
        if ( attempt.isPresent() ) {
            return attempt.get();
        }

        // Compute expensive result
        var result = performExpensiveComputation( key );

        // Cache result
        cache( "redis" ).set( cacheKey, result, 3600 );

        return result;
    }

    // If lock wasn't acquired and cache is still empty, compute anyway
    var result = performExpensiveComputation( key );
    cache( "redis" ).set( cacheKey, result, 3600 );
    return result;
}
```

### Time-Based Invalidation

```js
// Cache with automatic time-based refresh
function getDataWithAutoRefresh( key, computeFunction, timeout = 3600 ) {
    var cacheKey = "data:#key#";
    var timestampKey = "timestamp:#key#";

    var dataAttempt = cache( "redis" ).get( cacheKey );
    var timestampAttempt = cache( "redis" ).get( timestampKey );

    // Check if data exists and is not stale
    if ( dataAttempt.isPresent() && timestampAttempt.isPresent() ) {
        var age = dateDiff( "s", timestampAttempt.get(), now() );
        if ( age < timeout ) {
            return dataAttempt.get();
        }
    }

    // Refresh cache
    var result = computeFunction();
    cache( "redis" ).set( cacheKey, result, timeout );
    cache( "redis" ).set( timestampKey, now(), timeout );

    return result;
}

// Usage
reportData = getDataWithAutoRefresh(
    "monthlyReport",
    () => generateMonthlyReport(),
    86400 // Refresh daily
);
```

### Fragment Caching

```js
// Cache individual page fragments
function renderUserProfile( userID ) {
    var html = "";

    // Header - cached for 1 hour
    html &= cache( "redis" )
        .get( "fragment:header:#userID#" )
        .orElseGet( () => {
            var frag = "";
            savecontent variable="frag" {
                var user = getUserData( userID );
                writeOutput( "<div class='profile-header'>#user.name#</div>" );
            }
            cache( "redis" ).set( "fragment:header:#userID#", frag, 3600 );
            return frag;
        } );

    // Recent activity - cached for 5 minutes
    html &= cache( "redis" )
        .get( "fragment:activity:#userID#" )
        .orElseGet( () => {
            var frag = "";
            savecontent variable="frag" {
                var activities = getRecentActivity( userID );
                writeOutput( "<div class='activities'>" );
                for ( var activity in activities ) {
                    writeOutput( "<p>#activity.description#</p>" );
                }
                writeOutput( "</div>" );
            }
            cache( "redis" ).set( "fragment:activity:#userID#", frag, 300 );
            return frag;
        } );

    return html;
}
```

## 🧹 Cache Management

### Clearing Cache Entries

```js
// Clear single entry
cache( "redis" ).clear( "user:123" );

// Clear multiple entries
cache( "redis" ).clear( [ "user:123", "user:456", "user:789" ] );

// Clear all entries matching pattern
cache( "redis" ).clear( cacheFilter( "user:*" ) );

// Clear all query cache entries
cache( "redis" ).clear( cacheFilter( "query:*" ) );

// Clear entire cache
cache( "redis" ).clearAll();
```

### Cache Statistics

```js
// Get cache statistics
stats = cache( "redis" ).getStats();

writeOutput( "
    <h3>Redis Cache Statistics</h3>
    <ul>
        <li>Total Objects: #cache( 'redis' ).getSize()#</li>
        <li>Hit Rate: #numberFormat( stats.getHitRate() * 100, '0.00' )#%</li>
        <li>Hits: #stats.getHits()#</li>
        <li>Misses: #stats.getMisses()#</li>
    </ul>
" );
```

### Listing Cache Keys

```js
// Get all keys (use cautiously in production)
allKeys = cache( "redis" ).getKeys();

// Get keys matching pattern
userKeys = cache( "redis" ).getKeys( cacheFilter( "user:*" ) );

// Stream processing of keys
cache( "redis" )
    .getKeysStream( cacheFilter( "session:*" ) )
    .forEach( ( key ) => {
        writeOutput( "Session key: #key.getName()#<br>" );
    } );
```

### Cache Metadata

```js
// Store with metadata
metadata = {
    "source": "api",
    "version": "2.0",
    "timestamp": now()
};

cache( "redis" ).set(
    key = "api:data:123",
    value = apiData,
    timeout = 3600,
    idleTimeout = 0,
    metadata = metadata
);

// Retrieve metadata
cacheMetadata = cache( "redis" ).getCachedObjectMetadata( "api:data:123" );
writeOutput( "Data version: #cacheMetadata.version#" );
```
