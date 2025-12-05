---
description: Configure it your way!
icon: wrench-simple
---

# Runtime Configuration

BoxLang has an installation-level configuration file that allows developers to adjust various settings from the compiler to default cache providers, runtime-wide data sources, and much more.  Depending on which runtime you are using, the configuration file location might change, but the configuration segments remain  the same.

<table><thead><tr><th width="237">Runtime</th><th>Default Config Location</th></tr></thead><tbody><tr><td><strong>AWS Lamba</strong></td><td><code>{lambdaRoot}/boxlang.json</code></td></tr><tr><td><strong>Operating System</strong></td><td><code>~/.boxlang/config/boxlang.json</code></td></tr><tr><td><strong>MiniServer</strong></td><td><code>~/.boxlang/config/boxlang.json</code></td></tr><tr><td><strong>CommandBox</strong></td><td><code>~/.commandbox/servers/{serverHome}/WEB-INF/boxlang/config/boxlang.json</code></td></tr></tbody></table>

{% hint style="info" %}
All runtimes allow for configuration overrides.
{% endhint %}

### boxlang.json

Once you startup a runtime, the runtime will find the `BOXLANG_HOME`and create the `config/boxlang.json`file with the defaults that it ships with.  You may also change the granular config settings at runtime using the environment or Java properties by prefixing any configuration item with `BOXLANG_`or `boxlang.`  See below.

{% hint style="info" %}
If you are running BoxLang within CommandBox, the configuration file will be inside the server directory inside of CommandBox under `WEB-INF/boxlang/`. You can also run the following command to see the server home directory:

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
3. etc

## Boxlang.json Reference

Here is the latest reference of the current default `boxlang.json` file:

> [https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/resources/config/boxlang.json](https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/resources/config/boxlang.json)

{% @github-files/github-code-block url="https://github.com/ortus-boxlang/BoxLang/blob/development/src/main/resources/config/boxlang.json" %}

{% hint style="success" %}
Please note that JSON support in BoxLang allows you to use comments inline.
{% endhint %}

## Internal Variables

The following are the internal variable substitutions you can use in any value:

```json
 * ${boxlang-home} - The BoxLang home directory
 * ${user-home} - The user's home directory
 * ${user-dir} - The user's current directory
 * ${java-temp} - The java temp directory
```

Here is an example:

```json
"classGenerationDirectory": "${boxlang-home}/classes",
```

## Environmental/Properties Configuration

BoxLang gives you the ability to override any of the runtime configuration or module settings via environment variables or Java system properties.  For example adding an environment variable of `boxlang.security.allowedFileOperationExtensions=.exe,.sh`  would override the disallowed defaults, and allow users to upload and rename files with these extensions ( not a good idea! ).  &#x20;

The variable names can be either snake-cased or dot-delimited.  For example `BOXLANG_DEBUGMODE=true`  will work the same as `boxlang.debugMode=true`  to set the entire runtime in to debug mode. &#x20;

This convention allows  you to make granular changes to sub-segments of the configuration without overriding parent items.   JSON is also allowed when overriding config settings.  For example, if I wanted to set the runtime logging level to trace without putting the runtime in to DebugMode, I could set the environment variable: `boxlang.logging.loggers.runtime.level=TRACE`  or add the JVM arg `-Dboxlang.logging.loggers.runtime.level=TRACE`

### Environment Variable Substitution

BoxLang supports environment variable substitution using the syntax `${env.environment_variable_name:default}`. For example, using `${env.MYSQL_HOST:localhost}` will result in the value of the `MYSQL_HOST` environment variable, if found, or fall back to the `localhost` value if the environment variable is not defined.

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

## Configuration Segments

Here, you will find each segment and its configuration details.

{% content-ref url="configuration/directives.md" %}
[directives.md](configuration/directives.md)
{% endcontent-ref %}

{% content-ref url="configuration/caches.md" %}
[caches.md](configuration/caches.md)
{% endcontent-ref %}

{% content-ref url="configuration/datasources.md" %}
[datasources.md](configuration/datasources.md)
{% endcontent-ref %}

{% content-ref url="configuration/experimental.md" %}
[experimental.md](configuration/experimental.md)
{% endcontent-ref %}

{% content-ref url="configuration/executors.md" %}
[executors.md](configuration/executors.md)
{% endcontent-ref %}

{% content-ref url="configuration/logging.md" %}
[logging.md](configuration/logging.md)
{% endcontent-ref %}

{% content-ref url="configuration/modules.md" %}
[modules.md](configuration/modules.md)
{% endcontent-ref %}

{% content-ref url="configuration/scheduler.md" %}
[scheduler.md](configuration/scheduler.md)
{% endcontent-ref %}

{% content-ref url="configuration/security.md" %}
[security.md](configuration/security.md)
{% endcontent-ref %}
