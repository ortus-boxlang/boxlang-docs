[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryPrepend`

Adds a query to the beginning of another query

## Method Signature

```
QueryPrepend(query1=[query], query2=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query1` | `query` | `true` |  |  |
| `query2` | `query` | `true` |  |  |

## Examples

### Builds a simple query using queryNew and queryPrepend

Add new query to the end of the current query using queryPrepend.

<a href="https://try.boxlang.io/?code=eJydjT0LwjAQhufkVxw3VchgFQcVNycHcS9Fgj1swJzxbA3%2Be9PgB4iT6%2FN%2BPGw9XWEFl57kvqVYAJIPp71rDKcIDaDjjo4k5mbl0FpJqAKtKq3Uq4qwgHIynZuB5VkCuDm3jFrVuobRUjNF%2Fsv1QzUbl18qy%2FRR5f%2BdUCBuCshWA29%2FKkRxHa17H57pwB6jRE3t" target="_blank">Run Example</a>

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
queryPrepend( names, newnames );
writeDump( names );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJydjrEKwjAQhufkKY5MFTqU4qQ4FBRBsCjqJB1CPdoMifWaWER8d5OWYmen%2B%2Fnu%2BL%2Bz2NqjQ3rBCh5h5thFIIzUCDHICkUM4imprCV5YJxGUqWHb%2BAsz%2FYbWMCVMyZOrlUiDulCreCs8Dnbjus0Cat07jn%2FwGzJDXbnf9W%2BcFBqZevemSaDsMe7e23ET1cEXd9%2FIGzQ3CKwo9m3Tv%2Fwhx0pi2unm8lV4F%2FIalIe" target="_blank">Run Example</a>

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
queryPrepend( testQuery, newTestQuery );
writeDump( testQuery );

```



## Related

  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QueryClear](./QueryClear.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryColumnCount](./QueryColumnCount.md)
  * [QueryColumnData](./QueryColumnData.md)
  * [QueryColumnExists](./QueryColumnExists.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryCurrentRow](./QueryCurrentRow.md)
  * [QueryDeleteColumn](./QueryDeleteColumn.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryEach](./QueryEach.md)
  * [QueryEvery](./QueryEvery.md)
  * [QueryFilter](./QueryFilter.md)
  * [QueryGetCell](./QueryGetCell.md)
  * [QueryGetResult](./QueryGetResult.md)
  * [QueryInsertAt](./QueryInsertAt.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryMap](./QueryMap.md)
  * [QueryNew](./QueryNew.md)
  * [QueryNone](./QueryNone.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
