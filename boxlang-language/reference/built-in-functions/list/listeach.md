# ListEach

Used to iterate over a delimited list and run the function closure for each item in the list.

## Method Signature

```
ListEach(list=[string], callback=[function:Consumer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], ordered=[boolean])
```

### Arguments

| Argument                  | Type                | Required | Description                                                                                                                                                                                     | Default |
| ------------------------- | ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `list`                    | `string`            | `true`   | The delimited list to perform operations on                                                                                                                                                     |         |
| `callback`                | `function:Consumer` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Consumer which will only receive the 1st arg. |         |
| `delimiter`               | `string`            | `false`  | string the list delimiter                                                                                                                                                                       | `,`     |
| `includeEmptyFields`      | `boolean`           | `false`  | boolean whether to include empty fields in the returned result                                                                                                                                  | `false` |
| `multiCharacterDelimiter` | `boolean`           | `false`  | boolean whether the delimiter is multi-character                                                                                                                                                | `true`  |
| `parallel`                | `boolean`           | `false`  | Specifies whether the items can be executed in parallel                                                                                                                                         | `false` |
| `maxThreads`              | `integer`           | `false`  | The maximum number of threads to use when parallel = true                                                                                                                                       |         |
| `ordered`                 | `boolean`           | `false`  | (BoxLang only) whether parallel operations should execute and maintain order                                                                                                                    | `false` |

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
