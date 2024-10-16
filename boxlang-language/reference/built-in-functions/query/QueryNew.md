[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryNew`

Return new query based on the provided column list, column types, and/or row data.

<p>

 Available column types are:
 
<ul>

 
<li>
bigint
</li>

 
<li>
binary
</li>

 
<li>
bit
</li>

 
<li>
date
</li>

 
<li>
decimal
</li>

 
<li>
double
</li>

 
<li>
integer
</li>

 
<li>
null
</li>

 
<li>
object
</li>

 
<li>
other
</li>

 
<li>
time
</li>

 
<li>
timestamp
</li>

 
<li>
varchar
</li>

 
</ul>

 
<p>

 If 
<code>
columnTypeList
</code>
 is empty, all columns will be of type "object".

## Method Signature

```
QueryNew(columnList=[any], columnTypeList=[string], rowData=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `columnList` | `any` | `true` | The column list to be used in the query, Ex: "name, age, dob". It can also be an array of structs that will be used as the row data. |  |
| `columnTypeList` | `string` | `false` | Comma-delimited list specifying column data types. If empty, all columns will be of type "object". Ex: "varchar, integer, date" |  |
| `rowData` | `any` | `false` | Data to populate the query. Can be a struct (with keys matching column names), an array of structs, or an array of arrays (in<br>                   same order as columnList). Ex: [{name: "John", age: 30}, {name: "Jane", age: 25}] |  |

## Examples



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
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
