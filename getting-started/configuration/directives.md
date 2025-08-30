---
description: These are the global configuration settings for the runtime
icon: bolt-lightning
---

# Directives

Below, you can find all the configuration directives the language supports.

{% hint style="warning" %}
These directives will be placed in the `boxlang.json`file at the root level:

{% code title="boxlang.json" %}
```
{
    "directive": value
}
```
{% endcode %}
{% endhint %}



### Application Timeout

The default timeout for applications in BoxLang. The default is **0 = never expires**. The value must be a string timespan using the syntax shown:

```json
// Use Timespan syntax: "days, hours, minutes, seconds"
"applicationTimeout": "0,0,0,0",
```

### Class Generation Directory

This is the location where BoxLang will store compiled classes.

```json
"classGenerationDirectory": "${boxlang-home}/classes"
```

### Class Paths

BoxLang allows you to register global locations where we can discover BoxLang classes (.bx files). These must be absolute paths or use variable substitutions.

```json
// A collection of directories to lookup box classes in (.bx files), they must be absolute paths
"classPaths": [
	"${boxlang-home}/global/classes"
]
```

### Class Resolver Cache

This enables the class locations cache for the runtime, used when resolving class paths, mappings, and per-request mappings. This is recommended for production environments.

```json
// This enables the class locations cache for the runtime.  It's used when resolving class paths
// mostly using mappings, per request mappings, etc.
// We recommend you always enable this setting, unless debugging a very specific issue
"classResolverCache": true
```

### Clear Class Files On Startup

This setting will remove all class files from the class generation directory on startup. Useful for debugging and testing, but not recommended for production.

```json
// This setting if enabled will remove all the class files from the class generation directory
// This is useful for debugging and testing, but not recommended for production
"clearClassFilesOnStartup": false
```

### Custom Components Directory

BoxLang allows you to register global locations where we can register custom components for use in your templates:

```json
// A collection of BoxLang custom components directories, they must be absolute paths
"customComponentsDirectory": [
	"${boxlang-home}/global/components"
]
```

### Default Datasource

The name of the default datasource to use for database operations when no datasource is explicitly specified.

```json
"defaultDatasource": ""
```

### Max Tracked Completed Threads

The maximum number of completed threads to track for a single request. This prevents memory issues by flushing old completed threads.

```json
// The maximum number of completed threads to track for a single request. Old threads will be flushed out to prevent memory from filling.
// This only applies to the "thread" component bx:thread name="mythread" {} which tracks execution status and scopes for the remainder of the request that fired it.
// ONLY threads which have been completed will be eligible to be flushed.
// Note: when the limit is reached, the thread component and related BIFs will no longer throw exceptions on invalid thread names, they will silently ignore attempts to interrupt or join those threads
"maxTrackedCompletedThreads": 1000
```

### Trusted Cache

This enables the runnable loader's cache on disk for compiled BoxLang classes. When enabled, BoxLang will load a class and never inspect the file again. Enable for production, disable for development.

```json
// This enables the runnable loader's cache on disk for compiled BoxLang classes
// This means that it will load a Boxlang class and never inspect the file again
// Turn this on for production, but off for development so you can see your changes
"trustedCache": false
```

### Version

The version of the BoxLang runtime (automatically populated during build).

```json
// The version of the runtime
"version": "@build.version@"
```

### Whitespace Compression

Enable whitespace compression in output. Currently only used by web runtimes.

```json
// Enable whitespace compression in output.  Only in use by the web runtimes currently.
"whitespaceCompressionEnabled": true
```

### Debug Mode

This is a powerful setting. It puts the runtime into debug mode, where more verbose debugging will be activated, and when exceptions occur, more information will be shown by default. The default is `false` an we highly discourage its use in production.

```json
// This puts the entire runtime in debug mode
// Which will produce lots of debug output and metrics
// Also the debugging error template will be used if turned on
"debugMode": false,
```



### Default Datasource

The name of the default datasource to use for database operations when no datasource is explicitly specified.

```json
"defaultDatasource": ""
```

You can set this to the name of any datasource defined in the `datasources` configuration section. See the [Datasources](datasources.md) section for more details.

### Default Remote Method Return Format

The default return format for class invocations via web runtimes.

```json
// The default return format for class invocations via web runtimes
"defaultRemoteMethodReturnFormat": "json",
```

### Invoke Implicit Accessors

In BoxLang, implicit accessors default to `true` for BoxScript (.bx) files and `false` for CFML (.cfc) files. This means that properties on a class can be accessed externally, like field properties for mutation or access. You can override this default behavior by setting this configuration option.

```json
"invokeImplicitAccessor": true
```

{% hint style="info" %}
This setting is not present in the default `boxlang.json` as BoxLang uses intelligent defaults based on the source file type. Add this setting only if you want to override the default behavior.
{% endhint %}

Simple example:

```js
// Class has implicit accessors and mutators by default in BoxLang (.bx files)
class{
    property firstName
    property lastName
    property email
}

// Example
p = new Person()
// This calls the generated setters in the class
p.firstName = "luis"
p.lastname = "majano"
p.email = "info@boxlang.io"
// This calls the generated getters in the class
println( p.firstName );
```

### Java Library Paths

BoxLang allows you to register an array of locations or array of jars or classes that the runtime will class load into the runtime class loader. This allows you to class-load Java applications at runtime.

```json
// A collection of directories we will class load all Java *.jar files from
"javaLibraryPaths": [
	"${boxlang-home}/lib"
],
```

By default, we look into the `lib` folder in your BoxLang home.

### Locale

This is the default locale for the runtime. By default, we use the JVM locale. This value must be an IETF BCP language tag: [https://www.oracle.com/java/technologies/javase/jdk21-suported-locales.html](https://www.oracle.com/java/technologies/javase/jdk21-suported-locales.html)

```json
// The default locale for the runtime; defaults to the JVM locale if empty
// Please use the IETF BCP 47 language tag values
"locale": "es_sv",

// You can also use hypens
"locale": "es-sv",

// Or just the first part
"locale": "es",
```

### Mappings

Here is where you can create global class mappings in BoxLang. The value is a JSON object where the key is the name of the mapping, and the value is the absolute path location of the mapping. You can prefix the name of the mapping with `/` or not. Ultimately, we will add it for you as well.

```json
// A collection of BoxLang mappings, the key is the prefix and the value is the directory
"mappings": {
	"/": "${user-dir}",
	"/core" : "/opt/core"
},
```

Mappings are used to discover BoxLang classes, files and more.

### Modules Directory

BoxLang will search your home for a `modules` folder and register the modules found. However, you can add multiple locations to search for BoxLang modules. Each entry must be an absolute location.

```json
// A collection of BoxLang module directories, they must be absolute paths
"modulesDirectory": [
    "${boxlang-home}/modules"
],
```

### Request Timeout

The default timeout for requests in BoxLang. The default is 0 = never expire. The value must be a string timespan using the syntax shown:

```json
// Use Timespan syntax: "days, hours, minutes, seconds"
"requestTimeout": "0,0,0,0",
```

### Session Timeout

The default timeout for sessions in BoxLang. The default is 30 minutes. The value must be a string timespan using the syntax shown:

```json
// Use Timespan syntax: "days, hours, minutes, seconds"
"sessionTimeout": "0,0,30,0",
```

### Session Storage

In BoxLang, you can configure your user sessions to be stored in `memory` by default in a BoxLang sessions cache, or you can give it a custom cache name to store them in. If it's not `memory`\` then it must be a valid registered cache. (See [Caches](directives.md#caches))

```json
// Where sessions will be stored by default.  This has to be a name of a registered cache
// or the keyword "memory" to indicate our auto-created cache.
// This will apply to ALL applications unless overridden in the Application.cfc
"sessionStorage": "redis",
```

### Timezone

This is the global timezone to use in the runtime. By default, it will use the JVM timezone. This value requires IANA timezone database values: [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones#List](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)

```json
"timezone": "UTC"
```

### Use High Precision Math

By default BoxLang uses high-precision mathematics via `BigDecimal` operations. It analyses your operations and determines the precision accordingly. You can turn this off here for all applications and use Double based operations. If you disable this feature, then if you want high precision you will have to use the `precisionEvaluate( expression )` [BIF instead](../../boxlang-language/reference/built-in-functions/math/PrecisionEvaluate.md).

```json
// By default BoxLang uses high-precision mathematics via BigDecimal operations
// You can turn this off here for all applications
"useHighPrecisionMath": true,
```

### Valid Class Extensions

This is an array of all the extensions that will be processed as BoxLang classes. By default we target `bx, cfc`.

```json
// Extensions BoxLang will process as classes
"validClassExtensions": [
	"bx",
	// Moving to compat at final release
	"cfc"
],
```

### Valid Template Extensions

This is an array of all the extensions that will be processed as BoxLang templates. Meaning you can execute them and include them.  The core template extensions are `bxm, bxs, bxml, cfml, cfm, cfs` and are always available.  Here you can add other extensions that will process as templates.

```json
// Extensions BoxLang will process as templates.
// This is used by the RunnableLoader
"validTemplateExtensions": [],
```
