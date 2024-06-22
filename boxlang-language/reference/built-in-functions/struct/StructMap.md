[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructMap`

Used to map a struct to a new struct of the same type containing the result

## Method Signature

```
StructMap(struct=[structloose], callback=[function], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The target struct to test |  |
| `callback` | `function` | `true` | The function used to produce the right-hand value assignment in the new struct |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |

## Examples



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
  * [StructNew](./StructNew.md)
  * [StructReduce](./StructReduce.md)
  * [StructSome](./StructSome.md)
  * [StructSort](./StructSort.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
