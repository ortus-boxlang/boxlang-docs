[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructKeyTranslate`

Converts a struct with dot-notated keys in to an unflattened version

## Method Signature
```
StructKeyTranslate(struct=[structloose], deep=[boolean], retainKeys=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The struct to unflatten |  |
| `deep` | `boolean` | `false` | Whether to recurse in to nested keys - default false | `false` |
| `retainKeys` | `boolean` | `false` | Whether to retain the original dot-notated keys - default false | `false` |

## Examples

```
StructKeyTranslate(struct=[structloose], deep=[boolean], retainKeys=[boolean])
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
  * [StructMap](boxlang-language/reference/built-in-functions/StructMap.md)
  * [StructNew](boxlang-language/reference/built-in-functions/StructNew.md)
  * [StructReduce](boxlang-language/reference/built-in-functions/StructReduce.md)
  * [StructSome](boxlang-language/reference/built-in-functions/StructSome.md)
  * [StructSort](boxlang-language/reference/built-in-functions/StructSort.md)
  * [StructToQueryString](boxlang-language/reference/built-in-functions/StructToQueryString.md)
  * [StructToSorted](boxlang-language/reference/built-in-functions/StructToSorted.md)
  * [StructUpdate](boxlang-language/reference/built-in-functions/StructUpdate.md)
  * [StructValueArray](boxlang-language/reference/built-in-functions/StructValueArray.md)
