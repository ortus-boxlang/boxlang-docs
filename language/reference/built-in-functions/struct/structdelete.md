[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructDelete`

Deletes a key from a struct

## Method Signature
```
StructDelete(struct=[modifiableStruct], key=[string], indicateNotExists=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `modifiableStruct` | `true` | The struct target |  |
| `key` | `string` | `true` | The key to delete |  |
| `indicateNotExists` | `boolean` | `false` |  | `false` |

## Examples

```
StructDelete(struct=[modifiableStruct], key=[string], indicateNotExists=[boolean])
```

## Related
  * [StructAppend](StructAppend.md)
  * [StructClear](StructClear.md)
  * [StructCopy](StructCopy.md)
  * [StructEach](StructEach.md)
  * [StructEquals](StructEquals.md)
  * [StructEvery](StructEvery.md)
  * [StructFilter](StructFilter.md)
  * [StructFind](StructFind.md)
  * [StructFindKey](StructFindKey.md)
  * [StructFindValue](StructFindValue.md)
  * [StructGet](StructGet.md)
  * [StructGetMetadata](StructGetMetadata.md)
  * [StructInsert](StructInsert.md)
  * [StructIsCaseSensitive](StructIsCaseSensitive.md)
  * [StructIsOrdered](StructIsOrdered.md)
  * [StructKeyArray](StructKeyArray.md)
  * [StructKeyExists](StructKeyExists.md)
  * [StructKeyList](StructKeyList.md)
  * [StructKeyTranslate](StructKeyTranslate.md)
  * [StructMap](StructMap.md)
  * [StructNew](StructNew.md)
  * [StructReduce](StructReduce.md)
  * [StructSome](StructSome.md)
  * [StructSort](StructSort.md)
  * [StructToQueryString](StructToQueryString.md)
  * [StructToSorted](StructToSorted.md)
  * [StructUpdate](StructUpdate.md)
  * [StructValueArray](StructValueArray.md)
