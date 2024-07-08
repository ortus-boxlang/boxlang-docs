# Functions

Functions are the way to interact with objects, with no functions we have no object-oriented behaviors, no [abstractions](https://en.wikipedia.org/wiki/Abstraction) and no [encapsulation](https://en.wikipedia.org/wiki/Encapsulation\_\(computer\_programming\)). Functions have an automatic return type of `any` which means it can return any type of variable back to a user and an automatic visibility scope of `public`. They also can take in _ANY_ amount of arguments, which don't even have to be defined in the function signature. WOWZA!

Functions in BoxLang are also first-class object citizens. Meaning that each function can be addressed like an object. They can be even deleted, renamed or even injected at runtime. This is one of the most powerful qualities of the BoxLang dynamic language. You can at runtime manipulate objects and their functions.

{% hint style="info" %}
You can find all the different features of functions in the docs: [https://boxlang.ortusbooks.com/boxlang-language/classes/functions](https://boxlang.ortusbooks.com/boxlang-language/classes/functions)
{% endhint %}

### **Declaration**

```java
/**
 * Hints
 */
{access} {modifier:static|final|abstract} {returnType} function {name}({attributes}){}
```

### **Examples**

```java
function hello(){
  return "Hola";
}

abstract function getFile();
public static function testStatic(){}
public final function hello(){}

private function saveData(){

}

/**
 * Check for existence
 *
 * @name The key to check
 */
function boolean valueExists( required name ){
  return variables.exists( arguments.name );
}
```

{% hint style="info" %}
Please note that you can use valid JavaDoc syntax and [DocBox](https://github.com/Ortus-Solutions/DocBox) will document your functions and arguments as well.
{% endhint %}

## Function Access Types and Scopes

Functions can have different visibility contexts:

* `public` - Available to the class and externally
*   `private` - Available only to the class that declares the

    method and any classes that extend the class in

    which it is defined
*   `package` - Available only to the class that declares the

    method, classes that extend the class, or any

    other classes in the package
*   `remote` - Available to a locally or remotely executing page

    or class method, or a remote client through a URL,

    Flash, or a web service. To publish the function as a

    web service, this option is required.

Another interesting tidbit in BoxLang is that the visibility determines where the function will exist within the scope of the class. Remember that functions in BoxLang are objects themselves. They can be added, removed, renamed even at runtime thanks to BoxLang being a dynamic language.

* `public,remote` - The function reference is placed in both the `this` and `variables` scope
* `private,package` - The function reference is placed in the `variables` scope

Does this mean, that I can programmatically change an object at runtime by injecting (mixing) in new methods, or removing methods, or even renaming them? HECK YES SIREE BOB! This is the beauty of the dynamic language, you can manipulate object instances at runtime.

## Function Modifiers

Function modifiers allow you to declare special behaviors to functions, from `static` availability to `final` and `abstract` declarations. We have created a section for each of these types so that you can read more about the modifiers:

* [Static Constructs](static-constructs.md)
* [Final Constructs](final-constructs.md)
* [Abstract Constructs](abstract-constructs.md)

## Function Attributes & Metadata

The `function` construct can also have many attributes or name-value pairs that will give it extra functionality according to the BoxLang engine (metadata). You can find all of them here: [https://boxlang.ortusbooks.com/boxlang-language/classes/functions](https://boxlang.ortusbooks.com/boxlang-language/classes/functions). Below are the most common ones:

* `output` - Will this function send content to the output stream. Try avoiding this to `true` unless you are building libraries of some type, else you are breaking encapsulation
* `description` - A short text description of the function a part from the hint
* `returnFormat` - Format to return for remote callers

```java
function hello() description="" returnFormat=""{

}
```

Please note that in BoxLang, you can also declare these attributes via annotations in the comments section:

```java
/**
* Say Hello
*
* @description A nice function
* @output false
*/
function sayHello(){

}
```

Apart from the name-value pairs of attributes the BoxLang language gives you, you can also add your own. These are called function annotations or custom function metadata. They can be anything you like and they don't even have to have a value. BoxLang then allows you to read the metadata out of the functions via the `getMetadata()` or `getClassMetadata()` functions.

* [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/type/getmetadata](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/type/getmetadata)
* [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/getclassmetadata](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/getclassmetadata)

## Function Arguments

Arguments tell the function how to do their operation. A function can receive zero or more arguments separated by commas in its declaration.

**declaration**

```javascript
function(
 required type name=default attribute=value,
 required type name=default attribute=value
){
}
```

All BoxLang functions are dynamic, meaning they can take any number of arguments without you adding the signatures. You can call functions by passing arguments by position or via name-value pairs, or even with a structure/array of values, which will be called an `argumentCollection`.

**example**

```javascript
function sayHello( target ){
 return "Hi #target#! I'm #name#";
}

function add( required a, required b ){
 return a + b;
}


// Let's call add
calculator.add( 1, 2 );
calculator.add( a=1, b=2 );

// struct collection
values = { a = 1, b = 2 };
calculator.add( argumentCollection=values );

// array collection
values = [ 1, 2 ];
calculator.add( argumentCollection=values );
```

{% hint style="success" %}
**Tip:** Please also note that you can add a-la-carte metadata or name-value pairs to each argument inline or via annotations as we have seen above.
{% endhint %}

**example with annotations**

```javascript
/**
 * Constructor
 *
 * @wirebox The wirebox reference
 * @wirebox.inject wirebox
 */
function init( required wirebox ){
  variables.wirebox = arguments.wirebox;
  return this;
}
```

## Function Returns

BoxLang functions will use the `return` keyword to return a value from the function. A function can be marked `void` in its return type to denote that it does **not** return any value. However, if a function has no return type or `any` and you do not explicitly return a value, then the function will automatically return `null`.

```java
void function nada(){
 // I do stuff, but return nothing
}

function nada(){
 // I do stuff, but also do not return anything
}

function add( a, b ){
 return a + b;
}
```

## Function Scopes

You must be getting into the habit of scopes by now. Functions also have access to all Component scopes plus a few more that are only available to the function itself.

* `arguments` - Collects all the incoming arguments. If the function is called via positional, then this will be a struct with numbers as keys. If the function is called via name-value pairs, the struct will contain the same name-value pairs.
* `local` - A struct that contains all the variables that are ONLY defined in the functions via the `var` keyword.

## Function Var Scope or Local Scope

Each function has a `local` scope that is ONLY available for the lifetime of the function's execution. This is where you will define localized variables since your object can be multi-threaded. Always plan for multi-threaded applications and make sure you var scope your variables. Why? Well, if you do not var scope a variable, then your variable will end up in the implicit scope, which is `variables`.

```javascript
// Sum is not var scoped, so it will be placed in the variables scope, memory leak anyone?
function hello(){
  sum = a + b;

  return sum;
}

function hello( a, b ){
 var sum = a + b;
 return sum;
}

function hello( a, b ){
 local.sum = a + b;
 return local.sum;
}
```

BoxLang also has a weird cascading lookup for variables, so if you do not explicitly specify its scope, BoxLang will look for it for you. If you use a variable name without a scope prefix, BoxLang checks the scopes in the following order to find the variable:

* Local (function-local, UDFs, and Classes only)
* Arguments
* Thread local (inside threads only)
* Query (not a true scope; variables in query loops)
* Thread
* Variables
* CGI
* Cffile
* URL
* Form
* Cookie
* Client

Because BoxLang must search for variables when you do not specify the scope, you can improve performance by specifying the scope for all variables.

## Executing Functions

You can execute functions once you have an instance or reference of a class. If the function has arguments, you can pass them in three ways: positional, name-value pairs, or using a collection (array, struct) via the `argumentCollection` attribute.

```java
user = new User( name="luis" );
writeoutput( user.getName() );

hello = user.sayHello( "bob" );

hello = user.sayHello( target="bob" );

results = calculator.add( 1, 2 );
results = calculator.add( a=1, b=2 );

vals = [ 1, 2 ];
results = calculator.add( argumentCollection=vals );

vals = { a = 1, b = 2 };
results = calculator.add( argumentCollection=vals );
```
