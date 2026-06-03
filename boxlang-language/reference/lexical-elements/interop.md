---
icon: java
description: Overview of BoxLang's Java interoperability features, with a pointer to the full guide.
---

# Java Interoperability

BoxLang compiles to JVM bytecode and runs on the JVM, so Java classes are first-class citizens. Any Java library on the classpath is usable directly from BoxLang code without glue layers or adapters.

Key interop features at a glance:

- **`java:` prefix** — force the Java class resolver: `new java:java.util.HashMap()`.
- **`new` operator** — instantiate a Java class and call its constructor in one step.
- **BoxLang class references** — imported BoxLang classes can call constructors with `User.init(args)` or `User(args)`.
- **Java class references** — imported Java classes support the same constructor forms: `StringBuilder.init(args)` or `StringBuilder(args)`.
- **`createObject()`** — retrieve an uninitialized `DynamicObject`; call `.init()` to construct.
- **`extends="java:..."`** — a BoxLang class can extend a Java class; use `@overrideJava` on overriding methods.
- **`implements="java:..."`** — a BoxLang class can implement one or more Java interfaces.
- **`castAs` operator** — native type cast: `value castAs int`, `value castAs String[]`.
- **SAM auto-coercion** — closures, lambdas, and UDFs passed to `@FunctionalInterface` parameters are auto-wrapped; no proxy needed.
- **BIFs** — `CreateObject`, `JavaCast`, `CreateDynamicProxy`, `IsInstanceOf`, `GetBoxContext`, and more.

For the complete reference — class resolution, coercion strategies, inheritance, dynamic proxies, custom class loaders, and Mermaid architecture diagrams — see the full guide:

{% content-ref url="../../../boxlang-framework/java-integration.md" %}
[java-integration.md](../../../boxlang-framework/java-integration.md)
{% endcontent-ref %}
