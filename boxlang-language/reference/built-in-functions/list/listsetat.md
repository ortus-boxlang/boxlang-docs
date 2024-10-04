# ListSetAt

Retrieves an item in to a delimited list at the specified position

## Method Signature

```
ListSetAt(list=[string], position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments

| Argument                  | Type      | Required | Description                                                    | Default |
| ------------------------- | --------- | -------- | -------------------------------------------------------------- | ------- |
| `list`                    | `string`  | `true`   | string list to filter entries from                             |         |
| `position`                | `integer` | `true`   | numeric the one-based index position to retrieve the value at  |         |
| `value`                   | `string`  | `true`   | string the value to set at the specified position              |         |
| `delimiter`               | `string`  | `false`  | string the list delimiter                                      | `,`     |
| `includeEmptyFields`      | `boolean` | `false`  | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false`  | boolean whether the delimiter is multi-character               | `true`  |

## Examples

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
* [ListSome](listsome.md)
* [ListSort](listsort.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
* [ListValueCountNoCase](listvaluecountnocase.md)
