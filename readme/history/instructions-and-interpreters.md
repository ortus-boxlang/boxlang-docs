---
description: BoxLang is a dynamic language that runs on the JVM
---

# Instructions & Interpreters

## Dynamic Language

BoxLang is a **compiled** programming language that can’t run on your processor directly; it has to be fed into a middleman called the Java Virtual Machine in the form of [Java Bytecode](https://en.wikipedia.org/wiki/Java\_bytecode). It is also a **dynamic language (**[**https://en.wikipedia.org/wiki/Dynamic\_programming\_language**](https://en.wikipedia.org/wiki/Dynamic\_programming\_language)**)**, meaning you do not have the **typed** restrictions a compile-time language like Java has. This means you have greater flexibility as the engine **infers** your types. It allows you to do runtime manipulations like method injections, removals, metadata programming, etc., that a typical typed language would not allow. It also allows us to not be in the dreaded compile, build, deploy cycle since the BoxLang scripts will be evaluated, compiled, and executed all at runtime. There is no need for re-deploying or annoying restarts.

### Runtime Exceptions

However, with much power comes greater responsibility. There is a lot more potential for runtime exceptions because these exceptions cannot be caught by a compiler at compilation time, as compilation occurs simultaneously with execution. Thus, unit and integration testing becomes a real asset when building applications under a dynamic language. Wouldn't you know it? We also have a great tool for test-driven and behavior-driven development for BoxLang: [**TestBox**](https://testbox.ortusbooks.com/) ([https://testbox.ortusbooks.com/](https://testbox.ortusbooks.com/))

![TestBox Testing Framework](../../.gitbook/assets/testbox-logo.png)

{% hint style="info" %}
**TestBox** is a next-generation testing framework for BoxLang based on BDD (Behavior-Driven Development). It provides a clean, obvious syntax for writing tests. It contains a testing framework, runner, assertions, expectations library and ships with a mocking and stubbing library.
{% endhint %}

### Code Portability

The BoxLang engine will convert your BoxLang markup into byte code and feed it into the Virtual Machine (VM) to execute it. This approach allows you to write BoxLang code once and typically execute it on many different operating systems and hardware platforms.

You can run any BoxLang script in any BoxLangserver or the command line with CommandBox.

## Java Integration

BoxLang is a dynamic language for the JVM. Thus it runs in a full JDK/JRE context. It also provides you with hooks into the Java virtual machine. Meaning you can create and use Java objects natively in BoxLang. You can even create dynamic proxies and implement Java interfaces natively. Almost **any** Java library or program can be class-loaded and executed in BoxLang. For further reading, check out the [Java Integration Guide](https://boxlang.ortusbooks.com/boxlang-language/java-integration): [https://boxlang.ortusbooks.com/boxlang-language/java-integration](https://boxlang.ortusbooks.com/boxlang-language/java-integration)

```java
currentFile = createObject( "java", "java.io.File" ).init( getCurrentTemplatePath() );
writeOutput( currentFile.lastModified() );


createDynamicProxy(
  new cbproxies.models.Consumer( arguments.consumer ),
  [ "java.util.function.Consumer" ]
)
```

## Running BoxLang from the Command Line

This is a durable way to write BoxLang code because you save your instructions into a file. That file can then be backed up, transferred, added to source control, etc.

### An Example BoxLang File

We might create a file named `hello.bxm` like this:

```markup
<bx:output>Hello from BoxLang Land!</bx:output>
```

Then we could run the program like this `box hello.bxm` and get the following result:

```
Hello from BoxLang Land!
```

{% hint style="warning" %}
When you run `box hello.bxm` you’re loading the BoxLang instruction set engine and executing the code. Please note there is **NO** web server here. It is a pure command-line execution.
{% endhint %}

## CommandBox REPL

CommandBox sports a BoxLang **R**ead **E**val **P**rint **L**oop interface, commonly known as **REPL**. The REPL is like a programming calculator, input in, output out. It will execute BoxLang instructions and give you feedback on syntax and results. To start a REPL, we must go into the CommandBox shell by typing just `box` or opening the `box` binary.

Once in the CommandBox prompt, type `repl` and you will be placed in REPL mode:

![CommandBox](../../assets/repl.png)

Please note that the REPL in CommandBox opens in **script** mode, not **tag** mode. This means we must type in instructions that adhere to the BoxLang scripting or ECMA script-like syntax instead of the tag-based syntax. We will discover more about syntax in the next chapter.

For now, let's type the equivalent in Script syntax:

```javascript
writeOutput( "Hello from BoxLang Land!" )
```

![CommandBox](../../assets/repl-hello.png)

Boom! We get a magical hello from the CommandBox REPL.

{% hint style="success" %}
**Tip**: Our REPL supports not only one-line commands but also multi-line commands. Go ahead, try it!
{% endhint %}

```javascript
if( true ){
    writeoutput( "hello" )
}

echo( "hello" )
```

### Producing Output

In this book, we will primarily use the REPL or CommandBox for execution. During our exercises and code examples, we will use several functions to produce output. Here is a list of what we will use to produce output to the console, the output stream, or a log file.

<table><thead><tr><th width="198">Function</th><th>Description</th></tr></thead><tbody><tr><td><code>echo()</code></td><td>While <a href="https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writeoutput">writeOutput</a> writes to the page-output stream, this function writes to the main response buffer.<br><a href="https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/echo">https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/echo</a></td></tr><tr><td><code>systemOutput()</code></td><td>Writes the given object to the output stream<br><a href="https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/systemoutput">https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/systemoutput</a></td></tr><tr><td><code>writeOutput()</code></td><td>Appends text to the page-output stream.<br><a href="https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writeoutput">https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writeoutput</a></td></tr><tr><td><code>writeDump()</code></td><td>Outputs the elements, variables, and values of most BoxLang objects. Useful for debugging. You can display the contents of simple and complex variables, objects, classes, user-defined functions, and other elements.<br><a href="https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writedump">https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writedump</a></td></tr><tr><td><code>writeLog()</code></td><td>Writes a message to a <a href="https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/log">log</a> file.<br><a href="https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writelog">https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/system/writelog</a></td></tr></tbody></table>

{% hint style="success" %}
`writeDump()` is helpful in the console to visualize complex objects\
`writedump( var=variable, output="console" )`\
\
`You can also pass complex objects to` systemOuput() `as well.`
{% endhint %}
