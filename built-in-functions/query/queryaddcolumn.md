# QueryAddColumn

Adds a column to a query and populates its rows with the contents of a one-dimensional array.

## Method Signature

```
QueryAddColumn(query=[query], columnName=[string], datatype=[any], array=[array])
```

### Arguments

| Argument     | Type     | Required   | Description                                                                                                  | Default   |
| ------------ | -------- | ---------- | ------------------------------------------------------------------------------------------------------------ | --------- |
| `query`      | `query`  | `true`     | The query object to which the column should be added.                                                        |           |
| `columnName` | `string` | `true`     | The name of the column to add.                                                                               |           |
| `datatype`   | `any`    | `false`    | The column data type of the new column or the array to populate the column with as a shortcut for "varchar". | Varchar   |
| `array`      | `array`  | `false`    |                                                                                                              | \[]       |
| ----------   | ------   | ---------- | -------------                                                                                                | --------- |

## Examples

```
QueryAddColumn(query=[query], columnName=[string], datatype=[any], array=[array])
```

## Related

* [QueryAddRow](queryaddrow.md)
* [QueryAppend](queryappend.md)
* [QueryClear](queryclear.md)
* [QueryColumnArray](querycolumnarray.md)
* [QueryColumnCount](querycolumncount.md)
* [QueryColumnData](querycolumndata.md)
* [QueryColumnExists](querycolumnexists.md)
* [QueryCurrentRow](querycurrentrow.md)
* [QueryDeleteColumn](querydeletecolumn.md)
* [QueryDeleteRow](querydeleterow.md)
* [QueryEach](queryeach.md)
* [QueryEvery](queryevery.md)
* [QueryFilter](queryfilter.md)
* [QueryGetCell](querygetcell.md)
* [QueryGetResult](querygetresult.md)
* [QueryKeyExists](querykeyexists.md)
* [QueryMap](querymap.md)
* [QueryNew](querynew.md)
* [QueryPrepend](queryprepend.md)
* [QueryRecordCount](queryrecordcount.md)
* [QueryReduce](queryreduce.md)
* [QueryRowData](queryrowdata.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
