[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListCompact`

Compacts a list by removing empty items from the start and end of the list

## Method Signature
```
ListCompact(list=[string], delimiter=[string], multiCharacterDelimiter=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to compact | |
| `delimiter` | `string` | `false` | string the list delimiter | ,|
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | false|
|----------|------|----------|-------------|---------|



## Examples

```
ListCompact(list=[string], delimiter=[string], multiCharacterDelimiter=[boolean])
```

## Related
  * [GetToken](GetToken.md)
  * [ListAppend](ListAppend.md)
  * [ListAvg](ListAvg.md)
  * [ListChangeDelims](ListChangeDelims.md)
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
