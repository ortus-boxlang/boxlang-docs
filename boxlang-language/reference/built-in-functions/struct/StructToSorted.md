[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructToSorted`

Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

## Method Signature

```
StructToSorted(struct=[structloose], sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The struct to sort |  |
| `sortType` | `any` | `false` | An optional sort type to apply to that type - if a callback is given in this position it will be used as that argument | `text` |
| `sortOrder` | `string` | `false` | The sort order applicable to the sortType argument | `asc` |
| `localeSensitive` | `any` | `false` |  | `false` |
| `callback` | `function` | `false` | An optional callback to use as the sorting function |  |

## Examples

```
StructToSorted(struct=[structloose], sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function])
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
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
