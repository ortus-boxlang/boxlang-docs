# ListReduceRight

Run the provided udf over a reversed delimited list to reduce the values to a single output

## Method Signature

```
ListReduceRight(list=[string], callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments

| Argument                  | Type       | Required   | Description                                                                                                     | Default   |
| ------------------------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------- | --------- |
| `list`                    | `string`   | `true`     | The delimited list to perform operations on                                                                     |           |
| `callback`                | `function` | `true`     | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |           |
| `initialValue`            | `any`      | `false`    | The initial value of the reduction                                                                              |           |
| `delimiter`               | `string`   | `false`    | string the list delimiter                                                                                       | ,         |
| `includeEmptyFields`      | `boolean`  | `false`    | boolean whether to include empty fields in the returned result                                                  | false     |
| `multiCharacterDelimiter` | `boolean`  | `false`    | boolean whether the delimiter is multi-character                                                                | true      |
| ----------                | ------     | ---------- | -------------                                                                                                   | --------- |

## Examples

```
ListReduceRight(list=[string], callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
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
* [ListRemoveDuplicates](listremoveduplicates.md)
* [ListRest](listrest.md)
* [ListSetAt](listsetat.md)
* [ListSome](listsome.md)
* [ListSort](listsort.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
* [ListValueCountNoCase](listvaluecountnocase.md)
