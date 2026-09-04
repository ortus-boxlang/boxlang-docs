---
description: >-
  Powerful JSON serialization and deserialization with automatic class
  conversion and custom formatting
icon: node-js
---

# JSON

BoxLang provides comprehensive JSON (JavaScript Object Notation) support with automatic serialization of BoxLang data types, including classes, queries, arrays, structs, and more. The JSON engine is built on Jackson Jr and includes custom serializers for BoxLang-specific types.

{% hint style="info" %}
**Built on Jackson Jr**: BoxLang uses the high-performance Jackson Jr library with custom serializers and deserializers for BoxLang types. This ensures fast, reliable JSON processing with full control over the serialization format.
{% endhint %}

## 💻 JSON in Code

Let's explore JSON operations with practical examples:

```js
// Create complex data structure
user = {
    id: 1,
    name: "Alice Johnson",
    email: "alice@example.com",
    active: true,
    roles: [ "admin", "developer" ],
    metadata: {
        lastLogin: now(),
        preferences: { theme: "dark", language: "en" }
    }
};

// Serialize to JSON
json = user.toJSON();
println( json );

// Pretty print for readability
prettyJson = jsonSerialize( user, pretty: true );
println( prettyJson );

// Deserialize back to BoxLang data
restored = json.fromJSON();
println( "Name: " & restored.name );

// Validate JSON
if ( isJSON( json ) ) {
    println( "Valid JSON!" );
}

// List to JSON
tags = "programming,boxlang,json,tutorial";
jsonTags = tags.listToJSON();
println( jsonTags ); // ["programming","boxlang","json","tutorial"]
```

## 📚 JSON Built-In Functions (BIFs)

BoxLang provides JSON BIFs that can be called as functions or member methods on compatible types.

### Core JSON Functions

| Function            | Purpose                     | Member Method Available     |
| ------------------- | --------------------------- | --------------------------- |
| `jsonSerialize()`   | Convert data to JSON string | `toJSON()` on most types    |
| `jsonDeserialize()` | Parse JSON string to data   | `fromJSON()` on strings     |
| `isJSON()`          | Validate JSON string        | No                          |
| `jsonPrettify()`    | Format JSON for readability | `jsonPrettify()` on strings |

### Member Method Support

The `toJSON()` member method is available on:

* ✅ **Structs** - `myStruct.toJSON()`
* ✅ **Arrays** - `myArray.toJSON()`
* ✅ **Queries** - `myQuery.toJSON()`
* ✅ **Classes** - `myClass.toJSON()` (with automatic property serialization)
* ✅ **Numbers** - `123.toJSON()`
* ✅ **Booleans** - `true.toJSON()`
* ✅ **Strings** - `"text".listToJSON()` (converts list to JSON array)

The `fromJSON()` member method is available on:

* ✅ **Strings** - `jsonString.fromJSON()`

## 📤 JSON Serialization (jsonSerialize / toJSON)

Convert any BoxLang data to JSON format using `jsonSerialize()` or the `toJSON()` member method.

### Basic Serialization

```js
// Function syntax
person = { name: "Luis Majano", company: "Ortus Solutions", year: 2006 };
json = jsonSerialize( person );

// Member method syntax (preferred)
json = person.toJSON();

// Both produce: {"name":"Luis Majano","company":"Ortus Solutions","year":2006}
```

### Supported Data Types

BoxLang automatically serializes all native types:

```js
// Simple values
jsonSerialize( 42 );                    // "42"
jsonSerialize( true );                  // "true"
jsonSerialize( "Hello" );               // '"Hello"'

// Complex types
jsonSerialize( [ 1, 2, 3 ] );          // "[1,2,3]"
jsonSerialize( { a: 1, b: 2 } );       // '{"a":1,"b":2}'

// Dates (ISO 8601 format)
jsonSerialize( now() );                // "2025-12-09T14:30:00Z"

// Queries (see Query Serialization section)
qry = queryNew( "id,name", "integer,varchar", [ { id: 1, name: "Test" } ] );
jsonSerialize( qry );                  // Array of structs by default
```

### 🎨 Pretty Printing

Format JSON with indentation for readability:

```js
data = {
    name: "John Doe",
    age: 30,
    address: {
        street: "123 Main St",
        city: "Anytown",
        country: "USA"
    },
    hobbies: [ "reading", "cycling", "photography" ]
};

// Compact (default)
compactJson = data.toJSON();
// {"name":"John Doe","age":30,"address":{...}}

// Pretty formatted
prettyJson = jsonSerialize( data, pretty: true );
/* Output:
{
  "name" : "John Doe",
  "age" : 30,
  "address" : {
    "street" : "123 Main St",
    "city" : "Anytown",
    "country" : "USA"
  },
  "hobbies" : [ "reading", "cycling", "photography" ]
}
*/

// Great for configuration files
writeFile( "config.json", appConfig.toJSON( pretty: true ) );

// Or use jsonPrettify on existing JSON
uglyJson = '{"a":1,"b":{"c":2}}';
prettyJson = uglyJson.jsonPrettify();
```

### 🔑 Key Casing Preservation

BoxLang preserves the exact casing of struct keys in JSON:

```js
// Case-sensitive keys (quoted)
person = {
    "firstName": "Luis",
    "lastName": "Majano",
    "company": "Ortus Solutions"
};
person.toJSON();
// {"firstName":"Luis","lastName":"Majano","company":"Ortus Solutions"}

// Case-insensitive keys (unquoted) - stored uppercase
person = {
    firstName: "Luis",
    lastName: "Majano",
    company: "Ortus Solutions"
};
person.toJSON();
// {"FIRSTNAME":"Luis","LASTNAME":"Majano","COMPANY":"Ortus Solutions"}
```

{% hint style="success" %}
**Best Practice**: Always quote struct keys if you need exact casing in JSON output, especially for REST APIs and JavaScript interoperability.
{% endhint %}

### 📊 Query Serialization

Queries can be serialized in three different formats using the `queryFormat` argument:

```js
users = queryNew(
    "id,name,email",
    "integer,varchar,varchar",
    [
        { id: 1, name: "Alice", email: "alice@example.com" },
        { id: 2, name: "Bob", email: "bob@example.com" }
    ]
);

// Format: "struct" (default) - Array of structs
jsonSerialize( users, queryFormat: "struct" );
/* [
    {"id":1,"name":"Alice","email":"alice@example.com"},
    {"id":2,"name":"Bob","email":"bob@example.com"}
] */

// Format: "row" or "false" - Columns and row data arrays
jsonSerialize( users, queryFormat: "row" );
/* {
    "columns": ["id","name","email"],
    "data": [
        [1,"Alice","alice@example.com"],
        [2,"Bob","bob@example.com"]
    ]
} */

// Format: "column" or "true" - Columns and column data
jsonSerialize( users, queryFormat: "column" );
/* {
    "rowCount": 2,
    "columns": ["id","name","email"],
    "data": {
        "id": [1,2],
        "name": ["Alice","Bob"],
        "email": ["alice@example.com","bob@example.com"]
    }
} */

// Member method syntax
json = users.toJSON( queryFormat: "struct" );
```

{% hint style="info" %}
**Default Format**: Queries serialize as arrays of structs (`queryFormat="struct"`) when no format is specified. This is the most common format for REST APIs.
{% endhint %}

## 🎯 Class Serialization (The Magic!)

BoxLang makes it incredibly easy to serialize classes to JSON with **automatic property introspection**. The `BoxClassSerializer` intelligently converts class instances to JSON by examining their properties and respecting serialization annotations.

### Automatic Property Serialization

```js
/**
 * User class with automatic JSON serialization
 */
class User {
    property name="id" type="numeric";
    property name="username" type="string";
    property name="email" type="string";
    property name="createdDate" type="date";
    property name="roles" type="array";

    function init( id, username, email ) {
        variables.id = arguments.id;
        variables.username = arguments.username;
        variables.email = arguments.email;
        variables.createdDate = now();
        variables.roles = [ "user" ];
        return this;
    }
}

// Create instance
user = new User( 1, "alice", "alice@example.com" );

// Serialize to JSON - automatically includes all properties!
json = user.toJSON();
/* {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com",
    "createdDate": "2025-12-09T14:30:00Z",
    "roles": ["user"]
} */
```

### 🔒 Controlling Serialization with Annotations

Use annotations to control what gets serialized:

```js
/**
 * User class with serialization control
 */
@serializable( true )
@jsonExclude( "createdBy,modifiedBy" )
class User {
    property name="id" type="numeric";
    property name="username" type="string";
    property name="email" type="string";

    // Exclude sensitive data
    @jsonExclude( true )
    property name="password" type="string";

    @serializable( false )
    property name="passwordHash" type="string";

    // Exclude audit fields via class annotation
    property name="createdBy" type="string";
    property name="modifiedBy" type="string";

    // This will be included
    property name="active" type="boolean";
}

user = new User();
user.id = 1;
user.username = "alice";
user.email = "alice@example.com";
user.password = "secret123";        // Won't be serialized
user.passwordHash = "hashed...";     // Won't be serialized
user.createdBy = "admin";            // Won't be serialized
user.active = true;

json = user.toJSON();
/* {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com",
    "active": true
} */
```

### 🎨 Custom toJSON() Method

Override serialization completely with your own `toJSON()` method:

```js
class User {
    property name="id" type="numeric";
    property name="firstName" type="string";
    property name="lastName" type="string";
    property name="email" type="string";
    property name="passwordHash" type="string";

    /**
     * Custom JSON serialization
     * Combines firstName and lastName into fullName
     * Excludes sensitive data
     */
    function toJSON() {
        return {
            "id": variables.id,
            "fullName": "#variables.firstName# #variables.lastName#",
            "email": variables.email,
            "initials": "#variables.firstName.left(1)##variables.lastName.left(1)#"
        };
    }
}

user = new User();
user.id = 1;
user.firstName = "Alice";
user.lastName = "Johnson";
user.email = "alice@example.com";
user.passwordHash = "secret...";

json = user.toJSON();
/* {
    "id": 1,
    "fullName": "Alice Johnson",
    "email": "alice@example.com",
    "initials": "AJ"
} */
```

### 🔄 Recursive Class Handling

BoxLang automatically handles recursive class references:

```js
class Company {
    property name="id" type="numeric";
    property name="name" type="string";
    property name="employees" type="array";
}

class Employee {
    property name="id" type="numeric";
    property name="name" type="string";
    property name="company" type="Company";
}

company = new Company();
company.id = 1;
company.name = "Ortus Solutions";
company.employees = [];

employee = new Employee();
employee.id = 1;
employee.name = "Luis Majano";
employee.company = company;

company.employees.append( employee );

// Serializes without infinite recursion!
json = company.toJSON();
// Recursive references are handled gracefully
```

### 📋 Class Serialization Annotations Reference

\| Annotation | Scope | Purpose | Example | |------------|-------|---------|---------|------| | `@serializable` | Class/Property | Enable/disable serialization | `@serializable( false )` | | `@jsonExclude` | Class/Property | Exclude from JSON | `@jsonExclude( true )` | | `@jsonExclude` (list) | Class | Exclude multiple properties | `@jsonExclude( "password,secret" )` |

{% hint style="success" %}
**Best Practice**: Use property-level `@jsonExclude( true )` for individual fields and class-level `@jsonExclude( "field1,field2" )` with a comma-separated list for multiple fields. Implement custom `toJSON()` methods for complex transformation logic.
{% endhint %}

{% hint style="info" %}
**How It Works**: The `BoxClassSerializer` introspects the class's property definitions, filters out excluded properties, and serializes the `variables` scope values. Only properties defined with the `property` keyword are included in serialization.
{% endhint %}

## 📥 JSON Deserialization (jsonDeserialize / fromJSON)

Parse JSON strings back into BoxLang data structures using `jsonDeserialize()` or the `fromJSON()` member method.

### Basic Deserialization

```js
// Function syntax
json = '{"name":"Luis Majano","company":"Ortus Solutions","year":2006}';
person = jsonDeserialize( json );

// Member method syntax (preferred)
person = json.fromJSON();

// Access deserialized data
writeOutput( person.name );      // "Luis Majano"
writeOutput( person.company );   // "Ortus Solutions"
```

### Strict Mapping Mode

Control how JSON objects are mapped to BoxLang types:

```js
json = '{"name":"Alice","scores":[95,87,92]}';

// Strict mapping (default) - everything becomes structs
data = jsonDeserialize( json, strictMapping: true );
// { name: "Alice", scores: [95, 87, 92] }

// Non-strict mapping - may preserve Java types
data = jsonDeserialize( json, strictMapping: false );
```

### Supported JSON Types

BoxLang deserializes JSON to native types:

```js
// Primitives
jsonDeserialize( "42" );                    // 42 (numeric)
jsonDeserialize( "true" );                  // true (boolean)
jsonDeserialize( '"Hello"' );               // "Hello" (string)
jsonDeserialize( "null" );                  // null

// Arrays
jsonDeserialize( "[1,2,3]" );              // [1, 2, 3]
jsonDeserialize( '["a","b","c"]' );        // ["a", "b", "c"]

// Objects (become structs)
jsonDeserialize( '{"a":1,"b":2}' );        // { a: 1, b: 2 }

// Nested structures
json = '{
    "user": {
        "name": "Alice",
        "age": 30,
        "roles": ["admin", "developer"]
    }
}';
data = json.fromJSON();
writeOutput( data.user.name );              // "Alice"
writeOutput( data.user.roles[1] );          // "admin"
```

### Validation Before Deserialization

Always validate JSON before deserializing:

```js
function processJSON( string jsonData ) {
    if ( !isJSON( jsonData ) ) {
        throw( type="InvalidJSON", message="Invalid JSON provided" );
    }

    return jsonData.fromJSON();
}

// Safe deserialization
try {
    data = processJSON( userInput );
    // Process data...
} catch ( any e ) {
    writeOutput( "Error: #e.message#" );
}
```

## ✅ JSON Validation (isJSON)

Test if a string contains valid JSON:

```js
// Valid JSON
isJSON( '{"name":"Alice"}' );           // true
isJSON( '[1,2,3]' );                    // true
isJSON( '"Hello"' );                    // true
isJSON( 'true' );                       // true
isJSON( '42' );                         // true

// Invalid JSON
isJSON( '{name:"Alice"}' );             // false (unquoted key)
isJSON( "Hello" );                      // false (missing quotes)
isJSON( "" );                           // false (empty string)
isJSON( undefined );                    // false (not a string)

// Practical usage
if ( isJSON( apiResponse ) ) {
    data = apiResponse.fromJSON();
    processData( data );
} else {
    logError( "Invalid JSON response" );
}
```

## 📝 List to JSON Conversion

Convert delimited strings (lists) to JSON arrays:

```js
// Default comma delimiter
tags = "programming,boxlang,json,tutorial";
jsonArray = tags.listToJSON();
// ["programming","boxlang","json","tutorial"]

// Function syntax
categories = "tech,science,arts";
json = jsonSerialize( categories.listToArray() );

// Practical example: CSV to JSON
csvLine = "Alice,30,alice@example.com";
jsonData = csvLine.listToJSON();
// ["Alice","30","alice@example.com"]

// With custom delimiter
path = "home/user/documents/file.txt";
parts = path.listToArray( "/" ).toJSON();
// ["home","user","documents","file.txt"]
```

## 🎯 Advanced JSON Techniques

### Working with API Responses

```js
// Fetch and parse API response
http url="https://api.example.com/users" result="apiResult";

if ( isJSON( apiResult.fileContent ) ) {
    users = apiResult.fileContent.fromJSON();

    // Process users
    users.each( ( user ) => {
        println( "User: #user.name# (#user.email#)" );
    } );
} else {
    throw( "Invalid JSON response from API" );
}
```

### JSON Configuration Files

```js
// Load configuration from JSON file
configJson = fileRead( expandPath( "./config.json" ) );
config = configJson.fromJSON();

// Use configuration
datasource = config.database.datasource;
cacheTimeout = config.cache.timeout;

// Save updated configuration
config.features.newFeature = true;
fileWrite(
    expandPath( "./config.json" ),
    config.toJSON( pretty: true )
);
```

### Nested Data Transformation

```js
// Complex data structure
order = {
    orderId: 12345,
    customer: {
        id: 1,
        name: "Alice Johnson",
        email: "alice@example.com"
    },
    items: [
        { productId: 101, name: "Widget", quantity: 2, price: 29.99 },
        { productId: 102, name: "Gadget", quantity: 1, price: 49.99 }
    ],
    total: 109.97,
    orderDate: now()
};

// Serialize for API transmission
jsonPayload = order.toJSON();

// Send to API
http
    url="https://api.example.com/orders"
    method="POST"
    result="response" {
    httpParam type="header" name="Content-Type" value="application/json";
    httpParam type="body" value=jsonPayload;
}

// Parse response
if ( isJSON( response.fileContent ) ) {
    result = response.fileContent.fromJSON();
    orderId = result.id;
}
```

### JSON Stream Processing

```js
// Process large JSON arrays efficiently
jsonData = fileRead( "large-dataset.json" );
data = jsonData.fromJSON();

// Filter and transform
results = data
    .filter( ( item ) -> item.status == "active" )
    .map( ( item ) -> {
        return {
            id: item.id,
            name: item.name,
            processed: true
        };
    } );

// Save results
fileWrite( "results.json", results.toJSON( pretty: true ) );
```

## 🔧 Custom Serializers (Advanced)

BoxLang uses custom serializers for specific types. You can examine these in the BoxLang source:

* **`BoxClassSerializer`** - Handles class instances with property introspection
* **`BoxQuerySerializer`** - Handles query objects with format options
* **`BoxStructSerializer`** - Handles structs and maps
* **`BoxArraySerializer`** - Handles arrays and lists
* **`DynamicObjectSerializer`** - Handles Java object proxies
* **`ExceptionSerializer`** - Handles exception objects
* **`JavaArraySerializer`** - Handles native Java arrays

These serializers are automatically invoked when their respective types are encountered during JSON serialization.

## 📖 Function Reference

### jsonSerialize( data, \[queryFormat], \[useSecureJSONPrefix], \[useCustomSerializer], \[pretty] )

Convert BoxLang data to JSON string.

**Arguments:**

* `data` (any, required) - Data to serialize
* `queryFormat` (string) - Query format: `"struct"`, `"row"`, `"column"`, `"true"`, `"false"` (default: `"row"`)
* `useSecureJSONPrefix` (string/boolean) - Add secure prefix (not implemented)
* `useCustomSerializer` (boolean) - Use custom serializer (not implemented)
* `pretty` (boolean) - Pretty print with indentation (default: `false`)

**Returns:** String (JSON)

**Member Methods:**

* `data.toJSON()` - Available on most types
* `"list,items".listToJSON()` - Convert delimited string to JSON array

### jsonDeserialize( json, \[strictMapping], \[useCustomSerializer] )

Parse JSON string to BoxLang data.

**Arguments:**

* `json` (string, required) - JSON string to parse
* `strictMapping` (boolean) - Force all objects to structs (default: `true`)
* `useCustomSerializer` (string) - Custom serializer name (not implemented)

**Returns:** Any (native BoxLang types)

**Member Methods:**

* `jsonString.fromJSON()` - Parse JSON string

### isJSON( var )

Validate if string is valid JSON.

**Arguments:**

* `var` (any, required) - Value to test

**Returns:** Boolean

### jsonPrettify( var )

Format JSON string with indentation.

**Arguments:**

* `var` (string, required) - JSON string to format

**Returns:** String (formatted JSON)

**Member Methods:**

* `jsonString.jsonPrettify()` - Format JSON string

{% hint style="info" %}
JSON deserialization in BoxLang will always use ordered structs for objects which will preserve the key order of the original JSON string.  This is handy when reading a JSON file, modifying it, and writing it back out.
{% endhint %}

## 🎓 Best Practices

1. ✅ **Always quote struct keys** for exact casing in JSON output
2. ✅ **Use `isJSON()` validation** before deserializing user input
3. ✅ **Implement custom `toJSON()` methods** for complex class serialization logic
4. ✅ **Use `jsonExclude` annotations** to protect sensitive data (passwords, secrets)
5. ✅ **Prefer `pretty: true`** for configuration files and debugging
6. ✅ **Use `queryFormat="struct"`** for REST API responses (most compatible with JavaScript)
7. ✅ **Handle JSON errors gracefully** with try/catch blocks
8. ✅ **Validate API responses** with `isJSON()` before parsing
9. ✅ **Use member methods** (`toJSON()`, `fromJSON()`) for cleaner, more readable code
10. ✅ **Document serialization behavior** in class comments when using custom logic

## 🔗 Related Documentation

{% content-ref url="structures.md" %}
[structures.md](structures.md)
{% endcontent-ref %}

{% content-ref url="arrays.md" %}
[arrays.md](arrays.md)
{% endcontent-ref %}

{% content-ref url="queries.md" %}
[queries.md](queries.md)
{% endcontent-ref %}

{% content-ref url="classes/" %}
[classes](classes/)
{% endcontent-ref %}
