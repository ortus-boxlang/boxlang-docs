[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryColumnList`

This function returns the delimited column list of a query.

## Method Signature

```
QueryColumnList(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get the column names from |  |

## Examples

### Create a query and output the column list



<a href="https://try.boxlang.io/?code=eJzLrQwsTS2qVLBVKATRfqnlGgpKni46eYm5qTqJ6alKCprWXOVFmSWp%2FqUlBaUlGhB1zvk5pbl5PpnFQIFcqBGaIKUAWvYbBg%3D%3D" target="_blank">Run Example</a>

```java
myQuery = queryNew( "ID,name,age" );
writeOutput( queryColumnList( myQuery ) );

```

Result: ID,name,age

### Using a member function



<a href="https://try.boxlang.io/?code=eJzLrQwsTS2qVLBVKATRfqnlGgpKni46eYm5qTqJ6alKCprWXOVFmSWp%2FqUlBaUlGgq5EB16yfk5pbl5PpnFJRqaIEUAtqoY3g%3D%3D" target="_blank">Run Example</a>

```java
myQuery = queryNew( "ID,name,age" );
writeOutput( myQuery.columnList() );

```

Result: ID,name,age

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLKpUsFUoLE0tqvRLLddQUEpMTFRS0LTmSiwqAkoAyUSIhCFUMBrIigXKKCUqQflGEH4SjG8M4ScD%2BYEgcx1TUpzzc0pz8zQUCosqdYAqk5KUdEBGg4zEriQ5ORmhpLwosyTVpTS3QAPiUIhSn8ziErByBU2QIgD8kjvh" target="_blank">Run Example</a>

```java
qry = queryNew( "aaa" );
arr = arrayNew( 1 );
arr[ 1 ] = "a";
arr[ 2 ] = "b";
arr[ 3 ] = "c";
QueryAddColumn( qry, "bbb", arr );
QueryAddColumn( qry, "ccc", arr );
writeDump( queryColumnList( qry ) );

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
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
