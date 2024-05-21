[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListRemoveDuplicates`

De-duplicates a delimited list - either case-sensitively or case-insenstively

## Method Signature
```
ListRemoveDuplicates(list=[string], delimiter=[string], ignoreCase=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to deduplicate |  |
| `delimiter` | `string` | `false` | The delimiter of the list | `,` |
| `ignoreCase` | `boolean` | `false` | Whether case should be ignored or not during deduplication - defaults to false | `false` |

## Examples

```
ListRemoveDuplicates(list=[string], delimiter=[string], ignoreCase=[boolean])
```

## Related
  * [GetToken](GetToken.md)
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
  * [ListRest](ListRest.md)
  * [ListSetAt](ListSetAt.md)
  * [ListSome](ListSome.md)
  * [ListSort](ListSort.md)
  * [ListToArray](ListToArray.md)
  * [ListTrim](ListTrim.md)
  * [ListValueCount](ListValueCount.md)
  * [ListValueCountNoCase](ListValueCountNoCase.md)
