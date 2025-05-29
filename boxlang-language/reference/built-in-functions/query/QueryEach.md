[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryEach`

Iterates over query rows and passes each row per iteration to a callback function

## Method Signature

```
QueryEach(query=[query], callback=[function:Consumer], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over |  |
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Consumer which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |

## Examples

### Iterate over query rows instead of bx:loop()


```java
<bx:script>
	news = queryNew( "id,title", "integer,varchar", [
		{
			"id" : 1,
			"title" : "Dewey defeats Truman"
		},
		{
			"id" : 2,
			"title" : "Man walks on Moon"
		}
	] );

	function newsRow( Any row ) {
		writeOutput( "<tr>" );
		writeOutput( "<td>#row.ID#</td>" );
		writeOutput( "<td>#row.TITLE#</td>" );
		writeOutput( "</tr>" );
	}
</bx:script>

<table>
    <bx:script>
	queryEach( news, newsRow );
</bx:script>

</table>
```

Result: 1 Dewey defeats Truman
2 Man walks on Moon

### Iterate over query rows instead of bx:loop()

```java
<bx:script>
	news = queryNew( "id,title", "integer,varchar", [
		{
			"id" : 1,
			"title" : "Dewey defeats Truman"
		},
		{
			"id" : 2,
			"title" : "Man walks on Moon"
		}
	] );

	function newsRow( Any row ) {
		writeOutput( "<tr>" );
		writeOutput( "<td>#row.ID#</td>" );
		writeOutput( "<td>#row.TITLE#</td>" );
		writeOutput( "</tr>" );
	}
</bx:script>

<table>
    <bx:output>#queryEach( news, newsRow )#</bx:output>
</table>
```

Result: 1 Dewey defeats Truman
2 Man walks on Moon

### Additional Examples


```java
people = QueryNew( "name,dob,age", "varchar,date,int", [ 
	[
		"Susi",
		CreateDate( 1970, 1, 1 ),
		0
	],
	[
		"Urs",
		CreateDate( 1995, 1, 1 ),
		0
	],
	[
		"Fred",
		CreateDate( 1960, 1, 1 ),
		0
	],
	[
		"Jim",
		CreateDate( 1988, 1, 1 ),
		0
	]
] );
Dump( var=people, label="people - original query" );
/* Output:
 *
 * | name | dob                 | age |
 * ------------------------------------
 * | Susi | 1970-01-01 00:00:00 | 0   |
 * | Urs  | 1995-01-01 00:00:00 | 0   |
 * | Fred | 1960-01-01 00:00:00 | 0   |
 * | Jim  | 1988-01-01 00:00:00 | 0   |
 *
 */
people.each( ( Any row, Any rowNumber, Any recordset ) => {
	recordset.AGE[ rowNumber ] = DateDiff( "yyyy", row.DOB, Now() );
} );
Dump( var=people, label="people - with calculated age" );
 /* Output:
 *
 * | name | dob                 | age |
 * ------------------------------------
 * | Susi | 1970-01-01 00:00:00 | 45  |
 * | Urs  | 1995-01-01 00:00:00 | 20  |
 * | Fred | 1960-01-01 00:00:00 | 55  |
 * | Jim  | 1988-01-01 00:00:00 | 27  |
 *
 */
```



## Related

  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySort](./QuerySort.md)
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
  * [QueryAppend](./QueryAppend.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
