# QueryMap

This BIF will iterate over each row in the query and invoke the callback function for each item so you can do\
any operation on the row and return a new value that will be set at the same index in a new query.

The callback function will be passed the row as a struct, the current row number (1-based), and the query itself.

* If the callback requires strict arguments, it will only receive the row as a struct.
* If the callback does not require strict arguments, it will receive the row as a struct, the row number (1-based), and the query itself.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete.\
Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
QueryMap(query=[query], callback=[function:Function], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`      | `query`             | `true`   | The query to iterate over                                                                                                                                                                                         |         |
| `callback`   | `function:Function` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Function which will only receive the 1st arg.                |         |
| `parallel`   | `boolean`           | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`           | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

### Maps query results

Manipulates query column

[Run Example](https://try.boxlang.io/?code=eJxlj0FLxDAQhc%2FJr3jkIF0Iwnq09NY9LNgVoeBBPMTd6RrdpmuaGIrsf3dSZUU9Zebjvbw3jtKICm%2BR%2FLShVEDZnQ42HEhpnl2gPXn9bvz22XhGD5DiQwrBMoVrLHWev%2FS8qpoSTdhRRyaMaH3sjVNSnPQv19UfV2Mckjm8jhgcmmGYLfIRi1ImbwPVsT8WcLkqI9lFtw2Wpb053uXiBYybcPv0ggU4xnZFXi7XNaoKS4Z5a9ftzYpPVZvVPWfi4oeWUngK0buMSnmSHDV%2FzPL5bcx3vj5n%2Fi93xp8Zw2OR)

```java
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
writeDump( news );

function mapQuery( any Obj ) {
	if( Obj.ID == 1 ) Obj.TITLE = "NEW: " & Obj.TITLE;
	return Obj;
}
newQuery = QueryMap( news, mapQuery );
writeDump( newQuery );

```

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJx1UE1Lw0AQPWd%2FxWNPCQ6SCNaGUEENHgQrIp5CD2kz1YD5cJIYgvjfnZUKIukyC7Mz7828fS037RtjhceBZVrz6MPWecVUNFvKX9gS7Ecuu9dcqMh7prLutZbBeJnxPPs0dKUlzW6EtZ3q9RHFFyEh0kDgeqHxNnQgPEs3g4%2FPj%2BFvhYsZwuLogruymsEvl%2F%2FxZoMgMcKdfv7dff4%2Bb320P34QfFzVE6QZ6TdZD9WW5fDkXSNFxz0CrC7xaTwFZLDOMGx0oFublvu9ujnpUccUcJo%2BXBP%2B6joLowVBI9ZBAU4QJTqK%2B0FqR0jMl9M4SqmEoVJ5Tq5WvgF9r3EJ)

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
res = queryMap( people, ( Any row, Any rowNumber, Any recordset ) => {
	row[ "age" ] = DateDiff( "yyyy", row.DOB, CreateDate( 2016, 6, 9 ) ) + 1;
	return row;
} );
writeDump( res );

```

## Related

* [QueryAddColumn](QueryAddColumn.md)
* [QueryAddRow](QueryAddRow.md)
* [QueryAppend](QueryAppend.md)
* [QueryClear](QueryClear.md)
* [QueryColumnArray](QueryColumnArray.md)
* [QueryColumnCount](QueryColumnCount.md)
* [QueryColumnData](QueryColumnData.md)
* [QueryColumnExists](QueryColumnExists.md)
* [QueryColumnList](QueryColumnList.md)
* [QueryCurrentRow](QueryCurrentRow.md)
* [QueryDeleteColumn](QueryDeleteColumn.md)
* [QueryDeleteRow](QueryDeleteRow.md)
* [QueryEach](QueryEach.md)
* [QueryEvery](QueryEvery.md)
* [QueryFilter](QueryFilter.md)
* [QueryGetCell](QueryGetCell.md)
* [QueryGetResult](QueryGetResult.md)
* [QueryInsertAt](QueryInsertAt.md)
* [QueryKeyExists](QueryKeyExists.md)
* [QueryNew](QueryNew.md)
* [QueryNone](QueryNone.md)
* [QueryPrepend](QueryPrepend.md)
* [QueryRecordCount](QueryRecordCount.md)
* [QueryRecordCount](QueryRecordCount.md)
* [QueryReduce](QueryReduce.md)
* [QueryRegisterFunction](QueryRegisterFunction.md)
* [QueryReverse](QueryReverse.md)
* [QueryRowData](QueryRowData.md)
* [QueryRowSwap](QueryRowSwap.md)
* [QuerySetCell](QuerySetCell.md)
* [QuerySetRow](QuerySetRow.md)
* [QuerySlice](QuerySlice.md)
* [QuerySome](QuerySome.md)
* [QuerySort](QuerySort.md)
