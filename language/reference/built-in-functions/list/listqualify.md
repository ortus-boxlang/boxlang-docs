# ListQualify

Describe what the invocation of your bif function does

## Method Signature

```
ListQualify(list=[string], qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean])
```

### Arguments

| Argument             | Type      | Required   | Description   | Default   |
| -------------------- | --------- | ---------- | ------------- | --------- |
| `list`               | `string`  | `true`     |               |           |
| `qualifier`          | `string`  | `true`     |               |           |
| `delimiter`          | `string`  | `false`    |               | ,         |
| `elements`           | `string`  | `false`    |               | all       |
| `includeEmptyFields` | `boolean` | `false`    |               | false     |
| ----------           | ------    | ---------- | ------------- | --------- |

## Examples

```
ListQualify(list=[string], qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean])
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
