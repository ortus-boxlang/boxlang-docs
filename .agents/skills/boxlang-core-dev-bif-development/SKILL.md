---
name: boxlang-core-dev-bif-development
description: "Use this skill when creating custom BoxLang built-in functions (BIFs): @BoxBIF annotation, invoke() method, argument handling, accessing BoxRuntime and services, BoxLang vs Java BIF implementations, member functions, and registering BIFs via modules."
---

# BoxLang BIF Development

## Overview

Built-in functions (BIFs) are globally available functions in BoxLang — no imports
needed. When placed in a module's `bifs/` directory, they are automatically
discovered and registered at module load time. BIFs can be implemented in either
BoxLang or Java.

## BoxLang BIF

### Minimal Example

```boxlang
// bifs/Greet.bx
// File name = function name (case-insensitive: greet, Greet, GREET all work)

@BoxBIF
class {

    function invoke( required string name ) {
        return "Hello, #arguments.name#!"
    }

}
```

```boxlang
// Usage anywhere in BoxLang (no import)
greet( "Ada" )   // "Hello, Ada!"
```

### Full-Featured BoxLang BIF

```boxlang
// bifs/StringTitleCase.bx
@BoxBIF
class {

    /**
     * Converts a string to title case.
     *
     * @str The input string
     * @delimiters Word delimiters (default: space)
     * @return Title-cased string
     */
    string function invoke(
        required string str,
        string delimiters = " "
    ) {
        if ( !len( arguments.str ) ) return ""

        var words = listToArray( arguments.str, arguments.delimiters )
        return words
            .map( (w) -> uCase( left(w,1) ) & lCase( mid(w,2,len(w)) ) )
            .toList( arguments.delimiters )
    }

}
```

## Java BIF

For performance-critical functions or when you need deep JVM access:

```java
// src/main/java/com/example/bifs/StringTitleCase.java
package com.example.bifs;

import ortus.boxlang.runtime.bifs.BIF;
import ortus.boxlang.runtime.bifs.BoxBIF;
import ortus.boxlang.runtime.bifs.BoxMember;
import ortus.boxlang.runtime.context.IBoxContext;
import ortus.boxlang.runtime.scopes.ArgumentsScope;
import ortus.boxlang.runtime.scopes.Key;
import ortus.boxlang.runtime.types.Argument;
import ortus.boxlang.runtime.types.BoxLangType;

@BoxBIF
// Optional: also register as a member function on String
@BoxMember( type = BoxLangType.STRING, name = "titleCase" )
public class StringTitleCase extends BIF {

    // Declare argument metadata
    public StringTitleCase() {
        super();
        declaredArguments = new Argument[] {
            new Argument( true,  "string", Key.of( "str" ) ),
            new Argument( false, "string", Key.of( "delimiters" ), " " )
        };
    }

    /**
     * @param context   Current execution context
     * @param arguments Function arguments scope
     */
    @Override
    public Object invoke( IBoxContext context, ArgumentsScope arguments ) {
        String str        = arguments.getAsString( Key.of( "str" ) );
        String delimiters = arguments.getAsString( Key.of( "delimiters" ) );

        if ( str == null || str.isEmpty() ) return "";

        String[] words = str.split( "[" + delimiters + "]" );
        StringBuilder sb = new StringBuilder();
        for ( int i = 0; i < words.length; i++ ) {
            if ( i > 0 ) sb.append( delimiters.charAt( 0 ) );
            if ( !words[i].isEmpty() ) {
                sb.append( Character.toUpperCase( words[i].charAt(0) ) );
                sb.append( words[i].substring(1).toLowerCase() );
            }
        }
        return sb.toString();
    }
}
```

With `@BoxMember`, the BIF is also callable as a member function:
```boxlang
"hello world".titleCase()  // "Hello World"
titleCase( "hello world" ) // "Hello World" (BIF style)
```

## Key Java Classes for BIF Development

| Class/Interface | Package | Purpose |
|---|---|---|
| `BIF` | `ortus.boxlang.runtime.bifs` | Base class for all BIFs |
| `@BoxBIF` | `ortus.boxlang.runtime.bifs` | Marks a class as a BIF |
| `@BoxMember` | `ortus.boxlang.runtime.bifs` | Registers as member function |
| `IBoxContext` | `ortus.boxlang.runtime.context` | Current execution context |
| `ArgumentsScope` | `ortus.boxlang.runtime.scopes` | Typed argument access |
| `Key` | `ortus.boxlang.runtime.scopes` | String key interning |
| `Argument` | `ortus.boxlang.runtime.types` | Argument descriptor |
| `BoxLangType` | `ortus.boxlang.runtime.types` | Enum of BoxLang types |
| `BoxRuntime` | `ortus.boxlang.runtime` | Runtime singleton |

## Accessing BoxRuntime Services From a BIF

```java
import ortus.boxlang.runtime.BoxRuntime;
import ortus.boxlang.runtime.cache.providers.ICacheProvider;
import ortus.boxlang.runtime.services.CacheService;

@BoxBIF
public class CachedFetch extends BIF {

    private BoxRuntime runtime = BoxRuntime.getInstance();

    @Override
    public Object invoke( IBoxContext context, ArgumentsScope arguments ) {
        String url = arguments.getAsString( Key.of( "url" ) );

        CacheService cacheService = runtime.getCacheService();
        ICacheProvider cache      = cacheService.getDefaultCache();

        Object cached = cache.get( Key.of( url ) );
        if ( cached != null ) return cached;

        // Fetch data...
        Object result = fetchFromUrl( url );
        cache.set( Key.of( url ), result, 300L, 0L );  // 300s TTL
        return result;
    }
}
```

## Accessing Context Services

```java
@Override
public Object invoke( IBoxContext context, ArgumentsScope arguments ) {
    // Get the current request scope
    IScope requestScope = context.getScopeNearby( RequestScope.name );

    // Get the application scope
    IScope appScope = context.getScopeNearby( ApplicationScope.name );

    // Get the session scope
    IScope sessionScope = context.getScopeNearby( SessionScope.name );

    // Resolve a variable
    Object val = context.scopeFindNearby( Key.of( "myVar" ), null ).value();

    // Invoke another function
    Object result = context.invokeFunction( Key.of( "len" ), new Object[]{ "hello" } );

    return result;
}
```

## BoxLang BIF with Runtime Access

```boxlang
// bifs/GetAppSetting.bx
@BoxBIF
class {

    function invoke( required string key, any defaultValue = "" ) {
        // Access the BoxRuntime
        var runtime  = boxRuntime
        var appScope = getApplicationScope()  // available in web context

        return appScope.keyExists( arguments.key )
            ? appScope[ arguments.key ]
            : arguments.defaultValue
    }

}
```

## Registering a BIF Alias

```java
// Register under multiple names via multiple @BoxBIF annotations
@BoxBIF
@BoxBIF( alias = "strTitleCase" )
@BoxBIF( alias = "toTitleCase" )
public class StringTitleCase extends BIF { ... }
```

## Member Function Registration

Member functions are BIFs callable on a specific type using dot notation:

```java
@BoxBIF
@BoxMember( type = BoxLangType.ARRAY,  name = "shuffle" )   // array.shuffle()
@BoxMember( type = BoxLangType.STRING, name = "toSlug" )    // str.toSlug()
@BoxMember( type = BoxLangType.STRUCT, name = "deepMerge" ) // struct.deepMerge()
public class MyBIF extends BIF { ... }
```

```boxlang
[3,1,2].shuffle()
"Hello World".toSlug()   // "hello-world"
config.deepMerge( overrides )
```

## BIF Argument Types

```java
// Argument types available in ortus.boxlang.runtime.types.Argument
new Argument( required, type, key )
new Argument( required, type, key, defaultValue )

// Types: "any", "string", "numeric", "boolean", "array", "struct",
//        "query", "date", "function", "closure", "lambda", "class"
```

## Testing Your BIF

```boxlang
// tests/specs/MyBIFTest.bx
class extends="testbox.system.BaseSpec" {

    function run() {
        describe( "greet BIF", function() {

            it( "should greet a person by name", function() {
                expect( greet("Ada") ).toBe( "Hello, Ada!" )
            })

            it( "should handle empty name", function() {
                expect( greet("") ).toBe( "Hello, !" )
            })

            it( "should be callable as member function", function() {
                expect( "Ada".titleCase() ).toBe( "Ada" )
                expect( "hello world".titleCase() ).toBe( "Hello World" )
            })

        })
    }

}
```

```bash
box testbox run
```

## Discovering Registered BIFs

```boxlang
// List all registered BIFs (including your custom ones)
writeDump( getFunctionList() )

// Check if a specific BIF exists
if ( structKeyExists( getFunctionList(), "greet" ) ) {
    writeOutput( "greet BIF is registered!" )
}
```

## References

- [BoxLang Source — Core BIFs](https://github.com/ortus-boxlang/BoxLang/tree/development/src/main/java/ortus/boxlang/runtime/bifs)
- [BIF Base Class](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/bifs/BIF.java)
- [BoxBIF Annotation](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/java/ortus/boxlang/runtime/bifs/BoxBIF.java)
- [Module Template](https://github.com/ortus-boxlang/boxlang-module-template)
