[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryRowData`

Returns the cells of a query row as a structure

## Method Signature

```
QueryRowData(query=[query], rowNumber=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query object to which the row should be returned. |  |
| `rowNumber` | `integer` | `true` | Position of the query row to return. |  |

## Examples

### The simple queryGetRow example

Here we've a example to get the particular row value from myquery.


```java
<bx:set myQuery = queryNew( "id,name,age", "integer,varchar,integer", [ 
	[
		1,
		"Dharshini",
		20
		],
	[
		2,
		"Subash",
		18
		]
	] ) >
<bx:dump var="#queryrowdata( myQuery, 2 )#"/>
```


### The simple getRow example

We've example to get the particular row value from myquery using script syntax.


```java
<bx:script>
	var myQuery = queryNew( "id,title,author", "integer,varchar,varchar", [
		[
			1,
			"Charlottes Web",
			"E.B. White"
		],
		[
			3,
			"The Outsiders",
			"S.E. Hinton"
		],
		[
			4,
			"Mieko and the Fifth Treasure",
			"Eleanor Coerr"
		]
	] );
	writeDump( myQuery.getRow( 3 ) );
</bx:script>

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrVLBVKCxNLar0Sy3XUFDKTNHJS8xNVdIBMvNKdMoSi5IzEouUFDStuQr1ElNSgvKBqkwg3OLUEufUnBywLqAGQyDCKmEERFgljIEIq4SJDqYdMGfl54EoDJtg0iXl%2BUpY7INLZxSlghgY9sIUpOWXFilBrU8pzS3QUChEMANBAQUMApfEkkSgBNgekCwAYFhZSg%3D%3D" target="_blank">Run Example</a>

```java
q = queryNew( "id,name", "int,varchar" );
q.addRow( 4 );
q.setCell( "id", 1, 1 );
q.setCell( "id", 2, 2 );
q.setCell( "id", 3, 3 );
q.setCell( "id", 4, 4 );
q.setCell( "name", "one", 1 );
q.setCell( "name", "two", 2 );
q.setCell( "name", "three", 3 );
q.setCell( "name", "four", 4 );
dump( q );
dump( QueryRowData( q, 2 ) );

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
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
