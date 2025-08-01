---
icon: plug
---

# Datasources

A datasource is a **named** connection to a specific database with specified credentials. You can define a datasource in one of three locations:

1. [At the boxlang runtime level via your `boxlang.json` config file](datasources.md#defining-datasources-in-boxlang.json)
2. For web applications, [in your `Application.bx` via `this.datasources`](datasources.md#defining-datasources-in-applicationbx)
3. [Inline, at query time, via the `queryExecute()` BIF, `query` or `dbInfo` component, etc](datasources.md#defining-inline-datasources)

The datasource is then used to control the database's connection pool and allow the BoxLang engine to execute JDBC calls against it.

## What Database Vendors Are Supported?

The following database vendors are supported and available:

* [Apache Derby](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-derby/bx-derby-1.0.0.zip)
* [HyperSQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-hypersql/bx-hypersql-1.0.0.zip)
* [MariaDB](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mariadb/bx-mariadb-1.0.0.zip)
* [Microsoft SQL Server](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mssql/bx-mssql-1.0.0.zip)
* [MySQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mysql/bx-mysql-1.0.0.zip)
* [Oracle](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-oracle/bx-oracle-1.0.0.zip)
* [PostgreSQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-postgresql/bx-postgresql-1.0.0.zip)

Each database we support comes with an installable BoxLang module which either

1. provides the necessary client dependencies for making JDBC connections to a running database server (MySQL, Postgres, etc.)
2. OR contains the database vendor itself, as in the case of Apache Derby or HyperSQL, which are both in-memory database.

To use any of these databases you'll need to install its BoxLang module to support JDBC connections to that datasource.

## Make Sure to Specify a Driver

The datasource configuration struct should be defined exactly the same whether you are using an inline, ad-hoc datasource or configuring a datasource in your `boxlang.json` or `Application.bx`. Make sure you have a "driver" key defined OR the driver clearly denoted in the JDBC url:

{% code title="Application.bx" %}
```js
this.datasources[ "testDB" ] = {
	"driver": "mysql",
	// OR:
	"url" : "jdbc:mysql://localhost:3306/test"
};
```
{% endcode %}

## Defining Datasources In `boxlang.json`

You can define a datasource at the BoxLang runtime level by placing it in [your `boxlang.json` configuration file](../getting-started/configuration/):

{% code title="boxlang.json" %}
```js
  "datasources": {
      "theDerbyDB": {
      	"driver": "derby",
    	"connectionString": "jdbc:derby:memory:testDB;create=true"
      },
      "theMysqlDB": {
      	"driver": "mysql",
        "host": "${env.MYSQL_HOST:localhost}",
        "port": "${env.MYSQL_PORT:3306}",
        "database": "${env.MYSQL_DATABASE:myDB}",
        "username": "${env.MYSQL_USERNAME:root}",
        "password": "${env.MYSQL_PASSWORD}"
      }
  },
```
{% endcode %}

Note the use of BoxLang's environment variable replacement syntax for the datasource properties: `${env.MYSQL_HOST:localhost}`. See [Environment Variable Substitution](../getting-started/configuration.md#environment-variable-substitution) for more info.

## Defining Datasources In `Application.bx`

For web runtimes, you can also define the datasources in the `Application.bx`, which is sometimes our preferred approach as the connections are versioned controlled and more visible than in the admin. You will do this by defining a struct called `this.datasources`. Each **key** will be the name of the datasource to register and the **value** of each key a struct of configuration information for the datasource. However, we recommend that you setup environment variables in order to NOT store your passwords in plain-text in your source code.

{% code title="Application.bx" %}
```java
class{
    this.datasources = {
        // Driver Approach
        mysql = {
            database : "mysql",
            host : "localhost",
            port : "3306",
            driver : "MySQL",
            username : "root",
            password : "mysql",
            options : value
        },
        // URL approach
        mysql2 = {
            driver : "mysql",
            url : "jdbc:mysql://localhost:3306/test?useUnicode=true&characterEncoding=UTF-8&useLegacyDatetimeCode=true",
            username : "",
            password : ""
        },
        // Shorthand Approach
        myDSN = {
            class : "com.mysql.jdbc.Driver",
            connectionString : "jdbc:mysql://localhost:3306/test?useUnicode=true&characterEncoding=UTF-8&useLegacyDatetimeCode=true",
            username : "",
            password : ""
        },
        // Long Approach
        myDSN = {
            type : "mysql",
            database : "mysql",
            host : "localhost",
            port : "3306",
            username : "",
            password : ""
        }
    };
}
```
{% endcode %}

{% hint style="success" %}
For the inline approach, you will use the struct definition, as you see in the `Application.bx` above and pass it into the `bx:query` or `queryexecute` call.
{% endhint %}

## Defining Inline Datasources

Finally, for smaller or simpler applications with few queries, you may find it useful to define your datasource at query time. So instead of giving the name of the `datasource`, it can be a `struct` definition of the datasource you want to connect to:

```js
queryExecute(
  "SELECT * FROM Employees WHERE empid = ? AND country = ?", // sql
  [ 1, "USA" ], // params
  { // options
    datasource : {
      "driver": "mysql",
      "host": "${env.MYSQL_HOST:localhost}",
      "port": "${env.MYSQL_PORT:3306}",
      "database": "${env.MYSQL_DATABASE:myDB}",
      "username": "${env.MYSQL_USERNAME:root}",
      "password": "${env.MYSQL_PASSWORD}"
    }
  }
)
```

## Default Datasource

You can also define a default datasource to allow you to omit the `datasource` completely from query calls.

To do this, you'll need to define a default datasource in one of two locations:

1. In [your BoxLang runtime's `boxlang.json` config file](../getting-started/configuration/) via the `defaultDatasource` key
2. or, for web server runtimes, in a `this.datasource` variable in your `Application.bx` file

### Defining a default datasource via boxlang.json

{% code title="boxlang.json" %}
```json
   "defaultDatasource: {
      "driver": "mysql",
       "host": "${env.MYSQL_HOST:localhost}",
       "port": "${env.MYSQL_PORT:3306}",
       "database": "${env.MYSQL_DATABASE:myDB}",
       "username": "${env.MYSQL_USERNAME:root}",
       "password": "${env.MYSQL_PASSWORD}"
    },
   "datasources": {
      // You can still define additional datasources here! You're not limited to the default datasource
   },
```
{% endcode %}

### Defining a default datasource via Application.bx

{% code title="Application.bx" %}
```java
class{
    this.name = "myApp";

    // Default Datasource Name
    this.datasource = "pantry";

}
```
{% endcode %}

## Portable Datasources

You can also make your data sources portable from application to application or BoxLang engine to engine by using our [CFConfig](https://cfconfig.ortusbooks.com/) project. CFConfig allows you to manage almost every setting that shows up in the web administrator, but instead of logging into a web interface, you can manage it from the command line by hand or as part of a scripted server setup. You can seamlessly transfer config for all the following:

* CF Mappings
* Data sources
* Mail servers
* Request, session, or application timeouts
* Licensing information
* Passwords
* Template caching settings
* Basically any settings in the web based administrator

You can easily place a `.cfconfig.json` in the web root of your project, and if you start up a CommandBox server on any BoxLang engine, CFConfig will transfer the configuration to the engine's innards:

{% code title=".cfconfig.json" %}
```java
{
    "requestTimeoutEnabled":true,
    "whitespaceManagement":"white-space-pref",
    "requestTimeout":"0,0,5,0",
    "cacheDefaultObject":"coldbox",
    "caches":{
        "coldbox":{
            "storage":"true",
            "type":"RAM",
            "custom":{
                "timeToIdleSeconds":"1800",
                "timeToLiveSeconds":"3600"
            },
            "readOnly":"false"
        }
    },
    "datasources" : {
         "coldbox":{
             "host":"${DB_HOST}",
             "dbdriver":"${DB_DRIVER}",
             "database":"${DB_DATABASE}",
             "dsn":"jdbc:mysql://{host}:{port}/{database}",
             "custom":"useUnicode=true&characterEncoding=UTF-8&useLegacyDatetimeCode=true&autoReconnect=true",
             "port":"${DB_PORT}",
             "class":"${DB_CLASS}",
             "username":"${DB_USER}",
             "password":"${DB_PASSWORD}",
             "connectionLimit":"100",
             "connectionTimeout":"1"
         }
    }
}
```
{% endcode %}

{% embed url="https://cfconfig.ortusbooks.com/using-the-cli/command-overview" %}

## Datasource Configuration

### All Configuration Properties

| Property          | Type    | Default | Description                                                                                                                                                                                                |
| ----------------- | ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| driver            | String  |         | Datasource driver to use. Corresponds with the boxlang JDBC driver module - see [What Database Vendors Are Supported?](datasources.md#what-database-vendors-are-supported)                                 |
| dbdriver          | String  |         | Alias for `driver`. _Deprecated_                                                                                                                                                                           |
| class             | String  |         | Specify a custom or specific class to use as the database driver. _Not recommended - use the correct `driver` instead._                                                                                    |
| custom            | Struct  |         | Struct of custom properties.                                                                                                                                                                               |
| username          | String  |         | Database connection username.                                                                                                                                                                              |
| password          | String  |         | Database connection password.                                                                                                                                                                              |
| maxConnections    | Integer | 10      | The maximum number of connections. Alias for Hikari's `maximumPoolSize`                                                                                                                                    |
| minConnections    | Integer | 10      | The minimum number of connections. Alias for Hikari's `minimumIdle`                                                                                                                                        |
| connectionTimeout | Integer | 1       | Maximum time to wait for a successful connection, in seconds.                                                                                                                                              |
| idleTimeout       | Integer | 600     | The maximum number of idle time in seconds (10 Minutes = 600). Refers to the maximum amount of time a connection can remain idle in the pool before it is eligible for eviction.                           |
| maxLifetime       | Integer | 1800    | This property controls the maximum lifetime of a connection in the pool. An in-use connection will never be retired, only when it is closed will it then be removed. 30 minutes by default = 1800 seconds. |
| keepaliveTime     | Integer | 600     | This property controls how frequently HikariCP will attempt to keep a connection alive, in order to prevent it from being timed out by the database or network infrastructure. 10 Minutes = 600 seconds.   |
| autoCommit        | Boolean | true    | The default auto-commit state of connections created by this pool.                                                                                                                                         |
| registerMbeans    | Boolean | true    | Register mbeans for JMX connection monitoring support.                                                                                                                                                     |

In addition to the above properties, you can include any [Hikari configuration property](https://github.com/brettwooldridge/HikariCP?tab=readme-ov-file#gear-configuration-knobs-baby) you'd like in your datasource configuration:

```js
"coldbox":{
    ...
   "connectionInitSql":"custom SQL statement to run on connection initialize...",
}
```

## Datasource Connection Pooling

BoxLang uses [HikariCP](https://github.com/brettwooldridge/HikariCP) under the hood for connection pooling. Each datasource gets a dedicated connection pool. Use these configuration properties to adjust the pool size and behavior:

* `maxConnections`
* `minConnections`
* `connectionTimeout`
* `idleTimeout`
* `maxLifetime`
* `keepaliveTime`

### Pool Statistics

BoxLang offers a number of pool statistics which can be retrieved from the datasource object. To do this, first find your datasource name from the list of registered datasources:

```js
// get array of unique datasource names for all apps
writeDump( getBoxContext().getRuntime().getDatasourceService().getNames() );
```

Next, retrieve the datasource by its unique datasource name, and call `.getPoolStats()` on the result:

```js
writeDump( getBoxContext().getRuntime().getDatasourceService().get( "app_12345_my_Datasource_Name" ).getPoolStats() );
```

This returns a struct of pool metadata including the following keys:

* `pendingThreads`
* `idleConnections`
* `totalConnections`
* `activeConnections`
* `maxConnections`
* `minConnections`

Find out what datasources you have defined by dumping out:

```js
getBoxContext().getRuntime().getDatasourceService().getNames()
```
