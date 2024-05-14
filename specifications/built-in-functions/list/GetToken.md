[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetToken`

Determines whether a token of the list in the delimiters parameter is present in a string.

## Method Signature
```
GetToken(string=[string], index=[integer], delimiter=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | string list to filter entries from | |
| `index` | `integer` | `true` | numeric the one-based index position to retrieve the value at | |
| `delimiter` | `string` | `false` | string the list delimiter | ,|
|----------|------|----------|-------------|---------|



## Examples

```
GetToken(string=[string], index=[integer], delimiter=[string])
```

## Related
  * [ListAppend](ListAppend.md)
  * [ListAvg](ListAvg.md)
  * [ListChangeDelims](ListChangeDelims.md)
  * [ListCompact](ListCompact.md)
  * [ListContains](ListContains.md)
  * [ListContainsNoCase](ListContainsNoCase.md)
  * [ListDeleteAt](ListDeleteAt.md)
  * [ListEach](ListEach.md)
  * [ListEvery](ListEvery.md)
  * [ListFilter](ListFilter.md)
  * [ListFind](ListFind.md)
  * [ListFindNoCase](ListFindNoCase.md)
  * [ListFirst](ListFirst.md)
  * [ListGetAt](ListGetAt.md)
  * [ListIndexExists](ListIndexExists.md)
  * [ListInsertAt](ListInsertAt.md)
  * [ListItemTrim](ListItemTrim.md)
  * [ListLast](ListLast.md)
  * [ListLen](ListLen.md)
  * [ListMap](ListMap.md)
  * [ListPrepend](ListPrepend.md)
  * [ListQualify](ListQualify.md)
  * [ListReduceRight](ListReduceRight.md)
  * [ListRemoveDuplicates](ListRemoveDuplicates.md)
  * [ListRest](ListRest.md)
  * [ListSetAt](ListSetAt.md)
  * [ListSome](ListSome.md)
  * [ListSort](ListSort.md)
  * [ListToArray](ListToArray.md)
  * [ListTrim](ListTrim.md)
  * [ListValueCount](ListValueCount.md)
  * [ListValueCountNoCase](ListValueCountNoCase.md)
