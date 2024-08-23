---
description: Java scripting with BoxLang
icon: scroll
---

# JSR-223 Scripting

<figure><img src="../../.gitbook/assets/jsr-223.png" alt=""><figcaption></figcaption></figure>

### JSR 223 - Java Scripting

JSR 223, also known as "**Scripting for the Java Platform,**" is a specification that allows Java applications to integrate with scripting languages such as BoxLang, JavaScript, Groovy, Python, and others. It provides a standard API for accessing and embedding these scripting languages within Java code, enabling developers to mix and match Java and scripting languages seamlessly. This flexibility can enhance productivity and facilitate the rapid development of applications that require dynamic scripting capabilities.

{% embed url="https://www.oracle.com/technical-resources/articles/javase/scripting.html" %}

{% embed url="https://en.wikipedia.org/wiki/Scripting_for_the_Java_Platform" %}

BoxLang offers the JSR-233 runtime to integrate with BoxLang from any JVM language.

{% embed url="https://s3.amazonaws.com/apidocs.ortussolutions.com/boxlang/1.0.0/ortus/boxlang/runtime/scripting/package-summary.html" %}
API Docs
{% endembed %}

### Scripting Classes

The BoxLang scripting package can be found here: `ortus.boxlang.runtime.scripting`.  The classes that will assist you are:

* `BoxCompiledScript` - Implements the JSR `CompiledScript` interface ([https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/CompiledScript.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/CompiledScript.html))
* `BoxScopeBindings` - Implements the JSR `Bindings` interface ([https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/Bindings.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/Bindings.html))
* `BoxScriptingContext` - Implements the JSR `ScriptContext` interface ([https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptContext.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptContext.html))
* `BoxScriptingEngine` - Implements the JSR `ScriptEngine` and `Compilable` \
  [https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngine.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngine.html)\
  [https://docs.oracle.com/en/java/javase/17/docs/api//java.scripting/javax/script/Compilable.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/Compilable.html)
* `BoxScriptingFactory` - implements the JSR `ScriptEngineFactory` \
  [https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngineFactory.html](https://docs.oracle.com/en/java/javase/17/docs/api/java.scripting/javax/script/ScriptEngineFactory.html)

### Definitions

* **Script Factory** - creates scripting engines and gets metadata about scripting engines.
* **Script Engine** - provides a way to create bindings, scripts, and run statements.&#x20;
* **Invocable** - Our BoxLang engine also implements the scripting `Invocable` [interface](https://docs.oracle.com/en/java/javase/21/docs/api/java.scripting/javax/script/Invocable.html) so you can declare functions and classes (coming soon) and then execute them from the calling language.&#x20;
* **Bindings** - these are like scopes to BoxLang. The bridge between Java and BoxLang
* **Scripting Context** - Like the BoxLang context object, it provides scope lookups and access to bindings.

### Bindings

Bindings are under the hood `HashMaps`.  They are used to bind your Java code to the BoxLang code.  By default, in BoxLang, we provide three scopes you can bind bindings to:

* `Engine Scope` - The **default** scope which maps to the BoxLang `variables` scope
* `Request Scope` - The JSR request scope maps to the BoxLang `request` scope
* `Global Scope` - The JSR global scope maps to the BoxLang `server` scope

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

You can also cast it to our class to get enhanced methods and functionality

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

### Objects, Functions, Closures, Lambdas, Member Methods, Oh My!

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

* `getInterface( Class<T> )` - Build a dynamic proxy from the evaluated function and the passed in class
* `getInterface( Object, Class<T> )` - Build a dynamic proxy from the passed in `Object` and the passed in class.&#x20;

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
