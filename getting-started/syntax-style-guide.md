---
description: Quickly learn what the BoxLang language offers.
---

# Quick Syntax Style Guide

This guide provides a quick overview of BoxLang syntax styles, operators, and features. It aims to assist developers from other languages in their BoxLang development journey.  BoxLang has been heavily inspired by many different languages like Java, CFML, Groovy, Kotlin, Ruby, PHP, and much more.

### Dynamic & Loose Typing

BoxLang variables are dynamic and type-inferred.  We try our best to infer which type you are trying to set for variables at compile-time, but they can completely change at runtime.  You use the `var` keyword to specify a variable within functions, or just declare if you are in a `bxs` or `bxm` script file.

```groovy
// string infered
name = "boxlang"
// double infered
age = 1 
// boolean inferred
isActive = false 

function test(){
  var name = "hello"
}

```

You can also add types to arguments within functions or omit them, and it will default to `any,` which means, well, anything:

```cfscript
function add( required numeric a, required numeric b, boolean print = false ){

}
```

As you can see, not only can we make arguments required or not, but we can also add default values to arguments.  We can also do type promotions and auto-casting from types that can be castable to other types.  So, if we call our function like this:

```groovy
// we auto cast 1 to numeric, "true" to boolean
add( "1", 345, "true" )
```

This is handy as we really really try to match your incoming data to functional arguments.

### `Any` by default

If they are not specifically typed, all arguments are of `any` type. This means that they will be inferred at runtime and can change from one type to another.

### Case Insensitive

Most things in BoxLang can be done with **no** case sensitivity by default.  You can enable case sensitivity in many functions and components.  But we try to be insensitive as much as possible :). Here are a few observations:

* variable access&#x20;
* function calls
* component creations
* argument names

### Functional

BoxLang functions are first-class citizens.  That means you can pass them around, execute them, dynamically define them, inject them, remove them, and so much more.

It has 3 major functional types.

* **UDF** - User-defined function.  Can be created on any scripting template or within Classes
* **Closures** - Named or Anonymous Functions that carry with them their enclosing scope and context.  It uses the `=>` syntax.
* **Lambdas** - Pure functions that can be named or anonymous that carry NO enclosing scope.  Data in, Data out. It uses the `->` Syntax.

{% code title="hola.bxs" %}
```cfscript
function sayHello(){
    return "Hola!"
}
```
{% endcode %}

{% code title="MyClass.bx" %}
```cfscript
class{

    function init(){
        return this
    }
    
    function sayHello(){
        return "Hola!"
    }

}
```
{% endcode %}

```cfscript
// Named closure
myClosure = item => item++;
myClosure( 1 )

// Anonymous Closure
[1,2,3].filter( item => item > 2 )

// Named Lambda
myLambda = item -> item++;
myLambda( 1 )

// Anonymous Lambda
[1,2,3].filter( item -> item > 2 )
```

### `Public` by default

All functions and classes are public by default, so there is no need to add the `public` identifier if you don't want to.  This creates a very nice and low-verbosity approach to function declaration:

```cfscript
function hello(){

}

private function getData(){

}

protected function bindData(){

}
```

### Non-required arguments by default

All arguments are NOT required by default and will be defaulted to `null` if not passed.  You can use the `required` identifier to mark them as required.

### Default Arguments

You can create defaults for arguments, which can be literal or actual expressions:

```java
function save( transactional = true, data = {}, scope = "#expression#" )
```

### Expression Interpolation

BoxLang can interpret ANYTHING within `#` as an expression. This can be used for output, assignments, and much more.

```cfscript
"#now()# is a bif, and this #12 % 2# is a math expression, and more!"
```

### BIFs = Built-In Functions

BoxLang is inspired by many languages and it offers [built-in functions](../boxlang-language/reference/built-in-functions/) you can call from anywhere in your code.

```cfscript
println( "Hola from #now()#" )
```

### No Semicolons

As you can see, semicolons are completely optional. We prefer no semicolons unless you really, really need to demarcate a beginning and an end.

### Scopes

BoxLang offers many different persistence scopes according to where you are and what you are.  All scopes in BoxLang are backed by the Map interface.  So you can use them like maps, pass them around, etc.

#### Scripts

* `variables` - Where all variables are stored
* Unscoped variables go to the `variables` scope in a script

#### Classes

* `variables` - The private scope of the class
* `this` - The public scope of the class and also represents the instance
* `static` - The same as Java, a static scope bound to the blueprint of the class
* Unscoped variables go to the `variables` scope in a class

#### Functions/Lambdas/Closures

* `local` - A local scope available only to the function
* `arguments` - The incoming arguments
* `variables` - Access to the script or class private scope
* `this` - Access to the class public scope
* Unscoped variables go to the `local` scope in a function by default

#### Persistence Scopes

* `session` - stored in server RAM or external storage tracked by a unique visitor
* `client` - stored in cookies, databases, or external storages (simple values only)
* `application` - stored in server RAM or external storage tracked by the running BoxLang application
* `cookie` - stored in a visitor's browser (Web Only)
* `server` - stored in server RAM for ANY application for that BoxLang instance
* `request` - stored in RAM for a specific request ONLY
* `cgi` - read-only scope provided by the servlet container and BoxLang (Web Only)
* `form` - Variables submitted via HTTP posts (Web Only)
* `URL` - Variables incoming via HTTP GET operations or the incoming URL (Web Only)

### Scope Hunting

When you access a variable without specific scope access, BoxLang will try to find the variable for you in its nearest scope.  Example:

```cfscript
function( name ){
    // Looks in arguments first
    return name;
}
```

Check out our [Scopes](../boxlang-language/variable-scopes.md) section to learn more about scope hunting.

### Full Null Support

`null` is a real thing! It's nothing but real!  We support the `null` keyword, assignments, and usage.

### Data Types

All Java types can be used alongside the core BoxLang types:

* `any`&#x20;
* `array`
* `immutableArray`
* `binary`
* `boolean`
* `class`
* `date`
* `guid`
* `function`
* `integer`
* `numeric`
* `number`
* `query`
* `string`
* `struct`
* `immutableStruct`
* `uuid`

### Properties, not Fields

BoxLang classes can define properties as data members, they are not called fields.  You can define them in short or long format.  Please note that properties do require a semi-colon, as they can be very ambiguous.

All properties are stored in the `variaables` scope.

#### Short Form

The short form allows for `property [type=any] name [default=expression];`

```cfscript
class{
    
    // No type means `any`, no default means null
    property firstName;
    property numeric age default=1;
    property struct data default={ name:"this", age : 3, whatever : now() };

}
```

#### Long Form

The long form allows for name-value pairs.  We distinguish some value-pairs from those we don't will be added as metadata to the property.

```cfscript
class{

    property name="firstName" type="string" default="boxlang";
    property name="age" type="numeric"

}
```

Check out our [properties](../boxlang-language/classes/properties.md) section for all valid attributes.  Here are a few common ones

* `default`
* `name`
* `getter`
* `required`
* `setter`
* `type`

### Enhanced Classes

BoxLang classes are enhanced in many capabilities:

* Automatic Hash Code and Equals
* Automatic getters and setters for any property definition
* Implicit property accessors and mutators
* No package definition, we create one for you depending on where the class is located
* Metadata rich

Check out our [Classes](syntax-style-guide.md#classes) section for further information

### Annotations

BoxLang annotations can be added to properties, functions, and classes.  Using the following pattern:

```
@annonationName [literal=null]
```

You can add as many as you like in the target locations without creating Annotation classes.  They are all dynamic and can be named as you want.  The value is `null` if not defined, and can be any literal definiton : string, number, struct, array, etc.

### Metadata

All of these annotations and metadata can be retrieved at runtime by using the `getMetadata()` or `getClassMetadata()` bifs.  You can also look at the `.$bx` property in every boxlang object.  Which contains not only the metadata about each object, but ways to do meta-programming with it.  Like adding/modifying/removing properties/functions/annotations and much more.

Extra metadata can be added to functions, properties, classes as annoatations.

```java
@singleton
@transientCache false
@myMetadata "hello"
class{

}
```

### Getter and Setters

Automatic getters and setters for properties are by default.  You can disable them all for the class or one-by-one.  All the setters return an instance of `this` .  You can also override them as you see fit.

```cfscript
class{
    
    property name="firstName" type="string" default="boxlang";
    property name="age" type="numeric"

}

myClass = new MyClass().setFirstname( "luis" );
```

### Implicit Accessors

If you don't want to see the setter/getter method calls, turn on implicit access since it's `false` by default.

```cfscript
@invokeImplicitAccessor true
class{
    property name="firstName" type="string" default="boxlang";
    property name="age" type="numeric"
}

myClass = new MyClass();
myClass.age = 23
printLn( myClass.age )
```
