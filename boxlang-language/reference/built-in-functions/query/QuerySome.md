# QuerySome

Used to iterate over a query and test whether **ANY** items meet the test callback.

The function will be passed 3 arguments: the row, the currentRow, and the query.\
You can alternatively pass a Java Predicate which will only receive the 1st arg.\
The function should return true if the item meets the test, and false otherwise.

**Note:** This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.\
Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
QuerySome(query=[query], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                 | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`      | `query`              | `true`   | The query to iterate over                                                                                                                                                                                         |         |
| `callback`   | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query.                                                                                                |         |
| `parallel`   | `boolean`            | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`            | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

### The simple Querysome example

Here,we've example to check whether the 75 is exists or not in myquery mark column value.

```java
<bx:script>
	myQuery = queryNew( "id,name,mark", "integer,varchar,integer", [
		[
			1,
			"Rahu",
			75
		],
		[
			2,
			"Ravi",
			80
		]
	] );
	result = querySome( myQuery, ( Any details ) => {
		return details.MARK == 75;
	} );
	writeOutput( (result ? "Some" : "No") & " matches  Record found!" );
</bx:script>

```

Result: Some matches Record found!

### The Query Member Function example

Here,we've example to check whether the 85 is exists or not in myquery mark column value using query member function.

```java
<bx:script>
	myQuery = queryNew( "id,name,mark", "integer,varchar,integer", [
		[
			1,
			"Rahu",
			75
		],
		[
			2,
			"Ravi",
			80
		]
	] );
	result = myQuery.Some( ( Any details ) => {
		return details.MARK == 85;
	} );
	writeOutput( (result ? "Some" : "No") & " matches  Record found!" );
</bx:script>

```

Result: No matches Record found!

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJyNUE1Lw0AQPWd%2FxSOHsguDJAe1RVNQgwcPESmeSg9bs9WF5qPTpCGI%2F92JtRdJwWUXZmfem3nzalfVW4cEL63jPnOdRljawlFercm%2Bu5AQHiy%2FfVim3DaOfNlIbgkVLFUQhIt270OS6IGdlFN5GvHsOiLEcmGGWqSCFf0SXnk%2Fgp9dnsM%2FsstHCFdnBzz5YgQ%2Fnf7FqxXMjTrYrc9l%2Fd2w%2FqIqBFz%2FWELQuCt7cNXRKcjaYu34%2BN1xL70tDJI5PlXArmm5hNbDxNRvNmJkL0fMEuZF%2BnxPyKpOG2HMERlMJvgP9jZBHEVGpH4Nejv2QmmLWuMoXXLf3pR0hw%3D%3D)

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
valid = querySome( people, ( Any row, Any rowNumber, Any qryData ) => {
	return ((DateDiff( "yyyy", row.DOB, Now() ) > 0) && (DateDiff( "yyyy", row.DOB, Now() ) <= 100));
} );
writeDump( valid );

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
* [QueryMap](QueryMap.md)
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
* [QuerySort](QuerySort.md)
