---
description: Create module interceptors to listen and react to BoxLang runtime events
icon: ear-listen
---

# Interceptors

Interceptors follow the Observer/Intercepting Filter pattern, letting your module react to runtime events. Create them in **pure BoxLang** or **Java**.

{% tabs %}
{% tab title="🟦 BoxLang Interceptors" %}

Register interceptors in your `ModuleConfig.bx` `configure()` method:

**ModuleConfig.bx:**
```js
function configure() {
    settings = {};

    // Register interceptors
    interceptors = [
        {
            class: "interceptors.RequestLogger",
            properties: {
                logHeaders: true,
                logBody: false
            }
        }
    ];

    // Declare custom interception points
    customInterceptionPoints = [
        "onBeforeGreeting",
        "onAfterGreeting"
    ];
}
```

**File:** `interceptors/RequestLogger.bx`

```js
class {
    property name="logHeaders";
    property name="logBody";

    function onRequestStart( event ) {
        log.info( "Request started!" )

        if ( logHeaders ) {
            log.debug( "Headers: #event.getData()#" )
        }
    }

    function onRequestEnd( event ) {
        log.info( "Request ended!" )
    }
}
```

{% endtab %}

{% tab title="☕ Java Interceptors" %}

Implement the `IInterceptor` interface and annotate listener methods with `@InterceptionPoint`:

**File:** `src/main/java/ortus/boxlang/modules/mymodule/interceptors/RequestLogger.java`

```java
import ortus.boxlang.runtime.interceptors.IInterceptor;
import ortus.boxlang.runtime.interceptors.InterceptionPoint;
import ortus.boxlang.runtime.events.BoxEvent;
import ortus.boxlang.runtime.types.IStruct;
import ortus.boxlang.runtime.types.Struct;

public class RequestLogger implements IInterceptor {

    @InterceptionPoint( BoxEvent.ON_REQUEST_START )
    public void onRequestStart( IStruct data ) {
        System.out.println( "Request started!" );
    }

    @InterceptionPoint( BoxEvent.ON_REQUEST_END )
    public void onRequestEnd( IStruct data ) {
        System.out.println( "Request ended!" );
    }
}
```

**ServiceLoader Config:** `META-INF/services/ortus.boxlang.runtime.interceptors.IInterceptor`

```
ortus.boxlang.modules.mymodule.interceptors.RequestLogger
```

{% endtab %}
{% endtabs %}

## Lambda Interceptors

Register inline closures as interceptors for quick event handling:

```js
function configure() {
    interceptors = [
        {
            class: ( event ) => {
                log.info( "Quick listener fired!" )
            },
            name: "QuickListener@myModule"
        }
    ];
}
```

## Custom Interception Points

Declare your own events that other code can listen to:

```js
function configure() {
    customInterceptionPoints = [
        "onBeforeGreeting",
        "onAfterGreeting"
    ];
}

// Announce from module code
function doGreeting( required string name ) {
    announce( "onBeforeGreeting", { name: name } )

    var greeting = "Hello, #name#!"

    announce( "onAfterGreeting", { name: name, greeting: greeting } )

    return greeting
}
```

## Listening to Lifecycle Events

Your `ModuleConfig.bx` is automatically registered as an interceptor, so you can add any event method directly:

```js
class {
    // Listen for other modules loading
    function postModuleLoad( event ) {
        var moduleName = event.getData().moduleName
        log.info( "Module loaded: #moduleName#" )
    }

    // Listen for runtime startup
    function onModuleServiceStartup( event ) {
        log.info( "All modules are ready!" )
    }
}
```

{% hint style="info" %}
Interceptor names follow the convention `ClassName@moduleName`. If not specified, it's auto-derived from the class name.
{% endhint %}

## Next Steps

- [Services](services.md) — Global runtime services (Java only)
- [Schedulers](schedulers.md) — Scheduled task management (Java only)
- [Advanced Collaboration](../advanced-collaboration.md) — System settings and class resolvers
