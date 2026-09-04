---
description: Named classes defined inside other classes for encapsulation and organization
icon: box-open
---

# Inner Classes

Inner classes are **named classes defined inside the body of another class** in a `.bx` file. They let you organize related helper classes alongside their parent, keeping implementation details encapsulated while still being accessible when needed.

If [template classes](../syntax.md) let you define helpers inline in scripts, inner classes let you do the same thing inside your classes themselves.

```javascript
class Outer {

    class Inner {
        function getValue() {
            return "inner";
        }
    }

    function getInner() {
        return new Inner();
    }

}

result = new Outer().getInner().getValue();
// Result: "inner"
```

## 📥 Defining Inner Classes

An inner class is declared using the `class` keyword with a **name**, inside the body of an outer class:

```javascript
class Outer {

    class Inner {
        function getValue() {
            return "inner";
        }
    }

}
```

Inner classes can have all the same features as top-level classes:

* Properties
* Constructors (`init()`)
* Functions
* Static blocks
* Annotations
* `extends` and `implements`

```javascript
class Outer {

    class Helper {
        property name="label" default="helper";

        function init( label ) {
            variables.label = label;
            return this;
        }

        function getLabel() {
            return variables.label;
        }
    }

    function getHelper( label ) {
        return new Helper( label );
    }

}

helper = new Outer().getHelper( "custom" );
helper.getLabel();    // "custom"
```

## 🆕 Instantiating Inner Classes

Inner classes are instantiated using `new` from within the outer class:

```javascript
class Outer {

    class Inner {
        function getValue() {
            return "inner";
        }
    }

    function getInner() {
        return new Inner();
    }

}

outer = new Outer();
inner = outer.getInner();
inner.getValue();    // "inner"
```

Inner class instances are `IClassRunnable` objects, just like top-level class instances.

## 📦 Multiple Inner Classes

A single outer class can contain multiple inner classes:

```javascript
class Container {

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

    function compute( a, b ) {
        return new Multiplier().multiply( new Adder().add( a, b ), 2 );
    }

}

result = new Container().compute( 3, 4 );
// Result: 14
```

## 🪆 Nested Inner Classes

Inner classes can themselves contain inner classes, creating multiple levels of nesting:

```javascript
class Outer {

    class First {

        class Second {

            function getDepth() {
                return "second";
            }

        }

        function getSecond() {
            return new Second();
        }

        function getDepth() {
            return "first";
        }

    }

    function getFirst() {
        return new First();
    }

}

outer = new Outer();
first = outer.getFirst();
first.getDepth();              // "first"
first.getSecond().getDepth();  // "second"
```

## 🔗 Inheritance

Inner classes can extend other inner classes defined in the same outer class:

```javascript
class Outer {

    class Animal {
        function speak() {
            return "...";
        }
    }

    class Dog extends="Animal" {
        function speak() {
            return "Woof!";
        }
    }

    function getDog() {
        return new Dog();
    }

}

outer = new Outer();
outer.getDog().speak();    // "Woof!"
```

## 🧊 Static Members

Inner classes can have static blocks and static members:

```javascript
class Outer {

    class Config {
        static {
            static.MAX = 100;
        }
    }

    function getMax() {
        return Config::MAX;
    }

}

result = new Outer().getMax();
// Result: 100
```

## 🔌 Accessing Outer Class Statics

Inner classes can access the outer class's static members using both dot notation and double-colon syntax:

```javascript
class MyClass {

    static {
        static.GREETING = "hello";
    }

    class Inner {

        function getGreetingDot() {
            return MyClass.GREETING;
        }

        function getGreetingColon() {
            return MyClass::GREETING;
        }

    }

    function getInner() {
        return new Inner();
    }

}

inner = new MyClass().getInner();
inner.getGreetingDot();     // "hello"
inner.getGreetingColon();   // "hello"
```

The outer class can also reference its own statics by name:

```javascript
class MyClass {

    static {
        static.NAME = "MyClass";
    }

    function getName() {
        return MyClass.NAME;
    }

    function getNameColon() {
        return MyClass::NAME;
    }

}
```

## 🏗️ Hoisting

Inner classes are **hoisted** within the class body, meaning you can reference and instantiate an inner class before its definition:

```javascript
class Outer {

    function getWidget() {
        return new Widget();    // Works even though Widget is defined below
    }

    class Widget {
        function getName() {
            return "widget";
        }
    }

}

result = new Outer().getWidget().getName();
// Result: "widget"
```

## 🌍 External Access

Inner classes are compiled as sibling JVM classes with `$`-delimited names (e.g., `OuterClass$Inner`). This means they can be accessed from **outside** the outer class using the `$` separator syntax.

### Instantiating via `$` Syntax

```javascript
// Using fully qualified path with $ separator
widget = new path.to.OuterClass$Widget( "my-widget" );
widget.getName();    // "my-widget"
```

### Accessing Statics via `$` Syntax

```javascript
// Access inner class static field
result = path.to.OuterClass$Widget::WIDGET_TYPE;
```

### Nested Inner Classes via Chained `$`

```javascript
// Three levels deep: Outer$First$Second
second = new path.to.OuterClass$First$Second();
second.getDepth();    // "second"
```

## 📥 Importing Inner Classes

Inner classes can be imported using the `$` separator syntax:

```javascript
import path.to.OuterClass$Widget;

widget = new Widget( "imported-widget" );
widget.getName();    // "imported-widget"
```

### Importing with Alias

```javascript
import path.to.OuterClass$Widget as MyWidget;

widget = new MyWidget( "aliased-widget" );
widget.getName();    // "aliased-widget"
```

### Accessing Statics After Import

```javascript
import path.to.OuterClass$Widget;

result = Widget::WIDGET_TYPE;
// Result: "gadget"
```

### Referencing Inner Classes via Outer Class

You can also reference inner classes statically via the outer class name using dot or double-colon syntax:

```javascript
import path.to.OuterClass;

// Dot notation
widgetClass = OuterClass.Widget;

// Double-colon notation
widgetClass = OuterClass::Widget;

// Instantiate via the class reference
widget = new widgetClass( "test" );
```

### Using `createObject()`

```javascript
widget = createObject( "component", "path.to.OuterClass$Widget" );
```

## 📊 Metadata

Inner classes expose metadata through `$bx` (ClassMeta) and `getMetadata()`.

### `$bx` Metadata

```javascript
outer = new OuterClass();

// Get ClassMeta object
meta = outer.$bx;

// Get inner class map
inners = meta.getInnerBoxClasses();
// Returns Map<Key, Class<?>> with entries like { "Inner": OuterClass$Inner }

// Get enclosing class (null for top-level)
enclosing = outer.getInner().$bx.getEnclosingBoxClass();
```

### `getMetadata()` Struct

```javascript
outer = new OuterClass();
meta = getMetadata( outer );

// Inner classes struct
meta.innerClasses;
// { "Widget": "path.to.OuterClass$Widget", "Util": "path.to.OuterClass$Util" }

// Enclosing class (empty for top-level)
meta.enclosingClass;    // ""
```

For an inner class instance:

```javascript
widget = new OuterClass$Widget( "test" );
meta = getMetadata( widget );

meta.name;              // "path.to.OuterClass$Widget"
meta.simpleName;        // "Widget"
meta.fullname;          // "path.to.OuterClass$Widget"
meta.enclosingClass;    // "path.to.OuterClass"
meta.innerClasses;      // {} (empty if no nested inner classes)
meta.type;              // "Class"
meta.properties;        // Array of property metadata
meta.functions;         // Array of function metadata
```

### `getClassMetadata()`

```javascript
meta = getClassMetadata( "path.to.OuterClass$Widget" );
meta.name;    // "path.to.OuterClass$Widget"
```

### `isInstanceOf()` with Inner Classes

```javascript
widget = new OuterClass$Widget( "test" );

isInstanceOf( widget, "Widget" );                          // true
isInstanceOf( widget, "path.to.OuterClass$Widget" );       // true
isInstanceOf( widget, "OuterClass" );                      // false (not the parent)
```

## ☕ Java Interoperability

Inner classes can implement Java interfaces, making them useful for Java interop patterns:

```javascript
class implements="java:java.lang.Iterable" {

    property Array items;

    function init( array items = [] ) {
        variables.items = arguments.items;
        return this;
    }

    function iterator() {
        return new BoxIterator( variables.items );
    }

    // Inner class implementing java.util.Iterator
    class BoxIterator implements="java:java.util.Iterator" {

        property name="data";
        property name="position";

        function init( array data ) {
            variables.data = arguments.data;
            variables.position = 0;
            return this;
        }

        boolean function hasNext() {
            return variables.position < variables.data.len();
        }

        function next() {
            if ( !hasNext() ) {
                throw( type = "java.util.NoSuchElementException", message = "No more elements" );
            }
            variables.position++;
            return variables.data[ variables.position ];
        }

    }

}

// Use from Java or BoxLang
myList = new MyIterable( [ "a", "b", "c" ] );
iter = myList.iterator();
while ( iter.hasNext() ) {
    println( iter.next() );
}
```

## ⚠️ Naming Restrictions

### Outer Class Name is Reserved

When a class has inner classes, the outer class name becomes a **reserved variable name**. You cannot assign to it or use it as a function argument:

```javascript
// ERROR: Cannot assign to outer class name
class MyClass {
    class Inner {}

    function doStuff() {
        MyClass = "oops";    // Throws BoxRuntimeException
    }
}

// ERROR: Cannot use outer class name as argument
class MyClass {
    class Inner {}

    function doStuff( MyClass ) {    // Throws BoxRuntimeException
        return MyClass;
    }
}
```

### Inner Class Cannot Match File Name

An inner class cannot have the same name as the enclosing file's class name:

```javascript
// File: MyFile.bx
class {

    class MyFile {    // ERROR: Cannot match file name
        function getValue() {
            return "inner";
        }
    }

}
```

### Inner Class Names Cannot Be Assigned as Statics

You cannot overwrite an inner class name via static assignment:

```javascript
import path.to.OuterClass;

OuterClass::Inner = "oops";    // Throws BoxRuntimeException
OuterClass.Inner = "oops";     // Throws BoxRuntimeException
```

{% hint style="info" %}
**JVM Compilation**: Inner classes are compiled as sibling JVM classes with `$`-delimited names (e.g., `OuterClass$Inner`). This is consistent with how Java handles inner classes and enables seamless Java interoperability.
{% endhint %}

{% hint style="success" %}
**Tip**: Inner classes are ideal for helper classes, iterator implementations, builder patterns, and any situation where a class is tightly coupled to its parent and unlikely to be used independently.
{% endhint %}
