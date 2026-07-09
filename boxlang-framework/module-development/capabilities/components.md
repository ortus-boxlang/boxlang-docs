---
description: Create custom BoxLang components (tags) using BoxLang or Java
icon: cube
---

# Components (Tags)

Components are BoxLang's equivalent of XML-style tags (`bx:mytag`). Create them in **pure BoxLang** or **Java**.

{% tabs %}
{% tab title="🟦 BoxLang Components" %}

Place `.bx` files in your module's `components/` folder. Auto-discovered at runtime.

**File:** `components/Greet.bx`

```js
/**
 * A custom greeting component
 *
 * @attr name The name to greet (required)
 * @attr greeting The greeting prefix (default: "Hello")
 */
class {

    property name="name"     type="string";
    property name="greeting" type="string" default="Hello";

    /**
     * This method is invoked when the component is used
     * in template mode (with a body) or inline mode
     */
    function invoke(
        required any processor,
        required struct context,
        required struct attributes
    ) {
        var message = "#attributes.greeting#, #attributes.name#!";

        // Output the message
        processor.getOutputBuffer().append( message );

        // Process body content if any
        if ( !isNull( processor.getBody() ) ) {
            processor.processBody();
        }
    }
}
```

**Usage:**
```xml
<bx:greet name="World" greeting="Hi" />
<bx:greet name="World">
    <p>Additional content here</p>
</bx:greet>
```

{% endtab %}

{% tab title="☕ Java Components" %}

Extend `Component` and annotate with `@BoxComponent`. Registered via ServiceLoader.

**File:** `src/main/java/ortus/boxlang/modules/mymodule/components/Greet.java`

```java
import ortus.boxlang.runtime.components.Attribute;
import ortus.boxlang.runtime.components.BoxComponent;
import ortus.boxlang.runtime.components.Component;
import ortus.boxlang.runtime.components.Component.BodyResult;
import ortus.boxlang.runtime.context.IBoxContext;
import ortus.boxlang.runtime.scopes.Key;
import ortus.boxlang.runtime.types.IStruct;

@BoxComponent
public class Greet extends Component {

    public Greet() {
        declaredAttributes = new Attribute[] {
            new Attribute( Key.name, "string" ),
            new Attribute( Key.greeting, "string", "Hello" )
        };
    }

    @Override
    public BodyResult _invoke(
        IBoxContext context,
        IStruct attributes,
        ComponentBodyProxy body,
        IStruct data
    ) {
        String name     = attributes.getAsString( Key.name );
        String greeting = attributes.getAsString( Key.greeting );

        print( context, greeting + ", " + name + "!" );

        return processBody( context, body );
    }
}
```

**ServiceLoader Config:** `META-INF/services/ortus.boxlang.runtime.components.Component`

```
ortus.boxlang.modules.mymodule.components.Greet
```

{% endtab %}
{% endtabs %}

## Script-Style Usage

Components can also be invoked in script syntax:

```js
bx:greet name="World" greeting="Hi"

// With a body block
bx:greet name="World" {
    writeOutput( "<p>Extra content</p>" )
}
```

## Naming Convention

All components use the `bx:` prefix:
- Module component named `Greet` → `<bx:greet>`
- Module component named `DataTable` → `<bx:datatable>`

Component names are case-insensitive in markup.

## Next Steps

- [BIFs](bifs.md) — Create custom built-in functions
- [Interceptors](interceptors.md) — Listen to runtime events
- [Services](services.md) — Global runtime services (Java only)
