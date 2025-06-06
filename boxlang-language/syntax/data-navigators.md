---
description: >-
  Data Navigators provide a fluent, safe way to navigate and extract data from
  complex data structures in BoxLang
---

# Data Navigators

Data Navigators are a powerful BoxLang feature that provides a fluent, chainable interface for safely navigating and extracting data from complex data structures. Whether you're working with JSON files, API responses, configuration data, or nested structures, Data Navigators eliminate the need for verbose null checking and provide elegant error handling.

## Overview

Data Navigators solve common problems when working with complex data:

* **Safe Navigation**: No more "key doesn't exist" errors when traversing nested structures
* **Fluent Interface**: Chainable methods that read like natural language
* **Type Safety**: Built-in type casting with sensible defaults
* **Multiple Data Sources**: Works with JSON strings, files, structures, maps, and more
* **Flexible Extraction**: Get values with defaults, throw on missing data, or check existence

## Getting Started

### Creating a Data Navigator

Use the `dataNavigate()` BIF to create a navigator from various data sources:

```javascript
// From a structure
config = {
    "app": {
        "name": "MyApp",
        "version": "1.0.0",
        "database": {
            "host": "localhost",
            "port": 5432,
            "ssl": true
        }
    }
}
nav = dataNavigate( config )

// From a JSON string
jsonData = '{"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}'
nav = dataNavigate( jsonData )

// From a JSON file
nav = dataNavigate( "/path/to/config.json" )

// From a Java Map
javaMap = new java.util.HashMap()
nav = dataNavigate( javaMap )
```

### Basic Navigation

Navigate through nested structures using the fluent interface:

```javascript
// Setup test data
appConfig = {
    "application": {
        "name": "BoxLang App",
        "version": "2.0.0",
        "features": {
            "caching": true,
            "logging": {
                "level": "INFO",
                "appenders": [ "console", "file" ]
            }
        }
    }
}

nav = dataNavigate( appConfig )

// Navigate to a specific section
loggingNav = nav.from( "application", "features", "logging" )

// Get values with defaults
logLevel = loggingNav.getAsString( "level", "DEBUG" )
println( "Log Level: " & logLevel ) // "INFO"

// Check if values exist
if ( loggingNav.has( "appenders" ) ) {
    appenders = loggingNav.getAsArray( "appenders" )
    println( "Appenders: " & appenders.toList() )
}
```

### Navigation Methods

**Navigate to Segments**

```javascript
// Navigate to nested sections
userNav = dataNavigate( userData ).from( "profile", "settings" )
dbNav = dataNavigate( config ).from( "database" )

// Multiple level navigation
deepNav = dataNavigate( complexData )
    .from( "api", "v1" )
    .from( "endpoints", "users" )
```

**Check Existence**

```javascript
nav = dataNavigate( config )

// Check if keys exist
hasDatabase = nav.has( "database" )
hasSSLConfig = nav.has( "database", "ssl", "enabled" )

// Check current segment
userNav = nav.from( "users" )
if ( userNav.isPresent() ) {
    println( "Users section exists" )
}

if ( userNav.isEmpty() ) {
    println( "Users section is empty" )
}
```

### Data Extraction Methods

**Basic Retrieval**

```javascript
nav = dataNavigate( appConfig )

// Get raw values
appName = nav.get( "application", "name" )
version = nav.get( "application", "version" )

// Get with defaults
timeout = nav.get( "application", "timeout", 30 )
retries = nav.get( "application", "retries", 3 )

// Throw if missing (for required values)
apiKey = nav.getOrThrow( "application", "apiKey" )
```

**Basic Retrieval**

```javascript
nav = dataNavigate( serverConfig )

// BoxLang is dynamic - get() handles all types automatically
serverName = nav.get( "server", "name", "default-server" )
port = nav.get( "server", "port", 8080 )
sslEnabled = nav.get( "server", "ssl", false )
timeout = nav.get( "server", "timeout", 5000 )
lastUpdated = nav.get( "server", "lastUpdated" )

// Complex types work too
dbConfig = nav.get( "database" )
serverList = nav.get( "servers" )
```

**Typed Retrievals**

For cases where you need explicit type conversion, BoxLang provides typed methods:

```javascript
// Only use these when you need explicit type conversion
port = nav.getAsInteger( "server", "port", 8080 )
timeout = nav.getAsLong( "server", "timeout", 5000 )
loadFactor = nav.getAsDouble( "server", "loadFactor", 0.75 )
sslEnabled = nav.getAsBoolean( "server", "ssl", false )
lastUpdated = nav.getAsDate( "server", "lastUpdated" )
dbConfig = nav.getAsStruct( "database" )
serverList = nav.getAsArray( "servers" )
```

### Conditional Processing

**Execute Code Based on Presence**

```javascript
nav = dataNavigate( userProfile )

// Execute if key exists
nav.ifPresent( "email", email -> {
    println( "User email: " & email )
    sendWelcomeEmail( email )
} )

// Execute with fallback
nav.ifPresentOrElse( 
    "phone",
    phone -> {
        println( "Calling: " & phone )
        makePhoneCall( phone )
    },
    () -> {
        println( "No phone number available" )
        sendEmailInstead()
    }
)
```

### Practical Examples

#### Configuration Management

```javascript
// Load application configuration
function loadAppConfig( configPath ) {
    var nav = dataNavigate( configPath )
    
    return {
        "appName": nav.get( "app", "name", "Unknown App" ),
        "version": nav.get( "app", "version", "1.0.0" ),
        "debug": nav.get( "app", "debug", false ),
        "database": {
            "host": nav.get( "database", "host", "localhost" ),
            "port": nav.get( "database", "port", 5432 ),
            "ssl": nav.get( "database", "ssl", true )
        },
        "cache": {
            "enabled": nav.get( "cache", "enabled", true ),
            "provider": nav.get( "cache", "provider", "memory" ),
            "ttl": nav.get( "cache", "ttl", 3600 )
        }
    }
}

// Usage
appConfig = loadAppConfig( "/app/config.json" )
println( "Starting " & appConfig.appName & " v" & appConfig.version )
```

#### API Response Processing

```javascript
// Process API response data
function processUserData( apiResponse ) {
    var nav = dataNavigate( apiResponse )
    var users = [ ]
    
    // Check if response is successful
    if ( nav.getAsBoolean( "success", false ) ) {
        // Navigate to user data
        var userNav = nav.from( "data", "users" )
        
        if ( userNav.isPresent() ) {
            var userArray = userNav.getAsArray( "items", [ ] )
            
            for ( var userData in userArray ) {
                var userDataNav = dataNavigate( userData )
                
                users.append( {
                    "id": userDataNav.get( "id" ),
                    "name": userDataNav.get( "profile", "fullName", "Unknown" ),
                    "email": userDataNav.get( "contact", "email" ),
                    "active": userDataNav.get( "status", "active", false ),
                    "lastLogin": userDataNav.get( "activity", "lastLogin" )
                } )
            }
        }
    }
    
    return users
}

// Usage with API response
apiResponse = '
{
    "success": true,
    "data": {
        "users": {
            "items": [
                {
                    "id": "123",
                    "profile": {"fullName": "Alice Johnson"},
                    "contact": {"email": "alice@example.com"},
                    "status": {"active": true},
                    "activity": {"lastLogin": "2024-01-15T10:30:00Z"}
                }
            ]
        }
    }
}
'

users = processUserData( apiResponse )
```

#### Feature Flag Management

```javascript
// Feature flag configuration
function createFeatureManager( configData ) {
    var nav = dataNavigate( configData )
    
    return {
        "isEnabled": ( feature ) -> {
            return nav.get( "features", feature, "enabled", false )
        },
        
        "getConfig": ( feature ) -> {
            var featureNav = nav.from( "features", feature )
            if ( featureNav.isEmpty() ) {
                return { }
            }
            
            return {
                "enabled": featureNav.get( "enabled", false ),
                "rolloutPercent": featureNav.get( "rollout", 100 ),
                "environments": featureNav.get( "environments", [ ] ),
                "config": featureNav.get( "config", { } )
            }
        },
        
        "shouldShowForUser": ( feature, userID ) -> {
            var config = this.getConfig( feature )
            if ( !config.enabled ) return false
            
            // Simple hash-based rollout
            var userHash = hash( userID ).left( 2 ).parseInt( 16 )
            return ( userHash % 100 ) < config.rolloutPercent
        }
    }
}

// Usage
featureConfig = '
{
    "features": {
        "newDashboard": {
            "enabled": true,
            "rollout": 50,
            "environments": ["staging", "production"]
        },
        "betaFeature": {
            "enabled": false
        }
    }
}
'

features = createFeatureManager( featureConfig )

if ( features.isEnabled( "newDashboard" ) ) {
    println( "New dashboard is enabled" )
}
```

#### Database Configuration

```javascript
// Multi-environment database configuration
function getDatabaseConfig( environment = "development" ) {
    var nav = dataNavigate( "/config/database.json" )
    var envNav = nav.from( "environments", environment )
    
    // Fallback to default if environment not found
    if ( envNav.isEmpty() ) {
        envNav = nav.from( "environments", "default" )
    }
    
    var config = {
        "driver": envNav.get( "driver", "mysql" ),
        "host": envNav.get( "host", "localhost" ),
        "port": envNav.get( "port", 3306 ),
        "database": envNav.get( "database", "myapp" ),
        "username": envNav.get( "username", "root" ),
        "password": envNav.get( "password", "" ),
        "ssl": envNav.get( "ssl", false ),
        "pooling": {
            "enabled": envNav.get( "pool", "enabled", true ),
            "maxConnections": envNav.get( "pool", "max", 10 ),
            "timeout": envNav.get( "pool", "timeout", 30 )
        }
    }
    
    // Apply global settings
    var globalNav = nav.from( "global" )
    if ( globalNav.isPresent() ) {
        config.charset = globalNav.get( "charset", "utf8" )
        config.timezone = globalNav.get( "timezone", "UTC" )
    }
    
    return config
}

// Usage
dbConfig = getDatabaseConfig( "production" )
```

#### Log Configuration Processing

```javascript
// Parse logging configuration
function setupLogging( logConfigPath ) {
    var nav = dataNavigate( logConfigPath )
    var loggers = [ ]
    
    // Get global log level
    var globalLevel = nav.get( "logging", "level", "INFO" )
    
    // Process appenders
    var appendersNav = nav.from( "logging", "appenders" )
    if ( appendersNav.isPresent() ) {
        
        // Console appender
        appendersNav.ifPresent( "console", consoleConfig -> {
            var consoleNav = dataNavigate( consoleConfig )
            loggers.append( {
                "type": "console",
                "level": consoleNav.get( "level", globalLevel ),
                "pattern": consoleNav.get( "pattern", "%d{yyyy-MM-dd HH:mm:ss} - %m%n" ),
                "colored": consoleNav.get( "colored", true )
            } )
        } )
        
        // File appender
        appendersNav.ifPresent( "file", fileConfig -> {
            var fileNav = dataNavigate( fileConfig )
            loggers.append( {
                "type": "file",
                "level": fileNav.get( "level", globalLevel ),
                "path": fileNav.get( "path", "/logs/app.log" ),
                "maxSize": fileNav.get( "maxSize", "10MB" ),
                "maxFiles": fileNav.get( "maxFiles", 5 )
            } )
        } )
    }
    
    return loggers
}
```

### Error Handling and Validation

#### Safe Navigation Patterns

```javascript
// Safe navigation with validation
function getSecureConfig( configPath ) {
    try {
        var nav = dataNavigate( configPath )
        
        // Validate required sections exist
        if ( !nav.has( "security" ) ) {
            throw( type: "ConfigurationError", message: "Security configuration missing" )
        }
        
        var secNav = nav.from( "security" )
        
        return {
            "encryption": {
                "algorithm": secNav.getOrThrow( "encryption", "algorithm" ),
                "keyLength": secNav.get( "encryption", "keyLength", 256 ) // Keep as number
            },
            "authentication": {
                "provider": secNav.get( "auth", "provider", "local" ),
                "timeout": secNav.get( "auth", "timeout", 3600 ) // Keep as number
            }
        }
        
    } catch ( any e ) {
        writeLog( "Failed to load security config: " & e.message, "error" )
        return getDefaultSecurityConfig()
    }
}

function getDefaultSecurityConfig() {
    return {
        "encryption": {
            "algorithm": "AES",
            "keyLength": 256
        },
        "authentication": {
            "provider": "local",
            "timeout": 3600
        }
    }
}
```

#### Graceful Degradation

```javascript
// Load configuration with graceful fallbacks
function loadConfigWithFallbacks( primaryPath, fallbackPath ) {
    var config = { }
    
    // Try primary configuration
    try {
        var primaryNav = dataNavigate( primaryPath )
        config = extractConfig( primaryNav )
        println( "Loaded primary configuration from: " & primaryPath )
    } catch ( any e ) {
        writeLog( "Primary config failed: " & e.message, "warn" )
        
        // Try fallback configuration
        try {
            var fallbackNav = dataNavigate( fallbackPath )
            config = extractConfig( fallbackNav )
            println( "Loaded fallback configuration from: " & fallbackPath )
        } catch ( any e2 ) {
            writeLog( "Fallback config failed: " & e2.message, "error" )
            config = getHardcodedDefaults()
            println( "Using hardcoded default configuration" )
        }
    }
    
    return config
}

function extractConfig( nav ) {
    return {
        "app": nav.get( "name", "DefaultApp" ),
        "port": nav.get( "server", "port", 8080 ),
        "debug": nav.get( "debug", false )
    }
}
```

## Advanced Patterns

#### Configuration Inheritance

```javascript
// Implement configuration inheritance
function buildInheritedConfig( environment ) {
    var nav = dataNavigate( "/config/app.json" )
    var config = { }
    
    // Start with base configuration
    var baseNav = nav.from( "base" )
    if ( baseNav.isPresent() ) {
        config = extractAllSettings( baseNav )
    }
    
    // Apply environment-specific overrides
    var envNav = nav.from( "environments", environment )
    if ( envNav.isPresent() ) {
        var envConfig = extractAllSettings( envNav )
        config = mergeConfigs( config, envConfig )
    }
    
    return config
}

function mergeConfigs( base, override ) {
    // Simple merge - in practice you'd want deep merging
    var merged = duplicate( base )
    for ( var key in override ) {
        merged[ key ] = override[ key ]
    }
    return merged
}
```

#### Dynamic Configuration Validation

```javascript
// Validate configuration structure
function validateConfig( configData ) {
    var nav = dataNavigate( configData )
    var errors = [ ]
    
    // Required fields
    var required = [ 
        [ "app", "name" ],
        [ "app", "version" ],
        [ "database", "host" ]
    ]
    
    for ( var path in required ) {
        if ( !nav.has( path[ 1 ], path[ 2 ] ?: "" ) ) {
            errors.append( "Missing required field: " & path.toList( "." ) )
        }
    }
    
    // Type validations
    nav.ifPresent( "server", serverConfig -> {
        var serverNav = dataNavigate( serverConfig )
        var port = serverNav.get( "port" )
        
        if ( port != null && ( !isNumeric( port ) || port <= 0 || port > 65535 ) ) {
            errors.append( "Invalid port number: " & port )
        }
    } )
    
    return {
        "valid": errors.isEmpty(),
        "errors": errors
    }
}
```

## Best Practices

#### 1. Use Meaningful Defaults

```javascript
// Provide sensible defaults for all configuration values - get() works dynamically
serverConfig = nav.get( "server", {
    "host": "localhost",
    "port": 8080,
    "ssl": false,
    "timeout": 30
} )
```

#### 2. Validate Critical Configuration

```javascript
// Always validate required configuration
apiKey = nav.getOrThrow( "api", "key" ) // Will throw if missing
dbHost = nav.getOrThrow( "database", "host" )
```

#### 3. Leverage BoxLang's Dynamic Nature

```javascript
// BoxLang handles all types automatically with get()
enabled = nav.get( "feature", "enabled", false )
maxRetries = nav.get( "http", "maxRetries", 3 )
serverName = nav.get( "server", "name", "default" )
config = nav.get( "database" ) // Works for complex types too
```

#### 4. Handle Missing Sections Gracefully

```javascript
// Check for section existence before processing
var cacheNav = nav.from( "cache" )
if ( cacheNav.isPresent() ) {
    // Configure caching
    setupCaching( cacheNav )
} else {
    // Use default caching or disable
    useDefaultCaching()
}
```

#### 5. Log Configuration Issues

```javascript
// Log when using fallbacks or defaults
nav.ifPresentOrElse(
    "timeout",
    timeout -> println( "Using configured timeout: " & timeout ),
    () -> println( "No timeout configured, using default: 30s" )
)
```

## Conclusion

Data Navigators offer a robust and fluent way to work with complex data structures in BoxLang. They eliminate common errors, provide excellent defaults, and make configuration management both safe and readable.

Key benefits:

* **Safe Navigation**: No more null pointer exceptions when traversing data
* **Type Safety**: Built-in type conversion with sensible defaults
* **Fluent API**: Chainable methods that read like natural language
* **Flexible Sources**: Works with JSON files, strings, structures, and maps
* **Error Handling**: Graceful fallbacks and validation capabilities

Whether you're processing API responses, managing application configuration, or working with complex data structures, Data Navigators make your code more robust and maintainable.
