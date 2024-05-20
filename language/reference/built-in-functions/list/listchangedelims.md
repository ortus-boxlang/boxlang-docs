# ListChangeDelims

Converts the delimiters of a list to the new delimiter.

## Method Signature

```
ListChangeDelims(list=[string], newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments

| Argument             | Type      | Required   | Description                                                    | Default   |
| -------------------- | --------- | ---------- | -------------------------------------------------------------- | --------- |
| `list`               | `string`  | `true`     | string list to convert the delimiters.                         |           |
| `newDelimiter`       | `string`  | `true`     | string the new list delimiter                                  |           |
| `delimiter`          | `string`  | `false`    | string the old list delimiter                                  | ,         |
| `includeEmptyFields` | `boolean` | `false`    | boolean whether to include empty fields in the returned result | false     |
| ----------           | ------    | ---------- | -------------                                                  | --------- |

## Examples

```
ListChangeDelims(list=[string], newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean])
```

## Related

* [GetToken](gettoken.md)
* [ListAppend](listappend.md)
* [ListAvg](listavg.md)
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
* [ListValueCountNoCase](listvaluecountnocase.md)
