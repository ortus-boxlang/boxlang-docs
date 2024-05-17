# ListRest

Returns the remainder of a list after removing the first item

## Method Signature

```
ListRest(list=[string], delimiter=[string], includeEmptyFields=[boolean], offset=[integer])
```

### Arguments

| Argument             | Type      | Required   | Description                                                    | Default   |
| -------------------- | --------- | ---------- | -------------------------------------------------------------- | --------- |
| `list`               | `string`  | `true`     | The delimited list to perform operations on                    |           |
| `delimiter`          | `string`  | `false`    | string the list delimiter                                      | ,         |
| `includeEmptyFields` | `boolean` | `false`    | boolean whether to include empty fields in the returned result | false     |
| `offset`             | `integer` | `false`    |                                                                | 0         |
| ----------           | ------    | ---------- | -------------                                                  | --------- |

## Examples

```
ListRest(list=[string], delimiter=[string], includeEmptyFields=[boolean], offset=[integer])
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
* [ListSetAt](listsetat.md)
* [ListSome](listsome.md)
* [ListSort](listsort.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
* [ListValueCountNoCase](listvaluecountnocase.md)
