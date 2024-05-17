# ListFirst

Returns the first or last item in a delimited list, according to the specified function name

## Method Signature

```
ListFirst(list=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments

| Argument                  | Type      | Required   | Description                                                    | Default   |
| ------------------------- | --------- | ---------- | -------------------------------------------------------------- | --------- |
| `list`                    | `string`  | `true`     | string list to filter entries from                             |           |
| `delimiter`               | `string`  | `false`    | string the list delimiter                                      | ,         |
| `includeEmptyFields`      | `boolean` | `false`    | boolean whether to include empty fields in the returned result | false     |
| `multiCharacterDelimiter` | `boolean` | `false`    | boolean whether the delimiter is multi-character               | false     |
| ----------                | ------    | ---------- | -------------                                                  | --------- |

## Examples

```
ListFirst(list=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
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
