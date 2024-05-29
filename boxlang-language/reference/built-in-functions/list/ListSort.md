[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListSort`

Sorts a delimited list and returns the result

## Method Signature

```
ListSort(list=[string], sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to sort |  |
| `sortType` | `any` | `false` | Options are text, numeric, or textnocase |  |
| `sortOrder` | `string` | `false` | Options are asc or desc | `asc` |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `localeSensitive` | `boolean` | `false` | Sort based on local rules |  |
| `callback` | `any` | `false` | Optional function to use for sorting - if the sort type is a closure, it will be recognized as a callback |  |

## Examples

```
ListSort(list=[string], sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])
```

## Related

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListAvg](./ListAvg.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListCompact](./ListCompact.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListDeleteAt](./ListDeleteAt.md)
  * [ListEach](./ListEach.md)
  * [ListEvery](./ListEvery.md)
  * [ListFilter](./ListFilter.md)
  * [ListFind](./ListFind.md)
  * [ListFindNoCase](./ListFindNoCase.md)
  * [ListFirst](./ListFirst.md)
  * [ListGetAt](./ListGetAt.md)
  * [ListIndexExists](./ListIndexExists.md)
  * [ListInsertAt](./ListInsertAt.md)
  * [ListItemTrim](./ListItemTrim.md)
  * [ListLast](./ListLast.md)
  * [ListLen](./ListLen.md)
  * [ListMap](./ListMap.md)
  * [ListPrepend](./ListPrepend.md)
  * [ListQualify](./ListQualify.md)
  * [ListReduceRight](./ListReduceRight.md)
  * [ListRemoveDuplicates](./ListRemoveDuplicates.md)
  * [ListRest](./ListRest.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
