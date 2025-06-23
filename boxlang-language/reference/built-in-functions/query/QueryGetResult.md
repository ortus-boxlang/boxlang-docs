[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryGetResult`

Returns the metadata of a query.

## Method Signature

```
QueryGetResult(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get the result from |  |

## Examples

### Retrieves query metadata using queryGetResult



<a href="https://try.boxlang.io/?code=eJxtkDkLAjEQhevkVwypVNJ4VB6NKHaiYiNiEdfRXdjL2cRVZP%2B7Ey9YlJAw8%2FjmDS9HcpGFEZwd0m2OZQNUdNCpSVBpLlOLJyR9MRSEhljaghR3KQRTCvrQ1r5%2B4twpk%2BcxKikqXaM6dWpvUj6%2FWLeOZWTS0x%2B3Xh3L0QShp%2BQOmgOZ3JY%2ByifS9IqBs8ixCowxsNCCI2UJPz53GSIhRAcYQo%2FD3Su%2BUkzG681i6r2fFkpWL%2BMVFi7%2BftYM7UtowGcnUyVFFicuyb36HmD5AZcLY7s%3D" target="_blank">Run Example</a>

```java
fruit = queryNew( "id,name", "integer,varchar", [ 
	{
		"id" : 1,
		"name" : "apple"
	},
	{
		"id" : 2,
		"name" : "banana"
	},
	{
		"id" : 3,
		"name" : "orange"
	},
	{
		"id" : 4,
		"name" : "peach"
	}
] );
myQuery = queryExecute( "select * from fruit where id < 4", {}, {
	DBTYPE : "query"
} );
myResult = queryGetResult( myQuery );
writeDump( myResult );

```


### Retrieves query metadata using getResult member function



<a href="https://try.boxlang.io/?code=eJxtkMsKwjAQRdfJVwxZVQmCj5WPjehWVNyIuIh1bAttrWNiFem%2FO%2FEFRQkTZm4Od7g5kEssjODkkG4zLANQyV7nJkOluc0tRkj6YiiMDbG0ASnuUgimFPShrX3%2FxHlSpihSVFJUukZ16tTO5Hx%2BsW4dO5LJoz9uvTpWoAljT8ktNAYyuy18lE%2Bk6RVDZ5FjnTHF0EITDnTM%2BPK5yxgJIdnDEHoc7l5xSTEZr9bzqfd%2BWihZvYyXeHap%2F6z3jlaE9qUF%2FF5SYnHisiKAL8ryAz%2BJYZM%3D" target="_blank">Run Example</a>

```java
fruit = queryNew( "id,name", "integer,varchar", [ 
	{
		"id" : 1,
		"name" : "apple"
	},
	{
		"id" : 2,
		"name" : "banana"
	},
	{
		"id" : 3,
		"name" : "orange"
	},
	{
		"id" : 4,
		"name" : "peach"
	}
] );
myQuery = queryExecute( "select * from fruit where id < 4", {}, {
	DBTYPE : "query"
} );
myResult = myQuery.getResult();
writeDump( myResult );

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
