---
icon: crosshairs-simple
description: A quick overview of the BoxLang Language & Framework
---

# Overview

### What is BoxLang?

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption><p>BoxLang</p></figcaption></figure>

**BoxLang** is a modern dynamic JVM language that can be deployed on multiple runtimes, including all operating systems, web servers, Java application servers, AWS lambda, iOS, Android, web assembly, and more.

BoxLang combines many features from different programming languages, including Java, CFML, Python, Ruby, Go, and PHP, to provide developers with a modern, fluent, and expressive syntax. It has been designed to be a highly modular and dynamic language that takes advantage of all the modern features of the JVM.

### Goals <a href="#goals-3" id="goals-3"></a>

* Be dynamic, modular, lightweight and fast
* Be 100% interoperable with Java
* Be modern, functional and fluent
* Modularity at its core
* Take advantage of the modern JVM
* TDD/BDD Fully Tested Source
* Support and adapt to multiple runtimes
* Multi-Parser design to support running different dynamic languages like CFML, Groovy and more.
* Tooling and enhanced IDE

### Key Features

1. **Dynamic Language**: BoxLang is dynamically typed, meaning you don’t need to declare types if you don’t want to. It can do type inference, auto-casting, and promotions between different types. The language adapts itself to its deployed runtime. It can add/remove/modify methods and properties at runtime, making it highly flexible and adaptable.
2. **Low Verbosity Syntax:** BoxLang is a low-verbosity syntax language. It is highly functional, fluent, and human-readable. Our intent with BoxLang is to make it highly expressive and low ceremony.
3. **Scripting**: BoxLang can be used for enterprise modular applications and highly reusable and quick scripting on the JVM or Cloud Lambda architectures.
4. **InvokeDynamic:** BoxLang has a solid core foundation based on the JVM’s `InvokeDynamic` features. This makes the dynamic language extremely fast, predictable, and adaptable.
5. **Java Interoperability:** BoxLang is 100% interoperable with Java. You can extend and implement Java objects, use Java annotations, declare classes, import classes, and even write in Java seamlessly. Thanks to `InvokeDynamic` and our BoxLang `DynamicObject` core, everything in BoxLang is interoperable with Java.
6. **Pure Functions and Closures:** BoxLang supports creating and using closures as a functional programming aspect. However, it also supports [lambda pure functions 2](https://en.wikipedia.org/wiki/Pure\_function) without access to the surrounding context, which makes them extremely fast and portable. Functions are first-class citizens in BoxLang. You can define them dynamically, pass them around, and execute them whenever possible, making BoxLang a highly functional language.
7. **Event-Driven Language: BoxLang has an** internal interception event bus that can extend the language's capabilities or even your applications. You can listen to almost every part of the language, parser, and runtime or collaborate with your custom events.
8. **Modular**: BoxLang has been designed internally to support the concept of BoxLang modules that can enhance every aspect of the language or your applications built with BoxLang. BoxLang is one of the first languages you can build upon using modules. You can add new built-in functions, templating components, and new/modified functions on existing classes, functionality, Runtime Debugger, and AOP aspects, or you can listen to events within the language.
9. **Professional Open-Source:** BoxLang is a professional open-source project based on the Apache 2 license. Ortus Solutions supports every aspect of the language, and you can get a BoxLang+ subscription for professional support, extended features, and modular capabilities.
10. **Multi-Platform Development:** BoxLang has been designed to run on multiple platforms. This allows you to write adaptive code for any Operating System JVM, a servlet container web server, cloud lambda functions, iOS, Android, or even the browser via our web assembly package. BoxLang© builds upon its language core to be deployed on almost any running platform, present or future.
11. **Portable, Fluent, Human Scheduled Tasks:** BoxLang Scheduled Tasks Framework provides a centralized and portable way to define and manage scheduled tasks on your servers and applications. Source control your tasking with our scheduling DSL.
12. **CFML Compatible:** BoxLang supports a dual parser and transpiler to execute CFML code natively (maybe more languages later). This means that you can run all your applications written in CFML within BoxLang natively. We also provide tooling to automatically transpile your CFML code to BoxLang.© if you have a + Subscription.
13. **Tooling:** We provide the core language and several tools to help developers do their job easily and efficiently. We provide a Visual Studio Code extension for the language to provide syntax highlighting, debugger, code insight, code documentation, formatting, LSP integration, and more. Our + subscribers get even more tools like enhanced debuggers, CFML transformers, and more.
14. **Ecosystem:** Even though BoxLang is a new language, **it already has an established ecosystem** since every Java and CFML library works with BoxLang. This was our priority when designing BoxLang, and it would automatically be able to integrate and run libraries from the Java and CFML ecosystems. It ships with [CommandBox](https://www.ortussolutions.com/products/commandbox) as its package manager, server manager, task manager, and REPL tool. Almost any project in [https://central.sonatype.com/ 1](https://central.sonatype.com/) and [https://www.forgebox.io](http://www.forgebox.io/) should work with BoxLang.

### Is it CFML compatible?

{% hint style="danger" %}
This is still a work in progress until we go stable in Fall 2024
{% endhint %}

BoxLang had been designed with multiple parsers—one for BoxLang and one for CFML. The CFML parser transpiles to BoxLang at runtime or can be translated to BoxLang via our CLI tools. We try and support as much as we can from CFML. However, we have made very different decisions, and BoxLang is a fresh start for the JVM in a new language. We have introduced a compatibility module to keep old-school CFML working as it is under the BoxLang runtime.

You will have the choice to continue with CFML-compatible code or come to our new vision with BoxLang. We will support both indefinitely.

{% hint style="success" %}
We are also in the planning phases for building a [Groovy](https://www.groovy-lang.org/) parser as well.
{% endhint %}

### Release Video

We launched an open beta of BoxLang at our developer conference, [Into The Box.](https://www.intothebox.org/)

{% embed url="https://www.youtube.com/watch?v=8M0IdUl7IWg&t=1s" %}
