---
description: BoxLang speaks O.O. and functional tongues.
icon: codepen
---

# Classes & O.O.

BoxLang is an Object-Oriented programming language which means that all the things we interact with inside the virtual machine are objects, which in our case we will call Classes (`.bx`). Objects can hold data, called **properties**, and they can perform actions, called **methods** or **functions,** they can inherit from other objects, they can implement interfaces, they can contain metadata, and even act as RESTFul web services.

```java
@DisplayName( "Cat" )
class extends="Animal"{

    property boolean tail;
    property string name;

}
```

{% hint style="info" %}
Remember that objects are not only data but **data + behavior.**
{% endhint %}

For an example of an object, think about **you** as a human being. You have properties/attributes like height, weight, and eye color. You have functions/methods like walk, run, wash dishes, and daydream. Different kinds of objects have different properties and functions. Some might even just be a collection of functions (utility/static/service objects) or what are referred to as stateless objects, there is no instance data that they represent.

BoxLang supports not only the traditional avenues for object orientation but also many unique constructs and dynamic runtime additions. Enjoy!

## Classes and Instances

In Object-Oriented programming, we define **classes** which are abstract descriptions of a category or type of thing; a blueprint. In our case, we will call them classes and it defines what properties and functions all objects (instances) of that type have. You can consider them to be a blueprint of your object representation. They should have a distinct job and a **single** responsibility (if possible), try to avoid creating God objects.

{% hint style="info" %}
In object-oriented programming, a God object is an object that knows too much or does too much. The God object is an example of an anti-pattern. A common programming technique is to separate a large problem into several smaller problems (a divide and conquer strategy) and create solutions for each of them. - [https://en.wikipedia.org/wiki/God\_object](https://en.wikipedia.org/wiki/God_object)
{% endhint %}

Let's check out an example of a simple Component, `User.bx`

```java
 /**
 * I represent a user in the system
 * Remember that in BoxLang all properties have automatic getters/setters
 * @author Luis Majano
 */
 class{

  /**
  * The name of the user
  */
  property fullName;

  /**
  * The age of the user
  */
  property name="age" type="numeric";

  /**
  * Automatic Constructor if none provided.
  */

  function main(){
     // run baby, run!
  }

 }
```

Please check out the following articles:

* [https://en.wikipedia.org/wiki/Class\_(computer\_programming)](https://en.wikipedia.org/wiki/Class_\(computer_programming\))
* [https://en.wikipedia.org/wiki/Instance\_(computer\_science)](https://en.wikipedia.org/wiki/Instance_\(computer_science\))
* [https://en.wikipedia.org/wiki/Encapsulation\_(computer\_programming)](https://en.wikipedia.org/wiki/Encapsulation_\(computer_programming\))
* [https://en.wikipedia.org/wiki/Abstraction\_(software\_engineering)](https://en.wikipedia.org/wiki/Abstraction_\(software_engineering\))
* [https://en.wikipedia.org/wiki/God\_object](https://en.wikipedia.org/wiki/God_object)
* [https://en.wikipedia.org/wiki/Mutator\_method](https://en.wikipedia.org/wiki/Mutator_method)

### Notes of Interest

The attribute `accessors` in the class definition denotes that automatic **getters (**[**accessors**](https://en.wikipedia.org/wiki/Mutator_method)**)** and **setters (**[**mutators**](https://en.wikipedia.org/wiki/Mutator_method)**)** will be created for all defined properties in the object. Also notice that the class and each property can be documented using `/** **/` notation, which is great for automatic documentation generators like [DocBox](https://www.forgebox.io/view/docbox).

{% hint style="success" %}
Get into the habit of inline documentation, it can go a long way for automatic generators and make you look like you can document like a machine!
{% endhint %}

### Creating Instances

The _User.bx_ class above is a representation of _any_ user or the _idea_ of a user. In order to bring it to life we create an [**instance**](https://en.wikipedia.org/wiki/Instance_\(computer_science\)) of it, populate it with instance data, and then use it.

An instance is a copy of that blueprint stored in memory. BoxLang supports several equivalent construction forms for class references:

```java
import models.User

// Traditional constructor syntax
user = new User( name="luis" )

// Explicit constructor call on the class reference
user = User.init( name="luis" )

// Functional constructor syntax: the class reference is callable
user = User( name="luis" )

// Execute a function within it
user.run()
```

These forms work for BoxLang classes and Java classes. The `new` keyword remains fully supported, but imported class references are also first-class callable objects. Calling `.init()` on a class reference, or invoking the class reference directly, delegates to the same constructor pipeline as `new`.

```java
import models.User
import java:java.lang.StringBuilder

// BoxLang class
u1 = new User( "Luis" )
u2 = User.init( "Luis" )
u3 = User( "Luis" )

// Java class
b1 = new StringBuilder( "abc" )
b2 = StringBuilder.init( "abc" )
b3 = StringBuilder( "abc" )
```

Because class references are callable, they can also be stored, passed around, and used in functional pipelines:

```java
import models.User

factory = User
user    = factory( "Luis" )

names = [ "Alice", "Bob", "Charlie" ]
users = names.map( User )
```

The `createObject()` function is still valid and useful for dynamic, legacy, or intercepted creation paths. Unlike `new` or direct class-reference invocation, `createObject()` returns a class reference and does not call the constructor automatically. Call `.init()` explicitly when you need an initialized instance:

```java
user = createObject( "class", "User" ).init( name="luis" )
```

In later chapters we will investigate the concept of [dependency injection](../../extra-credit/dependency-injection.md). Please also note that the `createObject()` function can also be used to create different types of objects in BoxLang like:

* BoxLang Classes
* Java Objects
* Custom (Implemented by Modules)

## Constructors

Every object in theory should have a constructor method or a method that initializes the object to a **ready** state. Even if the constructor is empty, get into the habit of creating one.

```java
function init(){
 // prepare object state, cache data, start the engine
 return this;
}
```

Note that the constructor returns the `this` scope. This is a reference of the object itself that is returned. You can also return `this` from **ANY** other function which allows for expressive or fluently chainable methods.

```java
function setValue( required val ){
 variables.value = arguments.val;
 return this;
}

obj
 .setValue( 'myvalue' )
 .setValue( 'otherValue' );
```

By default when using the `new Object()` operator, the object's `init()` function will be called for you automatically. You can also call `init()` directly on a class reference, or call the class reference itself as a functional constructor.

```java
// Implicit Constructor
var obj = new Object()

// Explicit constructor on a class reference
var obj = Object.init()

// Functional constructor syntax
var obj = Object()

// Named and positional arguments both work for BoxLang class constructors
var user = User( name="luis" )
var user = User( "luis" )
```

If you use `createObject()`, then the `init()` is NOT called automatically for you; call it explicitly.

```java
var obj = createObject( "class", "Object" ).init()
```

Java classes follow the same class-reference model when imported. See the [Java Interop](../../boxlang-framework/java-integration.md) guide for Java-specific constructor and overload details.

### Pseudo-Constructor

The pseudo-constructor can be found in use in BoxLang and it's a unique beast. Any source code that exists between the `class` declaration and the first function is considered to be the pseudo-constructor. This area of execution will be executed for you implicitly whenever the object is created, even before the implicit `init()` method call. I know confusing, but here is a simple sequence: `new()/createObject() -> pseudo-constructor -> init()`

```java
class{
    // Pseudo Constructor starts here

    this.helper = now();
    static {
        staticVar : 2
    };

    // Pseudo Constructor ends here
    function init(){
        return this;
    }

}
```

## Class Scopes

Every class has certain visibility scopes where properties, variables and functions are attached to.

* `variables` - Private scope, visible internally to the class only, where all `properties` are placed in by default. Public and private function references are place here as well.
* `this` - Public scope, visible from the outside world (can break encapsulation) public function references are placed here.
* `static` - Same as in Java, ability to staticly declare variables and functions at the blueprint level and not at the instance level.

## Class Attributes

The `class` construct can also have many attributes or name-value pairs that will give it some extra functionality for SOAP/REST web services and for Hibernate ORM Persistence. Each BoxLang engine provides different capabilities. You can find all of them here: [https://cfdocs.org/cfcomponent](https://cfdocs.org/cfcomponent). Below are the most common ones:

* `accessors` - Enables automatic getters/setters for properties
* `extends` - Provides inheritance via the path of the Class
* `implements` - Names of the interfaces it implements
* `persistent` - Makes the object a Hibernate Entity which can be fine tuned through a slew of other attributes.
* `serializable` - Whether the class can be serialized into a string/binary format or not. Default is `true`.

```java
class accessors="true" serializable="false" extends="BaseUser"{

}

class implements="cachebox.system.cache.ICacheProvider"{}
```

Please note that in BoxLang you can also declare these attributes via annotations in the comments section.

```java
/**
* My User
* @extends BaseUser
* @accessors true
* @serializable true
*/
class{

}
```
