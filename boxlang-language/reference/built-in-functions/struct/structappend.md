[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructAppend`

Appends the contents of a second struct to the first struct either with or without overwrite

## Method Signature
```
StructAppend(struct1=[structloose], struct2=[structloose], overwrite=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct1` | `structloose` | `true` | The target struct which will be the recipient of the appending |  |
| `struct2` | `structloose` | `true` | The struct containing the values to be appended |  |
| `overwrite` | `boolean` | `false` | Default true. Whether to overwrite existing values found in struct1 from the values in struct2 | `true` |

## Examples

```
StructAppend(struct1=[structloose], struct2=[structloose], overwrite=[boolean])
```

## Related
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
  * [StructToSorted](boxlang-language/reference/built-in-functions/StructToSorted.md)
  * [StructUpdate](boxlang-language/reference/built-in-functions/StructUpdate.md)
  * [StructValueArray](boxlang-language/reference/built-in-functions/StructValueArray.md)
