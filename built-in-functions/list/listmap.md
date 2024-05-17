# ListMap

Used to iterate over a delimited list and run the function closure for each item in the list and create a new list from the returned values.

## Method Signature

```
ListMap(list=[string], callback=[function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument             | Type       | Required   | Description                                                                                                     | Default   |
| -------------------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------- | --------- |
| `list`               | `string`   | `true`     | The delimited list to perform operations on                                                                     |           |
| `callback`           | `function` | `true`     | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |           |
| `delimiter`          | `string`   | `false`    | string the list delimiter                                                                                       | ,         |
| `includeEmptyFields` | `boolean`  | `false`    | boolean whether to include empty fields in the returned result                                                  | false     |
| `parallel`           | `boolean`  | `false`    |                                                                                                                 | false     |
| `maxThreads`         | `integer`  | `false`    |                                                                                                                 |           |
| ----------           | ------     | ---------- | -------------                                                                                                   | --------- |

## Examples

```
ListMap(list=[string], callback=[function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
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
