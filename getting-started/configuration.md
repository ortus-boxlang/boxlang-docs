# Runtime Configuration

BoxLang has an installation-level configuration file which allows developers to adjust a wide range of settings from the compiler to default cache providers and runtime-wide datasources. You can adjust boxlang settings by placing a `config/boxlang.json` file in your BoxLang home directory.

## Runtime Home Directory

By default, the BoxLang home directory is a `.boxlang/` directory inside your user's home directory. For instance, on a Ubuntu machine this might be `/home/elpete/.boxlang/` if you are executing BoxLang under the `elpete` user account.

The BoxLang home can be adjusted on startup via a `--home` flag:

```bash
java -jar boxlang-1.0.0-all.jar --home /path/to/boxlang-home
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
 * The Available replacements are managed by the PlaceholderHelper class.
 * ${boxlang-home} - The BoxLang home directory
 * ${user-home} - The user's home directory
 * ${user-dir} - The user's current directory
 * ${java-temp} - The java temp directory
 * ${env.{variablename}:defaultValue} - The value of a valid environment variable or the default value
 */
{
    // This puts the entire runtime in debug mode
    // Which will produce lots of debug output and metrics
    "debugMode": false,
    // The BoxPiler settings
    "compiler": {
        // Where all generated classes will be placed
        "classGenerationDirectory": "${boxlang-home}/classes"
    },
    // The runtime settings
    "runtime": {
        // The default timezone for the runtime; defaults to the JVM timezone if empty
        // Please use the IANA timezone database values
        "timezone": "",
        // The default locale for the runtime; defaults to the JVM locale if empty
        // Please use the IETF BCP 47 language tag values
        "locale": "",
        // The request timeout for a request in milliseconds; 0 means no timeout
        "requestTimeout": 0,
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
        // You can assign a global default datasource to be used in the language
        "defaultDasource": "",
        // The registered global datasources in the language
        // The key is the name of the datasource and the value is a struct of the datasource settings
        "datasources": {
            // "testDB": {
            // 	"driver": "derby",
            // 	"connectionString": "jdbc:derby:memory:testDB;create=true"
            // }
            // "testdatasource": {
            // 	"driver": "mysql",
            // 	"host": "localhost",
            // 	"port": 3306,
            // 	"database": "test"
            // }
        },
        // The configuration for the BoxLang `default` cache.  If empty, we use the defaults
        "defaultCache": {},
        /**
		 * Register any named caches here.
		 * The key is the name of the cache and the value is the cache configuration.
		 * A `provder` property is required and the value is the name of the cache provider or the fully qualified class name.
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
        "compat": {
            "disabled": false,
            "settings": {
                "isLucee": true,
                "isAdobe": true
            }
        }
    }
}
```

## Environment Variable Substitution

BoxLang supports environment variable substitution by using the syntax `${env.{environment_variable_name}:default}`. For example, using `${env.MYSQL_HOST:localhost}` will result in the value of the `MYSQL_HOST` environment variable, if found, or fall back to the `localhost` value if the environment variable is not defined.

Inside your `boxlang.json` configuration file, you can use this to populate datasource credential secrets:

```json
{
    "runtime": {
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