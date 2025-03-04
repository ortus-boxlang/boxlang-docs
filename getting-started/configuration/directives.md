---
icon: bolt-lightning
description: These are the global configuration settings for the runtime
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

### Custom Tags Directory

BoxLang allows you to register global locations where we can register custom tags for use in your templates:

```json
// A collection of BoxLang custom tag directories, they must be absolute paths
"customTagsDirectory": [
	"${boxlang-home}/customTags"
],
```

### Debug Mode

This is a powerful setting. It puts the runtime into debug mode, where more verbose debugging will be activated, and when exceptions occur, more information will be shown by default. The default is `false` an we highly discourage its use in production.

```json
// This puts the entire runtime in debug mode
// Which will produce lots of debug output and metrics
// Also the debugging error template will be used if turned on
"debugMode": false,
```



### Default Remote Method Return Format

The default return format for class invocations via web runtimes.

```json
// The default return format for class invocations via web runtimes
"defaultRemoteMethodReturnFormat": "json",
```

### Invoke Implicit Accessors

In BoxLang, the default for implicit accessors is `true`. This means that properties on a class can be accessed externally, like field properties for mutation or access.

```json
"invokeImplicitAccessor" : true
```

Simple example:

```cfscript
// Class has implicit accessors and mutators by default in BoxLang
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

This is an array of all the extensions that will be processed as BoxLang templates. Meaning you can execute them and include them.

```json
// Extensions BoxLang will process as templates.
// This is used by the RunnableLoader
"validTemplateExtensions": [
	"bxs",
	"bxm",
	"bxml",
	// Moving to compat at final release
	"cfm",
	"cfml",
	"cfs"
],
```
