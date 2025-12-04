---
description: Learn how to use annotations in BoxLang for metadata-driven programming with classes, properties, and functions
icon: tag
---

# Annotations

Annotations in BoxLang are powerful metadata markers that can be attached to classes, properties, and functions. They enable metadata-driven programming, dependency injection, aspect-oriented programming, and runtime reflection capabilities.

## 🎯 Where Annotations Can Be Used

Annotations can be applied to three main constructs in BoxLang:

- **Classes** - Mark classes with metadata for framework behaviors
- **Properties** - Define metadata for class properties
- **Functions** - Add metadata to methods and functions

## 📝 Annotation Syntax

BoxLang supports two primary syntax styles for annotations: **standalone annotations** (using `@` prefix) and **inline annotations** (embedded in the declaration).

### Standalone Annotations

Standalone annotations appear on the line before the construct they annotate:

```js
@annotationName
class MyClass {
}

@inject
property userService;

@cached
function getData() {
}
```

### Inline Annotations

Inline annotations are embedded directly in the construct declaration:

```js
class singleton {
}

property name="test" inject;

function hello() annotation1 annotation2="value" {
}
```

## 💡 Annotation Values

Annotations can have different types of values:

### No Value (Empty String)

When an annotation has no value, it's defined with an empty string value by default:

```js
@singleton
class UserService {
}

property userRepository inject;
```

### String Values

Annotations can have simple string values:

```js
@inject( "UserService" )
property userService;

@cacheName( "users" )
function getUsers() {
}
```

String values can be specified with or without quotes (for simple values):

```js
@inject( UserService )
// Equivalent to:
@inject( "UserService" )
```

### Boolean Values

```js
@singleton( true )
class DatabaseService {
}

@required( false )
property optionalField;
```

### Array Literal Values

Annotations can accept array literals:

```js
@roles( [ "admin", "moderator" ] )
function deleteUser() {
}

@depends( [ "LogService", "CacheService" ] )
class UserService {
}
```

### Struct Literal Values

Struct literals provide named configuration:

```js
@cache( { timeout: 60, provider: "redis" } )
function getExpensiveData() {
}

@mcpTool( {
    name: "processData",
    description: "Processes user data",
    version: "2.0.0"
} )
function process() {
}
```

### Nested Literals

Array and struct literals can be nested:

```js
@configuration( {
    database: {
        host: "localhost",
        credentials: [ "user", "pass" ]
    },
    features: [ "caching", "logging" ]
} )
class Application {
}
```

## 📋 Annotation Format Examples

Different annotation formats for the same annotation:

```js
// Simple annotation - name from method name, defaults applied
@mcpTool
function processData() {
}

// With description only
@mcpTool( "Processes and validates user data" )
function processData() {
}

// Full configuration
@mcpTool( {
    name: "dataProcessor",
    description: "Processes and validates user data",
    version: "2.1.0"
} )
function processData() {
}
```

## 🔍 Runtime Metadata Access

BoxLang provides multiple ways to access annotation metadata at runtime, enabling powerful metaprogramming capabilities.

### Using getMetadata()

The `getMetadata()` function returns metadata for any BoxLang object:

```js
class singleton inject="CacheService" {
    @required
    property userName;

    @cached( { timeout: 60 } )
    function getData() {
        return "data";
    }
}

// Get metadata for an instance
myInstance = new MyClass();
meta = getMetadata( myInstance );

// Access class annotations
println( meta.singleton ); // "" (empty string, annotation exists)
println( meta.inject ); // "CacheService"

// Access property metadata
println( meta.properties[ 1 ].required ); // "" (annotation exists)

// Access function metadata
println( meta.functions.getData.cached.timeout ); // 60
```

### Using getClassMetadata()

Get metadata for a class without instantiating it:

```js
// Using class path
meta = getClassMetadata( "com.myapp.services.UserService" );

// Access annotations
if ( structKeyExists( meta, "singleton" ) ) {
    println( "This is a singleton class" );
}
```

### Using $bx.meta

Every BoxLang object has a `$bx.meta` property that provides direct access to its metadata:

```js
class singleton {
    property name="id" required;
}

myClass = new MyClass();

// Access metadata directly
println( myClass.$bx.meta.singleton ); // ""
println( myClass.$bx.meta.properties[ 1 ].required ); // ""

// Works with any object
myStruct = { name: "John" };
println( myStruct.$bx.meta ); // Struct metadata
```

## 🎨 Common Annotation Patterns

### Dependency Injection

```js
@singleton
class UserService {

    @inject
    property userRepository;

    @inject( "LogService" )
    property logger;

    @inject( "CacheService" )
    property cache;
}
```

### Caching

```js
class DataService {

    @cached( { timeout: 300, provider: "redis" } )
    function getExpensiveData() {
        return queryDatabase();
    }

    @cacheFlush( "getExpensiveData" )
    function updateData() {
        // Updates that invalidate cache
    }
}
```

### Security & Authorization

```js
class AdminController {

    @roles( [ "admin", "superuser" ] )
    @authenticated
    function deleteUser() {
        // Admin-only functionality
    }

    @permissions( [ "user.read", "user.write" ] )
    function updateUser() {
        // Permission-based access
    }
}
```

### Validation

```js
class User {

    @required
    @length( { min: 3, max: 50 } )
    property name;

    @required
    @email
    property emailAddress;

    @range( { min: 18, max: 120 } )
    property age;
}
```

### Framework Integration

```js
@restController
@route( "/api/users" )
class UserController {

    @get
    @route( "/:id" )
    function getUser( required numeric id ) {
        return userService.find( id );
    }

    @post
    @validated
    function createUser( required struct data ) {
        return userService.create( data );
    }
}
```

## 🔧 Custom Annotations

You can create your own annotations for custom framework features:

```js
@myCustomAnnotation( {
    behavior: "special",
    priority: 10
} )
class CustomService {

    @myValidator( { pattern: "^\d{3}-\d{4}$" } )
    property phoneNumber;
}

// Later, read and act on your custom annotations
meta = getMetadata( myService );
if ( structKeyExists( meta, "myCustomAnnotation" ) ) {
    config = meta.myCustomAnnotation;
    // Apply custom behavior based on annotation
}
```

## 💻 Complete Example

```js
@singleton
@service( { type: "business" } )
class UserService {

    @inject
    property userRepository;

    @inject( "LogService" )
    property logger;

    @transactional
    @cached( { timeout: 60, provider: "memory" } )
    function getAllUsers() {
        logger.info( "Fetching all users" );
        return userRepository.findAll();
    }

    @transactional
    @roles( [ "admin" ] )
    @audit( { action: "user.delete" } )
    function deleteUser( required numeric id ) {
        logger.warn( "Deleting user: #id#" );
        userRepository.delete( id );
    }

    @validated
    function createUser( required struct userData ) {
        // Validation happens before this runs
        return userRepository.create( userData );
    }
}

// Runtime metadata inspection
service = new UserService();
meta = service.$bx.meta;

// Check if it's a singleton
if ( structKeyExists( meta, "singleton" ) ) {
    println( "Service is a singleton" );
}

// Get function metadata
getAllUsersMeta = meta.functions.getAllUsers;
println( "Cache timeout: #getAllUsersMeta.cached.timeout#" );
println( "Is transactional: #structKeyExists( getAllUsersMeta, 'transactional' )#" );

// Inspect property injection
for ( prop in meta.properties ) {
    if ( structKeyExists( prop, "inject" ) ) {
        println( "Property #prop.name# requires injection" );
        if ( len( prop.inject ) ) {
            println( "  Inject: #prop.inject#" );
        }
    }
}
```

## 🎯 Best Practices

1. **Be Consistent** - Use the same annotation style throughout your codebase
2. **Document Custom Annotations** - Create documentation for custom annotations your framework uses
3. **Use Struct Literals for Complex Config** - When annotations need multiple values, use struct literals for clarity
4. **Leverage Metadata** - Use runtime metadata inspection for framework features like DI, validation, and caching
5. **Namespace Custom Annotations** - Prefix custom annotations to avoid conflicts (`@myapp_feature`)
6. **Keep It Simple** - Don't overuse annotations; keep your code readable
7. **Test Metadata Access** - Ensure your metaprogramming code handles missing annotations gracefully

## 📚 Related Topics

- {% content-ref url="README.md" %}Classes Overview{% endcontent-ref %}
- {% content-ref url="properties.md" %}Properties{% endcontent-ref %}
- {% content-ref url="functions.md" %}Functions{% endcontent-ref %}
- {% content-ref url="../reference/built-in-functions/struct.md" %}Struct Functions{% endcontent-ref %}
