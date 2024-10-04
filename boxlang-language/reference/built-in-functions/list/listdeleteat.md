# ListDeleteAt

Deletes an element from a list.

Returns a copy of the list, without the specified element.

## Method Signature

```
ListDeleteAt(list=[string], position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments

| Argument                  | Type      | Required | Description                                                     | Default |
| ------------------------- | --------- | -------- | --------------------------------------------------------------- | ------- |
| `list`                    | `string`  | `true`   | The list to delete from.                                        |         |
| `position`                | `integer` | `true`   | The one-based index position of the element to delete.          |         |
| `delimiter`               | `string`  | `false`  | The delimiter used in the list.                                 | `,`     |
| `includeEmptyFields`      | `boolean` | `false`  | Whether to include empty fields in the list.                    | `false` |
| `multiCharacterDelimiter` | `boolean` | `false`  | <p>Whether the delimiter is a multi-character<br>delimiter.</p> | `false` |

## Examples

## Related

* [GetToken](gettoken.md)
* [ListAppend](listappend.md)
* [ListAvg](listavg.md)
* [ListChangeDelims](listchangedelims.md)
* [ListCompact](listcompact.md)
* [ListContains](listcontains.md)
* [ListContainsNoCase](listcontainsnocase.md)
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
