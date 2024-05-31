---
description: Quickly learn what the BoxLang language offers.
---

# Quick Syntax Style Guide

This guide provides a quick overview of BoxLang syntax styles, intricacies, operators, and features. It aims to assist developers from other languages in their BoxLang development journey. BoxLang has been heavily inspired by many different languages, including Java, CFML, Groovy, Kotlin, Ruby, PHP, and more.

{% hint style="success" %}
We also offer different [language differences](overview/language-differences/) guides (in progress).
{% endhint %}

### Dynamic & Loose Typing

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

### `Any` by default

If they are not specifically typed, all arguments are of `any` type. This means they will be inferred at runtime and can change from one type to another.

### Case Insensitive Functionality

Most things in BoxLang can be done with **no** case sensitivity by default.  You can enable case sensitivity in many functions and components, but we try to be insensitive as much as possible :). Here are a few observations where access is case-insensitive by nature:

* variable access in any scope
* function calls, even to Java classes
* function arguments, even on Java classes
* class creation, even on Java classes

### Functional

BoxLang functions are first-class citizens.  That means you can pass them around, execute them, dynamically define them, inject them, remove them, and so much more.

It has 3 major functional types:

* **UDF:** **User Defined Function -**  Can be created on any scripting template or within Classes
* **Closures** are _named_ or _anonymous_ functions that carry with them their surrounding scope and context. It uses the fat arrow `=>` syntax.
* **Lambdas** are _pure_ functions that can be _named_ or _anonymous_ and carry **NO** enclosing scope.  They are meant to be pure functions and produce no side efffect.  Data in, Data out. It uses the skinny arrow `->` Syntax.

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

BoxLang is inspired by many languages, and it offers [built-in functions](../boxlang-language/reference/built-in-functions/) you can call from anywhere in your code.  They are automatically registered by the core language and any collaborating module.

```cfscript
println( "Hola from #now()#" )
```

{% hint style="info" %}
To get a sense of all the BIFs registered in your runtime, do a&#x20;

writedump( getFunctionList() ) or println( getFunctionList() )
{% endhint %}

### No Semicolons

As you can see, semicolons are completely optional. We prefer no semicolons unless you really, really need to demarcate a beginning and an end.

### Scopes

BoxLang offers many different persistence and variable scopes depending on where and what you are. All scopes in BoxLang are backed by the Map interface, which in BoxLang land are called Structures.  They are case-insensitive by default, and you can pass them around as much as you like.

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

When you access a variable without specific scope access, BoxLang will try to find the variable for you in its nearest scope, depending on the context it finds itself.  Example:

```cfscript
function( name ){
    
    // add to data, which has no scope and no arguments exist
    // so it looks for it in the variables scope
    data.append( name )

    // Looks in arguments first
    return name;
}
```

Check out our [Scopes](../boxlang-language/variable-scopes.md) section to learn more about scope hunting.

### Full Null Support

`null` is a real thing! It's nothing but real!  We support the `null` keyword, assignments, and usage just like Java.  It follows the same rules.

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

### BoxLang Classes

BoxLang classes are enhanced in many capabilities compared to Java, but they are similar to Groovy and CFML.

* Automatic `package` definition
* Automatic Hash Code and Equals
* Implement by default `IClassRunnable, IReferenceable, IType, Serializable`
* Automatic getters and setters for any `property` definition
* Output is **false** by default for pseudo-constructors and functions
* You can activate Implicit property accessors and mutators
* Automatic metadata registration

Check out our [Classes](syntax-style-guide.md#classes) section for further information

### Properties, not Fields

BoxLang classes can define properties as data members, they are not called fields.  You can define them in short or long format.  Please note that properties do require a semi-colon, as they can be very ambiguous.

All properties are stored in the `variaables` scope.

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

Check out our [properties](../boxlang-language/classes/properties.md) section for all valid attributes.  Here are a few common ones

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
writedump( myClass.$bx ) or println( myClass.$bx )
```

The `$bx` object is the BoxLang meta object. It contains all the necessary metadata information about an object.  From it's Java Class, to functions, properties, data, etc.  It can be used on ANY BoxLang Type.

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
