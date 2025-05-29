[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryColumnArray`

This function returns the column array of a query.

## Method Signature

```
QueryColumnArray(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get the column names from |  |

## Examples

### Dump array of query columns



<a href="https://try.boxlang.io/?code=eJxdjjELwjAQhefkVxyZWsiio%2BIgutbJTRwOe2qxveglMQTxv5vaSbf3Ht8Hjyl5WMEjkuQdpQpM19rQhZ6MLZkDXUjsE%2BV0RSnTAbR6aaUKZmABMzvmiS%2FVbClRhpbOhMHDXuKAbLR62x9r%2Fmc1yJCwv3lwDI1zX0UfoV7qNg73arq3cX0ceC2CuQIef9cj8QFbuDei" target="_blank">Run Example</a>

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
dump( queryColumnArray( news ) );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLKpUsFUILE0tqvRLLddQUEpMTFRS0LTmSiwqMgTKRMdac4FlHVNSnPNzSnPzNBQKiyp1FJSSkpR0FMCqgKrLizJLUl1KcwuAsiDVEKWORUWJlWD1CpogVQBQVSJD" target="_blank">Run Example</a>

```java
qry = QueryNew( "aaa" );
arr1 = [];
QueryAddColumn( qry, "bb", arr1 );
writeDump( queryColumnArray( qry ) );

```



## Related

  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySort](./QuerySort.md)
  * [QueryEach](./QueryEach.md)
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
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
