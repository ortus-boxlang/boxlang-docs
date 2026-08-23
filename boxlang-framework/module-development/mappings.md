---
description: Understanding module mappings, class resolution, and the @moduleName notation
icon: route
---

# Mappings & Class Resolution

Every BoxLang module receives automatic mappings for class resolution and optional web access. Understanding these mappings is essential for importing classes and serving web content.

## Internal Module Mapping

When a module is registered, BoxLang creates an **internal mapping** for class resolution:

| Property | Value | Purpose |
|----------|-------|---------|
| **Path** | `bxModules.{moduleName}` | Internal class path prefix |
| **Physical** | Module root directory | Where classes/BIFs/components live |
| **Web Access** | ❌ No | Only for class resolution |

For a module named `myModule`, the internal mapping `bxModules.myModule` points to the module root. This is used for class resolution only — it's not web-accessible.

## Public Web Mapping

For serving static files via HTTP, BoxLang creates a **public mapping**:

| Property | Default | Customizable |
|----------|---------|--------------|
| **Folder** | `{moduleRoot}/public/` | ✅ `this.publicMapping` |
| **URL Path** | `/bxModules/{name}/public/` | ✅ Override mapping name |

Files in `myModule/public/css/style.css` are accessible at:

```
http://yourserver.com/bxModules/myModule/public/css/style.css
```

## Customizing Mappings

Override defaults in your module descriptor:

{% tabs %}
{% tab title="ModuleConfig.bx" %}
```js
class {
    // Override internal mapping name
    this.mapping = "customName";

    // Override public folder
    this.publicMapping = {
        name: "assets",           // URL: /bxModules/customName/assets/
        path: "web/static",       // Physical path relative to module root
        external: false           // true = absolute path
    };
}
```
{% endtab %}

{% tab title="Java @BoxModule" %}
```java
@BoxModule(
    mapping = @BoxMapping("customName"),
    publicMapping = @BoxMapping(
        name = "assets",
        path = "web/static",
        external = false
    )
)
public class MyModuleConfig implements IModuleConfig { }
```
{% endtab %}
{% endtabs %}

## The @moduleName Notation

BoxLang provides a powerful syntax for explicitly addressing classes from specific modules using the `@moduleName` suffix. This improves performance and eliminates ambiguity.

### Why Use @moduleName?

{% columns %}
{% column %}

**Without @moduleName:**
```js
import models.UserService
```

- BoxLang searches ALL modules
- Slower with many modules loaded
- Ambiguous if duplicates exist

{% endcolumn %}

{% column %}

**With @moduleName:**
```js
import models.UserService@myModule
```

- Direct lookup in the specified module
- Faster resolution
- No ambiguity
{% endcolumn %}
{% endcolumns %}

### Importing BoxLang Classes

```js
// Import from a specific module
import models.ActiveEntity@cborm
entity = new ActiveEntity()

// Import with alias
import models.ActiveEntity@cborm as AE
entity = new AE()

// Import component
import components.DataTable@bx-ui-forms
table = new DataTable()
```

### Importing Java Classes from Modules

The same notation works for Java classes packaged in modules:

```js
// Import Java class from module
import org.owasp.esapi.ESAPI@bx-esapi
encoder = ESAPI.encoder()

// Import with alias
import org.owasp.esapi.ESAPI@bx-esapi as SecurityAPI
encoder = SecurityAPI.encoder()

// Create instance directly
encoder = new java:org.owasp.esapi.reference.DefaultEncoder@bx-esapi()
```

### Using createObject()

```js
// Create BoxLang class from a module
service = createObject( "component", "models.UserService@myModule" )

// Create Java class from a module
driver = createObject( "java", "com.mysql.cj.jdbc.Driver@bx-mysql" )
```

{% hint style="warning" %}
The `@moduleName` notation requires the module to be **loaded and activated**. If the module isn't loaded, you'll get a class-not-found error.
{% endhint %}

## Class Loading Hierarchy

When resolving a class with `@moduleName`, BoxLang searches:

1. **Module's compiled classes** (`modules.{moduleName}` package prefix)
2. **Module's `libs/` folder** (JAR dependencies)
3. **Parent class loader** — for a module nested inside another, that is the containing module's loader, which then falls back to *its* parent, and so on up to the runtime class loader
4. **Runtime class loader** (BoxLang core classes — final fallback)

This isolation ensures modules don't interfere with each other's dependencies. A [nested module](module-inception.md) is the deliberate exception: it can see what its parent bundles, while staying isolated from its siblings.

## Custom Class Resolvers

Modules can register custom class resolvers with unique prefixes (extending the built-in `bx:` and `java:` resolvers). See [Advanced Collaboration](advanced-collaboration.md#custom-class-resolvers) for details.

## Best Practices

{% stepper %}
{% step %}
### Use @moduleName for Clarity

Always use `@moduleName` when importing classes from modules to avoid ambiguity and improve performance.

✅ `import models.UserService@myModule`
❌ `import models.UserService`

{% endstep %}

{% step %}
### Keep Public Folders Organized

Structure your `public/` folder logically:
```
public/
├── css/
├── js/
├── images/
└── templates/
```

{% endstep %}

{% step %}
### Document Your Mappings

In your module's README, document what mappings are created and how to import your classes.
{% endstep %}
{% endstepper %}

## Next Steps

- [Configuration](configuration.md) — Module settings and runtime overrides
- [Advanced Collaboration](advanced-collaboration.md) — System settings providers and class resolvers
- [Capabilities](capabilities/) — BIFs, components, services, and more
