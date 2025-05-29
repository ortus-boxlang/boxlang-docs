[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryClear`

This function clears the query

## Method Signature

```
QueryClear(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to clear |  |

## Examples

### queryClear member function

Description of the code example

<a href="https://try.boxlang.io/?code=eJx90MFKw0AQBuBz9il%2B9pTCUrF6UuuhFIQeKmJv4mGT%2FLihdlMnu4YgvrubFoQY8Daz8%2B0MM47SsMUSH5HSb9nl0HVltvZAbVLoA98o5tNK6aykpxeo7EtlWVIaN7g0Q3ziKdMriSWxst5TtMq%2BzQgvxnjX%2BB7Pwcp%2BSq%2F%2B9G2Kosda7J5Tez22G1qPB2E%2FSPWK2a3qpA58jOEYQ9rvaVgVXR0chGUjVXtXCC7u9S9dx8MxhzvfZvJ%2F54g2TTvfzKCIAeU7rbD6r9H8ZPLZUPwBrG5pEw%3D%3D" target="_blank">Run Example</a>

```java
heroes = queryNew( "id,Name", "integer,varchar", [ 
	{
		"id" : 1,
		"Name" : "Bruce Banner"
	},
	{
		"id" : 2,
		"Name" : "Tony Stark"
	},
	{
		"id" : 3,
		"Name" : "Bobby Drake"
	},
	{
		"id" : 4,
		"Name" : "Jean Grey"
	}
] );
writeOutput( "Query with records<br />" );
writeDump( heroes );
writeOutput( "The same query, but cleared<br />" );
writeDump( heroes.clear() );

```

Result: A query with 4 heroes, then a query with none

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyNzz0LwkAMBuD57leEmyrcoCIOioMfk4Mixal0OCS2B%2F1Mc5b%2Be0%2BrpW5u4UkI71tTBxuoHVJ3wjYAVZgcNZgElQb1MHRLDWmwBWOC5C0CKSIphApdY5X203wqRaw%2FeqWmx8UIw9xy2vNsxMcyLXpdepUxTNayJct4dlw59mF2eC8J4fKKt8%2FQEKzUcHVweRVA7Qt4IWxcxt8q79th9%2Ftze2ekf14%2BAc1KTh4%3D" target="_blank">Run Example</a>

```java
qry = queryNew( "name, age", "varchar, integer", [ 
	[
		"Susi",
		20
	],
	[
		"Urs",
		24
	],
	[
		"Smith",
		21
	],
	[
		"John",
		26
	]
] );
writeOutput( "Before QueryClear :" );
writeDump( qry );
result = queryClear( qry );
writeOutput( "After QueryClear :" );
writeDump( qry );

```



## Related

  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySort](./QuerySort.md)
  * [QueryEach](./QueryEach.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryColumnCount](./QueryColumnCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryCurrentRow](./QueryCurrentRow.md)
  * [QueryColumnData](./QueryColumnData.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryFilter](./QueryFilter.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryNew](./QueryNew.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryColumnExists](./QueryColumnExists.md)
  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryGetCell](./QueryGetCell.md)
  * [QueryGetResult](./QueryGetResult.md)
  * [QueryMap](./QueryMap.md)
  * [QueryEvery](./QueryEvery.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QuerySome](./QuerySome.md)
  * [QueryDeleteColumn](./QueryDeleteColumn.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QueryInsertAt](./QueryInsertAt.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
