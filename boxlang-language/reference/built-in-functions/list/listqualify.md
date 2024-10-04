# ListQualify

Inserts a string at the beginning and end of list elements.

## Method Signature

```
ListQualify(list=[string], qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean])
```

### Arguments

| Argument             | Type      | Required | Description                                                                                                    | Default |
| -------------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------- | ------- |
| `list`               | `string`  | `true`   | The list to qualify.                                                                                           |         |
| `qualifier`          | `string`  | `true`   | The string to insert at the beginning and end of each element.                                                 |         |
| `delimiter`          | `string`  | `false`  | The delimiter used in the list.                                                                                | `,`     |
| `elements`           | `string`  | `false`  | The elements to qualify. If set to "char", only elements that are all alphabetic characters will be qualified. | `all`   |
| `includeEmptyFields` | `boolean` | `false`  | If true, empty fields will be qualified.                                                                       | `false` |

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
