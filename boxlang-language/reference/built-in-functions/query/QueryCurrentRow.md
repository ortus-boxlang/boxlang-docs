[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryCurrentRow`

Returns the current row number

## Method Signature

```
QueryCurrentRow(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get the current row number from |  |

## Examples

### Simple QueryCurrentRow Example

Here we've example to get the currentRow number.


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
<bx:loop query="myQuery">
	<bx:if name == "Anil" >
		<bx:output>#queryCurrentRow( myQuery )#</bx:output>
	</bx:if>
</bx:loop>
```

Result: 2

### Simple currentRow Example

Here we've example to get the currentRow number from query using script syntax.


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
	bx:loop query="myQuery" {
		if( title == "Mieko and the Fifth Treasure" ) {
			writeOutput( myQuery.currentRow() );
		}
	}
</bx:script>

```

Result: 3

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwljrEOwjAMROf4KyxPrZS1Q0GdYGFB6sJSdQhgQQVJi0lUIsS%2Fk7TLDc9357OxlYgNtoElHnkukIardsYyaaSD83xj0Scju7uRhDoE1YFSda2T0tsSqF6vrKoWZh%2BZQY%2FlFs6fzXMcJ3zl%2BoZs%2Fkb4BTXL4Hkf7FSst0sQYedlTAsWF5Y5%2F4M%2FB6Itlg%3D%3D" target="_blank">Run Example</a>

```java
myQry = QueryNew( "id,name", "Integer,VarChar", [ 
	[
		99,
		"sm"
	],
	[
		55,
		"mk"
	]
] );
bx:loop query="myQry" {
	writeDump( querycurrentrow( myQry ) );
}

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
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
