---
description: They gotta exist somewhere!
icon: cube
---

# Variable Scopes

In the BoxLang language, many persistence and visibility scopes exist for variables to be placed in. These are differentiated by context: in a class, function, tag module, thread, or template.  These scopes are Java maps but enhanced to provide case-insensitivity, member functions and more.&#x20;

{% hint style="info" %}
All BoxLang scopes are implemented as BoxLang [structures](structures.md), basically case-insensitive concurrent hash maps behind the scenes.&#x20;
{% endhint %}

This idea that the variables you declare in templates, classes, and functions are stored in a structure makes your code highly flexible since you can interact with the entire scope fluently and with many different BIFs available.  You can also bind them to function calls, attributes, etc.  Thus, it capitulates on BoxLang being a dynamic language.

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

The only language keyword that can be used to tell the variable to store in a function's local scope is called `var`.  However, you can also just use the `local`scope directly or none at all. However, we do recommend being explicit on some occasions to avoid ambiguity.&#x20;

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

## Scripts & Template Scopes (bxm,bxs)

All scripts and templates have the following scopes available to them.  Please note that the `variables`scope can also be implicit.  You don't have to declare it.

* `variables` - The default or implicit scope to which all variables are assigned.

```javascript
a = "hello"
writeOutput( a )

// Is the same as
variables.a = "hello"
writeOutput( variables.a )
```

## Class Scopes (bx)

All classes in BoxLang follow Object-oriented patterns and have the following scopes available.  Another critical aspect of classes is that all declared functions will be placed in a visibility scope.

* `variables` - Private scope, visible internally to the class only
* `this` - Public scope, visible from the outside world
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

### Class Function Scopes

Depending on the function's visibility, BoxLang places a pointer for the function in the different scopes below.  Why? Because BoxLang is a dynamic language. Meaning at runtime, you can add/remove/modify functions if you want to.

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

## Templates/Scripts Function Scopes

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

## Closure Scopes

All closures are context-aware. Meaning they know about their birthplace and surrounding scopes.  If closures are used in side classes, then they will have access to the class' `variables`and `this`scope.&#x20;

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

## Lambdas (Pure Function) Scopes

Lambdas are pure functions in BoxLang, they do not carry their surrounding or birth context.  They are simpler and faster.

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

## Custom Component Scopes

In BoxLang, you can extend the language and create your own custom components that can be used in script or templating syntaxes.  They allow you to encapsulate behavior that can wrap up anything.

* `attributes` - Incoming component attributes
* `variables` - The default scope for variable assignments inside the component
* `caller` - Used within a custom component to set or read variables within the template that called it.

```xml
// Call a component using script
bx:component template="path/MyComponent.bxm" name="luis"{
    // Content here or more component calls or whatever
}

// Call a component in the templating language: thus looks like custom tags
<bx:component template="path/MyComponent.bxm" name="luis">
    More content
</bx:component>
```

Here is the component:

{% code title="path/MyComponent" %}
```xml
<bx:param name="attributes.name" default="nobody">
<bx:set fullName = "Welcome #attributes.name#">

<cfoutput>
Hello from Component world #fullName#
</cfoutput>
```
{% endcode %}

{% hint style="warning" %}
We highly discourage peeking out of your component using the `caller`scope, but it can sometimes be beneficial.  Use with caution.
{% endhint %}

## Thread Scopes

When you create threads with the `thread`component, you will have these scopes:

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

## **Evaluating Unscoped Variables**

If you use a variable name **without** a scope prefix, BoxLang checks the scopes in the following order to find the variable:

1. Local (function-local, UDFs and Classes only)
2. Arguments
3. Thread local (inside threads only)
4. Query (not a true scope; variables in query loops)
5. Thread
6. Variables
7. CGI
8. CFFILE
9. URL
10. Form
11. Cookie
12. Client

{% hint style="danger" %}
**IMPORTANT**: Because BoxLang must search for variables when you do not specify the scope, you can improve performance by specifying the scope for all variables. It can also help you avoid nasty lookups or unexpected results.
{% endhint %}

## Persistence Scopes

Can be used in any context, used for persisting variables for a period of time.

* `session` - stored in server RAM or external storages tracked by unique web visitor
* `client` - stored in cookies, databases, or external storages (simple values only)
* `application` - stored in server RAM or external storage tracked by the running BoxLang application
* `cookie` - stored in a visitor's browser
* `server` - stored in server RAM for ANY application for that BoxLang instance
* `request` - stored in RAM for a specific user request ONLY
* `cgi` - read only scope provided by the servlet container and BoxLang
* `form` - Variables submitted via HTTP posts
* `URL` - Variables incoming via HTTP GET operations or the incoming URL
