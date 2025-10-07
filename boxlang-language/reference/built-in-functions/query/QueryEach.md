[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryEach`

Iterates over query rows and passes each row per iteration to a callback function.

This function is used to perform an action for each row in the query.
 It does not return a value, but rather allows you to perform side effects such as printing or modifying data.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
QueryEach(query=[query], callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over |  |
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Consumer which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual argument |  |
| `ordered` | `boolean` | `false` |  | `false` |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ingored if parallel is false | `false` |

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
