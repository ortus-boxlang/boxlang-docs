# StructAppend

Appends the contents of a second struct to the first struct either with or without overwrite

## Method Signature

```
StructAppend(struct1=[structloose], struct2=[structloose], overwrite=[boolean])
```

### Arguments

| Argument    | Type      | Required | Description                                                                                              | Default |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------- | ------- |
| `struct1`   | `struct`  | `true`   | <p>The target struct which will be the recipient of the<br>appending</p>                                 |         |
| `struct2`   | `struct`  | `true`   | The struct containing the values to be appended                                                          |         |
| `overwrite` | `boolean` | `false`  | <p>Default true. Whether to overwrite existing values found<br>in struct1 from the values in struct2</p> | `true`  |

## Examples

## Related

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
* [StructReduce](StructReduce.md)
* [StructSome](StructSome.md)
* [StructSort](StructSort.md)
* [StructToQueryString](StructToQueryString.md)
* [StructToSorted](StructToSorted.md)
* [StructUpdate](StructUpdate.md)
* [StructValueArray](StructValueArray.md)
