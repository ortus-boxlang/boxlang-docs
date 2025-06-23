[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryColumnCount`

This function returns the number of columns in a query

## Method Signature

```
QueryColumnCount(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get the column count from |  |

## Examples

### Output number of query columns



<a href="https://try.boxlang.io/?code=eJzLrQwsTS2qVLBVKATRfqnlGgpKni46eYm5qTqJ6alKCprWXOVFmSWp%2FqUlBaUlGhB1zvk5pbl5zvmleUCRXKgZmiC1AHidG3M%3D" target="_blank">Run Example</a>

```java
myQuery = queryNew( "ID,name,age" );
writeOutput( queryColumnCount( myQuery ) );

```

Result: 3

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLKpUsFUoLE0tqvRLLddQUEpMTNRJSkrSSU5O1klJSdFJTU1VUtC05goEKXFMSQnKB6oqBOqCiQWnljin5uSABXXA%2BpWAVHFxMVZtOgrG%2BHVqGGpi12cIEi4vyixJdSnNLdCAuNk5P6c0N885vzSvBOoqkCoAFHxCng%3D%3D" target="_blank">Run Example</a>

```java
qry = queryNew( "aaa,bbb,ccc,ddd,eee" );
QueryAddRow( qry );
QuerySetCell( qry, "aaa", "sss" );
QueryAddRow( qry, 3 );
QuerySetCell( qry, "aaa", (1) );
QueryAddRow( qry, 1 );
writeDump( queryColumnCount( qry ) );

```



## Related

  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QueryClear](./QueryClear.md)
  * [QueryColumnArray](./QueryColumnArray.md)
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
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
