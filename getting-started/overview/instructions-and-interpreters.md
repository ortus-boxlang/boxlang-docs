---
description: BoxLang is a dynamic JSR-223 language that runs on the JVM
---

# Instructions & Interpreters

## Dynamic Language

BoxLang is a **compiled** programming language that can’t run on your processor directly; it has to be fed into a middleman called the Java Virtual Machine in the form of [Java Bytecode](https://en.wikipedia.org/wiki/Java\_bytecode). It is also a **dynamic language (**[**https://en.wikipedia.org/wiki/Dynamic\_programming\_language**](https://en.wikipedia.org/wiki/Dynamic\_programming\_language)**)**, meaning you do not have the **typed** restrictions a compile-time language like Java has.&#x20;

This means you have greater flexibility as the engine **infers** your types. It allows you to do runtime manipulations like method injections, removals, metadata programming, etc., that a typical typed language would not allow. It also allows us to not be in the dreaded compile, build, deploy cycle since the BoxLang scripts will be evaluated, compiled, and executed all at runtime.  No need for re-deploying or annoying restarts.

### Runtime Exceptions

However, with much power comes greater responsibility. There is a lot more potential for runtime exceptions because these exceptions cannot be caught by a compiler at compilation time, as compilation occurs simultaneously with execution. Thus, unit and integration testing becomes a real asset when building applications under a dynamic language. Wouldn't you know it? We also have a great tool for test-driven and behavior-driven development for BoxLang: [**TestBox**](https://testbox.ortusbooks.com/) ([https://testbox.ortusbooks.com/](https://testbox.ortusbooks.com/))

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**TestBox** is a next-generation testing framework for that is based on BDD (Behavior Driven Development) for providing a clean, obvious syntax for writing tests. It contains a testing framework, runner, assertions, and expectations library and ships with a mocking and stubbing library.
{% endhint %}

### Code Portability

BoxLang will convert your code into byte code and feed it into the Virtual Machine (VM) to execute it. The benefit of this approach is that you can write BoxLang code once and, typically, execute it on many different operating systems and hardware platforms.  Then you can use our multi-runtime approach and deploy to multiple runtimes.

## Java Interop

BoxLang is 100% interoperable with Java since it runs on the JVM.  It allows you to use all third-party Java libraries, import classes, extend, implement and much more.

```groovy
import java.lang.System
import java.util.Date as MyDate
import ortus.boxlang.runtime.types.Array

start = new MyDate().getTime()
num = 1000
myArray = []
myCopy = Array.copyOf( myArray )

printLn( myCopy.size() )
```

## Running from the Command Line

This is a durable way to write BoxLang code because you save your instructions into a file. That file can then be backed up, transferred, added to source control, etc.

### An Example Scripting File

We might create a file named `hello.bxs` like this:

```groovy
println( "Hello from BoxLang, printed on: " & now() )
```

Then we could run the program like this `boxlang hello.bxs` and get the following result:

```
Hello from BoxLang, printed on: {ts '2024-05-21 22:07:19'}
```

### BoxLang REPL

BoxLang ships with a memory REPL (Read Eval Print Loop) interface that you can use to test out the language.  Just run the `boxlang` binary, and you are ready to roll:

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
