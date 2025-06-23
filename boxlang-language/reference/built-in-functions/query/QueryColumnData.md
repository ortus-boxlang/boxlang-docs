[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryColumnData`

Returns the data in a query column.

## Method Signature

```
QueryColumnData(query=[query], columnName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get the column data from. |  |
| `columnName` | `string` | `true` | The name of the column to get the data from. |  |

## Examples

### Create and populate a query and output the 'name' column data as an array



<a href="https://try.boxlang.io/?code=eJxljcEKwjAQRM%2FmK5btJUL%2FoPQgVtCLIB7Fw2oCFZJWt4kSv95NcvQ0s8POPJ9O0XKCHooe7UcDIqw7NZG3i%2BQXtcLDZJiwFbdzjy%2FdbBjLtSfmVNw5R%2BraqVee2RiznV30kwZfAS1gHkTRN%2FF9JBZbEcJiu0QXBFbatTpQoL96fh6if2qQlR6bWmxK%2FgOIdT5L" target="_blank">Run Example</a>

```java
myQuery = QueryNew( "" );
names = [
	"Indra",
	"Elizabeth",
	"Harry",
	"Seth"
];
queryAddColumn( myQuery, "name", "varchar", names );
result = queryColumnData( myQuery, "name" );
Dump( var="#result#" );

```


### Using a member function



<a href="https://try.boxlang.io/?code=eJwtjcEKwjAQRM%2FmK5btJULxB0oPYgW9COJRPKxNoEISddso9evdJD3t7DBvxs%2FnaHmGFvI92a8GRFg3KpC3o%2FhXtcJjMExYi9q7x4%2FudhrydyDmOatLstStUe9UszVm93TRBw2%2BDNSAqRDlfoj7gVhkmZAttmN0k4wt6U2f6Y4m0guYYl30Lw3Ct1gVpMr%2BHwSjPBc%3D" target="_blank">Run Example</a>

```java
myQuery = QueryNew( "" );
names = [
	"Indra",
	"Elizabeth",
	"Harry",
	"Seth"
];
queryAddColumn( myQuery, "name", "varchar", names );
result = myQuery.columnData( "name" );
Dump( var="#result#" );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLrQwsTS2qVLBVANN%2BqeUaCkpKCprWXHmJuanFQPFoLk6lCiBQ0gEyKoFAiSvWmqsQpNoxJcU5P6c0N09DIRdijo6CEkifEpAuSyxKzkgsAjIhJgGNLEotLs0pAZoJ1g3R6pJYkoihHaS4vCizJNWlNLdAQwGqDygIAPqQOAQ%3D" target="_blank">Run Example</a>

```java
myQuery = QueryNew( "" );
names = [
	"xxxx",
	"yyyy"
];
queryAddColumn( myQuery, "name", "varchar", names );
result = queryColumnData( myQuery, "name" );
writeDump( result );

```



## Related

  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QueryClear](./QueryClear.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryColumnCount](./QueryColumnCount.md)
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
