---
description: Work with property files using BoxLang's fluent PropertyFile API
icon: file-lines
---

# 📄 Property Files

> Introduced in v1.4.0

## 🙋 What are Property Files?

Property files are simple text files that store configuration data in key-value pairs. They're commonly used for application settings, environment configurations, and localization. BoxLang provides a powerful, fluent API for reading, writing, and manipulating property files with ease.

```text
# Example property file
app.name=My Application
app.version=1.0.0
database.host=localhost
database.port=5432
```

### **🎯 Why Use BoxLang's PropertyFile Utility?**

* **Fluent API:** Chain operations together for clean, readable code
* **Format Preservation:** Maintains comments, whitespace, and original formatting
* **Smart Parsing:** Handles escaped characters, unicode, and line continuations
* **Type Safety:** Built-in validation and error handling
* **Memory Efficient:** Lazy loading and caching for optimal performance
* **Cross-Platform:** Works consistently across different operating systems

## 🚀 Getting Started

### Creating a PropertyFile Object

The main entry point is the `propertyFile()` BIF (Built-In Function):

```javascript
// Create a new empty property file
props = propertyFile();

// Create a new property file with a specific path that will be created if it doesn't exist
props = propertyFile( "./config.properties" );

// Load an existing property file
props = propertyFile( "/path/to/config.properties" );

// Load from a relative path
props = propertyFile( "./config/application.properties" );
```

**If the file path doesn't exist, the PropertyFile object will be created with that path for future use when storing.**

## 📖 Reading Properties

### 🔍 Getting Property Values

```javascript
// Load a property file
props = propertyFile( "./config.properties" );

// Get a property value
appName = props.get( "app.name" );

// Get with a default value
timeout = props.get( "connection.timeout", "30" );

// Check if a property exists
if ( props.exists( "debug.enabled" ) ) {
    writeOutput( "Debug mode is configured" );
}
```

### 📊 Getting All Properties

```javascript
// Get all properties as a struct
allProps = props.getAsStruct();
writeOutput( "App Name: " & allProps.appName );

// Get all properties as a Java Map
allPropsMap = props.getAsMap();

// Get just the property names
propertyNames = props.getPropertyNames();
writeDump( propertyNames );
```

### 🔢 Property File Information

```javascript
// Check if the file has any properties
if ( props.hasProperties() ) {
    writeOutput( "Found " & props.size() & " properties" );
}

// Get the file path
filePath = props.getPath();
```

## ✏️ Writing Properties

### 🔧 Setting Individual Properties

```javascript
// Create or load a property file
props = propertyFile( "./myapp.properties" );

// Set a single property
props.set( "app.name", "My Amazing App" );

// Chain multiple operations
props.set( "app.version", "2.0.0" )
     .set( "app.author", "BoxLang Developer" )
     .set( "app.environment", "production" );
```

### 📝 Setting Multiple Properties

```javascript
// Set multiple properties from a struct
newProps = {
    "database.host": "prod-db.example.com",
    "database.port": "5432",
    "database.name": "myapp_prod"
};

props.setMulti( newProps );

// Set multiple properties from another property file
otherProps = propertyFile( "./defaults.properties" );
props.mergeStruct( otherProps.getAsStruct() );
```

### 🗑️ Removing Properties

```javascript
// Remove a single property
props.remove( "debug.enabled" );

// Remove multiple properties
propsToRemove = [ "temp.setting", "old.config", "deprecated.value" ];
props.removeMulti( propsToRemove );

// Clear all properties (keeps comments and formatting)
props.clearProperties();

// Clear everything including comments
props.clear();
```

## 💾 Saving Property Files

### 📁 Storing to File

```javascript
// Save to the original file path
props.store();

// Save to a different path
props.store( "./backup/config.properties" );

// Chain operations with saving
props.set( "last.updated", now() )
     .addComment( "Updated on " & dateFormat( now(), "yyyy-mm-dd" ) )
     .store();
```

## 🎨 Formatting and Comments

### 💬 Adding Comments

```javascript
props.addComment( "Application Configuration" )
     .addComment( "Generated on " & dateFormat( now(), "full" ) )
     .addBlankLine()
     .set( "app.name", "My App" );
```

### 📏 Line Width Control

```javascript
// Set maximum line width for long values
props.setMaxLineWidth( 100 );

// Long values will be automatically wrapped with continuation characters
props.set( "long.description", "This is a very long description that will be automatically wrapped to multiple lines when it exceeds the maximum line width setting" );
```

## 🔄 Advanced Operations

### 🔀 Merging Property Files

```javascript
// Merge properties from another file
defaultProps = propertyFile( "./defaults.properties" );
userProps = propertyFile( "./user.properties" );

// Merge user properties into defaults
finalProps = defaultProps.mergeStruct( userProps.getAsStruct() );

// Save the merged result
finalProps.store( "./final.properties" );
```

### 🏗️ Creating from Existing Data

```javascript
// Create from a struct
configStruct = {
    "server.port": "8080",
    "server.host": "localhost",
    "app.debug": "false"
};

props = propertyFile().setMulti( configStruct );

// Create from a map (Java interop)
import java.util.HashMap;
configMap = createObject( "java", "java.util.HashMap" ).init();
configMap.put( "database.url", "jdbc:mysql://localhost:3306/mydb" );

props = propertyFile().mergeMap( configMap );
```

## 📚 Common Usage Patterns

### 🔧 Configuration Management

```javascript
// Load application configuration
config = propertyFile( expandPath( "./config/app.properties" ) );

// Update configuration at runtime
config.set( "app.last.startup", now() )
      .set( "app.instance.id", createUUID() )
      .store();

// Environment-specific settings
environment = config.get( "app.environment", "development" );
if ( environment == "production" ) {
    config.set( "logging.level", "ERROR" );
} else {
    config.set( "logging.level", "DEBUG" );
}
```

### 🌐 Internationalization (i18n)

```javascript
// Load language-specific properties
locale = session.locale ?: "en_US";
messages = propertyFile( "./i18n/messages_#locale#.properties" );

// Get localized messages
welcomeMsg = messages.get( "welcome.message", "Welcome!" );
errorMsg = messages.get( "error.invalid.input", "Invalid input provided" );
```

### 🏭 Environment Configuration

```javascript
// Load environment-specific configuration
envFile = "./config/" & ( server.environment ?: "development" ) & ".properties";
envConfig = propertyFile( envFile );

// Override with local settings if they exist
localConfig = "./config/local.properties";
if ( fileExists( expandPath( localConfig ) ) ) {
    envConfig.mergeStruct( propertyFile( localConfig ).getAsStruct() );
}

// Use the configuration
dbHost = envConfig.get( "database.host" );
dbPort = envConfig.get( "database.port", "3306" );
```

### 📝 Build and Deployment

```javascript
// Generate build information
buildProps = propertyFile()
    .addComment( "Build Information" )
    .addComment( "Generated on " & dateFormat( now(), "yyyy-mm-dd HH:nn:ss" ) )
    .addBlankLine()
    .set( "build.timestamp", now() )
    .set( "build.version", application.version )
    .set( "build.revision", getGitRevision() )
    .set( "build.environment", server.environment )
    .store( "./build/build.properties" );
```

## 🔍 Data Export and Conversion

### 📄 Export Formats

```javascript
// Convert to JSON
propsAsJSON = props.toJSON();
writeOutput( propsAsJSON );

// Convert to string representation
propsAsString = props.toString();

// Get as native BoxLang struct for further processing
nativeStruct = props.getAsStruct();
```

### 🔄 Format Conversion

```javascript
// Convert property file to JSON file
props = propertyFile( "./config.properties" );
jsonData = props.toJSON();
fileWrite( "./config.json", jsonData );

// Convert JSON to property file
jsonConfig = deserializeJSON( fileRead( "./settings.json" ) );
propertyFile().setMulti( jsonConfig ).store( "./settings.properties" );
```

## 🛡️ Error Handling

### 🚨 Exception Management

```javascript
try {
    props = propertyFile( "./config.properties" );

    // Attempt to get a required property
    dbHost = props.get( "database.host" );

} catch ( any e ) {
    if ( e.type == "IllegalArgumentException" ) {
        writeOutput( "Required property not found: " & e.message );
        // Set default values
        props.set( "database.host", "localhost" )
             .store();
    } else {
        writeOutput( "Error loading property file: " & e.message );
    }
}
```

### ✅ Safe Property Access

```javascript
// Safe property access with defaults
config = propertyFile( "./app.properties" );

// Always provide defaults for critical settings
port = config.get( "server.port", "8080" );
timeout = config.get( "request.timeout", "30" );
debug = config.get( "debug.enabled", "false" ).toBoolean();

// Validate critical properties exist
requiredProps = [ "database.host", "database.username", "api.key" ];
for ( prop in requiredProps ) {
    if ( !config.exists( prop ) ) {
        throw( type="ConfigurationError", message="Required property missing: #prop#" );
    }
}
```

## 🎯 Best Practices

### ✅ Do's

* **Use descriptive property names** with dot notation for hierarchy
* **Provide default values** for optional configuration
* **Add comments** to explain complex or important settings
* **Validate required properties** at application startup
* **Use environment-specific files** for different deployment scenarios
* **Keep sensitive data separate** and secure (passwords, API keys)

### ❌ Don'ts

* **Don't hardcode file paths** - use relative paths or configuration
* **Don't ignore exceptions** - handle file access errors gracefully
* **Don't store large binary data** in property files
* **Don't forget to call store()** after making changes
* **Don't mix different data types** - property values are always strings

## 🚦 Performance Tips

### 🎯 Optimization Guidelines

* **Cache PropertyFile objects** for frequently accessed configurations
* **Use getAsStruct()** once and reuse for multiple property access
* **Minimize file I/O** by batching property updates
* **Set appropriate maxLineWidth** for your use case
* **Avoid unnecessary store() calls** - batch your changes

## 🔗 Integration Examples

### 🌐 Web Application Configuration

```javascript
// Application.bx
component {
    this.name = "MyApp";

    function onApplicationStart() {
        // Load application configuration
        application.config = propertyFile( expandPath( "./config/app.properties" ) );

        // Set application settings from properties
        this.datasource = application.config.get( "app.datasource" );
        this.sessionTimeout = application.config.get( "session.timeout", "30" );

        return true;
    }
}
```

### 🔧 Module Configuration

```javascript
// ModuleConfig.bx
component {
    function configure() {
        // Load module-specific properties
        var moduleProps = propertyFile( modulePath & "/config/module.properties" );

        // Configure module settings
        settings = {
            "apiEndpoint": moduleProps.get( "api.endpoint", "https://api.example.com" ),
            "timeout": moduleProps.get( "request.timeout", "30" ),
            "retryAttempts": moduleProps.get( "retry.attempts", "3" )
        };
    }
}
```

### 📱 CLI Application Settings

```javascript
// CLI script
config = propertyFile( expandPath( "~/.myapp/config.properties" ) );

// Get user preferences
verbose = config.get( "output.verbose", "false" ).toBoolean();
logLevel = config.get( "log.level", "INFO" );
defaultPath = config.get( "default.path", getCurrentDirectory() );

// Update usage statistics
config.set( "last.used", now() )
      .set( "usage.count", val( config.get( "usage.count", "0" ) ) + 1 )
      .store();
```

Property files in BoxLang provide a robust, flexible way to manage configuration data with a clean, fluent API that makes complex property file operations simple and intuitive. Whether you're building web applications, CLI tools, or enterprise systems, the PropertyFile utility adapts to your needs while maintaining data integrity and format preservation.
