---
description: Named classes defined inline within scripts and templates without needing a separate file
icon: file-code
---

# Template Classes

Template classes (also called **local classes**) let you define **named classes inline** within your `.bxs` scripts or `.bxm` templates without needing a separate `.bx` file. This means you can define helper classes right where you need them and use them on [try.boxlang.io](https://try.boxlang.io) which runs scripts in a single compilation unit.

```javascript
class Person {
    function getName() {
        return "Brad";
    }
}

result = new Person().getName();
// Result: "Brad"
```

## 📋 Table of Contents

* [Defining Template Classes](template-classes.md#defining-template-classes)
* [Instantiating](template-classes.md#instantiating)
* [Hoisting](template-classes.md#hoisting)
* [Multiple Classes](template-classes.md#multiple-classes)
* [Properties and Constructors](template-classes.md#properties-and-constructors)
* [Static Members](template-classes.md#static-members)
* [Inheritance](template-classes.md#inheritance)
* [Final and Abstract](template-classes.md#final-and-abstract)
* [Java Interoperability](template-classes.md#java-interoperability)
* [Imports](template-classes.md#imports)
* [Metadata](template-classes.md#metadata)
* [Templates](template-classes.md#templates)
* [Naming Restrictions](template-classes.md#naming-restrictions)

## 📥 Defining Template Classes

A template class is declared using the `class` keyword with a **name**, inline in a `.bxs` script or `.bxm` template:

```javascript
class Greeter {
    function greet( name ) {
        return "Hello, " & name & "!";
    }
}
```

Unlike file-based classes (`.bx` files), template classes are **only available within that compilation unit** — the script or template where they are defined.

## 🆕 Instantiating

Template classes are instantiated using `new` just like file-based classes:

```javascript
class Animal {
    function speak() {
        return "...";
    }
}

animal = new Animal();
animal.speak();    // "..."
```

Template class instances are `IClassRunnable` objects, the same as file-based class instances.

## 🏗️ Hoisting

Template classes are **hoisted** to the top of the compilation unit, meaning you can instantiate them **before** their textual definition:

```javascript
// Works even though Greeter is defined below
result = new Greeter().greet( "World" );

class Greeter {
    function greet( name ) {
        return "Hello, " & name & "!";
    }
}
// Result: "Hello, World!"
```

## 📦 Multiple Classes

You can define multiple template classes in the same script:

```javascript
class Adder {
    function add( a, b ) {
        return a + b;
    }
}

class Multiplier {
    function multiply( a, b ) {
        return a * b;
    }
}

adder      = new Adder();
multiplier = new Multiplier();
result     = multiplier.multiply( adder.add( 2, 3 ), 4 );
// Result: 20
```

## 📝 Properties and Constructors

Template classes support properties and `init()` constructors:

```javascript
class Counter {
    property numeric count default=0;

    function increment() {
        variables.count++;
    }

    function getCount() {
        return variables.count;
    }
}

c = new Counter();
c.increment();
c.increment();
c.increment();
c.getCount();    // 3
```

### Constructor with Arguments

```javascript
class Box {
    function init( value ) {
        variables.value = value;
        return this;
    }

    function getValue() {
        return variables.value;
    }
}

result = new Box( 42 ).getValue();
// Result: 42
```

## 🧊 Static Members

Template classes support static blocks, static variables, and static methods:

### Static Variables

```javascript
class Config {
    static {
        static.MAX_RETRIES = 5
        static.APP_NAME = "MyApp"
    }
}

Config::MAX_RETRIES;    // 5
Config::APP_NAME;       // "MyApp"
```

### Static Methods

```javascript
class MathUtil {
    static function add( a, b ) {
        return a + b
    }

    static function multiply( a, b ) {
        return a * b
    }
}

MathUtil::add( 3, 4 )       // 7
MathUtil::multiply( 5, 6 )   // 30
```

## 🔗 Inheritance

### Extending Another Template Class

```javascript
class Animal {
    function speak() {
        return "..."
    }
}

class Dog extends="Animal" {
    function speak() {
        return "Woof!"
    }
}

new Dog().speak()    // "Woof!"
```

### Multi-Level Inheritance

```javascript
class A {
    function getValue() {
        return "A"
    }
}

class B extends="A" {
    function getValueB() {
        return this.getValue() & "B"
    }
}

class C extends="B" {
    function getValueC() {
        return this.getValueB() & "C"
    }
}

new C().getValueC()    // "ABC"
```

### Using `super()`

```javascript
class Vehicle {
    function init( make ) {
        variables.make = make
        return this
    }

    function getMake() {
        return variables.make
    }
}

class Car extends="Vehicle" {
    function init( make, model ) {
        super.init( make )
        variables.model = model
        return this
    }

    function getInfo() {
        return this.getMake() & " " & variables.model
    }
}

new Car( "Toyota", "Camry" ).getInfo()    // "Toyota Camry"
```

## 🔒 Final and Abstract

### Final Classes

A `final` class cannot be extended:

```javascript
final class Immutable {
    function getValue() {
        return "fixed"
    }
}

new Immutable().getValue()    // "fixed"

// ERROR: Cannot extend a final class
class Child extends="Immutable" {}    // throws Exception
```

### Abstract Classes

An `@abstract` class cannot be instantiated directly but can be extended:

```javascript
@abstract class Shape {
    function describe() {
        return "I am a shape"
    }
}

class Circle extends="Shape" {
    function init( radius ) {
        variables.radius = radius
        return this
    }

    function getRadius() {
        return variables.radius
    }
}

// ERROR: Cannot instantiate abstract class
new Shape()    // throws Exception

// Works: instantiate the concrete subclass
circle = new Circle( 5 )
circle.describe()      // "I am a shape"
circle.getRadius()     // 5
```

## ☕ Java Interoperability

Template classes can implement Java interfaces and extend Java classes.

### Implementing a Java Interface

```javascript
class MyRunnable implements="java:java.lang.Runnable" {
    property name="didRun" default=false;

    void function run() {
        variables.didRun = true;
    }
}

r = new MyRunnable();
assert r instanceof "java.lang.Runnable";

thread = new java:Thread( r );
thread.start();
thread.join();
r.getDidRun();    // true
```

### Extending a Java Class

```javascript
class MyTask extends="java:java.util.TimerTask" {

    @overrideJava
    void function run() {
        println( "Hello from local TimerTask!" );
    }

}

task = new MyTask();
assert task instanceof "java.util.TimerTask";
```

### Implementing Comparable

```javascript
class Ranked implements="java:java.lang.Comparable" {
    property name="rank" default=0;

    function init( rank ) {
        variables.rank = rank;
        return this;
    }

    int function compareTo( other ) {
        return variables.rank - other.getRank();
    }
}

a = new Ranked( 3 );
b = new Ranked( 7 );
a.compareTo( b );    // -4 (less than 0)
```

## 📥 Imports

Template classes can use imports from the enclosing script:

```javascript
import java.util.Date;

class Event {
    function init( name ) {
        variables.name = name;
        variables.timestamp = new Date();
        return this;
    }

    function getInfo() {
        return variables.name & " at " & variables.timestamp.toString();
    }
}

new Event( "Party" ).getInfo();    // "Party at Mon May 18 ..."
```

{% hint style="warning" %}
**Name conflicts**: A template class name cannot conflict with an import alias, and an import alias cannot conflict with a template class name. Duplicate template class names (case-insensitive) also throw an error.
{% endhint %}

## 📊 Metadata

Template classes expose full metadata via `getMetadata()`, `getClassMetadata()`, and `$bx.meta`.

### `getMetadata()` on Instance

```javascript
class Person {
    property name="firstName" default="John";
    property name="lastName" default="Doe";

    function fullName() {
        return this.getFirstName() & " " & this.getLastName();
    }
}

meta = getMetadata( new Person() );
meta.name;          // "Person"
meta.type;          // "Class"
meta.properties;    // Array of 2 properties
meta.functions;     // Array of functions
```

### `getClassMetadata()` by Name

```javascript
class Widget {
    property name="label" default="default";
    function getLabel() {
        return variables.label;
    }
}

meta = getClassMetadata( "Widget" );
meta.name;    // "Widget"
meta.type;    // "Class"
```

### `$bx.meta`

```javascript
class Animal {
    property name="species" default="Unknown";
    function speak() {
        return "...";
    }
}

inst = new Animal();
meta = inst.$bx.meta;
meta.name;       // contains "Animal"
meta.type;       // "Class"
meta.properties; // Array of 1 property
```

## 🖼️ Templates

Template classes work inside `<bx:script>` islands in `.bxm` templates:

```xml
<bx:script>
    class Point {
        function init( x, y ) {
            variables.x = x;
            variables.y = y;
            return this;
        }

        function toString() {
            return "(" & variables.x & "," & variables.y & ")";
        }
    }

    result = new Point( 3, 4 ).toString();
</bx:script>
<!-- Result: "(3,4)" -->
```

### Nested Classes in Templates

Template classes can contain nested (inner) classes in templates:

```xml
<bx:script>
    class Parent {
        class Child {
            function greet() {
                return "hi";
            }
        }

        function getChild() {
            return new Child();
        }
    }

    result = new Parent().getChild().greet();
</bx:script>
<!-- Result: "hi" -->
```

{% hint style="info" %}
**Template vs Inner Classes**: Template classes are defined at the top level of a script or template. When a named class is defined inside another `.bx` class body, it is an [Inner Class](inner-classes.md) instead.
{% endhint %}

## ⚠️ Naming Restrictions

### Duplicate Names

Duplicate template class names are not allowed (case-insensitive):

```javascript
class Person {
    function getName() { return "first"; }
}

class Person {    // ERROR: Duplicate class name
    function getName() { return "second"; }
}
```

```javascript
class Widget {
    function getName() { return "lower"; }
}

class WIDGET {    // ERROR: Duplicate (case-insensitive)
    function getName() { return "upper"; }
}
```

### Import Conflicts

A template class name cannot conflict with an import:

```javascript
// ERROR: Import alias conflicts with class name
import java:java.util.HashMap as Widget;

class Widget {
    function getName() {
        return "widget";
    }
}
```

```javascript
// ERROR: Class name conflicts with import
class HashMap {
    function getName() {
        return "my hashmap";
    }
}

import java:java.util.HashMap;
```

### Cannot Define Inside a Function

Template classes cannot be defined inside a function body:

```javascript
class Wrapper {
    function factory() {
        class Product {    // ERROR: Cannot define class inside function
            function getName() {
                return "widget";
            }
        }
        return new Product();
    }
}
```

{% hint style="success" %}
**Tip**: Template classes are ideal for scripts, REPL sessions, and [try.boxlang.io](https://try.boxlang.io) where you want to define and use classes without creating separate files. For reusable classes shared across multiple files, use file-based `.bx` classes instead.
{% endhint %}
