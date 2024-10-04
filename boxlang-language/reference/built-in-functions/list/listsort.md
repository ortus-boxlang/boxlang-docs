# ListSort

Sorts a delimited list and returns the result

## Method Signature

```
ListSort(list=[string], sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])
```

### Arguments

| Argument                  | Type      | Required | Description                                                                                               | Default |
| ------------------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------- | ------- |
| `list`                    | `string`  | `true`   | The list to sort                                                                                          |         |
| `sortType`                | `any`     | `false`  | Options are text, numeric, or textnocase                                                                  |         |
| `sortOrder`               | `string`  | `false`  | Options are asc or desc                                                                                   | `asc`   |
| `delimiter`               | `string`  | `false`  | string the list delimiter                                                                                 | `,`     |
| `includeEmptyFields`      | `boolean` | `false`  | boolean whether to include empty fields in the returned result                                            | `false` |
| `multiCharacterDelimiter` | `boolean` | `false`  | boolean whether the delimiter is multi-character                                                          | `false` |
| `localeSensitive`         | `boolean` | `false`  | Sort based on local rules                                                                                 |         |
| `callback`                | `any`     | `false`  | Optional function to use for sorting - if the sort type is a closure, it will be recognized as a callback |         |

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
* [ListSetAt](listsetat.md)
* [ListSome](listsome.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
* [ListValueCountNoCase](listvaluecountnocase.md)
