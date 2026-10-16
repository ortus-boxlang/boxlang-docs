---
description: Learn about static constructs in BoxLang, including static constructors and static methods.
icon: map
---

# Static Constructs

### What is static?

In BoxLang, a static variable is a variable of a class that isn’t associated with an **instance** of a class. Instead, the variable belongs to the class definition itself. As a result, you can access the static variable without first creating the class instance.

### Why use static?

This allows you to create pure utility objects or stateless services that require no instance or holds no instance data. It can also accelerate the retrieval of such variables or methods since no instance has to be ever instantiated in order to be used.

### Where can I apply it?

In BoxLang, the `static` keyword can be applied in the pseudo-constructor in order to initialize static variables in a class. This is called the **static constructor**. The keyword can also be applied to functions within a Component in order to declare static functions.

## Static Constructor

The static constructor is execute once before the class is loaded for the first time, so every class of the same type will share the same **static** scope. This construct is placed inside the pseudo-constructor of the class.

```java
class MyFunkyCalculator{

    // Static Constructor
    static {
        CACHE_KEY = "luis",
        multiplier = 4
    }

}
```

## Static Methods

Static methods can be used without an instance of the class and can also access static variables declared in the static constructor by using the `static` scope from within the same class.

```java
class MyFunkyCalculator{

    // Static Constructor
    static {
        CACHE_KEY = "luis",
        multiplier = 4
    }


    public static function calculate( a ){
        return static.multiplier * a
    }

    public static function getGlobalCacheKey(){
        return static.CACHE_KEY
    }

}
```

## Accessing Static Constructs

We have seen how to declare the static constructor and static methods, but how in the world do we acces them from outside the class? We leverage the `::` double colon syntax.

```java
// Refer to the class by path, then use the :: and call a function or variable
MyFunkyCalculator::CACHE_KEY
MyFunkyCalculator::calculateValues( 1 )
```

## Missing Static Methods: `onMissingStaticMethod()`

{% hint style="info" %}
Available from BoxLang **1.19.0**.
{% endhint %}

Instance calls to methods that do not exist can be handled with `onMissingMethod()`. Static calls have their own handler: declare a **static** function called `onMissingStaticMethod()` and it is called whenever `MyClass::someMethod()` does not find `someMethod` in the static scope.

The handler receives the same arguments as `onMissingMethod()`:

| Argument | Type | Description |
| --- | --- | --- |
| `missingMethodName` | `string` | The name of the method that was called, as written |
| `missingMethodArguments` | `struct` | The arguments of the call. Positional arguments are keyed `1`, `2`, ...; named arguments keep their names |

Whatever the handler returns is returned to the caller.

```java
class User {

    static {
        finderCalls = 0
    }

    static function onMissingStaticMethod( string missingMethodName, struct missingMethodArguments ){
        static.finderCalls++

        if ( missingMethodName.startsWith( "findBy" ) ) {
            var column = missingMethodName.replaceNoCase( "findBy", "" )
            return "Finding user by #column# = #missingMethodArguments[ 1 ]#"
        }

        throw( type = "MethodNotFound", message = "User::#missingMethodName#() does not exist" )
    }

}
```

```java
User::findByEmail( "luis@ortussolutions.com" )
// Finding user by Email = luis@ortussolutions.com
```

### How it works

* The normal static lookup always runs first. The handler is only looked up when the method is missing, so regular static calls cost nothing extra.
* The handler runs as a static function of the class, so the `static` scope is available inside it.
* The handler is found in the class's **static scope**. It can be declared in the class, or put into the static scope at runtime, for example by a module that adds static methods to classes.
* Instance calls keep their usual order: `this` scope, parent class, static scope, class member functions and then `onMissingMethod()`. If none of those resolves and the class has no `onMissingMethod()`, the call falls through to `onMissingStaticMethod()`, just like instance calls can already reach static methods.
* If the class has no `onMissingStaticMethod()`, a missing static method throws the same error as before.

### Caching generated methods

A handler can put a function into the static scope under the missing name. The next call finds it and runs as a normal static method, without going through the handler again. This is how dynamic finders (like the ones in ORMs) avoid parsing the method name on every call.

```java
class User {

    static function onMissingStaticMethod( string missingMethodName, struct missingMethodArguments ){
        var column = missingMethodName.replaceNoCase( "findBy", "" )

        // Generate the finder once and cache it in the static scope
        structInsert( static, missingMethodName, ( value ) => "Finding user by #column# = #value#" )

        return "Finding user by #column# = #missingMethodArguments[ 1 ]#"
    }

}

User::findByEmail( "a@b.com" ) // goes through onMissingStaticMethod()
User::findByEmail( "c@d.com" ) // calls the cached static method directly
```
