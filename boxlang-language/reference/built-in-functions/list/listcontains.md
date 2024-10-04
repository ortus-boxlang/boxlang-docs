# ListContains

Return int position of value in delimited list, case sensitive or case-insenstive variations

## Method Signature

```
ListContains(list=[string], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments

| Argument                  | Type      | Required | Description                                                      | Default |
| ------------------------- | --------- | -------- | ---------------------------------------------------------------- | ------- |
| `list`                    | `string`  | `true`   | The list to be searched.                                         |         |
| `value`                   | `string`  | `true`   | The value to locate in the list or a function to filter the list |         |
| `delimiter`               | `string`  | `false`  | The list delimiter(s)                                            | `,`     |
| `includeEmptyFields`      | `boolean` | `false`  | Whether to include empty fields in the search                    | `false` |
| `multiCharacterDelimiter` | `boolean` | `false`  |                                                                  | `false` |

## Examples

## Related

* [GetToken](gettoken.md)
* [ListAppend](listappend.md)
* [ListAvg](listavg.md)
* [ListChangeDelims](listchangedelims.md)
* [ListCompact](listcompact.md)
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
