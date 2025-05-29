[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryReduce`

This function reduces the query to a single value.

## Method Signature

```
QueryReduce(query=[query], callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over |  |
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 4 arguments: the accumulator, the current item, the current index, and the query. You can alternatively pass a Java Predicate which will only receive the first 2<br>                    args. |  |
| `initialValue` | `any` | `true` | The initial value to use for the reduction |  |

## Examples

### Reduce column to total

Sum one query column

<a href="https://try.boxlang.io/?code=eJxtj8FqwkAQhs%2FZp%2FjZU0KX0lZ6qSj4AE2g1FMpstGJLugmncw2BMm7d6NepDkNfPN%2F8zMVByctFvgJxH1OXQpdjczYUx28aAP9a3l7sGycF9oTR%2FQFlZxVklyjGm%2FQtmmO1Goz0psa8fOrSgbzL9w4T9PCbDLfCtuuJGY3YbxERX0jmyupxR431d1LH7QLW0pxpQYpVr6HNZdRIsNiidjGJIE9LB5QPq7ei3X%2BOVeDwdN4t2MnVARpgqS4K4nLP6JPXqo%3D" target="_blank">Run Example</a>

```java
fruits = queryNew( "fruit,amount", "varchar,integer", [ 
	{
		"fruit" : "apples",
		"amount" : 15
	},
	{
		"fruit" : "pineapples",
		"amount" : 3
	},
	{
		"fruit" : "strawberries",
		"amount" : 32
	}
] );
total_fruits = queryReduce( fruits, ( Any a, Any b ) => {
	return a + b.AMOUNT;
}, 0 );
writeOutput( total_fruits );

```

Result: 50

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
date = createDateTime( 2016, 3, 13, 17, 0, 0 );
totalAge = queryreduce( people, ( Any age = 0, Any row, Any rowNumber, Any recordset ) => {
	return age + DateDiff( "yyyy", recordset.DOB, date );
} );
writeDump( totalAge );

```



## Related

  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySort](./QuerySort.md)
  * [QueryEach](./QueryEach.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryColumnCount](./QueryColumnCount.md)
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
