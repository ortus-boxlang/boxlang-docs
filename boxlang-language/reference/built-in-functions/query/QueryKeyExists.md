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

  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySort](./QuerySort.md)
  * [QueryEach](./QueryEach.md)
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
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
