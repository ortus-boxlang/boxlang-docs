---
description: BoxLang provides the easiest way to query a database
icon: database
---

# Queries

CFML became famous in its infancy because it was easy to query databases with a simple `cfquery` tag and no verbose ceremonious coding. There is no ceremony, just a plain datasource definition in the administrator, and we could easily query the database.

In modern times, we obviously have many more ways to query the database. With BoxLang, defining data sources can occur not only [in our web application's `Application.bx`](datasources.md#defining-datasources-in-applicationbx), but also [globally across the BoxLang runtime via our `boxlang.json` configuration file](datasources.md#defining-datasources-in-boxlangjson), not to mention defining datasources at runtime programmatically or [within the query constructs themselves](datasources.md#defining-inline-datasources).

{% hint style="info" %}
See [Application.bx](../boxlang-framework/applicationbx.md) for more information on how to leverage it for web development.
{% endhint %}

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

Most often you'll be writing queries in script syntax. Here's an example of using the [default datasource](datasources.md#default-datasource) in a script-syntax query:

```js
qItems = queryExecute(
 "SELECT QUANTITY, ITEM FROM CUPBOARD ORDER BY ITEM"
);
```

## Defining Datasources

The datasource configuration struct should be defined exactly the same whether you are using an inline, ad-hoc datasource or configuring a datasource in your `boxlang.json` or `Application.bx`. Make sure you have a "driver" key defined OR the driver clearly denoted in the JDBC url:

```js
this.datasources[ "testDB" ] = {
    "driver"    : "mysql",
    "host"      : "localhost",
    "port"      : "3306",
    "database"  : "test"
    // OR:
    "url"       : "jdbc:mysql://localhost:3306/test"
};
```

For more information on datasource configuration, see our [main Datasources documentation page](https://boxlang.ortusbooks.com/boxlang-language/datasources)

## Displaying Results

The query object can be iterated on like a normal collection through a `for, bx:loop or bx:output` , `each()` constructs.

{% embed url="https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/output" %}

{% embed url="https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/loop" %}

### In a BXM Template

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

We usually won't have the luxury of simple queries; we will need user input to construct our queries. Here is where you need to be extra careful not to allow for [SQL injection.](https://owasp.org/www-community/attacks/SQL_Injection) BoxLang has several ways to help you prevent SQL Injection, whether using tags or script calls. Leverage the `bx:queryparam` construct/tag ([https://boxlang.ortusbooks.com/boxlang-language/reference/types/queryparam](https://boxlang.ortusbooks.com/boxlang-language/reference/types/queryparam)) and always sanitize your input via the `encode` functions in BoxLang.

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
Please note that the `cf_sql_{type}` syntax is only supported when [bx-compat-cfml](https://forgebox.io/view/bx-compat-cfml) is installed. Hence, `{type}` should be preferred in all new queries moving forward.
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

* `result` - Name of the variable to store the query results in.
* `maxRows` - Limit the number of rows retrieved from the database.
* `queryTimeout` - Max execution time to allow the query to run before aborting with a query timeout error.
* `returnType` - Return the result as an array, query, or struct.
* `fetchSize` - Set a custom result set batch size to improve performance on large queries. Is equivalent to `blockfactor` in CFML, but matches the JDBC statement option name.
* `cache` - Enable or disable caching
* `cacheKey` - A unique string used to identify this query for caching purposes.
* `cacheProvider` - Name of the cache provider used for caching this query. A default cache provider will be assigned if none set,
* `cacheTimeout` - Max time, as a duration, to allow cached results to be returned.

For CFML compatibility, the following options are also supported once [bx-compat-cfml](https://forgebox.io/view/bx-compat-cfml) is installed:

* `blockfactor` - alias for `fetchSize`
* `cacheID` - alias for `cacheKey`
* `cacheRegion` - alias for `cacheProvider`
* `cachedAfter` - coerced to a `cacheTimeout` duration if the current datetime is "after" the `cachedAfter` value.
* `cachedWithin` - alias for `cacheTimeout`, unless value is "request". Support planned for `cachedWithin=request`.

The following options are unimplemented, but support is planned:

* `cachedWithin=request`
* `timezone`
* `psq`
* `dbtype=query`
* `lazy`

The following query options are unimplemented, with no support planned:

* `username`
* `password`
* `debug`
* `clientInfo`
* `fetchClientInfo`
* `ormoptions`
