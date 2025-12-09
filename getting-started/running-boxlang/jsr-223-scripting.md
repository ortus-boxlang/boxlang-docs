---
description: Integrate BoxLang into Java applications using JSR-223 Scripting
icon: scroll
---

# JSR-223 Scripting

<figure><img src="../../.gitbook/assets/jsr-223.png" alt=""><figcaption></figcaption></figure>

## 🚀 Getting Started for Java Developers

JSR 223, also known as "**Scripting for the Java Platform,**" enables seamless integration between Java applications and scripting languages like BoxLang. This guide shows Java developers how to embed BoxLang's dynamic capabilities directly into their applications.

{% embed url="https://www.oracle.com/technical-resources/articles/javase/scripting.html" %}

## 📋 Table of Contents

- [Getting Started for Java Developers](#getting-started-for-java-developers)
- [Adding BoxLang to Your Project](#adding-boxlang-to-your-project)
- [Quick Start Example](#quick-start-example)
- [Architecture Overview](#architecture-overview)
- [Common Use Cases for Java Developers](#common-use-cases-for-java-developers)
- [Core Scripting Classes](#core-scripting-classes)
- [BoxLang Home Configuration](#boxlang-home-configuration)
- [Production Considerations](#production-considerations)
- [Integration Patterns](#integration-patterns)

## 📦 Adding BoxLang to Your Project

### Maven Dependency

Add BoxLang to your Maven project's `pom.xml`:

```xml
<dependency>
    <groupId>io.boxlang</groupId>
    <artifactId>boxlang</artifactId>
    <version>1.5.0</version>
</dependency>
```

### Gradle Dependency

For Gradle projects, add to your `build.gradle`:

```groovy
dependencies {
    implementation 'io.boxlang:boxlang:1.5.0'
}
```

### Direct JAR Download

Download the latest BoxLang JAR from:

- **Releases**: [https://github.com/ortus-boxlang/BoxLang/releases](https://github.com/ortus-boxlang/BoxLang/releases)
- **Snapshots**: [https://s3.amazonaws.com/downloads.ortussolutions.com/boxlang/](https://s3.amazonaws.com/downloads.ortussolutions.com/boxlang/)

Add the JAR to your project's classpath:

```bash
# Compile with BoxLang
javac -cp "boxlang-1.5.0.jar:." MyApp.java

# Run with BoxLang
java -cp "boxlang-1.5.0.jar:." MyApp
```

### System Requirements

- **Java 21+** (BoxLang requires JDK 21 or later)
- **JSR-223 Support** (included in standard Java installations)

## 🏗️ Quick Start Example

Here's a complete Java application demonstrating BoxLang integration:

```java
import javax.script.*;
import ortus.boxlang.runtime.scripting.BoxScriptingFactory;

public class BoxLangExample {
    public static void main( String[] args ) throws ScriptException {
        // Get BoxLang engine
        ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

        // Pass data to BoxLang
        Bindings bindings = engine.createBindings();
        bindings.put( "name", "Java Developer" );
        bindings.put( "items", java.util.Arrays.asList( "Spring", "Maven", "BoxLang" ) );

        // Execute BoxLang code
        Object result = engine.eval( """
            message = "Hello " & name & "!"
            itemCount = items.len()
            return {
                greeting: message,
                totalItems: itemCount,
                technologies: items.map( ( item ) => item.uCase() )
            }
        """, bindings );

        System.out.println( "Result: " + result );
    }
}
```

{% embed url="https://en.wikipedia.org/wiki/Scripting_for_the_Java_Platform" %}

## 🔧 Architecture Overview

BoxLang offers complete JSR-223 compliance for seamless integration with JVM applications. Understanding the core components helps Java developers leverage BoxLang effectively.

{% embed url="https://s3.amazonaws.com/apidocs.ortussolutions.com/boxlang/1.0.0/ortus/boxlang/runtime/scripting/package-summary.html" %}
API Documentation
{% endembed %}

## 💡 Common Use Cases for Java Developers

### Configuration & Rules Engine

```java
// Load business rules from external files
ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

Bindings context = engine.createBindings();
context.put( "order", orderObject );
context.put( "customer", customerData );

Boolean eligible = ( Boolean ) engine.eval( """
    // Business logic in BoxLang - easier for business users to modify
    if ( order.total > 1000 && customer.tier == "GOLD" ) {
        return true
    }

    if ( customer.loyaltyPoints > 5000 ) {
        return true
    }

    return false
""", context );
```

### Template Processing

```java
// Process templates with BoxLang's powerful string handling
ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

Bindings data = engine.createBindings();
data.put( "user", userObject );
data.put( "notifications", notificationList );

String html = ( String ) engine.eval( """
    template = "
        <h1>Welcome #{user.name}!</h1>
        <div class='notifications'>
        #notifications.map( ( n ) => '<p>' & n.message & '</p>' ).join( '' )#
        </div>
    "

    // Use proper string replacement instead of evaluate() BIF
    result = template
    result = result.replace( "#{user.name}", user.name )
    // Add more replacements as needed

    return result
""", data );
```

### Data Transformation

```java
// Transform JSON/XML with BoxLang's built-in functions
ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

Bindings bindings = engine.createBindings();
bindings.put( "jsonData", rawJsonString );

Map result = ( Map ) engine.eval( """
    data = deserializeJSON( jsonData )

    return {
        processedAt: now(),
        recordCount: data.records.len(),
        summary: data.records
            .filter( ( r ) => r.active == true )
            .groupBy( "category" )
            .map( ( category, items ) => {
                category: category,
                count: items.len(),
                totalValue: items.sum( "value" )
            } )
    }
""", bindings );
```

## 📚 Core Scripting Classes

The BoxLang scripting package can be found here: `ortus.boxlang.runtime.scripting`. The classes that will assist you are:

- `BoxCompiledScript` - Implements the JSR `CompiledScript` interface ([https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/CompiledScript.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/CompiledScript.html))
- `BoxScopeBindings` - Implements the JSR `Bindings` interface ([https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/Bindings.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/Bindings.html))
- `BoxScriptingContext` - Implements the JSR `ScriptContext` interface ([https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptContext.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptContext.html))
- `BoxScriptingEngine` - Implements the JSR `ScriptEngine` and `Compilable`
  [https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngine.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngine.html)
  [https://docs.oracle.com/en/java/javase/17/docs/api//java.scripting/javax/script/Compilable.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/Compilable.html)
- `BoxScriptingFactory` - implements the JSR `ScriptEngineFactory`
  [https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngineFactory.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngineFactory.html)

### Definitions

- **Script Factory** - creates scripting engines and gets metadata about scripting engines.
- **Script Engine** - provides a way to create bindings, scripts, and run statements.
- **Invocable** - Our BoxLang engine also implements the scripting `Invocable` [interface](https://docs.oracle.com/en/java/javase/21/docs/api/java.scripting/javax/script/Invocable.html) so you can declare functions and classes (coming soon) and then execute them from the calling language.
- **Bindings** - these are like scopes to BoxLang. The bridge between Java and BoxLang
- **Scripting Context** - Like the BoxLang context object, it provides scope lookups and access to bindings.

### Bindings

Bindings are under the hood `HashMaps`. They are used to bind your Java code to the BoxLang code. By default, in BoxLang, we provide three scopes you can bind bindings to:

- `Engine Scope` - The **default** scope which maps to the BoxLang `variables` scope
- `Request Scope` - The JSR request scope maps to the BoxLang `request` scope
- `Global Scope` - The JSR global scope maps to the BoxLang `server` scope

### Discovering Engines

To find out what engines are available in your platform you can run the following:

```java
ScriptEngineManager mgr = new ScriptEngineManager();
List<ScriptEngineFactory> factories = mgr.getEngineFactories();
```

### BoxLang ScriptEngine

To get started, you need to get an instance of the BoxLang Scripting Engine.  You can do so by using the Java `ScriptEngineManager()` class or importing our `BoxScriptingEngine` class.

{% code lineNumbers="true" %}
```java
import javax.script.*;

ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

// Or directly via our BoxScriptingFactory class

import ortus.boxlang.runtime.scripting.BoxScriptingFactory;

ScriptEngine engine = new BoxScriptingFactory().getScriptEngine();
```
{% endcode %}

You can also cast it to our class to get enhanced methods and functionality:

```java
BoxScriptingEngine engine = (BoxScriptingEngine) new BoxScriptingFactory().getScriptEngine();
```

#### Debug Mode

If you ever need to send debugging information to the console from the BoxRuntime in the scripting engine, you can create a new script engine and pass the `debug` flag to it.

```java
import ortus.boxlang.runtime.scripting.BoxScriptingFactory;

ScriptEngine engine = new BoxScriptingFactory().getScriptEngine( true );
```

This will start up the `BoxRuntime` in debug mode.

## 🏠 BoxLang Home Configuration

### Default BoxLang Home

When you create a BoxLang scripting engine, it initializes a BoxLang runtime instance that uses a home directory for configuration and modules. By default, BoxLang uses:

```
{user.home}/.boxlang/
```

For example:

- **Linux/macOS**: `/home/username/.boxlang/` or `/Users/username/.boxlang/`
- **Windows**: `C:\Users\username\.boxlang\`

### Custom Home Directory

You can configure a custom BoxLang home directory using system properties or environment variables:

```java
// Option 1: Set system property before creating engine
System.setProperty( "boxlang.home", "/custom/boxlang/home" );
ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

// Option 2: Set environment variable (BOXLANG_HOME)
// Set environment variable before running your Java application
// export BOXLANG_HOME=/custom/boxlang/home
```

### Runtime Configuration

The BoxLang home directory contains:

- **`config/boxlang.json`** - Runtime configuration file
- **`lib/`** - Custom modules and libraries
- **`logs/`** - Runtime log files (if file logging is enabled)

You can customize the runtime behavior by modifying the `boxlang.json` configuration file:

```java
// Access runtime configuration through the engine
BoxScriptingEngine boxEngine = ( BoxScriptingEngine ) engine;
BoxRuntime runtime = boxEngine.getRuntime();
// Configuration is automatically loaded from {BOXLANG_HOME}/config/boxlang.json
```

### Multiple Runtime Instances

For applications requiring isolated BoxLang environments, you can create separate instances:

```java
// Create first instance with custom home
System.setProperty( "boxlang.home", "/app1/boxlang" );
ScriptEngine engine1 = new ScriptEngineManager().getEngineByName( "BoxLang" );

// Note: BoxRuntime is singleton-based, so use separate JVMs or custom factory for true isolation
// For most use cases, separate bindings provide sufficient isolation
```

### Configuration Override

You can also override specific configuration settings using system properties or environment variables by prefixing with `boxlang.` or `BOXLANG_`:

```java
// Override specific settings
System.setProperty( "boxlang.runtime.debugMode", "true" );
System.setProperty( "boxlang.runtime.classGenerationDirectory", "/tmp/boxlang-classes" );

// These will override values in boxlang.json
ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );
```

### Eval() BoxLang Code

Once you access the script engine, you can use the plethora of `eval()` methods to execute the BoxLang source and bind with specific dynamic bindings.  You can execute scripts from strings or reader objects.  You can also compile a script/class into a `CompiledScript` and then execute it at a later point in time via the `compile()` methods.

```java
boxlang.eval( "println( 'hello world' )" )
```

You can use eval with the following signatures

```java
/**
 * Evaluate a script in the context of the ScriptContext
 *
 * @param script  The script to evaluate
 * @param context The context to evaluate the script in
 *
 * @return The result of the script evaluation
 */
public Object eval( String script, ScriptContext context ) throws ScriptException

/**
 * Evaluate a script in the context of the ScriptContext
 *
 * @param reader  The reader to read the script from
 * @param context The context to evaluate the script in
 *
 * @return The result of the script evaluation
 */
public Object eval( Reader reader, ScriptContext context ) throws ScriptException

/**
 * Evaluate a script bound only to the top-level BoxRuntime context
 *
 * @param reader The reader to read the script from
 *
 * @return The result of the script evaluation
 */
public Object eval( Reader reader ) throws ScriptException

/**
 * Evaluate a script using the given Bindings
 *
 * @param script The script to evaluate
 * @param n      The Bindings to use
 *
 * @return The result of the script evaluation
 */
@Override
public Object eval( String script, Bindings n ) throws ScriptException

@Override
public Object eval( Reader reader, Bindings n ) throws ScriptException

/**
 * Evaluate a script bound only to the top-level BoxRuntime context
 *
 * @param script The script to evaluate
 *
 * @return The result of the script evaluation
 */
public Object eval( String script ) throws ScriptException
```

### Bindings - Passing Data to the Scripts

Data can be passed into the engine by defining a _Bindings_ object and passing it as a second parameter to the _eval_ function.  You will do so by using the `createBindings()` method.  If you casted the engine to our `BoxScriptingEngine` class, you will also get a `createBindings( Map m )` so you can quickly create bindings from a map of data.

{% code lineNumbers="true" %}
```java
Bindings bindings = boxlang.createBindings();
bindings.put( "count", 3 );
bindings.put( "name", "luis" );
bindings.put( "age", 1 );

// Or if you have already a map of data
Bindings bindings = boxlang.createBindings( myMap );

// Script and evaluate the last result
result = engine.eval( """
  println( 'Hello, ' & name & '!' )
  newAge = age + 1
  totalAge = newAge + 1
  request.nameTest = name
  server.nameTest = name
""", bindings );

// We cannot use the same bindings, these are just to send
// We need to get the bounded bindings now via the `getBindings()` method
Bindings resultBindings = engine.getBindings();
// The result of the script is the last expression
assertThat( result ).isEqualTo( "World" );
// Test the bindings
assertThat( resultBindings.get( "newAge" ) ).isEqualTo( 2 );
assertThat( engine.getRequestBindings().get( "nameTest" ) ).isEqualTo( "World" );
assertThat( engine.getServerBindings().get( "nameTest" ) ).isEqualTo( "World" );
```
{% endcode %}

{% hint style="warning" %}
Once you bind the engine with bindings before execution, you must get the modified bindings via the `engine.getBindings()` method.  If you don't do this, you will only have access to the simple hashmap to bind the engine.
{% endhint %}

### Calling Functions From Java to BoxLang

You can also use the `eval()` method to define functions, closures, or lambdas in BoxLang and execute them in your host language.  We do so by evaluating the script, casting the engine to `Invocable,` and using the `invokeFunction()` method.

```java
engine.eval( """
    function sayHello( name ) {
        return 'Hello, ' & name & '!'
    }
""");

Invocable	invocable	= ( Invocable ) engine;
Object		result		= invocable.invokeFunction( "sayHello", "World" );
assertThat( result ).isEqualTo( "Hello, World!" );
```

### Objects, Functions, Closures, Lambdas, Member Methods

You can also use the `invokeMethod( object, name, args )` function, which allows you to target a specific object, such as a BoxLang class, member method, struct, lambda, closure or collection of functions.

```java
// Create a struct
engine.eval( "myStr = { foo : 'bar' }" );
// Make it invocable
Invocable invocable = ( Invocable ) engine;
// Invoke the struct's count() member method
Object result = invocable.invokeMethod( engine.get( "myStr" ), "count" );
assertThat( result ).isEqualTo( 1 );
```

This is indeed truly powerful as you can not only invoke functions on objects, but also member methods in any valid BoxLang type.

### Compiling Scripts

Apart from executing strings, you can also compile BoxLang scripts and evaluate them using the `compileScript( String ) or compileScript( Reader )` methods.  You will get a `Box CompiledScript` class, which you can then use the `eval()` methods and binding methods at a later point in time.

{% code lineNumbers="true" %}
```java
CompiledScript script = engine
		    .compile( """
			import ortus.boxlang.runtime.scopes.Key;

			name = [ 'John', 'Doe',  Key.of( 'test' ) ]
			name.reverse()
		    """ );

// Execute it
Object results	= script.eval();
assertThat( ( Array ) results ).containsExactly( Key.of( "test" ), "Doe", "John" );
```
{% endcode %}

### Dynamic Interfaces

JSR223 also allows you to dynamically create interface proxies for any functions or classes you map in the dynamic language.  Let's say you want to create a nice BoxLang function that maps to a Java Runnable.  In our example, we will create the `run` function and then map that via JSR223 to the `Runnable` interface so we can execute it as a runnable object.

```java
engine.eval("""
	function run() {
		print('Hello, world! I am running from a thread.');
	}
""");

Invocable invocable = ( Invocable ) engine;
// Map our function to a Runnable class
Runnable runnable = invocable.getInterface( Runnable.class );
runnable.run();
```

As you can see from the sample above, you can use the `getInterface( class<?> )` method to map the evaluated code to any interface of your choosing.  Here are the two methods you can use for interfaces:

- `getInterface( Class<T> )` - Build a dynamic proxy from the evaluated function and the passed in class
- `getInterface( Object, Class<T> )` - Build a dynamic proxy from the passed in `Object` and the passed in class.

Let's finish this section with another example. Using a struct and anonymous functions, let's build a BoxLang virtual object and treat it as a `Runnable` interface.

```java
// Define a BoxLang struct with a `run` key that points to an
// anonymous function
engine.eval("""
  methods = {
    run : function() {
	print('Hello, world!');
    }
  }
""");
// cast it to invocable
Invocable invocable = ( Invocable ) engine;
// Get the interface from that object that map to a Runnable
Runnable runnable = invocable.getInterface( engine.get( "methods" ), Runnable.class );
// Run Forest Run!
runnable.run();
```

### Capturing Output

We have also added the capability for your host language to seed your own String Writers into the engine so you can capture output.  BoxLang can produce two types of output

1. **System output** - Bifs and components that send output to the `System.out`
2. **Buffer output -** A BoxLang request has an output String buffer that can be used to produce output which can be sent to console, web, etc.

```java
Writer oldWriter = engine.getContext().getWriter();
// Create my own writer
StringWriter	stringWriter	= new StringWriter();
// Talk to the engine's context and seed in the new writer
engine.getContext().setWriter( stringWriter );

// Execute some code that outputs to the system out
engine.eval("""
  println('Hello, world!')
""");

// Now let's get that output!
assertThat( stringWriter.toString().trim() ).isEqualTo( "Hello, world!" );

// Replace the old writer back!
engine.getContext().setWriter( oldWriter );
```

### Runtime Source Code

The runtime source code can be found here: [https://github.com/ortus-boxlang/BoxLang/tree/development/src/main/java/ortus/boxlang/runtime/scripting](https://github.com/ortus-boxlang/BoxLang/tree/development/src/main/java/ortus/boxlang/runtime/scripting)

We welcome any pull requests, testing, docs, etc.

## 🏭 Production Considerations

### Performance Optimization

```java
// Compile once, execute multiple times
ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );
CompiledScript compiled = ( ( Compilable ) engine ).compile( """
    function processOrder( order ) {
        // Complex business logic here
        return {
            processed: true,
            total: order.items.sum( "price" ),
            timestamp: now()
        }
    }
""" );

// Reuse compiled script for better performance
for ( Order order : orders ) {
    Bindings context = engine.createBindings();
    context.put( "order", order );

    Map result = ( Map ) compiled.eval( context );
    // Process result...
}
```

### Thread Safety

```java
// BoxLang scripting engines are thread-safe for compilation
// but each execution should use separate bindings
public class BoxLangProcessor {
    private final CompiledScript processor;

    public BoxLangProcessor() throws ScriptException {
        ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );
        this.processor = ( ( Compilable ) engine ).compile( loadScript() );
    }

    public Object process( Map<String, Object> data ) throws ScriptException {
        // Create fresh bindings for each execution
        Bindings bindings = processor.getEngine().createBindings();
        bindings.putAll( data );

        return processor.eval( bindings );
    }
}
```

### Error Handling

```java
try {
    Object result = engine.eval( boxlangCode, bindings );
    // Handle success
} catch ( ScriptException e ) {
    // BoxLang compilation or runtime error
    logger.error( "BoxLang script failed: " + e.getMessage(), e );

    // Get detailed error information
    if ( e.getCause() != null ) {
        logger.error( "Root cause: " + e.getCause().getMessage() );
    }

    // Line number information (if available)
    if ( e.getLineNumber() >= 0 ) {
        logger.error( "Error at line: " + e.getLineNumber() );
    }
}
```

## 🔗 Integration Patterns

### Spring Framework Integration

```java
@Configuration
public class BoxLangConfig {

    @Bean
    @Scope( "prototype" ) // New engine per injection
    public ScriptEngine boxLangEngine() {
        return new ScriptEngineManager().getEngineByName( "BoxLang" );
    }

    @Bean
    public BoxLangService boxLangService() {
        return new BoxLangService( boxLangEngine() );
    }
}

@Service
public class BoxLangService {
    private final ScriptEngine engine;

    public BoxLangService( ScriptEngine engine ) {
        this.engine = engine;
    }

    public Object executeTemplate( String template, Map<String, Object> variables ) {
        try {
            Bindings bindings = engine.createBindings();
            bindings.putAll( variables );
            return engine.eval( template, bindings );
        } catch ( ScriptException e ) {
            throw new RuntimeException( "Template execution failed", e );
        }
    }
}
```

### Maven Build Integration

```xml
<!-- pom.xml -->
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <version>3.1.0</version>
    <executions>
        <execution>
            <id>run-boxlang-scripts</id>
            <phase>generate-resources</phase>
            <goals>
                <goal>java</goal>
            </goals>
            <configuration>
                <mainClass>com.mycompany.BoxLangScriptRunner</mainClass>
                <arguments>
                    <argument>${project.basedir}/scripts/generate-config.bx</argument>
                </arguments>
            </configuration>
        </execution>
    </executions>
</plugin>
```

### Gradle Build Integration

```groovy
// build.gradle
task runBoxLangScripts( type: JavaExec ) {
    classpath = sourceSets.main.runtimeClasspath
    main = 'com.mycompany.BoxLangScriptRunner'
    args = [ 'scripts/data-processing.bx' ]
}

// Run BoxLang scripts during build
compileJava.dependsOn runBoxLangScripts
```
