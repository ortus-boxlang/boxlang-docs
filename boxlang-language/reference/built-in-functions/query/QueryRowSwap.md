[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryRowSwap`

In a query object, swap the record in the sourceRow with the record from the destinationRow.

## Method Signature

```
QueryRowSwap(query=[query], source=[numeric], destination=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to swap a row with |  |
| `source` | `numeric` | `true` | The row to swap from |  |
| `destination` | `numeric` | `true` | The row to swap to |  |

## Examples

### Example1

This is Example1

<a href="https://try.boxlang.io/?code=eJxNzjELwjAQBeA5%2BRVHpgq3VLuJizh1cFDBoXSI9rCBtjFna8i%2FN00Ruhy8773hHAc4gJuIw5l8BoqtNw0OuieFoMww0osYv5qfreZIFUhRSSFyjEcd7UNJUeNi22S3lmxjmVbFLhWlDisrkt1N1xndzy5r2Ozlx%2Bt3%2Fn%2FpYv015gwcB4QcoZgnns1Ip6mPvqyj%2FQAo9TLP" target="_blank">Run Example</a>

```java
qry = queryNew( "rowid,name", "integer,varchar", [ 
	[
		1,
		"Bob"
	],
	[
		2,
		"Theodore"
	],
	[
		3,
		"Jay"
	],
	[
		4,
		"William"
	]
] );
swap1 = queryRowSwap( qry, 1, 4 );
writeDump( swap1 );

```


### Member function version.

Using the member function.

<a href="https://try.boxlang.io/?code=eJxNzjEPgjAQBeC5%2FRWXTphcTEA242KYHFw0cSAMVS7ShFI5wab%2F3hYWlkvue294Iwc4wTgThyv5DBQ7b1octCWFoMww0ZsYf5pfneZINUhRSyFyjEed3VNJ0eBqxWL3jlzrmDbBYQkuOmysXOxh%2Bt5om1w2sDvKr9efIk3isI9bbvHNIEcoU%2BjZTFTNNtLai%2FYH6yUwnQ%3D%3D" target="_blank">Run Example</a>

```java
qry = queryNew( "rowid,name", "integer,varchar", [ 
	[
		1,
		"Bob"
	],
	[
		2,
		"Theodore"
	],
	[
		3,
		"Jay"
	],
	[
		4,
		"William"
	]
] );
swap2 = qry.rowSwap( 1, 4 );
writeDump( swap2 );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxNzbEKwkAMBuD58hThpgpZbEfxFQR1LB1iL6hDay%2B1Hvf25iqKS%2Fjz8cMfNeMe4yKaD5Iq9PdAIw%2FiyeL4lKsovVj7G6tRi%2BBacG5Ldjx7cB19pF7l8ifNKn0R6HCzgznxNEmwuWOZOz3S2aTCqJmwJmxKKSyD0bf6A%2BuU5w0PzSxE" target="_blank">Run Example</a>

```java
qry = queryNew( "id,name", "integer,varchar", [ 
	[
		1,
		"a"
	],
	[
		2,
		"b"
	],
	[
		3,
		"c"
	]
] );
swapped = QueryRowSwap( qry, 2, 3 );
dump( swapped );
dump( qry );

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
  * [QueryRowData](./QueryRowData.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
