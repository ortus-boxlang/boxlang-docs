---
description: Configure it your way!
---

# Runtime Configuration

BoxLang has an installation-level configuration file that allows developers to adjust various settings from the compiler to default cache providers and runtime-wide data sources. You can adjust boxlang settings by placing a `config/boxlang.json` file in your BoxLang home directory.  By default, we create one for you once your execute the runtime for the first time.

{% hint style="info" %}
If you are running BoxLang within CommandBox, then the configuration file will be inside the server directory inside of CommandBox under `WEB-INF/boxlang/`.  You can also run the following command to see the server home directory:

```
server status property=serverHome
```
{% endhint %}

## Runtime Home Directory

By default, the BoxLang home directory is a `.boxlang/` directory inside your user's home directory. For instance, on a Ubuntu machine, this might be `/home/elpete/.boxlang/` if you are executing BoxLang under the `elpete` user account.

ℹ️ The BoxLang home can be adjusted on startup via a `--home` flag:

```bash
boxlang --home /path/to/boxlang-home
```

By allowing a custom home directory, you can manage multiple BoxLang runtimes and allow:

1. custom, per-runtime configuration
2. a custom set of BoxLang modules
3. etc, etc.

## Boxlang.json Reference

Here is a full reference of the current default `boxlang.json` file:

```json
/**
 * BoxLang Configuration File
 *
 * Here are some of the available variables you can use in this file:
 * ${boxlang-home} - The BoxLang home directory
 * ${user-home} - The user's home directory
 * ${user-dir} - The user's current directory
 * ${java-temp} - The java temp directory
 * ${env.variablename:defaultValue} - The value of a valid environment variable or the default value. Example: ${env.CFCONFIG_HOME:/etc/cfconfig}
 */
{
// Where all generated classes will be placed
"classGenerationDirectory": "${boxlang-home}/classes",
// This puts the entire runtime in debug mode
// Which will produce lots of debug output and metrics
// Also the debugging error template will be used if turned on
"debugMode": false,
// The default timezone for the runtime; defaults to the JVM timezone if empty
// Please use the IANA timezone database values
"timezone": "",
// The default locale for the runtime; defaults to the JVM locale if empty
// Please use the IETF BCP 47 language tag values
"locale": "",
// If true, you can call implicit accessors/mutators on object properties. By default it is enabled
// You can turn it on here for all applications or in the Application.cfc
"invokeImplicitAccessor": true,
// Use Timespan syntax: "days, hours, minutes, seconds"
"applicationTimeout": "0,0,0,0",
// The request timeout for a request in seconds; 0 means no timeout
"requestTimeout": "0,0,0,0",
// The session timeout: 30 minutes
"sessionTimeout": "0,0,30,0",
// Where sessions will be stored by default.  This has to be a name of a registered cache
// or the keyword "memory" to indicate our auto-created cache.
// This will apply to ALL applications unless overridden in the Application.cfc
"sessionStorage": "memory",
// A collection of BoxLang mappings, the key is the prefix and the value is the directory
"mappings": {
	"/": "${user-dir}"
},
// A collection of BoxLang module directories, they must be absolute paths
"modulesDirectory": [
	"${boxlang-home}/modules"
],
// A collection of BoxLang custom tag directories, they must be absolute paths
"customTagsDirectory": [
	"${boxlang-home}/customTags"
],
// A collection of directories we will class load all Java *.jar files from
"javaLibraryPaths": [
	"${boxlang-home}/lib"
],
// The location of the log files the runtime will produce
"logsDirectory": "${boxlang-home}/logs",
// You can assign a global default datasource to be used in the language
"defaultDasource": "",
// The registered global datasources in the language
// The key is the name of the datasource and the value is a struct of the datasource settings
"datasources": {
	// "testDB": {
	// 	  "driver": "derby",
	//    "connectionString": "jdbc:derby:memory:testDB;create=true"
	// }
	// "testdatasource": {
	// 	  "driver": "derby",
	// 	  "host": "localhost",
	// 	  "port": 3306,
	// 	  "database": "test"
	// }
},
// The configuration for the BoxLang `default` cache.  If empty, we use the defaults
// See the ortus.boxlang.runtime.config.segments.CacheConfig for all the available settings
// This is used by query caching, template caching, and other internal caching, unless you override it
"defaultCache": {},
/**
* Register any named caches here.
* The key is the name of the cache and the value is the cache configuration.
*
* A `provider` property is required and the value is the name of the cache provider or the fully qualified class name.
* The `properties` property is optional and is a struct of properties that are specific to the cache provider.
*/
"caches": {
	"imports": {
		"provider": "BoxCacheProvider",
		"properties": {
			"evictCount": 1,
			"evictionPolicy": "LRU",
			"freeMemoryPercentageThreshold": 0,
			"maxObjects": 200,
			"defaultLastAccessTimeout": 1800,
			"defaultTimeout": 3600,
			"objectStore": "ConcurrentStore",
			"reapFrequency": 120,
			"resetTimeoutOnAccess": false,
			"useLastAccessTimeouts": true
		}
	}
},
/**
 * The BoxLang module settings
 * The key is the module name and the value is a struct of settings for that specific module
 * The `disabled` property is a boolean that determines if the module should be enabled or not
 * The `settings` property is a struct of settings that are specific to the module and will be override the module settings
 */
"modules": {
	// The Compat Module
	// "compat": {
	// 	"disabled": false,
	// 	"settings": {
	// 		"isLucee": true,
	// 		"isAdobe": true
	// 	}
	// }
}
}

```

## Internal Variables

The following are the internal variable substitutions you can use in any value:

```
 * ${boxlang-home} - The BoxLang home directory
 * ${user-home} - The user's home directory
 * ${user-dir} - The user's current directory
 * ${java-temp} - The java temp directory
```

## Environment Variable Substitution

BoxLang supports environment variable substitution using the syntax `${env.environment_variable_name}:default}`. For example, using `${env.MYSQL_HOST:localhost}` will result in the value of the `MYSQL_HOST` environment variable, if found, or fall back to the `localhost` value if the environment variable is not defined.

Inside your `boxlang.json` configuration file, you can use this to populate datasource credential secrets:

```json
{
    // ...
    "datasources": {
        "mySqlServerDB": {
            driver: "mssql",
            host: "localhost",
            port: "${env.MSSQL_PORT:1433}",
            database: "myDB",
            username: "${env.MSSQL_USERNAME:sa}",
            password: "${env.MSSQL_PASSWORD:123456Password}"
        }
    },
    
}
```
