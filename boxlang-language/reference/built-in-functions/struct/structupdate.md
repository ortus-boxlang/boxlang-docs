[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructUpdate`

Updates or sets a key/value pair in to a struct

## Method Signature
```
StructUpdate(struct=[modifiableStruct], key=[string], value=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `modifiableStruct` | `true` | The target struct |  |
| `key` | `string` | `true` | The struct key |  |
| `value` | `any` | `true` | The value to assign for the specified key |  |

## Examples

```
StructUpdate(struct=[modifiableStruct], key=[string], value=[any])
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
  * [StructToSorted](boxlang-language/reference/built-in-functions/StructToSorted.md)
  * [StructValueArray](boxlang-language/reference/built-in-functions/StructValueArray.md)
