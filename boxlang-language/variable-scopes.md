---
description: They gotta exist somewhere!
icon: cube
---

# Variable Scopes

In the BoxLang language, many persistence and visibility scopes exist for variables to be placed in. These are differentiated by context: in a class, function, component, thread, script or template.  These scopes are Java maps but enhanced to provide case-insensitivity, member functions and more.  There are also different scopes that become alive depending on the execution of certain constructs, such as queries, threads, and http calls.

{% hint style="info" %}
All BoxLang scopes are implemented as BoxLang [structures](structures.md), basically case-insensitive maps behind the scenes.
{% endhint %}

## 📋 Table of Contents

- [Local Scope](#local-scope)
- [Variables Scope](#variables-scope)
- [This Scope](#this-scope)
- [Arguments Scope](#arguments-scope)
- [Application Scope](#application-scope)
- [Session Scope](#session-scope)
- [Request Scope](#request-scope)
- [Server Scope](#server-scope)
- [CGI Scope](#cgi-scope)
- [Form Scope](#form-scope)
- [URL Scope](#url-scope)
- [Thread Scopes](#thread-scopes)
- [Scope Searching](#scope-searching)
- [Best Practices](#best-practices)

When you declare variables in templates, classes, or functions, they’re stored within a structured scope. This design makes your code highly flexible, allowing you to fluently interact with the entire scope through a wide range of BIFs. You can even bind these variables directly to function calls, attributes, and more—highlighting the dynamic power at the core of BoxLang.

```javascript
// Examples

/**
 * Get the state representation of the scheduler task
 */
function getMemento(){
	// I can do a filter on an entire scope
	return variables.filter( ( key, value ) => {
		return isCustomFunction( value ) || listFindNoCase( "this", key ) ? false : true;
	} );
}


// Argument binding
results = matchClassRules( argumentCollection = arguments );
results = matchClassRules( argumentCollection = myMap );

// I can dump entire scopes
writedump( variables )
```

The only language keyword that can be used to tell the variable to store in a function's local scope is called `var`.  However, you can also just use the `local`scope directly or none at all. However, we do recommend being explicit on some occasions to avoid ambiguity.

{% hint style="warning" %}
It's a good idea to scope variables to avoid scope lookups, which could in turn create issues or even leaks.
{% endhint %}

```javascript
function getData(){
	// Placed in the function's local scope
	var data = "luis"
	// Also placed in the function's local scope
	data = "luis"
	// Also placed in the function's local scope
	local.data = "luis"
}
```

## 📄 Template/Scripts (`bxm,bxs`)

All scripts and templates have the following scopes available to them.  Please note that the `variables`scope can also be implicit.  You don't have to declare it.

* `variables` - The default or implicit scope to which all variables are assigned.

```javascript
a = "hello"
writeOutput( a )

// Is the same as
variables.a = "hello"
writeOutput( variables.a )
```

## ⚡Templates/Scripts Function Scopes

All user-defined functions declared in templates or scripts will have the following scopes available:

* `variables` - Has access to private variables within a Class or Page
* `local` - Function-scoped variables only exist within the function execution. Referred to as `var` scoping. The default assignment scope in a function.
* `arguments` - Incoming variables to a function

```javascript
function sayHello( required name ){
    var fullName = "Hello #arguments.name#"
    // case insensitive
    return FULLNAME
}

writeOutput( sayHello( "luis" ) )
```

## 🗳️ Classes (`bx`)

All classes in BoxLang follow Object-oriented patterns and have the following scopes available.  Another critical aspect of classes is that all declared functions will be placed in a visibility scope.

* `variables` - Private scope, visible internally to the class only
* `this` - Public scope, visible from the outside world and a self-reference internally
* `static` - Store variables in the classes blueprint and not the instance
* `super`- Only available if you use inheritance

```java
class extends="MyParent"{

    static {
        className = "MyClass"
    }

    variables.created = now()
    this.PUBLIC = "Hola"

    function init(){
        super.init()
    }

    function main(){
        println( "hello #static.className#" )
    }

}
```

### Function Scopes

Depending on a function’s visibility, BoxLang automatically places a reference (or pointer) to that function in different scopes, within the class ensuring that it can be discovered and invoked appropriately. Why does it do this? Because BoxLang is a dynamic language by design.

In practice, this means that functions in BoxLang are not locked down at compile time. Instead, they remain fully malleable at runtime—you can add new functions, remove existing ones, or even modify their behavior on the fly. This flexibility allows developers to build more adaptive and expressive applications, where behaviors can evolve based on context, configuration, or user interaction.

By managing function pointers across scopes, BoxLang ensures that these runtime changes are immediately reflected wherever the function is expected to live. Whether it’s within a local scope, a component, or a broader application context, the dynamic nature of BoxLang makes it possible to treat functions as living members of your application rather than static, unchangeable artifacts.

* `Private` Function
  * `variables`
* `Public or Remote` Functions
  * `variables`
  * `this`

```java
// Try it out
class {

    function main(){
        writedump( var: this, label: "public" );
        writedump( var: variables, label: "private" );
    }

    private function test(){}
    public function hello(){}

}
```

## ⚡Closures

All closures in BoxLang are context-aware, which means they carry with them knowledge of the environment in which they were created. In other words, a closure isn’t just a function—it’s a function plus the scope it was born in. This allows closures to maintain access to variables, functions, and references that existed at the time they were defined, even if they are later executed in a completely different context.

For example, if you define a closure inside a function, it will continue to “remember” the local variables of that function, making it a powerful tool for encapsulating state and creating reusable logic without polluting the global or class-level scopes.

When closures are defined inside classes, they become even more useful. In this case, closures automatically capture the class’s `variables` scope (the private, per-instance data) as well as the `this` scope (the public interface of the instance). This means closures have seamless access to both the internal state of the class and its public methods, enabling elegant encapsulation of behavior that can directly interact with the object’s data.

This context-awareness is what makes closures in BoxLang so flexible. They’re not isolated pieces of code; they are “living” functions that carry their birthplace with them. This ensures that wherever you pass them—whether into a higher-order function, as an event handler, or across asynchronous execution—they still know exactly where they came from and what they can interact with.

* `variables` - Has access to private variables from where they were created (Classes, scripts or templates)
* `this` - Has access to public variables from where they were created (Classes)
* `local` - Function-scoped variables only exist within the function execution. Referred to as `var` scoping. The default assignment scope in a function.
* `arguments` - Incoming variables to a function

```javascript
variables.CONSTANT = 1.4

// Define a closure that returns another function
function makeMultiplier( factor ) {
    return ( number ) => number * factor * variables.CONSTANT;
}

// Create multiplier functions using closures
double = makeMultiplier( 2 )
triple = makeMultiplier( 3 )

// Call the closure functions
println( double( 5 ) )  // Output: 10
println( triple( 5 ) )  // Output: 15

// Closures can also capture outer variables
function counter() {
    var count = 0;
    return () => {
        count++
        return count
    };
}

increment = counter()
println( increment() )  // Output: 1
println( increment() )  // Output: 2
println( increment() )  // Output: 3

```

## 🪶 Lambdas

Lambdas in BoxLang are designed to be pure functions. Unlike closures, they do not capture or carry along the scope in which they were defined. In other words, lambdas don’t “remember” their birthplace or have access to surrounding variables. They exist independently of the context in which they were created.

This distinction has two major implications:

1.	**Simplicity** – Because lambdas are context-free, they are lightweight and predictable. They only operate on the `arguments` explicitly passed to them and any values they define internally. You don’t have to worry about hidden dependencies or external scope leaks. This makes them ideal for short, focused operations like transformations, mappings, or small inline computations.
2.	**Performance** – Without the overhead of capturing surrounding scopes, lambdas are faster to create and execute compared to closures. They don’t need to carry around extra baggage such as references to variables, this, or parent function contexts. This efficiency makes them an excellent choice in performance-sensitive scenarios, especially when used in large iterations, functional pipelines, or hot paths in your application.

In essence, lambdas in BoxLang provide a lean, functional style of programming: self-contained, efficient, and free of side effects. They shine when you need a quick function without any ties to the broader context—perfect for concise logic that should remain pure and context-independent.

* `local` - Function-scoped variables only exist within the function execution. Referred to as `var` scoping. The default assignment scope in a function.
* `arguments` - Incoming variables to a function

```javascript
// Define a simple lambda that squares a number
square = (x) -> x * x

println( square( 4 ) ) // Output: 16
println( square( 5 ) ) // Output: 25

// Lambda that adds two numbers
add = (a, b) -> a + b

println( add( 10, 20 ) ) // Output: 30

// Using a lambda to filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = numbers.filter( (n) -> n % 2 == 0 )

println( evens ) // Output: [2, 4, 6]


// Sorting a list in descending order
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort( (a, b) -> b - a )

println( numbers ) // Output: [9, 5, 4, 3, 1, 1]

```

The following will throw an exception as it will try to reach outside of itself:

```javascript
function testLambdaScope() {
    localVar = "I am local"

    // This lambda will fail because it tries to access localVar
    brokenLambda = () -> localVar

    println( brokenLambda() ) // This will cause an error
}

testLambdaScope()

```

## 🏷️ Components

In BoxLang, you’re not limited to the built-in components—you can extend the language itself by creating your own custom components. These components can be invoked seamlessly in both script syntax and templating syntax, giving developers a consistent way to encapsulate and reuse functionality across different coding styles.

Custom components are powerful because they allow you to wrap up behavior into a self-contained unit that can handle input, manage its own internal state, and even communicate back to the calling template. This makes them excellent for building reusable UI constructs, workflow blocks, or domain-specific abstractions.  They also do not affect the parser, but rather are invoked at runtime.  This means, that you can create predictable, reusable components without worrying about breaking the syntax of your BoxLang code.

Every custom/core component automatically has access to a set of special scopes that give it flexibility and power:

•	**attributes** – Holds the incoming arguments or attributes passed into the component. This is how you provide input to customize the component’s behavior.
•	**variables** – Acts as the default scope for variable assignments inside the component, ensuring that the component has its own sandboxed data environment.
•	**caller** – Provides a way for the component to interact with the template that invoked it, allowing you to set or read variables from the caller’s context. This enables two-way communication between the component and the outside world.

### Example Usage

You can call a component using **script syntax,** where it looks and feels like a function call with a block of content:

```js
// Call a component using script
bx:component template="path/MyComponent.bxm" name="luis"{
    // Content here or more component calls or whatever
}
```

Or you can invoke it using **templating syntax**, which is closer to traditional custom tags:

```xml
<!-- Templating syntax: call a component -->
<bx:component template="path/MyComponent.bxm" name="luis">
    Inner content, text, or other nested components
</bx:component>
```

{% hint style="warning" %}
We highly discourage peeking out of your component using the `caller`scope, but it can sometimes be beneficial.  Use with caution.
{% endhint %}

## 🧵 Thread

When you create threads with the `thread`component, you will have these scopes available to you:

* `attributes` - Passed variables via a thread
* `thread` - A thread-specific scope that can be used for storage and retrieval.  Only the owning thread can write to this scope.  All other threads and the main thread can read the variables.
* `local` - Variables local to the thread context
* `variables` - The surrounding declared template or class `variables`scope
* `this`- The surrounding declared class scope

```javascript
bx:thread
    name="exampleThread"
    message="Hello from the thread!"
{

    // You can use var, local or none
    var incomingMessage = attributes.message

    // Defining local variables inside the thread
    local.threadLocalVar = "This is a local thread variable"
    threadLocalVar2 = "Another local var"

    // Setting variables in the thread scope (can be accessed after completion)
    // Only this thread can write to it.
    thread.finalMessage = "Thread has completed execution!"
    thread.calculationResult = 42

    println( "Thread is running..." )
    println( "Incoming Message: " & incomingMessage )
    println( "Local Variable in Thread: " & threadLocalVar )
}

// Wait for the thread to finish before accessing thread scope variables
threadJoin( "exampleThread" )

// Accessing thread scope variables after execution
println( "Thread Final Message: " & bxthread.exampleThread.finalMessage )
println( "Thread Calculation Result: " & exampleThread.calculationResult )

```

### 🧵 bxThread

The `bxThread` scope is a special BoxLang scope that provides access to thread metadata and variables from anywhere in your request. It contains a key for every thread that has been executed in the current request, making it easy to access thread data from outside the thread context.

* `bxThread` - Global scope containing all threads executed in the current request
* Each thread key contains metadata and variables set from within that thread

```javascript
// Creating multiple threads
bx:thread name="dataProcessor" id="123" {
    thread.processedData = "Data processed for ID: #attributes.id#"
    thread.timestamp = now()
}

bx:thread name="emailSender" recipient="user@example.com" {
    thread.emailSent = true
    thread.recipient = attributes.recipient
    thread.sentAt = now()
}

// Wait for threads to complete
threadJoin( "dataProcessor,emailSender" )

// Access thread data from anywhere using bxThread scope
println( "Data Processor Result: " & bxThread.dataProcessor.processedData )
println( "Email Status: " & bxThread.emailSender.emailSent )
println( "Email Recipient: " & bxThread.emailSender.recipient )

// You can also iterate over all threads in the current request
for( threadName in bxThread ) {
    println( "Thread: #threadName# completed at #bxThread[threadName].timestamp#" )
}
```

## 🌐 Runtime Scopes

BoxLang runs in different runtime contexts, and the available scopes depend on which runtime you're using. Understanding these differences is crucial for building portable applications.

### 🖥️ Core OS

When running BoxLang in CLI mode or core OS runtime, you have access to these scopes:

* `variables` - Default scope for variable assignments
* `local` - Function-scoped variables
* `arguments` - Function arguments
* `application` - Application-wide persistence (requires Application.bx)
* `session` - Session persistence (requires Application.bx)
* `request` - Request-scoped variables
* `server` - Server-wide persistence across all applications
* `thread` - Thread-specific variables
* `bxThread` - Global thread metadata scope

```javascript
// CLI Example - Only core scopes available
server.appName = "My CLI App"
request.startTime = now()
application.version = "1.0.0" // Requires Application.bx

println( "Running in CLI mode with core scopes only" )
```

### 🕸️ Web Runtimes

When running in web runtimes (Servlet, MiniServer, Lambda, Desktop), you get additional web-specific scopes:

**All Core Scopes PLUS:**

* `url` - HTTP GET parameters from the URL
* `form` - HTTP POST form data
* `cgi` - Server and request environment variables
* `cookie` - Browser cookies
* `bxFile` - File upload information (during file uploads)
* `bxHttp` - HTTP request/response data (during HTTP operations)

```javascript
// Web Example - Full scope access
url.debug = "true"  // From: myapp.com?debug=true
form.username = "john.doe"  // From POST form
cookie.preferences = "dark-mode"  // Browser cookie
cgi.remote_addr = "192.168.1.1"  // Client IP address

println( "Running in web mode with full scope access" )
println( "Client IP: #cgi.remote_addr#" )
println( "Debug Mode: #url.debug#" )
```

{% hint style="info" %}
**Runtime Detection**: You can check your runtime context using `server.boxlang.runtime.name` to conditionally access web scopes.
{% endhint %}

## 🔍 Unscoped Variables

If you use a variable name **without** a scope prefix, BoxLang checks the scopes in the following order to find the variable (When we say `function` it includes closures, UDFs and lambdas):

1. Local (Functions only)
2. Arguments (Functions only)
3. Attributes (Components only)
4. Thread local (inside threads only)
5. Query (variables in active query loops)
6. Thread
7. Variables

If the runtime is web-based, it will also check these scopes last:

8. CGI
9.  URL
10. Form
11. Cookie

{% hint style="danger" %}
**IMPORTANT**: Because BoxLang must search for variables when you do not specify the scope, you can improve performance by specifying the scope for all variables. It can also help you avoid nasty lookups or unexpected results.
{% endhint %}

## 🔍 Query Loop Scope

When you iterate over a query using `bx:loop` or functional methods like `queryEach()`, BoxLang automatically registers the query with the current context and makes the column names available as unscoped variables for the duration of each iteration.

```javascript
// Create a query
myQuery = queryNew( "id,name,email", "integer,varchar,varchar", [
    [ 1, "Luis", "luis@example.com" ],
    [ 2, "Brad", "brad@example.com" ],
    [ 3, "Jon", "jon@example.com" ]
] )

// Loop over query - column names become available as variables
bx:loop query="myQuery" {
    // Unscoped column references automatically resolve to current row
    println( "ID: #id#" )        // Accesses myQuery.id for current row
    println( "Name: #name#" )    // Accesses myQuery.name for current row
    println( "Email: #email#" )  // Accesses myQuery.email for current row

    // You can also use explicit query syntax
    println( "ID: #myQuery.id[queryCurrentRow(myQuery)]#" )

    // Or access via the query scope
    println( "Current row: #queryCurrentRow(myQuery)#" )
}

// Script syntax for query loops
for( row in myQuery ) {
    println( "Name: #name#" )  // Column names available as variables
}
```

### Query Loop Variables

During query iteration, these special variables and functions are available:

| Variable/Function | Description |
|-------------------|-------------|
| **Column Names** | All query column names are available as unscoped variables containing the current row's value |
| `queryCurrentRow(query)` | Returns the current row number (1-based) |
| `currentRow` | Alias for current row number (when using member function syntax) |
| `columnArray` | Array of column names in the query |
| `columnList` | Comma-separated list of column names |
| `recordCount` | Total number of rows in the query |

### Query Loop Behavior

```javascript
employees = queryNew( "id,firstName,lastName,salary", "integer,varchar,varchar,numeric", [
    [ 1, "John", "Doe", 50000 ],
    [ 2, "Jane", "Smith", 75000 ],
    [ 3, "Bob", "Johnson", 60000 ]
] )

// Using column names directly
bx:loop query="employees" {
    fullName = "#firstName# #lastName#"

    // Check current row
    if( queryCurrentRow(employees) == 2 ) {
        println( "Middle employee: #fullName#" )
    }

    // Access query metadata
    println( "Row #queryCurrentRow(employees)# of #recordCount#" )
}

// Grouped query loops
sales = queryNew( "region,product,amount", "varchar,varchar,numeric", [
    [ "North", "Widget", 100 ],
    [ "North", "Gadget", 200 ],
    [ "South", "Widget", 150 ],
    [ "South", "Gadget", 250 ]
] )

bx:loop query="sales" group="region" {
    println( "Region: #region#" )

    bx:loop query="sales" group="product" {
        println( "  Product: #product# - Amount: #amount#" )
    }
}
```

### Member Function Syntax

```javascript
myQuery = queryNew( "id,name", "integer,varchar", [
    [ 1, "Alice" ],
    [ 2, "Bob" ]
] )

// Using member functions
myQuery.each( ( row, index ) => {
    println( "Row #index#: #row.name#" )
} )

// Map over query
names = myQuery.map( ( row ) => row.name )
```

{% hint style="info" %}
**Performance Tip**: When accessing query columns in loops, unscoped column names are resolved through the query loop scope, which is efficient. However, if you need to access variables from outer scopes, be explicit with your scoping to avoid ambiguity.
{% endhint %}

<a href="https://try.boxlang.io" target="_blank">Try query loops on try.boxlang.io</a>

## ⚠️ Catch Scope

When an exception is caught in a `try/catch` block, BoxLang creates a special `catch` context that makes the exception variable available. The exception variable contains detailed information about the error.

```javascript
try {
    // Code that might throw an error
    result = 10 / 0
} catch( any e ) {
    // 'e' is the exception variable - available as an unscoped variable
    println( "Error: #e.message#" )
    println( "Type: #e.type#" )
    println( "Detail: #e.detail#" )

    // You can also reference it explicitly
    println( "Stack trace: #e.stackTrace#" )
}
```

### Exception Variable Structure

The exception variable (commonly named `e`, `ex`, or `error`) is a struct containing:

| Property | Description |
|----------|-------------|
| `message` | The error message |
| `type` | The exception type (e.g., "Application", "Database", "Expression") |
| `detail` | Detailed error information |
| `stackTrace` | Full stack trace as a string |
| `tagContext` | Array of stack frames with file/line information |
| `cause` | The underlying Java exception (if applicable) |
| `errorCode` | Error code (if applicable) |
| `extendedInfo` | Additional error information (if applicable) |

### Catch Scope Behavior

```javascript
function divide( a, b ) {
    try {
        return a / b
    } catch( any e ) {
        // Exception variable available in catch block
        println( "Division error: #e.message#" )
        println( "Error occurred at: #e.tagContext[1].template#:#e.tagContext[1].line#" )

        // Rethrow with additional context
        throw( type="CustomError", message="Division failed", cause=e )
    }
}

// Multiple catch blocks with typed exceptions
try {
    // Some database operation
    query = queryExecute( "SELECT * FROM users WHERE id = ?", [ invalidId ] )
} catch( database e ) {
    // Handle database-specific errors
    println( "Database error: #e.message#" )
    println( "SQL State: #e.sqlState#" )
} catch( any e ) {
    // Handle all other errors
    println( "General error: #e.message#" )
}

// Nested try/catch blocks
try {
    try {
        // Inner operation
        throw( type="inner", message="Inner error" )
    } catch( e ) {
        // 'e' refers to inner exception
        println( "Caught inner: #e.message#" )

        // Wrap and rethrow
        throw( type="outer", message="Outer error", object=e )
    }
} catch( outer e ) {
    // 'e' refers to outer exception
    println( "Caught outer: #e.message#" )
    println( "Original cause: #e.cause.message#" )
}
```

### CFML Compatibility

In CFML compatibility mode (using the `bx-compat-cfml` module), the exception variable is also available as `cfcatch`:

```javascript
try {
    // Some operation
} catch( any e ) {
    // Both 'e' and 'cfcatch' reference the same exception
    println( e.message )        // BoxLang syntax
    println( cfcatch.message )  // CFML compat syntax
}
```

### Rethrowing Exceptions

Within a catch block, you can use the `rethrow` statement to re-throw the current exception:

```javascript
try {
    // Risky operation
    processData()
} catch( any e ) {
    // Log the error
    logger.error( "Error processing data: #e.message#" )

    // Clean up resources
    cleanup()

    // Rethrow the original exception
    rethrow
}
```

{% hint style="warning" %}
**Scope Visibility**: The exception variable is only available within the `catch` block. Once execution exits the catch block, the variable is no longer in scope.
{% endhint %}

<a href="https://try.boxlang.io" target="_blank">Try exception handling on try.boxlang.io</a>

## 🔒 Final Variables

BoxLang supports the `final` modifier for variables in any scope, which prevents the variable from being reassigned after its initial assignment. This is useful for creating constants and preventing accidental modifications.

```javascript
// Class scope with final variables
class {
    final variables.API_VERSION = "1.0"
    final this.MAX_RETRIES = 3
    final static.COMPANY_NAME = "Ortus Solutions"

    function init() {
        final local.instanceId = createUUID()

        // This would throw an error:
        // API_VERSION = "2.0"  // Cannot reassign final variable

        return this
    }
}

// Function scope with final variables
function processData( required data ) {
    final var startTime = now()
    final local.processId = createUUID()

    // Process data here...

    // These would throw errors:
    // startTime = now()  // Cannot reassign final variable
    // processId = "new-id"  // Cannot reassign final variable

    return {
        "processId" : processId,
        "duration" : dateDiff( "s", startTime, now() )
    }
}

// Persistence scopes with final variables
final application.appVersion = "1.0.0"
final session.userType = "premium"
final request.requestId = createUUID()
```

{% hint style="warning" %}
**Important**: Final variables must be assigned a value when declared. Attempting to reassign a final variable will result in a runtime error.
{% endhint %}

## 💾 Persistence Scopes

Can be used in any context, used for persisting variables for a period of time.

* `session` - stored in server RAM or external storages tracked by unique web visitor
* `application` - stored in server RAM or external storage tracked by the running BoxLang application
* `cookie` - stored in a visitor's browser
* `server` - stored in server RAM for ANY application for that BoxLang instance
* `request` - stored in RAM for a specific user request ONLY
* `cgi` - read only scope provided by the servlet container and BoxLang
* `form` - Variables submitted via HTTP posts
* `URL` - Variables incoming via HTTP GET operations or the incoming URL

### Practical Persistence Examples

```javascript
// 🔧 Server Scope - Cross-application persistence
server.startupTime = now()
server.totalRequests = ( server.totalRequests ?: 0 ) + 1
server.sharedCache = {}

// 📱 Application Scope - Application-wide data
application.version = "2.1.0"
application.userCount = 0
application.settings = {
    "debugMode" : false,
    "maxUsers" : 1000
}

// 👤 Session Scope - User-specific data (Web only)
session.userId = "user123"
session.preferences = {
    "theme" : "dark",
    "language" : "en"
}
session.shoppingCart = []

// 🍪 Cookie Scope - Browser-stored data (Web only)
cookie.lastVisit = now()
cookie.userPrefs = "theme=dark;lang=en"
// Set cookie with options
bx:cookie name="sessionToken" value="abc123" expires="30" secure="true"

// 📨 Request Scope - Single request data
request.startTime = now()
request.userAgent = cgi.http_user_agent
request.processingSteps = []

// 📊 CGI Scope - Read-only server/request info (Web only)
println( "Client IP: #cgi.remote_addr#" )
println( "Request Method: #cgi.request_method#" )
println( "User Agent: #cgi.http_user_agent#" )
println( "Server Name: #cgi.server_name#" )

// 📝 Form Scope - POST data (Web only)
if( structKeyExists( form, "username" ) ) {
    println( "Username submitted: #form.username#" )
    println( "Email: #form.email#" )
}

// 🔗 URL Scope - GET parameters (Web only)
if( structKeyExists( url, "action" ) ) {
    switch( url.action ) {
        case "login":
            // Handle login
            break
        case "logout":
            // Handle logout
            break
    }
}
```

### Scope Interaction Examples

```javascript
// Copy data between scopes
session.userPreferences = duplicate( form )

// Merge scopes
request.allData = {}
structAppend( request.allData, url )
structAppend( request.allData, form )
```

### Scope Debugging & Performance

```javascript
// Debugging scopes - dump entire scopes
writeDump( var=variables, label="Variables Scope" )
writeDump( var=session, label="Session Data", top=10 )
writeDump( var=application, label="App Settings" )

// Check scope contents
if( structIsEmpty( session ) ) {
    println( "No session data found" )
}

// Performance - scope size monitoring
function getScopeInfo() {
    return {
        "variablesCount" : structCount( variables ),
        "sessionSize" : structCount( session ),
        "applicationKeys" : structKeyArray( application ),
        "requestMemory" : structCount( request )
    }
}

// Scope iteration for debugging
for( key in variables ) {
    if( isCustomFunction( variables[key] ) ) {
        println( "Function found: #key#" )
    }
}

// Performance best practices
function efficientScopeUsage() {
    // ✅ Good - explicit scoping
    local.result = variables.data.process()

    // ❌ Bad - unscoped variable (scope hunting)
    result = data.process()  // BoxLang must search scopes

    // ✅ Good - cache scope references
    local.mySession = session
    local.mySession.lastAction = now()
    local.mySession.pageViews++

    // ❌ Bad - repeated scope access
    session.lastAction = now()
    session.pageViews++
}
```

{% hint style="info" %}
**Performance Tip**: Always scope your variables explicitly. Unscoped variables trigger scope hunting, which impacts performance, especially in complex applications.
{% endhint %}

## 🖥️ Server Scope

The `server` scope is a global scope that lives for the entire lifetime of the BoxLang runtime instance. It contains system information, BoxLang runtime details, and can store custom variables that need to persist across all applications and requests.  It contains the following sub-scopes:

* `boxlang` - BoxLang runtime information
* `cli` - Command line execution details
* `java` - Java runtime information
* `os` - Operating system information
* `separator` - File system separators
* `system` - System properties and environment

### 🏗️ Server Scope Structure

The server scope is automatically populated with several unmodifiable sub-structures:

#### 🎯 BoxLang Information (`server.boxlang`)

| Key | Type | Description |
|-----|------|-------------|
| `buildDate` | string | Build date of the BoxLang runtime |
| `boxlangId` | string | Unique identifier for this BoxLang instance |
| `codename` | string | Release codename for this version |
| `cliMode` | boolean | Whether running in CLI mode |
| `debugMode` | boolean | Whether debug mode is enabled |
| `jarMode` | boolean | Whether running from JAR file |
| `modules` | struct | Information about loaded modules |
| `runtimeHome` | string | Path to BoxLang runtime directory |
| `version` | string | BoxLang version number |

```javascript
// BoxLang runtime information
println( "BoxLang Version: #server.boxlang.version#" )
println( "Codename: #server.boxlang.codename#" )
println( "Build Date: #server.boxlang.buildDate#" )
println( "Runtime Home: #server.boxlang.runtimeHome#" )
println( "CLI Mode: #server.boxlang.cliMode#" )
println( "Debug Mode: #server.boxlang.debugMode#" )
println( "JAR Mode: #server.boxlang.jarMode#" )

// Access loaded modules
writeDump( server.boxlang.modules )
```

#### 🏢 Operating System Information (`server.os`)

| Key | Type | Description |
|-----|------|-------------|
| `additionalinformation` | string | Additional OS information |
| `arch` | string | System architecture (x86, x64, etc.) |
| `archModel` | string | Architecture model |
| `hostname` | string | Local machine hostname |
| `ipAddress` | string | Local machine IP address |
| `macAddress` | string | Local machine MAC address |
| `name` | string | Operating system name |
| `version` | string | Operating system version |

```javascript
// Operating system details
println( "OS Name: #server.os.name#" )
println( "OS Version: #server.os.version#" )
println( "Architecture: #server.os.arch#" )
println( "Hostname: #server.os.hostname#" )
println( "IP Address: #server.os.ipAddress#" )
println( "MAC Address: #server.os.macAddress#" )
```

#### ☕ Java Runtime Information (`server.java`)

| Key | Type | Description |
|-----|------|-------------|
| `archModel` | string | Architecture model |
| `availableLocales` | array | List of available locales |
| `defaultLocale` | string | Default system locale |
| `executionPath` | string | Java execution path |
| `freeMemory` | numeric | Available free memory in bytes |
| `maxMemory` | numeric | Maximum memory available in bytes |
| `totalMemory` | numeric | Total memory allocated in bytes |
| `vendor` | string | Java vendor name |
| `version` | string | Java version number |

```javascript
// Java environment details
println( "Java Version: #server.java.version#" )
println( "Java Vendor: #server.java.vendor#" )
println( "Available Memory: #server.java.freeMemory# bytes" )
println( "Max Memory: #server.java.maxMemory# bytes" )
println( "Total Memory: #server.java.totalMemory# bytes" )
println( "Default Locale: #server.java.defaultLocale#" )

// Available locales
for( locale in server.java.availableLocales ) {
    println( "Locale: #locale#" )
}
```

#### 📁 File System Separators (`server.separator`)

| Key | Type | Description |
|-----|------|-------------|
| `file` | string | File separator character (/ or \\) |
| `line` | string | Line separator character(s) |
| `path` | string | Path separator character (; or :) |

```javascript
// File system separators
println( "Path Separator: #server.separator.path#" )
println( "File Separator: #server.separator.file#" )
println( "Line Separator: #server.separator.line#" )
```

#### 💻 CLI Information (`server.cli`)

| Key | Type | Description |
|-----|------|-------------|
| `args` | array | Original command line arguments |
| `command` | string | Full command line used to start BoxLang |
| `executionPath` | string | Directory from which CLI was executed |
| `parsed` | struct | Parsed command line arguments |

```javascript
// CLI execution details (only available in CLI mode)
if( server.boxlang.cliMode ) {
    println( "Execution Path: #server.cli.executionPath#" )
    println( "Command: #server.cli.command#" )
    writeDump( server.cli.args )
    writeDump( server.cli.parsed )
}
```

#### ⚙️ System Properties and Environment (`server.system`)

| Key | Type | Description |
|-----|------|-------------|
| `environment` | struct | System environment variables (if security allows) |
| `properties` | struct | Java system properties (if security allows) |

{% hint style="warning" %}
**Security Note**: The `server.system` scope content depends on the `populateServerSystemScope` security setting. When disabled, both `environment` and `properties` will be empty structs.
{% endhint %}

```javascript
// System environment and properties (if security allows)
// Check security setting: populateServerSystemScope
if( !structIsEmpty( server.system.environment ) ) {
    println( "Environment Variables Available" )
    println( "PATH: #server.system.environment.PATH#" )
}

if( !structIsEmpty( server.system.properties ) ) {
    println( "System Properties Available" )
    println( "Java Home: #server.system.properties['java.home']#" )
}
```

### 🔧 Custom Server Variables

You can store your own variables in the server scope for cross-application persistence:

```javascript
// Store custom server-wide data
server.appStartTime = now()
server.requestCounter = 0
server.globalSettings = {
    "maintenance" : false,
    "debugEnabled" : true
}

// Increment request counter
server.requestCounter++

// Check maintenance mode across applications
if( server.globalSettings.maintenance ) {
    abort "System is under maintenance"
}
```

### 🔒 Unmodifiable Keys

The following keys cannot be modified once the server scope is initialized:

* `boxlang` - BoxLang runtime information
* `os` - Operating system information
* `java` - Java runtime information
* `separator` - File system separators
* `system` - System properties and environment

```javascript
// These will throw errors after initialization:
// server.boxlang = "modified"  // ❌ Cannot modify
// server.os.name = "custom"    // ❌ Cannot modify

// But this is allowed:
server.customData = "allowed"  // ✅ Custom keys are allowed
```

## 🌐 CGI Scope

The `CGI` scope is a read-only scope available only in web runtimes that contains HTTP request information and server environment variables. It provides access to web server and request details following the Common Gateway Interface standard.

### 📡 Request Information

```javascript
// Basic request details
println( "Request Method: #cgi.request_method#" )     // GET, POST, PUT, etc.
println( "Request URL: #cgi.request_url#" )           // Full request URL
println( "Script Name: #cgi.script_name#" )           // Request URI
println( "Query String: #cgi.query_string#" )         // URL parameters
println( "Path Info: #cgi.path_info#" )               // Additional path info

// Content information
println( "Content Type: #cgi.content_type#" )         // Request content type
println( "Content Length: #cgi.content_length#" )     // Request body size
```

### 🖥️ Server Information

```javascript
// Server details
println( "Server Name: #cgi.server_name#" )           // Server hostname
println( "Server Port: #cgi.server_port#" )           // Server port
println( "Server Protocol: #cgi.server_protocol#" )   // HTTP/1.1, HTTP/2, etc.
println( "Server Port Secure: #cgi.server_port_secure#" ) // Secure port if HTTPS

// Local server information
println( "Local Address: #cgi.local_addr#" )          // Server IP address
println( "Local Host: #cgi.local_host#" )             // Server hostname
```

### 👤 Client Information

```javascript
// Client/remote details
println( "Remote Address: #cgi.remote_addr#" )        // Client IP address
println( "Remote Host: #cgi.remote_host#" )           // Client hostname
println( "Remote User: #cgi.remote_user#" )           // Authenticated user

// Request security
println( "HTTPS: #cgi.https#" )                       // Boolean - is secure
println( "HTTP Host: #cgi.http_host#" )               // Host header with port
```

### 📂 File Path Information

```javascript
// Template and path information
println( "Template Path: #cgi.cf_template_path#" )    // Absolute template path
println( "BX Template Path: #cgi.bx_template_path#" ) // BoxLang template path
println( "Path Translated: #cgi.path_translated#" )   // Physical path
```

### 🌐 HTTP Headers

The CGI scope automatically provides access to all HTTP headers using the `http_` prefix:

```javascript
// Common HTTP headers
println( "User Agent: #cgi.http_user_agent#" )        // Browser/client info
println( "Accept: #cgi.http_accept#" )                 // Accepted content types
println( "Accept Language: #cgi.http_accept_language#" ) // Language preferences
println( "Accept Encoding: #cgi.http_accept_encoding#" ) // Compression support
println( "Connection: #cgi.http_connection#" )         // Connection type
println( "Referer: #cgi.http_referer#" )              // Referring page
println( "Cookie: #cgi.http_cookie#" )                // Cookie header

// Custom headers are also accessible
println( "Authorization: #cgi.http_authorization#" )   // Auth header
println( "X-Forwarded-For: #cgi.http_x_forwarded_for#" ) // Proxy headers
```

### 🔍 CGI Scope Behavior

```javascript
// CGI scope never throws errors - returns empty string for missing keys
println( "Non-existent key: '#cgi.nonexistent#'" )    // Returns: ""

// Check if keys exist
if( len( cgi.http_user_agent ) ) {
    println( "User agent is available" )
}

// Iterate over all CGI variables
for( key in cgi ) {
    println( "#key#: #cgi[key]#" )
}

// Dump all CGI information
writeDump( var=cgi, label="CGI Scope" )
```

### 🔐 Security and SSL Information

```javascript
// SSL/TLS certificate information (when available)
println( "Auth Type: #cgi.auth_type#" )               // Authentication method
println( "Auth User: #cgi.auth_user#" )               // Authenticated username
println( "Cert Issuer: #cgi.cert_issuer#" )           // Certificate issuer
println( "Cert Subject: #cgi.cert_subject#" )         // Certificate subject
println( "Cert Key Size: #cgi.cert_keysize#" )        // Certificate key size

// HTTPS specific information
if( cgi.https == "on" ) {
    println( "HTTPS Key Size: #cgi.https_keysize#" )
    println( "HTTPS Secret Key Size: #cgi.https_secretkeysize#" )
}
```

### 📊 Available CGI Variables

The CGI scope provides access to these standard variables:

| Variable | Description |
|----------|-------------|
| `auth_password` | HTTP authentication password |
| `auth_type` | HTTP authentication type |
| `auth_user` | HTTP authenticated username |
| `bx_template_path` | BoxLang template physical path |
| `cf_template_path` | CFML-compatible template path |
| `content_length` | Request content length |
| `content_type` | Request content type |
| `context_path` | Web application context path |
| `gateway_interface` | CGI version |
| `http_*` | All HTTP headers with `http_` prefix |
| `https` | Whether request is secure |
| `local_addr` | Server IP address |
| `local_host` | Server hostname |
| `path_info` | Additional path information |
| `path_translated` | Physical path of template |
| `query_string` | URL query parameters |
| `remote_addr` | Client IP address |
| `remote_host` | Client hostname |
| `remote_user` | Authenticated remote user |
| `request_method` | HTTP method (GET, POST, etc.) |
| `request_url` | Complete request URL |
| `script_name` | Request URI |
| `server_name` | Server hostname |
| `server_port` | Server port number |
| `server_port_secure` | Secure server port |
| `server_protocol` | HTTP protocol version |

## � Form Scope

The `form` scope is a scope available only in web runtimes that contains HTTP POST data submitted from HTML forms. It automatically parses form fields from `application/x-www-form-urlencoded` and `multipart/form-data` requests.

### 🎯 Basic Form Handling

```js
// HTML form submission
<form method="POST" action="/process">
    <input type="text" name="username" value="john.doe" />
    <input type="email" name="email" value="john@example.com" />
    <input type="password" name="password" value="secret123" />
    <button type="submit">Submit</button>
</form>

// BoxLang processing
if( structKeyExists( form, "username" ) ) {
    username = form.username
    email = form.email
    password = form.password

    println( "User: #username#" )
    println( "Email: #email#" )
}
```

### 📦 Array-Based Form Fields (New in 1.9.0)

BoxLang automatically parses form fields with array notation (`[]`) into native arrays, making it easy to work with multiple values without manual conversion:

```js
// HTML form with multiple checkboxes
<form method="POST" action="/preferences">
    <h3>Select Your Favorite Colors:</h3>
    <input type="checkbox" name="colors[]" value="red" />
    <input type="checkbox" name="colors[]" value="blue" />
    <input type="checkbox" name="colors[]" value="green" />

    <h3>Select Programming Languages:</h3>
    <input type="checkbox" name="languages[]" value="boxlang" />
    <input type="checkbox" name="languages[]" value="java" />
    <input type="checkbox" name="languages[]" value="javascript" />

    <button type="submit">Save Preferences</button>
</form>

// BoxLang automatically parses as arrays
colors = form.colors
// colors = ["red", "blue", "green"] (if all selected)

languages = form.languages
// languages = ["boxlang", "java"] (example selection)

// Use array methods directly
println( "Selected #colors.len()# colors" )
println( "Color list: #colors.toList()#" )

// Iterate over selections
for( color in colors ) {
    println( "User likes: #color#" )
}

// Filter selections
modernLanguages = languages.filter( ( lang ) => lang != "javascript" )
```

### 🎯 Array Notation Examples

```js
// Multi-select dropdowns
<select name="categories[]" multiple>
    <option value="news">News</option>
    <option value="sports">Sports</option>
    <option value="tech">Technology</option>
</select>

// BoxLang processing
if( structKeyExists( form, "categories" ) ) {
    categories = form.categories  // Already an array!

    // Save to database
    for( category in categories ) {
        queryExecute(
            "INSERT INTO user_categories (user_id, category) VALUES (?, ?)",
            [ userId, category ]
        )
    }
}

// Dynamic form fields
<input type="text" name="emails[]" placeholder="Email 1" />
<input type="text" name="emails[]" placeholder="Email 2" />
<input type="text" name="emails[]" placeholder="Email 3" />

// Process email list
emails = form.emails  // Array of email addresses

// Validate and filter
validEmails = emails.filter( ( email ) => {
    return len( email ) && isValid( "email", email )
} )

println( "Valid emails: #validEmails.toList()#" )
```

### 📋 Nested Arrays

```js
// Complex form with grouped data
<input type="text" name="products[0][name]" value="Widget" />
<input type="number" name="products[0][qty]" value="5" />

<input type="text" name="products[1][name]" value="Gadget" />
<input type="number" name="products[1][qty]" value="3" />

// BoxLang creates nested structure
products = form.products
// products = [
//     { "name": "Widget", "qty": 5 },
//     { "name": "Gadget", "qty": 3 }
// ]

// Process order items
total = products.reduce( ( sum, product ) => {
    return sum + ( product.qty * getPrice( product.name ) )
}, 0 )
```

### 🔄 Backward Compatibility

Traditional single-value form fields continue to work as always:

```js
// Single value form fields (no array notation)
<input type="text" name="firstName" value="John" />
<input type="text" name="lastName" value="Doe" />

// BoxLang processing
firstName = form.firstName  // "John" (string)
lastName = form.lastName    // "Doe" (string)

// Mixed: some arrays, some single values
<input type="text" name="username" value="johndoe" />
<input type="checkbox" name="roles[]" value="admin" />
<input type="checkbox" name="roles[]" value="editor" />

// Process mixed form
username = form.username  // String
roles = form.roles        // Array
```

### 🎨 Form Scope Methods

Since form is a struct, you have access to all struct methods:

```js
// Check if form was submitted
if( !structIsEmpty( form ) ) {
    println( "Form was submitted" )
}

// Check for specific fields
if( structKeyExists( form, "username" ) ) {
    println( "Username provided" )
}

// Get field with default
email = structKeyExists( form, "email" ) ? form.email : ""

// Validate all fields present
requiredFields = [ "username", "email", "password" ]
missingFields = requiredFields.filter( ( field ) => {
    return !structKeyExists( form, field )
} )

if( missingFields.len() ) {
    abort "Missing fields: #missingFields.toList()#"
}

// Dump entire form for debugging
writeDump( var=form, label="Form Data" )
```

### 🚨 Security Best Practices

```js
// Always validate and sanitize form input
username = form.username ?: ""

// Validate length
if( len( username ) < 3 || len( username ) > 50 ) {
    throw( type="ValidationError", message="Invalid username length" )
}

// HTML encode output to prevent XSS
safeUsername = encodeForHTML( username )

// Validate array inputs
colors = form.colors ?: []

// Ensure it's actually an array
if( !isArray( colors ) ) {
    colors = [ colors ]  // Convert single value to array
}

// Validate each item
validColors = [ "red", "blue", "green", "yellow" ]
selectedColors = colors.filter( ( color ) => {
    return arrayContains( validColors, color )
} )

// SQL injection prevention with parameterized queries
queryExecute(
    "INSERT INTO users (username, email) VALUES (?, ?)",
    [ form.username, form.email ]
)
```

### 📤 File Uploads

File uploads create special entries in the form scope:

```js
// File upload form
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="avatar" />
    <button type="submit">Upload</button>
</form>

// Access file information
if( structKeyExists( form, "avatar" ) ) {
    fileInfo = form.avatar

    println( "Filename: #fileInfo.clientFilename#" )
    println( "Size: #fileInfo.fileSize# bytes" )
    println( "Type: #fileInfo.contentType#" )

    // Move uploaded file
    fileMove( fileInfo.tmpFile, expandPath( "./uploads/#fileInfo.clientFilename#" ) )
}
```

{% hint style="info" %}
**New in 1.9.0**: Array notation automatically converts multiple values into native arrays, eliminating the need for manual `listToArray()` conversions. This works with checkboxes, multi-select dropdowns, and dynamic form fields.
{% endhint %}

## 🔗 URL Scope

The `url` scope is a scope available only in web runtimes that contains HTTP GET parameters from the query string. It automatically parses URL parameters and makes them available as variables.

### 🎯 Basic URL Parameters

```js
// URL: https://example.com/page?name=John&age=30&debug=true

// Access URL parameters
name = url.name      // "John"
age = url.age        // "30" (string)
debug = url.debug    // "true" (string)

println( "Name: #name#" )
println( "Age: #age#" )

// Convert to appropriate types
ageNumeric = val( url.age )
debugBoolean = url.debug == "true"
```

### 📦 Array-Based URL Parameters (New in 1.9.0)

Just like the form scope, the URL scope now automatically parses parameters with array notation (`[]`) into native arrays:

```js
// URL: /search?tags[]=boxlang&tags[]=java&tags[]=modern&sort=recent

// BoxLang automatically parses as array
tags = url.tags
// tags = ["boxlang", "java", "modern"]

sort = url.sort
// sort = "recent" (single value)

// Use array methods directly
println( "Searching for #tags.len()# tags" )
println( "Tags: #tags.toList()#" )

// Build query dynamically
tagConditions = tags.map( ( tag ) => "tags LIKE '%#tag#%'" )
whereClause = tagConditions.toList( " OR " )

// Execute search
results = queryExecute(
    "SELECT * FROM articles WHERE #whereClause# ORDER BY created #url.sort#",
    {},
    { datasource: "mydb" }
)
```

### 🎯 Practical URL Array Examples

```js
// Filter with multiple values
// URL: /products?categories[]=electronics&categories[]=computers&price=low

categories = url.categories
// categories = ["electronics", "computers"]

priceFilter = url.price
// priceFilter = "low"

// Build dynamic query
products = queryExecute(
    "SELECT * FROM products
     WHERE category IN (?)
     AND price_range = ?
     ORDER BY price ASC",
    [ categories.toList(), priceFilter ]
)

// Pagination with sorting
// URL: /users?fields[]=name&fields[]=email&fields[]=created&page=2

fields = url.fields ?: [ "*" ]
// fields = ["name", "email", "created"]

page = val( url.page ?: 1 )
pageSize = 20

// Build SELECT clause
selectClause = fields.toList( ", " )

// Paginated query
users = queryExecute(
    "SELECT #selectClause# FROM users
     LIMIT #pageSize# OFFSET #(page - 1) * pageSize#"
)

// Multiple filters
// URL: /reports?types[]=sales&types[]=inventory&regions[]=north&regions[]=south

reportTypes = url.types
regions = url.regions

// Generate report
report = generateReport(
    types: reportTypes,
    regions: regions
)
```

### 🔄 URL Parameter Combinations

```js
// URL: /search?q=boxlang&filters[]=recent&filters[]=popular&limit=50

// Mix of single values and arrays
searchQuery = url.q              // "boxlang"
filters = url.filters            // ["recent", "popular"]
limit = val( url.limit ?: 10 )   // 50

// Complex filtering
results = searchService.search(
    query: searchQuery,
    filters: filters,
    limit: limit
)

// URL building helper
function buildSearchUrl( query, filters, limit ) {
    params = "q=#urlEncodedFormat(query)#"

    // Add array parameters
    for( filter in filters ) {
        params &= "&filters[]=#urlEncodedFormat(filter)#"
    }

    params &= "&limit=#limit#"

    return "/search?#params#"
}

// Generate URL with arrays
searchUrl = buildSearchUrl( "boxlang", [ "recent", "popular" ], 50 )
// Result: /search?q=boxlang&filters[]=recent&filters[]=popular&limit=50
```

### 📋 Nested URL Parameters

```js
// URL: /data?filters[0][field]=status&filters[0][value]=active&filters[1][field]=type&filters[1][value]=premium

// BoxLang creates nested structure
filters = url.filters
// filters = [
//     { "field": "status", "value": "active" },
//     { "field": "type", "value": "premium" }
// ]

// Build WHERE clause dynamically
whereClauses = filters.map( ( filter ) => {
    return "#filter.field# = '#filter.value#'"
} )

whereSQL = whereClauses.toList( " AND " )

// Execute query
records = queryExecute(
    "SELECT * FROM records WHERE #whereSQL#"
)
```

### 🔍 URL Scope Methods

```js
// Check if parameters exist
if( !structIsEmpty( url ) ) {
    println( "URL parameters present" )
}

// Check specific parameter
if( structKeyExists( url, "id" ) ) {
    recordId = val( url.id )
}

// Get with default value
page = structKeyExists( url, "page" ) ? val( url.page ) : 1
sortOrder = url.sort ?: "asc"

// Validate required parameters
requiredParams = [ "id", "action" ]
missingParams = requiredParams.filter( ( param ) => {
    return !structKeyExists( url, param )
} )

if( missingParams.len() ) {
    throw(
        type: "MissingParameter",
        message: "Missing required parameters: #missingParams.toList()#"
    )
}

// Dump all URL parameters for debugging
writeDump( var=url, label="URL Parameters" )
```

### 🚨 Security Best Practices

```js
// Always validate and sanitize URL parameters
id = val( url.id ?: 0 )

if( id <= 0 ) {
    throw( type="ValidationError", message="Invalid ID" )
}

// Whitelist valid values
validSortOrders = [ "asc", "desc" ]
sortOrder = url.sort ?: "asc"

if( !arrayContains( validSortOrders, sortOrder ) ) {
    sortOrder = "asc"  // Default to safe value
}

// Validate array inputs
tags = url.tags ?: []

// Ensure it's an array
if( !isArray( tags ) ) {
    tags = [ tags ]
}

// Sanitize each tag
sanitizedTags = tags.map( ( tag ) => {
    return encodeForHTML( tag )
} )

// Use parameterized queries
results = queryExecute(
    "SELECT * FROM posts WHERE tags IN (?) ORDER BY created #sortOrder#",
    [ sanitizedTags.toList() ]
)

// XSS prevention for display
safeSearchTerm = encodeForHTML( url.q ?: "" )
println( "Showing results for: #safeSearchTerm#" )
```

### 🔗 URL Building Helpers

```js
// Build URLs with array parameters
function buildUrl( baseUrl, params ) {
    queryString = []

    for( key in params ) {
        value = params[key]

        if( isArray( value ) ) {
            // Add array parameters
            for( item in value ) {
                queryString.append( "#key#[]=#urlEncodedFormat(item)#" )
            }
        } else {
            // Add single parameter
            queryString.append( "#key#=#urlEncodedFormat(value)#" )
        }
    }

    return "#baseUrl#?#queryString.toList('&')#"
}

// Usage
searchUrl = buildUrl( "/search", {
    "q": "boxlang",
    "tags": [ "java", "modern", "dynamic" ],
    "sort": "recent",
    "page": 2
} )

println( searchUrl )
// Output: /search?q=boxlang&tags[]=java&tags[]=modern&tags[]=dynamic&sort=recent&page=2

// Link with array parameters
function filterLink( addFilter ) {
    currentFilters = url.filters ?: []
    newFilters = currentFilters.append( addFilter )

    return buildUrl( cgi.script_name, {
        "filters": newFilters
    } )
}
```

### 🎨 Advanced URL Patterns

```js
// URL: /api/data?include[]=user&include[]=comments&exclude[]=metadata

// Selective field inclusion
include = url.include ?: []
exclude = url.exclude ?: []

// Build field list
fields = getAllFields()
    .filter( ( field ) => include.len() == 0 || arrayContains( include, field ) )
    .filter( ( field ) => !arrayContains( exclude, field ) )

// Fetch data with selected fields
data = queryExecute(
    "SELECT #fields.toList()# FROM data WHERE id = ?",
    [ url.id ]
)

// URL with operators
// URL: /filter?age[gte]=18&age[lte]=65&status[in][]=active&status[in][]=pending

// Parse complex filters
ageMin = val( url[ "age[gte]" ] ?: 0 )
ageMax = val( url[ "age[lte]" ] ?: 999 )
statusIn = url[ "status[in]" ] ?: [ "active" ]

// Build WHERE clause
whereClause = "age BETWEEN #ageMin# AND #ageMax# AND status IN (#statusIn.toList("','")#)"
```

{% hint style="info" %}
**New in 1.9.0**: Array notation (`[]`) in URL parameters automatically creates native arrays, making it easier to handle multiple values for filtering, sorting, and complex queries without manual parsing.
{% endhint %}

{% hint style="warning" %}
**Security**: Always validate and sanitize URL parameters before using them in queries, file operations, or displaying in output. Use parameterized queries to prevent SQL injection and encode output to prevent XSS attacks.
{% endhint %}

## �🚫 Client Scope

The `client` scope is not supported in core BoxLang.  This is a CFML legacy scope that is only available via our `bx-compat-cfml` module.  If you would like to use it, please install the module.

```bash
# Using OS CLI
install-bx-module bx-compat-cfml

# Using CommandBox
box bx-compat-cfml
```
