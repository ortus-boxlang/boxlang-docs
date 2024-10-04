# ListFilter

Filters a delimted list and returns the values from the callback test

## Method Signature

```
ListFilter(list=[string], filter=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument                  | Type                 | Required | Description                                                                                                    | Default |
| ------------------------- | -------------------- | -------- | -------------------------------------------------------------------------------------------------------------- | ------- |
| `list`                    | `string`             | `true`   | string list to filter entries from                                                                             |         |
| `filter`                  | `function:Predicate` | `true`   | function closure filter test. You can alternatively pass a Java Predicate which will only receive the 1st arg. |         |
| `delimiter`               | `string`             | `false`  | string the list delimiter                                                                                      | `,`     |
| `includeEmptyFields`      | `boolean`            | `false`  | boolean whether to include empty fields in the returned result                                                 | `false` |
| `multiCharacterDelimiter` | `boolean`            | `false`  | boolean whether the delimiter is multi-character                                                               | `true`  |
| `parallel`                | `boolean`            | `false`  | boolean whether to execute the filter in parallel                                                              | `false` |
| `maxThreads`              | `integer`            | `false`  | number the maximum number of threads to use in the parallel filter                                             |         |

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
