---
description: 'Welcome to BoxLang: A Modern Dynamic JVM Language'
---

# ⚡ Introduction

<figure><img src=".gitbook/assets/logo-gradient-dark.png" alt=""><figcaption></figcaption></figure>

**BoxLang** is a modern dynamic JVM language that can be deployed on multiple platforms: operating system JVM, web server, lambda, iOS, android, web assembly, and more. BoxLang combines many features from different programming languages, including Java, ColdFusion, Python, Ruby, Go, and PHP, to provide developers with a modern and expressive syntax.

BoxLang has been designed to be a highly adaptable and dynamic language to take advantage of all the modern features of the JVM and was designed with a number of goals in mind:

1. Be a rapid application development (RAD) scripting language and middleware.
2. Be dynamic, modular, lightweight, and fast.
3. Be 100% interoperable with Java.
4. Be able to be deployed as a standalone binary with no JVM required (Much like Kotlin)
5. Be modern, functional, and fluent (Think mixing CFML, Node, Kotlin, Java, and Clojure)
6. Be able to support the following runtime environments.
   1. Native OS Binaries (CLI Tooling, compilers, etc.)
   2. Servlet Containers - CommandBox/Tomcat/Jetty/JBoss
   3. Android/iOS Devices
   4. Web assembly
7. Compile down to Java ByteCode
8. Allow backwards compatibility with existing CFML templates

Key features of BoxLang

1. **Dynamic Language**: BoxLang is dynamically typed, meaning you don’t need to declare types if you don’t want to and can do auto-casting and promotions between different types. BoxLang can infer types and also use underlying types for many variables. The language adapts itself to its deployed runtime. It can add/remove/modify methods and properties at runtime. Making it highly flexible and adaptable.
2. **Low Verbosity Syntax:** BoxLang is a low-verbosity syntax language. It is highly functional, fluent, and human-readable. Our intent with BoxLang is to make it highly expressive and low ceremony.
3. **Scripting**: BoxLang can be used not only for enterprise modular applications but also for highly reusable and quick scripting on the JVM.
4. **InvokeDynamic:** BoxLang is built with a solid core foundation based on the InvokeDynamic features of the JVM. This makes the dynamic language extremely fast, predictable, and adaptable.
5. **Java Interoperability:** BoxLang is 100% interoperable with Java. You can extend and implement Java objects, use annotations, declare classes, import, and more. Thanks to `InvokeDynamic` and our BoxLang `DynamicObject` core, everything in BoxLang is interoperable with Java.
6. **Pure Functions and Closures:** BoxLang supports the creation and usage of closures as a functional programming aspect. However, it also supports the concept of lambda pure functions that have no surrounding context access. Functions are first-class citizens in BoxLang, you can define them dynamically, pass them around and execute them whenever you want. This allows for BoxLang to be a highly functional language.
7. **Event Driven Language:** BoxLang has an event bus internally that can be used to extend the capabilities of the language or even your own applications. You can listen to almost every part of the language, parser and even the runtime or collaborate with your own events.
8. **Modular**: BoxLang has been designed internally to support the concept of BoxLang modules that can enhance every aspect of the language or your applications built with BoxLang. BoxLang is one of the very first languages you can build upon using hierarchical modules. You can add new built-in functions, tags, new/modify functions on existing classes, functionality, AOP aspects, or just listen to events within the language itself.
9. **Professional Open-Source:** BoxLang is a professional open-source project based on the Apache 2 license. Every aspect of the language is supported by Ortus Solutions and you can get a BoxLang+ subscription to not only get professional support but extended features and modular capabilities.
10. **Multi-Platform Development:** BoxLang has been designed to run on many different platforms distinctively. This allows you to write adaptive code for any Operating System JVM, a servlet container web server, cloud lambda functions, iOS, Android or even the browser via our web assembly package. BoxLang builds upon it’s language core so it can be deployed on almost any running platform present or future.
11. **ColdFusion/CFML Compatible:** BoxLang supports a dual parser and compiler that can execute ColdFusion/CFML code natively (maybe more languages later). This means that you can run all your ColdFusion applications within BoxLang natively. We also provide tooling to automatically transpile your ColdFusion code to BoxLang as well.

## Support Open Source

This book is available free of charge [online](https://boxlang.ortusbooks.com) and commercially as a [downloadable or printed book](https://www.ortussolutions.com/learn/books). Your support goes a long way to help the development of this book, future book endeavors, and all the open-source projects we work on. To support us, please consider becoming our patron at [patreon.com/ortussolutions](https://patreon.com/ortussolutions) for as little as $10/month.

## Ortus Solutions, Corp

![](assets/ortus-medium.jpg)

This book was written and maintained by [Luis Majano](https://www.luismajano.com) and the [Ortus Solutions](https://www.ortussolutions.com) Development Team.

> Ortus Solutions is a company that focuses on building professional open source tools, custom applications and great websites! We're the team behind ColdBox, the de-facto enterprise BoxLang HMVC Platform, TestBox, the BoxLang Testing and Behavior Driven Development (BDD) Framework, ContentBox, a highly modular and scalable Content Management System, CommandBox, the BoxLang \<BoxLang> CLI, package manager, etc, and many more - [https://www.ortussolutions.com/](https://www.ortussolutions.com/)
