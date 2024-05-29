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

  * [StructAppend](./StructAppend.md)
  * [StructClear](./StructClear.md)
  * [StructCopy](./StructCopy.md)
  * [StructDelete](./StructDelete.md)
  * [StructEach](./StructEach.md)
  * [StructEquals](./StructEquals.md)
  * [StructEvery](./StructEvery.md)
  * [StructFilter](./StructFilter.md)
  * [StructFind](./StructFind.md)
  * [StructFindKey](./StructFindKey.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructGet](./StructGet.md)
  * [StructGetMetadata](./StructGetMetadata.md)
  * [StructInsert](./StructInsert.md)
  * [StructIsCaseSensitive](./StructIsCaseSensitive.md)
  * [StructIsOrdered](./StructIsOrdered.md)
  * [StructKeyArray](./StructKeyArray.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructMap](./StructMap.md)
  * [StructNew](./StructNew.md)
  * [StructReduce](./StructReduce.md)
  * [StructSome](./StructSome.md)
  * [StructSort](./StructSort.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructValueArray](./StructValueArray.md)
