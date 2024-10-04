# QueryNew

Return new query based on the provided column list, column types, and/or row data.

, Available column types are: ,

* , ,
* ,bigint,
* , ,
* ,binary,
* , ,
* ,bit,
* , ,
* ,date,
* , ,
* ,decimal,
* , ,
* ,double,
* , ,
* ,integer,
* , ,
* ,null,
* , ,
* ,object,
* , ,
* ,other,
* , ,
* ,time,
* , ,
* ,timestamp,
* , ,
* ,varchar,
* , ,

, ,

, If ,`,columnTypeList,`, is empty, all columns will be of type "object".

## Method Signature

```
QueryNew(columnList=[any], columnTypeList=[string], rowData=[any])
```

### Arguments

| Argument         | Type     | Required | Description                                                                                                                                                                                                               | Default |
| ---------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `columnList`     | `any`    | `true`   | The column list to be used in the query, Ex: "name, age, dob". It can also be an array of structs that will be used as the row data.                                                                                      |         |
| `columnTypeList` | `string` | `false`  | Comma-delimited list specifying column data types. If empty, all columns will be of type "object". Ex: "varchar, integer, date"                                                                                           |         |
| `rowData`        | `any`    | `false`  | <p>Data to populate the query. Can be a struct (with keys matching column names), an array of structs, or an array of arrays (in<br>same order as columnList). Ex: [{name: "John", age: 30}, {name: "Jane", age: 25}]</p> |         |

## Examples

## Related

* [QueryAddColumn](queryaddcolumn.md)
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
* [QueryInsertAt](queryinsertat.md)
* [QueryKeyExists](querykeyexists.md)
* [QueryMap](querymap.md)
* [QueryPrepend](queryprepend.md)
* [QueryRecordCount](queryrecordcount.md)
* [QueryReduce](queryreduce.md)
* [QueryReverse](queryreverse.md)
* [QueryRowData](queryrowdata.md)
* [QueryRowSwap](queryrowswap.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
