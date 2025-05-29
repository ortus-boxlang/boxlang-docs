[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QuerySetCell`

Sets a cell to a value.

## Method Signature

```
QuerySetCell(query=[query], column=[string], value=[any], row=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to set the cell in |  |
| `column` | `string` | `true` | The column name to set the cell in |  |
| `value` | `any` | `true` | The value to set the cell to |  |
| `row` | `integer` | `false` | The row number to set the cell in. If no row number is specified, the cell on the last row is set. |  |

## Examples

### Tag Example

 


```java
<!--- start by making a query ---> 
 <bx:query name="GetCourses" datasource="cfdocexamples"> 
 SELECT Course_ID, Descript 
 FROM Courses 
 </bx:query> 
<bx:set temp = queryAddRow( GetCourses ) > 
<bx:set Temp = querySetCell( GetCourses, "Number", 100 * CountVar ) > 
```


### Script member function example




```java
<bx:script>
	q = queryNew( "id,name" );
	q.addRow();
	q.setCell( "id", 1, 1 );
	q.setCell( "name", "one", 1 );
	writeDump( q );
</bx:script>

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrVLBVKCxNLar0Sy3XUFDKTNHJS8xNVVLQtOYKBAk7pqQE5QNlCuEiwaklzqk5OUAhHZB6JR0FQyDCLg02C0jn54EosKKU0twCqHEAHzIjhw%3D%3D" target="_blank">Run Example</a>

```java
q = queryNew( "id,name" );
QueryAddRow( q );
QuerySetCell( q, "id", 1, 1 );
QuerySetCell( q, "name", "one", 1 );
dump( q );

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
  * [QueryInsertAt](./QueryInsertAt.md)
  * [QueryClear](./QueryClear.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
