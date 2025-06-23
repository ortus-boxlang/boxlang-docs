[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryGetCell`

This function maps the query to a new query.

## Method Signature

```
QueryGetCell(query=[query], column_name=[string], row_number=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over |  |
| `column_name` | `string` | `true` |  |  |
| `row_number` | `integer` | `false` |  |  |

## Examples

### The simple querygetcell example

Here we've example about querygetcell. We created query using queryNew() then we got the last title column value using querygetCell. If we give row number displays the particular row title value otherwise it displays last row value.


```java
<bx:set myQuery = queryNew( "id,name", "integer,varchar", [ 
	[
		1,
		"Rajesh"
		],
	[
		2,
		"Anil"
		]
	] ) >
<bx:output>#querygetcell( myQuery, "name" )#</bx:output>
```

Result: Anil

### The simple querygetcell (getCell) script based example

Here we've the example to get particular column(title) value in script syntax


```java
<bx:script>
	var myQuery = queryNew( "id,title", "integer,varchar", [
		[
			1,
			"Charlottes Web"
		],
		[
			3,
			"The Outsiders"
		],
		[
			4,
			"Mieko and the Fifth Treasure"
		]
	] );
	writeOutput( myQuery.getCell( "title", 2 ) );
</bx:script>

```

Result: The Outsiders

### Additional Examples


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
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
