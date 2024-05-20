[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructReduce`

Run the provided udf against struct to reduce the values to a single output

## Method Signature
```
StructReduce(struct=[structloose], callback=[function], initialValue=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The struct to reduce |  |
| `callback` | `function` | `true` | The function to invoke for each entry in the struct. The function will be passed 4 arguments: the accumulator, they entry key,<br>                    the<br>                    current index, and the original struct. The function should return the new accumulator value. |  |
| `initialValue` | `any` | `false` | The initial value of the accumulator |  |

## Examples

```
StructReduce(struct=[structloose], callback=[function], initialValue=[any])
```

## Related
  * [StructAppend](StructAppend.md)
  * [StructClear](StructClear.md)
  * [StructCopy](StructCopy.md)
  * [StructDelete](StructDelete.md)
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
  * [StructSome](StructSome.md)
  * [StructSort](StructSort.md)
  * [StructToQueryString](StructToQueryString.md)
  * [StructToSorted](StructToSorted.md)
  * [StructUpdate](StructUpdate.md)
  * [StructValueArray](StructValueArray.md)
