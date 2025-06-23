[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryKeyExists`

This function returns true if the key exists in the query

## Method Signature

```
QueryKeyExists(query=[query], key=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to check for the key |  |
| `key` | `string` | `true` | The key to check for |  |

## Examples

### Check to see if column exists in Query

Uses the member function syntax

<a href="https://try.boxlang.io/?code=eJxdjrEKwjAURefkKy6ZWgiCjoqbjtXFTRyCfWpoTTV5MRbx303VRbd7H%2Bc8rqMUMMc1ku9XlAooW2u23JLSOTumI3l9M35%2FMj6ftpDiIYXImMIUYz3kD5%2BrWlCiHjUdyHDAxsezcUqKp%2F6xJn9WZRySaZuAzqHqurcidyhnMnnLtI58iVzA5bGjhvrl3QYOeev3RTmQLzYjOmI%3D" target="_blank">Run Example</a>

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
writeOutput( news.keyExists( "title" ) );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLrQwsTS2qVLBVKATRfqnlGgpKyaXFJZ4uOiDKLzE3VUlB05qrvCizJNWlNLdAA6LSO7XStSKzuKRYQyEXYoaOglJiOkgx0cqRLADpAQBbsC8%2F" target="_blank">Run Example</a>

```java
myQuery = queryNew( "custID,custName" );
writeDump( queryKeyExists( myQuery, "age" ) );
writeDump( queryKeyExists( myQuery, "custName" ) );

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
