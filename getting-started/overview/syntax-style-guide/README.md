---
description: Quickly learn what the BoxLang language offers.
---

# Quick Syntax Style Guide

This guide provides a quick overview of BoxLang syntax styles, intricacies, operators, and features. It aims to assist developers from other languages in their BoxLang development journey. BoxLang has been heavily inspired by many different languages, including Java, CFML, Groovy, Kotlin, Ruby, PHP, and more.

{% hint style="success" %}
If you are a CFML developer, check out also our [CFML Guide.](cfml.md)
{% endhint %}

## Dynamic & Loose Typing

BoxLang variables are **dynamic** and **type-inferred**.  We try our best to infer which type you are trying to set for variables at compile-time, but they can completely change at runtime.  You use the `var` keyword to specify a variable within functions or declare them inline if you are in a `bxs` or `bxm` script file.

{% hint style="info" %}
File Types:

* `bx` - A BoxLang class
* `bxs` - A BoxLang scripting file
* `bxm` - A BoxLang templating markup file
{% endhint %}

```groovy
// Infered as 'String'
name = "boxlang"

// Inferred as Double
age = 1
// But I can redeclare it to a string if I need to
age = "one"

// Inferred as Double
isActive = false

// Inferred as Date
today = now()

// Use the `var` keyword to define function-local only variables
function test(){
  var name = "hello"
}

```

You can also add types to arguments within functions or omit them, and it will default to `any,` which means, well, anything:

```cfscript
function add( required numeric a, required numeric b, boolean print = false ){

}
```

As you can see, not only can we make arguments **required** or not, but we can also add **default** values to arguments.  BoxLang does not allow method overrides since basically, every method can take an infinite nubmer of arguments, defined or even NOT defined.

We can also do type promotions and auto-casting from types that can be castable to other types.  So, if we call our function like this:

```groovy
// we auto cast 1 to numeric, "true" to boolean
add( "1", 345, "true" )
```

This is handy as we really really try to match your incoming data to functional arguments.

## `Any` by default

If they are not specifically typed, all arguments and variable declarations are of `any` type. This means they will be inferred at runtime and can change from one type to another.

```cfscript
// Variables declared in a script are of any type and inferred
name = "luis"

function hello( name ){
    // argument name can be anything
}
```

## Case Insensitive Functionality

Most things in BoxLang can be done with **no** case sensitivity by default.  You can enable case sensitivity in many functions and components, but we try to be insensitive as much as possible :). Here are a few observations where access is case-insensitive by nature:

* variable access in any scope
* function calls, even to Java classes
* function arguments, even on Java classes
* class creation, even on Java classes

```cfscript
name = "luis"
// Name can be outputted in any case
println( "Hi, my name is #NamE#" )

// Even maps or arrays
myMap = { name : "luis", age : 12 }
println( "My name is #mymap.NAME# and my age is #mymap.age#" )
```

{% hint style="info" %}
Internally we leverage a `Key` class that provides us with case insensitivity.  Each map has a `Key` as the, well, key.
{% endhint %}

## Expression Interpolation

BoxLang can interpret ANYTHING within `#` as an expression. This can be used for output, assignments, and much more.

```cfscript
"#now()# is a bif, and this #12 % 2# is a math expression, and more!"
```

## Multi-Line Strings

You can declare multi-line strings by using the `"""` start and end operators.  You can also use any interpolation in between.

```java
myLargeContent = """
    Hi,

    How are you today #name#!

    This is a very nice email with merged data!

    Thanks for purchasing #item#!
"""

mailService.send( myLargeContent )
```

## Multi-Variable Assignments

BoxLang supports the concept of multi-variable declaration and assignments by just cascading variables using the `=` operator.

```cfscript
name = threadname = taskName = "I am Spartacus!"
```

This will create the 3 variables in the `variables` scope with the name "I am Spartacus!"

## Switch Statements

The BoxLang switch statements can work on any literal but also on any expression

```cfscript
switch( expression ) {
    case value : case value2 :{
        break;
    }

    default : nothing
}
```

## Catch \`any\` exception

BoxLang allows you to catch `any` exception using our `any` operator

```
try{
    .. funky code here
} catch( any e ){

    // We just caught every single exception known to man!

}
```

## Multi-Catch Exceptions

In BoxLang you can catch multiple exceptions by using the pipe | operator.  They can be both BoxLang exceptions or Java exception types:

```cfscript
catch( foo.com | brad | com.luis.majano e ) {}
```

## No Semicolons

As you can see, semicolons are completely optional. We prefer no semicolons unless you really, really need to demarcate a beginning and an end.

## Scopes

BoxLang offers many different persistence and variable scopes depending on where and what you are. All scopes in BoxLang are backed by the Map interface, which in BoxLang land are called Structures.  They are case-insensitive by default; you can pass them around as much as you like.

#### Scripts (`bxm, bxs`)

Scripts can be written in full script (`bxs`) or using our templating language (`bxm`).

* `variables` - Where all variables are stored
* Unscoped variables go to the `variables` scope in a script

#### Classes

BoxLang supports all Object-oriented constructs know in several languages.  We expand on the areas of metaprogramming and dynamic typing.

* `variables` - The private scope of the class
* `this` - The public scope of the class and also represents the instance
* `static` - The same as Java, a static scope bound to the blueprint of the class
* Unscoped variables go to the `variables` scope in a class

#### Functions/Lambdas/Closures

BoxLang supports 3 types of Functions.

* `local` - A local scope available only to the function
* `arguments` - The incoming arguments
* `variables` - Access to the script or class private scope
* `this` - Access to the class public scope
* Unscoped variables go to the `local` scope in a function by default

#### Persistence Scopes

BoxLang and some of it's runtimes also offer out of the box scopes for persistence.

* `session` - stored in server RAM or external storage tracked by a unique visitor
* `client` - stored in cookies, databases, or external storages (simple values only)
* `application` - stored in server RAM or external storage tracked by the running BoxLang application
* `cookie` - stored in a visitor's browser (Web Only)
* `server` - stored in server RAM for ANY application for that BoxLang instance
* `request` - stored in RAM for a specific request ONLY
* `cgi` - read-only scope provided by the servlet container and BoxLang (Web Only)
* `form` - Variables submitted via HTTP posts (Web Only)
* `URL` - Variables incoming via HTTP GET operations or the incoming URL (Web Only)

{% hint style="info" %}
Please visit our [scopes](../../../boxlang-language/variable-scopes.md) section to find out much more about scopes in BoxLang.
{% endhint %}

### Scope Hunting

When you access a variable without specific scope access, BoxLang will try to find the variable for you in its nearest scope.  This is done internally via a context object, which can be decorated at runtime depending on WHERE the code is being executed (CLI, web, lambda, android, etc)  Example:

```cfscript
function( name ){

    // add to data, which has no scope and no arguments exist
    // so it looks for it in the variables scope
    data.append( name )

    // Looks in arguments first
    return name;
}
```

Check out our [Scopes](../../../boxlang-language/variable-scopes.md) section to learn more about scope hunting.

## Full Null Support

`null` is a real thing! It's nothing but real!  We support the `null` keyword, assignments, and usage just like Java.  It follows the same rules.

## CastAs Operator

BoxLang has a natural casting operator that is fluent and readable.

```java
myJavaClass( value castAs "long" )

return {
    age : value castAs "int",
    tags : value castAs "String[]",
    isActive : "#value#" castAs "Boolean"
}
```

You can also use our handy `javaCast()` bif if you needed to.

### Human Operators

We have several fluent operators using english instead of symbols.



### InstanceOf Operator

Like other languages, we also offer an `instanceOf` operator alongside a nice BIF: `isInstanceOf()`.  You can also use negation using our lovely `not` operator.

```java
isInstanceOf( obj, "Map" )

if( obj instanceOf "String" )
if( obj instanceOf "MyUser" )
if( obj not instanceOf "Integer" )

```

## Data Types

All Java types can be used alongside the core BoxLang types:

* `any`&#x20;
* `array`
* `immutableArray`
* `binary`
* `boolean`
* `class`
* `closure`
* `date`
* `double`
* `guid`
* `function`
* `float`
* `integer`
* `lambda`
* `numeric`
* `number`
* `query`
* `string`
* `struct`
* `immutableStruct`
* `uuid`

## Arrays are Human

Arrays in BoxLang start at 1, not 0. End of story!

## Array/Struct Initializers

Arrays and Structs in BoxLang can be created using literal constructs. Please note that values within the literal declarations can also be expressions.

```cfscript
// empty array
array = []
// array with data
array = [ 1, 23, 234 ]

// empty struct
myMap = {}
// struct with data
myMap = { age:1, test: now() }
```

## Truthy/Falsey

BoxLang Truthy and Falsey are concepts used in programming to determine the "truth" of a value in a Boolean context. In many programming languages, values other than true and false can be evaluated for their truthiness. Understanding truthy and falsey values is crucial for writing effective and accurate code when evaluating conditions or performing logical operations.

### **Truthy values**

* positive numbers (or strings which can be parsed as numbers)
* boolean true
* string “true”
* string “yes”
* array with at least one item
* query with at least one row
* struct with at least one key

### **Falsey values:**

* A `null` value
* The number 0 or string “0”
* boolean false
* string “false”
* string “no”
* empty arrays
* empty queries
* empty structs

## Imports & Class Locators

BoxLang offers the ability to import both BoxLang and Java classes natively into scripts or classes.

```java
// Import java classes
import java:java.io.IOException
import java:java.nio.file.FileSystems
import java:java.nio.file.Path

// Import BoxLang classes
import models.User
import models.cborm.MyService
```

Works just like Java. However, you will notice a nice `java:` prefix.  This is called an class locator prefix.  BoxLang supports these out of the box:

* `java:` - Java classes to import or instantiate
* `bx:` - BoxLang classes to import or instantiate (Default, not required)

{% hint style="warning" %}
You can also remove the `java:` prefix and BoxLang will try to locate the class for you.  Careful, as it will scan all locations.
{% endhint %}

#### Import Aliases

You can also alias imports to provide less ambiguity when dealing with classes with the same name:

```java
// Import java classes
import java:java.nio.file.Path as jPath
import models.utils.Path

myJavaPath = new jPath()
myBxPath = new Path()
```

All the object resolvers prefixes can be used anywhere a class or path is expected:

* Creating classes and instances: `createObject(), new`&#x20;
* Using `imports`&#x20;
* Extending classes
* Implementing interfaces

```java
class implements="java:java.util.List" {

}

class extends="java:ortus.boxlang.runtime.types.Struct"{

}
```

## Null Coalescing aka Elvis Operator

BoxLang supports the null coalescing operator `?:` to allow you to evaluate if values are empty or null. This is **not** a shortened ternary as other languages.

```
( expression ) ?: 'value or expression'
```

This tests the left-hand side of the `?:` and if its `null` then it will evaluate the rigth expression or value.  This can be used on if statements, assignments, loops, etc.

## Safe Navigation Operator

BoxLang supports safety navigation on ANY object that can be dereferenced: structs, maps, classes, etc.  This basically allows you to test if the value exists or not and continue dereferencing or return null

```cfscript
age = form.userdata?.age;

fullName = userClass?.getFullName()
```

Imagine how tedious this code is

```java
if( order ){

    if( order.hasCustomer() ){
        if( order.getCustomer().hasAddress() ){
            println( order.getCustomer().getAddress() )
        }
    }

}
```

Now let's transform this code:

```java
println( order?.getCustomer()?.getAddress() )
```

## Assert

BoxLang offers an `assert` operators that will evaluate an expression and if the expression is falsey it will throw an assert exceptions.

```groovy
// Asserts that the name is truthy
assert name

// Assert an expression
assert myService.hasData()
assert name.length() > 3

// Assert a lambda/closure result.
assert ()-> { do something }
assert ()=> { do something }

```

## Functional

BoxLang functions are first-class citizens.  That means you can pass them around, execute them, dynamically define them, inject them, remove them, and so much more.

It has 3 major functional types:

* **UDF—User-Defined Function**—Can be created on any scripting template or within Classes. They carry no context with them.
* **Closures** are _named_ or _anonymous_ functions that carry with them their surrounding scope and context. It uses the fat arrow `=>` syntax.
* **Lambdas** are _pure_ functions that can be _named_ or _anonymous_ and carry **NO** enclosing scope.  They are meant to be pure functions and produce no side effect.  Data in, Data out. It uses the skinny arrow `->` Syntax.

{% code title="hola.bxs" %}
```cfscript
// A scripting UDF
function sayHello(){
    return "Hola!"
}
```
{% endcode %}

{% code title="MyClass.bx" %}
```cfscript
// Some class UDFs
class{

    function init(){
        return this
    }

    function sayHello(){
        return "Hola!"
    }

}

myClass = new MyClass()

// Let's create an alias to the function
myClass.hola = myClass.sayHello
// Let's remove the sayHello function
myClass.sayHello = null

println( myClass.hola() )
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

All functions and classes are `public` by default, so there is no need to add the `public` identifier if you don't want to.  This creates a very nice and low-verbosity approach to function declaration:

```cfscript
function hello(){}
// Same as:
public function hello(){}

// private
private function getData(){}

// protected
protected function bindData(){}
```

### Non-required arguments by default

All arguments are NOT required by default and will be defaulted to `null` if not passed.  You can use the `required` identifier to mark them as required.

```cfscript
function save( required user, boolean transactional = false, Logger logger ){

}
```

### Default Arguments

You can create defaults for arguments, which can be literal or actual expressions:

```cfscript
function save( transactional = true, data = {}, scope = "#expression#" ){
}

function hello( name = variables.defaultName ){
    println( "Hola #arguments.name#" )
}
```

### Argument Collections

Similar to var arguments in Java, BoxLang allows the `arguments` scope to be completely be variable. meaning you can declare the arguments, but you can pass as many as you like and they will all be added into the `arguments` scope.

Another feature is that you can bind and apply these arguments at function execution time from any map or structure via the `argumentCollection` special argument.  This allows you to collect arguments and dispatch the function call, and BoxLang will match the argument names for you.  This can be great for dynamic argument collection, form collection, JSON packets, etc.

```cfscript
function save( name, age, isActive, logIt=false ){
    .. Do your thing here!!
}

// Call the save using a map/struct
myMap = { name: "test", age: 40, isActive: true }
// Use the special argumentCollection designator
save( argumentCollection : myMap )
```

This is a great time saver.

### Auto-casting Arguments & Return Values <a href="#auto-casting-argument-and-return-value-types" id="auto-casting-argument-and-return-value-types"></a>

In BoxLang, we actively cast the incoming argument value to the specified declared argument.&#x20;

```cfscript
function setAge( numeric age )
```

BoxLang will try to auto cast the incoming argument to the `numeric` type in this instance.

It will also auto cast the outgoing return value for you.  So if your function specifies that the return value is a boolean, but you return a string, it will auto cast it to boolean for you.

```cfscript
function Boolean isAlive(){
    return "yes"
}
```

### BIFs = Built-In Functions

BoxLang is inspired by many languages, and it offers [built-in functions](../../../boxlang-language/reference/built-in-functions/) you can call from anywhere in your code.  They are automatically registered by the core language and any collaborating module.

```cfscript
println( "Hola from #now()#" )
```

{% hint style="info" %}
To get a sense of all the BIFs registered in your runtime, do a&#x20;

writedump( getFunctionList() ) or println( getFunctionList() )
{% endhint %}

### Member Functions

Member functions are special functions attached to all data types in BoxLang, whether they are structs, arrays, strings, numbers, dates, Java objects, classes, etc. We provide tons of member functions, but developers can also contribute their own via BoxLang modules.  All member functions map back to built-in functions.

```cfscript
myArray = [1,2,3,4]
println( myArray.count() )

fruitArray = [
    {'fruit'='apple', 'rating'=4},
    {'fruit'='banana', 'rating'=1},
    {'fruit'='orange', 'rating'=5},
    {'fruit'='mango', 'rating'=2},
    {'fruit'='kiwi', 'rating'=3}
]
favoriteFruites = fruitArray.filter( item -> item.rating >= 3 )
```

{% hint style="info" %}
You can find all the collection of member functions in our [types](../../../boxlang-language/reference/types/) section.
{% endhint %}



## BoxLang Classes

BoxLang classes are enhanced in many capabilities compared to Java, but they are similar to Groovy and CFML.

* Automatic `package` definition
* Automatic Hash Code and Equals
* Automatic constructor created for you
* No need to add a name to the `class` definition, we use the filename
* Implements by default `IClassRunnable, IReferenceable, IType, Serializable`
* Automatic getters and setters for any `property` definition
* Allows for pseudo constructor blocks for initializations and more (Space between last property and first function)
* Output is **false** by default for pseudo-constructors and functions
* You can activate Implicit property accessors and mutators
* Automatic metadata registration into the `$bx` BoxMeta programming object
* Allows for single inheritance
* Allows for interfaces
* Allows for `static` blocks, functions, and properties
* Allows for `final` properties (coming soon)
* Allows for `lazy` properties (coming soon)
* Allows for property observers (coming soon)
* Allows for scope observers (coming soon)
* Functions in a class can have different visibilities: `private, public, protected, remote`

Check out our [Classes](./#classes) section for further information

### Properties, not Fields

BoxLang classes can define properties as data members; they are not called fields and are always `private` meaning they will be stored in the `variables` scope.  You can define them in short or long format.  Please note that properties do require a semi-colon, as they can be very ambiguous.

All properties are stored in the `variables` scope.

#### Short Form

The short form allows for `property [type=any] name [default=expression];`

```cfscript
class{

    // No type means `any`, no default means null
    property firstName;
    // A numeric age with a default value of 1
    property numeric age default=1;
    // A struct data with a default struct literal
    property struct data default={ name:"this", age : 3, whatever : now() };

}
```

#### Long Form

The long form allows for name-value pairs. We distinguish some value pairs from those we don't, and those we don't will be added as metadata to the property.

```cfscript
class{

    property name="firstName" type="string" default="boxlang";
    property name="age" type="numeric";

    property name="data"
        type="struct"
        default={ name:"this", age : 3, whatever : now() };

}
```

Check out our [properties](../../../boxlang-language/classes/properties.md) section for all valid attributes.  Here are a few common ones

* `default` - The property's default value
* `name` - The property's name
* `getter` - Boolean indicator to generate or not the getter for the property. Default is **true**
* `required` - If the property requires a value or not.
* `setter` - Boolean indicator to generate or not the setter for the property. Default is **true**
* `type` - The default type of the property defaults to `any`

{% hint style="info" %}
BoxLang also advertises Class creations, so modules can collaborate with extra metadata and properties or inspect the properties and act on them.

Our dependency injection framework does this.
{% endhint %}

### Automatic Constructor

Constructors in classes for BoxLang are not overloads but a single `init()` method.  However, by default we create one for you.  It can also take in named parameters or an `argumentCollection` to initialize all properties.

{% code title="User.bx" lineNumbers="true" %}
```cfscript
class{

	property name;
	property email;
	property isActive;

}

// Create a new user with no data
user = new User()

// Create one with named params
user = new User( name: "BoxLang", email: "info@boxlang.io", isActive: true )

// Create one with an arg collection
myArgs = { name: "BoxLang", email: "info@boxlang.io", isActive: true }
user = new User( argumentCollection: myArgs )
```
{% endcode %}

{% hint style="danger" %}
If you create your own `init()` then it's your job to initialize your class :)
{% endhint %}

### Annotations

BoxLang annotations can be added to `properties`, `functions`, and `classes`.  Using the following pattern:

```
@annonationName [AnyLiteralExpression=null]
```

You can add as many as you like to the target locations without creating annotation classes or boilerplate.  The annotation's value is completely optional and can be a literal express, which can be a string, list, array, struct, JSON, etc.

### Metadata: $bx

All of these annotations and metadata can be retrieved at runtime by using the `getMetadata()` or `getClassMetadata()` bifs.  You can also look at the `.$bx` property in every boxlang object.  Which contains not only the metadata about each object, but ways to do meta-programming with it.  Like adding/modifying/removing properties/functions/annotations.

Extra metadata can be added to functions, properties, classes, or annotations.

```java
@singleton
@transientCache false
@myMetadata "hello"
class{

}

myClass = new MyClass()
writeOutput( myClass.$bx.meta ) or println( myClass.$bx.meta )
```

The `$bx` object is the BoxLang meta object. It contains all the necessary metadata information about an object.  From it's Java Class, to functions, properties, data, etc.  It can be used on ANY BoxLang Type.  Here are the properties in the `$bx` object available to you. It also contains many methods that exist in the `BoxMeta` object.

* `meta` - A struct of metadata about the class
* `$class` - The Java `Class` that represents your class

### Getter and Setters

By default, automatic **getters** and **setters** for properties are enabled. You can disable them all for the class or one by one. All the setters return an instance of `this`. You can also override them as you see fit.

```cfscript
class{

    property name="firstName" type="string" default="boxlang";
    property name="age" type="numeric"

    // Override the getter
    function getAge(){
        // log it
        return variables.age
    }

    // Override the setter
    function setFirstName( firstName ){
        // Log here
        variables.firstname = arguments.firstName;
        return this;
    }

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
