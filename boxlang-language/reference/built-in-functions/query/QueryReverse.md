[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryReverse`

This function reverses the query data

## Method Signature

```
QueryReverse(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to reverse |  |

## Examples

### Reverses a queries results



<a href="https://try.boxlang.io/?code=eJyN0DsLwjAQB%2FC5%2BRRHpgpB8TH5GqQgONRBN3FI9Y8VMdVrUinidzdVEaoObvf43cFdCs6Q04jODlzGuIQk91sV6yOk8qGx2IFVoXmTavalFYngKoLAK0l9aqsqfnCfyQm7DWiijQFLEdxUDXfqeJmZkhZW8%2BGbdj%2F2ZklSUsT6gG%2Fbq9sZtKEpo6ykWFNjIC68t5g7e3LW37dM8Ty3P0yYWmP5JpE7nkJKnz%2F5OccowDm2fyxovmzYqNp3vihkIg%3D%3D" target="_blank">Run Example</a>

```java
heroes = queryNew( "id,Name", "integer,varchar", [ 
	{
		"id" : 1,
		"Name" : "Bruce Banner"
	},
	{
		"id" : 2,
		"Name" : "Tony Stark"
	},
	{
		"id" : 3,
		"Name" : "Bobby Drake"
	},
	{
		"id" : 4,
		"Name" : "Jean Grey"
	}
] );
writeOutput( "The query:<br />" );
writeDump( heroes );
writeOutput( "The reversed query:<br />" );
writeDump( heroes.reverse() );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrSS0uCSxNLapUsFUoBNF%2BqeUaCkp5ibmpCjoKiempSjoKSmWJRckZiUVAgbzS3NSizGSgYLUCF6efo6%2BrgpVCNBcnp1JwaXGmkg6IFVpUrMTFGQtkO7rDpI0MQFJGJkBxrloFTWuu8qLMklT%2F0pKC0hKgdSEZqRDbrWySihT07ZTgSlxKcws0FErgrsSqtSi1LLWoODUFrxlgOahKFBNB6gDfPE5x" target="_blank">Run Example</a>

```java
testQuery = queryNew( "name , age", "varchar , numeric", { 
	NAME : [
		"Susi",
		"Urs"
	],
	AGE : [
		20,
		24
	]
} );
writeOutput( "The query:<br />" );
writeDump( testQuery );
writeOutput( "The reversed query:<br />" );
writeDump( queryreverse( testQuery ) );

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
