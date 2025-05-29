[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryAppend`

This function clears the query

## Method Signature

```
QueryAppend(query1=[query], query2=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query1` | `query` | `true` |  |  |
| `query2` | `query` | `true` |  |  |

## Examples

### Builds a simple query using queryNew and queryAppend

Add new query to the end of the current query using queryAppend.

<a href="https://try.boxlang.io/?code=eJzLS8xNLVawVSgsTS2q9Est11BQSs0tyInPTNHJA0op6SgoZeaVpKanFumUJRYlZyQWAYWiFbg4o7k4OWFKlRSsFAyNjC11QGJgbUABJa%2F8jDwlLs5YrlgFTWuuvNTyPLLswmKVqYEhmlWJeakIq8DmOxYUpOalaCiALdVRgFsPlC8vyixJdSnNLYDKgsQAT19Ndw%3D%3D" target="_blank">Run Example</a>

```java
names = queryNew( "empl_id,name", "integer,varchar", [ 
	[
		"empl_id" : 1239,
		"name" : "John"
	]
] );
newnames = queryNew( "empl_id,name", "integer,varchar", [
	[
		"empl_id" : 1501,
		"name" : "Jane"
	]
] );
queryAppend( names, newnames );
writeDump( names );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJydjrEKwjAQhufkKY5MFTqU4qQ4FBRBsCDqJB1CPUyGxJomFhHf3UtLsbPT%2FXx3%2FN95bP0hoHvBCh5xltglIKw0CCnIG4oUxFO6WklHwAaDTtcE38BZWew3sIALZ0wcQ6tFGtPZtYKzinKxHdd5Flf5nDj%2FwGzJLXanf9VUOCiN9qp35tkg7PHurqz46aqo6%2FuLpkF7TcCPYiqdvkF3ndMe18E0k6vIv2%2FyUag%3D" target="_blank">Run Example</a>

```java
testQuery = queryNew( "name , age", "varchar , numeric", { 
	NAME : [
		"Susi",
		"Urs"
	],
	AGE : [
		20,
		24
	]
} );
newTestQuery = queryNew( "name , age", "varchar , numeric", [
	[
		"Smith",
		20
	],
	[
		"John",
		24
	]
] );
queryAppend( testQuery, newTestQuery );
writeDump( testQuery );

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
  * [QueryClear](./QueryClear.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
