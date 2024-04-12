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
        return static.multiplier * a;
    };
    public static function getGlobalCacheKey(){
        return static.CACHE_KEY;
    }

}
```

## Accessing Static Constructs

We have seen how to declare the static constructor and static methods, but how in the world do we acces them from outside the class? We leverage the `::` double colon syntax.

```java
// Refer to the class by path, then use the :: and call a function or variable
MyFunkyCalculator::CACHE_KEY;
MyFunkyCalculator::calculateValues( 1 );
```
