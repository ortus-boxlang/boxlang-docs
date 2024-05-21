[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListReduceRight`

Run the provided udf over a reversed delimited list to reduce the values to a single output

## Method Signature
```
ListReduceRight(list=[string], callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The delimited list to perform operations on |  |
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |

## Examples

```
ListReduceRight(list=[string], callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
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
  * [ListRemoveDuplicates](ListRemoveDuplicates.md)
  * [ListRest](ListRest.md)
  * [ListSetAt](ListSetAt.md)
  * [ListSome](ListSome.md)
  * [ListSort](ListSort.md)
  * [ListToArray](ListToArray.md)
  * [ListTrim](ListTrim.md)
  * [ListValueCount](ListValueCount.md)
  * [ListValueCountNoCase](ListValueCountNoCase.md)
