# ListValueCountNoCase

returns a count of the number of occurrences of a value in a list

## Method Signature

```
ListValueCountNoCase(list=[string], value=[string], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments

| Argument             | Type      | Required   | Description                                   | Default   |
| -------------------- | --------- | ---------- | --------------------------------------------- | --------- |
| `list`               | `string`  | `true`     | The list to be searched.                      |           |
| `value`              | `string`  | `true`     | The value to locale                           |           |
| `delimiter`          | `string`  | `false`    | The list delimiter(s)                         | ,         |
| `includeEmptyFields` | `boolean` | `false`    | Whether to include empty fields in the search | false     |
| ----------           | ------    | ---------- | -------------                                 | --------- |

## Examples

```
ListValueCountNoCase(list=[string], value=[string], delimiter=[string], includeEmptyFields=[boolean])
```

## Related

* [GetToken](gettoken.md)
* [ListAppend](listappend.md)
* [ListAvg](listavg.md)
* [ListChangeDelims](listchangedelims.md)
* [ListCompact](listcompact.md)
* [ListContains](listcontains.md)
* [ListContainsNoCase](listcontainsnocase.md)
* [ListDeleteAt](listdeleteat.md)
* [ListEach](listeach.md)
* [ListEvery](listevery.md)
* [ListFilter](listfilter.md)
* [ListFind](listfind.md)
* [ListFindNoCase](listfindnocase.md)
* [ListFirst](listfirst.md)
* [ListGetAt](listgetat.md)
* [ListIndexExists](listindexexists.md)
* [ListInsertAt](listinsertat.md)
* [ListItemTrim](listitemtrim.md)
* [ListLast](listlast.md)
* [ListLen](listlen.md)
* [ListMap](listmap.md)
* [ListPrepend](listprepend.md)
* [ListQualify](listqualify.md)
* [ListReduceRight](listreduceright.md)
* [ListRemoveDuplicates](listremoveduplicates.md)
* [ListRest](listrest.md)
* [ListSetAt](listsetat.md)
* [ListSome](listsome.md)
* [ListSort](listsort.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
