# QueryFilter

Filters query rows specified in filter criteria\
This BIF will invoke the callback function for each row in the query, passing the row as a struct.

* If the callback returns true, the row will be included in the new query.
* If the callback returns false, the row will be excluded from the new query.
* If the callback requires strict arguments, it will only receive the row as a struct.
* If the callback does not require strict arguments, it will receive the row as a struct, the row number (1-based), and the query itself.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.\
Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
QueryFilter(query=[query], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                 | Required | Description                                                                                                                                                                                                           | Default |
| ------------ | -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`      | `query`              | `true`   | The query to get filtered                                                                                                                                                                                             |         |
| `callback`   | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the query row as a struct, the row number, the query. You can alternatively pass a Java Predicate which will only receive the 1st arg. |         |
| `parallel`   | `boolean`            | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                           | `false` |
| `maxThreads` | `integer`            | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p>     |         |

## Examples

### Filter a query

[Run Example](https://try.boxlang.io/?code=eJx9kVFLwzAUhZ%2BbX3HJUwthoL45KtRVYVBFRl9EZMT1bgtLk5neWorsv3vb6ZgIPuXmwHdO7onDroEU3lsM%2FSN2MUhTKer3qMiQRalYcIQbDOpDh9VWn04JyVSMXFZVC8%2BoYy8FLyL6FFE0z%2BEaLhRP5fPTHc%2FyzfudHIV5WYzKzPq2goysbqSIDuqMvPyfLHyowK%2Bh3CIsjNv84a%2FO%2BbWx9W%2F%2BAR0YB7dWr3YDKl6HbYacUxv3xhKGn61iyFwPy%2BECCaQ3wEkBqQ3uKE7GrDT9fuxUHAbDLhjCvK338dFz5m1bu1yTjmEM43qPPUMyIV%2BYhvgHWOQMxr8AcZxzkg%3D%3D)

```java
news = queryNew( "id,type,title", "integer,varchar,varchar" );
queryAddRow( news, [
	{
		ID : 1,
		TYPE : "book",
		TITLE : "Cloud Atlas"
	},
	{
		ID : 2,
		TYPE : "book",
		TITLE : "Lord of The Rings"
	},
	{
		ID : 3,
		TYPE : "film",
		TITLE : "Men in Black"
	}
] );
books = queryFilter( news, ( Any _news ) => {
	return _news.TYPE == "book";
} );
writeDump( queryColumnData( books, "title" ).toList( ", " ) );

```

Result: Cloud Atlas, Lord of The Rings

### Filter a query as member function

[Run Example](https://try.boxlang.io/?code=eJx9kMFKxDAQhs%2FNUww5tRAK6s2lQt16WKgiSy8iInEzuxs2TdY0tRTZd3fSiqwInjJ88M2f%2BS0OHRTw3qMfH3BIgWslwnhEEXQwyAUBG3CHXnxIv9nLn5dDtmCTVyq1dqRa2iXgmSWfLElWFVzDhaCpeXq8o5m%2FOXfgE1g19USWxvUKymBkx1lyEmfm5f9m7bwCt4Vmj7DWdvfHvzr3t9q0v%2F17tKAt3Bq5OUSVvcRrYk5sIx6SkxTQp5BCaUd4jQwyKG6AMjyG3tsZ5lNKUXx%2Fc8FOcdXgdcCqb4%2Fp3O3Smb61lQwyhSmGip0bhiwPrtZdoO4JUgbpX5DrcV4%3D)

```java
news = queryNew( "id,type,title", "integer,varchar,varchar" );
queryAddRow( news, [
	{
		ID : 1,
		TYPE : "book",
		TITLE : "Cloud Atlas"
	},
	{
		ID : 2,
		TYPE : "book",
		TITLE : "Lord of The Rings"
	},
	{
		ID : 3,
		TYPE : "film",
		TITLE : "Men in Black"
	}
] );
books = news.filter( ( Any _news ) => {
	return _news.TYPE == "book";
} );
writeDump( queryColumnData( books, "title" ).toList( ", " ) );

```

Result: Cloud Atlas, Lord of The Rings

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJy1kk1Lw0AQhs%2FZX%2FGSU1qSJj20pi0RjEXQQ6uIByk9bMyqgXx1m1iK9b87u9EikoggLhP2Y96Z2X0mpSjKVCDATS3kfiF2FsycZ8KOi8i0Yb5w%2BfDMpR3zStB%2BBWasmGGYt%2FU2MW1anUtBrjl9FoaTE8%2FGkAw95fOYsbY%2FAu7ktkU%2FGXXpL6SIWwLGnQWukqxF7%2Ftd%2BlA98Bd6tkZvxuZ1VlogGkGpidlIeSTSwGy2cFDI5CnJeYqNImmqILePZV2VdTVl6JPhAMWWJqKL7%2BOgFM6Po8mh2NOkaDvekAyeN9XW5DiAYEMrJqMOhcKrFeOuHMSzyeH7HYpQPaJb4TLXxWOSVkISnqiQOZJcq9lG7q81t5BOL3N1Rr9gg3LQhFiwcJbvIYud%2FblY1FkkZLOlFNQzjh6CU7wyQ4qqpgr3glMoaQfzZaicga44Y2%2BqIfGxiy03OLa07XYOwi8P0N3FP7X37%2BDfAasd7e8%3D)

```java
people = QueryNew( "name,dob", "varchar,date", [ 
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
	],
	[
		"Bob",
		CreateDate( 1988, 1, 1 ),
		0
	]
] );
Dump( var=people, label="people - original query" );
/* Output:
 *
 * | name | dob                 |
 * ------------------------------
 * | Susi | 1970-01-01 00:00:00 |
 * | Urs  | 1995-01-01 00:00:00 |
 * | Fred | 1960-01-01 00:00:00 |
 * | Jim  | 1988-01-01 00:00:00 |
 * | Bob  | 1988-01-01 00:00:00 |
 */
// filter - born in 1988
qryPeopleBornIn1988 = people.filter( ( Any row, Any rowNumber, Any qryData ) => {
	return Year( row.DOB ) == 1988;
} );
dump( var=qryPeopleBornIn1988, label="qryPeopleBornIn1988 - Born in 1988" );
 /* Output:
 *
 * | name | dob                 |
 * ------------------------------
 * | Jim  | 1988-01-01 00:00:00 |
 * | Bob  | 1988-01-01 00:00:00 |
 */
```

```java
<bx:script>
	q = QueryNew( "name, description" );
	bx:loop times=3 {
		getFunctionList().each( ( Any f ) => {
			var fd = getFunctionData( arguments.F );
			var r = QueryAddRow( q );
			QuerySetCell( q, "name", fd.NAME, r );
			QuerySetCell( q, "description", fd.DESCRIPTION, r );
		} );
	}
	dump( var=q.RECORDCOUNT, label="demo data set size" );
	s = "the";
</bx:script>


<bx:timer type="outline" label="Query of Query">
	<bx:query dbtype="query" name="q1">
		select 	name, description
		from 	q
		where 	description like <bx:queryparam value="%#s#%" sqltype="varchar">
	</bx:query>
</bx:timer>
<bx:dump var="#q1.RECORDCOUNT#">

<bx:timer type="outline" label="query.filter() with scoped variables">
	<bx:script>
		q2 = q.filter( ( Any row ) => {
			return (arguments.ROW.DESCRIPTION contains s);
		} );
	</bx:script>
	
</bx:timer>
<bx:dump var="#q2.RECORDCOUNT#">

<bx:timer type="outline" label="query.filter() without unscoped variables">
	<bx:script>
		q3 = q.filter( ( Any row ) => {
			return (row.DESCRIPTION contains s);
		} );
	</bx:script>
	
</bx:timer>
<bx:dump var="#q3.RECORDCOUNT#">
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
* [QuerySome](QuerySome.md)
* [QuerySort](QuerySort.md)
