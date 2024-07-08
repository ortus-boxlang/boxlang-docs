---
description: BoxLang provides the easiest way to query a database
---

# Queries

BoxLang became famous in its infancy because it was easy to query databases with a simple `bx:query` tag and no verbose ceremonious coding. There is no ceremony, just a plain datasource definition in the administrator, and we could easily query the database.

In modern times, we have many more ways to query the database, and defining data sources can occur not only [in our web application's `Application.bx`](queries.md#defining-datasources-in-applicationbx), but also [globally across the BoxLang runtime via our `boxlang.json` configuration file](queries.md#defining-datasources-in-boxlangjson), not to mention defining datasources at runtime programmatically or [within the query constructs themselves](queries.md#defining-inline-datasources).

{% hint style="info" %}
See [Application.bx](../boxlang-framework/applicationbx.md) for more information on how to leverage it for web development.
{% endhint %}

## What is a Datasource?

A datasource is a **named** connection to a specific database with specified credentials. You can define a datasource in one of three locations:

1. [At the boxlang runtime level via your `boxlang.json` config file](queries.md#defining-datasources-in-boxlangjson)
2. For web applications, [in your `Application.bx` via `this.datasources`](queries.md#defining-datasources-in-applicationbx)
3. [Inline, at query time, via the `queryExecute()` BIF, `query` or `dbInfo` component, etc](queries.md#defining-inline-datasources)

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

## What is a query?

A query is a request to a database representing the results' rows and columns. It returns a BoxLang `query` object containing a **record set** and other metadata information about the query. The query can ask for information from the database, write new data to the database, update existing information in the database, or delete records from the database. This can be done in several ways:

* Using the `bx:query` tag. ([https://boxlang.ortusbooks.com/boxlang-language/reference/types/query](https://boxlang.ortusbooks.com/boxlang-language/reference/types/query))
* Using the `queryExecute()` function. ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/queryexecute](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/queryexecute))

Here's the tag syntax for a query using a named `"pantry"` datasource:

```html
<bx:query name = "qItems" datasource="pantry">
 SELECT QUANTITY, ITEM
 FROM CUPBOARD
 ORDER BY ITEM
</bx:query>
```

Most often you'll be writing queries in script syntax. Here's an example of using the [default datasource](queries.md#default-datasource) in a script-syntax query:

```js
qItems = queryExecute(
 "SELECT QUANTITY, ITEM FROM CUPBOARD ORDER BY ITEM"
);
```

## Defining Datasources

The datasource configuration struct should be defined exactly the same whether you are using an inline, ad-hoc datasource or configuring a datasource in your `boxlang.json` or `Application.bx`. Make sure you have a "driver" key defined OR the driver clearly denoted in the JDBC url:

```js
this.datasources[ "testDB" ] = {
	"driver": "mysql",
	// OR:
	"url" : "jdbc:mysql://localhost:3306/test"
};
```

### Defining Datasources In `boxlang.json`

You can define a datasource at the BoxLang runtime level by placing it in your `boxlang.json`:

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

### Defining Datasources In `Application.bx`

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

### Defining Inline Datasources

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

1. In your BoxLang runtime's `boxlang.json` config file via the `defaultDatasource` key
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

### Portable Datasources

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

## Displaying Results

The query object can be iterated on like a normal collection through a `for, bx:loop or bx:output` , `each()` constructs.

{% embed url="https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/output" %}

{% embed url="https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/loop" %}

**In a CFM Template**

```xml
<bx:output query = "qItems">
There are #qItems.Quantity# #qItems.Item# in the pantry<br />
</bx:output>
```

You leverage the `bx:output` tag by passing the `query` to it. Then in the block of the tag you use dot/array notation and interpolation to output the column you want. BoxLang will iterate over all rows in the query for you.

```xml
<bx:output query = "qItems" encodeFor="html">
There are #qItems[ 'quantity' ]# #qItems[ 'item' ]# in the pantry<br />
</bx:output>
```

{% hint style="info" %}
By specifying `encodefor="html"` each variable is encoded using the `encodeForHTML` function before it is output.
{% endhint %}

**Using Loops**

```java
for( var row in qItems ){
 systemOutput( "There are #row.quantity# #row.item# in the pantry" );
}

qItems.each( function( row, index ){
 systemOutput( "There are #row.quantity# #row.item# in the pantry" );

} );

for( var i = 1; i lte qItems.recordCount; i++ ){
 systemOutput( "There are #qItems.quantity[ i ]# #qItems.item[ i ]# in the pantry" );
}
```

As you can see, many ways to iterate over the query exist. Choose the approach that suits your needs.

### Multi-Threaded Looping

BoxLang allows you to leverage the `each()` operations in a multi-threaded fashion. The `queryEach()` or `each()` functions allow for a `parallel` and `maxThreads` arguments so the iteration can happen concurrently on as many `maxThreads` as supported by your JVM.

```java
queryEach( array, callback, parallel:boolean, maxThreads:numeric );
each( collection, callback, parallel:boolean, maxThreads:numeric );
```

This is incredibly awesome, as now your callback will be called concurrently! However, please note that once you enter concurrency land, you should shiver and tremble. Thread concurrency will be of the utmost importance, and you must ensure that var scoping is done correctly and that appropriate locking strategies are in place.

```java
myquery.each( function( row ){
   myservice.process( row );
}, true, 20 );
```

Even though this approach to multi-threaded looping is easy, it is not performant and/or flexible. Under the hood, the BoxLang uses a single thread executor for each execution, do not allow you to deal with exceptions, and if an exception occurs in an element processor, good luck; you will never know about it. This approach can be verbose and error-prone, but it's easy. You also don't control where the processing thread runs and are at the mercy of the engine.

### ColdBox Futures Parallel Programming

If you would like a functional and much more flexible approach to multi-threaded or parallel programming, consider using the ColdBox Futures approach (usable in ANY framework or non-framework code). You can use it by installing ColdBox or WireBox into any BoxLang application and leveraging our `async` programming constructs, which behind the scenes, leverage the entire Java Concurrency and Completable Futures frameworks.

{% embed url="https://coldbox.ortusbooks.com/digging-deeper/promises-async-programming/parallel-computations" %}
ColdBox Futures and Async Programming
{% endembed %}

Here are some methods that will allow you to do parallel computations:

* `all( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures to execute them in parallel. When you call on it, it will return a future that will retrieve an array of the results of all the operations.
* `allApply( items, fn, executor ):array` : This function can accept an array of items or a struct of items of any type and apply a function to each of the items in parallel. The `fn` argument receives the appropriate item and must return a result. Consider this a parallel `map()` operation.
* `anyOf( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures and will execute them in parallel. However, instead of returning all of the results in an array like `all()`, this method will return the future that executes the fastest! Race Baby!
* `withTimeout( timeout, timeUnit )` : Apply a timeout to `all()` or `allApply()` operations. The `timeUnit` can be days, hours, microseconds, milliseconds, minutes, nanoseconds, and seconds. The default is milliseconds.

## Using Input

We usually won't have the luxury of simple queries; we will need user input to construct our queries. Here is where you need to be extra careful not to allow for [SQL injection.](https://owasp.org/www-community/attacks/SQL\_Injection) BoxLang has several ways to help you prevent SQL Injection, whether using tags or script calls. Leverage the `bx:queryparam` construct/tag ([https://boxlang.ortusbooks.com/boxlang-language/reference/types/queryparam](https://boxlang.ortusbooks.com/boxlang-language/reference/types/queryparam)) and always sanitize your input via the `encode` functions in BoxLang.

```java
// Named variable holder
// automatic parameterization via inline struct definitions
queryExecute(
 "select quantity, item from cupboard where item_id = :itemID"
 { itemID = { value=arguments.itemID, sqltype="numeric" } }
);

// Positional placeholder
queryExecute(
 "select quantity, item from cupboard where item_id = ?"
 [ { value=arguments.itemID, sqltype="varchar" } ]
);
```

You can use the `:varname` notation in your SQL construct to denote a **variable** placeholder or `?` to denote a **positional** placeholder. The `bx:queryparam` tag or the inline `sqltype` construct will bind the value to a specific database type to avoid SQL injection and to further the database explain plan via types. The available SQL binding types are:

* `bigint`
* `bit`
* `char`
* `blob`
* `clob`
* `nclob`
* `date`
* `decimal`
* `double`
* `float`
* `idstamp`
* `integer`
* `longvarchar`
* `longnvarchar`
* `money`
* `money4`
* `nchar`
* `nvarchar`
* `numeric`
* `real`
* `refcursor`
* `smallint`
* `sqlxml`
* `time`
* `timestamp`
* `tinyint`
* `varchar`

{% hint style="warning" %}
Please note that the types can be prefixed with `cf_sql_{type}` or just used as `{type}`.
{% endhint %}

## Query Methods

Several query methods are available in BoxLang that can help you manage queries and create them on the fly ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/query](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/query)). Please note that you can also use chaining and member functions as well.

* `queryNew()`
* `queryAddRow()`
* `queryAddColumn()`
* `queryColumnArray()`
* `queryColumnCount()`
* `queryColumnData()`
* `queryColumnExists()`
* `queryColumnList()`
* `queryCurrentRow()`
* `queryDeleteColumn()`
* `queryDeleteRow()`
* `queryEach()`
* `queryEvery()`
* `queryFilter()`
* `queryGetCell()`
* `queryGetResult()`
* `queryGetRow()`
* `queryMap()`
* `queryRecordCount()`
* `queryReduce()`
* `queryRowData()`
* `querySetCell()`
* `querySlice()`
* `querySome()`
* `querySort()`
* `quotedValueList()`
* `valueList()`

## Building Queries

You can use a combination of the methods above to create your own queries:

```java
news = queryNew("id,title", "integer,varchar");
queryAddRow(news);
querySetCell(news, "id", "1");
querySetCell(news, "title", "Dewey defeats Truman");
queryAddRow(news);
querySetCell(news, "id", "2");
querySetCell(news, "title", "Men walk on Moon");
writeDump(news);


users = queryNew( "firstname", "varchar", [{"firstname":"Han"}] );
subUsers = queryExecute( "select * from users", {}, { dbtype="query" } );
writedump( subUsers );

news = queryNew("id,title",
    "integer,varchar",
    [ {"id":1,"title":"Dewey defeats Truman"}, {"id":2,"title":"Man walks on Moon"} ]);
writeDump(news);

news = queryNew("id,title",
    "integer,varchar",
    {"id":1,"title":"Dewey defeats Truman"});
writeDump(news);
```

## Query of Queries

Query a local database variable without going through your database is another great way to query an already queried query. Too many queries?

```java
users = queryNew( "firstname", "varchar", [{"firstname":"Han"}] );
subUsers = queryExecute( "select * from users", {}, { dbtype="query" } );
writedump( subUsers );
```

Please note that using a query of queries can be quite slow sometimes, not all the time. An alternative approach is to use modern `queryFilter()` operations to actually filter out the necessary data from a query or `querySort()`, etc.

## Returning Arrays of Structs or Struct of Structs

You can also determine the return type of database queries as something other than the BoxLang query object. You can choose an array of structs or a struct of structs. This is fantastic for modern applications that rely on rich JavaScript frameworks and produce JSON.

This is achieved by passing the `returntype` attribute within the query options or just an attribute of the `bx:query` tag ([https://boxlang.ortusbooks.com/boxlang-language/reference/types/query](https://boxlang.ortusbooks.com/boxlang-language/reference/types/query))

```java
users = queryNew( "firstname", "varchar", [{"firstname":"Han"}] );
subUsers = queryExecute( "select * from users", {}, { dbtype="query", returntype="array" } );
writedump( subUsers );

users = queryNew( "id, firstname", "integer, varchar", [{"id":1, "firstname":"Han"}] );
subUsers = queryExecute( "select * from users", {}, { dbtype="query", returntype="struct", columnkey="id" } );
writedump( subUsers );
```

## QB = Query Builder

We have created a fantastic module to deal with queries in a fluent and elegant manner. We call it **QB** short for **q**uery **b**uilder ([https://www.forgebox.io/view/qb](https://www.forgebox.io/view/qb)). You can install it using CommandBox into your application by just saying:

```bash
box install qb
```

Using qb, you can:

* Quickly scaffold simple queries
* Make complex, out-of-order queries possible
* Abstract away differences between database engines

```java
// qb
query = wirebox.getInstance( 'Builder@qb' );
q = query.from( 'posts' )
         .whereNotNull( 'published_at' )
         .whereIn( 'author_id', [5, 10, 27] )
         .get();
```

You can find all the documentation in our Ortus Books docs: [http://qb.ortusbooks.com/](http://qb.ortusbooks.com/)

## BoxLang Query Options

BoxLang supports the following query options:

* `result`
* `maxRows`
* `queryTimeout`
* `returnType`
* `fetchSize` - Set a custom result set batch size to improve performance on large queries. Is equivalent to `blockfactor` in CFML, but matches the JDBC statement option name.
* `blockfactor` - Alias for `fetchSize`. Must install the `bx-compat` module to utilize.

The following options are unimplemented, but most have support planned:

* `timezone`
* `username`
* `password`
* `dbtype`
* `cachedAfter`
* `cachedWithin`
* `debug`
* `cacheID`
* `cacheRegion`
* `clientInfo`
* `fetchClientInfo`
* `lazy`
* `psq`
* `ormoptions`