[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryEvery`

Used to iterate over a Query and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the Query.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large Queries, especially when the test function is computationally expensive or the Query is large.

## Method Signature

```
QueryEvery(query=[query], closure=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to test against the callback. |  |
| `closure` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### All values greater than 50

Find out if every value in the query is greater than 50


```java
<bx:script>
	data = query( foo=[
		51,
		52,
		535
	] );
	allGT50 = queryEvery( ( Any row ) => {
		return row.FOO > 50;
	} );
</bx:script>

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzFkkFPg0AQhc%2Fsr3jhYMBs7WLa2qqYqMSDhxpjPDUetjJVEgq4BZvG%2Bt%2BdBW1M05rqxc2Q3WXfDMy3r6C8SAkhbisyiyHNPbiZnpKM87HUT%2BRKuK%2FaPD5rI2Ndkkyykt%2BNIJyRcBz3rpolruTVpSE%2BjvjxEAyOlETAAd%2BeKeE8yM%2BEezPboB90t%2BmvDMUbEnpbP3CdTDfo%2B%2F11vXiAfyKialp44A7DoiYhkeoxpaHbbNFCbpKnJNMpXiwh1ya193FTlUVVHgvsc2AJy4wnpob1sQRzxNLqWjuMpp7lypMl2VIBB5Q6roPfKlu10TFO1LpB90edxVjrej%2FXY3pNvX5%2Fu64t2m2wGzSDSxNeJHnGpGybYyrnRBlLdRYjOFSilrDBGqAH9MoUPXg4zxYw%2BVx%2BLYbVdEym2b6YRWTL%2BwjP8CYcQ2VlMnievc4omUzYpQse7ETOPIhuLiSG%2BdzzOeMMysfeHnbRnoYIlPL5St%2FtvcYrM9Q%2FvfJC08KWBtccgdJUtBOiTlOi%2Bx%2BIOr9i1P0bolWDNSJ8YzTR6cxC%2BgCECzEP" target="_blank">Run Example</a>

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
 */
// data validation - age between 0 and 120
valid = people.every( ( Any row, Any rowNumber, Any qryData ) => {
	return ((DateDiff( "yyyy", row.DOB, Now() ) > 0) && (DateDiff( "yyyy", row.DOB, Now() ) <= 100));
} );
dump( var=valid, label="valid - age between 0 and 120" );
/* Output: true */
// data validation - age between 40 and 50
valid = people.every( ( Any row, Any rowNumber, Any qryData ) => {
	return ((DateDiff( "yyyy", row.DOB, Now() ) > 40) && (DateDiff( "yyyy", row.DOB, Now() ) <= 50));
} );
dump( var=valid, label="valid - age between 40 and 50" );
 /* Output: false */
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
