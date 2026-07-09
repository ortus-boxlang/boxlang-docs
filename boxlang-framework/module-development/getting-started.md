---
description: Step-by-step guide to create your first BoxLang module using templates
icon: rocket
---

# Getting Started

Create your first BoxLang module in minutes using our official templates. Choose between pure BoxLang for rapid development or Java + BoxLang for full runtime integration.

## Pick Your Path

{% tabs %}
{% tab title="🟦 Pure BoxLang" %}

### 1. Clone the Template

```bash
git clone https://github.com/ortus-boxlang/boxlang-module-template-bx.git my-module
cd my-module
```

### 2. Customize Metadata

Edit `box.json` with your module details:

```json
{
  "name": "My Amazing Module",
  "version": "1.0.0",
  "slug": "bx-my-module",
  "shortDescription": "Does amazing things",
  "boxlang": {
    "minimumVersion": "1.0.0",
    "moduleName": "myModule"
  }
}
```

### 3. Configure ModuleConfig.bx

```js
class {
    property name="moduleRecord";
    property name="boxRuntime";
    property name="log";

    this.version     = "1.0.0";
    this.mapping     = "myModule";
    this.author      = "Your Name";
    this.description = "My amazing module";

    function configure() {
        settings = {
            loadedOn: now(),
            loadedBy: "Your Name"
        };

        interceptors = [];
        customInterceptionPoints = [];
    }

    function onLoad() {}
    function onUnload() {}
}
```

### 4. Add Your First BIF

Create `bifs/HelloWorld.bx`:

```js
/**
 * Returns a greeting message
 *
 * @param name The name to greet
 * @return Greeting string
 */
function invoke( required string name ) {
    return "Hello, #name#! Welcome to BoxLang modules."
}
```

### 5. Test Locally

```js
// Load the module
moduleService.loadModule(
    createObject( "java", "java.nio.file.Paths" ).get( "/path/to/my-module" )
)

// Use your BIF
result = helloWorld( "Developer" )
writeOutput( result )
```

**✅ Done!** No build step required — your module is ready to distribute.

{% endtab %}

{% tab title="☕ Java + BoxLang" %}

### 1. Clone the Template

```bash
git clone https://github.com/ortus-boxlang/boxlang-module-template.git my-module
cd my-module
```

### 2. Configure Module Metadata

Edit `box.json` and `gradle.properties`:

```json
{
  "name": "My Amazing Module",
  "version": "@build.version@+@build.number@",
  "slug": "bx-my-module",
  "shortDescription": "Does amazing things",
  "boxlang": {
    "minimumVersion": "1.14.0",
    "moduleName": "myModule"
  }
}
```

### 3. Create ModuleConfig.bx

Same as the pure BoxLang approach — place it at `src/main/bx/ModuleConfig.bx`:

```js
class {
    property name="moduleRecord";
    property name="boxRuntime";
    property name="log";

    this.version     = "@build.version@+@build.number@";
    this.mapping     = "myModule";
    this.author      = "Your Name";
    this.description = "My amazing module";

    function configure() {
        settings = {
            key: "value"
        };
    }

    function onLoad() {}
    function onUnload() {}
}
```

{% hint style="info" %}
You can also use a Java `IModuleConfig` class annotated with `@BoxModule` instead. Both ModuleConfig.bx and Java work — Java takes priority if both exist. See [Module Descriptor](module-descriptor.md).
{% endhint %}

### 4. Add a Java BIF

Create `src/main/java/ortus/boxlang/modules/mymodule/bifs/Greet.java`:

```java
@BoxBIF
public class Greet extends BIF {

    public Greet() {
        declaredArguments = new Argument[] {
            new Argument( true, Argument.STRING, Key.name )
        };
    }

    @Override
    public Object _invoke( IBoxContext context, ArgumentsScope arguments ) {
        String name = arguments.getAsString( Key.name );
        return "Hello, " + name + "! Welcome to BoxLang modules.";
    }
}
```

Register via ServiceLoader in `src/main/resources/META-INF/services/ortus.boxlang.runtime.bifs.BIF`:

```
ortus.boxlang.modules.mymodule.bifs.Greet
```

### 5. Build & Test

```bash
./gradlew build
./gradlew test
```

Output is in `build/module/` ready for distribution.

**✅ Done!** Your Java + BoxLang module is built and packaged.

{% endtab %}
{% endtabs %}

## Module Folder Structure

{% tabs %}
{% tab title="Pure BoxLang" %}
```
my-module/
├── box.json              # Module metadata
├── ModuleConfig.bx        # Module descriptor
├── bifs/                  # BoxLang BIFs
│   └── HelloWorld.bx
├── components/            # BoxLang components (tags)
│   └── MyTag.bx
├── interceptors/          # BoxLang interceptors
│   └── Listener.bx
├── libs/                  # External JARs
├── public/                # Static web assets
└── tests/                 # TestBox tests
```
{% endtab %}

{% tab title="Java + BoxLang" %}
```
my-module/
├── box.json
├── build.gradle
├── src/
│   ├── main/
│   │   ├── bx/                    # BoxLang source
│   │   │   ├── ModuleConfig.bx
│   │   │   ├── bifs/
│   │   │   └── components/
│   │   ├── java/ortus/boxlang/modules/mymodule/
│   │   │   ├── bifs/              # Java BIFs
│   │   │   ├── components/        # Java components
│   │   │   ├── services/          # Java services
│   │   │   └── interceptors/      # Java interceptors
│   │   └── resources/
│   │       └── META-INF/services/ # ServiceLoader config
│   └── test/
│       └── java/                  # JUnit tests
├── libs/                          # External JARs
├── public/                        # Static web assets
└── build/module/                  # Build output
```
{% endtab %}
{% endtabs %}

## Available Template Injections

When writing your `ModuleConfig.bx`, BoxLang automatically injects these properties:

| Property | Type | Purpose |
|----------|------|---------|
| `moduleRecord` | `ModuleRecord` | The module's registration record |
| `boxRuntime` | `BoxRuntime` | The BoxLang runtime singleton |
| `functionService` | `FunctionService` | Register/query BIFs |
| `componentService` | `ComponentService` | Register/query components |
| `interceptorService` | `InterceptorService` | Register/announce interceptors |
| `asyncService` | `AsyncService` | Async execution and futures |
| `schedulerService` | `SchedulerService` | Scheduled task management |
| `datasourceService` | `DatasourceService` | Datasource and JDBC |
| `cacheService` | `CacheService` | Cache store management |
| `log` | `BoxLangLogger` | Module-specific logger |

{% hint style="info" %}
All injected services are also available from `boxRuntime.getService( "ServiceName" )` if you need them outside of ModuleConfig.bx.
{% endhint %}

## Next Steps

- [Module Descriptor](module-descriptor.md) — Deep dive into `box.json` and `ModuleConfig.bx`
- [Architecture](architecture.md) — Understand module isolation and class loading
- [Capabilities](capabilities/) — Explore what modules can provide
