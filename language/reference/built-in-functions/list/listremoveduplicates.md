# ListRemoveDuplicates

De-duplicates a delimited list - either case-sensitively or case-insenstively

## Method Signature

```
ListRemoveDuplicates(list=[string], delimiter=[string], ignoreCase=[boolean])
```

### Arguments

| Argument     | Type      | Required   | Description                                                                    | Default   |
| ------------ | --------- | ---------- | ------------------------------------------------------------------------------ | --------- |
| `list`       | `string`  | `true`     | The list to deduplicate                                                        |           |
| `delimiter`  | `string`  | `false`    | The delimiter of the list                                                      | ,         |
| `ignoreCase` | `boolean` | `false`    | Whether case should be ignored or not during deduplication - defaults to false | false     |
| ----------   | ------    | ---------- | -------------                                                                  | --------- |

## Examples

```
ListRemoveDuplicates(list=[string], delimiter=[string], ignoreCase=[boolean])
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
* [ListRest](listrest.md)
* [ListSetAt](listsetat.md)
* [ListSome](listsome.md)
* [ListSort](listsort.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
* [ListValueCountNoCase](listvaluecountnocase.md)
