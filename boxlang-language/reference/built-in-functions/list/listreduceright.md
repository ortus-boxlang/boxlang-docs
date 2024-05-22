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
  * [GetToken](boxlang-language/reference/built-in-functions/GetToken.md)
  * [ListAppend](boxlang-language/reference/built-in-functions/ListAppend.md)
  * [ListAvg](boxlang-language/reference/built-in-functions/ListAvg.md)
  * [ListChangeDelims](boxlang-language/reference/built-in-functions/ListChangeDelims.md)
  * [ListCompact](boxlang-language/reference/built-in-functions/ListCompact.md)
  * [ListContains](boxlang-language/reference/built-in-functions/ListContains.md)
  * [ListContainsNoCase](boxlang-language/reference/built-in-functions/ListContainsNoCase.md)
  * [ListDeleteAt](boxlang-language/reference/built-in-functions/ListDeleteAt.md)
  * [ListEach](boxlang-language/reference/built-in-functions/ListEach.md)
  * [ListEvery](boxlang-language/reference/built-in-functions/ListEvery.md)
  * [ListFilter](boxlang-language/reference/built-in-functions/ListFilter.md)
  * [ListFind](boxlang-language/reference/built-in-functions/ListFind.md)
  * [ListFindNoCase](boxlang-language/reference/built-in-functions/ListFindNoCase.md)
  * [ListFirst](boxlang-language/reference/built-in-functions/ListFirst.md)
  * [ListGetAt](boxlang-language/reference/built-in-functions/ListGetAt.md)
  * [ListIndexExists](boxlang-language/reference/built-in-functions/ListIndexExists.md)
  * [ListInsertAt](boxlang-language/reference/built-in-functions/ListInsertAt.md)
  * [ListItemTrim](boxlang-language/reference/built-in-functions/ListItemTrim.md)
  * [ListLast](boxlang-language/reference/built-in-functions/ListLast.md)
  * [ListLen](boxlang-language/reference/built-in-functions/ListLen.md)
  * [ListMap](boxlang-language/reference/built-in-functions/ListMap.md)
  * [ListPrepend](boxlang-language/reference/built-in-functions/ListPrepend.md)
  * [ListQualify](boxlang-language/reference/built-in-functions/ListQualify.md)
  * [ListRemoveDuplicates](boxlang-language/reference/built-in-functions/ListRemoveDuplicates.md)
  * [ListRest](boxlang-language/reference/built-in-functions/ListRest.md)
  * [ListSetAt](boxlang-language/reference/built-in-functions/ListSetAt.md)
  * [ListSome](boxlang-language/reference/built-in-functions/ListSome.md)
  * [ListSort](boxlang-language/reference/built-in-functions/ListSort.md)
  * [ListToArray](boxlang-language/reference/built-in-functions/ListToArray.md)
  * [ListTrim](boxlang-language/reference/built-in-functions/ListTrim.md)
  * [ListValueCount](boxlang-language/reference/built-in-functions/ListValueCount.md)
  * [ListValueCountNoCase](boxlang-language/reference/built-in-functions/ListValueCountNoCase.md)
