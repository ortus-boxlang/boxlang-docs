---
description: Java scripting with BoxLang
---

# JSR-223 Scripting

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

* Script Factory - creates scripting engines and gets metadata about scripting engines.
* Script Engine - provides a way to create bindings, scripts, and run statements.
* Bindings - these are like scopes to BoxLang. The bridge between Java and BoxLang
* Scripting Context - Like the BoxLang context object, it provides scope lookups and access to bindings.

### Bindings

Bindings are under the hood `HashMaps`.  They are used to bind your Java code to the BoxLang code.  By default in BoxLang, we provide three scopes you can bind bindings to:

* `Global Scope` - The **default** scope which maps to the BoxLang `variables` scope
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

```java
import javax.script.*;

ScriptEngine engine = new ScriptEngineManager().getEngineByName( "BoxLang" );

// Or by Class

import ortus.boxlang.runtime.scripting.BoxScriptingFactory;

ScriptEngine engine = new BoxScriptingFactory().getScriptEngine();
```

### Eval() BoxLang Code

Once you get access to the script engine you can use the plethora of `eval()` methods to execute the BoxLang source and binding with specific bindings.  You can execute scripts from strings or reader objects.  You can also compile a script/class into a `CompiledScript` and then execute it.

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

Data can be passed into the engine by defining a _Bindings_ object and passing it as a second parameter to the _eval_ function:

```java
Bindings bindings = boxlang.createBindings();
bindings.put( "count", 3 );
bindings.put( "name", "luis" );
bindings.put( "age", 1 );

engine.eval( """
  println( 'Hello, ' & name & '!' )
  newAge = age + 1
  totalAge = newAge + 1
  request.nameTest = name
  server.nameTest = name
""", bindings );

// We cannot use the same bindings, these are just to send
// We need to get the bounded bindings now via the `getBindings()` method
Bindings resultBindings = engine.getBindings();
assertThat( result ).isEqualTo( "World" );
assertThat( modifiedBindings.get( "newAge" ) ).isEqualTo( 2 );
assertThat( engine.getRequestBindings().get( "nameTest" ) ).isEqualTo( "World" );
assertThat( engine.getServerBindings().get( "nameTest" ) ).isEqualTo( "World" );


```

{% hint style="warning" %}
Once you bind the engine with bindings before execution, you must get the modified bindings via the `engine.getBindings()` method.  If you don't do this, you will only have access to the simple hashmap to bind the engine.
{% endhint %}

### Compiling Scripts

Apart from executing strings, you can also compile BoxLang scripts and evaluate them using the `compileScript( String ) or compileScript( Reader )` methods.  You will get a `Box CompiledScript` class, which you can then use the `eval()` methods and binding methods.

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

Happy Coding!!



