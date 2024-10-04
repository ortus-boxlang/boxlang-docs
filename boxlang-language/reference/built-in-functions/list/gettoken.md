# GetToken

Determines whether a token of the list in the delimiters parameter is present in a string.

Returns the token found at position index of the string, as a string. If index is greater than the number of tokens in the string, returns an empty string.

## Method Signature

```
GetToken(string=[string], index=[integer], delimiter=[string])
```

### Arguments

| Argument    | Type      | Required | Description                                                   | Default |
| ----------- | --------- | -------- | ------------------------------------------------------------- | ------- |
| `string`    | `string`  | `true`   | string list to filter entries from                            |         |
| `index`     | `integer` | `true`   | numeric the one-based index position to retrieve the value at |         |
| `delimiter` | `string`  | `false`  | string the list delimiter                                     | `,`     |

## Examples

## Related

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
* [ListSort](listsort.md)
* [ListToArray](listtoarray.md)
* [ListTrim](listtrim.md)
* [ListValueCount](listvaluecount.md)
* [ListValueCountNoCase](listvaluecountnocase.md)
