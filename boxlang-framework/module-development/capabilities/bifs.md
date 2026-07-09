---
description: Create custom Built-In Functions (BIFs) in BoxLang or Java for your module
icon: function
---

# Built-In Functions (BIFs)

BIFs are custom functions that extend BoxLang's built-in function library. Create them in **pure BoxLang** or **Java**.

{% tabs %}
{% tab title="🟦 BoxLang BIFs" %}

Place `.bx` files in your module's `bifs/` folder. They are auto-discovered and compiled at runtime.

**File:** `bifs/Greet.bx`

```js
/**
 * Returns a greeting message
 *
 * @param name The name to greet (required)
 * @param greeting The greeting prefix (default: "Hello")
 *
 * @return The formatted greeting string
 */
function invoke(
    required string name,
    string greeting = "Hello"
) {
    return "#greeting#, #name#!"
}
```

**Usage from BoxLang:**
```js
result = greet( "World" )
// → "Hello, World!"

result = greet( name = "World", greeting = "Hi" )
// → "Hi, World!"
```

**Features:**
- ✅ No compilation — just create the file
- ✅ Auto-discovered by folder scanning
- ✅ Supports `@BoxMember` annotation for member methods
- ✅ Full access to BoxLang runtime via injected services

{% endtab %}

{% tab title="☕ Java BIFs" %}

Extend the `BIF` class and annotate with `@BoxBIF`. Registered via ServiceLoader.

**File:** `src/main/java/ortus/boxlang/modules/mymodule/bifs/Greet.java`

```java
import ortus.boxlang.runtime.bifs.BIF;
import ortus.boxlang.runtime.bifs.BoxBIF;
import ortus.boxlang.runtime.bifs.BoxMember;
import ortus.boxlang.runtime.context.IBoxContext;
import ortus.boxlang.runtime.scopes.ArgumentsScope;
import ortus.boxlang.runtime.scopes.Key;
import ortus.boxlang.runtime.types.Argument;
import ortus.boxlang.runtime.types.BoxLangType;

@BoxBIF
@BoxMember( type = BoxLangType.STRING )
public class Greet extends BIF {

    public Greet() {
        declaredArguments = new Argument[] {
            new Argument( true, Argument.STRING, Key.name ),
            new Argument( false, Argument.STRING, Key.greeting, "Hello" )
        };
    }

    @Override
    public Object _invoke( IBoxContext context, ArgumentsScope arguments ) {
        String name     = arguments.getAsString( Key.name );
        String greeting = arguments.getAsString( Key.greeting );
        return greeting + ", " + name + "!";
    }
}
```

**ServiceLoader Config:** `src/main/resources/META-INF/services/ortus.boxlang.runtime.bifs.BIF`

```
ortus.boxlang.modules.mymodule.bifs.Greet
```

**Features:**
- ✅ Compiled performance — no runtime compilation
- ✅ Full Java ecosystem access
- ✅ Better IDE tooling and type safety
- ✅ Can implement complex Java interfaces

{% endtab %}
{% endtabs %}

## Member Functions

Register BIFs as member methods on BoxLang types:

{% tabs %}
{% tab title="BoxLang" %}
```js
/**
 * @BoxMember string
 */
function shout( required string text ) {
    return text.ucase() & "!!!"
}
```

Usage: `"hello".shout()` → `"HELLO!!!"`
{% endtab %}

{% tab title="Java" %}
```java
@BoxBIF
@BoxMember( type = BoxLangType.STRING )
public class StringShout extends BIF {
    // ... implementation
}
```

Usage: `"hello".shout()` → `"HELLO!!!"`
{% endtab %}
{% endtabs %}

## When to Use Which

| Criteria | BoxLang BIFs | Java BIFs |
|----------|--------------|-----------|
| Complexity | Simple logic | Complex algorithms |
| Performance | Good for most cases | Critical paths |
| Dependencies | None or minimal | External JARs |
| Development speed | Fast iteration | Requires rebuild |
| Team skills | BoxLang developers | Java developers |

## Next Steps

- [Components](components.md) — Create custom BoxLang tags
- [Interceptors](interceptors.md) — Listen to runtime events
- [Services](services.md) — Global runtime services (Java only)
