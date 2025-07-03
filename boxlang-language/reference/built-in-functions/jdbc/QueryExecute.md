# QueryExecute

Execute an SQL query and returns the results.

## Parameters

The `parameters` argument can be used to bind parameters to the SQL query.\
You can use either an array of binding parameters or a struct of named binding parameters.\
The SQL must have the parameters bound using the syntax `?` for positional parameters or `:name` for named parameters.

Example:

```
 queryExecute( sql: "SELECT * FROM users WHERE id = ?", params: [ 1 ] );
 queryExecute( sql: "SELECT * FROM users WHERE id = :id", params: { id: 1 } );
 
```

You can also treat each named parameter to not only be a key-value pair, but also a struct with additional options:

* **value:any** - The value to bind to the parameter
* **type:string** - The type of the value, defaults to "varchar"
* **maxLength:numeric** - The maximum length of the value, only applicable for string types
* **scale:numeric** - The scale of the value, only applicable for decimal types, defaults to 0
* **null:boolean** - Whether the value is null, defaults to false
* **list:boolean** - Whether the value is a list, defaults to false
* **separator:string** - The separator to use for list values, defaults to ","

Example:

```
 queryExecute( sql: "SELECT * FROM users WHERE id = :id", params: { id: { value: 1, type: "integer" } } );
 queryExecute( sql: "SELECT * FROM users WHERE id IN (:ids)", params: { ids: { value: [ 1, 2, 3 ], type: "integer", list: true, separator: "," } } );
 
```

## Options

The available options for this BIF are:

* <>**cache:boolean** - Whether to cache the query results, defaults to false
* **cacheKey:string** - Your own cache key, if not specified, the SQL will be used as the cache key
* **cacheTimeout:timespan|seconds** - The timeout for the cache, defaults to 0 (no timeout)
* **cacheLastAccessTimeout:timespan|seconds** - The timeout for the last access to the cache, defaults to 0 (no timeout)
* **cacheProvider:string** - The cache provider to use, defaults to the default cache provider
* **columnKey:string** - The column to use as the key when returntype is "struct"
* **datasource:string** - The datasource name to use for the query, if not specified, the default datasource will be used
* **dbtype:string** - The database type to use for the query, this is either for query of queries or HQL. Mutually exclusive with `datasource`
* **fetchsize:numeric** - Number of rows to fetch from database at once, defaults to all rows (0)
* **maxrows:numeric** - Maximum number of rows to return
* **result** - The name of the variable to store the results of the query
* **returntype** - The return type: "query", "array", "struct"
* **timeout** - Query timeout in seconds

## Method Signature

```
QueryExecute(sql=[string], params=[any], options=[struct])
```

### Arguments

| Argument  | Type     | Required | Description                                                            | Default |
| --------- | -------- | -------- | ---------------------------------------------------------------------- | ------- |
| `sql`     | `string` | `true`   | The SQL to execute                                                     |         |
| `params`  | `any`    | `false`  | An array of binding parameters or a struct of named binding parameters | `[]`    |
| `options` | `struct` | `false`  | A struct of query options                                              | `{}`    |

## Examples

### Simple Example

SQL only example. Assumes that a default datasource has been specified (by setting the variable `this.datasource` in Application.bx).

```java
qryResult = queryExecute("SELECT * FROM Employees");
```

### Using Named Placeholders

Use `:structKeyName` in your sql along with a struct of key/value pairs:

```java
qryResult = queryExecute(
  "SELECT * FROM Employees WHERE empid = :empid AND country = :country", 
  {
    country="USA", 
    empid=1
  }
);
```

### Using Positional Placeholders

You can pass placeholders by position using an array of parameters and the question mark `?` symbol:

```java
qryResult = queryExecute(
  "SELECT * FROM Employees WHERE empid = ? AND country = ?", 
  [
    1,
    "USA"
  ]
);
```

### Query of Queries

Query a local database variable without going through your database

[Run Example](https://try.boxlang.io/?code=eJxNzLEKwkAMBuD58hQhUxWfQHERC07FQQcRh%2FNMsWCr5i5WKffu3jlIh8BPkv9Tz%2BJxiU9l%2BVTcF0h1Iz50tmWaIb2suKuVFI8IZgBjRnecI21sR2AinHCyAK%2Fn%2FRgs3%2Bw0cEI939gFnGIt9xY1PyVziGnArFe7w7bM2q9FEDPWSxP4ou2jwL%2Bb1l9gIzcU)

```java
users = queryNew( "firstname", "varchar", [ 
	{
		"firstname" : "Han"
	}
] );
subUsers = queryExecute( "select * from users", {}, {
	DBTYPE : "query"
} );
writedump( subUsers );

```

### Return Query as an Array of Structs - Boxlang5+

Return a query object converted into an array of structs.

[Run Example](https://try.boxlang.io/?code=eJxNjUELgkAQhc87v2KYk4W%2FoOgSCZ0kRA8RHTYbSXCtZnczEf97a1B4GHi89%2BZ73rJY3ODTs%2FQpdxFSVYt1rTZMMdJLS3nTEuQJQQ2g1CzHFdJetwRqhDMu1mD9pZgDkzeX3nGAWm64dLjESu4G%2FVQKzGEMB2q3zY%2BHZKJ9vygGlSV5kaU%2FW4vonmCcNjqpHV%2B9eUT4nwv2B3mGPVI%3D)

```java
users = queryNew( "firstname", "varchar", [ 
	{
		"firstname" : "Han"
	}
] );
subUsers = queryExecute( "select * from users", {}, {
	DBTYPE : "query",
	RETURNTYPE : "array"
} );
writedump( subUsers );

```

Result: \[ { firstname: "Han" } ]

### Return Query as an Array of Structs - Boxlang 4.5

Return a query object converted into an array of structs.

```java
users = queryNew( "firstname", "varchar", [ 
	{
		"firstname" : "Han"
	}
] );
subUsers = queryExecute( "select * from users", {}, {
	DBTYPE : "query",
	RETURNTYPE : "array-of-entities"
} );
writedump( subUsers );

```

Result: \[ { firstname: "Han" } ]

### Return Query as a Struct of Structs

Return a query object converted into a struct of structs. (Struct key is based on the "columnkey" parameter)

[Run Example](https://try.boxlang.io/?code=eJxNjk0LgkAQhs%2B7v2LYk4WXrkWXSggqC9FDRAfTsYS0mt3NQvzvzQZ9HAaGh%2FfLaiQNY7hZpGeIjQeqzH0oStKmTitUPoPa4BHJh3tK2SklZjuQopVCsFjBEAa%2B%2B38mRmqe1kqKTu6hN5LaHpL%2FpuCBmTXIbRrPmBnoQ0GXCqwTcX7b8Ukxm8TbTeDS3i7FNVEQJ1H4wdqQzYzj0%2FUyWYWLYOswr5Kd622oNJjb6urBdwLjF4O4SLA%3D)

```java
users = queryNew( "id, firstname", "integer, varchar", [ 
	{
		"id" : 1,
		"firstname" : "Han"
	}
] );
subUsers = queryExecute( "select * from users", {}, {
	DBTYPE : "query",
	RETURNTYPE : "struct",
	COLUMNKEY : "id"
} );
writedump( subUsers );

```

Result: { 1: { id: 1, firstname: "Han" } }

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxNj09rwkAQxc87n2LYUyp70aMlh6orPagtqVVEQljMaAMxibsbbSn57m42%2BOcy7%2FHeDPwmsWQshniqSf8t6BIgT7JUYFIQtbIv9brUecoF8qywdCAt8Kz07kc9jCu3CGwLjPWFG7zKVWG5t%2BqgMw4sFl0%2F8KFRZ%2Brqi7Kk2x5ifHkFjxGRqfM7lPylXW0pQHPKQ%2F4lZ3K8xB5Oo485Jp5%2B%2FS4j2RG7o2GrjqhSWh1N%2BA9sIeUEh%2BgcW73NvqXzT4TLzadPbr8Aa6ARWFY2Kwt%2FPxnddjwQh6ZFTetjFeAzsAuv0S5fdA%3D%3D)

```java
_test = queryNew( "_id, _need, _forWorld", "integer, varchar, varchar", [ 
	[
		1,
		"plant",
		"agri"
	],
	[
		2,
		"save",
		"water"
	]
] );
queryResult = queryExecute( sql="SELECT * FROM _test WHERE _need = :need", params={
	NEED : {
		VALUE : "plant",
		TYPE : "varchar"
	}
}, options={
	DBTYPE : "query"
} );
dump( queryResult );

```

```java
queryExecute( sql="insert into user (name) values (:name)", params={ 
	NAME : {
		VALUE : "boxlang",
		TYPE : "varchar"
	}
}, options={
	DBTYPE : "query",
	RESULT : "insertResult"
} );
dump( insertResult.GENERATEDKEY );

```

## Related

* [IsInTransaction](IsInTransaction.md)
* [IsWithinTransaction](IsWithinTransaction.md)
* [PreserveSingleQuotes](PreserveSingleQuotes.md)
* [TransactionCommit](TransactionCommit.md)
* [TransactionRollback](TransactionRollback.md)
* [TransactionSetSavepoint](TransactionSetSavepoint.md)
