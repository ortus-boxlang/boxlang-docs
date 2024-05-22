[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructToSorted`

Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

## Method Signature
```
StructToSorted(struct=[structloose], sortType=[any], sortOrder=[string], path=[string], callback=[function])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The struct to sort |  |
| `sortType` | `any` | `false` | An optional sort type to apply to that type - if a callback is given in this position it will be used as that argument | `text` |
| `sortOrder` | `string` | `false` | The sort order applicable to the sortType argument | `asc` |
| `path` | `string` | `false` |  |  |
| `callback` | `function` | `false` | An optional callback to use as the sorting function |  |

## Examples

```
StructToSorted(struct=[structloose], sortType=[any], sortOrder=[string], path=[string], callback=[function])
```

## Related
  * [StructAppend](boxlang-language/reference/built-in-functions/StructAppend.md)
  * [StructClear](boxlang-language/reference/built-in-functions/StructClear.md)
  * [StructCopy](boxlang-language/reference/built-in-functions/StructCopy.md)
  * [StructDelete](boxlang-language/reference/built-in-functions/StructDelete.md)
  * [StructEach](boxlang-language/reference/built-in-functions/StructEach.md)
  * [StructEquals](boxlang-language/reference/built-in-functions/StructEquals.md)
  * [StructEvery](boxlang-language/reference/built-in-functions/StructEvery.md)
  * [StructFilter](boxlang-language/reference/built-in-functions/StructFilter.md)
  * [StructFind](boxlang-language/reference/built-in-functions/StructFind.md)
  * [StructFindKey](boxlang-language/reference/built-in-functions/StructFindKey.md)
  * [StructFindValue](boxlang-language/reference/built-in-functions/StructFindValue.md)
  * [StructGet](boxlang-language/reference/built-in-functions/StructGet.md)
  * [StructGetMetadata](boxlang-language/reference/built-in-functions/StructGetMetadata.md)
  * [StructInsert](boxlang-language/reference/built-in-functions/StructInsert.md)
  * [StructIsCaseSensitive](boxlang-language/reference/built-in-functions/StructIsCaseSensitive.md)
  * [StructIsOrdered](boxlang-language/reference/built-in-functions/StructIsOrdered.md)
  * [StructKeyArray](boxlang-language/reference/built-in-functions/StructKeyArray.md)
  * [StructKeyExists](boxlang-language/reference/built-in-functions/StructKeyExists.md)
  * [StructKeyList](boxlang-language/reference/built-in-functions/StructKeyList.md)
  * [StructKeyTranslate](boxlang-language/reference/built-in-functions/StructKeyTranslate.md)
  * [StructMap](boxlang-language/reference/built-in-functions/StructMap.md)
  * [StructNew](boxlang-language/reference/built-in-functions/StructNew.md)
  * [StructReduce](boxlang-language/reference/built-in-functions/StructReduce.md)
  * [StructSome](boxlang-language/reference/built-in-functions/StructSome.md)
  * [StructSort](boxlang-language/reference/built-in-functions/StructSort.md)
  * [StructToQueryString](boxlang-language/reference/built-in-functions/StructToQueryString.md)
  * [StructUpdate](boxlang-language/reference/built-in-functions/StructUpdate.md)
  * [StructValueArray](boxlang-language/reference/built-in-functions/StructValueArray.md)
